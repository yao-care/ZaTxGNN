---
layout: default
title: Imatinib
parent: Model Prediction Only (L5)
nav_order: 259
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Imatinib: predicted new indication Heart fibrosarcoma (evidence level L5). Approved use: Chronic myelogenous leukaemia (BCR-ABL1 positive), GIST…"
monitor_inn: "Imatinib"
predicted_indications: ["heart fibrosarcoma", "fibroblastic neoplasm", "conventional fibrosarcoma", "kidney fibrosarcoma", "low grade fibromyxoid sarcoma", "liposarcoma", "liver fibrosarcoma", "autosomal recessive familial Mediterranean fever", "ovarian myxoid liposarcoma", "familial rhabdoid tumor"]
---

# Imatinib
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

## Imatinib: From Systemic Mastocytosis, GIST and CML to Heart Fibrosarcoma
{: .text-alpha }

## One-Sentence Summary

Imatinib is a tyrosine kinase inhibitor originally used for chronic myelogenous leukaemia, gastrointestinal stromal tumour (GIST), systemic mastocytosis, dermatofibrosarcoma protuberans (DFSP) and hypereosinophilic syndromes.
The TxGNN model's top-ranked prediction is **heart fibrosarcoma**, but there are **no clinical trials** and only **1 publication** (a general 2008 review of imatinib indications) for this specific disease.
The evidence is essentially model prediction plus mechanistic extrapolation, so this top-ranked prediction should be treated as a hypothesis, not a finding.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myelogenous leukaemia (BCR-ABL1 positive), GIST, systemic mastocytosis, DFSP, hypereosinophilic syndrome (the SAHPRA record has no indication text; these come from the knowledge graph) |
| Predicted New Indication | Heart fibrosarcoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 (rank 1 prediction; no trials, mechanistic extrapolation only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not available in the data compiled for this report. Imatinib is generally known as an inhibitor of the PDGFR, KIT and ABL kinases, and the literature retrieved for this report describes it in those terms.

The mechanistic argument for heart fibrosarcoma is an extrapolation from DFSP, which is already an imatinib indication. DFSP carries a COL1A1-PDGFB fusion that drives constitutive PDGFR signalling, and imatinib blocks it. There is no direct data on primary cardiac fibrosarcoma, and it is unknown whether such tumours share this PDGFB-dependent biology. The prediction should therefore be read as plausible but unproven.

The wider list of predictions shows the same pattern:
- **Fibroblastic neoplasm** (rank 2, score 99.94%): largely a re-labelling of the existing DFSP indication, supported by reviews and the 2025 European DFSP guideline. Evidence level L3. It is the best-supported item in the list, but it is not a new use.
- **Liposarcoma** (rank 6): three Phase 1/2 or Phase 2 sarcoma trials exist, but they enrolled mixed histologies. Liposarcoma is typically driven by MDM2/CDK4 amplification, not KIT or PDGFR, so the mechanistic link is weak.
- **Conventional fibrosarcoma, kidney fibrosarcoma, low grade fibromyxoid sarcoma, liver fibrosarcoma, familial Mediterranean fever, ovarian myxoid liposarcoma and familial rhabdoid tumour**: indirect, unrelated or absent evidence. The high scores for several of these are likely graph-based artefacts.

## Clinical Trial Evidence

No clinical trials were registered for heart fibrosarcoma. Currently no related clinical trials registered.

Trials found for other predicted indications are not evidence for this one, but give context on imatinib in sarcomas:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00031915](https://clinicaltrials.gov/study/NCT00031915) | Phase 2 | Completed | Not reported | Imatinib in metastatic or unresectable soft tissue and bone sarcoma (liposarcoma-specific results not provided) |
| [NCT00006357](https://clinicaltrials.gov/study/NCT00006357) | Phase 1/2 | Completed | 91 | Dose-finding and activity of STI571 (imatinib) in advanced soft tissue sarcoma |
| [NCT00154388](https://clinicaltrials.gov/study/NCT00154388) | Phase 2 | Completed | 185 | Exploratory basket study in life-threatening rare malignancies; not histology-specific |

## Literature Evidence

Heart fibrosarcoma, the top-ranked prediction, has one retrieved publication. The table also lists the most relevant imatinib-sarcoma publications retrieved for related predictions.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Review | Prescrire International | Heart fibrosarcoma: review of imatinib's expanding indications, concluding that the new indications lack robust evidence |
| [19451433](https://pubmed.ncbi.nlm.nih.gov/19451433/) | 2009 | Phase 2 trial | J Clin Oncol | Multicentre Phase 2 trial of imatinib across 10 sarcoma subtypes (liposarcoma list) |
| [39904126](https://pubmed.ncbi.nlm.nih.gov/39904126/) | 2025 | Guideline | Eur J Cancer | European interdisciplinary guideline update (2024) on DFSP diagnosis and treatment (fibroblastic neoplasm list) |
| [42062942](https://pubmed.ncbi.nlm.nih.gov/42062942/) | 2026 | Cohort | BMC Cancer | 153 Chinese DFSP patients: COL1A1::PDGFB prevalence and outcomes with Mohs surgery plus postoperative imatinib |
| [25852058](https://pubmed.ncbi.nlm.nih.gov/25852058/) | 2015 | Cohort/Molecular | Mol Cancer Ther | CDK4 as a therapeutic target in imatinib-resistant DFSP (conventional fibrosarcoma list) |
| [30901500](https://pubmed.ncbi.nlm.nih.gov/30901500/) | 2019 | Preclinical | Drug Dev Res | Liposomal/nanocochleate imatinib plus dexketoprofen against fibrosarcoma (preclinical only) |
| [15794712](https://pubmed.ncbi.nlm.nih.gov/15794712/) | 2005 | Review | Expert Opin Drug Saf | Development and application of imatinib |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 42/34/0496 | Imavec | Capsule (oral) | Not available in the compiled data |

One valid single-ingredient registration, no cancelled registrations. Essential Medicines List status was not available in the compiled data.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Professional Information (PI) warnings and precautions. The knowledge graph links imatinib with neutropenia, thrombocytopenia, anaemia and agranulocytosis as cautions |
| Emetogenicity Classification | Please refer to the Professional Information (PI) warnings and precautions |
| Monitoring Items | FBC, liver function, renal function, fluid status and cardiac status (based on the knowledge-graph cautions below) |
| Handling Protection | Please refer to the Professional Information (PI) warnings and precautions |

## Safety Considerations

The SAHPRA package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for authoritative safety information. Report adverse drug reactions to SAHPRA.

**Knowledge-graph cautions (not label text):** the TxGNN knowledge graph links imatinib with contraindication-type relationships for many conditions. They include:
- Cardiac and fluid: congestive heart failure, heart failure, coronary artery disease, heart valve disease, congenital heart disease, pericardial effusion, pulmonary edema, brain edema, hypertension
- Liver and biliary: liver failure, liver disease, gallbladder disease, hyperbilirubinemia, Gilbert syndrome
- Kidney: kidney disease
- Haematological: thrombocytopenia, neutropenia, agranulocytosis, anaemia
- Metabolic: diabetes mellitus, diabetic ketoacidosis, obesity disorder, hypophosphatemia
- Other: active peptic ulcer disease, pyoureter

These are graph associations and should be verified against the PI.

**Drug interactions:** 100 interactions were recorded (DDInter); the first 20 returned include the following.
- **Major:** eliglustat, naloxegol
- **Moderate (examples):** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), clarithromycin, cimetidine, aprepitant, morphine, naltrexone, pioglitazone, glimepiride, saxagliptin, lansoprazole, dexlansoprazole

A specific safety signal in the literature: a case report (PMID 30096127) describes imatinib-induced DRESS (drug reaction with eosinophilia and systemic symptoms) in a patient with DFSP, who was managed with desensitisation.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Heart fibrosarcoma has no registered trials and only a general review, so the high TxGNN score (99.94%) is not backed by disease-specific evidence. The best-supported prediction, fibroblastic neoplasm (L3), mainly restates the already-established DFSP indication. Safety information from the SAHPRA label is also missing.

**To proceed, the following is needed:**
- Disease-specific evidence for cardiac fibrosarcoma, such as case series reporting PDGFB fusion or PDGFR/KIT status and imatinib response
- Molecular testing (COL1A1-PDGFB fusion) in candidate patients, since benefit is likely confined to PDGFB-driven tumours
- SAHPRA package insert warnings and contraindications for Imavec, to complete safety screening
- Mechanism of action data for imatinib, to firm up the mechanistic-link analysis
- The SAHPRA-approved indication text, and EML status, for the Imavec registration
- Evaluation of the second-ranked fibroblastic neoplasm as a separate, lower-risk question focused on the PDGFB-fusion DFSP subset, where current evidence is strongest
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

