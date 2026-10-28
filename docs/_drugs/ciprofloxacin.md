---
layout: default
title: Ciprofloxacin
parent: Model Prediction Only (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ciprofloxacin: predicted new indication Diffuse scleroderma (evidence level L4). Approved use: Bacterial infections (typhoid fever, salmonellosis, paratyphoid fever…"
monitor_inn: "Ciprofloxacin"
predicted_indications: ["diffuse scleroderma", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "punctate epithelial keratoconjunctivitis", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Ciprofloxacin
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

## Ciprofloxacin: From Bacterial Infections to Diffuse Scleroderma
{: .text-alpha }

## One-Sentence Summary

Ciprofloxacin is a fluoroquinolone antibiotic, originally used for bacterial infections such as typhoid fever, salmonellosis, bacterial pneumonia and shigellosis.
The TxGNN model predicts it may be useful for **diffuse scleroderma**, but there are **0 registered clinical trials** and only **2 publications**, both indirect or exploratory.
This is a model-driven hypothesis with limited supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (typhoid fever, salmonellosis, paratyphoid fever, bacterial pneumonia, shigellosis and others). The South African registration records compiled for this report do not include approved indication text. |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 0.9987 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 8 of 8) |
| Number of SAHPRA Registrations | 8 (valid: 8) |
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

Ciprofloxacin has 8 valid single-ingredient SAHPRA registrations and no cancelled ones. The five below are shown; the other three are Biofloxx 500, Ciploxx 250 and Xindex. Approved indication text and Essential Medicines List status are not available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 36/20.1.1/0377 | Ciploxx 500 | Tablet | Not stated in compiled data |
| Reg. No. 35/20.1.1/0101 | Orpic | Tablet | Not stated in compiled data |
| Reg. No. A39/20.1.1/0646 | Sabax-ciprofloxacin 50ml | Infusion | Not stated in compiled data |
| Reg. No. 33/16.2/0024 | Ciprobay HC Otic Drops | Drops | Not stated in compiled data |
| Reg. No. A40/15.1/0048 | Ceprolen 5ml | Drops | Not stated in compiled data |

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

**Note:** Another predicted indication for ciprofloxacin, **septicemic plague**, has stronger supporting evidence. It includes randomized non-inferiority trial publications for bubonic plague and animal model data, and is rated L2. It may merit its own evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

