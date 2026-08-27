---
layout: default
title: Temozolomide
parent: 僅模型預測 (L5)
nav_order: 426
evidence_level: L5
indication_count: 2
---

# Temozolomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Temozolomide: An Already-Established Agent Confirmed for Adult Astrocytic Tumour

## One-Sentence Summary

> Temozolomide is an oral alkylating agent within the imidazotetrazine class. The TxGNN model predicts high relevance to **Adult Astrocytic Tumour** (glioblastoma / anaplastic astrocytoma), a link supported by **2 clinical trials** and **20 publications**, including multiple landmark Phase 3 RCTs (e.g. the Stupp protocol) that have already made temozolomide the global standard of care for this tumour type. This is best understood as **evidence confirming an established indication** rather than a novel repurposing signal — the evidence pack does not record a distinct "original indication" for temozolomide, and the literature shows the predicted indication essentially overlaps with its long-standing clinical use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured as structured data in this evidence pack; literature indicates temozolomide is already an established chemotherapy for glioblastoma/anaplastic astrocytoma |
| Predicted New Indication | Adult Astrocytic Tumour |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 |
| South Africa Market Status | Not marketed (unregistered) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Mechanism-of-action data was not returned from DrugBank for this evidence pack, but the accompanying repurposing rationale supplies the relevant pharmacology: temozolomide is an oral imidazotetrazine DNA-alkylating agent that crosses the blood–brain barrier and methylates guanine at the O6 position of DNA. Failure of DNA mismatch repair to resolve this lesion triggers apoptosis in tumour cells.

This mechanism is the pharmacological basis of the Stupp protocol — concomitant and adjuvant temozolomide with radiotherapy — which has been the global standard of care for newly diagnosed glioblastoma since the 2005 NEJM trial (PMID 15758009) and remains supported by numerous subsequent Phase 3 trials. Because "adult astrocytic tumour" (which includes glioblastoma and anaplastic astrocytoma) is precisely the tumour category temozolomide was developed and approved for elsewhere, the TxGNN signal here reflects a well-established, mechanistically direct relationship rather than an exploratory cross-indication hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | Completed | 500 | Randomised trial comparing temozolomide alone vs. PCV (procarbazine, lomustine, vincristine) in recurrent WHO Grade III/IV astrocytic tumours |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | Completed | 26 | Dose-finding study of cabozantinib (XL184) combined with temozolomide and radiotherapy in newly diagnosed glioblastoma; temozolomide used as a co-administered standard-of-care backbone, not the primary study drug |

No South African National Clinical Trials Register (SANCTR) or Pan African Clinical Trials Registry (PACTR) entries were returned in this evidence pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | RCT | N Engl J Med | Landmark Stupp trial: radiotherapy plus concomitant/adjuvant temozolomide improves survival over radiotherapy alone in glioblastoma |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | RCT (5-year follow-up) | Lancet Oncol | EORTC-NCIC trial 5-year analysis confirms durable survival benefit of temozolomide + radiotherapy |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | RCT (CeTeG/NOA-09) | Lancet | Lomustine-temozolomide combination superior to temozolomide alone in MGMT-methylated glioblastoma |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | RCT | JAMA | Tumor-Treating Fields plus temozolomide improves survival vs. temozolomide alone in glioblastoma maintenance therapy |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | RCT (AVAglio) | N Engl J Med | Bevacizumab added to temozolomide/radiotherapy in newly diagnosed glioblastoma |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | RCT (NOA-08) | Lancet Oncol | Temozolomide alone vs. radiotherapy alone in elderly patients with malignant astrocytoma |
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | RCT (NRG Oncology BN007) | J Clin Oncol | Dual immune checkpoint blockade evaluated alongside temozolomide-based regimens in MGMT-unmethylated glioblastoma |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Review | JAMA | Overview of glioblastoma and other primary brain malignancies in adults, including temozolomide-based standard of care |
| [25920709](https://pubmed.ncbi.nlm.nih.gov/25920709/) | 2015 | Review | J Neurooncol | Radiotherapy and temozolomide outcomes in anaplastic astrocytic gliomas |
| [41345097](https://pubmed.ncbi.nlm.nih.gov/41345097/) | 2025 | Phase Ib/II trial (GEINO 1602) | Nat Commun | Glasdegib combined with temozolomide/radiotherapy in newly diagnosed glioblastoma |

---

## South Africa Market Information

Temozolomide has **0 SAHPRA registrations** on record in this evidence pack and market status is **not marketed**. No product registration table can be generated at this time; this must be confirmed directly against the SAHPRA product register before any clinical planning proceeds.

---

## Cytotoxicity

Temozolomide is an antineoplastic alkylating agent (imidazotetrazine class), used for a malignant tumour indication, so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — alkylating agent (imidazotetrazine class) |
| Myelosuppression Risk | Please refer to the Professional Information (PI) warnings and precautions — no drug-specific toxicity data was returned in this evidence pack |
| Emetogenicity Classification | Please refer to the Professional Information (PI) warnings and precautions |
| Monitoring Items | Full blood count with differential and platelets, liver and renal function — confirm exact schedule against the PI |
| Handling Protection | Standard cytotoxic drug handling precautions apply; confirm against institutional protocol and the PI |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic and clinical evidence for temozolomide in astrocytic tumours is exceptionally strong (L1, multiple completed Phase 3 RCTs), but the drug is currently unregistered in South Africa and the evidence pack has two data gaps: TFDA/PI-equivalent warnings and contraindications (Blocking) and confirmed mechanism-of-action documentation (High). These gaps must close before a formal safety review (S1) can proceed, even though clinical efficacy evidence is not in question.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI), including warnings, contraindications, and drug interaction data
- Confirmation of DrugBank-sourced mechanism-of-action documentation
- SAHPRA registration/import pathway status for temozolomide in South Africa
- Clarification of the originally approved indication, since this was not captured as structured data in the evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

