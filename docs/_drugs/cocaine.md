---
layout: default
title: Cocaine
parent: Model Prediction Only (L5)
nav_order: 143
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cocaine: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not recorded in the SAHPRA registration data. The pharmacology data d…"
monitor_inn: "Cocaine"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "papillary conjunctivitis", "rhinitis", "irritable bowel syndrome", "anaphylaxis", "neurocirculatory asthenia", "atopic conjunctivitis", "food-dependent exercise-induced anaphylaxis", "pharyngitis"]
---

# Cocaine
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

# Cocaine: From Local Anaesthesia to Cauda Equina Syndrome (Prediction Not Supported)

## One-Sentence Summary

Cocaine is a natural-product local anaesthetic and monoamine reuptake inhibitor. The only South African registration in the data compiled for this report is a liquid toothache product, and no approved indication text is recorded for it. The TxGNN model predicts it may be useful for **cauda equina syndrome**, but there are **0 clinical trials** and only **1 case report** (not involving cocaine as a therapy), so this prediction is best regarded as a graph-based artefact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA registration data. The pharmacology data describes clinical use as a local anaesthetic in nasal, oral and laryngeal surgery |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, cocaine blocks sodium channels (local anaesthetic effect) and inhibits monoamine reuptake. The pharmacology data also lists activity at the 5-HT3 receptor and the dopamine transporter (DAT, rat data).

**The prediction is not mechanistically credible.** Cauda equina syndrome is a compressive neurological emergency that needs urgent surgical decompression. A local anaesthetic or stimulant would not treat the compression. The only publication retrieved is a case report on lumbosacral disc pathology that does not involve cocaine. The high TxGNN score most likely reflects network proximity in the knowledge graph rather than a real therapeutic link.

**Other predicted indications** were also reviewed, and none is supported:

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Obsolete neurogenic bladder | 99.96% | L5 | Prediction only; obsolete disease term; unsuitable given cardiovascular and abuse risks |
| Papillary conjunctivitis | 99.95% | L5 | No evidence; topical cocaine is toxic to the corneal epithelium |
| Rhinitis | 99.92% | L4 | One RCT compared topical cocaine with adrenaline in endoscopic sinus surgery (a surgical field-preparation use, not rhinitis treatment). Most literature describes cocaine as a *cause* of rhinitis and midline destruction |
| Irritable bowel syndrome | 99.89% | L5 | Retrieved papers unrelated to cocaine |
| Anaphylaxis | 99.88% | L4 | Only preclinical catecholamine-uptake studies; epinephrine is the standard therapy |
| Neurocirculatory asthenia | 99.83% | L5 | A stimulant would be expected to worsen symptoms |
| Atopic conjunctivitis | 99.83% | L5 | No evidence; ocular toxicity |
| Food-dependent exercise-induced anaphylaxis | 99.82% | L5 | No evidence; adds cardiovascular risk |
| Pharyngitis | 99.71% | L4 | Literature documents harm (mucosal burns, abscess); safer anaesthetics such as lidocaine exist |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The single publication retrieved for cauda equina syndrome:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31528422](https://pubmed.ncbi.nlm.nih.gov/31528422/) | 2019 | Case report/Review | Surgical Neurology International | Case of distal cauda equina syndrome from lumbosacral disc pathology; describes diagnostic challenges. Cocaine is not studied as a treatment |

For context, the most relevant item among the other predicted indications is an RCT in rhinitis-related surgery:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24678064](https://pubmed.ncbi.nlm.nih.gov/24678064/) | 2014 | RCT | Int Forum Allergy Rhinol | Topical cocaine vs adrenaline for surgical field visualisation in endoscopic sinus surgery (not treatment of rhinitis) |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G2815 | Toothache Essence (Dozen) | Liquid | Not recorded |

Essential Medicines List (EML) inclusion status could not be determined from the data compiled for this report.

---

## Safety Considerations

- **Disease associations from the knowledge graph (not label text):** the TxGNN knowledge graph links cocaine with contraindication to epilepsy, sudden cardiac arrest, heart conduction disease, thyrotoxicosis, hyperthyroidism and Graves disease.
- **Pharmacological interactions (target-level, no severity grading):** the data lists activity at 5-HT3AB, 5-HT3A and the dopamine transporter (rat data). These are target interactions rather than drug-drug interaction rules.
- **Literature-based concerns:** the retrieved publications document cocaine-associated nasal septal and palatal necrosis, mucosal burns, bronchospasm, allergic reactions and severe infections. Its abuse liability and cardiovascular risk are also prohibitive for new indications.

Please refer to the SAHPRA-approved Professional Information (PI) for formal warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predicted indications rest on model output alone or on indirect and harm-related literature. There are no clinical trials, and cocaine's abuse liability, cardiovascular toxicity and tissue toxicity, together with safer established alternatives, argue against pursuing repurposing.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications and approved indication), which is currently missing and blocks safety screening
- Mechanism of action data (for example from DrugBank)
- Any direct clinical evidence of benefit for the predicted indication, none of which currently exists
- A clear regulatory and scheduling review, since cocaine is a controlled substance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

