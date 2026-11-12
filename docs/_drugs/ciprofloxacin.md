---
layout: default
title: Ciprofloxacin
parent: Model Prediction Only (L5)
nav_order: 124
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
monitor_inn: "Ciprofloxacin"
predicted_indications: ["diffuse scleroderma", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "punctate epithelial keratoconjunctivitis", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy"]
description: "Ciprofloxacin: predicted new indication Diffuse scleroderma (evidence level L5). Approved use: Not recorded in the local data"
---

# Ciprofloxacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Ciprofloxacin: Diffuse scleroderma
{: .text-alpha }

## One-Sentence Summary

Ciprofloxacin is a fluoroquinolone antibiotic, originally used for bacterial infections such as typhoid fever, salmonellosis, bacterial pneumonia and shigellosis.
The TxGNN model predicts it may be useful for **diffuse scleroderma**, but there are **0 registered clinical trials** and only **2 publications**, both indirect or exploratory.
This is a model-driven hypothesis with limited supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 0.9987 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 76 of 107; 4 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 107 (valid: 76, of which 4 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ciprofloxacin is a well-established antibacterial agent, and its efficacy in bacterial infections is proven. Its link to scleroderma is indirect.

Two lines of reasoning are available in the literature:

1. **Possible antifibrotic effect on skin.** Scleroderma is an autoimmune connective tissue disorder marked by microvascular injury and excessive skin fibrosis. A 2010 study investigated whether oral ciprofloxacin could reduce skin fibrosis. The proposed mechanism is an effect on collagen synthesis and fibroblast activity, but this has not been confirmed.
2. **Treating a complication, not the disease.** Ciprofloxacin may treat small bowel bacterial overgrowth in systemic sclerosis, which causes chronic diarrhoea and weight loss. This addresses a gastrointestinal complication rather than the underlying scleroderma.

The evidence is therefore indirect, and the high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or demonstrated clinical benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Exploratory antifibrotic skin study (abstract describes a double-blind randomized controlled design) | The Journal of Dermatology | Tested whether oral ciprofloxacin reduces scleroderma severity and skin fibrosis. The results are not included in the data compiled for this report. |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Diagnostic/cohort study | British Journal of Rheumatology | 24 systemic sclerosis patients with malabsorption symptoms were assessed for small bowel bacterial overgrowth. This addresses a GI complication, not the disease itself. |

---

## South Africa Market Information

Approved indication text and Essential Medicines List status are not available in the data compiled for this report.

<!-- review:begin za-lic-20261105-ciprofloxacin-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Ciprofloxacin has 8 valid single-ingredient SAHPRA registrations and no cancelled ones. The five below are shown; the other three are Biofloxx 500, Ciploxx 250 and Xindex. Approved indication text and Essential Medicines List status are not available in the data compiled for this report." Removed: it said the registrations were cancelled, not registered, or not valid, which did not match the SAHPRA registration data as of 2026-11-05. The SAHPRA data list 107 registrations for this drug, 76 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-ciprofloxacin-1 -->

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 32/20.1.1/0118 | Ciprofloxacin 250 pharma-q | tablet | Valid |
| 32/20.1.1/0119 | Ciprofloxacin 500 pharma-q | tablet | Valid |
| 33/20.1.1/0365 | Cifran 250 | tablet | Valid |
| 33/20.1.1/0366 | Cifran 500 | tablet | Valid |
| 33/20.1.1/0371 | Simayla ciprofloxacin | tablet | Valid |

Showing 5 of 107 registrations (valid registrations first).

<!-- licenses:end -->

Oral and injectable forms are available locally. For scleroderma, the oral route is the one studied in the available literature.

---

## Safety Considerations

Label-based warnings and contraindications were not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Contraindication-related conditions (from a knowledge graph, not label text):**
- Cardiac: long QT syndrome (including familial), torsades de pointes
- Neurological and neuromuscular: epilepsy, peripheral neuropathy and other peripheral nervous system disease, myasthenia gravis (including adult-onset) and neuromuscular junction disease
- Musculoskeletal: tendinitis, periarthritis, Achilles bursitis, heel spur, exostosis
- Renal and metabolic: kidney disease, pyoureter, potassium deficiency
- Gastrointestinal and infection: *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, superimposed infection

**Drug interactions:** 100 interactions were identified, and 20 were available for review. Those rated **Major** are:
- Corticosteroids: hydrocortisone, triamcinolone, dexamethasone, betamethasone
- Bupropion

Corticosteroids are commonly used in scleroderma care, so this matters for the proposed indication. Moderate interactions include metformin, pioglitazone, acarbose, famotidine, loperamide, aprepitant, acetylsalicylic acid and budesonide.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Support for scleroderma is limited to one exploratory skin study and one study of a GI complication, with no registered trials. The prediction rests mainly on a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence.
- Safety data from the PI were not available, and the knowledge-graph contraindications include neuromuscular and tendon conditions that are relevant to scleroderma patients.

**To proceed, the following is needed:**
- The full results of the 2010 randomized antifibrotic study (PMID 20507401), and independent replication
- A registered, adequately powered controlled trial with clinical endpoints such as skin score
- The SAHPRA package insert warnings and contraindications
- Mechanism of action data and a mechanistic rationale for antifibrotic activity
- A review of interactions with corticosteroids and other drugs commonly used in scleroderma

It includes randomized non-inferiority trial publications for bubonic plague and animal model data, and is rated L2. It may merit its own evaluation.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "Ciprofloxacin has 8 valid single-ingredient SAHPRA registrations and no cancelled ones. The five below are shown; the other three are Bioflo" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

