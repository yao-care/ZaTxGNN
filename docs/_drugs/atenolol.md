---
layout: default
title: Atenolol
parent: Model Prediction Only (L5)
nav_order: 50
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Atenolol: predicted new indication Posterolateral myocardial infarction (evidence level L5). Approved use: Hypertension, myocardial infarction"
monitor_inn: "ATENOLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "chronic pulmonary heart disease"]
---

# Atenolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Atenolol: From Hypertension and Myocardial Infarction to Posterolateral Myocardial Infarction

## One-Sentence Summary

Atenolol is a beta-1 selective blocker, originally used to treat hypertension and myocardial infarction.
The TxGNN model predicts it may be effective for **posterolateral myocardial infarction**,
but **no clinical trials** and **no publications** specific to this subtype were found, so the prediction rests mainly on extension from the approved myocardial infarction indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, myocardial infarction (from the knowledge graph; SAHPRA indication text is not available in the data compiled for this report) |
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 (no clinical trials or literature for this subtype; model prediction plus mechanistic reasoning only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Atenolol is, however, a well-established beta-1 selective blocker. It lowers heart rate, myocardial contractility and oxygen demand, and these effects underlie its use after myocardial infarction.

Posterolateral myocardial infarction is an anatomical subtype of myocardial infarction, which is already an approved indication. The prediction is therefore best seen as an extension of the existing indication, not a distinct repurposing signal. Benefit is plausible by the same mechanism, but there is no subtype-specific evidence.

**Other predicted indications (for context):**

| Rank | Predicted Indication | Score | Evidence Summary | Decision |
|---|---|---|---|---|
| 2 | Posteroinferior myocardial infarction | 99.87% | One small 1985 crossover RCT comparing atenolol and diltiazem anti-ischaemic activity after MI; indirect only | Research question |
| 3 | Malignant hypertensive renal disease | 99.85% | None; usually managed with parenteral agents | Hold |
| 4 | Malignant renovascular hypertension | 99.85% | One 2008 case report; definitive treatment is revascularisation | Hold |
| 5 | Pulmonary hypertension, unclear multifactorial mechanism | 99.84% | None; beta-blockers are generally avoided in pulmonary arterial hypertension | Hold |
| 6 | Pulmonary hypertension owing to lung disease/hypoxia | 99.84% | Retrieved literature mostly off-topic; rat studies are contradictory | Hold |
| 7 | Septal myocardial infarction | 99.84% | One 1981 thallium scintigraphy study; not outcome evidence | Research question |
| 8 | Braddock syndrome | 99.80% | None | Hold |
| 9 | Chronic pulmonary heart disease | 99.04% | Mostly systemic hypertension literature; not supportive | Hold |

## Clinical Trial Evidence

Currently no related clinical trials registered for posterolateral myocardial infarction.

## Literature Evidence

Currently no related literature available for posterolateral myocardial infarction.

The only nearby publication is for the related subtype, posteroinferior myocardial infarction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) | 1985 | RCT (small, crossover, single-blind) | La Revue de médecine interne | Atenolol 200 mg vs diltiazem 240 mg in 23 patients, 4 weeks after a limited postero-inferior or anterior MI, using computerised exercise testing; indirect, small and old |

## South Africa Market Information

Atenolol is registered with SAHPRA in 6 valid single-ingredient registrations. Approved indication text and Essential Medicines List status are not available in the data compiled for this report. Three of the products (Sandoz Co-Tenidone, Tenoret 50 and Tenchlor HS) are listed as atenolol-containing tablets with registration numbers in the 7.1.3 category; their ingredient make-up should be confirmed against the Professional Information.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 41/5.2/0005 | Gulf atenolol | Tablet | Not available |
| Reg. No. A38/5.2/0502 | Tenopress | Tablet | Not available |
| Reg. No. 32/5.2/0670 | B-block | Tablet | Not available |
| Reg. No. Y/7.1.3/24 | Sandoz Co-Tenidone 50/12.5 | Tablet | Not available |
| Reg. No. S/7.1.3/201 | Tenoret 50 50mg/12.5mg | Tablet | Not available |

## Safety Considerations

Warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available in the data compiled for this report. Please refer to the PI and report adverse drug reactions to SAHPRA.

**Contraindication-related conditions (from the knowledge graph, not label text):** liver failure, asthma (including intrinsic and allergic), diabetes mellitus (types 1 and 2) and diabetic ketoacidosis, atrioventricular block, Raynaud disease, anaphylaxis, systemic lupus erythematosus, psoriasis, gout, pancreatitis, anuria, anxiety and neurotic disorders, and several electrolyte or metabolic disorders (potassium deficiency, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease). These should be verified against the PI.

**Drug interactions:** The interaction screen returned 100 interactions, of which 20 were reviewed here. Most are Moderate, including:
- Epinephrine
- Corticosteroids (hydrocortisone, triamcinolone, betamethasone, budesonide)
- Anticholinergics (atropine, hyoscyamine)
- Bupropion
- Morphine
- Acetohexamide
- Calcium salts (acetate, carbonate, citrate, gluconate, lactate and others)

Minor interactions include acetylsalicylic acid, aluminium hydroxide and attapulgite.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score reflects proximity to the already approved myocardial infarction indication, not independent evidence. No trials or subtype-specific literature support posterolateral myocardial infarction, and the only related study is small, old and indirect. The safety data also remain incomplete.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications and approved indications) for the registered atenolol products
- Confirmation of whether the approved myocardial infarction indication already covers this subtype, which would make a separate repurposing case unnecessary
- Mechanism of action data
- Subtype-specific clinical evidence, or a clinical judgement that existing myocardial infarction trial data can be applied
- Review of the knowledge-graph contraindications (especially asthma, diabetes and atrioventricular block) against the PI
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

