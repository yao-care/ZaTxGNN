---
layout: default
title: Cefpodoxime
parent: Model Prediction Only (L5)
nav_order: 104
evidence_level: L5
indication_count: 2
monitor_inn: "Cefpodoxime"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis"]
last_modified_at: 2026-10-29
description: "Cefpodoxime: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not stated in the SAHPRA licence records compiled for this report (ce…"
---

# Cefpodoxime
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Cefpodoxime: From Bacterial Infections to Osteoarthritis
{: .text-alpha }

## One-Sentence Summary

Cefpodoxime is an oral third-generation cephalosporin antibiotic, marketed in South Africa as a tablet and as an oral suspension. The TxGNN model predicts it may be relevant to **osteoarthritis** (and, at a near-identical score, rheumatoid arthritis), but **no clinical trials and no publications** were found to support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA licence records compiled for this report (cefpodoxime is a cephalosporin antibacterial) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 0.9925 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 2 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. In general, cefpodoxime is a beta-lactam antibiotic that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins. This is an antibacterial mechanism.

No mechanistic link between this action and osteoarthritis is supported by the data. No anti-inflammatory, chondroprotective or analgesic mechanism is established for cefpodoxime. The same applies to rheumatoid arthritis, where no immunomodulatory activity relevant to the autoimmune pathology is known.

The very high TxGNN score (0.9925 for osteoarthritis, 0.9924 for rheumatoid arthritis) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The near-identical scores for the two arthritis conditions fit this pattern. Any rationale, for example an indirect effect on infection-related joint disease, is speculative.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 54/20.1.1/0469 | Cefpodoxime 100 Mg Ascend | Tablet | Not stated in the records compiled |
| Reg. No. 43/20.1.1/0245 | Orchid Cefpodoxime 40 Mg/ 5 Ml | Suspension | Not stated in the records compiled |

Both registrations are valid single-ingredient products. No Essential Medicines List (EML) information was available in the data compiled for this report.

## Safety Considerations

**Drug Interactions:** The interaction query returned 78 entries. The 20 shown in the data compiled are all rated Moderate. They fall mainly into these groups:
- **Acid-suppressing agents:** famotidine, ranitidine (including ranitidine bismuth citrate), cimetidine, nizatidine, and proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole)
- **Antacids:** aluminium hydroxide, calcium carbonate, magaldrate, magnesium carbonate, magnesium hydroxide, magnesium oxide
- **Aminoglycosides:** kanamycin, neomycin
- **Other:** balsalazide

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for osteoarthritis comes only from the TxGNN model. There are no clinical trials, no publications and no plausible mechanism for an antibacterial beta-lactam in a degenerative or autoimmune joint disease. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data and a biologically plausible rationale for osteoarthritis
- Any preclinical or clinical studies that directly address osteoarthritis
- The SAHPRA Professional Information (warnings, contraindications and approved indications), which is currently missing and blocks safety screening
- Confirmation of route and formulation suitability, which has not yet been assessed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

