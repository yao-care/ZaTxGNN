---
layout: default
title: Latanoprostene Bunod
parent: Model Prediction Only (L5)
nav_order: 287
evidence_level: L5
indication_count: 10
---

# Latanoprostene Bunod
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

# Latanoprostene bunod: From Glaucoma / Ocular Hypertension to Visceral Calciphylaxis

## One-Sentence Summary

Latanoprostene bunod is an eye-drop medicine marketed in South Africa as Vyzulta, and it is used to lower eye pressure in glaucoma and ocular hypertension. The TxGNN model predicts it may be effective for **visceral calciphylaxis**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it remains a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glaucoma / ocular hypertension (the registration record supplied does not include approved indication text) |
| Predicted New Indication | Visceral calciphylaxis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Latanoprostene bunod lowers eye pressure through two pathways. Its latanoprost acid component activates the prostaglandin FP receptor and increases uveoscleral outflow. Its nitric oxide (NO)-donating component causes vasodilation and increases outflow through the trabecular meshwork. Formal mechanism-of-action data were not supplied for this report, so this description is based on the drug's known pharmacology.

Visceral calciphylaxis is a serious disorder of vascular calcification. Neither NO-mediated vasodilation nor FP receptor agonism has an established role in it, so any mechanistic link is speculative. The high TxGNN score (0.998) reflects patterns in the knowledge graph, not clinical or mechanistic evidence. It should not be read as support for use in this condition.

The drug is also a topical ocular product. Reaching a visceral vascular disease would need a very different route and exposure, and route compatibility has not been assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for visceral calciphylaxis.

---

## Literature Evidence

Currently no related literature available for visceral calciphylaxis.

**Context from other predictions.** Trials and literature exist only for other predicted indications:
- Two completed trials (NCT03949244, NCT03931317) measured blood-flow surrogates in people with glaucoma or ocular hypertension. They were listed under the broad "vascular disease" prediction (rank 6). They are indirect evidence and do not concern calciphylaxis.
- The predicted "primary hereditary glaucoma" (rank 2) very likely restates the drug's known ocular use rather than a true repurposing. Evidence in hereditary or early-onset forms still needs verification.
- Most other top-ranked predictions (thoracic outlet syndromes, coronary artery dissection, lymphangiectasis, hemangioendothelioma) have no supporting data and no plausible mechanism.
- For angiodysplasia of the stomach (rank 8), a vasodilator could in theory worsen bleeding from vascular malformations, which is a safety concern.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 53/15.4/0226 | Vyzulta | Drops | Not stated in the registration record supplied |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug interaction records were found in the data supplied.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature and no plausible mechanism. It is also a topical ocular product being proposed for a systemic vascular calcification disease. A high model score alone does not justify further investment.

**To proceed, the following is needed:**
- Formal mechanism-of-action data and a mechanistic case linking NO or FP receptor signalling to vascular calcification
- Preclinical or observational evidence in calcification models or patients
- Assessment of route and exposure compatibility (topical ocular vs systemic disease)
- The SAHPRA package insert warnings and contraindications, needed before any safety screening
- If ocular or microvascular repurposing is of interest, review the glaucoma-related predictions and the blood-flow trials separately

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

