---
layout: default
title: Magnesium Hydroxide
parent: 僅模型預測 (L5)
nav_order: 299
evidence_level: L5
indication_count: 6
---

# Magnesium Hydroxide
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

# Magnesium Hydroxide: From Antacid Use to Active Peptic Ulcer Disease

## One-Sentence Summary

> Magnesium Hydroxide (DrugBank DB09104) is classically used as an over-the-counter antacid/laxative agent; a distinct, registry-documented "original indication" is not recorded in this evidence pack.
> The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**,
> with **0 dedicated clinical trials** but **20 supporting publications** (including a completed randomized controlled trial) currently backing this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this dataset — Magnesium Hydroxide is pharmacologically classified worldwide as an antacid/laxative; no `taiwan_regulatory.licenses` entries are available to cite a formal registered indication |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.98% (rank 267) |
| Evidence Level | L2 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The structured mechanism-of-action (MOA) field for Magnesium Hydroxide is not populated in this evidence pack. However, the literature evidence collected for this candidate consistently documents its pharmacology: Mg(OH)₂ reacts directly with secreted gastric hydrochloric acid to form MgCl₂ and water, neutralizing free acid, raising intragastric pH, and reducing pepsin activity. Several studies also show that magnesium/aluminium-hydroxide antacids stimulate endogenous mucosal prostaglandin and bicarbonate secretion, producing a cytoprotective effect that supports ulcer healing (PMID 22950493, 2595273, 2390927, 1769429).

Because Magnesium Hydroxide is already established internationally as a component of antacid therapy, the relationship between its (undocumented-in-registry) traditional use and the TxGNN-predicted indication — active peptic ulcer disease — is mechanistically direct rather than a distant repurposing signal. This explains both the very high prediction score (>99.9%) and the consistent volume of supporting literature spanning decades (1979–2022), much of it from the classic cimetidine-vs-antacid comparative trial era of the 1980s.

Mechanistically, the pathway is straightforward: acid neutralization → reduced pepsin activity → reduced mucosal irritation → prostaglandin/EGF-mediated mucosal repair → ulcer healing. This is a well-characterized, internally consistent mechanism rather than a novel biological hypothesis, which supports plausibility but also means the "new" indication substantially overlaps with the drug's known pharmacological class use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Magnesium Hydroxide specifically in active peptic ulcer disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT | Scandinavian Journal of Gastroenterology | 12-week double-blind trial (n=72): antacid+anticholinergic achieved 50% ulcer healing vs. 67% with cimetidine, both superior to placebo |
| [1526089](https://pubmed.ncbi.nlm.nih.gov/1526089/) | 1992 | RCT | Clinical Pharmacology and Therapeutics | 8-week multicenter RCT showing an H2-antagonist superior to placebo in healing benign gastric ulcer and relieving peptic ulcer symptoms (acid-suppression comparator context) |
| [22950493](https://pubmed.ncbi.nlm.nih.gov/22950493/) | 2013 | Review | Current Pharmaceutical Design | Reviews gastric cytoprotection mechanisms; antacids protect mucosa and promote ulcer healing beyond simple acid neutralization |
| [6086186](https://pubmed.ncbi.nlm.nih.gov/6086186/) | 1984 | Cohort/Review | Clinics in Gastroenterology | Reviews antacids and anticholinergics for duodenal ulcer treatment, comparing pharmacology and side-effect profiles |
| [2401189](https://pubmed.ncbi.nlm.nih.gov/2401189/) | 1990 | Cohort | Drugs Under Experimental and Clinical Research | Retrospective cohort of 267 paediatric patients with peptic symptoms evaluating efficacy of pharmacological agents including antacids |
| [2595273](https://pubmed.ncbi.nlm.nih.gov/2595273/) | 1989 | Preclinical | Scandinavian Journal of Gastroenterology | Rat model: Al(OH)₃/Mg(OH)₂ antacid dose-dependently prevented ethanol-, aspirin-, and stress-induced gastric lesions via prostaglandin-mediated gastroprotection |
| [35720246](https://pubmed.ncbi.nlm.nih.gov/35720246/) | 2022 | In vitro | Medicine and Pharmacy Reports | Evaluated acid-neutralizing capacity of antacids (including magnesium/aluminium hydroxide) marketed in Morocco |
| [37146](https://pubmed.ncbi.nlm.nih.gov/37146/) | 1979 | Review | Fortschritte der Medizin | Describes antacid neutralizing capacity and dosing regimen (1 and 3 hours post-meal) required to control peptic ulcer acid secretion |
| [3018068](https://pubmed.ncbi.nlm.nih.gov/3018068/) | 1986 | Clinical study | Journal of Clinical Gastroenterology | Compared sodium bicarbonate vs. aluminum-magnesium hydroxide antacid on postprandial gastric acid buffering in duodenal ulcer patients |
| [2986275](https://pubmed.ncbi.nlm.nih.gov/2986275/) | 1985 | RCT | Scandinavian Journal of Gastroenterology | Randomized double-blind 6-week trial: sucralfate vs. alginate/antacid in reflux esophagitis, ~70% symptomatic improvement in both arms |

---

## South Africa Market Information

Magnesium Hydroxide is **not currently marketed or registered in South Africa** — the evidence pack records 0 SAHPRA registrations and a market status of "Not Marketed." No product/dosage-form/registration data is available to tabulate at this time.

---

## Safety Considerations

No structured safety data (key warnings, contraindications, or drug interactions) is available in the evidence pack for Magnesium Hydroxide. Please refer to the SAHPRA-approved Professional Information (PI) for safety information, and report any adverse drug reactions to SAHPRA.

**Note on a mechanism-related safety signal identified in the supporting literature:** several studies on antacid pharmacology (PMID 1500660, 20617595) describe an "acid rebound" phenomenon — a paradoxical increase in gastric acid secretion following antacid administration, particularly with calcium-containing formulations and potentially relevant to prolonged or high-dose magnesium/aluminium hydroxide use. This should be factored into any clinical guardrail protocol developed for use in active peptic ulcer disease.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction score is very high (99.98%) and is corroborated by a substantial, mechanistically coherent literature base — including a completed randomized controlled trial (PMID 7034155) directly testing an antacid regimen in active peptic ulcer healing. However, there are no indication-specific registered clinical trials, no SAHPRA market authorization, and no structured MOA or safety data in this evidence pack, so the prediction should be treated as supportive of an already well-known pharmacological use rather than a novel, independently validated repurposing signal.

**To proceed, the following is needed:**
- Structured mechanism-of-action (MOA) data via DrugBank API query (currently flagged as a High-severity data gap, DG002)
- SAHPRA-approved Professional Information (PI) covering warnings/precautions and contraindications (currently flagged as a Blocking data gap, DG001) — required before any S1 safety assessment can proceed
- Confirmation of South African registration pathway/status, since the drug is currently not marketed locally
- Clarification of the drug's registry-documented original indication(s) to properly benchmark "repurposing distance"
- A specific guardrail addressing the acid-rebound phenomenon noted in the literature, particularly for prolonged or high-dose regimens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

