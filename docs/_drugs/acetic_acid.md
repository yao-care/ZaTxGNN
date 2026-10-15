---
layout: default
title: Acetic Acid
parent: Model Prediction Only (L5)
nav_order: 15
evidence_level: L5
indication_count: 10
---

# Acetic Acid
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

# Acetic Acid: From Otitis Externa to Post-Bacterial Disorder

## One-Sentence Summary

Acetic acid was originally used as a topical acidifying and antibacterial agent for ear conditions (otitis externa and external ear disease). The TxGNN model predicts it may be effective for **post-bacterial disorder**, but there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Otitis externa; external ear disease (from the TxGNN knowledge graph, as no registration in South Africa states an approved indication) |
| Predicted New Indication | Post-bacterial disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, acetic acid is a weak organic acid used topically as an antiseptic and pH-modifying agent. Its efficacy in superficial ear infection is the basis of its original use, and it is generally understood to act by lowering local pH and inhibiting bacterial and fungal growth.

"Post-bacterial disorder" is a vague category. It covers sequelae that appear after a bacterial infection, which are often immune-mediated or structural rather than active infection. A topical antibacterial agent has no clear mechanism for treating such sequelae, so no specific mechanistic link can be supported. The high model score likely reflects network proximity in the knowledge graph rather than biological plausibility.

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
| A39/34/0163 | Sabax Low Magnesium Acid Diasol (1000Ml) | Solution | Not stated in the data compiled |
| 29/34/0328 | Haemocarb acid concentrate 5l afm7204 | Infusion | Not stated in the data compiled |
| A39/34/0168 | Sabax Standard Acute Acid Diasol | Solution | Not stated in the data compiled |
| SECTION 21 | Haemodialysis Concentrate | Solution | Not stated in the data compiled |

All four registrations are single-ingredient products with valid status. By product name they are haemodialysis acid concentrates, not topical ear preparations. The local market therefore does not directly reflect the original otic use or any of the predicted indications. The "SECTION 21" entry is an authorisation for use of an unregistered product rather than a standard registration number.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease contraindication links in the TxGNN knowledge graph, not from product label text): inherited porphyria, porphyrin metabolism disease, porphyria, herpes simplex infection, and geniculate herpes zoster. These should be verified against the approved Professional Information (PI).
- **Drug Interactions**: No interactions were found in the data queried.

Warnings and contraindications from the SAHPRA-approved PI were not available for this report. Please refer to the approved PI for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output only (L5), with no trials, no relevant literature, and no plausible mechanistic link for this vague indication. The local registrations are dialysis concentrates, which are unrelated to the proposed use.

**To proceed, the following is needed:**
- Detailed mechanism of action data
- SAHPRA package insert warnings and contraindications
- A more clearly defined target condition and a plausible route of administration, since route compatibility has not been assessed

**Note on other predictions:** Among the other predicted indications, **tinea corporis** (score 99.25%) has the most supporting material. It consists of historical reports (1946-1958) of dilute acetic acid for tinea capitis and foot epidermophytosis, plus indirect in vitro antifungal work. It carries an L4 rating and a "Research Question" status, though it still has no registered trials and only old, uncontrolled studies. A 2023 report of burns from acid-based folk remedies also flags a safety concern for uncontrolled topical use. This signal may be worth a separate, focused evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

