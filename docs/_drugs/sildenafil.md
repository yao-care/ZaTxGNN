---
layout: default
title: Sildenafil
parent: Model Prediction Only (L5)
nav_order: 419
evidence_level: L5
indication_count: 10
---

# Sildenafil
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

# Sildenafil: From Pulmonary Arterial Hypertension and Erectile Dysfunction to Genetic Alopecia

## One-Sentence Summary

Sildenafil is a PDE5 inhibitor originally used for pulmonary arterial hypertension, erectile dysfunction, psychologic dyspareunia and premature ejaculation.
The TxGNN model's top-ranked prediction is **Ambras type hypertrichosis universalis congenita**, but it has no supporting trials or publications. The most biologically coherent signal among the top 10 predictions is **genetic alopecia**, with **0 clinical trials** and **1 publication** (a 2018 exploratory report on hair growth).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension, erectile dysfunction, psychologic dyspareunia, premature ejaculation (from the TxGNN knowledge graph; no approved indication text is available from the SAHPRA records) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita (rank 1). Genetic alopecia (rank 9) is the best-supported prediction. |
| TxGNN Prediction Score | 98.41% (rank 1); 75.03% (genetic alopecia) |
| Evidence Level | L5 (rank 1 prediction); L4 (genetic alopecia) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold (rank 1 prediction). Genetic alopecia is classed as a research question. |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this report. Sildenafil is known to be a phosphodiesterase type 5 (PDE5) inhibitor. It raises intracellular cGMP and causes vasodilation, which underlies its use in pulmonary arterial hypertension and erectile dysfunction.

For the top-ranked prediction, Ambras type hypertrichosis universalis congenita, the score is graph-based only. No clinical trials or publications support it. The link would be speculative, perhaps through shared hair-follicle or vascular signalling, and a mechanistic rationale cannot be built from the available data. The same applies to the other predictions in the top 10 (malformation syndromes, Dandy-Walker syndrome, hair shaft abnormalities, lipid disorders, trichomegaly and an obsolete skeletal syndrome). None has clinical evidence, and no plausible PDE5-related mechanism is evident.

Two predictions have some supporting context:

- **Genetic alopecia (rank 9):** A 2018 report describes a hair-growth effect of sildenafil. A plausible mechanism is cGMP-mediated vasodilation and increased perifollicular blood flow, which may support the anagen (growth) phase. This is the most biologically coherent signal in the set, but it remains exploratory.
- **Hypertrichosis (rank 5):** The only publication is a case report of glibenclamide (not sildenafil) in Cantú syndrome. It provides only indirect context on K-ATP channel and vascular biology. Cantú syndrome patients have vasodilatory and cardiovascular features, so safety would need careful consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the top 10 predicted indications.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30292404](https://pubmed.ncbi.nlm.nih.gov/30292404/) | 2018 | Preclinical/exploratory report (design not specified) | Biochem Biophys Res Commun | Reports a novel effect of sildenafil on hair growth. It is a PDE5 inhibitor that raises cGMP; its effect on human hair follicles was previously unknown. (Genetic alopecia) |
| [31175705](https://pubmed.ncbi.nlm.nih.gov/31175705/) | 2019 | Case report | Am J Med Genet A | Glibenclamide treatment in a neonate with Cantú syndrome (ABCC9 gain-of-function variant). It concerns glibenclamide, not sildenafil, and gives only indirect, mechanism-adjacent context. (Hypertrichosis) |

---

## South Africa Market Information

All 4 registrations are valid single-ingredient products. No approved indication text, manufacturer or Essential Medicines List (EML) status is available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 42/7.1.5/1071 | Dynafil | Tablet | Not available |
| Reg. No. 50/7.1.5/0062 | Lifaned 50 | Film-coated tablet (Fct) | Not available |
| Reg. No. 43/7.1.5/0887 | Avigra | Tablet | Not available |
| Reg. No. 45/7.1.5/0874 | Raviag | Tablet | Not available |

---

## Safety Considerations

SAHPRA package insert warnings and contraindications were not available for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Contraindication-related conditions from the knowledge graph** (these are drug-disease edges, not label text, and must be verified against the PI):
- **Cardiovascular:** aortic stenosis and other aortic valve disease, hypotensive disorder, acute coronary syndrome, myocardial infarction, coronary thrombosis, hypertrophic cardiomyopathy (including familial), pulmonary veno-occlusive disease, stroke and cerebrovascular disorders, cerebral infarction
- **Haematological:** sickle cell anaemia, hereditary persistence of fetal haemoglobin, haemoglobinopathy, plasma cell myeloma, leukaemia
- **Genitourinary:** priapism, Peyronie disease (penile fibromatosis), balanitis xerotica obliterans
- **Other:** liver failure, anterior ischaemic optic neuropathy, hearing loss disorders, oesophageal dyskinesia

**Drug interactions:** The interaction screen returned 100 interactions in total, and 20 are shown in the data compiled for this report.
- **Major:** Clarithromycin
- **Moderate:** aprepitant, morphine, dexamethasone, lorcaserin, canagliflozin, cimetidine, dapagliflozin, eluxadoline, empagliflozin, sapropterin, miconazole, clotrimazole, ertugliflozin, opium, papaverine, troglitazone
- **Unknown severity:** calcitriol, acarbose, sucralfate

Cantú syndrome and similar vasodilatory conditions would need particular attention to hypotension risk.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predictions rest only on graph-based scores. No clinical trials exist, and literature is absent or indirect. Genetic alopecia has one exploratory hair-growth report and a plausible vasodilation mechanism, so it is best treated as a research question rather than a candidate for clinical use.

**To proceed, the following is needed:**
- Mechanism of action data (a DrugBank query)
- SAHPRA package insert warnings and contraindications (a blocking gap that prevents safety screening)
- Controlled human studies of sildenafil in genetic alopecia, with the study design of PMID 30292404 clarified
- A safety assessment for any new route or population, particularly hypotension and the cardiovascular contraindications listed above
- Confirmation of approved indications and EML status for the four SAHPRA-registered products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

