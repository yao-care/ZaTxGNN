---
layout: default
title: Terbinafine
parent: Model Prediction Only (L5)
nav_order: 442
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Terbinafine: predicted new indication Creeping myiasis (evidence level L5). Approved use: Tinea pedis, tinea corporis, tinea infection, tinea unguium…"
monitor_inn: "Terbinafine"
predicted_indications: ["creeping myiasis", "furuncular myiasis", "wound myiasis", "myiasis", "cutaneous candidiasis", "toxoplasmosis", "blastomycosis", "tinea manuum", "echinococcus granulosus infectious disease", "superficial mycosis"]
---

# Terbinafine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Terbinafine: From Tinea Infections to Creeping Myiasis

## One-Sentence Summary

Terbinafine is an antifungal medicine originally used for superficial fungal skin and nail infections such as tinea pedis, tinea corporis, tinea unguium and pityriasis versicolor.
The TxGNN model's top-ranked prediction is **creeping myiasis** (a fly-larva skin infestation), but there are **0 clinical trials** and **0 publications** supporting it. The prediction rests on graph proximity alone.
Of the ten predictions reviewed, the credible ones are those close to terbinafine's existing antifungal use (**tinea manuum** and **superficial mycosis**). The top-ranked myiasis predictions are not credible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, tinea corporis, tinea infection, tinea unguium, pityriasis versicolor, dermatophytosis of groin and perianal area (the SAHPRA registrations in the data compiled for this report carry no indication text, so these come from the TxGNN knowledge graph) |
| Predicted New Indication | Creeping myiasis (rank 1) |
| TxGNN Prediction Score | 96.74% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 |
| Recommended Decision | Hold |

**Note on the other predictions:** Several predictions score lower than creeping myiasis but have far better support. The most actionable are:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 8 | Tinea manuum | 90.11% | L4 | Proceed with Guardrails |
| 10 | Superficial mycosis | 84.47% | L4 | Proceed with Guardrails |
| 5 | Cutaneous candidiasis | 95.04% | L4 | Research Question |
| 7 | Blastomycosis | 91.76% | L4 | Research Question |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. From general pharmacology, terbinafine is an allylamine antifungal. It inhibits fungal squalene epoxidase, which depletes ergosterol and lets squalene accumulate. This is fungicidal against dermatophytes.

**Creeping myiasis and other myiasis predictions (ranks 1-4):** These are not mechanistically plausible. Myiasis is an infestation by fly larvae, and squalene epoxidase inhibition is not an established way to kill them. Standard management is larval removal, sometimes with ivermectin. The only linked paper (PMID 25016125) is a case report in which a furuncle did not respond to several treatments, including terbinafine, and was finally diagnosed as myiasis. It does not show terbinafine working. The other linked paper (PMID 39081689) describes a kidney transplant recipient with chromoblastomycosis and myiasis, where terbinafine was likely aimed at the fungal infection. The high scores most likely reflect co-mention and graph proximity, not real efficacy.

**Tinea manuum and superficial mycosis (ranks 8 and 10):** These are the sensible predictions. They are essentially extensions of terbinafine's established use. Tinea manuum (fungal infection of the hands) is closely related to the existing indications of tinea pedis and tinea corporis, and caused by the same dermatophytes. Superficial mycosis largely overlaps with the existing labelled indications, so it is not a true repurposing.

**Cutaneous candidiasis and blastomycosis (ranks 5 and 7):** These are plausible but unproven. Terbinafine is only variably active against *Candida* and is often fungistatic there, and azoles remain standard of care. For blastomycosis, itraconazole and amphotericin B are standard, and the supporting evidence is a single case report of a related infection (paracoccidioidomycosis).

**Other predictions:** Toxoplasmosis (rank 6) and *Echinococcus granulosus* infection (rank 9) have no supporting evidence or mechanistic rationale. The papers linked to toxoplasmosis concern antifungal formulations and dermatophyte typing, not *Toxoplasma*.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the ten predicted indications, including the top-ranked creeping myiasis. No SANCTR or PACTR identifiers were found in the data compiled for this report.

---

## Literature Evidence

**Creeping myiasis (rank 1):** Currently no related literature available.

