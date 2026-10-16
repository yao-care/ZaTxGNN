---
layout: default
title: Phenylalanine
parent: Model Prediction Only (L5)
nav_order: 371
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Phenylalanine: predicted new indication Sclerosing cholangitis (evidence level L5). Approved use: Not stated in the registration data compiled for this report"
---

# Phenylalanine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Phenylalanine: From Amino Acid Nutritional Component to Sclerosing Cholangitis

## One-Sentence Summary

Phenylalanine is an essential amino acid. In South Africa it is registered as a component of parenteral nutrition and peritoneal dialysis solutions.
The TxGNN model predicts it may be effective for **Sclerosing Cholangitis**, but there are **no registered clinical trials** and only **3 publications**, none of which show a therapeutic effect.
The prediction is therefore computational only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data compiled for this report (all 11 SAHPRA registrations are amino acid-containing infusion products) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, phenylalanine is an essential amino acid that is a component of multi-ingredient parenteral nutrition and dialysis products. A therapeutic mechanism for sclerosing cholangitis has not been established.

The data compiled for this report show no direct mechanistic link. The only loosely related paper (2005) studied plasma tyrosine, a phenylalanine metabolite, in relation to fatigue in primary biliary cirrhosis and primary sclerosing cholangitis. It describes an association with a symptom, not a treatment effect. A plausible but unproven hypothesis is that aromatic amino acid metabolism is altered in cholestatic liver disease. That points to a possible biomarker role rather than a therapeutic one.

Supplementing phenylalanine in a liver disease with impaired hepatic amino acid metabolism could also carry risk. The high TxGNN score should therefore be treated as a hypothesis-generating signal only.

A second prediction, **congenital prothrombin deficiency** (score 99.26%), has no trials and no literature. Phenylalanine has no known role in prothrombin synthesis or function, so this prediction is likely a knowledge-graph artefact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohort | BMC Gastroenterology | Examined the relationship between plasma tyrosine and fatigue in primary biliary cirrhosis and primary sclerosing cholangitis. This is an association with a symptom, not a treatment effect. |
| [32025163](https://pubmed.ncbi.nlm.nih.gov/32025163/) | 2020 | Cohort (metabolomic) | J Clin Exp Hepatol | Serum metabolic signature of cholangiocarcinoma versus benign hepatobiliary disease. Biomarker study, not relevant to treatment. |
| [2103382](https://pubmed.ncbi.nlm.nih.gov/2103382/) | 1990 | Preclinical/assay | J Gastroenterol Hepatol | Radioimmunoassay of a formylated peptide (fMLP) showing enterohepatic circulation. Not relevant to phenylalanine as a treatment. |

---

## South Africa Market Information

All 11 registrations are currently valid single-entity registrations. Approved indication text is not available in the data compiled for this report. Essential Medicines List (EML) status was not available. The five main registrations are shown below.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 37/34/0243 | Nutrineal PD4 with 1.1% amino acids 2.5L | Infusion | Not available |
| Reg. No. 38/34/0172 | Extraneal 2L single bag | Infusion | Not available |
| Reg. No. 37/25.2/0503 | Oliclinomel N6 900E 2000ml | Infusion | Not available |
| Reg. No. 41/25/0757 | Nutriflex Lipid Peri | Infusion | Not available |
| Reg. No. 52/25/0739 | Numeta G13E | Infusion | Not available |

Other registrations include Numeta G16E, Smofkabiven, Smofkabiven Peripheral, Nutriflex Omega Specialized, Nutriflex Lipid Special 625ml and Adco-Ipratropium (ni201). The Adco-Ipratropium entry is listed as a vial and looks unusual for a phenylalanine-containing product, so its link to this drug should be verified.

---

## Safety Considerations

Warnings, contraindications and drug interaction data are not available from the label sources compiled for this report. The knowledge graph (PrimeKG, not label text) lists the following diseases as potential contraindications:

- **Metabolic:** phenylketonuria and other disorders of phenylalanine metabolism, phosphorus metabolism disease
- **Renal:** kidney disease, chronic kidney disease, chronic renal failure, end-stage renal failure, nephrolithiasis, nephrocalcinosis, acute urate nephropathy, pyoureter
- **Calcium-related:** hypercalcaemia, humoral hypercalcaemia of malignancy, sarcoidosis
- **Cardiovascular:** heart disease, cardiovascular disease, digitalis poisoning, ventricular fibrillation

These are knowledge-graph associations and need confirmation against the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials, and the available literature describes biomarker or symptom associations rather than a therapeutic effect. Whether the product labels contain safety information has not been established, and phenylalanine may carry risk in liver disease.

**To proceed, the following is needed:**
- Download and review the SAHPRA package inserts (warnings, contraindications, approved indications), a blocking gap for safety screening
- Mechanism of action data, for example from DrugBank
- Targeted literature search for a biological rationale linking phenylalanine to sclerosing cholangitis
- Preclinical evidence of benefit and safety in cholestatic liver disease
- Verification of the Adco-Ipratropium registration link
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

