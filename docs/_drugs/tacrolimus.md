---
layout: default
title: Tacrolimus
parent: 僅模型預測 (L5)
nav_order: 420
evidence_level: L5
indication_count: 3
---

# Tacrolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Tacrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

> Tacrolimus is a calcineurin inhibitor internationally approved as a topical treatment for atopic dermatitis (and systemically for organ transplant rejection prophylaxis).
> The TxGNN model predicts it may also be effective for **Seborrheic Dermatitis**,
> with **2 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in South Africa; internationally approved for atopic dermatitis (topical ointment) and organ transplant rejection prophylaxis (systemic) |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, tacrolimus is a calcineurin inhibitor: it blocks calcineurin-dependent dephosphorylation of NF-AT, suppressing T-cell activation and downstream pro-inflammatory cytokine release. In its topical (ointment) form, this action underlies its established efficacy in atopic dermatitis, a T-cell-mediated inflammatory skin disease.

Seborrheic dermatitis shares an inflammatory, T-cell-associated component with atopic dermatitis, and both conditions are commonly managed with topical anti-inflammatory agents on sensitive facial skin. Because topical tacrolimus does not cause skin atrophy — a key limitation of long-term corticosteroid use — it is pharmacologically attractive for chronic, relapsing facial dermatoses that require maintenance therapy.

This mechanistic plausibility is directly supported by real-world use: topical calcineurin inhibitors (tacrolimus and pimecrolimus) have already been studied and used off-label in seborrheic dermatitis for over two decades, including dedicated Phase 3/4 maintenance trials, reinforcing that the TxGNN prediction reflects an area of active, mechanistically coherent clinical practice rather than a purely computational extrapolation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Evaluated tacrolimus ointment (Protopic) for maintenance treatment of severe facial seborrheic dermatitis in adults, aiming to reduce relapse frequency and steroid use |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Assessed whether proactive once/twice-weekly 0.1% tacrolimus ointment maintains remission and reduces exacerbation in adult facial seborrheic dermatitis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33010323](https://pubmed.ncbi.nlm.nih.gov/33010323/) | 2021 | RCT | J Am Acad Dermatol | Multicenter double-blind RCT: tacrolimus 0.1% vs ciclopiroxolamine 1% for maintenance therapy in severe facial seborrheic dermatitis |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Clinical Study | Annals of Dermatology | Maintenance therapy of facial seborrheic dermatitis with 0.1% tacrolimus ointment, extending the atopic dermatitis intermittent-TCI regimen model |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | RCT | Annals of Parasitology | Comparative trial of sertaconazole 2% cream vs tacrolimus 0.03% cream in 60 seborrheic dermatitis patients |
| [12833030](https://pubmed.ncbi.nlm.nih.gov/12833030/) | 2003 | Open-label pilot | J Am Acad Dermatol | 18 patients treated with 0.1% tacrolimus for up to 28 days; 61% achieved complete clearance |
| [37067129](https://pubmed.ncbi.nlm.nih.gov/37067129/) | 2023 | Comparative study | Indian J Dermatol Venereol Leprol | Oral itraconazole + topical tacrolimus vs topical tacrolimus alone for maintenance treatment in Vietnam |
| [39219446](https://pubmed.ncbi.nlm.nih.gov/39219446/) | 2024 | Cochrane SR/Network Meta-Analysis | Clin Exp Allergy | Network meta-analysis of topical anti-inflammatory treatments (including calcineurin inhibitors) for eczema-spectrum disease |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | Reviews pathophysiology, safety, and efficacy of topical calcineurin inhibitors specifically in seborrheic dermatitis |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic Review | Am J Clin Dermatol | Systematic review of topical treatments (antifungals, keratolytics, corticosteroids, TCIs) for facial seborrheic dermatitis |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | Overview of facial seborrheic dermatitis pathogenesis and emerging therapeutic options including TCIs |
| [28685715](https://pubmed.ncbi.nlm.nih.gov/28685715/) | 2017 | Mechanistic/Cohort | Chinese Medical Journal | Investigates Staphylococcus epidermidis colonization and skin barrier impairment in facial seborrheic dermatitis, informing disease mechanism |

---

## South Africa Market Information

Tacrolimus is currently **not registered with SAHPRA** — no marketed products, dosage forms, or approved indication text are available in this evidence pack (0 licenses recorded). As a result, no formulation-specific South African labeling data (e.g., topical ointment strength, EML status) can be reported at this time.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3/4 trials plus a substantial, consistent literature base (including a randomized maintenance-therapy trial) support tacrolimus's efficacy in facial seborrheic dermatitis, and the mechanistic rationale (calcineurin inhibition, low atrophy risk) is well established from its approved atopic dermatitis use. However, tacrolimus is not currently registered in South Africa and drug-level safety/label data are unavailable, so clinical adoption cannot proceed without further regulatory and safety input.

**To proceed, the following is needed:**
- SAHPRA/TFDA-approved Professional Information (warnings, contraindications) — currently a blocking data gap (DG001)
- Confirmed mechanism of action documentation from DrugBank (DG002)
- A regulatory pathway assessment for South African registration, since tacrolimus is not currently marketed locally
- Formal drug interaction (DDI) review, as none is currently on record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

