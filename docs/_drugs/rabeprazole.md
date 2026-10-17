---
layout: default
title: Rabeprazole
parent: Model Prediction Only (L5)
nav_order: 399
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Rabeprazole: predicted new indication Smouldering systemic mastocytosis (evidence level L5). Approved use: Peptic ulcer disease"
monitor_inn: "Rabeprazole"
predicted_indications: ["gastroduodenitis", "duodenal obstruction", "abnormality of glucagon secretion"]
---

# Rabeprazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Rabeprazole: From Peptic Ulcer Disease to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Rabeprazole is a proton pump inhibitor, originally used for peptic ulcer disease, gastroesophageal reflux disease (GORD) and gastric acid hypersecretory states such as Zollinger-Ellison syndrome.
The TxGNN model predicts it may be effective for **Smouldering systemic mastocytosis**, but **no clinical trials and no publications** currently support this specific prediction. The score likely reflects an existing link to systemic mastocytosis in the knowledge graph rather than new evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease (the SAHPRA registration entries compiled for this report contain no indication text; original indications come from the knowledge graph) |
| Predicted New Indication | Smouldering systemic mastocytosis |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, rabeprazole is a proton pump inhibitor that irreversibly blocks gastric H+/K+-ATPase and suppresses acid secretion. Its efficacy in acid-related disease is well established.

Systemic mastocytosis is already among rabeprazole's original indications in the knowledge graph. In this disease, excess mast cell histamine drives gastric acid hypersecretion. The high prediction score most likely reflects this existing link and graph proximity, not a new finding.

Acid suppression can control the gastrointestinal symptoms of histamine excess. It does **not** modify the underlying clonal mast cell disease, so any benefit would be symptomatic only. The same reasoning applies to the second-ranked prediction, lymphoadenopathic mastocytosis with eosinophilia (score 99.35%), for which there is also no clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for smouldering systemic mastocytosis.

---

## Literature Evidence

Currently no related literature available for smouldering systemic mastocytosis.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 33/11.4.3/0206 | Pariet | Tablet | Not available in the data compiled |
| Reg. No. 56/11.4.3/0623.621 | Ulcopraz 10 | Tablet | Not available in the data compiled |

Both registrations are valid single-ingredient oral tablets. Essential Medicines List (EML) status was not available in the data compiled for this report.

---

## Safety Considerations

- **Contraindications (knowledge graph, not label text):** liver disease, gallbladder disease, osteoporosis, postmenopausal osteoporosis, bone fracture. These come from drug-disease edges in the knowledge graph and must be verified against the SAHPRA-approved label.
- **Drug Interactions:** 100 interactions were identified (DDInter). Examples:
  - **Major:** acalabrutinib, atazanavir
  - **Moderate:** amikacin, amphotericin B (several formulations), amphetamine, apalutamide, aprepitant, armodafinil, bosutinib, thiazide diuretics (bendroflumethiazide, benzthiazide)
  - **Minor:** acetylsalicylic acid, axitinib
- **Pharmacogenomics:** Reviews note that CYP2C19 polymorphism can affect PPI exposure, although rabeprazole is among the least affected PPIs.
- **Long-term use:** Literature raises long-term PPI safety questions (for example, a possible association with Alzheimer's disease, which is a low-tier review and not established).

Warnings and contraindications from the SAHPRA package insert were not available. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for smouldering systemic mastocytosis rests on model score and an existing label link only. There are no trials or publications, and rabeprazole would give symptomatic acid control at most, not disease modification.

**To proceed, the following is needed:**
- Clinical or observational data on PPI use for GI symptoms in smouldering systemic mastocytosis
- SAHPRA package insert warnings, contraindications and approved indications (currently a blocking gap for safety screening)
- Mechanism of action data to support mechanistic-link analysis
- Review of the 100 identified drug interactions against likely co-medications in mastocytosis patients

**Other predictions for context:**
- **Peptic ulcer disease (active) and gastric ulcer:** these are within the existing approved indication, so they are not true repurposing. Evidence is L1 (for example, placebo-controlled RCTs in PMID 9590413), supporting **Proceed with Guardrails** (CYP2C19 variability, long-term PPI safety).
- **Gastroduodenitis:** L2 evidence (for example, PMID 25100080, an RCT of ulcer recurrence prevention in low-dose aspirin users), supporting **Proceed with Guardrails**.
- **Duodenogastric reflux:** L2 evidence from small mixed-design studies, a **research question** requiring a confirmatory trial.
- **Gastrojejunal ulcer:** indirect evidence only, a **research question**.
- **Duodenal obstruction, peptic ulcer perforation, abnormality of glucagon secretion, lymphoadenopathic mastocytosis with eosinophilia:** **Hold** (indirect or no evidence).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

