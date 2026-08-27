---
layout: default
title: Metoclopramide
parent: 僅模型預測 (L5)
nav_order: 313
evidence_level: L5
indication_count: 5
---

# Metoclopramide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Metoclopramide: From Nausea, Vomiting and Gastroparesis to Gastric Ulcer

## One-Sentence Summary

> Metoclopramide is a dopamine D2-receptor antagonist internationally used for nausea, vomiting and gastroparesis (its formal South African licensing status could not be confirmed — it is currently **not marketed** locally).
> The TxGNN model predicts it may be effective for **Gastric Ulcer**, but supporting evidence is thin: only **2 clinical trials** (neither designed to treat ulcers) and **20 publications**, most of which are decades-old preclinical or mechanistic studies rather than disease-specific efficacy data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Nausea, vomiting and gastroparesis (internationally established use; not derivable from South African licensing data, as the drug has 0 SAHPRA registrations on record) |
| Predicted New Indication | Gastric Ulcer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, metoclopramide is a dopamine D2-receptor antagonist with two principal effects: a central antiemetic action (blocking the medullary chemoreceptor trigger zone) and a peripheral prokinetic action (increasing gastric emptying and lower oesophageal sphincter tone via dopamine antagonism and enhanced acetylcholine release). It has no acid-suppressing or mucosal-protective activity — the two mechanisms that underlie standard gastric ulcer therapy (e.g., PPIs, H2-blockers, sucralfate).

Gastric ulcer and metoclopramide's established indications (gastroparesis, GERD-related motility disorders, chemotherapy/surgery-related nausea) both involve the upper gastrointestinal tract, which likely explains the TxGNN model's high similarity score — the knowledge graph associates the drug with anatomically and symptomatically adjacent GI conditions. However, the underlying evidence base does not support a therapeutic (ulcer-healing) mechanism: several preclinical rodent studies (below) suggest an indirect "ulcer-protective" effect via improved gastric drainage and reduced pyloric reflux, independent of acid secretion, but this has not been translated into any completed disease-specific human trial.

Reflecting this, the two identified clinical trials do not test metoclopramide as an ulcer treatment — one is a pharmacist-led prescribing-safety quality improvement study, and the other evaluates pre-endoscopy use to improve visualization in active GI bleeding, not ulcer healing itself.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03747107](https://clinicaltrials.gov/study/NCT03747107) | N/A | Completed | 19 | Pharmacist- and data-driven prescribing safety quality improvement programme in primary care (Scotland); not a gastric ulcer treatment trial — low relevance (grade C). |
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Phase 4 | Unknown | 60 | Tests whether pre-endoscopy metoclopramide improves gastric visibility and reduces need for repeat intervention in upper GI bleeding; evaluates a procedural adjunct, not ulcer healing — status unknown, no published results (grade B). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [775822](https://pubmed.ncbi.nlm.nih.gov/775822/) | 1976 | Clinical study | ZFA. Zeitschrift für Allgemeinmedizin | Reports on therapy of gastric and duodenal ulcer with metoclopramide (abstract not available). |
| [19225](https://pubmed.ncbi.nlm.nih.gov/19225/) | 1977 | Review | Drugs | General review of drug treatments for gastric and duodenal ulcer (abstract not available). |
| [2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/) | 1989 | Animal study | Arch Int Pharmacodyn Ther | Metoclopramide (20–50 mg/kg) produced an ulcer-protective effect in aspirin-induced and pylorus-ligated rat models, comparable to ranitidine. |
| [6436177](https://pubmed.ncbi.nlm.nih.gov/6436177/) | 1984 | Animal study | Indian J Physiol Pharmacol | Protected against experimentally induced gastric ulceration in guinea pigs without affecting acid secretion — effect attributed to improved gastric drainage, not mucosal healing. |
| [6336644](https://pubmed.ncbi.nlm.nih.gov/6336644/) | 1983 | Review | Annals of Internal Medicine | Pharmacology review: dopamine antagonism drives antiemetic and GI-stimulatory effects; no acid-suppressive or mucosal-protective mechanism described. |
| [16807979](https://pubmed.ncbi.nlm.nih.gov/16807979/) | 2006 | RCT (double-blind) | Yonsei Medical Journal | IV metoclopramide plus ranitidine reduced preoperative gastric contents vs. placebo in day-case surgery patients; not disease-specific to ulcer. |
| [4779253](https://pubmed.ncbi.nlm.nih.gov/4779253/) | 1973 | Clinical study | Current Medical Research and Opinion | Examined bile reflux in gastric ulcer patients and the effect of smoking, metoclopramide and carbenoxolone sodium (abstract not available). |
| [797497](https://pubmed.ncbi.nlm.nih.gov/797497/) | 1976 | Review | Clinical Pharmacokinetics | Reviews how gastric ulcer and other conditions/drugs alter gastric emptying and downstream drug absorption. |
| [28652516](https://pubmed.ncbi.nlm.nih.gov/28652516/) | 2017 | Animal study | J Smooth Muscle Res | Studied effects of prokinetic drugs, including metoclopramide, on gastric emptying after acetic-acid-induced ulceration in rats; found regional differences by ulcer site. |
| [6106882](https://pubmed.ncbi.nlm.nih.gov/6106882/) | 1980 | Review | Medizinische Klinik | German-language review on conservative (non-surgical) treatment of gastric ulcer (abstract not available). |

---

## South Africa Market Information

No SAHPRA registration for metoclopramide is recorded in the evidence pack (0 licenses; market status: Not Marketed). Local product/dosage-form data could not be extracted.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: original evidence pack flags TFDA label warnings/contraindications as a **Blocking** data gap — this must be resolved before any safety review can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The mechanistic link is weak: metoclopramide has no acid-suppressive or mucosal-protective action, the standard mechanisms for gastric ulcer treatment. Supporting evidence is limited to preclinical rodent/guinea-pig studies and clinical trials that were not designed to test ulcer treatment (procedural/QI studies), yielding an evidence level of only L4.
- No completed Phase 2/3 RCT directly evaluates metoclopramide for gastric ulcer therapy.

**To proceed, the following is needed:**
- TFDA/SAHPRA-approved Professional Information (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Detailed mechanism of action (MOA) data from DrugBank — currently a **High**-severity gap (DG002)
- A disease-specific clinical trial or observational study directly testing gastric ulcer healing endpoints
- Confirmation of South African regulatory/marketing pathway, since the drug currently has no SAHPRA registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

