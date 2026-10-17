---
layout: default
title: Darunavir
parent: Moderate Evidence (L3-L4)
nav_order: 164
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-15
description: "Darunavir: predicted new indication Simian immunodeficiency virus infection (evidence level L4). Approved use: HIV infection / AIDS"
monitor_inn: "DARUNAVIR"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
---

# Darunavir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

# Darunavir: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Darunavir is an HIV-1 protease inhibitor, originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, but there are **no registered clinical trials** and only **4 publications**, all preclinical studies in macaques that mainly tested antiretroviral combinations rather than darunavir alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection / AIDS (the registration record in South Africa has no approved indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Darunavir is a known HIV-1 protease inhibitor, and its efficacy in HIV infection is established.

SIV is a lentivirus closely related to HIV, and its protease is homologous to HIV protease. It is therefore biologically plausible that a protease inhibitor would act on SIV, which fits the high TxGNN score.

This prediction has little repurposing value for human use. SIV infection occurs in non-human primates and is mainly relevant as a research model for HIV cure and viral reservoir studies. Darunavir is already approved for HIV in humans, so this is not a new human indication.

Other predictions from the model were weaker:
- **Feline acquired immunodeficiency syndrome (veterinary):** a mechanistic rationale exists, but FIV protease differs from HIV-1 protease in substrate specificity and inhibitor sensitivity. No trials or literature were found.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter:** no clear mechanistic link was identified, and the score likely reflects knowledge-graph artifacts.
- **Obsolete familial combined hyperlipidemia:** the disease term is obsolete, and protease inhibitors are associated with dyslipidaemia as an adverse effect, which argues against benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Preclinical (non-human primate) | PLoS One | Suppressive combination ART plus the HDAC inhibitor SAHA in SIV-infected Chinese rhesus macaques, as a model of viral reservoirs |
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Preclinical (non-human primate) | AIDS Res Hum Retroviruses | Comparison of two coformulated injectable cART regimens in SIVmac239-infected rhesus macaques |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Preclinical (non-human primate) | PLoS Pathog | Highly intensified multidrug ART induced long-term viral suppression and restricted the viral reservoir in a simian AIDS model |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Preclinical (non-human primate) | AIDS | Auranofin restricted the viral reservoir in the monkey AIDS model and contained viral load after ART suspension |

All four studies are indirect: they test ART regimens or adjunct agents, not darunavir alone.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 56/20.2.8/0838 | Ronivid 400/50 Mg | Film-coated tablet (Fct) | Not stated in the data compiled for this report |

Essential Medicines List (EML) inclusion status is not available in the data compiled for this report.

---

## Safety Considerations

**Knowledge-graph contraindication signals** (from drug-disease relationships, not from label text, so they must be verified against the Professional Information):
- Liver failure, liver disease, cirrhosis of liver
- Chronic hepatitis B and C virus infection
- Gallbladder disease
- Hyperglycaemia, diabetes mellitus, diabetic ketoacidosis
- Hypertriglyceridaemia
- Haemophilia

**Drug Interactions:** 100 interactions were identified in the DDInter database. Most listed ones are Moderate, including:
- Antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, saxagliptin, canagliflozin, dapagliflozin, albiglutide, chlorpropamide, acetohexamide)
- Corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone)
- Aprepitant and clarithromycin
- **Major:** cisapride

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence is four indirect preclinical macaque studies, with no clinical trials. SIV infection is not a human disease, so the prediction adds little repurposing value beyond darunavir's existing HIV indication.

**To proceed, the following is needed:**
- Retrieve the SAHPRA package insert to obtain warnings, contraindications and the approved indication (a blocking gap for safety screening)
- Obtain detailed mechanism of action data from DrugBank
- Studies testing darunavir specifically against SIV, if the research question is to be pursued
- Confirm whether any research or veterinary use justifies further evaluation, since the other predicted indications (feline AIDS, the rare neurodevelopmental disorder, obsolete hyperlipidaemia) have no supporting evidence and the last carries a possible safety concern
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

