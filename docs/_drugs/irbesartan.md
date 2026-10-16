---
layout: default
title: Irbesartan
parent: Model Prediction Only (L5)
nav_order: 273
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Irbesartan: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension, diabetic nephropathy"
---

# Irbesartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Irbesartan: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Irbesartan is an angiotensin II receptor blocker (ARB), originally used to treat hypertension and diabetic nephropathy.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but there are currently **no registered clinical trials and no publications** supporting this specific prediction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, diabetic nephropathy (the South African registrations in the data compiled for this report carry no indication text) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

Other predictions in the same analysis:

| Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|
| Malignant hypertensive renal disease | 99.31% | L5 | Hold |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 99.25% | L4 | Research question |
| Pulmonary hypertension with unclear multifactorial mechanism | 99.25% | L5 | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, irbesartan blocks the angiotensin II type 1 (AT1) receptor. Its efficacy in hypertension and diabetic nephropathy is established, and mechanistically it may be applicable to hypertension driven by renin-angiotensin-aldosterone system (RAAS) activation.

Malignant renovascular hypertension is strongly driven by RAAS activation, so the mechanistic rationale is plausible. The high TxGNN score probably reflects similarity to the existing hypertension indication rather than independent evidence.

There is also an important safety concern. ARBs carry a risk of acute kidney injury in renovascular disease, particularly with bilateral renal artery stenosis or stenosis in a single functioning kidney. This is the very population that the predicted indication describes. The kidney-related prediction (malignant hypertensive renal disease) is consistent with the approved use in diabetic nephropathy. However, it is a hypertensive emergency setting, where oral ARB monotherapy is not standard care.

For the pulmonary hypertension predictions, the only supporting material is indirect preclinical work (see below). Systemic antihypertensive effects of an ARB may not translate to the pulmonary vasculature, and there is a risk of systemic hypotension.

## Clinical Trial Evidence

Currently no related clinical trials registered. No NCT, SANCTR or PACTR identifiers were found for any of the four predicted indications.

## Literature Evidence

No literature was found for malignant renovascular hypertension. For the third-ranked prediction (pulmonary hypertension owing to lung disease and/or hypoxia), the most relevant retrieved publications are all preclinical or reviews, with no clinical studies. The retrieved papers were not specific to this indication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35288835](https://pubmed.ncbi.nlm.nih.gov/35288835/) | 2022 | Review | Inflammopharmacology | Pleiotropic effects of AT1 receptor antagonists in hypoxia induced by cardiac ischaemia |
| [30356256](https://pubmed.ncbi.nlm.nih.gov/30356256/) | 2018 | Preclinical (in vitro) | PLoS One | Irbesartan protected cardiomyocytes under hypoxic stress |
| [34626328](https://pubmed.ncbi.nlm.nih.gov/34626328/) | 2022 | Preclinical (animal) | Sleep Breath | Irbesartan attenuated sleep apnoea-induced cardiac apoptosis |
| [17142340](https://pubmed.ncbi.nlm.nih.gov/17142340/) | 2007 | Preclinical (animal) | Am J Physiol Heart Circ Physiol | Irbesartan inhibited coronary angiogenesis stimulated by chronic intermittent hypoxia in neonatal rats |
| [34147903](https://pubmed.ncbi.nlm.nih.gov/34147903/) | 2021 | Preclinical (animal) | Biomed Pharmacother | Irbesartan ameliorated pulmonary artery lesions in a rat model of chronic mountain sickness |
| [34286497](https://pubmed.ncbi.nlm.nih.gov/34286497/) | 2021 | Preclinical (study type not classified) | Eur Rev Med Pharmacol Sci | Irbesartan improved oxidative stress in rats with high-altitude pulmonary hypertension, via effects on intestinal flora |
| [15526904](https://pubmed.ncbi.nlm.nih.gov/15526904/) | 2004 | Preclinical (animal) | Renal Failure | Irbesartan reduced cyclosporine nephrotoxicity (off-target for this indication) |

These findings concern hypoxia-induced tissue injury and high-altitude disease models, not pulmonary hypertension in patients with lung disease. The hypoxia and HIF-1α pathway link is a hypothesis worth testing, but it is not clinical evidence. Several other retrieved papers (Chinese herbal medicine studies and a roxadustat case report) were not about irbesartan and are not listed.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 46/7.1.3/0124 | Jubitan | Tablet (oral) | Not available in the data compiled |
| Reg. No. 42/7.1.3/0116 | Co Irbewin 300/25 | Tablet (oral) | Not available in the data compiled |
| Reg. No. 45/7.1.3/0073 | Isart Co 150 | Tablet (oral) | Not available in the data compiled |

All three registrations are currently valid. Two product names (Co Irbewin, Isart Co) suggest irbesartan/hydrochlorothiazide combinations, so the exact composition should be confirmed against the registered Professional Information. Essential Medicines List (EML) status was not available in the data compiled for this report.

## Safety Considerations

**Contraindications flagged in the knowledge graph (not label text):**
The TxGNN knowledge graph lists the following disease associations. These come from graph edges and must be verified against the SAHPRA-approved Professional Information:
- Angioedema (including hereditary, acquired and RAAS-blocker-induced forms)
- Renal artery obstruction and anuria
- Hypotensive disorder
- Diabetes mellitus and diabetic ketoacidosis
- Electrolyte and metabolic conditions: potassium deficiency disease, hypercalcaemia, hyperparathyroidism, phosphorus metabolism disease, nephrocalcinosis, gout and hyperuricaemia
- Hepatic coma and hepatic encephalopathy
- Pancreatitis
- Systemic lupus erythematosus
- Muscle disorders (myopathy, rhabdomyolysis, familial periodic paralysis)
- Neonatal jaundice

Some of these probably relate to the hydrochlorothiazide component of combination products rather than irbesartan itself.

**Drug Interactions:**
The interaction screen returned 100 interactions in total, of which 20 are listed in the data compiled. The most clinically important:
- **Major:** potassium citrate and potassium bicarbonate (risk of hyperkalaemia)
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), acetylsalicylic acid, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), insulins (aspart, degludec), morphine, bupropion, aprepitant, dronabinol, and bowel preparations (picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes)

SAHPRA package insert warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (malignant renovascular hypertension) is supported only by the model score, with no trials or publications, and it falls in a setting where ARBs carry a recognised risk of acute kidney injury. The pulmonary hypertension prediction has a plausible hypoxia-related hypothesis but only indirect preclinical evidence, so it is best treated as a research question rather than a treatment proposal.

**To proceed, the following is needed:**
- The SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for irbesartan, to support the mechanistic-link analysis
- Clinical data in renovascular hypertension, with a specific safety assessment for renal artery stenosis
- Clinical or well-designed translational studies of irbesartan in pulmonary hypertension, if that direction is to be pursued
- Confirmation of the approved indications, composition and EML status of the three South African registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

