---
layout: default
title: Calcium
parent: Model Prediction Only (L5)
nav_order: 89
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Calcium: predicted new indication Thrombotic disease (evidence level L5). Approved use: Not available"
monitor_inn: "Calcium"
predicted_indications: ["thrombotic disease", "hemoglobinopathy", "female breast carcinoma", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "exostosis", "pyropoikilocytosis, hereditary", "vein disease", "non-inflammatory vasculopathy"]
---

# Calcium
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

## Calcium: From an Unspecified Registered Indication to Thrombotic Disease
{: .text-alpha }

## One-Sentence Summary

Calcium is an essential mineral and electrolyte. In South Africa it appears in five registered products, but none of them has an approved indication text in the data compiled for this report.
The TxGNN model predicts it may be effective for **thrombotic disease** (score 98.3%), yet **none of the 2 listed clinical trials tests calcium** and the supporting literature is indirect.
The evidence is model prediction only, and calcium's known physiology suggests it promotes clotting rather than preventing it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the registration data) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 98.25% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for calcium in the data compiled for this report.

Calcium is essential for platelet activation and for several calcium-dependent steps of the coagulation cascade (including clotting factor IV). This points to a **pro-thrombotic** role in normal physiology, not a therapeutic effect against thrombosis. The high TxGNN score probably reflects strong network associations between calcium and clotting biology, not evidence that giving calcium treats or prevents thrombosis. No calcium-specific clinical evidence supports the prediction.

Other lower-ranked predictions have indirect links only:
- **Hemoglobinopathy and beta-thalassemia:** calcium handling and iron metabolism interact, and hypoparathyroidism and bone disease are recognised complications. This supports calcium monitoring or supplementation, not a disease-modifying role.
- **Female breast carcinoma:** calcium signalling features in breast cancer biology, and calcium is commonly co-administered for bone protection during aromatase inhibitor therapy. No trial tests calcium as a cancer treatment.
- **Other predictions** (partial deletion of chromosome 16p, glucophosphate isomerase deficiency anaemia, exostosis, hereditary pyropoikilocytosis, vein disease, non-inflammatory vasculopathy): no plausible therapeutic link or no relevant evidence was found.

## Clinical Trial Evidence

For the top prediction (thrombotic disease):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04319627](https://clinicaltrials.gov/study/NCT04319627) | Phase 3 | Recruiting | 2700 | Statins added to anticoagulation to reduce recurrent venous events in VTE. Does not test calcium. |
| [NCT03692754](https://clinicaltrials.gov/study/NCT03692754) | Phase 2/3 | Unknown | 30 | Atorvastatin in newly diagnosed immune thrombocytopenia. Does not test calcium. |

Neither trial provides direct evidence for calcium. No SANCTR or PACTR identifiers were available in the data compiled for this report.

## Literature Evidence

For the top prediction (thrombotic disease), the most relevant publications are mechanistic or review papers. None is a clinical trial of calcium.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30530092](https://pubmed.ncbi.nlm.nih.gov/30530092/) | 2019 | Review | Cell Calcium | Store-operated calcium entry in platelets and thrombo-inflammation. |
| [38880165](https://pubmed.ncbi.nlm.nih.gov/38880165/) | 2024 | Review | Life Sciences | Calcium fluxes and mitochondrial metabolism in platelet activation and thrombosis. |
| [39796525](https://pubmed.ncbi.nlm.nih.gov/39796525/) | 2024 | Review | Nutrients | Vitamin D deficiency and thrombotic disease risk. |
| [35993516](https://pubmed.ncbi.nlm.nih.gov/35993516/) | 2022 | Review | Am J Physiol Cell Physiol | Procoagulant platelets in thromboinflammation. |
| [41055696](https://pubmed.ncbi.nlm.nih.gov/41055696/) | 2026 | Preclinical | Blood | STK10 regulates platelet function in arterial thrombosis. |
| [40540747](https://pubmed.ncbi.nlm.nih.gov/40540747/) | 2025 | Preclinical | Blood | LRRC8 channels regulate platelet activation and arterial thrombosis. |

These papers describe calcium's role in platelet activation, which supports a pro-thrombotic function and not a therapeutic one.

## South Africa Market Information

Five registrations are recorded. No approved indication text is available for any of them. Essential Medicines List (EML) inclusion status could not be determined from the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTICLE 21B N/A | ITN 7009a 2520ml | TPN | Not available |
| Exclusion under Section 36 & Section 14 | ITN8011XA 1520ml adult | TPN | Not available |
| T/30.3/704 | Stabilised Human Serum-5% Protein Solution | Infusion | Not available |
| G2667 (Act 101/1965) | Gericomplex | Capsule | Not available |
| 41/10.2.1/0849 | Spiriva Respimat inhaler 60 doses | Inhaler | Not available |

Several of these are multi-component or unrelated products (parenteral nutrition, a serum protein solution, a multivitamin/mineral capsule, a tiotropium inhaler) in which calcium is a constituent or excipient. They do not represent calcium as a stand-alone therapeutic.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (evidence level L5). Neither trial tests calcium, the literature is mechanistic, and calcium's role in clotting suggests it may promote thrombosis. The other predicted indications (hemoglobinopathy, beta-thalassemia, breast carcinoma) have only indirect evidence and are better treated as research questions.

**To proceed, the following is needed:**
- Approved indication and safety information (warnings, contraindications) from the SAHPRA Professional Information for each registered product
- Mechanism of action data to clarify any therapeutic link
- Direct clinical evidence of calcium itself, ideally randomised trials, for any proposed indication
- A safety review of thrombotic risk, since calcium may be pro-thrombotic
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

