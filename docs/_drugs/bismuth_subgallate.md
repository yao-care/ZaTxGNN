---
layout: default
title: Bismuth Subgallate
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
---

# Bismuth Subgallate
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

# Bismuth Subgallate: From Gastrointestinal Astringent to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Bismuth subgallate is a bismuth(III) salt of gallic acid, traditionally used as a gastrointestinal astringent, topical haemostatic agent, and internal deodorant for ostomy patients — with no registered indication in South Africa. The TxGNN model's top-ranked prediction is **Heparin Cofactor 2 Deficiency** (score: 98.16%); however, this prediction lacks any known mechanistic basis and is likely a knowledge graph topology artefact. Among all 10 predicted indications, **Peptic Ulcer Disease** (rank 10) presents the strongest evidence base, supported by **3 publications** and a plausible mechanistic rationale rooted in bismuth's anti-*H. pylori* and mucosal-protective properties — though direct studies on bismuth subgallate specifically are absent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No SAHPRA-registered indication (traditionally: gastrointestinal astringent, topical haemostatic) |
| Predicted New Indication (Top TxGNN) | Heparin Cofactor 2 Deficiency |
| TxGNN Prediction Score | 98.16% |
| Evidence Level | L5 (model prediction only; no supporting clinical studies identified) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for bismuth subgallate. Based on known information, bismuth subgallate is a bismuth(III) salt of gallic acid. Its recognised biological activities include mucosal astringency (via protein precipitation at epithelial surfaces), anti-*Helicobacter pylori* activity mediated by the bismuth ion (Bi³⁺), and antioxidant/mild anti-inflammatory properties derived from the gallic acid moiety. There is no SAHPRA-approved product monograph, and no formal MOA has been documented in the data available for this report.

**Regarding the top TxGNN prediction — Heparin Cofactor 2 Deficiency:** Heparin cofactor II (HCII) is a serine protease inhibitor that controls thrombin activity; deficiency leads to uncontrolled thrombin activation and elevated thrombotic risk. There is no known mechanism by which bismuth subgallate could upregulate HCII expression or activity. The high TxGNN score is most likely a **knowledge graph topology false positive**: four of the top six predictions involve coagulation-related diseases (ranks 1, 2, 4, and 6), a clustering pattern that strongly indicates graph-level node connectivity bias rather than genuine drug–disease association.

**The most mechanistically plausible predictions** are those relating to upper gastrointestinal pathology (ranks 9 and 10). Bismuth ions can form a protective colloidal layer over inflamed mucosa, inhibit *H. pylori* adhesion receptors in vitro, and the gallic acid component provides additive antioxidant and anti-inflammatory activity. These properties are directly relevant to both peptic ulcer disease and gastroduodenitis. Class-level evidence from related bismuth salts (bismuth subcitrate, bismuth subsalicylate) further supports biological plausibility, though direct studies on bismuth subgallate in these indications are lacking and extrapolation must be treated with caution.

---

## Clinical Trial Evidence

No clinical trials have been identified for bismuth subgallate across all 10 predicted indications (ClinicalTrials.gov and ICTRP both queried; all returned zero results as of 2026-03-24).

Currently no related clinical trials registered.

---

## Literature Evidence

