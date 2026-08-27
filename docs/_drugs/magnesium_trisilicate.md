---
layout: default
title: Magnesium Trisilicate
parent: 僅模型預測 (L5)
nav_order: 300
evidence_level: L5
indication_count: 5
---

# Magnesium Trisilicate
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

# Magnesium Trisilicate: From Antacid Use to Peptic Ulcer Disease (Gastric & Gastrojejunal Ulcer)

## One-Sentence Summary

> Magnesium Trisilicate is a long-established antacid agent. The TxGNN model's top-ranked prediction for this drug is **Active Peptic Ulcer Disease** (score 99.86%), an umbrella diagnosis that clusters together several closely related, model-predicted sub-indications — **Gastrojejunal Ulcer**, **Gastric Ulcer**, **Gastroduodenitis**, and **Peptic Ulcer Perforation**. Direct evidence for the umbrella term itself is absent, but two of its sub-types (Gastric Ulcer, Gastrojejunal Ulcer) are supported by **20+ historical publications**, including two comparative/double-blind RCTs, while the drug currently has **no SAHPRA market presence** in South Africa.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antacid use (gastric hyperacidity / dyspepsia) — no formal SAHPRA-approved indication text is available, as no license record exists for this substance in the evidence pack |
| Predicted New Indication | Active Peptic Ulcer Disease (top-ranked; closely related sub-types Gastric Ulcer and Gastrojejunal Ulcer carry the strongest direct evidence) |
| TxGNN Prediction Score | 99.86% (model rank 1125) |
| Evidence Level | L4 for "active peptic ulcer disease" itself (no direct trials/literature); **L2** for the sibling sub-indications Gastric Ulcer and Gastrojejunal Ulcer (historical RCT support) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this DrugBank entry is not available (DG002, High severity). Based on known pharmacology, magnesium trisilicate is a classic **antacid**: it neutralises gastric hydrochloric acid and, in aqueous suspension, precipitates a colloidal silicic acid layer that adheres to and locally protects the ulcer bed and surrounding mucosa. This dual acid-neutralising / mucosal-coating action is the same mechanism historically exploited in antacid combination products (e.g., aluminium hydroxide + magnesium trisilicate, sold historically as Gelusil-type products).

TxGNN's five predictions for this drug are not five unrelated diseases — they form a single acid-related ulcer-disease cluster: **active peptic ulcer disease** (rank 1, the umbrella term), **gastrojejunal ulcer** (rank 2), **peptic ulcer perforation** (rank 3), **gastroduodenitis** (rank 4), and **gastric ulcer** (rank 5). This internal consistency supports the biological plausibility of the model's output: an antacid is mechanistically suited to acid-related mucosal ulceration and inflammation.

