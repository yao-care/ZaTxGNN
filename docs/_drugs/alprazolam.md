---
layout: default
title: Alprazolam
parent: Model Prediction Only (L5)
nav_order: 24
evidence_level: L5
indication_count: 3
---

# Alprazolam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Alprazolam: From Its Registered Indication (Not Stated in the Data) to Insomnia

## One-Sentence Summary

Alprazolam is a benzodiazepine marketed in South Africa as tablets, but the data does not record its approved indication.
The TxGNN model predicts it may be effective for **insomnia**, but **none of the 7 retrieved clinical trials tests alprazolam for insomnia** and **no supporting publications** were found.
The prediction is therefore model-only for now.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 (the pack lists L4, but no mechanistic or preclinical study was retrieved) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Alprazolam is a GABA-A positive allosteric modulator, and sedation is a plausible class effect of benzodiazepines. That gives a reasonable biological link to sleep problems.

The very high score (99.81%) most likely reflects closeness to other benzodiazepines in the knowledge graph. It does not show that alprazolam works for insomnia. Dependence, tolerance, withdrawal difficulty and safety in elderly patients also argue against advancing this indication without direct evidence.

## Clinical Trial Evidence

None of the trials below tests alprazolam for insomnia. They are related only by drug family, setting or population.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A (cohort) | Unknown | 1400 | Prospective cohort on risks and benefits of hypnotics for sleep disorders in elderly patients in Taiwan. Relevant to safety context; alprazolam-specific data unconfirmed |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | N/A | Completed | 170 | Self-management intervention to stop benzodiazepines in Veterans. About cessation, not efficacy |
| [NCT03327506](https://clinicaltrials.gov/study/NCT03327506) | Phase 4 | Unknown | 128 | Hypnosis vs alprazolam premedication for perioperative anxiety. Anxiety setting, not insomnia |
| [NCT00266409](https://clinicaltrials.gov/study/NCT00266409) | Phase 4 | Completed | 418 | Niravam (alprazolam) plus SSRI/SNRI vs SSRI/SNRI alone in generalised anxiety or panic disorder. Not insomnia |
| [NCT01584440](https://clinicaltrials.gov/study/NCT01584440) | Phase 2 | Completed | 220 | AVP-923 vs placebo for agitation in Alzheimer's disease. Role of alprazolam unverified |
| [NCT01146600](https://clinicaltrials.gov/study/NCT01146600) | Phase 2 | Completed | 26 | Clarithromycin for hypersomnia. Different drug and condition |
| [NCT01893632](https://clinicaltrials.gov/study/NCT01893632) | Phase 2 | Terminated | 2 | Gabapentin for benzodiazepine dependence. Ended early; no efficacy information for alprazolam |

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Five SAHPRA registrations were found, all oral tablets. The approved indication text and manufacturer are not recorded for any of them.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 28/2.6/0001 | Biozane | Tablet |
| Reg. No. 29/2.6/0182 | Azor | Tablet |
| Reg. No. 30/2.6/0264 | Zopax | Tablet |
| Reg. No. 31/2.6/0241 | Coprax | Tablet |
| Reg. No. 32/2.6/0372 | Mylan alprazolam | Tablet |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Concerns raised in the evidence review for this drug class and use:
- **Dependence, tolerance and withdrawal**: A 1988 controlled discontinuation report documents difficulty stopping alprazolam.
- **Elderly patients**: Safety concerns argue against use without direct evidence.

No drug interaction records were found in the database query.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction rests on a strong model score and a plausible class effect. There is no trial or publication testing alprazolam for insomnia, and the dependence and withdrawal risks are well documented.

**To proceed, the following is needed:**
- Alprazolam-specific insomnia evidence (randomised trials or systematic reviews)
- SAHPRA Professional Information warnings and contraindications (blocking gap for safety screening)
- Approved indication text for the five registrations, and mechanism of action data from DrugBank
- A dependence, withdrawal and elderly-safety plan if the indication is pursued

**Side note on agoraphobia (rank 3 prediction):** It has substantial evidence (multiple placebo-controlled RCTs and a 2023 network meta-analysis for panic disorder). It is likely already a labelled use, so it may not be true repurposing. Check it against the SAHPRA label before treating it as a repurposing signal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

