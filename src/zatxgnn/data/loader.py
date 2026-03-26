#!/usr/bin/env python3
"""South Africa MPR (Medicine Price Registry) drug data loader.

This module loads drug data from the South Africa Medicine Price Registry.
Data is obtained via API from https://medicineprices.org.za/

Data source: SAHPRA registered medicines with Single Exit Prices
"""

import json
import re
from pathlib import Path
from typing import Optional

import pandas as pd


def load_mpr_data(filepath: Path) -> pd.DataFrame:
    """Load MPR JSON data file.

    Args:
        filepath: Path to mpr_medicines.json

    Returns:
        DataFrame with MPR data
    """
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Extract ingredients from the ingredients array
    for med in data:
        ingredients = med.get("ingredients", [])
        if ingredients:
            # Join all ingredient names
            ing_names = [ing.get("name", "") for ing in ingredients if ing.get("name")]
            med["ingredient_names"] = "; ".join(ing_names)
        else:
            med["ingredient_names"] = ""

    df = pd.DataFrame(data)
    return df


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize column names for consistency.

    MPR data has these fields:
    - id: unique identifier
    - nappi_code: NAPPI code
    - name: medicine name
    - dosage_form: tablet, capsule, etc.
    - sep: Single Exit Price
    - number_of_generics: generic alternatives count
    """
    column_map = {
        "id": "MPR_ID",
        "nappi_code": "NAPPI_Code",
        "name": "Product_Name",
        "dosage_form": "Dosage_Form",
        "sep": "SEP_Price",
        "number_of_generics": "Generic_Count",
    }

    df = df.rename(columns=column_map)
    return df


def extract_ingredient(name: str) -> str:
    """Extract active ingredient from medicine name.

    MPR names are like "Paracetamol Clicks (500mg tablet)"
    We extract the first word(s) before parentheses or dosage.
    """
    if pd.isna(name):
        return ""

    name = str(name)

    # Remove content in parentheses
    name = re.sub(r"\s*\([^)]*\)", "", name)

    # Remove dosage patterns like "500mg", "10ml", etc.
    name = re.sub(r"\s+\d+\s*(mg|ml|mcg|g|iu|%)\b", "", name, flags=re.IGNORECASE)

    # Remove brand suffixes
    name = re.sub(r"\s+(tablet|capsule|injection|syrup|cream|ointment|solution).*$", "", name, flags=re.IGNORECASE)

    # Clean up
    name = name.strip()

    # Take first part if there's a dash or comma (often separates brand/generic)
    if " - " in name:
        name = name.split(" - ")[0].strip()

    return name


def load_fda_drugs(filepath: Optional[Path] = None) -> pd.DataFrame:
    """Load and process MPR drug data.

    This is the main entry point, compatible with the standard TxGNN interface.

    Args:
        filepath: Optional path to MPR data file. If not provided,
                  looks for data in standard locations.

    Returns:
        DataFrame with columns:
            - NAPPI_Code: NAPPI identification number
            - Product_Name: Drug product name
            - Active_Ingredients: Active ingredients
    """
    base_dir = Path(__file__).parent.parent.parent.parent
    data_dir = base_dir / "data"
    raw_dir = data_dir / "raw"

    # Try to find MPR data file
    if filepath is None:
        possible_files = [
            raw_dir / "mpr_medicines.json",
            raw_dir / "mpr_dump.json",
            data_dir / "mpr_medicines.json",
        ]

        for f in possible_files:
            if f.exists():
                filepath = f
                break

    if filepath is None or not filepath.exists():
        print("Warning: No MPR data found.")
        print("Please run: python scripts/download_mpr_data.py")
        print("Expected file: data/raw/mpr_medicines.json")
        return pd.DataFrame(columns=["NAPPI_Code", "Product_Name", "Active_Ingredients"])

    print(f"Loading MPR data from: {filepath}")

    # Load and process
    df = load_mpr_data(filepath)
    df = normalize_columns(df)

    # Use ingredient_names from the API if available, otherwise extract from product name
    if "ingredient_names" in df.columns:
        df["Active_Ingredients"] = df["ingredient_names"].fillna("")
        # Filter out empty ingredients and use extract_ingredient as fallback
        mask = df["Active_Ingredients"] == ""
        df.loc[mask, "Active_Ingredients"] = df.loc[mask, "Product_Name"].apply(extract_ingredient)
    else:
        # Fallback: extract from medicine names
        df["Active_Ingredients"] = df["Product_Name"].apply(extract_ingredient)

    # Also add to 'ingredients' column for compatibility
    df["ingredients"] = df["Active_Ingredients"]
    df["brand_name"] = df["Product_Name"]

    # Ensure required columns exist
    required_cols = ["NAPPI_Code", "Product_Name", "Active_Ingredients"]
    for col in required_cols:
        if col not in df.columns:
            df[col] = ""

    # Remove duplicates by ingredient
    df = df[df["Active_Ingredients"].notna() & (df["Active_Ingredients"] != "")]
    df = df.drop_duplicates(subset=["Active_Ingredients"]).reset_index(drop=True)

    print(f"  Total medicines: {len(df)}")
    print(f"  Unique ingredients: {df['Active_Ingredients'].nunique()}")

    return df


def filter_active_drugs(df: pd.DataFrame) -> pd.DataFrame:
    """Filter active drugs with valid ingredients.

    Args:
        df: Drug DataFrame

    Returns:
        Filtered DataFrame
    """
    col = "Active_Ingredients" if "Active_Ingredients" in df.columns else "ingredients"
    active = df[df[col].notna() & (df[col] != "")].copy()
    active = active.reset_index(drop=True)
    return active


def get_drug_summary(df: pd.DataFrame) -> dict:
    """Get drug data summary statistics.

    Args:
        df: Drug DataFrame

    Returns:
        Summary statistics dictionary
    """
    all_ingredients = set()
    ing_col = "Active_Ingredients" if "Active_Ingredients" in df.columns else "ingredients"
    name_col = "Product_Name" if "Product_Name" in df.columns else "brand_name"

    for ing_str in df[ing_col].dropna():
        # MPR ingredients are typically single per entry
        all_ingredients.add(str(ing_str).strip())

    return {
        "total_count": len(df),
        "with_ingredient": df[ing_col].notna().sum(),
        "unique_products": df[name_col].nunique() if name_col in df.columns else 0,
        "unique_ingredients": len(all_ingredients),
    }


def get_unique_ingredients(df: pd.DataFrame) -> list[str]:
    """Extract unique ingredients from loaded data."""
    all_ingredients = []

    col = "Active_Ingredients" if "Active_Ingredients" in df.columns else "ingredients"
    for ing_str in df[col].dropna():
        all_ingredients.append(str(ing_str).strip())

    return sorted(set(all_ingredients))


if __name__ == "__main__":
    # Test loading
    df = load_fda_drugs()
    print(f"\nLoaded {len(df)} drugs")

    if len(df) > 0:
        ingredients = get_unique_ingredients(df)
        print(f"Unique ingredients: {len(ingredients)}")
        print(f"\nSample ingredients: {ingredients[:10]}")
