---
layout: default
title: Esomeprazole
parent: Model Prediction Only (L5)
nav_order: 217
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Esomeprazole: predicted new indication Duodenogastric reflux (evidence level L5). Approved use: Peptic ulcer disease, gastroesophageal reflux disease…"
monitor_inn: "Esomeprazole"
predicted_indications: ["duodenal obstruction", "abnormality of glucagon secretion", "Smouldering systemic mastocytosis", "multiple endocrine neoplasia", "acne (disease)"]
---

# Esomeprazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Esomeprazole: From Peptic Ulcer Disease and Reflux Disease to Duodenogastric Reflux

## One-Sentence Summary

Esomeprazole is a proton pump inhibitor (PPI) originally used for acid-related conditions such as peptic ulcer disease, gastroesophageal reflux disease (GORD), reflux oesophagitis and Zollinger-Ellison syndrome.
The TxGNN model predicts it may be effective for **duodenogastric reflux** (bile reflux into the stomach).
This is supported by **no registered clinical trials** and only **1 general review article**, so the prediction is currently unproven.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, gastroesophageal reflux disease, reflux oesophagitis, Zollinger-Ellison syndrome (no approved-indication text is available in the SAHPRA records) |
| Predicted New Indication | Duodenogastric reflux |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L4 (mechanistic rationale only; no disease-specific studies) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Esomeprazole belongs to the PPI class, which suppresses gastric acid. In reflux-related disease, this may reduce mucosal injury and relieve symptoms.

The prediction has an important limitation. Duodenogastric (bile) reflux is driven mainly by duodenal contents such as bile and pancreatic fluid, not by acid. A PPI would therefore offer, at best, symptomatic benefit by lowering the acid component of mucosal irritation. It would not address the cause. The one supporting reference is a general review of PPI clinical use and pharmacokinetics, and it does not examine this condition.

The high TxGNN score likely reflects the closeness of this condition to acid-related upper gastrointestinal diseases in the knowledge graph. It should not be read as evidence of benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | Eur J Clin Pharmacol | General update on PPI clinical use and pharmacokinetics. PPIs are first-choice drugs for peptic ulcer, H. pylori infection, GORD, NSAID-induced GI lesions and Zollinger-Ellison syndrome. It does not address duodenogastric reflux. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 51/11.4.3/0932 | Nectizole IV | Infusion |
| Reg. No. 45/11.4.3/0121 | Nexipraz OTC | Tablet |
| Reg. No. 45/3.1/0179 | Vimovo 500/20 mg | Tablet |

All three registrations are currently valid. Both injectable (infusion) and oral (tablet) routes are available. Approved indication text and Essential Medicines List status were not available in the data compiled for this report.

---

## Safety Considerations

- **Conditions flagged in the knowledge graph (not label text):** The TxGNN knowledge graph lists drug-disease contraindication links for liver failure, osteoporosis, postmenopausal osteoporosis, bone fracture and chronic atrophic gastritis. These need verification against the approved Professional Information (PI).
- **Drug interactions:** The interaction query returned 100 entries, and the first 20 were reviewed.
  - **Major:** acalabrutinib and atazanavir.
  - **Moderate:** abametapir (topical), hydrochlorothiazide, amphotericin B (including the lipid complex), amikacin, amphetamine, fenofibrate, apalutamide, armodafinil, atorvastatin, bendamustine, bosutinib and bumetanide.
  - **Minor:** acetylsalicylic acid, axitinib, bortezomib, brivaracetam and cyanocobalamin.

Label-based warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials and no disease-specific publications for duodenogastric reflux. Bile reflux is not primarily acid-driven, so any benefit would likely be limited to symptoms. The prediction rests on model score and general PPI pharmacology.

Other predicted indications in this analysis, such as duodenal ulcer and active peptic ulcer disease, have much stronger trial support. They are essentially on-label or closely related uses rather than true repurposing.

**To proceed, the following is needed:**
- Disease-specific clinical or observational data on PPIs, or esomeprazole specifically, in duodenogastric (bile) reflux, including symptom and mucosal outcomes
- Clarification of whether the expected benefit is symptomatic only
- The SAHPRA Professional Information (PI) for warnings, contraindications and approved indications
- Detailed mechanism-of-action data
- A review of long-term PPI safety (for example bone health and interactions) if prolonged use is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

