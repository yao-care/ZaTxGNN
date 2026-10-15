---
layout: default
title: Lopinavir
parent: Model Prediction Only (L5)
nav_order: 301
evidence_level: L5
indication_count: 3
---

# Lopinavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Lopinavir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Lopinavir is an HIV protease inhibitor, originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but this is a model prediction only, with **no clinical trials** and **no publications** currently supporting this specific indication.
The top-ranked prediction is also an animal disease, so its relevance to human practice in South Africa is limited.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection / AIDS (the SAHPRA records compiled for this report contain no approved indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Lopinavir is a known HIV-1 protease inhibitor. Its efficacy in HIV infection is established, and the reasoning below draws on general pharmacological knowledge rather than the supplied data.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV-1, so a protease inhibitor is plausible as an antiviral. However, FIV protease differs from HIV-1 protease in substrate specificity and inhibitor sensitivity. Published work suggests HIV-1 protease inhibitors are not reliably active against it. The very high TxGNN score most likely reflects proximity in the knowledge graph rather than demonstrated biology.

The other two predictions are weaker still:
- **Simian immunodeficiency virus (SIV) infection** (score 99.90%, evidence level L4): SIV is a primate model of HIV and largely duplicates the original indication. It has little standalone value as a human repurposing target. Three preclinical macaque studies exist, listed below.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 99.90%, evidence level L5): No mechanistic link could be established. It is a rare genetic disorder with no known rationale for a protease inhibitor, and there are no trials or publications.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked predicted indication (feline acquired immunodeficiency syndrome), nor for the other two predicted indications.

## Literature Evidence

No literature is available for the top-ranked indication. The three publications below relate to the second-ranked prediction, SIV infection. All are preclinical studies in nonhuman primates and provide only indirect support.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Preclinical (nonhuman primate) | Journal of Virology | Viral decay in SIV-infected macaques given a 7-day quadruple antiretroviral regimen, used to compare viral dynamics with HIV-1 |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Preclinical (SHIV model construction) | Microbes and Infection | Built a SHIV carrying the HIV-1 protease gene, intended as a tool for testing protease inhibitors in vivo; replication was blocked by a protease inhibitor in cell culture |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Preclinical (nonhuman primate) | Journal of Virological Methods | Oral AZT + 3TC + lopinavir/ritonavir in SHIV 89.6P-infected macaques, assessing effects on the CD8 subset |

## South Africa Market Information

Lopinavir has 3 valid single-ingredient registrations with SAHPRA. No approved indication text or manufacturer details were available in the data compiled for this report. Essential Medicines List (EML) status was not available in the data.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 43/20.2.8/0356 | Aluvia 100/25 | Tablet | Not available |
| Reg. No. 51/20.2.8/0123 | Lopimune 40/10 Oral Pellets | Capsule | Not available |
| Reg. No. 55/20.2.8/0388 | Quadrimune | Capsule | Not available |

## Safety Considerations

**Contraindication-related conditions (from the TxGNN knowledge graph, not label text):**
The knowledge graph links lopinavir to the following conditions as contraindications or cautions. These should be verified against the SAHPRA-approved Professional Information (PI).
- **Cardiac and conduction:** long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease, atrioventricular block, myocardial ischaemia, coronary artery disease, cardiomyopathy (including hypertrophic), endomyocardial fibrosis, myocardial disorder
- **Hepatic and biliary:** liver disease, cirrhosis, gallbladder disease, chronic hepatitis B and C infection, hyperbilirubinaemia (including hereditary and Gilbert syndrome)
- **Metabolic:** pancreatitis, hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, hypertriglyceridaemia, familial combined hyperlipidaemia, potassium deficiency
- **Haematological:** haemophilia

**Drug Interactions:** 65 interactions were identified in total; the main ones are listed below (first 20 shown in the data).
- **Major:** dolasetron, papaverine
- **Moderate:** acarbose, bisacodyl, castor oil, dapagliflozin, famotidine, glycerin, lactitol, lactulose, levofloxacin, magnesium citrate, magnesium hydroxide, metformin, mineral oil, ondansetron, palonosetron, phenolphthalein
- **Minor:** cimetidine, clotrimazole

The QT-related conditions and the major and moderate interactions with QT-prolonging agents (dolasetron, ondansetron, palonosetron, levofloxacin) point to cardiac conduction as a key safety theme.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications, as label-based data were not available. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest on model scores alone. The top-ranked indication is a veterinary disease with no trials or literature, and published work suggests HIV-1 protease inhibitors are not reliably active against FIV protease. The second is an animal model of HIV that duplicates the existing indication, and the third has no plausible mechanism. None represents a credible human repurposing opportunity at present.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical evidence of lopinavir activity against the relevant target, such as FIV protease, if the veterinary direction is pursued
- A target-level hypothesis and preclinical validation for the neurodevelopmental disorder prediction, if it is to be considered
- Review of other TxGNN predictions beyond the top three for human diseases with a stronger mechanistic basis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

