---
layout: default
title: Zinc Sulfate
parent: Model Prediction Only (L5)
nav_order: 481
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-04
monitor_inn: "ZINC SULFATE"
predicted_indications: ["pharyngitis", "nasal cavity disease", "acute laryngopharyngitis", "congenital prothrombin deficiency"]
description: "Zinc Sulfate: predicted new indication Pharyngitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Zinc Sulfate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Zinc Sulfate: Pharyngitis
{: .text-alpha }

## One-Sentence Summary

Zinc sulfate is a zinc salt used as a mineral supplement and in topical or local preparations.
The TxGNN model predicts it may be relevant for **pharyngitis**, but the supporting evidence is weak: **1 registered clinical trial** (in a related condition, postoperative sore throat) and **2 publications**, and the only randomised trial in pharyngitis itself found no benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general knowledge, zinc has plausible local effects in the oropharynx, including support of mucosal repair, modulation of local inflammation and possible antiviral activity.

The available studies concern sore throat or mucosal injury after surgery or radiotherapy rather than infectious pharyngitis, so the link to the predicted indication is only partial. The very high TxGNN score (0.9985) is a computational output and does not by itself establish efficacy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02405832](https://clinicaltrials.gov/study/NCT02405832) | Not applicable | Completed | 87 | Randomised, double-blind, placebo-controlled study of zinc lozenges for postoperative sore throat after intubation. This is a related condition, not pharyngitis, and it used lozenges rather than zinc sulfate. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23720981](https://pubmed.ncbi.nlm.nih.gov/23720981/) | 2013 | RCT | J Med Assoc Thai | Randomised, placebo-controlled trial of zinc sulfate for radiation-induced oral mucositis and pharyngitis in head and neck cancer patients. No benefit of zinc sulfate was found for radiation-induced pharyngitis. |
| [20123362](https://pubmed.ncbi.nlm.nih.gov/20123362/) | 2010 | Case report / clinical observation | Oral Surg Oral Med Oral Pathol Oral Radiol Endod | Long-lasting taste disturbance after tonsillectomy; discusses a possible role of zinc deficiency. Indirect evidence only. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H1501 (OM) | Nazene Z 20ml | Spray | Not recorded in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: The interaction data compiled for this report list mostly minor interactions (for example with corticosteroids such as hydrocortisone, dexamethasone and betamethasone, and with biologic immunosuppressants). Moderate interactions were recorded with alendronic acid, risedronic acid, ibandronate, tetracycline and baloxavir marboxil. Separating the timing of doses of zinc and these agents should be considered.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only randomised trial in pharyngitis itself found no benefit of zinc sulfate, and the lozenge trial addresses a related condition (postoperative sore throat), so all direct evidence is negative or absent. The high TxGNN score alone does not justify progression.

**To proceed, the following is needed:**
- Well-designed randomised trials of zinc sulfate in infectious pharyngitis
- Mechanism of action data and the approved indication and safety information from the SAHPRA Professional Information for the registered product

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

