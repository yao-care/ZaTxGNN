---
layout: default
title: Pramocaine
parent: Model Prediction Only (L5)
nav_order: 380
evidence_level: L5
indication_count: 10
---

# Pramocaine
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

# Pramocaine: From Topical Local Anaesthesia to Papillary Conjunctivitis

## One-Sentence Summary

Pramocaine is a topical local anaesthetic, registered in South Africa as a suppository (Anugesic).
The TxGNN model predicts it may be useful for **papillary conjunctivitis**,
but **no clinical trials and no publications** currently support this prediction, which rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA record; pramocaine is a topical local anaesthetic |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Pramocaine is a topical local anaesthetic that blocks voltage-gated sodium channels. In theory this could ease ocular surface discomfort or itch.

The link is weak. Papillary conjunctivitis is driven by allergic or mechanical causes, and a sodium channel blocker does not treat either. Topical anaesthetics also carry a risk of corneal toxicity with ocular use, which makes them unsuitable for repeated or chronic use on the eye. The high score is most likely a knowledge-graph association rather than a mechanistically grounded signal.

The other nine top-ranked predictions share these limitations. They include vernal, atopic and rosacea conjunctivitis, acne keloid, acrodermatitis chronica atrophicans, neonatal and amyopathic dermatomyositis, familial hydroa vacciniforme, and childhood connective-tissue-disease-associated interstitial lung disease. All have scores of 97.8% to 98.5%, all are L5 with no trials or literature, and all are rated Hold. At best, pramocaine might give symptomatic relief of pain or itch in the skin conditions. No plausible mechanism reaches the underlying disease in any of them, and none applies to interstitial lung disease.

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR or PACTR).

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| E512 | Anugesic | Suppository | Not stated in the record |

The only registered form is a suppository (rectal route). It is not suited to ocular or dermatological use, so any repurposing would need a different formulation and a new registration.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Two points from the prediction review also apply. Ocular exposure to topical anaesthetics risks corneal injury. Use in neonates raises concern about systemic absorption through immature skin.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials or publications, and the proposed mechanism does not address the cause of papillary conjunctivitis. Ocular use of a topical anaesthetic also carries a known safety risk.

**To proceed, the following is needed:**
- The SAHPRA package insert, with warnings and contraindications, for the safety screen
- Mechanism of action data from DrugBank
- Preclinical or clinical evidence of benefit in the predicted condition, including ocular tolerability
- An ophthalmic formulation and route assessment, since the only registered product is a suppository

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

