---
layout: default
title: Meloxicam
parent: 僅模型預測 (L5)
nav_order: 304
evidence_level: L5
indication_count: 10
---

# Meloxicam
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

Using this evidence pack, I need to flag one important judgment call up front: the JSON's `predicted_indications` list is ranked by raw TxGNN score, and rank #1 (`acromesomelic dysplasia, Hunter-Thompson type`, score 99.92%) is explicitly annotated in its own `repurposing_rationale` as a likely **knowledge-graph artifact** with no mechanistic plausibility (Hold/L5). Reporting that as the headline finding would mislead the reader. The only candidate in this pack with real supporting literature, a defensible mechanism, and an evidence-based recommendation is **rank #8 — rheumatoid factor-positive polyarticular Juvenile Idiopathic Arthritis (JIA)** (L2, "Proceed with Guardrails"). I am building the report around that candidate and summarizing the other nine as a rejected-signal appendix, per standard pharmacovigilance/repurposing review practice.

---

# Meloxicam: From NSAID Anti-Inflammatory Use to Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis

## One-Sentence Summary

Meloxicam is a COX-2-preferential NSAID whose original indication data is not captured in this evidence pack, but which is broadly established for osteoarthritis, rheumatoid arthritis, and ankylosing spondylitis pain and inflammation control. Of ten TxGNN-predicted new indications reviewed for Meloxicam, the only one supported by real-world clinical safety literature is **rheumatoid factor-positive polyarticular Juvenile Idiopathic Arthritis (JIA)**, with **1 supporting publication** (a Phase 4 safety registry) and no registered clinical trials specific to this pairing. The nine other top-scoring predictions (mostly rare skeletal dysplasias and genetic syndromes) lack any supporting evidence or mechanistic link and are not recommended for further action.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (data gap — see below); Meloxicam is a publicly established NSAID used for osteoarthritis, rheumatoid arthritis and ankylosing spondylitis |
| Predicted New Indication | Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis (JIA) |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L2 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Meloxicam was not available in this evidence pack (data gap DG002). Based on well-established pharmacological knowledge, Meloxicam is a **COX-2-preferential non-steroidal anti-inflammatory drug (NSAID)**. It inhibits prostaglandin synthesis, reducing the inflammatory mediators responsible for synovial pain, swelling, and stiffness — the core pathology of inflammatory arthritides.

Rheumatoid factor-positive polyarticular JIA shares the same underlying pathophysiology as adult rheumatoid arthritis: synovitis driven by prostaglandin-mediated inflammation across multiple joints. Because Meloxicam's mechanism directly targets this pathway, its applicability to JIA is mechanistically coherent rather than incidental.

Notably, the evidence pack's own rationale indicates that Meloxicam is **already approved in several jurisdictions for JIA in children aged 2 and older**. This means the TxGNN "prediction" in this case largely reflects a real, existing clinical use that was simply absent from the `original_indications` field of this dataset (a data completeness gap) rather than a genuinely novel pharmacological hypothesis. This strengthens confidence in the signal but also means the "new indication" framing should be read as "confirmatory/already-established use," not a speculative repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specific to Meloxicam and rheumatoid factor-positive polyarticular JIA (ClinicalTrials.gov and ICTRP searches returned zero results for this pairing as of the data cutoff).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/) | 2014 | Cohort / Phase 4 safety registry | Pediatric Rheumatology Online Journal | Long-term, real-world safety and developmental outcome data for JIA patients treated with celecoxib or non-selective NSAIDs (including Meloxicam-class agents), supporting an acceptable safety profile for chronic NSAID use in this population. |

---

## South Africa Market Information

No SAHPRA registrations were identified for Meloxicam in this evidence pack (`market_status: 未上市 / Not marketed`, `total_licenses: 0`). Given that Meloxicam is a widely available NSAID internationally, this "not marketed" status should be independently verified against the current SAHPRA product register before any regulatory conclusions are drawn — it may reflect a data-collection gap in this pack rather than true absence from the South African market.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(This evidence pack's `key_warnings`, `contraindications`, and drug-drug interaction fields were all unpopulated — flagged internally as data gap DG001, Blocking severity, because it prevents a formal S1 safety pre-assessment.)*

---

## Other TxGNN Predictions Reviewed (Not Recommended)

For completeness, the remaining nine high-scoring TxGNN predictions for Meloxicam were reviewed and are **not** recommended for further action — each lacks clinical trials, literature, and a credible mechanistic link to Meloxicam's NSAID activity:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Why Rejected |
|------|----------------------|:---:|:---:|------|------|
| 1 | Acromesomelic dysplasia, Hunter-Thompson type | 99.92% | L5 | Hold | Non-inflammatory skeletal dysplasia (GDF5 mutation); likely knowledge-graph artifact |
| 2 | Brachyolmia-amelogenesis imperfecta syndrome | 99.92% | L5 | Hold | Genetic skeletal/dental developmental disorder; no NSAID relevance |
| 3 | Myosclerosis | 99.90% | L5 | Hold | Fibrotic, not inflammatory, muscle pathology |
| 4 | Brachyolmia | 99.89% | L5 | Hold | Genetic skeletal dysplasia; no inflammatory component |
| 5 | Pseudoachondroplasia | 99.81% | L5 | Hold | COMP-gene cartilage disorder; NSAID at most symptomatic, not disease-modifying |
| 6 | Spondyloarthropathy, susceptibility to | 99.52% | L4 | Research Question | Node likely represents genetic *susceptibility*, not active disease — needs TxGNN node semantics clarified before action |
| 7 | Rheumatoid nodulosis | 99.51% | L5 | Hold | Vasculitis/macrophage-driven nodules; not NSAID-responsive |
| 9 | WHIM syndrome | 99.38% | L5 | Hold | Primary immunodeficiency (CXCR4 mutation); no COX-pathway relevance |
| 10 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.36% | L5 | Hold | Congenital malformation syndrome; no inflammatory basis |

This pattern — very high TxGNN scores clustering on rare skeletal/genetic syndromes with no mechanistic or evidentiary support — suggests these reflect structural similarity artifacts in the knowledge graph rather than genuine repurposing signals, and should be deprioritized in favor of the JIA signal above.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Meloxicam's use in rheumatoid factor-positive polyarticular JIA is mechanistically sound, supported by a Phase 4 real-world safety registry, and already reflects existing international regulatory approval for pediatric JIA — this is a data-completeness confirmation more than a novel hypothesis. However, the absence of SAHPRA-specific PI/safety data (DG001, Blocking) and confirmed South African market registration status means it cannot proceed to full clinical guidance without further regulatory verification.

**To proceed, the following is needed:**
- Confirm current SAHPRA registration status for Meloxicam (this pack shows 0 registrations, which should be verified against the live SAHPRA register)
- Obtain SAHPRA-approved Professional Information (PI) — warnings, contraindications, and pediatric dosing for JIA specifically (DG001)
- Obtain formal mechanism-of-action documentation from DrugBank or equivalent source (DG002)
- Clarify whether TxGNN's "spondyloarthropathy, susceptibility to" node (rank 6) represents active disease or genetic risk status before considering it further
- If pursued, define a pediatric rheumatology monitoring plan (renal function, GI tolerability, growth/development) consistent with existing international JIA labeling for Meloxicam
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

