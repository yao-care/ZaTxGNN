---
layout: default
title: Cefpodoxime
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 10
---

# Cefpodoxime
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

# Cefpodoxime: From Bacterial Infections to Osteoarthritis Susceptibility

## One-Sentence Summary

Cefpodoxime is a third-generation oral cephalosporin antibiotic, originally indicated for the treatment of bacterial infections including upper and lower respiratory tract infections and urinary tract infections.
The TxGNN model predicts it may have activity against **Osteoarthritis Susceptibility** (top-ranked indication),
however **no supporting clinical trials or published literature** currently exist for this repurposing direction, placing the evidence at the lowest confidence tier (**L5 — model prediction only**).

Notably, all 10 top-ranked TxGNN predictions for this drug fall within musculoskeletal, skeletal dysplasia, or connective tissue disease clusters, a pattern consistent with a knowledge graph clustering artefact rather than independent mechanistic signals.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (cephalosporin antibiotic class; not registered with SAHPRA) |
| Predicted New Indication | Osteoarthritis Susceptibility |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacological class information, Cefpodoxime is a third-generation cephalosporin antibiotic (beta-lactam class) whose antibacterial efficacy is established via inhibition of bacterial cell wall synthesis (penicillin-binding protein inhibition). It has no known cartilage-protective, matrix metalloproteinase (MMP)-inhibitory, or osteoarthritis-modifying activity.

The repurposing rationale analysis in this Evidence Pack explicitly identifies **no direct mechanistic link** between cefpodoxime and osteoarthritis susceptibility. While some antibiotic classes have genuine musculoskeletal research precedents — for example, tetracyclines such as doxycycline and minocycline have been investigated for MMP-3/MMP-13 inhibition in OA, and minocycline has Level 1 RCT data (the MIRA trial) in rheumatoid arthritis — **these mechanisms do not apply to the beta-lactam class**. Cefpodoxime has no immune-modulatory activity and no published data in any joint disease setting.

The high TxGNN scores across all 10 predictions (0.986–0.993), spanning osteoarthritis, rheumatoid arthritis, skeletal dysplasias (brachyolmia, pseudoachondroplasia, acromesomelic dysplasia), and rare syndromes (colobomatous microphthalmia-rhizomelic dysplasia), are most parsimoniously explained by **musculoskeletal disease cluster proximity in the knowledge graph** rather than genuine pharmacological predictions. The near-identical score banding across unrelated skeletal conditions strongly supports a systematic cluster-scoring phenomenon rather than individual mechanistic signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA via [https://www.sahpra.org.za](https://www.sahpra.org.za).

> **Note:** As cefpodoxime is not currently registered in South Africa, clinicians should consult the originator product's Professional Information from its country of registration and apply standard cephalosporin class precautions, including allergy history screening (cross-reactivity with penicillins) and renal dose adjustment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predicted indications for cefpodoxime are classified at evidence level L5 (model prediction only), with zero supporting clinical trials or publications identified across all 10 queried disease–drug pairs. The predicted indications — predominantly skeletal dysplasias, connective tissue diseases, and rare congenital syndromes — bear no established mechanistic connection to a beta-lactam antibiotic, and the scoring pattern is consistent with a knowledge graph clustering artefact. There is currently no scientific basis to advance this drug toward repurposing investigation for any of the predicted indications.

**To proceed, the following would be needed:**

- Formal MOA characterisation confirming any plausible non-antibacterial activity (e.g., anti-inflammatory, MMP-inhibitory, or immune-modulatory effects) — none are currently documented
- At least one peer-reviewed hypothesis paper or preclinical study linking cefpodoxime to musculoskeletal or cartilage biology before clinical investigation could be ethically or scientifically justified
- SAHPRA registration data and an approved Professional Information document, as the drug has no current South African regulatory status
- Independent review of the TxGNN knowledge graph to assess whether the musculoskeletal cluster artefact affects other beta-lactam predictions systematically
- If osteoarthritis is the therapeutic area of interest, exploration of better-evidenced antibiotic candidates (e.g., doxycycline, minocycline) with existing human data should be prioritised over cefpodoxime

---

> **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. This assessment is based on data available as of 5 April 2026.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

