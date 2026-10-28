---
layout: default
title: Ezetimibe
parent: Model Prediction Only (L5)
nav_order: 221
evidence_level: L5
indication_count: 1
monitor_inn: "EZETIMIBE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-23
description: "Ezetimibe: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Hyperlipidaemia"
---

# Ezetimibe
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

## Ezetimibe: From Hyperlipidaemia to Cholesterol-Ester Transfer Protein Deficiency
{: .text-alpha }

## One-Sentence Summary

Ezetimibe is a cholesterol-absorption inhibitor, with relations recorded in the knowledge graph for hyperlipidaemia, familial hypercholesterolaemia and sitosterolemia.
The TxGNN model predicts it may be useful for **cholesterol-ester transfer protein (CETP) deficiency**.
There are **no clinical trials** and **no publications that directly study this disease**, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperlipidaemia (relation recorded in the knowledge graph; the licence records compiled for this report contain no indication text) |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9909 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 6 of 6) |
| Number of SAHPRA Registrations | 6 (valid: 6) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on general pharmacology, ezetimibe inhibits NPC1L1-mediated intestinal cholesterol absorption and lowers LDL-C.

CETP deficiency is a rare condition marked by high HDL-C and reduced CETP-mediated transfer of cholesteryl esters. The only link to ezetimibe is shared lipid-metabolism pathways, which likely explains the high TxGNN score. No direct mechanism ties NPC1L1 inhibition to correcting or treating CETP deficiency.

CETP deficiency is mostly a biochemical phenotype rather than a clearly defined disease with an unmet treatment need, so the clinical rationale is weak. Any benefit would be indirect, for example lowering LDL-C in a patient who also has dyslipidaemia.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Neither publication below studies CETP deficiency with ezetimibe. They are listed as background only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40911366](https://pubmed.ncbi.nlm.nih.gov/40911366/) | 2025 | Review | European Heart Journal | Overview of lipid-lowering targets, including LDL-C, triglycerides, apoB and Lp(a), and their role in residual cardiovascular risk |
| [31779098](https://pubmed.ncbi.nlm.nih.gov/31779098/) | 2019 | Animal study | International Journal of Molecular Sciences | Heterozygous Ldlr-deficient hamster model (functional CETP) for testing a PCSK9 antibody in hyperlipidaemia and atherosclerosis |

---

## South Africa Market Information

Six single-ingredient registrations are recorded. The approved indication text is not available in the records compiled for this report. Essential Medicines List status is not available.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 54/7.5/0364 | Ezorb | Tablet | Not available |
| 55/7.5/0779 | Lypstaplus 10 Mg/10 Mg | Tablet | Not available |
| 50/7.5/1171 | Liptruzet 10/10 | Film-coated tablet | Not available |
| 54/7.5/0693 | Reguchole 10/5Mg | Tablet | Not available |
| A51/7.5/1008 | Tryzetor Plus 10/20 Mg | Tablet | Not available |

A sixth registration, Liptruzet 10/40 (50/7.5/1173, film-coated tablet), is also recorded.

---

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** contraindication links to pancreatitis, liver disease, gallbladder disease, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, substance abuse/dependence, rhabdomyolysis and nodular fasciitis. These must be checked against the SAHPRA-approved Professional Information (PI).
- **Drug interactions (100 recorded; main ones listed):**
  - Moderate: chenodeoxycholic acid, eluxadoline, rosuvastatin, simvastatin.
  - Severity not classified: calcitriol, pantoprazole, glimepiride, mesalazine, doxycycline, clotrimazole, acarbose, morphine, metformin, omeprazole, palonosetron, rosiglitazone, lansoprazole, cimetidine, vancomycin, lactulose.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score and a shared lipid-metabolism link. No trial or publication directly studies ezetimibe in CETP deficiency, and the condition has no clear unmet treatment need.

**To proceed, the following is needed:**
- Mechanism-of-action data from DrugBank
- SAHPRA Professional Information, including indications, warnings and contraindications
- Evidence that CETP deficiency is a clinical condition needing treatment
- Any study of ezetimibe in patients with CETP deficiency
- Review of the muscle, liver and gallbladder safety relations against the PI
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