The most relevant publications across the stronger predictions are listed below. They are mostly reviews and case reports, with few controlled studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1911319](https://pubmed.ncbi.nlm.nih.gov/1911319/) | 1991 | Clinical study (placebo-controlled) | Br J Dermatol | Two weeks of oral terbinafine 250 mg daily versus placebo in moccasin tinea pedis and tinea manuum (53 adults, 28 evaluable) |
| [15679673](https://pubmed.ncbi.nlm.nih.gov/15679673/) | 2005 | Case report | Mycoses | Tinea manuum bullosa (*T. verrucosum*) cured clinically and mycologically with terbinafine 250 mg daily |
| [10940119](https://pubmed.ncbi.nlm.nih.gov/10940119/) | 2000 | Comparative study | Int J Dermatol | Tinea manus treated with 1-week itraconazole versus terbinafine (no abstract available) |
| [39567411](https://pubmed.ncbi.nlm.nih.gov/39567411/) | 2024 | Review | Mycopathologia | Update on dermatophyte epidemiology and treatment, noting rising terbinafine-resistant *T. indotineae* |
| [1372222](https://pubmed.ncbi.nlm.nih.gov/1372222/) | 1992 | Review | Drugs | Terbinafine pharmacology and efficacy in superficial mycoses; about 90% mycological and 80% overall efficacy in tinea corporis/cruris and tinea pedis |
| [10439936](https://pubmed.ncbi.nlm.nih.gov/10439936/) | 1999 | Review | Drugs | Oral terbinafine 250 mg/day gives mycological cure in over 80% of superficial dermatophyte infections |
| [9593126](https://pubmed.ncbi.nlm.nih.gov/9593126/) | 1998 | In vitro study | Antimicrob Agents Chemother | Terbinafine activity against 350 cutaneous *Candida* isolates and other yeasts |
| [10886159](https://pubmed.ncbi.nlm.nih.gov/10886159/) | 2000 | Case report | Br J Dermatol | Paracoccidioidomycosis resolved with terbinafine after co-trimoxazole failed |
| [40024788](https://pubmed.ncbi.nlm.nih.gov/40024788/) | 2025 | Surveillance study | Med Mycol J | Terbinafine-resistant dermatophytes isolated in Japan |
| [38623728](https://pubmed.ncbi.nlm.nih.gov/38623728/) | 2024 | Review | Expert Opin Pharmacother | Rising antifungal resistance in dermatophytosis |

PMID 10417874 is a randomised trial of ajoene (a garlic-derived compound) with terbinafine as the comparator. It is not evidence for a new terbinafine indication.

---

## South Africa Market Information

All five SAHPRA registrations are valid single-ingredient products. The registration records in the data compiled for this report contain no approved-indication text or manufacturer. Essential Medicines List status could not be confirmed from the data.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A40/20.2.2/0344 | Dermax 250 | Tablet (oral) | Not recorded in the data |
| 38/20.2.2/0148 | Terbicil | Cream (topical) | Not recorded in the data |
| 32/20.2.2/0564 | Lamisil derm gel | Gel (topical) | Not recorded in the data |
| Z/20.2.2/186 | Lamisil | Cream (topical) | Not recorded in the data |
| 42/20.2.2/0382 | Almatil | Cream (topical) | Not recorded in the data |

Only one oral product (a tablet) is registered. The other four are topical. This matters because systemic infections would need the oral form.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (these come from the TxGNN knowledge graph, not from the product label, and should be verified against the Professional Information):
- Kidney disease
- Liver disease
- Gallbladder disease
- Pyoureter
- Systemic lupus erythematosus (including paediatric)
- Substance abuse/dependence

**Drug interactions:** The interaction query returned 100 interactions in total; only the first 20 are available here. The most clinically relevant listed:
- **Major:** Eliglustat
- **Moderate:** Morphine, Naltrexone, Ondansetron, Dexfenfluramine, Fenfluramine
- **Minor:** Cimetidine
- **Severity unrated:** Phentermine, pantoprazole, glimepiride, doxycycline, clotrimazole, metformin, omeprazole, lansoprazole, prednisone, hydrocortisone, potassium chloride, loperamide, rosiglitazone

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications, which were not available in the data compiled for this report. Report adverse drug reactions to SAHPRA.

**Resistance:** Terbinafine-resistant dermatophytes, notably *Trichophyton indotineae* and squalene epoxidase mutants, are increasingly reported. Susceptibility testing and antifungal stewardship are advisable for non-responding infections.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, creeping myiasis)

**Rationale:**
- The creeping myiasis prediction (and the related furuncular myiasis, wound myiasis and myiasis predictions) has no trials, no supporting literature and no plausible mechanism. The score reflects graph proximity only. Established treatment is larval removal or ivermectin.
- **Tinea manuum** and **superficial mycosis** are suitable for **Proceed with Guardrails**. They sit next to terbinafine's existing indications, though the evidence is mostly reviews and older studies, which keeps the level at L4. Resistance is the main guardrail.
- Cutaneous candidiasis and blastomycosis are research questions only. Toxoplasmosis and echinococcosis should be held.

**To proceed, the following is needed:**
- SAHPRA Professional Information (PI) warnings, contraindications and approved indications, which are missing and block formal safety screening
- Mechanism of action data (for example from DrugBank)
- For tinea manuum: confirmation that the registered oral and topical products' approved indications already cover it, and local dermatophyte susceptibility data for South Africa
- For any hepatic, renal or lupus-related use: a review of the knowledge-graph contraindication signals against the PI
- A full review of the remaining interaction list beyond the 20 shown, particularly for eliglustat
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

