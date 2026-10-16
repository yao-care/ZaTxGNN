---
layout: default
title: Dorzolamide
parent: Model Prediction Only (L5)
nav_order: 200
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dorzolamide: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Open-angle glaucoma"
monitor_inn: "Dorzolamide"
predicted_indications: ["primary hereditary glaucoma", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "alopecia", "diffuse alopecia areata", "glaucoma 1, open angle", "open angle glaucoma", "congestive heart failure", "acute pulmonary heart disease", "respiratory failure"]
---

# Dorzolamide
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

# Dorzolamide: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Dorzolamide is a topical carbonic anhydrase inhibitor, originally used to lower eye pressure in open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, but **no clinical trials and no publications** specifically support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma; ocular hypertension (taken from the knowledge-graph indication data, because the SAHPRA licence records compiled here contain no indication text) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dorzolamide inhibits carbonic anhydrase II in the ciliary processes of the eye. This reduces the production of aqueous humour and lowers intraocular pressure (IOP). Lowering IOP is also the main treatment goal in other forms of glaucoma, so a model that links dorzolamide to a related glaucoma is mechanistically plausible. Detailed mechanism-of-action data from DrugBank were not available for this report.

There are important caveats. Hereditary (congenital or juvenile) glaucoma usually involves developmental abnormalities of the drainage angle. A drug that only reduces fluid production may therefore give uncertain benefit. Use in children would also need its own safety assessment.

A Phase 2 trial in paediatric glaucoma (NCT01527682, below) was found in the data compiled for a related glaucoma entry. It tested dorzolamide alongside latanoprost in children whose glaucoma had not responded to surgery. This is only indirect context and does not confirm efficacy in hereditary glaucoma.

For context, the model's other top predictions are weaker: the hair-loss conditions have no plausible mechanism and are likely network artefacts, and the cardiopulmonary conditions are unlikely with a topical drug. The model's two entries closest to the approved use (glaucoma 1, open angle; open angle glaucoma) are the existing indication, not new repurposing.

---

## Clinical Trial Evidence

Currently no clinical trials are registered for primary hereditary glaucoma in the data compiled for this report.

One indirectly relevant study was found under a related glaucoma entry:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Latanoprost and dorzolamide in primary paediatric glaucoma refractory to surgery; assessed IOP-lowering effect and safety (results not summarised in the data) |

No SANCTR or PACTR identifiers were found.

---

## Literature Evidence

Currently no related literature available for primary hereditary glaucoma.

For the established indication, the compiled data include a network meta-analysis ([PMID 26526633](https://pubmed.ncbi.nlm.nih.gov/26526633/), Ophthalmology, 2016) and a Cochrane review ([PMID 17943780](https://pubmed.ncbi.nlm.nih.gov/17943780/), 2007). These support dorzolamide in primary open-angle glaucoma and ocular hypertension, but not in hereditary glaucoma.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| 54/15.4/0257 | Dorzopt Forte | Drops |
| 51/15.4/0162 | Ocudor Co | Drops |

Both registrations are valid. Approved indication text and Essential Medicines List status were not available in the data compiled for this report.

---

## Safety Considerations

SAHPRA package-insert warnings and contraindications were not available for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Additional information from the knowledge graph (these are drug-disease links, not label text, and need confirmation against the PI):

- **Possible contraindication signals:** diabetes mellitus and diabetic ketoacidosis, myasthenia gravis and other neuromuscular junction disease, hyperthyroidism (Graves disease, thyrotoxicosis), hypoglycaemia, atrioventricular block, pulmonary emphysema and bronchial disease, and anaphylaxis. Several of these resemble known cautions for beta-blocker co-formulations. Dorzolamide is often combined with timolol, so they may not all apply to dorzolamide alone.
- **Drug interactions:** No drug-drug interactions were identified. The interaction data list only dorzolamide's pharmacological targets (carbonic anhydrase isoforms CA1, CA7, CA12 and CA14).
- **Paediatric use:** Hereditary glaucoma commonly presents in children, so paediatric safety would need a separate assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by a very high model score (99.99%) but by no trial or publication specific to primary hereditary glaucoma (evidence level L5). The mechanism is plausible, but the benefit is uncertain because hereditary forms often involve structural angle abnormalities. The strong evidence in the compiled data relates to open-angle glaucoma, which is the existing indication and not a new one.

**To proceed, the following is needed:**
- Review of the Phase 2 paediatric glaucoma study (NCT01527682) and any other paediatric or hereditary glaucoma data, to see whether dorzolamide lowers IOP in this group
- Specialist ophthalmology input on whether IOP lowering with a carbonic anhydrase inhibitor is useful in hereditary glaucoma subtypes
- Paediatric safety assessment, including systemic absorption and acid-base effects
- The SAHPRA package inserts for Dorzopt Forte and Ocudor Co, to confirm approved indications, warnings and contraindications
- Detailed mechanism-of-action data from DrugBank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

