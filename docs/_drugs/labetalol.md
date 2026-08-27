---
layout: default
title: Labetalol
parent: 僅模型預測 (L5)
nav_order: 276
evidence_level: L5
indication_count: 4
---

# Labetalol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using the report template directly (straightforward document-generation task from a fully-specified Evidence Pack — no additional skill needed).

# Labetalol: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

> Labetalol is a combined alpha/beta-adrenergic blocking antihypertensive (original indication text and MOA were not provided in this evidence pack — flagged as data gaps DG001/DG002).
> The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**,
> with **no registered clinical trials** and only **2 incidental literature mentions** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in evidence pack (no SAHPRA license text available; general pharmacology: hypertension, incl. hypertensive emergencies) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L4 (incidental case-report mentions only; no dedicated studies) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for labetalol is not available in this evidence pack (data gap DG002). Based on general pharmacological knowledge, labetalol is a combined alpha-1/beta-adrenergic receptor antagonist used for blood pressure control, including in hypertensive emergencies. Malignant renovascular hypertension is a severe, rapidly progressive form of hypertension driven by renal-artery pathology and markedly elevated vascular tone — the pathophysiological domain in which combined alpha/beta-blockade is mechanistically most relevant. This may explain why the TxGNN knowledge graph links labetalol both to this indication and to the closely related "malignant hypertensive renal disease" (identical score 0.9908, adjacent graph rank), suggesting the model is capturing a broader "malignant hypertension" cluster rather than a highly specific signal.

The two supporting literature citations are incidental rather than dedicated studies: one describes labetalol (with minoxidil) used for acute blood pressure control in a case of hallucinogen-induced renal vasculitis presenting as malignant hypertension; the other is a paediatric case report of hyponatremic hypertensive syndrome presenting as malignant hypertension, with no confirmed labetalol use in the abstract provided. The mechanistic rationale is plausible, but it is not yet backed by studies specifically designed to evaluate labetalol in this indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | Case report | The Medical Journal of Australia | Labetalol (with minoxidil) used for acute blood pressure control in a 20-year-old with hallucinogen-induced renal vasculitis and malignant hypertension; prednisone resolved the underlying arteritis |
| [15113447](https://pubmed.ncbi.nlm.nih.gov/15113447/) | 2004 | Case report | BMC Nephrology | Describes hyponatremic hypertensive syndrome (renovascular) presenting as malignant hypertension in an 18-month-old; labetalol use not confirmed in available abstract |

## South Africa Market Information

No SAHPRA registrations are recorded for labetalol in this evidence pack (`total_licenses: 0`; market status: **Not Marketed**). No dosage forms or approved indication text are therefore available to summarise.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials and no SAHPRA market presence for labetalol in South Africa, and the two literature citations are incidental case-report mentions rather than dedicated studies of this indication. Combined with a blocking safety data gap (DG001), the evidence base is currently insufficient to advance beyond hold.

**To proceed, the following is needed:**
- TFDA/SAHPRA-approved PI warnings and contraindications (DG001 — blocking)
- Confirmed mechanism of action (DG002)
- Dedicated clinical or observational studies evaluating labetalol specifically in malignant renovascular hypertension (not incidental mentions)
- Confirmation of SAHPRA registration/import pathway status, since the drug is currently not marketed in South Africa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

