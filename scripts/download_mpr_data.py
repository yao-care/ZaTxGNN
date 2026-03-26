#!/usr/bin/env python3
"""Download South Africa Medicine Price Registry data.

Uses the full search API to get ingredient information.
"""

import json
import requests
from pathlib import Path
import time

# Common drug names to search for comprehensive coverage
COMMON_DRUGS = [
    # Pain/Anti-inflammatory
    "paracetamol", "aspirin", "ibuprofen", "diclofenac", "naproxen", "celecoxib",
    "tramadol", "codeine", "morphine", "fentanyl", "oxycodone",
    # Cardiovascular
    "amlodipine", "atenolol", "metoprolol", "propranolol", "bisoprolol",
    "lisinopril", "enalapril", "ramipril", "perindopril", "captopril",
    "losartan", "valsartan", "irbesartan", "telmisartan", "candesartan",
    "hydrochlorothiazide", "furosemide", "spironolactone", "indapamide",
    "simvastatin", "atorvastatin", "rosuvastatin", "pravastatin", "ezetimibe",
    "warfarin", "clopidogrel", "rivaroxaban", "apixaban", "dabigatran",
    "digoxin", "amiodarone", "diltiazem", "verapamil", "nifedipine",
    # Diabetes
    "metformin", "glimepiride", "gliclazide", "glibenclamide", "pioglitazone",
    "sitagliptin", "empagliflozin", "dapagliflozin", "liraglutide", "insulin",
    # GI
    "omeprazole", "esomeprazole", "pantoprazole", "lansoprazole", "rabeprazole",
    "ranitidine", "famotidine", "domperidone", "metoclopramide", "ondansetron",
    "loperamide", "lactulose", "bisacodyl", "senna",
    # Respiratory
    "salbutamol", "ipratropium", "tiotropium", "fluticasone", "budesonide",
    "montelukast", "theophylline", "prednisolone", "dexamethasone",
    # CNS/Psychiatric
    "sertraline", "fluoxetine", "paroxetine", "citalopram", "escitalopram",
    "venlafaxine", "duloxetine", "mirtazapine", "amitriptyline", "trazodone",
    "diazepam", "lorazepam", "alprazolam", "clonazepam", "zolpidem",
    "haloperidol", "risperidone", "olanzapine", "quetiapine", "aripiprazole",
    "carbamazepine", "valproate", "phenytoin", "levetiracetam", "lamotrigine",
    "levodopa", "carbidopa", "pramipexole", "ropinirole",
    # Antibiotics
    "amoxicillin", "ampicillin", "penicillin", "flucloxacillin", "cloxacillin",
    "cephalexin", "cefuroxime", "ceftriaxone", "cefixime", "cefpodoxime",
    "azithromycin", "clarithromycin", "erythromycin", "roxithromycin",
    "ciprofloxacin", "levofloxacin", "moxifloxacin", "norfloxacin", "ofloxacin",
    "doxycycline", "tetracycline", "minocycline",
    "metronidazole", "clindamycin", "vancomycin", "linezolid",
    "trimethoprim", "sulfamethoxazole", "nitrofurantoin",
    # Antifungals
    "fluconazole", "itraconazole", "ketoconazole", "clotrimazole", "miconazole",
    "nystatin", "terbinafine", "griseofulvin",
    # Antivirals
    "acyclovir", "valacyclovir", "famciclovir", "oseltamivir",
    "tenofovir", "lamivudine", "efavirenz", "dolutegravir", "ritonavir",
    # Antiparasitics
    "albendazole", "mebendazole", "praziquantel", "ivermectin",
    "chloroquine", "artemether", "lumefantrine", "mefloquine",
    # Hormones/Steroids
    "levothyroxine", "propylthiouracil", "carbimazole",
    "prednisone", "hydrocortisone", "betamethasone", "triamcinolone",
    "testosterone", "estradiol", "progesterone", "norethisterone",
    "ethinylestradiol", "levonorgestrel", "medroxyprogesterone",
    # Vitamins/Supplements
    "folic acid", "vitamin", "calcium", "iron", "zinc", "magnesium",
    # Eye/Ear
    "timolol", "latanoprost", "brimonidine", "dorzolamide", "travoprost",
    "chloramphenicol", "gentamicin",
    # Skin
    "clobetasol", "mometasone",
    "tretinoin", "adapalene", "benzoyl",
    # Other
    "allopurinol", "colchicine", "febuxostat",
    "sildenafil", "tadalafil",
    "finasteride", "tamsulosin", "alfuzosin",
    "cyclosporine", "tacrolimus", "mycophenolate", "azathioprine",
]


def download_all_medicines():
    """Download all medicines from MPR API using full search endpoint."""
    # Use /api/v2/search which includes ingredients
    base_url = "https://medicineprices.org.za/api/v2/search"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; ZaTxGNN/1.0)"}

    all_medicines = []
    seen_ids = set()

    for drug in COMMON_DRUGS:
        print(f"Fetching '{drug}'...")
        try:
            resp = requests.get(f"{base_url}?q={drug}", headers=headers, timeout=30)
            if resp.status_code == 200:
                medicines = resp.json()
                new_count = 0
                for med in medicines:
                    if med["id"] not in seen_ids:
                        seen_ids.add(med["id"])
                        all_medicines.append(med)
                        new_count += 1
                if new_count > 0:
                    print(f"  +{new_count} new (total: {len(all_medicines)})")
            time.sleep(0.3)  # Rate limiting
        except Exception as e:
            print(f"  Error: {e}")

    # Save to file
    output_path = Path(__file__).parent.parent / "data" / "raw" / "mpr_medicines.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_medicines, f, indent=2, ensure_ascii=False)

    print(f"\nTotal unique medicines: {len(all_medicines)}")
    print(f"Saved to: {output_path}")

    # Print ingredient stats
    with_ingredients = sum(1 for m in all_medicines if m.get("ingredients"))
    print(f"With ingredients: {with_ingredients}")

    return all_medicines


if __name__ == "__main__":
    download_all_medicines()
