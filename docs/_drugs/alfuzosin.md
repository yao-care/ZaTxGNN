---
layout: default
title: Alfuzosin
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 10
---

# Alfuzosin
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

# Alfuzosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Alfuzosin is a selective alpha-1 adrenergic receptor antagonist, originally established for the treatment of benign prostatic hyperplasia (BPH) by relaxing smooth muscle in the prostate and bladder neck. The TxGNN model predicts it may have potential activity against **Ambras type hypertrichosis universalis congenita** — a rare congenital hair disorder — with a prediction score of **99.99%**. However, there are currently **no clinical trials** and **no supporting publications** for this indication, placing this prediction at the lowest possible evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Benign Prostatic Hyperplasia (BPH) — based on established pharmaceutical knowledge; no SAHPRA-approved indication text available |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmaceutical knowledge, alfuzosin is a selective alpha-1 adrenergic receptor antagonist. It works by blocking alpha-1 receptors in the smooth muscle of the prostate gland and bladder neck, reducing urinary outflow obstruction in men with BPH. It has no known antineoplastic, genetic, or hair follicle-targeted properties.

Ambras type hypertrichosis universalis congenita is an exceptionally rare genetic disorder caused by mutations in the *TRPS1* gene (chromosome 8q23–24), characterised by excessive hair growth covering the entire body and face. Alpha-1 adrenergic receptors are indeed expressed in hair follicles, and sympathetic nervous system signalling is known to modulate hair follicle cycling to some degree. This provides a superficial biological connection. However, the critical problem is that Ambras hypertrichosis is caused by a structural gene defect — and there is no known pathway by which alpha-1 receptor blockade could correct or compensate for a *TRPS1* loss-of-function mutation.

The extremely high TxGNN score (0.9999943) is most likely the result of indirect, multi-step connections within the knowledge graph between hair follicle–related nodes, a well-recognised artefact described as topological false positives. Notably, 6 of the top 10 predicted indications for alfuzosin in this evidence pack are rare hair and hair follicle disorders (hypertrichosis, hair shaft abnormalities, trichomegaly, hypotrichosis), suggesting a systematic over-prediction bias in the hair-related node cluster of the knowledge graph rather than a true biological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Alfuzosin is not currently registered with SAHPRA and is not marketed in South Africa. No approved product registrations, dosage forms, or indication texts are on record. Any investigational or compassionate use would require prior SAHPRA authorisation.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> **Note for prescribers:** Safety data specific to alfuzosin (TFDA prescribing information, warnings, and contraindications) was not retrievable as part of this evidence pack. Known class-effect considerations for alpha-1 blockers include orthostatic hypotension, dizziness, and intraoperative floppy iris syndrome, but formal safety data should be confirmed through the official PI before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This TxGNN prediction for Ambras type hypertrichosis universalis congenita is supported by zero clinical trials and zero literature evidence. The mechanistic link between alpha-1 adrenergic blockade and a *TRPS1* gene-mutation-driven disorder is biologically implausible, and the high model score almost certainly reflects knowledge graph topology artefacts rather than a genuine repurposing signal. The same pattern is observed across 6 of the top 10 predictions for this drug, all of which are rare hair disorders.

**To proceed, the following is needed:**
- Retrieval of the full DrugBank MOA profile and pharmacology data for alfuzosin (currently a data gap)
- Retrieval of TFDA/SAHPRA-approved prescribing information for safety evaluation (currently blocking — DG001)
- Preclinical mechanistic evidence demonstrating any effect of alpha-1 receptor blockade on TRPS1-dependent hair follicle biology before further evaluation is warranted
- Independent review of the KG node structure for hair disorder clusters to quantify topological false-positive risk for this drug class
- If any future mechanistic hypothesis is generated, a full de novo evidence search specifically pairing alfuzosin with *TRPS1*-pathway biology would be required

> **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

