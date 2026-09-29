---
layout: default
title: Omega-3 Fatty Acids
parent: Model Prediction Only (L5)
nav_order: 351
evidence_level: L5
indication_count: 10
---

# Omega-3 Fatty Acids
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

# Omega-3 Fatty Acids: From a Marketed Infusion Product to Tendinitis

## One-Sentence Summary

Omega-3 fatty acids (EPA/DHA) are registered in South Africa as a component of one infusion product, Nutriflex Omega Specialized. The TxGNN model predicts they may be useful for **tendinitis**. There are **no registered clinical trials** and **15 publications**, mostly animal, laboratory or observational studies, with one human RCT whose target condition is unconfirmed and one human trial reporting no benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Tendinitis |
| TxGNN Prediction Score | 99.13% |
| Evidence Level | L4 (preclinical and mechanistic support only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

The registered indication text for the product is not recorded in the dataset, so no original indication is shown.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the dataset. Based on the supplied literature, EPA and DHA are precursors of specialised pro-resolving mediators (such as resolvins and maresins). These mediators help switch off inflammation. They also reduce pro-inflammatory eicosanoid and cytokine signalling.

Chronic tendinopathy is thought to involve inflammation that fails to resolve. Laboratory work on tendon cells from patients with Achilles tendinopathy and shoulder tendon tears found dysregulated resolution pathways. It also found that adding pro-resolving mediators moderated their inflammatory responses. Rat models of Achilles tendinopathy showed benefit with omega-3 or DHA. An observational study found a low Omega-3 Index in patients with degenerative rotator cuff tears.

These links are plausible but indirect. Human clinical evidence is thin, and one trial in lateral epicondylitis found no effect (see below).

---

## Clinical Trial Evidence

Currently no related clinical trials registered for tendinitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30364577](https://pubmed.ncbi.nlm.nih.gov/30364577/) | 2018 | RCT (multicentre, double-blind, placebo-controlled) | BMJ Open Sport Exerc Med | Long-chain omega-3 in rotator cuff related shoulder pain. The target condition is truncated in the source title, so relevance is unconfirmed. |
| [16215602](https://pubmed.ncbi.nlm.nih.gov/16215602/) | 2005 | Randomised trial | Tidsskr Nor Laegeforen | Essential fatty acid supplement had no effect on pain in lateral epicondylitis. |
| [37146985](https://pubmed.ncbi.nlm.nih.gov/37146985/) | 2023 | Scoping review | J Sport Rehabil | Reviews nutritional supplements for tendinopathy. There is no consensus on optimal management. |
| [18950988](https://pubmed.ncbi.nlm.nih.gov/18950988/) | 2009 | Review | J Hand Ther | Asks whether PUFAs and antioxidants have a role in rotator cuff tendinopathy. Robust evidence is lacking. |
| [31492432](https://pubmed.ncbi.nlm.nih.gov/31492432/) | 2019 | Observational | Prostaglandins Leukot Essent Fatty Acids | Degenerative rotator cuff tears are associated with a low Omega-3 Index. |
| [36458821](https://pubmed.ncbi.nlm.nih.gov/36458821/) | 2023 | Animal study | Appl Physiol Nutr Metab | Omega-3 plus exercise reduced collagenase-induced Achilles tendinopathy in rats. |
| [34612118](https://pubmed.ncbi.nlm.nih.gov/34612118/) | 2022 | Animal study | Connect Tissue Res | DHA was protective in a rat Achilles tendinopathy model and was compared with collagen. |
| [40376939](https://pubmed.ncbi.nlm.nih.gov/40376939/) | 2025 | Experimental study | Am J Sports Med | Aerobic exercise with omega-3 was studied for its effect on tendon healing after Achilles rupture. |
| [30916999](https://pubmed.ncbi.nlm.nih.gov/30916999/) | 2019 | Laboratory study | FASEB J | Pro-resolving mediators 15-epi-LXA4 and MaR1 countered inflammation in tendon stromal cells from patients. |
| [31437425](https://pubmed.ncbi.nlm.nih.gov/31437425/) | 2019 | Laboratory study | Am J Pathol | Pro-resolving mediators LXB4 and RvE1 regulated inflammation in stromal cells from shoulder tendon tears. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 49/25/0065 | Nutriflex Omega Specialized | Infusion |

The only available route is injectable (infusion). This is not a route used for tendinitis, so route compatibility would need to be addressed.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug interaction records were found in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The tendinitis prediction has a high model score but rests on animal, laboratory and observational data. The one human trial that clearly addresses a tendon condition (lateral epicondylitis) showed no benefit. The safety data needed for screening are also missing.

Other predicted indications are weaker: most have no evidence at all. For the platelet-related ones (Glanzmann thrombasthenia, pseudo-von Willebrand disease, primary release disorder of platelets), omega-3's anti-aggregatory effect runs in the opposite direction and raises a bleeding-risk concern. Fibromyalgia has slightly more support (a small Phase 2 trial, n=19, and a recent RCT) but no Phase 3 confirmation.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of the target condition in the 2018 RCT (PMID 30364577)
- Human clinical data in tendinopathy, or a registered trial
- Assessment of an oral formulation, since only an infusion product is registered locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

