---
layout: default
title: Metoclopramide
parent: Model Prediction Only (L5)
nav_order: 321
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-29
monitor_inn: "METOCLOPRAMIDE"
predicted_indications: ["gastroduodenitis", "peptic ulcer perforation"]
description: "Metoclopramide: predicted new indication Gastroduodenitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Metoclopramide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Metoclopramide: Gastroduodenitis
{: .text-alpha }

## One-Sentence Summary

Metoclopramide is a prokinetic and antiemetic drug, originally used for gastroesophageal reflux disease (GORD) and oesophagitis.
The TxGNN model predicts it may be effective for **gastric ulcer**, but only **1 clinical trial** (Phase 4, status unknown) and a body of mostly older review literature relate to this direction.
The evidence concerns procedural use during endoscopy, not ulcer treatment, so this remains a research question.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 (observational and review-level evidence only; no completed Phase 3 or Phase 2/3 RCT for this indication) |
| South Africa Market Status | Marketed (valid licences: 4 of 4) |
| Number of SAHPRA Registrations | 4 (valid: 4) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. From general pharmacology, metoclopramide is a dopamine D2 antagonist and 5-HT4 agonist that enhances gastric emptying and upper gastrointestinal motility. This is the basis for its use in reflux disease and nausea.

Gastric ulcer and reflux disease are both upper gastrointestinal acid-peptic conditions, and the TxGNN score likely reflects this network proximity. Metoclopramide, however, has no direct ulcer-healing mechanism: it neither suppresses acid nor protects the mucosa. Its plausible role is limited to symptom control, such as delayed gastric emptying or bile reflux accompanying ulcer disease.

The one registered trial uses metoclopramide as premedication before endoscopy in upper GI bleeding. This is a procedural use that improves visualisation, not ulcer treatment. The very high prediction score should therefore be read as a signal of model proximity, not independent evidence of ulcer efficacy.

Other ranked predictions follow the same pattern:

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Gastroduodenitis | 0.9990 | L5 | Motility-based link only; two recent RCTs address endoscopic visualisation in GI bleeding, not inflammation |

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Phase 4 | Unknown | 60 | Double-blind, single-centre RCT of metoclopramide premedication in upper GI bleeding. Tests whether it reduces repeat endoscopy, interventional radiology or surgery, and improves visualisation. Only partially relevant to ulcer treatment; no results available |

