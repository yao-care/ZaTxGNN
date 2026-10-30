---
layout: default
title: Latanoprost
parent: Model Prediction Only (L5)
nav_order: 288
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
monitor_inn: "Latanoprost"
predicted_indications: ["visceral calciphylaxis", "hypotrichosis simplex of the scalp", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "congenital hypotrichosis milia", "angiodysplasia of stomach", "blue toe syndrome", "lymphangiectasis"]
description: "Latanoprost: predicted new indication Visceral calciphylaxis (evidence level L5). Approved use: Not recorded in the local data"
---

# Latanoprost
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Latanoprost: Visceral calciphylaxis
{: .text-alpha }

## One-Sentence Summary

Latanoprost is a prostaglandin F2-alpha analogue originally used to treat open-angle glaucoma and ocular hypertension.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Visceral calciphylaxis |
| TxGNN Prediction Score | 0.9983 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 2 of 3) |
| Number of SAHPRA Registrations | 3 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, latanoprost is a prostaglandin F2-alpha analogue that lowers intraocular pressure (IOP) by increasing uveoscleral outflow of aqueous humour. This is the basis of its use in open-angle glaucoma.

Primary hereditary (including congenital) glaucoma is also an IOP-driven disease, so an IOP-lowering drug is biologically plausible. The very high TxGNN score probably reflects the similarity of this condition to the approved glaucoma indication. It is a model prediction, not clinical evidence.

There are important caveats. In congenital forms, trabecular meshwork dysgenesis may limit the response to drugs that target outflow. The paediatric safety profile would also need separate evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 46/15.4/0918 | Spersatan | Drops | Not available in the compiled data |
| Reg. No. 51/15.4/0618 | Aglatan | Drops | Not available in the compiled data |
| Reg. No. 47/15.4/0528 | Co-atana 2.5ml | Drops | Not available in the compiled data |

All three registrations are valid single-ingredient products in drop form. Essential Medicines List (EML) status could not be confirmed from the data compiled for this report.

## Safety Considerations

- **Conditions flagged in the knowledge graph as contraindication links** (these come from drug-disease graph edges, not from label text): uveitis, iris disease, ciliary body disease, panuveitis, macular retinal edema, cystoid macular edema, iritis, conjunctivitis, and acute contagious conjunctivitis.
- **Drug Interactions:** An interaction screen returned 100 potential interacting drugs, but none has a defined severity level. Examples include calcitriol, glimepiride, doxycycline, clotrimazole, atropine, metformin, omeprazole, prednisone, triamcinolone and simvastatin. Because severity is unclassified, these should not be read as clinically significant without further review.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible for an IOP-driven disease, but there are no trials or publications for primary hereditary glaucoma. The label safety data are also missing, and the paediatric relevance is unaddressed. The prediction is a research question at this stage.

**To proceed, the following is needed:**
- A literature and trial search specific to latanoprost in primary hereditary and congenital glaucoma, including paediatric data
- The SAHPRA Professional Information (warnings, contraindications, approved indications) for the three registered products
- Detailed mechanism of action data
- Review of the unclassified drug interactions and of the knowledge-graph contraindication signals, especially for inflammatory eye conditions
- A paediatric safety and dosing assessment, plus expert ophthalmology input on whether outflow-targeted therapy can work in trabecular dysgenesis

---

### Other Predicted Indications (for reference)

All of the following have no trials or literature in the compiled data, and all are model predictions only.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 2 | Visceral calciphylaxis | 0.9983 | L5 | Hold. No clear mechanistic link; minimal systemic exposure from eye drops |
| 3 | Hypotrichosis simplex of the scalp | 0.9981 | L5 | Research question. Prostaglandin analogues prolong the hair growth phase, but responsiveness in this genetic disorder is unestablished |
| 4 | Arterial thoracic outlet syndrome | 0.9978 | L5 | Hold. Mechanical compression condition |
| 6 | Neurogenic thoracic outlet syndrome | 0.9972 | L5 | Hold. No plausible link |
| 7 | Congenital hypotrichosis milia | 0.9971 | L5 | Research question. Indirect hair-follicle rationale only |
| 8 | Angiodysplasia of stomach | 0.9970 | L5 | Hold. Vasodilation could theoretically worsen bleeding |
| 9 | Blue toe syndrome | 0.9969 | L5 | Hold. Source treatment (atheroembolism or thrombosis) is needed |
| 10 | Lymphangiectasis | 0.9967 | L5 | Hold. Relevance to lymphatic vessels unclear |

Of these, the hair-growth disorders (ranks 3 and 7) have the most biologically plausible rationale after hereditary glaucoma, but remain unproven.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

