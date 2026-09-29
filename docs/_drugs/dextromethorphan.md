---
layout: default
title: Dextromethorphan
parent: Model Prediction Only (L5)
nav_order: 170
evidence_level: L5
indication_count: 6
---

# Dextromethorphan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Dextromethorphan: From Cough and Cold Symptom Relief to Nasal Cavity Disease

## One-Sentence Summary

Dextromethorphan is a cough suppressant that appears in several South African cold and flu products.
The TxGNN model predicts it may be useful for **nasal cavity disease**, but this is a model prediction only.
There are **no clinical trials for this condition** and **no supporting publications** in the evidence provided.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cough (antitussive), inferred from the cough and flu product names. The registered indication text was not supplied. |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, dextromethorphan is a central antitussive that acts as an NMDA receptor antagonist and sigma-1 agonist. It is already marketed in combination cold and flu products.

The link to nasal cavity disease is plausible only for symptom relief, such as cough or postnasal drip. It is not established by the data here, and dextromethorphan would not treat the underlying nasal condition. A high TxGNN score reflects proximity in the knowledge graph, not proof of benefit.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06958692](https://clinicaltrials.gov/study/NCT06958692) | Phase 3 | Recruiting | 388 | Dextromethorphan plus bupropion sustained-release tablets versus placebo in adults with major depressive disorder. No results yet. |

This trial is in major depressive disorder, not nasal cavity disease, so it does not support the predicted indication. It is why the pack assigned L3, but by the evidence-level rules the correct level is L5.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 28/5.8/0231 | Flustat | Syrup |
| Reg. No. H/10.1/140 | Vicks Medinite | Syrup |
| Reg. No. 28/20.2.2/0119 | Medaspor topical | Cream |
| Reg. No. 28/5.8/0304 | Kiddyflu | Syrup |
| Reg. No. Y/5.8/308 | Demazin Flu | Effervescent tablet |

Approved indication text was not available for any registration. A dextromethorphan-containing topical cream is unusual, so the registration should be checked against the SAHPRA record.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone. The only listed trial is in depression, and there is no literature. The other predicted indications (acute laryngopharyngitis, faucial diphtheria, trigeminal autonomic cephalalgia, cervical disc degenerative disorder, allergic urticaria) also have no supporting evidence. Faucial diphtheria and allergic urticaria have no plausible mechanism and are likely false positives.

**To proceed, the following is needed:**
- The SAHPRA package insert, for approved indications, warnings and contraindications. This is a blocking gap.
- Mechanism of action data from DrugBank.
- Trials or literature that directly study dextromethorphan in nasal cavity disease or its symptoms.
- A check that the requested route and dosage form suit the target condition.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

