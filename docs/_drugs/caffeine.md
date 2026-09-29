---
layout: default
title: Caffeine
parent: Moderate Evidence (L3-L4)
nav_order: 84
evidence_level: L4
indication_count: 10
---

# Caffeine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Caffeine: From Approved Products to Nasal Cavity Disease

## One-Sentence Summary

Caffeine is a long-established stimulant that is marketed in South Africa, mainly in oral capsule, tablet and syrup products.
The TxGNN model predicts it may be useful for **nasal cavity disease**, but this rests on **0 clinical trials** and only **3 loosely related publications**.
None of the publications tests caffeine as a treatment for a nasal disease, so this is a model prediction with very little support.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 20 |
| Recommended Decision | Hold |

The registration records supplied contain no approved-indication text, so the original indication is not shown.

## Why is This Prediction Reasonable?

Caffeine acts mainly by blocking adenosine receptors and inhibiting phosphodiesterase (PDE). A detailed mechanism-of-action record is not currently available for this evaluation.

The link to nasal disease is weak and indirect. Bitter taste receptors (T2Rs) are found in airway and nasal tissue, and caffeine is a possible secondary target there. The nasal caffeine gel study concerns delivering caffeine through the nose to improve cognition. It does not treat a nasal disease. No study reports a nasal disease outcome, so the high TxGNN score is a prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | Review | Pharmacology & Therapeutics | Bitter taste receptors are expressed in the nasal cavity and lungs. This is a possible target but not evidence of benefit. |
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | Formulation/preclinical | Current Drug Delivery | A nasal caffeine thermo-sensitive gel was developed to improve cognition after sleep deprivation. It is about drug delivery, not nasal disease. |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | Animal study | Cancer Research | Black tea and caffeine reduced lung tumours in rats given a tobacco carcinogen. It is not relevant to nasal disease. |

## South Africa Market Information

Twenty registrations exist. The five main ones are listed below. Registration records give no approved-indication text or manufacturer, and Essential Medicines List status is not available.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. X/5.8/383 | Adco-sinal ns | Capsule |
| Reg. No. 29/5.8/0782 | Sinuend | Tablet |
| Reg. No. 27/2.8/0574 | Adco-salterpyn | Tablet |
| Reg. No. 28/2.8/0383 | Tensodol | Tablet |
| Reg. No. 29/2.8/0280 | Spectrapain Forte T | Tablet |

Across all registrations the dosage forms are oral capsules and tablets, plus a syrup.

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried source.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no trials and no studies of caffeine for any nasal disease. The mechanistic link is speculative, and the safety information needed to move forward is missing.

**To proceed, the following is needed:**
- The SAHPRA package insert warnings and contraindications (a blocking gap for safety screening). These can be obtained by downloading and parsing the PI from the SAHPRA website.
- A documented mechanism of action, for example from the DrugBank API, to test the link to nasal disease.
- Evidence that caffeine acts on a specific nasal condition, such as a preclinical model or a pilot study.
- Route compatibility assessment. Registered forms are oral, and a nasal use would need a different route.

Among the other predictions, hypnic headache has a more concrete lead. Reviews describe caffeine as a case-based therapeutic option there, so it may be a better research question than nasal disease.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

