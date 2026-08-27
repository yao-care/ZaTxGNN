---
layout: default
title: Esomeprazole
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
---

# Esomeprazole
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

# Esomeprazole: From Acid-Related Disorders to Duodenogastric Reflux

## One-Sentence Summary

Esomeprazole is a proton pump inhibitor (PPI) with globally established use in gastric acid-related conditions (GERD, peptic ulcer disease, H. pylori eradication). The TxGNN model predicts it may be effective for **Duodenogastric Reflux**, but this is currently supported only by mechanistic reasoning and **1 general review article** — no clinical trials specifically address this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acid-related disorders (GERD, peptic ulcer disease, H. pylori eradication) — well-established PPI-class use; formal SAHPRA-approved indication text is unavailable because the product is not currently marketed in South Africa |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L4 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for esomeprazole is not available in this evidence pack (DrugBank MOA query is flagged as a data gap). Based on known information, esomeprazole is the S-isomer of omeprazole and belongs to the proton pump inhibitor (PPI) class, which irreversibly inhibits the H+/K+-ATPase pump in gastric parietal cells to suppress acid secretion. Its efficacy in acid-related disorders — peptic ulcer, H. pylori infection, GERD, NSAID-induced gastrointestinal lesions, and Zollinger-Ellison syndrome — is well established (per the supporting literature in this pack).

However, the mechanistic link to duodenogastric reflux is weak. Duodenogastric reflux is primarily driven by bile acids and pancreatic enzymes refluxing into the stomach, not by gastric acid itself. PPI therapy has no direct causal mechanism against this pathology; at best it may indirectly alter bile salt activity by raising intragastric pH. This is an indirect, non-specific mechanism rather than a targeted pharmacological rationale, which is why the evidence level is capped at L4 and the recommendation is Hold.

It is also worth noting that other TxGNN-predicted indications for esomeprazole in this dataset (e.g., duodenal ulcer, active peptic ulcer disease) carry much stronger clinical trial evidence (L1), but these largely represent already-established core PPI-class indications rather than genuine repurposing candidates.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | European Journal of Clinical Pharmacology | General review confirming PPIs as first-line therapy for peptic ulcer, H. pylori infection, GERD, NSAID-induced GI lesions, and Zollinger-Ellison syndrome; does not specifically address duodenogastric reflux |

---

## South Africa Market Information

Esomeprazole is currently **not marketed** in South Africa, and no SAHPRA product registrations are on record in this evidence pack.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.53%), the mechanistic link between PPI-mediated acid suppression and duodenogastric reflux (a bile/pancreatic-enzyme-driven condition) is indirect and non-specific. No clinical trials specifically evaluate esomeprazole for this indication, and only one general (non-specific) review supports it. Additionally, TFDA/SAHPRA-approved safety data (warnings, contraindications) are missing and flagged as a **Blocking** data gap, preventing any initial safety assessment.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) — warnings and contraindications (currently blocking)
- Confirmed mechanism of action data from DrugBank
- Dedicated clinical or observational studies evaluating esomeprazole specifically for duodenogastric reflux
- Clarification of a South African market/registration pathway, as the product is currently unmarketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

