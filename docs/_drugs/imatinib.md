---
layout: default
title: Imatinib
parent: 僅模型預測 (L5)
nav_order: 200
evidence_level: L5
indication_count: 10
---

# Imatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Imatinib: From Chronic Myeloid Leukaemia to Fibroblastic Neoplasms

## One-Sentence Summary

Imatinib (Gleevec/Glivec) is a targeted tyrosine kinase inhibitor originally approved for chronic myeloid leukaemia (CML) and gastrointestinal stromal tumours (GIST), acting by blocking BCR-ABL, c-KIT, and PDGFR kinases. Across ten TxGNN-predicted indications, the most compelling is **fibroblastic neoplasm** — encompassing Dermatofibrosarcoma Protuberans (DFSP) — which is already FDA-approved and supported by a **2025 European interdisciplinary guideline** and **20 publications**, representing Level L1 evidence and a "Proceed with Guardrails" recommendation. The remaining nine predicted indications carry substantially weaker or absent evidentiary support and are either held or flagged as research questions pending biomarker-driven study design.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic myeloid leukaemia (CML); gastrointestinal stromal tumours (GIST) |
| Primary Predicted Indication (Best Evidence) | Fibroblastic neoplasm (Dermatofibrosarcoma Protuberans) |
| TxGNN Prediction Score | 99.94% (model rank #601) |
| Evidence Level | L1 |
| South Africa Market Status | Not registered with SAHPRA (data as of 2026-04-04) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Proceed with Guardrails** (Fibroblastic neoplasm/DFSP) |

> **Multi-indication note:** This is a multi-indication evaluation (Candidate ID: TW-DB00619-multi). The report focuses on the best-supported prediction (Rank 2: fibroblastic neoplasm). A full summary of all ten predictions is presented in the table below.

---

## All Predicted Indications at a Glance

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|-------------|----------------|---------|
| 1 | Heart fibrosarcoma | 99.94% | L4 | Hold |
| **2** | **Fibroblastic neoplasm (DFSP)** | **99.94%** | **L1** | **Proceed with Guardrails** |
| 3 | Conventional fibrosarcoma | 99.93% | L2 | Research Question |
| 4 | Kidney fibrosarcoma | 99.93% | L3 | Research Question |
| 5 | Low grade fibromyxoid sarcoma | 99.93% | L5 | Hold |
| 6 | Liposarcoma | 99.88% | L2 | Research Question |
| 7 | Liver fibrosarcoma | 99.86% | L4 | Hold |
| 8 | Autosomal recessive familial Mediterranean fever | 99.86% | L5 | Hold |
| 9 | Ovarian myxoid liposarcoma | 99.85% | L5 | Hold |
| 10 | Familial rhabdoid tumour | 99.83% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Imatinib is a small-molecule competitive inhibitor of several receptor tyrosine kinases, most importantly BCR-ABL (the constitutively active fusion kinase that drives CML), c-KIT (mutated in most GISTs), PDGFR-α, and PDGFR-β. Rather than broadly poisoning dividing cells as conventional chemotherapy does, imatinib slots into the ATP-binding pocket of these specific kinases and switches off their signalling. Its success in CML — transforming a previously fatal leukaemia into a manageable chronic condition — established the proof of concept that blocking a single aberrant kinase can fundamentally alter cancer biology.

The connection to **fibroblastic neoplasms**, and to Dermatofibrosarcoma Protuberans (DFSP) in particular, is mechanistically direct and unusually well-defined. DFSP is characterised in over 90% of cases by a chromosomal translocation t(17;22)(q22;q13), which fuses the collagen gene COL1A1 with the platelet-derived growth factor B (PDGFB) gene. The resulting fusion protein is constitutively secreted and binds PDGFR-β in an autocrine loop, driving relentless fibroblastic proliferation. Imatinib's selective PDGFR-β inhibition directly severs this growth signal — the same mechanism by which it works in GIST (via KIT inhibition), just targeting a different kinase in the same family. The 2025 European interdisciplinary guideline (PMID 39904126) continues to endorse imatinib as the standard systemic option for advanced or unresectable DFSP, and the FDA has approved this indication for adults since 2006.

The TxGNN model's high-confidence prediction for this category therefore confirms established regulatory science rather than generating a speculative hypothesis — a valuable validation of the model's mechanistic reasoning. Where the model extends predictions to rarer or more molecularly heterogeneous entities (conventional fibrosarcoma, kidney fibrosarcoma, liposarcoma), biological plausibility depends heavily on whether individual tumours express imatinib-sensitive targets (PDGFR, KIT), meaning biomarker pre-screening is essential before any clinical application beyond DFSP.

---

## Clinical Trial Evidence

No dedicated clinical trials were retrieved for the fibroblastic neoplasm query directly, but highly relevant completed trials covering DFSP and PDGFR-expressing sarcomas are available from the overlapping conventional fibrosarcoma and soft tissue sarcoma queries:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT00085475](https://clinicaltrials.gov/study/NCT00085475) | Phase II | Completed | 17 | Imatinib in locally advanced or metastatic DFSP and Giant Cell Fibroblastoma harbouring the t(17;22) COL1A1/PDGF-β translocation; demonstrated objective responses in biomarker-positive patients — the most directly relevant DFSP-specific imatinib trial |
| [NCT00154388](https://clinicaltrials.gov/study/NCT00154388) | Phase II | Completed | 185 | Broad exploratory study of imatinib in life-threatening malignant rare diseases with imatinib-sensitive tyrosine kinases; captures rare fibrosarcoma subtypes; provides safety and general efficacy data across rare sarcomas |
| [NCT00006357](https://clinicaltrials.gov/study/NCT00006357) | Phase I/II | Completed | 91 | Dose-finding and efficacy study of imatinib (STI571) in advanced soft tissue sarcoma; includes fibrosarcoma and liposarcoma subgroups; most directly powered study for the sarcoma class |
| [NCT00031915](https://clinicaltrials.gov/study/NCT00031915) | Phase II | Completed | Not reported | North American Sarcoma Study Group multi-centre Phase II trial of imatinib in metastatic or unresectable soft tissue and bone sarcoma; enrolment data missing, limiting statistical evaluation |

---

## Literature Evidence

Top publications supporting the fibroblastic neoplasm / DFSP prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39904126](https://pubmed.ncbi.nlm.nih.gov/39904126/) | 2025 | Clinical Practice Guideline | European Journal of Cancer | Updated 2024 European interdisciplinary guideline (EADO/EDF/UEMS/EADV): imatinib recommended as standard systemic therapy for advanced or unresectable DFSP in adults |
| [30297237](https://pubmed.ncbi.nlm.nih.gov/30297237/) | 2018 | Clinical Guideline | Bulletin du Cancer | French national DFSP management guideline; confirms COL1A1-PDGFB translocation as the diagnostic molecular hallmark; imatinib recommended for unresectable or metastatic disease |
| [33449152](https://pubmed.ncbi.nlm.nih.gov/33449152/) | 2021 | Review | Cellular and Molecular Life Sciences | Comprehensive review of PDGFRA/PDGFRB mutations in human disease; establishes PDGFB chromosomal rearrangements as the mechanistic basis of DFSP and related fibroblastic tumours, directly supporting imatinib's PDGFR-β target |
| [28795284](https://pubmed.ncbi.nlm.nih.gov/28795284/) | 2017 | Review | Current Treatment Options in Oncology | Multidisciplinary review of DFSP; imatinib established as systemic option for unresectable cases alongside surgery and radiotherapy |
| [31466588](https://pubmed.ncbi.nlm.nih.gov/31466588/) | 2019 | Review | Dermatologic Clinics | DFSP characterised by COL1A1-PDGFB fusion; imatinib for unresectable or advanced disease; NCCN-endorsed approach |
| [26027711](https://pubmed.ncbi.nlm.nih.gov/26027711/) | 2015 | Review | Expert Review of Anticancer Therapy | Current treatment options for DFSP; PDGFB rearrangement underpins imatinib sensitivity; surgery is primary for localised disease, imatinib is standard for unresectable or metastatic settings |
| [36630365](https://pubmed.ncbi.nlm.nih.gov/36630365/) | 2023 | Review | Clinical and Experimental Dermatology | t(17;22)(q22;q13) found in >90% of DFSP; imatinib as systemic option in advanced DFSP; discusses clinical features, histological subtypes, and management |
| [35038826](https://pubmed.ncbi.nlm.nih.gov/35038826/) | 2022 | Phase II Trial | Cancer Research and Treatment | Phase II trial of imatinib in desmoid tumour (aggressive fibromatosis); whole-genome sequencing identified NOTCH2 and HES1 as potential response biomarkers; expands the mechanistic rationale for imatinib in fibroblastic tumours beyond DFSP |
| [25852058](https://pubmed.ncbi.nlm.nih.gov/25852058/) | 2015 | Translational Research | Molecular Cancer Therapeutics | CDKN2A/p16 loss identified as a driver of imatinib resistance in DFSP; CDK4 proposed as a co-target; important for understanding resistance mechanisms in the fibrosarcomatous DFSP variant |
| [15794712](https://pubmed.ncbi.nlm.nih.gov/15794712/) | 2005 | Review | Expert Opinion on Drug Safety | Foundational review of imatinib's development and mechanism; describes BCR-ABL, KIT, and PDGFR inhibition; positions imatinib for solid tumour applications including fibroblastic neoplasms |

---

## South Africa Market Information

No SAHPRA product registrations for imatinib were identified in the current dataset (0 licences recorded; market status: not registered as of 2026-04-04).

> **Important:** Imatinib (Gleevec/Glivec, Novartis) is a WHO Essential Medicine and is widely used in oncology practice globally. The absence of records in this dataset likely reflects a **data collection gap** rather than true non-availability. South African healthcare professionals should verify the current registration status directly via the [SAHPRA Medicines Control Database](https://www.sahpra.org.za/find-a-medicine/). Imatinib is also available through Novartis's GIPAP (Gleevec International Patient Assistance Program) for qualifying patients.

---

## Cytotoxicity

Imatinib is an antineoplastic agent (targeted therapy). All predicted indications are malignant neoplasms and the original indication involves cancer; this section applies in full.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — small molecule tyrosine kinase inhibitor (TKI); not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | **Moderate** — neutropenia, thrombocytopenia, and anaemia are common; grade 3/4 neutropenia reported in up to 17% of GIST patients at standard doses |
| Emetogenicity Classification | **Low to moderate** (oral administration; nausea is the most common GI complaint but rarely dose-limiting) |
| Monitoring Items | Full blood count (FBC) with differential at baseline and regularly during treatment; liver function tests (LFTs); renal function; weight and oedema assessment (fluid retention is a class effect of PDGFR inhibitors) |
| Handling Protection | Standard precautions for oral antineoplastic agents apply; cytotoxic handling guidelines should be followed per institutional policy and the SANS/NIOH guidelines for handling hazardous pharmaceuticals |

---

## Safety Considerations

Detailed SAHPRA-specific safety data — including local prescribing warnings, contraindications, and South African-registered drug interaction information — were not available in the current dataset.

> Please refer to the SAHPRA-approved Professional Information (PI) for imatinib for complete safety information. Report suspected adverse drug reactions to SAHPRA via the [MedSafety online reporting portal](https://www.sahpra.org.za/pharmacovigilance/). Internationally, known safety concerns include severe fluid retention, hepatotoxicity, cardiac dysfunction, and embryo-foetal toxicity — South African clinicians should review the current PI for full details before prescribing.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(Fibroblastic Neoplasm / DFSP)*

**Rationale:**
Imatinib's activity in DFSP is mechanistically established (COL1A1-PDGFB fusion → constitutive PDGFR-β activation), FDA-approved since 2006, and reaffirmed by the 2025 European interdisciplinary guideline. The TxGNN prediction is validating proven regulatory science — making this among the most straightforward drug repurposing confirmations possible, with L1 evidence supporting clinical use in appropriate patients.

**To proceed, the following is needed:**

- **SAHPRA registration verification:** Confirm imatinib's current SAHPRA registration status and approved indications in South Africa; update the evidence pack with accurate licence data
- **SAHPRA Professional Information (PI):** Obtain the approved South African PI for complete contraindications, warnings, and drug interaction information before any prescribing
- **Local guideline alignment:** Confirm that NCCN and European guideline recommendations for DFSP are incorporated into South African oncology practice standards (via SASOG, SAOA, or equivalent bodies)
- **For Research Question indications (conventional fibrosarcoma, kidney fibrosarcoma, liposarcoma):** Design biomarker-stratified prospective studies using PDGFR/KIT immunohistochemistry or next-generation sequencing (NGS) to identify patient subgroups most likely to benefit before any clinical use outside of registered indications
- **For all Hold indications** (heart fibrosarcoma, low grade fibromyxoid sarcoma, liver fibrosarcoma, familial Mediterranean fever, ovarian myxoid liposarcoma, familial rhabdoid tumour): No clinical use outside formally approved clinical trials; mechanistic links are insufficient or absent at this stage

---

*Data cutoff: 2026-04-04 · Evidence Pack v4 · Candidate ID: TW-DB00619-multi*

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All clinical decisions should be made in accordance with SAHPRA-approved prescribing information and current South African treatment guidelines.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

