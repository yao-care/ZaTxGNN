---
layout: default
title: Zinc Sulfate
parent: Model Prediction Only (L5)
nav_order: 477
evidence_level: L5
indication_count: 4
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Zinc Sulfate: From a Registered Spray Product to Pharyngitis

## One-Sentence Summary

Zinc sulfate is registered in South Africa as the spray product Nazene Z 20ml, and its SAHPRA record does not state an approved indication.
The TxGNN model predicts it may be effective for **pharyngitis**, with **4 registered clinical trials** and **3 publications** retrieved for this indication.
Most of that evidence is indirect: the trials mainly concern COVID-19 and postoperative sore throat, not infectious pharyngitis.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L2 (weak; see note below) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

*Note on evidence level:* L2 rests on randomised studies of zinc for sore throat and pharyngitis in non-infectious settings (postoperative and radiation-induced). None is a phase-labelled trial in infectious pharyngitis, so the true strength is closer to the lower end of this level.

---

## Why is This Prediction Reasonable?

Zinc has plausible local effects in the oropharynx: antiviral activity, mucosal protection and anti-inflammatory action. This fits the results of the lozenge and gargle studies for sore throat.

The direct human evidence concerns **postoperative sore throat** and **radiation-induced pharyngitis**, not infectious pharyngitis. The four registered trials mostly address COVID-19, so they do not support this indication.

Currently, detailed mechanism of action data and the original approved indication are not available. Zinc sulfate is a mineral salt with a marketed spray product in South Africa. Its local mucosal effects may be applicable to throat inflammation, but this could not be cross-checked against the product label.

Other predictions for this drug are weaker:
- **Acute laryngopharyngitis** (score 99.81%): the only evidence is indirect, a clinical study in radiotherapy-induced oropharyngeal mucositis.
- **Nasal cavity disease** (score 99.81%): no clinical evidence, and a safety concern (see Safety Considerations).
- **Congenital prothrombin deficiency** (score 99.16%): no plausible mechanism and no studies. This is a model artifact.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02405832](https://clinicaltrials.gov/study/NCT02405832) | Not applicable | Completed | 87 | Randomised, double-blind, placebo-controlled study of preoperative zinc lozenges for postoperative sore throat. Most relevant to the sore-throat symptom, but the setting is postoperative, not infectious. |
| [NCT04446104](https://clinicaltrials.gov/study/NCT04446104) | Phase 3 | Completed | 4257 | DORM trial of COVID-19 prophylaxis in migrant workers. Zinc is one component of a multi-arm design; no direct evidence for pharyngitis. |
| [NCT04370782](https://clinicaltrials.gov/study/NCT04370782) | Phase 4 | Completed | 18 | Hydroxychloroquine and zinc with azithromycin or doxycycline for outpatient COVID-19. Different disease and very small sample. |
| [NCT04621461](https://clinicaltrials.gov/study/NCT04621461) | Phase 4 | Completed | 3 | Placebo-controlled zinc trial in outpatient COVID-19. Different disease and too small to be informative. |

No SANCTR or PACTR registrations were identified in the evidence provided.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23720981](https://pubmed.ncbi.nlm.nih.gov/23720981/) | 2013 | RCT | J Med Assoc Thai | Double-blind, placebo-controlled trial of zinc sulfate supplementation for radiation-induced oral mucositis and pharyngitis in head and neck cancer patients. |
| [38693477](https://pubmed.ncbi.nlm.nih.gov/38693477/) | 2024 | RCT (per title; classified as review in the pack) | BMC Anesthesiol | Compared preoperative zinc, magnesium and budesonide gargles for incidence and severity of postoperative sore throat after intubation. |
| [20123362](https://pubmed.ncbi.nlm.nih.gov/20123362/) | 2010 | Case report | Oral Surg Oral Med Oral Pathol Oral Radiol Endod | Post-tonsillectomy dysgeusia; zinc deficiency discussed as a possible contributor. Low relevance. |

For the related predicted indication acute laryngopharyngitis, one indirect clinical study exists: [PMID 33623304](https://pubmed.ncbi.nlm.nih.gov/33623304/) (2020, Indian J Palliat Care). It reports a benefit of zinc sulfate in oropharyngeal mucositis during chemoradiation for oropharyngeal and hypopharyngeal cancers.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. H1501 (OM) | Nazene Z 20ml | Spray | Not stated in the available record |

---

## Safety Considerations

- **Intranasal use:** Intranasal zinc sulfate is a known agent for producing peripheral anosmia (loss of smell) in animals. Both dog studies retrieved for nasal cavity disease used it for this purpose. If the registered spray is used intranasally, this signal needs review before any new use is considered.
- **Drug Interactions:** No interaction records were found for this drug.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct human evidence for sore throat comes from postoperative and radiation-related settings, not infectious pharyngitis. The registered trials mostly concern COVID-19. Warnings and contraindications from the SAHPRA package insert have not yet been reviewed, which blocks safety screening.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, route of administration) from the SAHPRA website
- Mechanism of action data, for example from DrugBank
- The approved indication of Nazene Z, to confirm the original use and route compatibility
- A trial of zinc in infectious pharyngitis, or a justification for extrapolating from postoperative and radiation-induced sore throat
- A dedicated safety review of intranasal zinc sulfate and anosmia risk

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