However, the strength of *actual supporting evidence* varies sharply within this cluster. The umbrella term "active peptic ulcer disease" and "gastroduodenitis" have **no direct trial or literature hits** in this evidence pack (L4, Research Question) — their support is only inferred by extrapolation from the sibling entries below. **Gastrojejunal ulcer** and **gastric ulcer**, by contrast, are backed by decades of clinical literature testing magnesium trisilicate (often in antacid combinations) directly in peptic/gastric ulcer patients, including a 1965 double-blind RCT and a 1984 South African comparative trial (L2, Proceed with Guardrails). **Peptic ulcer perforation**, on the other hand, is a surgical emergency requiring operative management of peritonitis/haemorrhage — an antacid's acid-neutralising mechanism does not address this acute complication, so this prediction is mechanistically mismatched and is scored L5/Hold, most likely reflecting semantic proximity within the ulcer-disease ontology rather than a genuine therapeutic signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Predicted Indication | Key Findings |
|---------|------|------|------|------|---------|
| [NCT07310927](https://clinicaltrials.gov/study/NCT07310927) | Phase 2/3 | Recruiting | 140 | Gastric Ulcer (indirect relevance, grade C) | Compares alginate vs. sucralfate (both add-on to PPI) for GERD symptom relief; does not test magnesium trisilicate and targets GERD rather than gastric ulcer itself — included only as adjacent acid-related-disease context |

No SANCTR or PACTR-registered trials were identified. No clinical trials were found for "active peptic ulcer disease," "gastrojejunal ulcer," "peptic ulcer perforation," or "gastroduodenitis" that test magnesium trisilicate directly.

---

## Literature Evidence

| PMID | Year | Type | Journal | Supports Indication | Key Findings |
|------|-----|------|------|------|---------|
| [14248445](https://pubmed.ncbi.nlm.nih.gov/14248445/) | 1965 | RCT (double-blind) | British Medical Journal | Gastrojejunal Ulcer | Double-blind trial of bismuth aluminate vs. magnesium trisilicate in peptic ulceration with simultaneous gastric acid analysis |
| [6328685](https://pubmed.ncbi.nlm.nih.gov/6328685/) | 1984 | RCT (comparative) | South African Medical Journal | Gastric Ulcer | 88 patients with endoscopically proven gastric/duodenal ulcer treated with ranitidine vs. an antacid containing aluminium hydroxide + magnesium trisilicate (Gelusil); 4-week healing rates 74% (ranitidine) vs. 63% (antacid), difference not significant — a locally relevant (South African) comparative dataset |
| [20321118](https://pubmed.ncbi.nlm.nih.gov/20321118/) | 1938 | Clinical study | Canadian Medical Association Journal | Gastrojejunal Ulcer | Early foundational clinical study of magnesium trisilicate in the treatment of peptic ulcer |
| [15425465](https://pubmed.ncbi.nlm.nih.gov/15425465/) | 1950 | Cohort/clinical study | American Journal of Digestive Diseases | Gastrojejunal Ulcer | Aluminium hydroxide + magnesium trisilicate plus mucin in 125 patients with peptic ulcer |
| [20271751](https://pubmed.ncbi.nlm.nih.gov/20271751/) | 1947 | Cohort/clinical study | Archives of Surgery | Gastrojejunal Ulcer | Gastroscopic and clinical studies of aluminium hydroxide + magnesium trisilicate plus mucin in peptic ulcer treatment |
| [6368445](https://pubmed.ncbi.nlm.nih.gov/6368445/) | 1983 | Controlled trial | International Journal of Tissue Reactions | Gastric Ulcer | 40 gastric ulcer outpatients: De-Nol (tripotassium dicitrato bismuthate) vs. an antacid mixture containing magnesium trisilicate, assessed by endoscopy at day 14 and 28 |
| [4301560](https://pubmed.ncbi.nlm.nih.gov/4301560/) | 1968 | Clinical study | Wiener medizinische Wochenschrift | Gastrojejunal Ulcer | Antacid effect of a magnesium trisilicate–hyoscyamine combination preparation (Neoplex B) |
| [6547921](https://pubmed.ncbi.nlm.nih.gov/6547921/) | 1984 | Experimental/physiological study | Fortschritte der Medizin | Gastric Ulcer / Gastrojejunal Ulcer | Endoscopic measurement of transmural electrical potential difference at gastric ulcer sites following local application of sucralfate, aluminium hydroxide, and magnesium trisilicate |
| [15688172](https://pubmed.ncbi.nlm.nih.gov/15688172/) | 2005 | Case review (safety) | Der Urologe | Gastric Ulcer (safety signal) | Reviews silica-containing urinary calculi; flagged in the evidence pack as a long-term safety signal relevant to renal-impaired patients on chronic silicate-containing antacids |
| [6293043](https://pubmed.ncbi.nlm.nih.gov/6293043/) | 1982 | Cohort (safety) | Scandinavian Journal of Gastroenterology Supplement | Gastrojejunal Ulcer (safety signal) | Reviews mineral-metabolism side effects of long-term antacid therapy (phosphate depletion, bone demineralisation), relevant to chronic use in high-risk patients |

---

## South Africa Market Information

Magnesium Trisilicate is currently **not marketed in South Africa**: the evidence pack shows 0 SAHPRA licenses and no registered products. No historical or current SAHPRA registration record, dosage form, or approved indication text was available for extraction. Any repurposing pathway would first require establishing (or re-establishing) a South African regulatory registration before clinical use could be considered.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Note on data completeness:** Retrieval of formal safety warnings and contraindications for this drug is flagged as a **Blocking data gap (DG001)** — until TFDA/PI-equivalent warning and contraindication text is obtained, this candidate cannot proceed to a formal S1 safety pre-assessment. Separately, the literature evidence above surfaces two safety signals worth monitoring if this candidate advances: (1) long-term silicate exposure has been associated with silica-containing urinary calculi (PMID 15688172), and (2) long-term antacid use has been associated with mineral-metabolism disturbances such as phosphate depletion and bone demineralisation in high-risk patients (PMID 6293043). No formal drug-interaction (DDI) data was returned by the current query (status: not found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking data gap (DG001) means formal SAHPRA/TFDA-equivalent safety warnings and contraindications are not yet available, so this candidate cannot yet pass safety pre-assessment (S1).
- The drug has **zero current SAHPRA registrations** in South Africa, meaning there is no existing local regulatory or PI reference point.
- While the sub-indications Gastric Ulcer and Gastrojejunal Ulcer are individually reasonable (L2, Proceed with Guardrails) based on historical RCT-level evidence, the top-ranked umbrella prediction "active peptic ulcer disease" itself has no direct trial or literature support (L4), and a related model prediction (peptic ulcer perforation) is mechanistically inappropriate for antacid monotherapy (Hold).

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/SAHPRA-equivalent Professional Information (warnings, contraindications) before any S1 safety pre-assessment
- Resolve DG002: obtain confirmed DrugBank mechanism-of-action data
- Confirm whether a South African regulatory pathway (new registration or import authorisation) exists or would be required, given current 0-license status
- Source more contemporary literature/RCTs — the current corpus is dominated by studies from 1938–1990, predating modern PPI-era comparator standards
- Establish a renal-function monitoring plan given the silicate urinary-calculi signal, particularly for long-term or renal-impaired patients
- Complete a formal DDI screen — the current query returned no data, and broader antacid-class literature (e.g., PMID 7336470, phenytoin bioavailability) suggests interaction risk warrants explicit review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

