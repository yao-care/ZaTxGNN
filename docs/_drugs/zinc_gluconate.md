---
layout: default
title: Zinc Gluconate
parent: Model Prediction Only (L5)
nav_order: 479
evidence_level: L5
indication_count: 10
---

# Zinc Gluconate
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

# Zinc Gluconate: From Ascorbic Acid Deficiency (Scurvy) to Anemia of Prematurity

## One-Sentence Summary

Zinc gluconate is a zinc salt. In the knowledge graph used for this prediction, its original indications are ascorbic acid deficiency and scurvy.
The TxGNN model predicts it may be effective for **anemia of prematurity**, but **no clinical trials and no publications** currently support this specific prediction.
The evidence is therefore model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ascorbic acid deficiency, scurvy (from the knowledge graph; no approved indication text is available in the SAHPRA records) |
| Predicted New Indication | Anemia of prematurity |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, zinc gluconate is a zinc salt, and zinc is an essential trace element involved in many enzymatic pathways, including haem synthesis and erythropoiesis. This offers a plausible, but unproven, link to anaemia.

The relationship between the original indications (nutrient deficiency states) and anemia of prematurity is a loose nutritional one. Both involve micronutrient shortfalls, but the data compiled for this report do not show a direct mechanistic bridge.

There is also a safety tension. Zinc can antagonise copper absorption, and copper deficiency can itself cause anaemia. One case report in the compiled literature describes severe anaemia from chronic excess zinc gluconate intake. Any use in preterm infants would need careful weighing of this risk.

The other nine predictions for this drug are also very high scoring (above 99.8%). Only the top-ranked prediction is evaluated in detail here. Several of the others are broad ontology categories or rare dental and jaw dysplasias, and they have little or no supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for anemia of prematurity.

## Literature Evidence

Currently no related literature available for anemia of prematurity.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 52/24/0031 | Nutryelt | Infusion | Not available in the data compiled |
| G2667 (ACT 101/1965) | Gericomplex | Capsule | Not available in the data compiled |
| 41/10.2.1/0849 | Spiriva respimat inhaler 60 doses | Inhaler | Not available in the data compiled |

All three registrations are valid single-ingredient entries. Essential Medicines List (EML) status could not be determined from the data compiled.

Note that the listing of Spiriva Respimat (an inhaler product) under zinc gluconate looks inconsistent and should be verified against the SAHPRA register before any reliance is placed on it.

## Safety Considerations

**Knowledge graph contraindication signals** (from drug-disease edges in the TxGNN knowledge graph, not from label text):
- Cardiovascular: hypertensive disorder, hypertension
- Autoimmune and inflammatory: rheumatoid arthritis, systemic lupus erythematosus (including paediatric), multiple sclerosis
- Allergic and respiratory: allergic rhinitis, vasomotor rhinitis, asthma
- Haematological and metabolic: blood coagulation disease, sickle cell anaemia, hereditary persistence of fetal haemoglobin, primary hyperoxaluria, hereditary haemochromatosis, haemosiderosis, iron metabolism disease, Wilson disease
- Other: diarrhoeal disease, HIV infectious disease, AIDS, leukaemia

**Drug interactions:** The interaction query returned 100 entries. The first 19 reviewed include:
- **Moderate:** alendronic acid, risedronic acid, ibandronate (bisphosphonates), tetracycline, baloxavir marboxil
- **Minor:** mainly immunosuppressants and biologics (for example abatacept, adalimumab, azathioprine, baricitinib) and corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone)

Moderate interactions with bisphosphonates, tetracycline and baloxavir are consistent with zinc chelation, so dosing separation is generally advisable.

**Additional safety signals from the compiled literature:**
- Intranasal zinc gluconate has been linked to anosmia (loss of smell) in humans and animals.
- Chronic excess zinc intake can cause copper-deficiency anaemia.

Please refer to the SAHPRA-approved Professional Information (PI) for label warnings and contraindications, which were not available in the data compiled. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for anemia of prematurity rests on a model score alone, with no registered trials or publications. The mechanistic link is plausible but unsupported, and the copper-antagonism risk is particularly relevant in preterm infants.

**To proceed, the following is needed:**
- Retrieve the SAHPRA package inserts to obtain approved indications, warnings and contraindications (a blocking gap for safety screening)
- Obtain detailed mechanism of action data
- Conduct a literature search for zinc supplementation in preterm infants, including copper status and haematological outcomes
- Verify the SAHPRA registration data, in particular the Spiriva entry
- Define the route and formulation required for neonatal use, as route compatibility has not been assessed
- Establish a safety monitoring plan (zinc and copper status, haemoglobin) before any clinical evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

