---
layout: default
title: Framycetin
parent: 僅模型預測 (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
---

# Framycetin
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

# Framycetin: From Topical Antibacterial Use to Sclerosing Cholangitis

## One-Sentence Summary

Framycetin is an aminoglycoside antibiotic historically restricted to topical use (eye, ear, and skin infections) because of its high ototoxicity and nephrotoxicity risk when given systemically. The TxGNN model predicts a possible association with **Sclerosing Cholangitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags it as likely model noise.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no SAHPRA registration or DrugBank indication text available); background pharmacology points to topical antibacterial use in eye, ear, and skin infections |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for framycetin is not available in this evidence pack (flagged as data gap DG002, High severity). Based on the information that is available, framycetin is an aminoglycoside antibiotic that binds the bacterial 30S ribosomal subunit to inhibit protein synthesis, giving it activity against many aerobic gram-negative organisms. Clinically, its use has historically been limited to topical formulations (ophthalmic, otic, dermatological) because systemic administration carries a high risk of ototoxicity and nephrotoxicity.

Sclerosing cholangitis is a chronic, autoimmune/fibrotic biliary disease with no established infectious or antibacterial etiology. The evidence pack's own mechanistic assessment concludes there is no direct biological link between framycetin's ribosome-inhibition mechanism and biliary fibrosis, and explicitly classifies this specific prediction as likely statistical noise from the TxGNN model rather than a biologically grounded hypothesis. No clinical trials or literature records were returned for this drug–disease pair (query log entries #2–#4), reinforcing that the signal is model-only.

For context, of the ten candidates TxGNN generated for framycetin, only urinary tract infection (rank 2, score 99.42%, evidence level L4, one supporting PubMed record) and bronchitis (rank 8, evidence level L3, one supporting PubMed record) carry any literature evidence at all, and both are staged as "Research Question" rather than "Hold." This reflects that framycetin's antibacterial mechanism has some plausible — if historical and toxicity-limited — relevance to bacterial infections, but none to sclerosing cholangitis.

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov and ICTRP both returned 0 results for framycetin + sclerosing cholangitis).

## Literature Evidence

Currently no related literature available (PubMed returned 0 results for framycetin + sclerosing cholangitis).

## South Africa Market Information

Framycetin currently holds no SAHPRA registrations and is not marketed in South Africa (0 licenses on record). No product-level registration data is available for this evidence pack.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*Additional context from the repurposing rationale (not formal safety data):* aminoglycosides as a class, including framycetin, carry well-known risks of ototoxicity and nephrotoxicity with systemic exposure — the reason clinical use has historically been confined to topical routes. Data gap DG001 (Blocking: PI warnings/contraindications) must be resolved before any formal safety evaluation (Stage S1) can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 (model prediction only) — zero clinical trials and zero publications support a framycetin–sclerosing cholangitis link, and the evidence pack's own mechanistic review judges the pairing as likely model noise given the absence of any biological connection between an antibacterial mechanism and an autoimmune/fibrotic biliary disease.
- Framycetin has no current SAHPRA registration in South Africa, and a Blocking data gap (DG001: PI warnings/contraindications) prevents even a preliminary safety review.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain SAHPRA-approved PI labeling for warnings and contraindications
- Resolve DG002 (High): obtain confirmed mechanism-of-action data from DrugBank
- If continuing to investigate framycetin repurposing, redirect focus to the higher-plausibility candidates in this evidence pack — urinary tract infection (rank 2, L4) and bronchitis (rank 8, L3) — which have at least limited historical literature support
- No further action recommended for the sclerosing cholangitis indication absent new mechanistic or clinical evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

