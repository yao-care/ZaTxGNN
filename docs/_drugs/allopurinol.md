---
layout: default
title: Allopurinol
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
---

# Allopurinol
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

# Allopurinol: From Gout and Hyperuricaemia to Hepatic Porphyria

## One-Sentence Summary

Allopurinol is a xanthine oxidase (XO) inhibitor with a long-established international track record in the treatment of gout and hyperuricaemia, though it currently holds no SAHPRA registration in South Africa.
The TxGNN model predicts it may be effective for **Hepatic Porphyria**, with **0 clinical trials** and **2 publications** currently providing indirect mechanistic support.
Evidence remains at the preclinical hypothesis stage (L4), and the prediction — while biochemically plausible — requires dedicated clinical investigation before any translation can be considered.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gout and Hyperuricaemia (internationally established use; no SAHPRA registration on record in this dataset) |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 (preclinical / mechanistic hypothesis only) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Allopurinol and its pharmacologically active metabolite oxypurinol are well-characterised inhibitors of xanthine oxidase (XO), the enzyme that catalyses the terminal steps in purine catabolism — converting hypoxanthine and xanthine to uric acid. By inhibiting XO, allopurinol reduces uric acid production and is the cornerstone treatment for chronic gout and hyperuricaemia worldwide.

The proposed link to acute hepatic porphyria rests on a separate but biochemically related observation: oxypurinol has been shown in vitro to inhibit δ-aminolevulinate synthase 1 (ALAS1), the rate-limiting enzyme of hepatic haem biosynthesis. In acute hepatic porphyrias (AHP), ALAS1 is abnormally induced by triggers such as fasting, hormonal fluctuations, and certain drugs. This induction leads to toxic accumulation of porphyrin precursors — aminolaevulinic acid (ALA) and porphobilinogen (PBG) — which drive the acute neurovisceral attacks characteristic of this disease. If allopurinol suppresses ALAS1 activity, it could theoretically reduce precursor accumulation and attenuate or prevent acute attacks.

However, this mechanistic rationale currently exists entirely at the hypothesis and in vitro level. The shared biochemical substrate (the hepatic haem regulatory pool) provides conceptual coherence, but no dedicated clinical trial or controlled observational study has tested this hypothesis in porphyria patients. The two supporting publications are an expert hypothesis paper (Badawy, 2019) and a rat-liver pharmacology study examining carbamazepine-induced porphyria exacerbation (Morgan & Badawy, 1992) — neither directly demonstrates that allopurinol is effective or safe in human hepatic porphyria.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis / Mechanistic Review | Medical Hypotheses | Proposes that inhibiting haem utilisation by tryptophan 2,3-dioxygenase (TDO) — thereby preserving hepatic regulatory haem — could suppress ALAS1 induction in acute hepatic porphyrias; provides theoretical basis for targeting haem biosynthesis upstream |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Animal Study (rat liver) | Biochemical Pharmacology | Demonstrates that carbamazepine at low oral doses exacerbates haem metabolism in rat liver via depletion of the regulatory haem pool and ALAS induction; establishes a screening model for porphyria exacerbation and contextualises haem pathway sensitivity to drug intervention |

---

## South Africa Market Information

Allopurinol currently has **no registered products** with SAHPRA according to this dataset, and its market status is recorded as **not marketed** in South Africa.

> **Note for clinicians:** Allopurinol appears on the WHO Essential Medicines List (EML) and is registered in multiple high-income and middle-income countries. If this dataset reflects a data retrieval gap rather than a genuine absence of registration, SAHPRA's online medicines register should be consulted directly to confirm current status before any prescribing or procurement decision.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) — or, in the absence of a local registration, the manufacturer's international summary of product characteristics (SmPC) — for full safety information. Report any suspected adverse drug reactions to SAHPRA through the MedSafety reporting system.

> **Known class-level considerations for prescribers** (not sourced from this Evidence Pack; based on established pharmacology):
> Allopurinol is associated with a risk of severe cutaneous adverse reactions (SCAR), including Stevens-Johnson syndrome and toxic epidermal necrolysis, particularly in patients carrying the **HLA-B\*58:01** allele. This allele is prevalent in several South African population groups (especially in individuals of Asian ancestry). Pharmacogenomic screening prior to initiation is strongly recommended in accordance with current CPIC and local guidelines.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.95%), and there is a biochemically coherent — if speculative — mechanistic link between allopurinol's ALAS1-inhibitory properties and the pathophysiology of acute hepatic porphyria. However, the total evidence base consists of two indirect publications (one hypothesis paper, one animal study), zero registered clinical trials, and no human data in porphyria patients. This places the candidate firmly at L4, which is insufficient to support clinical translation without further foundational work.

**To proceed, the following is needed:**

- **Formal MOA confirmation:** Obtain DrugBank or primary literature data on oxypurinol's ALAS1-inhibitory activity, including concentration-response data and comparison with current standard-of-care (givosiran, haem arginate)
- **Dedicated preclinical studies:** In vitro (porphyria cell models) and in vivo (AIP mouse models) studies directly measuring ALA/PBG reduction under allopurinol treatment
- **Safety evaluation in AHP context:** Assessment of hepatotoxicity risk, given that allopurinol itself can cause liver injury and patients with acute porphyria have baseline hepatic vulnerability
- **SAHPRA registration status clarification:** Confirm whether allopurinol is registered in South Africa; if not, identify the regulatory pathway for a repurposing indication
- **HLA-B\*58:01 prevalence data for South African cohorts:** Required for any future clinical trial protocol to stratify pharmacogenomic risk
- **Engagement with South African porphyria patient registries** (e.g., through the South African Porphyria Network) to assess feasibility of a Proof-of-Concept study

---

> ⚠️ **Disclaimer:** This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All predictions should be interpreted in conjunction with qualified clinical and regulatory expertise.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

