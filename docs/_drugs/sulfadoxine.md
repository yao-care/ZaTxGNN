---
layout: default
title: Sulfadoxine
parent: Model Prediction Only (L5)
nav_order: 429
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Sulfadoxine: predicted new indication Gout (evidence level L5). Approved use: Not stated in the SAHPRA record compiled for this report (the drug is…"
monitor_inn: "Sulfadoxine"
predicted_indications: ["gout", "bronchitis", "brain small vessel disease 1 with or without ocular anomalies", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "diabetic nephropathy", "conjunctivitis", "appendicitis", "obsolete hyperuricemia (disease)", "Lesch-Nyhan syndrome", "peritonitis"]
---

# Sulfadoxine
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

# Sulfadoxine: From Malaria (Registered Antimalarial Use) to Gout

## One-Sentence Summary

Sulfadoxine is a long-acting sulfonamide that inhibits the folate pathway of microbes and is registered in South Africa as Fansidar tablets, where it is used mainly with pyrimethamine against malaria.
The TxGNN model predicts it may be effective for **gout**, but **no clinical trials and no relevant publications** support this prediction.
It is a graph-based signal only and should be treated as hypothesis-level.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA record compiled for this report (the drug is generally used with pyrimethamine for malaria) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 99.10% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, sulfadoxine is a long-acting sulfonamide that inhibits dihydropteroate synthase in the microbial folate pathway.

For gout, no plausible mechanism has been identified. Sulfadoxine has no known uricosuric or xanthine oxidase inhibitory activity. The high score (0.991) most likely reflects graph proximity, possibly through sulfonamide-class links to urate handling, rather than a real pharmacological relationship.

Other predictions for this drug show the same weakness:
- **Obsolete hyperuricemia (disease)** and **Lesch-Nyhan syndrome** are probably the same signal as gout, because they sit close to it in the knowledge graph. They are not independent evidence.
- **Bronchitis** and **peritonitis** have only a general antibacterial rationale. Acute bronchitis is mostly viral, and better-characterised antibiotics exist.
- **Diabetic nephropathy** has no therapeutic rationale. Sulfonamides are renally cleared and carry renal and hypoglycaemia concerns.
- **Conjunctivitis**: the one paper describes ocular damage caused by sulfadoxine-pyrimethamine, which is an adverse effect, not a benefit.
- **Two COL4A1-related rare vascular disorders** and **appendicitis** have no mechanistic link, and the literature matches look like retrieval artefacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for gout.

---

## Literature Evidence

Currently no related literature available for gout.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| K/20.2.6/68 | Fansidar | Tablet (oral) | Indication text not available in the data compiled for this report |

The Essential Medicines List (EML) status of this product could not be determined from the data compiled for this report.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (drug-disease links in PrimeKG, not taken from label text, so they must be verified against the Professional Information):
- Blood disorders: thrombocytopenia, neutropenia, agranulocytosis, anaemia, macrocytic anaemia, folic acid deficiency anaemia, G6PD deficiency
- Kidney and liver disease, and gallbladder disease
- Porphyria (including inherited porphyria and porphyrin metabolism disease)
- Epilepsy
- Metabolic conditions: glycogen storage disease, cystinuria, galactosemia
- Pyoureter

**Drug interactions** (DDInter, 50 interactions recorded, all 20 listed in the data compiled for this report rated Moderate):
- Sulfonylureas and other insulin secretagogues: chlorpropamide, glimepiride, glipizide, glyburide, tolazamide, repaglinide, nateglinide
- Insulins: aspart, degludec, detemir, glargine, glulisine, lispro, human (isophane, regular, zinc, zinc extended, inhaled rapid-acting)
- Others: naltrexone, picosulfuric acid

The main practical concern is additive blood-glucose lowering with antidiabetic agents.

**Reported serious adverse effect (from the literature compiled for this report):** a case report describes Lyell syndrome (toxic epidermal necrolysis) with severe ocular sequelae after sulfadoxine-pyrimethamine.

SAHPRA package insert warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The gout prediction rests only on a knowledge-graph score, with no trials, no supporting literature and no plausible mechanism. The drug also carries notable safety concerns (severe cutaneous reactions, blood disorders, renal effects), and established urate-lowering agents are available.

**To proceed, the following is needed:**
- Retrieve the SAHPRA package insert to confirm the registered indication, warnings and contraindications
- Obtain mechanism of action data (for example from DrugBank) and test whether any urate-related mechanism exists
- Run a systematic literature search specific to sulfonamides and urate handling, to check whether the graph signal has any real basis
- Consider reprioritising to candidates with actual supporting evidence, since the other nine predictions are equally unsupported
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

