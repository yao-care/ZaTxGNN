---
layout: default
title: Diltiazem
parent: Model Prediction Only (L5)
nav_order: 181
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Diltiazem: predicted new indication Obsolete susceptibility to ischaemic stroke (evidence level L5). Approved use: Hypertension, atrial fibrillation, Prinzmetal angina…"
monitor_inn: "DILTIAZEM"
predicted_indications: ["obsolete susceptibility to ischemic stroke"]
---

# Diltiazem
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Diltiazem: From Hypertension to Susceptibility to Ischaemic Stroke (Obsolete Ontology Term)

## One-Sentence Summary

Diltiazem is a calcium channel blocker, originally used for hypertension, atrial fibrillation, Prinzmetal (vasospastic) angina and ventricular tachycardia.
The TxGNN model predicts it may be relevant to **"obsolete susceptibility to ischemic stroke"**, but **no clinical trials and no publications** were found in the data compiled for this report. The prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, atrial fibrillation, Prinzmetal angina, ventricular tachycardia (from the TxGNN knowledge graph; the SAHPRA registration entries contain no indication text) |
| Predicted New Indication | Obsolete susceptibility to ischaemic stroke |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for this report. Diltiazem is generally known as a non-dihydropyridine L-type calcium channel blocker. Its efficacy in hypertension and in cardiac rhythm and angina disorders is established. Mechanistically, it could plausibly relate to ischaemic stroke through blood pressure lowering, vasodilation, reduced vasospasm and possible effects on cerebral vascular tone. This is general pharmacological reasoning, not evidence from the data compiled for this report.

There are important caveats:
- The predicted disease term is labelled **"obsolete"**, meaning it is a deprecated ontology entry. The prediction may reflect a legacy or duplicated disease node rather than a distinct clinical indication.
- Stroke prevention through blood pressure control is already an expected benefit of treating hypertension. It is not a novel repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 28/7.1/0298 | Sandoz Diltiazem HCl 60 | Tablet | Not available |
| Reg. No. 28/7.1/0579 | Tilazem 180 CR | Sustained-release capsule (SRC) | Not available |
| Reg. No. 30/7.1/0183 | Adco-Zildem SR | Sustained-release capsule (SRC) | Not available |

All 3 registrations are valid single-ingredient products. None are cancelled. Essential Medicines List (EML) status is not covered by the data compiled for this report.

---

## Safety Considerations

- **Disease-level contraindication signals (from the knowledge graph, not label text):**
  - Cardiac conduction and rhythm: atrioventricular block, sick sinus syndrome (including the familial form), Wolff-Parkinson-White syndrome, Lown-Ganong-Levine syndrome, ventricular tachycardia (including catecholaminergic and infant forms)
  - Haemodynamic and structural: hypotensive disorder, aortic stenosis (including aortic valve disease and supravalvular forms), hypertrophic cardiomyopathy, renal artery obstruction
  - Organ function: kidney disease, liver disease, gallbladder disease, pyoureter
  - Haematological: neutropenia, agranulocytosis
  - Angioedema (acquired, hereditary and RAAS-blocker-induced forms)
  - Connective tissue, bone and cartilage disease
- **Drug Interactions:** 100 interactions are recorded. Examples from the data:
  - **Major:** loperamide
  - **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), pioglitazone, bupropion, aprepitant, morphine, acetylsalicylic acid, canagliflozin, and calcium salts (carbonate, chloride, citrate, acetate and others)

  Polypharmacy is a particular concern in a stroke population.

The knowledge-graph signals are not a substitute for label information. Please refer to the SAHPRA-approved Professional Information (PI) for formal warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high model score. There are no trials or publications, the target disease term is obsolete, and any stroke-related benefit overlaps with existing blood pressure control. Evidence is at L5.

**To proceed, the following is needed:**
- Clarify which current disease entity the obsolete term maps to, and define a clinically meaningful stroke-related indication
- Mechanism of action data and a mechanistic-link analysis
- Systematic literature and trial searches (including SANCTR and PACTR) on diltiazem in stroke prevention or outcomes
- SAHPRA package insert warnings and contraindications, which are needed before any safety screening
- A review of interaction and contraindication risks for a stroke population on multiple medicines
- Route and formulation compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

