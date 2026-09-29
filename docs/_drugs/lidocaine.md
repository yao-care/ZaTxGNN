---
layout: default
title: Lidocaine
parent: Model Prediction Only (L5)
nav_order: 295
evidence_level: L5
indication_count: 10
---

# Lidocaine
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

# Lidocaine: From Local Anaesthesia to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Lidocaine is a local anaesthetic, marketed in South Africa in an injectable combination product and a tablet product.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **no clinical trials and no publications** currently support this prediction.
The mechanistic case is weak, so this is a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data. Lidocaine is generally known as a local anaesthetic. |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.99% (model rank 158) |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Lidocaine is a voltage-gated sodium channel blocker, which is the basis of its local anaesthetic action. In the eye, this could at most give symptomatic relief of ocular surface pain.

The prediction is **not well supported mechanistically**. Punctate epithelial keratoconjunctivitis is a disease of the corneal and conjunctival surface. Sodium channel blockade offers no known disease-modifying effect. Topical anaesthetics can also impair corneal epithelial healing, which could work against the goal of treatment.

The high TxGNN score reflects patterns in the knowledge graph, not confirmed biology or clinical data. It should be read as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| F/21.5.4/228 | Depo-Medrol With Lidocaine | Injection | Not stated in registration data |
| W/2.7/142 | Nurofen period pain (was Nurofen extra s...) | Tablet | Not stated in registration data |

- Both products are combination products. No ophthalmic (eye drop, gel or ointment) lidocaine product appears among the registrations provided, so route compatibility with an ocular indication is unconfirmed.
- The Nurofen tablet listing should be checked against the SAHPRA register, as lidocaine is not an expected tablet ingredient.
- Essential Medicines List status is not available in the Evidence Pack.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The Evidence Pack does record two general cautions:
- Topical anaesthesia may suppress protective ocular reflexes and delay corneal epithelial healing.
- A review of intravenous lidocaine in refractory headache (PMID 19250287) reported neuropsychiatric and cardiac side-effects, which shows that systemic exposure carries real toxicity.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials or publications for this indication and a mechanism that does not fit the disease. Topical anaesthesia could also be harmful to the corneal surface.

Other lower-ranked predictions were also reviewed. "Conjunctival disorder" has indirect literature, mostly on SUNCT/SUNA headache and procedural eye anaesthesia. It is not evidence for treating a conjunctival disease.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings and contraindications), which is currently missing and blocks safety screening
- Mechanism of action data from DrugBank
- A preclinical or clinical rationale showing a disease-modifying benefit in corneal or conjunctival surface disease, not just symptom relief
- Confirmation of whether an ophthalmic lidocaine formulation exists in South Africa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

