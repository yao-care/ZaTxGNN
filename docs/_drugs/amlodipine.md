---
layout: default
title: Amlodipine
parent: Model Prediction Only (L5)
nav_order: 31
evidence_level: L5
indication_count: 10
---

# Amlodipine
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

# Amlodipine: From Hypertension (Original Indication Not Recorded in the Evidence Pack) to Brain Stem Infarction

## One-Sentence Summary

Amlodipine is an L-type calcium channel blocker, generally used for hypertension. The Evidence Pack does not record an original indication, so this is background knowledge. The TxGNN model predicts it may be effective for **brain stem infarction**, but **0 clinical trials** and **0 publications** support this specific prediction (Evidence Level L5). Two other predicted indications have more support: **intracerebral hemorrhage** (L2) and **cerebral artery occlusion** (L4).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (all SAHPRA indication text is blank) |
| Predicted New Indication | Brain stem infarction |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Amlodipine is a calcium channel blocker, and any link to brain stem infarction would be indirect. The most plausible routes are vascular risk reduction through blood pressure lowering, or calcium channel blockade itself. No trials or literature were retrieved to test either idea.

The high TxGNN score (99.94%, rank 543) shows only that the knowledge graph places this drug near the disease. It is not evidence of clinical benefit. Because the original indication is missing from the data, this may also overlap with existing hypertension care rather than being true repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered for brain stem infarction. No SANCTR or PACTR entries were retrieved.

## Literature Evidence

Currently no related literature available for brain stem infarction.

## Other Predicted Indications With Evidence

Several lower-ranked predictions have more support than the top-ranked one.

| Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Summary |
|------|------|------|------|------|
| Intracerebral hemorrhage | 99.79% | L2 | S2 | Amlodipine is a component of the low-dose triple pill tested in TRIDENT. The evidence reflects blood pressure control, not an amlodipine-specific effect. |
| Cerebral artery occlusion | 99.89% | L4 | S1 | Animal stroke models show reduced infarct size. No completed clinical trial tests amlodipine. |
| MRI-defined brain infarct | 99.86% | L4 | S0 | One blood pressure strategy trial, not amlodipine-specific. |
| Malignant renovascular hypertension | 99.90% | L4 | S0 | Two pediatric case reports only. |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 99.91% | L5 | S0 | The retrieved papers are generic hypoxia biology. Vasodilators can inhibit hypoxic pulmonary vasoconstriction, which is a safety concern rather than support. |
| Malignant hypertensive renal disease; pulmonary hypertension with unclear multifactorial mechanism; Braddock syndrome; ABri amyloidosis | 99.84–99.91% | L5 | S0 | Prediction only, with no trials or literature. |

### Key Clinical Trials (Intracerebral Hemorrhage and Related Stroke Indications)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1671 | TRIDENT: fixed low-dose triple BP-lowering pill vs placebo for recurrent stroke after intracerebral haemorrhage. It is the strongest evidence but tests a combination that includes amlodipine. |
| [NCT07458880](https://clinicaltrials.gov/study/NCT07458880) | NA | Recruiting | 140 | Triple antihypertensive medication after intracerebral hemorrhage. No results yet. |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | NA | Terminated | 4 | TRIDENT MRI sub-study. Uninformative. |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study. No usable data. |
| [NCT00134160](https://clinicaltrials.gov/study/NCT00134160) | Phase 4 | Completed | 1000 | High-dose ARB vs ARB plus calcium channel blocker for cardiovascular events in elderly hypertensive patients. The partner drug is unverified. |
| [NCT03264352](https://clinicaltrials.gov/study/NCT03264352) | Phase 4 | Recruiting | 11414 | BP intervention in adults with type 2 diabetes and high-normal BP. Loosely related. |
| [NCT03015311](https://clinicaltrials.gov/study/NCT03015311) | NA | Unknown | 8000 | STEP: intensive vs standard systolic BP target in elderly hypertensive patients. Amlodipine use unverified. |
| [NCT02850081](https://clinicaltrials.gov/study/NCT02850081) | Phase 3 | Completed | 31 | Statin neuroprotection around carotid endarterectomy. Does not test amlodipine. |
| [NCT00805311](https://clinicaltrials.gov/study/NCT00805311) | Phase 4 | Terminated | 400 | Carotid endarterectomy vs medical treatment in asymptomatic stenosis. Not amlodipine-specific. |

### Key Literature (Cerebral Artery Occlusion)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21538457](https://pubmed.ncbi.nlm.nih.gov/21538457/) | 2011 | Preclinical (animal) | J Neurosci Res | Amlodipine and atorvastatin were protective and additive after transient MCAO in Zucker metabolic syndrome rats, via antiapoptotic and antiautophagic mechanisms. |
| [20971084](https://pubmed.ncbi.nlm.nih.gov/20971084/) | 2011 | Preclinical (animal) | Brain Res | Combined amlodipine plus atorvastatin gave synergistic benefit on neuronal damage after stroke. |
| [21276424](https://pubmed.ncbi.nlm.nih.gov/21276424/) | 2011 | Preclinical (animal) | Brain Res | Synergistic protection against ischemic stroke damage with amlodipine plus atorvastatin. |
| [17070425](https://pubmed.ncbi.nlm.nih.gov/17070425/) | 2006 | Preclinical (animal) | Am J Hypertens | Amlodipine reduced stroke size in ApoE-deficient mice. |
| [17904110](https://pubmed.ncbi.nlm.nih.gov/17904110/) | 2007 | Preclinical (animal) | Brain Res | Calcium channel blockers with antioxidative effects prevented neuronal damage after transient focal ischemia in rats. |

## South Africa Market Information

Amlodipine is marketed in South Africa with 20 SAHPRA registrations. The approved indication text is not recorded in the Evidence Pack. The 5 main registrations are listed below.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 38/7.1/0183 | Amloc | Tablet |
| Reg. No. A39/7.1/0532 | Amlodac | Tablet |
| Reg. No. A39/7.1/0533 | Amlodac | Tablet |
| Reg. No. A39/7.1/0545 | Austell-amlodipine | Tablet |
| Reg. No. 50/7.1.3/0510 | Stytem 40/10 | Tablet |

All registered forms are oral tablets.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

One point from the predictions is worth noting: vasodilators can inhibit hypoxic pulmonary vasoconstriction and may worsen gas exchange in lung disease. This is a caution for the pulmonary hypertension predictions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Brain stem infarction is a model prediction only (L5), with no trials or literature. Amlodipine's most credible neurological signal is in intracerebral hemorrhage (L2, via the TRIDENT triple pill) and cerebral artery occlusion (L4, animal data). Both are confounded by combination therapy or lack human data.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- The original indication, so overlap with existing hypertension use can be assessed
- For intracerebral hemorrhage, a review of TRIDENT results to see whether an amlodipine-specific effect can be separated from the combination
- Reassessment of the top-ranked indication only if trials or literature specific to brain stem infarction emerge

*This report is for research reference only and does not constitute medical advice. Predicted repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