No SANCTR or PACTR registrations were identified in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42259699](https://pubmed.ncbi.nlm.nih.gov/42259699/) | 2026 | RCT (triple-blind, placebo-controlled) | Rev Gastroenterol Mex | High-dose IV metoclopramide (20 mg) for gastroduodenal visualisation in acute upper GI bleeding of ≤24 h; usefulness described as controversial. Retrieved under the gastroduodenitis prediction |
| [38059896](https://pubmed.ncbi.nlm.nih.gov/38059896/) | 2024 | RCT (double-blind) | Am J Gastroenterol | Metoclopramide for gastric visualisation by endoscopy in active upper GI bleeding. Retrieved under the gastroduodenitis prediction |
| [786607](https://pubmed.ncbi.nlm.nih.gov/786607/) | 1976 | Review | Drugs | Pharmacology and clinical use of metoclopramide, including easing emergency endoscopy in upper GI haemorrhage. Retrieved under the gastric ulcer prediction |
| [6336644](https://pubmed.ncbi.nlm.nih.gov/6336644/) | 1983 | Review | Ann Intern Med | Metoclopramide pharmacology: dopamine antagonism, antiemetic effect and GI smooth muscle stimulation. Retrieved under the peptic ulcer prediction |
| [19445547](https://pubmed.ncbi.nlm.nih.gov/19445547/) | 2009 | Systematic review | Paediatr Drugs | Evidence-based review of pharmacological management of GOR in children |
| [2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/) | 1989 | Animal study | Arch Int Pharmacodyn Ther | Metoclopramide showed ulcer-protective effects in aspirin-induced and pylorus-ligated rat models. Preclinical only. Retrieved under the peptic ulcer prediction |
| [8095331](https://pubmed.ncbi.nlm.nih.gov/8095331/) | 1993 | Review | Postgrad Med | Strategies for ulcers and reflux oesophagitis refractory to standard regimens |
| [11879596](https://pubmed.ncbi.nlm.nih.gov/11879596/) | 2002 | Review | Curr Treat Options Gastroenterol | Functional (non-ulcer) dyspepsia and the role of gastric emptying assessment |
| [6782467](https://pubmed.ncbi.nlm.nih.gov/6782467/) | 1981 | Randomised crossover study | MMW Munch Med Wochenschr | In 12 healthy men, neither domperidone nor metoclopramide significantly changed serum gastrin or gastric acid secretion |
| [797497](https://pubmed.ncbi.nlm.nih.gov/797497/) | 1976 | Review | Clin Pharmacokinet | Drugs and diseases (including gastric ulcer) that alter gastric emptying |

Most of the literature is older review material on motility and dyspepsia. None shows that metoclopramide heals gastric ulcers in humans. The one human study of acid secretion found no effect.

---

## South Africa Market Information

All four registrations are single-ingredient products with valid status. No approved indication text or manufacturer details are available in the data compiled for this report. Essential Medicines List (EML) status was not available in the compiled data and should be confirmed.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 29/5.7.2/0781 | Pramalon | Injection | Not available |
| Reg. No. V/5.7.2/352 | Bio metoclopramide | Tablet | Not available |
| Reg. No. Q/5.7.2/228 | Metoclopramide 10 oethmaan | Tablet | Not available |
| Reg. No. L/5.7.2/0319 | Clopamon | Syrup | Not available |

Available routes are injectable, oral (tablet) and oral liquid (syrup).

---

## Safety Considerations

**Contraindications flagged in the knowledge graph** (drug-disease edges, not label text):

- **Neurological and movement disorders:** Parkinson disease and parkinsonian disorder, tardive dyskinesia, lingual-facial-buccal dyskinesia, torsion dystonia, epilepsy, neuroleptic malignant syndrome
- **Cardiovascular and catecholamine-related:** hypertension and hypertensive disorder, phaeochromocytoma and related adrenal or sympathetic tumours
- **Gastrointestinal:** active peptic ulcer disease. This is relevant to the proposed indication and warrants clinical review. A labelled contraindication also exists for suspected GI perforation or obstruction, where increased motility is hazardous.
- **Metabolic:** porphyria and related disorders, pyruvate dehydrogenase E3 deficiency, methemoglobinemia due to methemoglobin reductase deficiency
- **Organ impairment:** cirrhosis of liver, impaired renal function
- **Psychiatric:** anxiety disorder, neurotic disorder, dysthymic disorder
- **Other tumours:** duodenum, small intestine and heart cancers

**Drug interactions:** The interaction screen returned 100 interacting drugs; the 20 reviewed include the following.

- **Major:** tramadol, amisulpride
- **Moderate:** opioids (fentanyl, alfentanil, codeine, dihydrocodeine), sedating antihistamines (chlorpheniramine, cetirizine, phenyltoloxamine), alprazolam, amitriptyline, amobarbital, ethanol, amantadine, abiraterone, amifampridine, and others
- **Minor:** acetaminophen

Many of these involve additive central nervous system depression or extrapyramidal effects.

Please also refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications, which were not available in the data compiled for this report. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Metoclopramide has no direct ulcer-healing mechanism, and the only trial and recent RCTs study endoscopic visualisation in GI bleeding rather than ulcer treatment. The high TxGNN score reflects network proximity to reflux disease, not independent efficacy evidence. The knowledge graph also flags active peptic ulcer disease as a contraindication.
- The SAHPRA package insert safety data, which blocks safety screening, are also missing.

**To proceed, the following is needed:**
- Download and review the SAHPRA package insert (warnings, contraindications, approved indications) for the four registered products
- Detailed mechanism of action data (e.g. from DrugBank)
- Controlled clinical evidence of ulcer healing or recurrence outcomes, not only endoscopic visualisation
- Clarification of the contraindication status in active peptic ulcer disease and suspected perforation
- A defined safety plan for neurological adverse effects (extrapyramidal reactions, tardive dyskinesia) and for the major interactions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

