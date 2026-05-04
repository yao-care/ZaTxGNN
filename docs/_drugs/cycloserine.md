---
layout: default
title: Cycloserine
parent: 僅模型預測 (L5)
nav_order: 153
evidence_level: L5
indication_count: 10
---

# Cycloserine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Cycloserine: From Tuberculosis to Irritable Bowel Syndrome

## One-Sentence Summary

Cycloserine is a second-line antibiotic primarily used in the treatment of multidrug-resistant tuberculosis (MDR-TB). The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome (IBS)**, however there are currently **no clinical trials** and **no publications** directly supporting this specific repurposing direction. This prediction remains at the model-only stage (L5) and warrants significant caution.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multidrug-resistant tuberculosis (MDR-TB) — second-line agent |
| Predicted New Indication | Irritable Bowel Syndrome (IBS) |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 (Model prediction only, no clinical studies) |
| South Africa Market Status | Not marketed (no SAHPRA registrations identified) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available for this evidence pack. Based on known pharmacology, cycloserine is a D-alanine analogue that inhibits bacterial cell wall synthesis by blocking the enzymes alanine racemase and D-alanine:D-alanine ligase. This mechanism accounts for its established use against *Mycobacterium tuberculosis*. Additionally, D-cycloserine acts as a partial agonist at the glycine modulatory site of the NMDA (N-methyl-D-aspartate) receptor, which has led to investigation of its neuropsychiatric properties.

The mechanistic link between cycloserine and IBS is indirect and speculative. Some antibiotics, notably rifaximin, have demonstrated efficacy in IBS, presumably through modulation of gut microbiota. However, cycloserine's antimicrobial spectrum is primarily directed against mycobacteria, with no established activity against the gut flora implicated in IBS pathophysiology. The NMDA partial agonist activity of D-cycloserine could theoretically influence visceral hypersensitivity (a key feature of IBS), but this hypothesis has never been tested in preclinical or clinical settings.

Overall, the biological plausibility for this repurposing candidate is weak. The high TxGNN prediction score likely reflects network-level associations in the knowledge graph rather than a validated pharmacological rationale. Given cycloserine's well-documented neurotoxicity profile (seizures, psychosis, peripheral neuropathy), the risk-benefit balance for a functional gastrointestinal disorder like IBS would be unfavourable without compelling efficacy evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for cycloserine in irritable bowel syndrome.

---

## Literature Evidence

Currently no related literature available for cycloserine in irritable bowel syndrome.

---

## South Africa Market Information

Cycloserine does not currently hold any SAHPRA registrations. However, it is worth noting that cycloserine (Seromycin) is included on the WHO Essential Medicines List for the treatment of MDR-TB, and South Africa — bearing one of the world's highest TB burdens — may access this drug through the national TB programme or Section 21 (unregistered medicine) applications via SAHPRA. Healthcare professionals should verify current access pathways through the National Department of Health.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information, or the WHO Model Prescribing Information for cycloserine. Key safety concerns known from international sources include:

- **Neuropsychiatric toxicity**: Seizures, psychosis, confusion, depression, suicidal ideation, and insomnia are well-documented adverse effects
- **Peripheral neuropathy**: Reported with prolonged use
- **Monitoring requirements**: Serum drug levels (target 20–35 µg/mL), renal function, liver function, and neuropsychiatric assessment should be performed regularly
- **Pyridoxine supplementation**: Co-administration of pyridoxine (vitamin B6) is recommended to reduce neurotoxicity risk

Report adverse drug reactions to SAHPRA via the national pharmacovigilance reporting system.

---

## Additional Predicted Indications (Summary)

The TxGNN model generated 10 predicted indications for cycloserine. All received a **Hold** recommendation due to insufficient evidence. Below is a summary for completeness:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Clinical Trials | Publications | Recommendation |
|------|---------------------|-------------|----------------|-----------------|--------------|----------------|
| 1 | Irritable Bowel Syndrome | 99.95% | L5 | 0 | 0 | Hold |
| 2 | Acne | 99.91% | L5 | 0 | 0 | Hold |
| 3 | Gastroparesis | 99.66% | L5 | 0 | 0 | Hold |
| 4 | Conjunctivitis | 99.27% | L4 | 0 | 3 | Hold |
| 5 | Insomnia | 99.21% | L4 | 3 | 2 | Hold ⚠️ |
| 6 | Pharyngitis | 99.01% | L5 | 0 | 0 | Hold |
| 7 | Nasal Cavity Disease | 99.01% | L5 | 0 | 1 | Hold |
| 8 | Acute Laryngopharyngitis | 98.85% | L5 | 0 | 0 | Hold |
| 9 | Postgastrectomy Syndrome | 98.79% | L5 | 0 | 0 | Hold |
| 10 | Rhinitis | 98.70% | L5 | 0 | 0 | Hold |

**⚠️ Critical Note on Insomnia (Rank 5):** This is a **negative association**. Published literature (PMID [36712725](https://pubmed.ncbi.nlm.nih.gov/36712725/)) explicitly reports cycloserine-induced insomnia as an adverse drug reaction. The clinical trials found (NCT03216356, NCT05395494, NCT03395392) investigated D-cycloserine for psychiatric conditions (PTSD, fibromyalgia, bipolar depression) — not insomnia — and none were designed to assess sleep outcomes. Cycloserine is more likely to **worsen** than improve insomnia.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications lack meaningful clinical evidence supporting cycloserine repurposing. The top prediction (IBS) is at evidence level L5 with zero clinical trials and zero publications. The mechanistic rationale is speculative at best, and cycloserine's significant neurotoxicity profile makes it a poor candidate for repurposing into conditions (IBS, acne, rhinitis, pharyngitis) where safer and well-established treatments already exist. No SAHPRA registration exists for this drug in South Africa.

**To proceed, the following would be needed:**
- Preclinical studies demonstrating cycloserine activity in IBS models (gut motility, visceral hypersensitivity, microbiome modulation)
- Detailed mechanism of action analysis linking NMDA receptor modulation or antimicrobial properties to IBS pathophysiology
- Risk-benefit assessment given cycloserine's neuropsychiatric toxicity profile versus the non-life-threatening nature of IBS
- SAHPRA regulatory pathway assessment for any new indication development
- Consultation with the South African gastroenterology and infectious disease clinical communities

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require rigorous clinical validation before any therapeutic application. All predictions should be interpreted with appropriate scientific caution.*

*Data cutoff: 2026-04-05 | Evidence Pack version: v4*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

