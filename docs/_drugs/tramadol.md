---
layout: default
title: Tramadol
parent: Model Prediction Only (L5)
nav_order: 454
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tramadol: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Osteoarthritis, arthropathy"
monitor_inn: "Tramadol"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "spondyloarthropathy, susceptibility to", "juvenile idiopathic arthritis", "juvenile arthritis due to defect in LACC1", "rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis"]
---

# Tramadol
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

# Tramadol: From Osteoarthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Tramadol is an opioid analgesic that acts on the mu-opioid receptor and on serotonin/noradrenaline reuptake. It was originally linked to osteoarthritis and arthropathy.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but **no clinical trials and no publications** support this prediction. It is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoarthritis, arthropathy (from the knowledge graph; the SAHPRA registration records contain no indication text) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not available in the data compiled for this report. Based on general pharmacology, tramadol is a mu-opioid agonist with serotonin and noradrenaline reuptake inhibition. It provides symptomatic pain relief and does not change the course of disease.

Acromesomelic dysplasia, Hunter-Thompson type is a rare genetic skeletal disorder caused by loss of function of the *GDF5* (CDMP1) gene. Tramadol does not act on this pathway. The very high TxGNN score most likely reflects closeness in the knowledge graph to skeletal and joint disease nodes (such as osteoarthritis), not a true therapeutic relationship.

The other top-ranked predictions are similar. Most are rare genetic skeletal or connective tissue disorders (brachyolmia, pseudoachondroplasia, myosclerosis) or juvenile and rheumatoid arthritis variants. At best, tramadol could give symptomatic pain relief in some of these conditions. None has a disease-modifying rationale, and none has supporting clinical data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for tramadol in this predicted indication. The only publication retrieved (for a lower-ranked prediction, juvenile idiopathic arthritis) concerns ketoprofen, a different drug, and is not evidence for tramadol.

## South Africa Market Information

Tramadol is marketed in South Africa under 9 valid SAHPRA registrations, all single-ingredient entries. Approved indication text and Essential Medicines List (EML) status were not available in the data compiled for this report. Some product names (for example Tramazac co, Painogesic Co, Dytracet, Tamoltra) suggest tramadol/paracetamol combinations, although the records classify them as single entries. Please confirm the composition in the Professional Information (PI).

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 32/2.9/0652 | Tramahexal | Capsule | Not available |
| Reg. No. 44/2.9/0496 | Tramazac SR | Sustained-release tablet (Srt) | Not available |
| Reg. No. 36/2.9/0337 | Dolotram 50 | Injection | Not available |
| Reg. No. 37/2.9/0532 | Dolotram | Capsule | Not available |
| Reg. No. 54/2.9/0185 | Domadol Plus | Tablet | Not available |

Four further registrations are valid: Tramazac co 37.5mg/325mg (45/2.9/0303), Painogesic Co (A 48/2.9/0774), Dytracet (45/2.9/0747) and Tamoltra 37.5mg/325mg (46/2.9/0976).

## Safety Considerations

SAHPRA package insert warnings and contraindications could not be retrieved, so the PI must be reviewed before any further evaluation. Report adverse drug reactions to SAHPRA.

- **Knowledge-graph contraindications** (from the PrimeKG graph, not label text): hypertensive disorder, liver failure, liver disease, cirrhosis, epilepsy, anxiety and neurotic disorders, dysthymic disorder, diabetes mellitus and diabetic ketoacidosis, substance abuse/dependence and withdrawal (including alcohol withdrawal), respiratory failure, paracetamol poisoning, serotonin syndrome, intracranial hypertension, central nervous system infections and others.
- **Drug interactions**: 100 interactions were identified, and the first 20 are listed in the data compiled for this report.
  - **Major**: alvimopan, bupropion, cisapride, dexfenfluramine, diethylpropion, dolasetron, dronabinol, ephedrine, fenfluramine.
  - **Moderate**: atropine, bisacodyl, castor oil, cimetidine, clarithromycin, clidinium, dicyclomine, eliglustat, eluxadoline, famotidine, glycerin.
- **Paediatric use**: several of the predicted indications are juvenile conditions. Tramadol carries significant paediatric restrictions, including the risk of respiratory depression and CYP2D6 variability.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN score, with no clinical trials or publications. There is no credible mechanistic link between a symptomatic opioid analgesic and a genetic skeletal dysplasia. All ten top predictions are L5, and none has clinical support.

**To proceed, the following is needed:**
- Detailed mechanism-of-action data, to confirm whether any plausible link exists
- The SAHPRA Professional Information (warnings, contraindications and approved indications)
- Any clinical or observational evidence for tramadol in the predicted condition
- If the aim is symptomatic pain relief in skeletal or joint disorders, a separate evaluation of that use against existing analgesic guidance, including paediatric safety
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

