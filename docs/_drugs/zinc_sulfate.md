---
layout: default
title: Zinc Sulfate
parent: Moderate Evidence (L3-L4)
nav_order: 481
evidence_level: L3
indication_count: 4
last_modified_at: 2026-10-15
description: "Zinc Sulfate: predicted new indication Pharyngitis (evidence level L3). Approved use: Not available"
monitor_inn: "ZINC SULFATE"
predicted_indications: ["pharyngitis", "nasal cavity disease", "acute laryngopharyngitis", "congenital prothrombin deficiency"]
---

# Zinc Sulfate
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **4** 
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

## Zinc Sulfate: From an Unspecified Original Indication to Pharyngitis
{: .text-alpha }

## One-Sentence Summary

Zinc sulfate is registered in South Africa as a single-ingredient nasal/oral spray (Nazene Z 20ml), but the data compiled for this report do not record an approved indication for it.
The TxGNN model predicts it may be effective for **pharyngitis**,
with **1 clinical trial** (a postoperative sore throat study) and **2 publications** currently supporting this direction. This evidence is indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the SAHPRA registration record has no approved indication text) |
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L3 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Zinc has plausible local effects in the oropharynx, including support of mucosal repair, modulation of local inflammation, and possible antiviral activity. These are hypotheses, not confirmed mechanisms for zinc sulfate in this setting.

The available studies concern sore throat after surgery or mucositis caused by radiotherapy, not infectious pharyngitis. The link to the predicted indication is therefore partial. The very high TxGNN score (99.85%) is a computational prediction and does not by itself establish efficacy.

Other predictions in the model output are weaker:
- **Acute laryngopharyngitis** (score 99.81%): the only evidence is a study of radiation-induced oropharyngeal mucositis, which is indirect. No registered trials were identified.
- **Nasal cavity disease** (score 99.81%): the literature describes zinc sulfate mainly as a tool to induce anosmia in animals, which raises an olfactory toxicity concern rather than showing benefit.
- **Congenital prothrombin deficiency** (score 99.16%): there is no mechanistic rationale and no supporting evidence, and this looks like a model artifact.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02405832](https://clinicaltrials.gov/study/NCT02405832) | Not applicable | Completed | 87 | Randomised, double-blind, placebo-controlled study of preoperative zinc lozenges for postoperative sore throat. Directly relevant to throat symptoms, but it is not a pharyngitis trial. The lozenge form and surgical population limit generalisability. No results are summarised in the data compiled for this report. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23720981](https://pubmed.ncbi.nlm.nih.gov/23720981/) | 2013 | RCT | J Med Assoc Thai | Randomised, double-blind, placebo-controlled trial of zinc sulfate supplementation to reduce radiation-induced oral mucositis and pharyngitis in head and neck cancer patients. |
| [20123362](https://pubmed.ncbi.nlm.nih.gov/20123362/) | 2010 | Case report / clinical observation | Oral Surg Oral Med Oral Pathol Oral Radiol Endod | Review of long-lasting taste disturbance after tonsillectomy. Dietary zinc deficiency has been proposed as a possible contributor. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H1501 (OM) | Nazene Z 20ml | Spray | Not recorded in the data compiled for this report |

Essential Medicines List (EML) status could not be determined from the data compiled for this report.

## Safety Considerations

**Contraindication signals from the knowledge graph.** These come from drug-disease links in the TxGNN knowledge graph (PrimeKG), not from approved label text, and should be verified against the Professional Information (PI). The graph lists, among others:
- Cardiovascular and blood pressure: hypertension, hypotensive disorder, heart disease, cardiovascular disease
- Renal and urinary: kidney disease, nephrolithiasis, nephrocalcinosis, acute urate nephropathy
- Hepatic and gallbladder: liver disease, gallbladder disease
- Metabolic and endocrine: diabetes mellitus, hyperglycaemia, diabetic ketoacidosis, hyperthyroidism, Graves disease, thyrotoxicosis, hyperparathyroidism, hypercalcaemia
- Other: anxiety and neurotic disorders, sarcoidosis, diarrhoeal disease, angle-closure glaucoma

**Drug interactions.** The interaction query completed, with 100 interactions recorded. The 19 entries shown in the data compiled for this report are mostly minor (immunosuppressants, biologics and corticosteroids such as abatacept, adalimumab, hydrocortisone, dexamethasone and azathioprine). The moderate ones are:
- Bisphosphonates: alendronic acid, risedronic acid, ibandronate
- Tetracycline
- Baloxavir marboxil

Separate zinc from these agents as advised in the PI, since zinc is likely to reduce their absorption.

**Nasal safety concern.** Literature on intranasal zinc sulfate describes olfactory damage (anosmia) in animal models. Intranasal use in humans should be approached with caution.

The SAHPRA package insert warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Only one small, non-pharyngitis trial of a different zinc formulation (lozenges) and indirect literature support the predicted indication. The high TxGNN score is not evidence of efficacy. The SAHPRA label safety data are missing, and the knowledge graph and animal data raise unresolved safety questions, especially for intranasal use. Pharyngitis could be revisited as a research question once these gaps are closed.

**To proceed, the following is needed:**
- The SAHPRA package insert (indication, warnings, contraindications) for Nazene Z, which is currently a blocking gap
- Mechanism of action data
- Controlled trials in infectious pharyngitis using a defined zinc sulfate formulation and dose
- Review of olfactory safety for any nasal or oropharyngeal spray use
- Confirmation of the original approved indication and EML status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

