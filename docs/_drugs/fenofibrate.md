---
layout: default
title: Fenofibrate
parent: Model Prediction Only (L5)
nav_order: 224
evidence_level: L5
indication_count: 1
monitor_inn: "FENOFIBRATE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-29
description: "Fenofibrate: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Hypertriglyceridaemia, hyperlipidaemia, familial hyperlipidaemia…"
---

# Fenofibrate
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

## Fenofibrate: From Hyperlipidaemia to Cholesterol-Ester Transfer Protein Deficiency
{: .text-alpha }

## One-Sentence Summary

Fenofibrate is a lipid-lowering drug used in hypertriglyceridaemia, hyperlipidaemia and related familial lipid disorders.
The TxGNN model predicts it may be relevant for **cholesterol-ester transfer protein (CETP) deficiency**, but there are **no registered clinical trials** and only **3 publications** (all preclinical or mechanistic, none studying the disease itself), so the evidence is very weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertriglyceridaemia, hyperlipidaemia, familial hyperlipidaemia, familial combined hyperlipidaemia and hypoalphalipoproteinaemia (relations recorded in the knowledge graph; the local registration lists no indication text) |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9961 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, fenofibrate is a PPAR-alpha agonist. It lowers triglycerides and raises HDL cholesterol, and in mice it upregulates genes involved in HDL remodelling, such as phospholipid transfer protein (PMID 11342537).

CETP deficiency is characterised by markedly raised HDL cholesterol and impaired cholesteryl ester transfer. The overlap with fenofibrate is therefore in lipoprotein metabolism. However, the direction of effect is questionable. Fenofibrate already raises HDL-C, so it would not correct the high HDL-C of CETP deficiency. CETP deficiency is also generally regarded as a lipid-profile abnormality rather than a condition that clearly needs treatment.

The only study combining the two themes (PMID 20332533) tested CETP *inhibition* together with PPAR-alpha agonism in transgenic mice. That is a different context from CETP deficiency as a disease. The very high TxGNN score most likely reflects network proximity within lipid-metabolism pathways rather than a true therapeutic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20332533](https://pubmed.ncbi.nlm.nih.gov/20332533/) | 2010 | Preclinical | J Cardiovasc Pharmacol Ther | In human ApoB100/CETP transgenic mice, the CETP inhibitor torcetrapib and fenofibrate were tested for effects on lipid profiles; CETP inhibition combined with PPAR-alpha agonism raised HDL-C and lowered LDL-C |
| [11342537](https://pubmed.ncbi.nlm.nih.gov/11342537/) | 2001 | Mechanistic/Preclinical | J Biol Chem | Fenofibrate induced the phospholipid transfer protein gene, accounting for HDL enlargement in treated mice |
| [30271349](https://pubmed.ncbi.nlm.nih.gov/30271349/) | 2018 | Mechanistic/Preclinical | Front Physiol | Plasma HDL-C did not correlate with faecal cholesterol or cholesterol efflux capacity, suggesting HDL function matters more than HDL-C level |

None of these studies directly addresses CETP deficiency as a disease.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 52/7.5/0769 | Pravafen 40/160 mg | Capsule (oral) | No indication text available in the data compiled for this report |

Note: the data compiled for this report records one valid registration. The product name suggests it may contain more than one active ingredient, so this registration should not be taken as describing how single-ingredient fenofibrate is approved. Essential Medicines List status is not available in the data compiled for this report.

---

## Safety Considerations

**Contraindication relations recorded in the knowledge graph** (not taken from label text) include:
- Liver failure and liver disease
- Pancreatitis
- Gallbladder disease, cholelithiasis and cholecystolithiasis
- Muscle disorders: myopathy, muscular disease, rhabdomyolysis
- Impaired renal function
- Blood disorders: thrombocytopenia, anaemia, leukopenia, agranulocytosis, neutropenia and related congenital neutropenias

**Drug Interactions:** 100 interactions were found in total. The records listed are all of Moderate severity:
- Sulfonylureas: acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide
- Insulins: multiple formulations (human, aspart, degludec, detemir, glargine, glulisine, lispro and others), which may affect glycaemic control
- Chenodeoxycholic acid
- Esomeprazole

For full warnings and contraindications, refer to the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction rests on model score alone. No clinical trials exist, and the three publications are preclinical or mechanistic and do not study CETP deficiency, so the evidence level is L5. The expected direction of effect (further HDL-C elevation in a condition already marked by high HDL-C) does not support a treatment benefit, and it is unclear that the condition needs treatment.

**To proceed, the following is needed:**
- Clear clinical justification that CETP deficiency requires treatment, and a defined therapeutic goal
- Human data (case series or trials) in patients with CETP deficiency
- Mechanism of action data for fenofibrate
- SAHPRA Professional Information warnings and contraindications for the single-ingredient product, as the only local registration appears to be for a product that may contain more than one active ingredient
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