Literature identified relates to **Peptic Ulcer Disease** (rank 10) only. All three publications investigated bismuth class compounds — bismuth subcitrate, bismuth subsalicylate, or generic "bismuth salts" — **not bismuth subgallate specifically**. Evidence represents class-level inference and should not be directly attributed to bismuth subgallate without further study.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2199292](https://pubmed.ncbi.nlm.nih.gov/2199292/) | 1990 | Narrative Review | *Gastroenterology* | Bismuth therapy comparable to H₂-receptor antagonists for peptic ulcer disease with lower relapse rate; bismuth acts as an antimicrobial agent suppressing *H. pylori*; combination with conventional antibiotics can eliminate the organism |
| [1589712](https://pubmed.ncbi.nlm.nih.gov/1589712/) | 1992 | Pharmacokinetic Study | *Scand J Gastroenterology* | Oral bismuth absorption is <0.1% across all tested compounds; basic bismuth gallate (bismuth subgallate) showed slightly higher absorption (0.038%) than bismuth salicylate/nitrate/aluminate (0.005–0.002%), with no whole-body retention detected |
| [8280948](https://pubmed.ncbi.nlm.nih.gov/8280948/) | 1993 | In Vitro Study | *Zentralbl Bakteriol* | Bismuth salts inhibit *H. pylori* receptor binding in vitro; mechanistically supports bismuth's role in peptic ulcer therapy; Tween detergents (comparator) showed similar receptor disruption |

---

## Prediction Summary: All 10 Indications

A full overview of all TxGNN predictions is provided below for completeness. This view is particularly important given the atypical prediction profile (coagulation disease cluster at top ranks).

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Mechanistic Plausibility |
|------|---------|-------------|----------------|----------|--------------------------|
| 1 | Heparin Cofactor 2 Deficiency | 98.16% | L5 | Hold | Very low — no known HCII pathway link; likely false positive |
| 2 | Antithrombin Deficiency Type 2 | 98.01% | L5 | Hold | Very low — no SERPINC1 pathway link |
| 3 | Rheumatoid Arthritis | 98.01% | L4 | Hold | Low — indirect anti-inflammatory via NF-κB; no DMARD activity |
| 4 | Factor 5 Excess with Spontaneous Thrombosis | 97.98% | L5 | Hold | Very low — likely cluster bias with ranks 1, 2, and 6 |
| 5 | Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome | 97.02% | L5 | Hold | Very low — rare embryonic developmental syndrome |
| 6 | Thrombophilia | 96.93% | L5 | Hold | Low — no anticoagulant mechanism established |
| 7 | Brachydactyly-Syndactyly Syndrome | 96.30% | L5 | Hold | Very low — congenital BMP/WNT pathway disorder |
| 8 | Gout | 94.07% | L4 | Hold | Low — theoretical xanthine oxidase inhibition by gallic acid moiety only; not validated for the intact molecule |
| 9 | Gastroduodenitis | 93.46% | L4 | Research Question | Moderate — mucosal astringency and antioxidant activity; overlaps with peptic ulcer pathology; no direct data |
| 10 | Peptic Ulcer Disease | 92.53% | L3 | Research Question | Moderate — class evidence for anti-*H. pylori* and mucosal protection; bismuth subgallate not directly studied |

---

## South Africa Market Information

Bismuth subgallate is **not currently registered with SAHPRA** and holds **no active product licences** in South Africa. It does not appear on the Essential Medicines List (EML). Any clinical research or compassionate-use application involving this compound would require either formal SAHPRA registration or a **Section 21 approval** (Medicines and Related Substances Act, Act 101 of 1965) for use of an unregistered medicine.

---

## Safety Considerations

Complete safety data (including warnings, contraindications, and drug–drug interactions) were not available in this Evidence Pack and could not be evaluated.

> Please consult international reference sources (DrugBank DB13909, WHO monographs, or equivalent) for safety information prior to any clinical or research use of bismuth subgallate. As there is no SAHPRA-approved Professional Information document for this compound, adverse drug reactions should be reported to SAHPRA through the MedSafe or relevant national pharmacovigilance reporting pathway.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction profile for bismuth subgallate is dominated by coagulation-related rare diseases in the top six ranks — a pattern consistent with knowledge graph cluster bias rather than genuine pharmacological association. The two most plausible predictions (gastroduodenitis and peptic ulcer disease) rest on indirect class-level evidence from other bismuth salts and carry no registered clinical trial support. The drug is also entirely absent from the South African market, creating an additional regulatory barrier before any clinical translation.

**To proceed, the following is needed:**

- **MOA characterisation**: Retrieve and document the formal mechanism of action for bismuth subgallate via DrugBank API and primary literature review (currently flagged as a High-severity data gap)
- **Safety data completion**: Obtain full warnings, contraindications, and drug interaction profile before any clinical consideration (currently a Blocking-severity data gap)
- **SAHPRA regulatory pathway assessment**: Determine whether a Section 21 application or full registration is appropriate for a South African research context
- **Compound-specific preclinical studies**: Commission in vitro and/or in vivo studies directly on bismuth subgallate (not class analogues) for gastroduodenitis and peptic ulcer disease, with appropriate *H. pylori* inhibition assays
- **Re-evaluation of coagulation-cluster predictions**: Flag ranks 1, 2, 4, and 6 as potential false positives in the knowledge graph model and consider re-weighting node topology in future TxGNN runs for this compound class

---

> **Disclaimer:** This report is intended for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All predictions should be interpreted within the context of appropriate clinical and scientific expertise.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

