---
layout: default
title: Temozolomide
parent: Model Prediction Only (L5)
nav_order: 437
evidence_level: L5
indication_count: 1
monitor_inn: "TEMOZOLOMIDE"
predicted_indications: ["cauda equina neoplasm"]
last_modified_at: 2026-10-29
description: "Temozolomide: predicted new indication Cauda equina neoplasm (evidence level L5). Approved use: Anaplastic astrocytoma, astrocytoma (excluding glioblastoma)…"
---

# Temozolomide
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

## Temozolomide: From Anaplastic Astrocytoma to Cauda Equina Neoplasm
{: .text-alpha }

## One-Sentence Summary

Temozolomide is an oral alkylating chemotherapy agent. The knowledge graph records it for anaplastic astrocytoma, astrocytoma (excluding glioblastoma) and brain glioblastoma. The TxGNN model predicts it may be useful for **cauda equina neoplasm**, but no clinical trials are registered and the only support is **3 publications**, one of which is a single case report on a closely related tumour (spinal myxopapillary ependymoma).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anaplastic astrocytoma, astrocytoma (excluding glioblastoma), brain glioblastoma (relations recorded in the knowledge graph; the local licence contains no indication text) |
| Predicted New Indication | Cauda equina neoplasm |
| TxGNN Prediction Score | 0.9930 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, temozolomide is an oral alkylating agent that methylates DNA (notably at O6-guanine). This causes cytotoxic lesions and cell death, particularly in tumour cells with low MGMT expression. It crosses the blood-brain barrier.

Cauda equina tumours are mostly neuroepithelial tumours of the spinal canal, most commonly myxopapillary ependymoma. They are therefore biologically related to the CNS gliomas for which temozolomide is recorded in the knowledge graph. This gives the prediction some biological plausibility.

Two caveats apply. The score is a computational prediction, not clinical evidence. No MGMT status data for this tumour type are available in the data compiled for this report.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29270703](https://pubmed.ncbi.nlm.nih.gov/29270703/) | 2018 | Case report | Eur Spine J | Temozolomide showed remarkable efficacy in a recurrent spinal myxopapillary ependymoma with cerebrospinal dissemination (single patient plus literature review) |
| [42760727](https://pubmed.ncbi.nlm.nih.gov/42760727/) | 2026 | Case report | Medicine | Nasal NUT carcinoma managed with multimodal treatment including radiotherapy; not directly about cauda equina neoplasm |
| [18706663](https://pubmed.ncbi.nlm.nih.gov/18706663/) | 2009 | Case report | Neuro-Chirurgie | Neuromeningeal cryptococcosis in a child treated for pontine glioma; not directly about cauda equina neoplasm |

Only the first report is relevant to this prediction, and it concerns a related tumour type rather than "cauda equina neoplasm" itself. No cited study directly addresses the predicted disease, so the evidence level is L5.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 32/26/0724 | Temodal 250 Mg Capsules | Capsule | Not stated in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | Medium to high. The knowledge graph records contraindication relations with neutropenia, thrombocytopenia, pancytopenia, lymphopenia, aplastic anaemia and agranulocytosis |
| Emetogenicity Classification | Please refer to the Professional Information (PI) warnings and precautions |
| Monitoring Items | FBC with differential, liver function and renal function |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindication relations in the knowledge graph (not label text):** liver failure, thrombocytopenia, neutropenia, agranulocytosis, anaemia, macrocytic anaemia, pneumocystosis, pancytopenia, lymphopenia, myelodysplastic syndrome, idiopathic aplastic anaemia, aplastic anaemia.
- **Drug interactions:** 100 interactions were found in total. The listed ones include a moderate interaction with naltrexone and a minor interaction with levofloxacin. Many others (for example pantoprazole, omeprazole, lansoprazole, metformin, morphine, prednisone, hydrocortisone, doxycycline, amphotericin B) have an unknown severity grade and need checking against the PI.

Please refer to the SAHPRA-approved Professional Information (PI) for label warnings and contraindications, which were not available for this report. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no registered trials and no study that directly addresses cauda equina neoplasm. The only relevant evidence is one case report in a related tumour. The SAHPRA label warnings were also unavailable, so the safety review cannot proceed.

**To proceed, the following is needed:**
- Obtain and review the SAHPRA Professional Information, including indications, warnings and contraindications.
- Gather studies that directly address cauda equina tumours (for example myxopapillary ependymoma series or trials) and assess MGMT status data.
- Confirm the mechanism of action data from DrugBank.
- Design a haematological monitoring plan, given the myelosuppression-related contraindication relations.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

