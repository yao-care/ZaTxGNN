---
layout: default
title: Zinc Sulfate
parent: 僅模型預測 (L5)
nav_order: 469
evidence_level: L5
indication_count: 4
---

# Zinc Sulfate
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

# Zinc Sulfate: From Nutritional Supplementation to Pharyngitis

## One-Sentence Summary

> Zinc Sulfate does not have a South Africa-registered original indication in this evidence pack (SAHPRA registration status: 0 licenses, market status: not marketed); it is generally recognised as a trace-element/mineral supplement used for zinc deficiency and adjunctive care of mucosal/upper-respiratory conditions.
> The TxGNN model predicts it may be effective for **Pharyngitis**,
> with **4 clinical trials** and **3 publications** currently supporting this direction, though only one trial (postoperative sore throat) directly targets a pharyngitis-like endpoint.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — Zinc Sulfate is not currently SAHPRA-registered and no original indication is recorded in this evidence pack |
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L2 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Zinc Sulfate in this evidence pack. Based on known pharmacological information, zinc ions applied locally to the pharyngeal mucosa are understood to have astringent, anti-inflammatory, and immunomodulatory effects. Zinc lozenges have been studied for their ability to inhibit rhinovirus replication and reduce inflammatory cytokines, and are clinically used to shorten the course of the common cold and sore throat.

However, the supporting evidence largely comes from trials designed around **COVID-19 treatment/prevention** or **postoperative sore throat**, rather than general (typically viral) pharyngitis as a primary endpoint. This means the mechanistic link to pharyngitis is a reasonable extrapolation rather than direct, disease-specific evidence — the strongest single study (a randomized, double-blind trial of zinc lozenges for postoperative sore throat syndrome, n=87) supports symptomatic benefit in a related but distinct clinical context.

Because no original indication or SAHPRA registration exists for this drug in the current dataset, the case for repurposing rests entirely on general pharmacological plausibility plus trial evidence in adjacent conditions (sore throat, radiation-induced oropharyngeal mucositis), rather than on an established indication-to-indication mechanistic bridge.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02405832](https://clinicaltrials.gov/study/NCT02405832) | N/A | Completed | 87 | Randomized, double-blind, placebo-controlled trial of preoperative oral zinc lozenges for prevention of postoperative sore throat syndrome; directly relevant to pharyngeal symptoms (Relevance grade A) |
| [NCT04446104](https://clinicaltrials.gov/study/NCT04446104) | Phase 3 | Completed | 4257 | Randomized prophylaxis trial (DORM Trial) among migrant workers at high risk of COVID-19; large sample but primary endpoint is infection prevention, not pharyngitis symptoms (Relevance grade B) |
| [NCT04370782](https://clinicaltrials.gov/study/NCT04370782) | Phase 4 | Completed | 18 | Hydroxychloroquine + zinc with azithromycin or doxycycline for outpatient COVID-19; zinc effect not isolated, very small sample (Relevance grade C) |
| [NCT04621461](https://clinicaltrials.gov/study/NCT04621461) | Phase 4 | Completed | 3 | Randomized, placebo-controlled trial of zinc for outpatient COVID-19; enrollment far below target, likely terminated early (Relevance grade C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38693477](https://pubmed.ncbi.nlm.nih.gov/38693477/) | 2024 | RCT | BMC Anesthesiology | Preoperative zinc, magnesium, and budesonide gargles compared for reducing incidence/severity of postoperative sore throat (POST) after endotracheal intubation |
| [23720981](https://pubmed.ncbi.nlm.nih.gov/23720981/) | 2013 | RCT | Journal of the Medical Association of Thailand | Randomized, double-blind, placebo-controlled trial of zinc sulfate for alleviating radiation-induced oral mucositis and pharyngitis in head and neck cancer patients |
| [20123362](https://pubmed.ncbi.nlm.nih.gov/20123362/) | 2010 | Case series | Oral Surgery, Oral Medicine, Oral Pathology, Oral Radiology, and Endodontics | Discusses long-lasting post-tonsillectomy dysgeusia, noting a proposed but unconfirmed role for dietary zinc deficiency in its pathogenesis |

---

## South Africa Market Information

Zinc Sulfate currently has **0 SAHPRA registrations** and is **not marketed** in South Africa. No product listings, registration numbers, or approved indication text are available in this evidence pack.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Note:** A Blocking-severity data gap (DG001) was identified — TFDA/SAHPRA-equivalent label warnings and contraindications were not retrievable, which prevents completion of the initial safety screening (S1) stage for this candidate. This must be resolved before any clinical guardrails can be defined.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The strongest supporting evidence (postoperative sore throat RCTs) is adjacent to, not directly aligned with, general pharyngitis, and no SAHPRA registration or original indication exists to anchor a repurposing comparison. A Blocking data gap on label warnings/contraindications also prevents a safety determination.

**To proceed, the following is needed:**
- Product label / Professional Information (PI) warnings, precautions, and contraindications (DG001, Blocking)
- Mechanism of action (MOA) data from DrugBank or equivalent source (DG002, High)
- A trial or systematic review with pharyngitis (rather than sore throat/COVID-19) as the primary endpoint
- Clarification of intended route/formulation and SAHPRA registration pathway, since the drug is currently unmarketed in South Africa

*Note: Three additional TxGNN-predicted indications for this drug (nasal cavity disease, acute laryngopharyngitis, congenital prothrombin deficiency) were also evaluated. Nasal cavity disease was flagged as a likely false positive — supporting literature describes zinc's **ototoxic/neurotoxic** effect on olfactory tissue (used experimentally to *induce* anosmia), not a therapeutic effect. Congenital prothrombin deficiency had no supporting evidence at all (L5, Hold). These are noted for completeness but were excluded from the main report as pharyngitis represents the top-ranked and best-evidenced candidate.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

