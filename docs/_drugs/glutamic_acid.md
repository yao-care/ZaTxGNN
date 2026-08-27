---
layout: default
title: Glutamic Acid
parent: 僅模型預測 (L5)
nav_order: 240
evidence_level: L5
indication_count: 10
---

# Glutamic Acid
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

# Glutamic Acid: From No Registered Indication to Postmenopausal Osteoporosis

## One-Sentence Summary

Glutamic acid (DrugBank DB00142) is a non-essential amino acid that is **not currently registered or marketed in South Africa** and has no documented approved clinical indication in this evidence pack. The TxGNN model predicts it may be effective for **Postmenopausal Osteoporosis**, but this is currently supported by only **1 loosely-related clinical trial** and **11 largely mechanistic/animal publications** — the evidence remains preliminary.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is unmarketed with no registered indication text |
| Predicted New Indication | Postmenopausal Osteoporosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 (preclinical/mechanistic) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for glutamic acid in this evidence pack. Glutamic acid is a naturally occurring, non-essential amino acid involved broadly in nitrogen metabolism, acid-base buffering, and as a precursor to neurotransmitters (e.g., GABA); it has no registered therapeutic indication in South Africa at this time.

The mechanistic rationale for a link to postmenopausal osteoporosis rests on glutamic acid's proposed role as a substrate in acid-base buffering of skeletal tissue and downstream calcium/bone metabolism pathways. An animal study demonstrated that glutamic acid ameliorated estrogen-deficiency menopausal-like symptoms in ovariectomized mice, and a related compound, poly-gamma-glutamic acid, was shown in a small acute human study to enhance calcium absorption in postmenopausal women. Together these findings suggest a plausible, but not yet proven, pathway between glutamic acid and bone metabolism.

Importantly, **no clinical trial or publication in this evidence pack directly tests glutamic acid itself as a treatment for postmenopausal osteoporosis in humans**. The single captured clinical trial evaluates ibandronate (an unrelated bisphosphonate) and was included only via disease-keyword matching. This prediction should therefore be regarded as a research hypothesis rather than a clinically actionable signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00048061](https://clinicaltrials.gov/study/NCT00048061) | Phase 3 | Completed | 1609 | Compared monthly vs. daily oral ibandronate regimens (with calcium/vitamin D) in postmenopausal osteoporosis. **Note:** does not test glutamic acid — captured by disease-keyword match only; relevance graded low (C) by evidence pipeline. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14529146](https://pubmed.ncbi.nlm.nih.gov/14529146/) | 2003 | RCT | The Keio Journal of Medicine | Vitamin D3/K2 treatment sustains lumbar BMD and prevents fractures; mentions vitamin K2 enhances gamma-carboxylation of bone glutamic acid residues. Does not test glutamic acid itself. |
| [14584089](https://pubmed.ncbi.nlm.nih.gov/14584089/) | 2003 | RCT | Yonsei Medical Journal | Combined vitamin K2 + bisphosphonate treatment in postmenopausal osteoporosis; vitamin K2 mechanism involves carboxylation of bone glutamic acid residues. Unrelated drug intervention. |
| [19172219](https://pubmed.ncbi.nlm.nih.gov/19172219/) | 2009 | RCT | Journal of Bone and Mineral Metabolism | Randomized study of menatetrenone (vitamin K2) vs. calcium aspartate on bone turnover markers; unrelated to glutamic acid supplementation. |
| [11668761](https://pubmed.ncbi.nlm.nih.gov/11668761/) | 2001 | Review | Tidsskrift for den Norske Laegeforening | Summary review of vitamin K in Norwegian diet and osteoporosis; not related to glutamic acid. |
| [26144993](https://pubmed.ncbi.nlm.nih.gov/26144993/) | 2015 | Animal study | Nutrition Research | Glutamic acid ameliorated estrogen-deficiency menopausal-like symptoms in ovariectomized mice — the most directly relevant preclinical evidence for this drug. |
| [18187428](https://pubmed.ncbi.nlm.nih.gov/18187428/) | 2007 | Human physiological trial | Journal of the American College of Nutrition | Poly-gamma-glutamic acid (related compound) acutely increased calcium absorption in postmenopausal women. |
| [40950804](https://pubmed.ncbi.nlm.nih.gov/40950804/) | 2025 | Cohort/Metabolomic | Journal of Diabetes and Metabolic Disorders | Explored amino acid profiles, aging, and sex hormone interactions in elderly patients; general metabolomic association, not an intervention study. |
| [29437025](https://pubmed.ncbi.nlm.nih.gov/29437025/) | 2018 | Genetic association | Endocrine, Metabolic & Immune Disorders Drug Targets | Studied VKORC1 polymorphism (vitamin K pathway) and osteoporosis risk; mentions glutamic acid residues only as an enzymatic substrate concept. |
| [34529430](https://pubmed.ncbi.nlm.nih.gov/34529430/) | 2021 | Preclinical (drug delivery) | Nano Letters | Bone-targeting polymer vesicle using a poly-glutamic-acid-based copolymer for estradiol delivery; glutamic acid used as a delivery scaffold, not as active agent. |
| [39698319](https://pubmed.ncbi.nlm.nih.gov/39698319/) | 2024 | Animal/mechanistic | Frontiers in Cellular and Infection Microbiology | Investigated a traditional ointment's effect via gut microbiota-bone metabolism axis in postmenopausal osteoporosis; unrelated to glutamic acid. |

---

## South Africa Market Information

Glutamic acid has **no SAHPRA registrations on record** (0 licenses, market status: Not Marketed). No dosage form, brand name, or approved indication text is available for South Africa.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L4 (preclinical/mechanistic only) — the prediction is supported by animal studies and studies of related-but-distinct compounds (vitamin K2, poly-gamma-glutamic acid), with no human interventional trial testing glutamic acid itself for postmenopausal osteoporosis. The drug is also unregistered and unmarketed in South Africa, and core safety data (warnings, contraindications, DDI) are entirely unavailable (flagged as a **Blocking** data gap).

**To proceed, the following is needed:**
- SAHPRA-equivalent professional information (PI) covering warnings, contraindications, and drug interactions (Blocking gap — required before any S1 safety assessment)
- Documented mechanism of action (MOA) data from DrugBank or equivalent source (High-priority gap — needed for mechanistic relevance analysis)
- A dedicated human interventional/RCT evaluating glutamic acid (not related compounds) for bone health outcomes in postmenopausal women
- Confirmation of registration pathway/status should market entry to South Africa be considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

