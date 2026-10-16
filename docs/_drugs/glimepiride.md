---
layout: default
title: Glimepiride
parent: Model Prediction Only (L5)
nav_order: 246
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Glimepiride: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "GLIMEPIRIDE"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Glimepiride
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

# Glimepiride: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Glimepiride is a sulfonylurea originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**,
but there are currently **no clinical trials** and **no publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (from the knowledge-graph indication data; the SAHPRA registration records compiled for this report contain no approved indication text) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, glimepiride is a sulfonylurea that closes pancreatic KATP channels to stimulate insulin release, and its efficacy in type 2 diabetes is established.

No mechanistic link to stiff person syndrome (SPS) has been established. SPS is an autoimmune neurological disorder involving anti-GAD65 antibodies and impaired GABAergic signalling, which is quite different from the pancreatic action of glimepiride. The only conceivable connection is the diabetes comorbidity common in SPS, and this is speculative.

The prediction should be read with caution. Focal stiff limb syndrome (an SPS-spectrum disorder) has an identical score, which suggests the signal is driven by shared disease-ontology neighbours in the knowledge graph rather than independent drug-specific evidence. Other high-scoring predictions for this drug follow a similar pattern:

- **Focal stiff limb syndrome** (99.75%): same score as classic SPS; likely a graph-neighbour effect.
- **Opsismodysplasia** (99.74%): only a loose link through insulin/PI3K signalling (INPPL1/SHIP2), with no supporting data.
- **Thiamine-responsive dysfunction syndrome** (99.73%): sulfonylureas might treat the diabetes component symptomatically, but this would not modify the disease.
- **Localized lipodystrophies** (99.56%–99.62%): near-identical scores across subtypes suggest a class-level graph artefact; insulin-secretagogue action could even be unhelpful.
- **Pancreatic agenesis** (99.55%): biologically implausible, because glimepiride needs residual beta cells to work.

## Clinical Trial Evidence

Currently no related clinical trials registered for classic stiff person syndrome.

## Literature Evidence

Currently no related literature available for classic stiff person syndrome.

## South Africa Market Information

Glimepiride is marketed in South Africa with 3 valid single-ingredient registrations, all in oral tablet form. The approved indication text was not available in the data compiled for this report, and Essential Medicines List (EML) status was not available.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 41/21.2/0656 | Accord glimepiride | Tablet | Not available |
| Reg. No. A39/21.2/0023 | Glimepiride 1 oethmaan | Tablet | Not available |
| Reg. No. 43/21.2/0005 | Amaryl Combi 2/500 | Tablet | Not available |

## Safety Considerations

Label warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available in the data compiled for this report. Please refer to the PI for full safety information. Report adverse drug reactions to SAHPRA.

- **Contraindications suggested by the knowledge graph** (not label text): kidney disease, liver disease, gallbladder disease, congestive heart failure, osteoporosis (including postmenopausal), infectious disease, thymus gland disease, and multiple pituitary-related conditions (hypopituitarism, pituitary hormone deficiencies, growth hormone deficiencies, hypogonadotropic hypogonadism, Kallmann syndrome, Sheehan syndrome). Also listed was pyoureter. These should be verified against the PI.
- **Drug Interactions**: 100 interactions were identified in the DDI database. The 20 reviewed include mostly Moderate-level interactions. Examples include:
  - Beta-agonists and sympathomimetics (salbutamol, formoterol, epinephrine, phenylephrine, pseudoephedrine)
  - Beta-blocker (acebutolol)
  - Corticosteroids (hydrocortisone; topical hydrocortisone and alclometasone are Minor)
  - NSAIDs (ibuprofen, ketorolac)
  - H2 blockers (famotidine, ranitidine)
  - Hydrochlorothiazide, acetazolamide, acitretin, ethinylestradiol, nitazoxanide
  - Albiglutide (GLP-1 agonist)
  - Ethanol

  Many of these are expected to alter glycaemic control, so hypoglycaemia or loss of control should be monitored.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the TxGNN score alone, with no clinical trials, no relevant publications, and no plausible mechanistic link between a pancreatic KATP-channel blocker and an autoimmune GABAergic disorder. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data for glimepiride (e.g., from DrugBank)
- Any biological or clinical rationale linking sulfonylurea action to SPS, supported by preclinical or observational data
- SAHPRA Professional Information (warnings, contraindications, approved indication text) to complete safety screening
- Evaluation of whether the high score reflects a graph artefact, given that focal stiff limb syndrome has an identical score
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

