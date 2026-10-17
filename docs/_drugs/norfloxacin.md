---
layout: default
title: Norfloxacin
parent: Model Prediction Only (L5)
nav_order: 349
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Norfloxacin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Urinary tract infection, typhoid fever, salmonellosis…"
monitor_inn: "Norfloxacin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "diffuse scleroderma", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Norfloxacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Norfloxacin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Norfloxacin is a fluoroquinolone antibiotic, originally used for infections such as urinary tract infection, typhoid fever, dysentery and bacterial pneumonia.
The TxGNN model predicts it may be effective for **hyperamylasemia**, but there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, typhoid fever, salmonellosis, bacterial pneumonia and other bacterial infections (the SAHPRA registrations in the compiled data carry no indication text, so these come from the knowledge graph) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the compiled data. Norfloxacin is a fluoroquinolone antibiotic that inhibits bacterial DNA gyrase and topoisomerase IV, and its efficacy against bacterial infections is established.

The review found no identifiable mechanistic link to hyperamylasemia. Norfloxacin has no known action on amylase regulation or pancreatic physiology. The high TxGNN score appears to be a graph-based prediction artefact without biological support, and this prediction should not be treated as a credible new indication.

Other predictions for this drug (ranks 2-10) were also reviewed. Most are likewise computational only and lack biological plausibility, for example polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility, diffuse scleroderma and monoclonal gammopathy. Norfloxacin and other fluoroquinolones are associated with peripheral neuropathy as an adverse effect, which argues against use in hematological disease associated with acquired peripheral neuropathy.

The only prediction with a plausible rationale is **septicemic plague** (rank 10, score 99.37%), which is an extension of the existing antibacterial use rather than true repurposing. Fluoroquinolones are active against *Yersinia pestis*, but the available evidence is preclinical and concerns the drug class rather than norfloxacin specifically. Better-characterised agents (streptomycin, gentamicin, doxycycline, ciprofloxacin, levofloxacin) are preferred.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for hyperamylasemia.

---

## Literature Evidence

Currently no related literature available for hyperamylasemia.

For context, the literature retrieved for other predictions is limited and does not support norfloxacin efficacy in those conditions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10987101](https://pubmed.ncbi.nlm.nih.gov/10987101/) | 2000 | Preclinical (animal) | Antibiotiki i khimioterapiia | Mouse study of combined fluoroquinolone and vaccine prophylaxis for plague. Norfloxacin had less effect on post-vaccine immunity than ciprofloxacin, ofloxacin and pefloxacin (septicemic plague) |
| [8834911](https://pubmed.ncbi.nlm.nih.gov/8834911/) | 1996 | Cohort/Observational | Antimicrob Agents Chemother | Fluoroquinolone-resistant *E. coli* emerged in the faecal flora of 10 of 25 haematology patients on norfloxacin prophylaxis (monoclonal gammopathy; shows resistance, not therapeutic benefit) |
| [22959880](https://pubmed.ncbi.nlm.nih.gov/22959880/) | 2012 | Case series | Am J Ophthalmol | Repeated corneal swabbing for microsporidial keratoconjunctivitis. No norfloxacin efficacy shown |
| [12867402](https://pubmed.ncbi.nlm.nih.gov/12867402/) | 2003 | Case series | Ophthalmology | Six cases of microsporidial keratoconjunctivitis in healthy individuals. No norfloxacin efficacy shown |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 43/20.1.1/0657 | Utifloxa | Tablet | Not available in the compiled data |
| Reg. No. 32/20.1.1/0377 | Floxin | Tablet | Not available in the compiled data |

Both registrations are valid single-ingredient oral products. Essential Medicines List (EML) status was not available in the compiled data.

---

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these come from graph relationships, not from label text):
- Cardiac: long QT syndrome (including familial), torsades de pointes
- Hepatic and renal: liver failure, liver disease, cirrhosis, kidney disease, gallbladder disease
- Neurological and psychiatric: epilepsy, peripheral neuropathy, peripheral nervous system disease, anxiety disorder, psychotic disorders, mental disorder
- Musculoskeletal: tendinitis, rhabdomyolysis
- Metabolic: diabetes mellitus, diabetic ketoacidosis, potassium deficiency
- Haematological: thrombocytopenia, anaemia

**Drug Interactions** (100 interactions recorded; the main ones in the data are listed):
- **Major:** hydrocortisone, dexamethasone, betamethasone, triamcinolone (corticosteroids), bupropion, chlorpropamide
- **Moderate:** antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, canagliflozin, albiglutide), famotidine, loperamide, acetylsalicylic acid, balsalazide, bisacodyl, calcium and potassium salts

Please refer to the SAHPRA-approved Professional Information (PI) for official warnings and contraindications, and report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for hyperamylasemia has no clinical trials, no literature and no plausible mechanism, so it is a model output only (L5). Norfloxacin also carries a notable safety profile (QT prolongation, tendon, neurological and glucose-related effects, and many interactions), so there is no basis to pursue this indication.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking norfloxacin to amylase regulation or pancreatic physiology
- Supporting preclinical or clinical studies
- Mechanism of action data and the SAHPRA package insert warnings and contraindications, to complete safety screening
- If any fluoroquinolone-based indication is pursued, the septicemic plague question would only be worth studying as an antibacterial extension, and would need comparison against established agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

