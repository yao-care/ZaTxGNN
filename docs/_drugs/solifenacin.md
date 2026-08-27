---
layout: default
title: Solifenacin
parent: 僅模型預測 (L5)
nav_order: 413
evidence_level: L5
indication_count: 10
---

# Solifenacin
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

# Solifenacin: From Overactive Bladder to Polycystic Kidney Disease 3 (with or without Polycystic Liver Disease)

## One-Sentence Summary

> Solifenacin is a selective M3 muscarinic receptor antagonist established for overactive bladder (OAB), identified from the literature within this evidence pack (no South African product-label text is available, as the drug is not currently marketed here).
> The TxGNN model's top-ranked prediction is that it may be effective for **Polycystic Kidney Disease 3, with or without Polycystic Liver Disease**,
> but this ranking is supported by **0 clinical trials** and **20 publications that describe the disease itself, not solifenacin's use in it** — the evidence pack's own analysis flags this as a likely knowledge-graph topology artefact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Overactive bladder (OAB) — identified from literature within this evidence pack; no South African/SAHPRA product-label text available (see Market Status below) |
| Predicted New Indication | Polycystic Kidney Disease 3, with or without Polycystic Liver Disease |
| TxGNN Prediction Score | 97.13% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for solifenacin is not available in this evidence pack (flagged internally as a High-severity data gap, DG002). Based on generally established pharmacology, solifenacin is a selective M3 muscarinic receptor antagonist that relaxes detrusor smooth muscle, which is the basis of its use in overactive bladder.

Polycystic Kidney Disease 3 (with or without polycystic liver disease) is a genetic ciliopathy in which cyst growth is driven by cAMP-dependent signalling in renal tubular and cholangiocyte epithelium — a pathway unrelated to bladder detrusor contractility. None of the 20 literature results returned for this pairing discuss solifenacin, muscarinic antagonism, or cAMP-cystogenesis; they are disease-overview reviews and guidelines about PKD/PLD genetics, diagnosis, and management (e.g., ADPKD genetics, EASL cystic liver disease guidelines).

The evidence pack's own rationale is explicit on this point: the high TxGNN score most likely reflects the topological proximity of urinary- and renal-system nodes in the knowledge graph, rather than a real pharmacological relationship. This mechanistic implausibility, combined with the complete absence of drug-specific trials or literature, is why this candidate is scored L4 and recommended for **Hold** rather than active development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38958301](https://pubmed.ncbi.nlm.nih.gov/38958301/) | 2024 | Guideline | Am J Gastroenterol | ACG guideline on focal liver lesions, including management of polycystic liver disease; does not discuss solifenacin |
| [30819518](https://pubmed.ncbi.nlm.nih.gov/30819518/) | 2019 | Review | Lancet | Overview of ADPKD genetics, clinical manifestations (renal cysts, liver cysts, hypertension); no drug-therapy discussion relevant to solifenacin |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | ADPKD/PCLD clinical course; notes tolvaptan (a vasopressin-receptor antagonist, not solifenacin) as an approved ADPKD therapy |
| [29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) | 2018 | Review | J Am Soc Nephrol | Genetic complexity and causative genes (PKD1, PKD2, PRKCSH, SEC63, GANAB) of ADPKD/ADPLD |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Review | Adv Kidney Dis Health | Genetic spectrum and phenotypes of polycystic kidney and liver disease |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Clinical Practice Guideline | J Hepatol | EASL guideline on diagnosis and management of cystic liver diseases |
| [28375157](https://pubmed.ncbi.nlm.nih.gov/28375157/) | 2017 | Genetic study | J Clin Invest | Whole-exome sequencing identifying isolated PCLD genes and polycystin-1 pathway effectors |
| [34034501](https://pubmed.ncbi.nlm.nih.gov/34034501/) | 2022 | Review | Rev Esp Enferm Dig | Diagnosis and management of hepatic hydatid cyst (a differential diagnosis, not PKD/PLD treatment) |
| [36047551](https://pubmed.ncbi.nlm.nih.gov/36047551/) | 2022 | Review | Rev Med Suisse | Overview of polycystic liver disease subtypes and clinical course |
| [37266470](https://pubmed.ncbi.nlm.nih.gov/37266470/) | 2023 | Case report | Maedica | Case of ADPKD/polycystic liver disease co-occurring with gastric cancer |

None of the above publications evaluate solifenacin, and none support a treatment rationale for this indication.

---

## South Africa Market Information

Solifenacin is currently **not marketed** in South Africa: **0 SAHPRA registrations** are on record in this evidence pack, so no registered product name, dosage form, or approved-indication text is available for South Africa.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

(Note: retrieval of TFDA/SAHPRA-equivalent label warnings and contraindications is flagged internally as a **Blocking** data gap — this must be resolved before any safety pre-assessment can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The 97.13% TxGNN score for Polycystic Kidney Disease 3 is not supported by any drug-specific clinical trial or literature evidence; the pack's own analysis attributes the score to knowledge-graph topological proximity rather than a plausible pharmacological mechanism.
- Separately, this same evidence pack contains a substantially stronger candidate for solifenacin repurposing — **"low compliance bladder" (rank 7)**, evidence level L2, with a Phase 4 trial and multiple RCTs directly evaluating antimuscarinic therapy (including solifenacin) for neurogenic/low-compliance bladder, a mechanistically direct extension of its OAB indication, scored "Proceed with Guardrails." That candidate merits prioritized review ahead of this one.

**To proceed, the following is needed:**
- Preclinical or mechanistic evidence directly linking M3 muscarinic antagonism to cAMP-driven cystogenesis in PKD3/PLD before this candidate can be re-scored above L4
- SAHPRA-equivalent Professional Information (PI) — warnings and contraindications (Blocking gap, DG001)
- Confirmed original indication and mechanism-of-action documentation for solifenacin (DG002)
- Verification of South Africa registration status, given 0 SAHPRA licenses are currently on record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

