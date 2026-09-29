---
layout: default
title: Fentanyl
parent: Model Prediction Only (L5)
nav_order: 225
evidence_level: L5
indication_count: 10
---

# Fentanyl
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

# Fentanyl: From Pain Management to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fentanyl is a potent mu-opioid agonist used for analgesia. The registration data supplied for South Africa does not state its approved indication.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, with **no clinical trials** and **no publications** supporting this direction.
This is a model prediction only and is most likely a graph artefact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data supplied (drug class: mu-opioid analgesic) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.46% (rank 3012) |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Fentanyl acts as a mu-opioid receptor agonist, which produces analgesia.

NSIAD is a rare condition in which gain-of-function mutations in *AVPR2* or *GNAS* cause the kidney to retain water inappropriately. Mu-opioid agonism is not a known modulator of this pathway, so no plausible mechanistic link can be drawn between fentanyl's analgesic use and this condition.

The high score most likely reflects the structure of the knowledge graph rather than independent biological signal. The prediction should be treated as a hypothesis with no supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 29/2.7/0605 | Pharma-q fentanyl ampoule 2ml | Injection |
| Reg. No. 48/2.9/0054 | Effentora 100 | Effervescent tablet |

Available routes are injectable and oral (effervescent tablet).

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials, no literature and no plausible mechanism. It is a model output only (L5). The requirement that a potent, dependence-forming opioid be justified by real evidence is not met.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (PI), covering indications, warnings and contraindications, to complete safety screening
- Mechanism of action data, and a biological rationale linking mu-opioid activity to AVPR2/GNAS-driven water retention
- Any preclinical or clinical signal for fentanyl in NSIAD (none was found in this search)

**Other predicted indications worth noting:**

| Predicted Indication | Score | Evidence Level | Note |
|------|------|------|------|
| Tourette syndrome | 99.05% | L5 | No trials or literature; dependence risk is a poor fit for a chronic paediatric-onset condition |
| Trichotillomania | 98.87% | L4 | One 2002 physiological probe study (PMID 12369265), not a treatment trial |
| Myofascial pain syndrome | 98.09% | L4 | Symptomatic analgesia, already within fentanyl's pain use. Verify NCT00343733 (Phase 3, completed, n=120) to confirm fentanyl is the study drug and the condition. If confirmed, the level could rise to L1 or L2 |
| Manic bipolar affective disorder | 97.73% | L5 | Retrieved literature covers overdose, case reports and anaesthesia interactions, not efficacy |
| Migraine with brainstem aura | 97.71% | L4 | Case report only; opioids are generally discouraged in migraine |
| Methaemoglobinaemia | 97.22% | L5 | Co-mention in anaesthesia literature; no therapeutic rationale |
| Myositis fibrosa | 97.04% | L5 | Prediction only; identical score to idiopathic granulomatous myositis suggests a shared graph neighbourhood |
| Idiopathic granulomatous myositis | 97.04% | L5 | Prediction only; analgesia would not address the underlying pathology |
| Tendinitis | 97.04% | L4 | Literature is perioperative analgesia after shoulder surgery, not treatment of tendinitis |

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

