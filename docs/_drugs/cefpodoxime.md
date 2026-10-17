---
layout: default
title: Cefpodoxime
parent: Model Prediction Only (L5)
nav_order: 105
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cefpodoxime: predicted new indication Osteoarthritis susceptibility (evidence level L5). Approved use: Not stated in the SAHPRA registration data compiled for this report (…"
monitor_inn: "Cefpodoxime"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis", "hemoglobinopathy", "brachyolmia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "pseudoachondroplasia"]
---

# Cefpodoxime
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

# Cefpodoxime: From Bacterial Infections to Osteoarthritis Susceptibility

## One-Sentence Summary

Cefpodoxime is a third-generation cephalosporin antibiotic that works by inhibiting bacterial cell wall synthesis. The TxGNN model predicts it may be relevant to **osteoarthritis susceptibility**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. The prediction appears to reflect knowledge-graph structure rather than a pharmacological rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data compiled for this report (cefpodoxime is a cephalosporin antibiotic) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, cefpodoxime is a third-generation cephalosporin that binds penicillin-binding proteins and blocks bacterial cell wall synthesis. Its established role is in treating bacterial infections.

**The prediction is not well supported mechanistically.** "Osteoarthritis susceptibility" is a genetic risk phenotype, not a treatable disease state. No known pathway links a beta-lactam antibiotic to it. The high TxGNN score (0.993) most likely reflects knowledge-graph topology rather than pharmacological reasoning.

The other top-ranked predictions show the same pattern:

| Rank | Predicted Indication | TxGNN Score | Assessment |
|------|------|------|------|
| 2 | Osteoarthritis | 99.25% | No established mechanism. Some antibiotics (e.g., doxycycline) have been studied for MMP inhibition, but this is not established for cephalosporins. |
| 3 | Rheumatoid arthritis | 99.24% | No known immunomodulatory activity. Established therapies act on immune pathways that cefpodoxime does not target. |
| 4 | Hemoglobinopathy | 98.84% | Antibiotics are used only for infection complications, not as disease-modifying therapy. |
| 5 | Brachyolmia | 98.76% | Rare skeletal dysplasia. No known interaction with the relevant pathways. |
| 6–10 | Rare genetic skeletal and developmental disorders | 98.60–98.71% | No plausible mechanism. Likely artifacts of shared graph neighbours. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 54/20.1.1/0469 | Cefpodoxime 100 Mg Ascend | Tablet | Not available in the data compiled |
| Reg. No. 43/20.1.1/0245 | Orchid Cefpodoxime 40 Mg/ 5 Ml | Suspension | Not available in the data compiled |

Both registrations are valid single-ingredient products. Essential Medicines List (EML) status was not available in the data compiled for this report.

## Safety Considerations

**Drug Interactions**

A total of 78 interacting drugs were identified. The 20 listed in the data compiled are all rated **Moderate**:

- **Acid-reducing agents (H2 blockers):** famotidine, ranitidine, ranitidine bismuth citrate, cimetidine, nizatidine
- **Proton pump inhibitors:** omeprazole, esomeprazole, rabeprazole, lansoprazole, dexlansoprazole, pantoprazole
- **Antacids:** aluminium hydroxide, calcium carbonate, magaldrate, magnesium carbonate, magnesium hydroxide, magnesium oxide
- **Aminoglycosides:** kanamycin, neomycin
- **Other:** balsalazide

Acid-reducing agents and antacids may reduce cefpodoxime absorption. Aminoglycosides warrant caution because of additive nephrotoxicity concerns. Please verify these against the approved Professional Information (PI).

For warnings and contraindications, please refer to the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is computational only, with no clinical trials, no publications, and no plausible mechanism. The top-ranked indication is a genetic risk phenotype rather than a treatable disease. Evidence is at the lowest level (L5), so repurposing is not justified at this time.

**To proceed, the following is needed:**
- Mechanism of action data and a credible mechanistic hypothesis linking cefpodoxime to a musculoskeletal or inflammatory pathway
- Preclinical evidence (in vitro or animal) in a well-defined disease such as osteoarthritis
- The SAHPRA package insert (approved indications, warnings, contraindications) to enable safety screening
- Review of whether the predictions in this list, including osteoarthritis and rheumatoid arthritis, have any rationale beyond knowledge-graph similarity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

