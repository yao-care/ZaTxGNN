---
layout: default
title: Acamprosate
parent: Model Prediction Only (L5)
nav_order: 12
evidence_level: L5
indication_count: 10
---

# Acamprosate
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

# Acamprosate: From Alcohol Dependence to DECR Deficiency Encephalopathy

## One-Sentence Summary

Acamprosate is an oral medicine used to help maintain abstinence in alcohol dependence. The SAHPRA record supplied does not state an approved indication, so this use comes from the literature in the Evidence Pack. The TxGNN model ranks **progressive encephalopathy with leukodystrophy due to DECR deficiency** as its top prediction, but there are **0 clinical trials** and **0 publications** for it, and no plausible mechanistic link. This is a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA record. Literature in the pack describes relapse prevention in alcohol dependence after detoxification. |
| Predicted New Indication | Progressive encephalopathy with leukodystrophy due to DECR deficiency |
| TxGNN Prediction Score | 98.53% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Acamprosate is generally described as modulating glutamatergic (NMDA/mGluR5) and GABAergic signalling. Its efficacy in alcohol dependence is documented, but this report relies on general pharmacology, not on a recorded MOA.

For this prediction, **no plausible mechanistic link was identified**. DECR deficiency is a mitochondrial fatty-acid oxidation disorder. Acamprosate's proposed neurotransmitter modulation does not address that metabolic defect. The high score reflects a knowledge-graph association only and should not be read as clinical support.

The pack does contain stronger signals for other predictions (see "Other Predicted Indications" below). None of them changes the assessment of this top-ranked one.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication.

---

## Literature Evidence

Currently no related literature available for this indication.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 32/9/0097 | Besobrial | Tablet (oral) | Not provided in the record |

Essential Medicines List (EML) status was not provided in the data.

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned no results (0 interactions recorded). This is not the same as evidence of no interactions.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Other Predicted Indications in the Evidence Pack

Only the top-ranked prediction is assessed in detail above. The others, in the pack's rank order:

| Rank | Predicted Indication | Score | Evidence Level | Pack Recommendation | Comment |
|---|---|---|---|---|---|
| 2 | Trichotillomania | 98.07% | L5 | Hold | Speculative glutamatergic rationale; no trials or literature |
| 3 | Wernicke-Korsakoff syndrome | 98.07% | L4 | Hold | Only a general alcohol-dependence review; thiamine remains standard of care |
| 4 | Alcohol amnestic disorder | 95.65% | L5 | Hold | Adjacent to alcohol dependence; no evidence provided |
| 5 | Glaucoma | 94.29% | L5 | Hold | NMDA excitotoxicity hypothesis only |
| 6 | Tourette syndrome | 92.57% | L5 | Hold | Only trial (NCT02217007) was withdrawn with 0 participants |
| 7 | ADHD | 91.85% | L3 | Research Question | Small fragile X pilot ([NCT01300923](https://clinicaltrials.gov/study/NCT01300923), Phase 2, n=14, completed); a hypothesis for a fragile X-associated phenotype, not idiopathic ADHD |
| 8 | Absence epilepsy | 91.29% | L5 | Hold | Mechanism mismatch (T-type calcium channels) |
| 9 | Alcohol withdrawal | 90.61% | L1 | Proceed with Guardrails | Not a novel repurposing signal (see below) |
| 10 | Faciodigitogenital syndrome | 90.42% | L5 | Hold | No plausible mechanistic link |

**Rank 9 (alcohol withdrawal)** has the strongest evidence, including a completed Phase 3 trial ([NCT03634917](https://clinicaltrials.gov/study/NCT03634917), n=82) and an RCT ([PMID 11524307](https://pubmed.ncbi.nlm.nih.gov/11524307/)). It sits in the same clinical area as acamprosate's existing alcohol dependence use. Acamprosate's established role is relapse prevention after detoxification, and the evidence for symptom control during acute withdrawal is weaker. It should not be treated as new-indication evidence.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (DECR deficiency) rests on a model score alone. There are no trials or publications, and the mechanism does not fit. Two blocking or high-severity data gaps also remain: SAHPRA package insert safety information and the mechanism of action.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications, approved indication) for Reg. No. 32/9/0097
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking acamprosate to DECR deficiency, or a decision to review a different candidate (e.g. ADHD in fragile X syndrome, the only "Research Question" item) instead
- EML status and route-compatibility checks, both still pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

