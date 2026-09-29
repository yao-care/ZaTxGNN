---
layout: default
title: Temozolomide
parent: High Evidence (L1-L2)
nav_order: 434
evidence_level: L1
indication_count: 2
---

# Temozolomide
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **2** 
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

# Temozolomide: From an Unspecified Original Indication to Adult Astrocytic Tumour

## One-Sentence Summary

Temozolomide is an oral alkylating chemotherapy agent. The source data lists no original indication for it, although it is an established standard-of-care drug for glioblastoma and anaplastic astrocytoma.
The TxGNN model predicts it may be effective for **adult astrocytic tumour**, with **2 registered clinical trials** and **20 publications** currently supporting this direction.
The "new" indication is probably a labelling gap in the source data rather than a true repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the SAHPRA registration record has no indication text) |
| Predicted New Indication | Adult astrocytic tumour |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, temozolomide is an oral DNA alkylating agent that forms O6-methylguanine adducts and crosses the blood-brain barrier. Its activity depends largely on MGMT promoter methylation status.

Astrocytic tumours, including glioblastoma and anaplastic astrocytoma, are the main setting in which temozolomide is used. The very high TxGNN score agrees with the clinical evidence below. Because the original indication field is empty, this prediction is best read as confirming an established use rather than identifying a new one.

A second prediction, **cauda equina neoplasm** (score 99.30%), rests only on a single case report in relapsed spinal myxopapillary ependymoma. It has no registered trials and is a research question only (Evidence Level L4). The other PMID listed for it (cryptococcosis in a child with pontine glioma) is a keyword mismatch and is not evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | Completed | 500 | Randomised comparison of temozolomide vs PCV (procarbazine, lomustine, vincristine) in recurrent WHO grade III and IV astrocytic tumours; direct head-to-head evidence in the target disease |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | Completed | 26 | Dose-finding and PK/safety study of XL184 (cabozantinib) with temozolomide and radiotherapy in first-line glioblastoma; combination safety data, not efficacy evidence |

No SANCTR or PACTR identifiers were found in the Evidence Pack.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | RCT | N Engl J Med | Radiotherapy plus concomitant and adjuvant temozolomide compared with radiotherapy alone in glioblastoma (efficacy and safety) |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | RCT (5-year follow-up) | Lancet Oncol | 5-year analysis of the EORTC-NCIC phase III trial of radiotherapy with temozolomide vs radiotherapy alone |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | RCT | Lancet | CeTeG/NOA-09: lomustine-temozolomide vs standard temozolomide in newly diagnosed MGMT-methylated glioblastoma |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | RCT | JAMA | Tumour-treating fields plus maintenance temozolomide vs temozolomide alone in glioblastoma |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | RCT | N Engl J Med | Bevacizumab added to temozolomide and radiotherapy in newly diagnosed glioblastoma |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | RCT | Lancet Oncol | NOA-08: dose-dense temozolomide alone vs radiotherapy alone in elderly patients with malignant astrocytoma |
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | RCT (Phase 2/3) | J Clin Oncol | NRG BN007: dual immune checkpoint blockade in MGMT-unmethylated newly diagnosed glioblastoma |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Review | JAMA | Review of glioblastoma and other primary brain malignancies in adults |
| [25920709](https://pubmed.ncbi.nlm.nih.gov/25920709/) | 2015 | Clinical trial report | J Neurooncol | Radiotherapy and temozolomide in anaplastic astrocytoma and anaplastic oligo-astrocytoma |
| [10914698](https://pubmed.ncbi.nlm.nih.gov/10914698/) | 2000 | Review | Clin Cancer Res | Early overview of temozolomide in malignant glioma |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 32/26/0724 | Temodal 250 Mg Capsules | Capsule | Not recorded in the registration data |

Essential Medicines List (EML) inclusion status is not available in the Evidence Pack.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, imidazotetrazine class) |
| Myelosuppression Risk | Please refer to the Professional Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Professional Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI; haematological parameters (FBC) and liver function are generally monitored for cytotoxic agents |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Phase 3 randomised evidence (NCT00052455 and multiple published RCTs, including the EORTC-NCIC trial) supports temozolomide in astrocytic tumours, and the drug is marketed in South Africa. The prediction most likely reflects a gap in the source labelling rather than a new use.

**To proceed, the following is needed:**
- Confirm the SAHPRA-labelled indication from the package insert (currently missing; this blocks safety screening)
- Confirm MGMT promoter status, WHO grade and IDH status, and the treatment setting (newly diagnosed vs recurrent, with or without radiotherapy)
- Detailed mechanism of action data from DrugBank
- Safety and drug interaction data from the PI
- For the cauda equina neoplasm prediction: multidisciplinary tumour-board review and a prospective or registry-based evaluation before any use

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

