---
layout: default
title: Nicotinamide
parent: 僅模型預測 (L5)
nav_order: 332
evidence_level: L5
indication_count: 10
---

# Nicotinamide
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

# Nicotinamide: From an Undocumented Original Indication to Werner Syndrome (NAD+ Depletion)

## One-Sentence Summary

> This evidence pack does not record an original approved indication or mechanism of action for nicotinamide (Vitamin B3 amide), and it is currently **not marketed** in South Africa. Of the 10 TxGNN-predicted indications reviewed, the highest-scoring candidate ("elevated plasma zinc") is flagged by the evidence itself as a likely model artifact with no supporting rationale, so this report instead focuses on **Werner syndrome**, the candidate with the strongest biological and clinical grounding — **1 relevant published RCT** and **7 supporting mechanistic/review papers**, but **no registered clinical trials** to date.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no original indications or MOA recorded) |
| Predicted New Indication | Werner Syndrome (NAD+-depletion-driven premature aging) |
| TxGNN Prediction Score | 88.61% (rank 36,492) |
| Evidence Level | L3 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for this specific drug record is not available. Based on established pharmacology, nicotinamide is the amide form of Vitamin B3 (niacin) and functions as a precursor for NAD+/NADH and NADP+/NADPH synthesis via the salvage pathway — a role directly relevant to the Werner syndrome hypothesis below.

Werner syndrome is a rare hereditary progeroid condition caused by WRN helicase mutations. Published mechanistic work shows that WRN-deficient cells and patient samples exhibit depleted mitochondrial NAD+, impaired mitophagy, and accelerated senescence. Since nicotinamide is a direct metabolic precursor of NAD+, restoring NAD+ pools is a biologically coherent strategy for this disease — and a 2025 double-blind, randomized, placebo-controlled crossover trial reported benefit from **nicotinamide riboside** (a related but chemically distinct NAD+ precursor, not nicotinamide itself) in Werner syndrome patients.

**Important caveat:** the clinical trial evidence supporting this hypothesis was conducted with nicotinamide riboside, not nicotinamide. Both are NAD+ precursors but differ in bioavailability, metabolism, and dosing, so the RCT result cannot be assumed to transfer directly to nicotinamide without dedicated study. Note also that TxGNN's single highest-scoring prediction for this drug ("elevated plasma zinc," 97.83%) was excluded from this report — the evidence pack's own analysis identifies it as a likely semantic mis-linkage within a "micronutrient" concept cluster, with no supporting trials or literature and several retrieved trials explicitly contradicting the direction of the hypothesis (zinc *deficiency* prevention, not elevation).

---

## Clinical Trial Evidence

Currently no related clinical trials registered for nicotinamide in Werner syndrome.

*(A relevant randomized controlled trial exists in the published literature — see below — but tested nicotinamide riboside, not nicotinamide, and is not a registered trial record in this evidence pack.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40459998](https://pubmed.ncbi.nlm.nih.gov/40459998/) | 2025 | RCT | Aging Cell | Double-blind randomized crossover placebo-controlled trial of nicotinamide riboside (an NAD+ precursor related to nicotinamide) in Werner syndrome patients; NAD+ depletion implicated in disease pathogenesis, supplementation reported to be beneficial |
| [31754102](https://pubmed.ncbi.nlm.nih.gov/31754102/) | 2019 | Preclinical/Mechanistic | Nature Communications | NAD+ augmentation restores mitophagy and limits accelerated aging in Werner syndrome patient cells and animal models |
| [24757718](https://pubmed.ncbi.nlm.nih.gov/24757718/) | 2014 | Mechanistic | Aging Cell | Loss of WRN protein induces a metabolic shift compromising redox homeostasis, linking WRN deficiency to NAD+/redox pathways |
| [40179319](https://pubmed.ncbi.nlm.nih.gov/40179319/) | 2025 | Mechanistic | Aging | Decreased mitochondrial NAD+ in WRN-deficient cells linked to dysfunctional proliferation |
| [38184705](https://pubmed.ncbi.nlm.nih.gov/38184705/) | 2024 | Mechanistic | Cell & Bioscience | WRN loss accelerates abnormal adipocyte metabolism in Werner syndrome models |
| [34201700](https://pubmed.ncbi.nlm.nih.gov/34201700/) | 2021 | Review | Int J Mol Sci | DNA damage-induced neurodegeneration in accelerated ageing diseases including Werner syndrome |
| [33353663](https://pubmed.ncbi.nlm.nih.gov/33353663/) | 2021 | Review | J Investigative Dermatology | Skin abnormalities in DNA repair/premature aging/mitochondrial dysfunction disorders |

*One additional PubMed result (PMID 13469243) was excluded from this table — it matched on the author surname "Werner," not on Werner syndrome, and is unrelated (a 1957 cardiac arrhythmia case report).*

---

## South Africa Market Information

Nicotinamide currently has no SAHPRA registrations recorded (0 licenses; market status: Not Marketed). Any use in South Africa would require either a new SAHPRA registration application or access via SAHPRA's Section 21 (named-patient) mechanism.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Key warnings, contraindications, and drug-interaction data were not available in this evidence pack — this is flagged internally as a Blocking data gap.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking-severity data gap exists — no SAHPRA/TFDA-equivalent Professional Information (warnings, contraindications) is available for nicotinamide, which prevents even a preliminary safety assessment.
- The Werner syndrome hypothesis is mechanistically coherent and supported by one RCT, but that RCT used nicotinamide riboside, not nicotinamide — the evidence does not yet directly establish efficacy for this specific drug.
- The drug is not currently marketed in South Africa, adding a regulatory access step regardless of the evidence outcome.

**To proceed, the following is needed:**
- Official Professional Information / PI for nicotinamide (warnings, contraindications, interactions) — currently a blocking gap
- Formal mechanism-of-action documentation specific to nicotinamide (not the riboside analog)
- A study or pharmacological bridging analysis comparing nicotinamide vs. nicotinamide riboside NAD+-repletion efficacy in Werner syndrome
- Given Werner syndrome's rarity, engagement with rare-disease/orphan-drug regulatory pathways and specialist clinical input before any patient-facing use
- Clarification of the SAHPRA access route (new registration vs. Section 21) given current "Not Marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

