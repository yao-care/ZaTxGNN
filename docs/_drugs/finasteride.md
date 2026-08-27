---
layout: default
title: Finasteride
parent: 僅模型預測 (L5)
nav_order: 226
evidence_level: L5
indication_count: 6
---

# Finasteride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using the drug-repurposing evaluation report format supplied in the system prompt to structure this response.

**Note on methodology before the report:** The evidence pack's own `repurposing_rationale` fields flag ranks 1, 3, 4, 5, 6 (Ambras hypertrichosis, periodontal malformation, Dandy-Walker syndrome, hair shaft abnormality, trichomegaly) as likely **TxGNN knowledge-graph embedding artifacts** — no mechanistic link to finasteride's DHT pathway and zero supporting trials/literature (evidence level L5, Hold). Rank 2 ("hypertrichosis (disease)") is the only candidate with a coherent mechanism *and* actual literature/trial hits. As the report should not headline noise, this report is built around **rank 2** rather than the raw top-ranked (but non-credible) prediction.

---

# Finasteride: From Androgenetic Alopecia to Hypertrichosis

## One-Sentence Summary

> Finasteride is a 5α-reductase inhibitor used to treat androgen-dependent hair loss (androgenetic alopecia).
> Of the six TxGNN-predicted indications in this evidence pack, only **Hypertrichosis** (rank 2, score **99.99%**) has a biologically coherent mechanism and any supporting evidence base — **1 clinical trial** and **4 publications** — though none directly test finasteride in this indication. The other five top-ranked predictions were screened out as likely false-positive knowledge-graph associations.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Androgenetic alopecia (male pattern hair loss) — not confirmed via South Africa regulatory filings (see below) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on well-established pharmacology referenced within the pack's own literature (e.g. PMID 12942187), finasteride is a 5α-reductase inhibitor that blocks conversion of testosterone to dihydrotestosterone (DHT). It is used clinically for androgen-dependent hair conditions — reducing DHT-driven follicular miniaturisation in androgenetic alopecia.

Hypertrichosis and androgenetic alopecia sit at opposite ends of the same hair-growth axis, and the mechanistic case is only partial: per the evidence pack's own literature (PMID 12223963), most adult hypertrichosis is **not** androgen-dependent — it is iatrogenic (minoxidil, ciclosporine, diazoxide, glucocorticoids), metabolic (porphyria), nutritional, or paraneoplastic. A DHT-lowering drug would plausibly help only the androgen-dependent subset (i.e., hirsutism-type presentations), not hypertrichosis broadly. This is why the evidence level is capped at L4 (mechanism-only) rather than higher.

The other five TxGNN top predictions in this pack (Ambras syndrome, periodontal malformation syndrome, Dandy-Walker malformation, isolated hair shaft abnormality, familial trichomegaly) were reviewed and excluded from this report: each is annotated in the source data as having no plausible mechanistic link to DHT/5α-reductase biology, no supporting trials, and no supporting literature — consistent with knowledge-graph node-proximity noise rather than a genuine repurposing signal.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04293822](https://clinicaltrials.gov/study/NCT04293822) | Phase 4 | Unknown | 60 | Compares topical cetirizine gel vs. minoxidil 5% gel for androgenetic alopecia (AGA). **Note:** does not investigate finasteride and does not study hypertrichosis — flagged in the source data as relevance grade C (low relevance), included only via disease-node proximity. |

No SANCTR or PACTR-registered trials were identified in this evidence pack.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12942187](https://pubmed.ncbi.nlm.nih.gov/12942187/) | 2003 | Review | Der Hautarzt | Notes finasteride's established use in male pattern hair loss alongside laser hair removal for hypertrichosis/hirsutism — the strongest textual link between finasteride and this indication class, but does not report direct finasteride trial data for hypertrichosis. |
| [12223963](https://pubmed.ncbi.nlm.nih.gov/12223963/) | 2002 | Review | Annales de Dermatologie et de Vénéréologie | Distinguishes hypertrichosis (non-androgen-dependent) from hirsutism (androgen-dependent); indicates hormonal-mechanism drugs are relevant mainly to the hirsutism subset. |
| [10330884](https://pubmed.ncbi.nlm.nih.gov/10330884/) | 1999 | Review | Therapeutische Umschau | General review of treatment options for androgenetic alopecia and hirsutism, including oral therapy for male pattern hair loss. |
| [12444520](https://pubmed.ncbi.nlm.nih.gov/12444520/) | 2002 | Review | Der Hautarzt | Describes TrichoScan, a digital hair-analysis tool for monitoring hair-loss treatment response; methodological reference, not disease-specific evidence. |

## South Africa Market Information

Finasteride currently has **no SAHPRA registrations** in this evidence pack (`market_status: 未上市` / Not marketed, `total_licenses: 0`). No product listings, dosage forms, or approved indication text are available to summarise.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: this evidence pack flags PI warnings/contraindications as a Blocking data gap (DG001) — this must be resolved before any safety assessment can proceed.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No direct clinical or literature evidence tests finasteride in hypertrichosis or hirsutism specifically — the single trial identified doesn't use finasteride, and all four literature hits are indirect/contextual reviews (evidence level L4, mechanism-only).
- Finasteride is not currently marketed in South Africa (0 SAHPRA registrations), and PI-based safety data is a documented Blocking gap (DG001), so a formal safety review (S1) cannot be completed yet.

**To proceed, the following is needed:**
- SAHPRA/TFDA-approved Professional Information (warnings, contraindications) to close the Blocking safety gap
- Confirmed original indication and mechanism-of-action documentation (currently marked Data Gap)
- A direct interventional study of finasteride specifically in androgen-dependent hypertrichosis or hirsutism, rather than androgenetic alopecia alone
- Assessment of regulatory pathway/route feasibility if pursuing South African market entry for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

