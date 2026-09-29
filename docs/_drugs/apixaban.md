---
layout: default
title: Apixaban
parent: Moderate Evidence (L3-L4)
nav_order: 41
evidence_level: L4
indication_count: 10
---

# Apixaban
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Apixaban: From Thromboembolic Disorders to Migraine Disorder

## One-Sentence Summary

Apixaban is an oral anticoagulant (a direct factor Xa inhibitor), used to prevent and treat blood clots. The TxGNN model predicts it may be effective for **Migraine Disorder**, but the supporting evidence is thin: **1 indirectly related Phase 3 trial** and **4 publications**, mostly case reports. The published cases lean against benefit, with one report of migraine with aura worsening after apixaban was started.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Thromboembolic disorders (stroke prevention in atrial fibrillation, VTE). The indication text was not captured in the SAHPRA record extract, so this is based on the drug class. |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Apixaban is known as a direct factor Xa inhibitor. Its efficacy as an anticoagulant is established, and it may be mechanistically applicable to migraine only through a speculative thromboembolic hypothesis.

That hypothesis is that some migraine with aura may be linked to microthrombi or paradoxical emboli, for example through a patent foramen ovale (PFO). Older case reports describe migraine improving on heparin or warfarin. On this view, an anticoagulant might reduce attacks.

The available apixaban data do not support this. One case report describes migraine with aura worsening after apixaban was started. Another describes a patient whose migraine with aura resolved on warfarin but returned on apixaban. The high TxGNN score (0.99) is a knowledge-graph prediction, not clinical support.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | Compares PFO closure or anticoagulants against antiplatelet therapy to prevent stroke recurrence. Migraine is not the primary endpoint, and the anticoagulant arm is not confirmed to be apixaban. It gives indirect context only. |

No SANCTR or PACTR registrations were identified.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Case report | The Neurologist | Migraine with aura worsened after starting apixaban. The report notes the literature on direct oral anticoagulants in migraine is scarce and controversial. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case report | Headache | A 55-year-old woman had 12 years of remission of migraine with aura on warfarin. Symptoms returned within 3 weeks of switching to apixaban and resolved again on resuming warfarin. |
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Retrospective study (75 patients) | Lupus | Antithrombotic therapy in refractory migraine with antiphospholipid antibodies. Whether apixaban was used is not confirmed. |
| [29611190](https://pubmed.ncbi.nlm.nih.gov/29611190/) | 2018 | Case report | Headache | Vestibular migraine resolved on warfarin and topiramate. Apixaban was not involved. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 56/8.2/0627.625 | Xarpix 2,5 | Fct | Not recorded in the extracted data |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The Evidence Pack contains no interaction records for apixaban. The 2023 case report above suggests apixaban may aggravate migraine with aura in some patients, so this would need attention in any future study.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The only apixaban-specific migraine evidence is case reports, and the two most relevant ones point the wrong way: worsening on apixaban, and no benefit on apixaban despite benefit on warfarin. The one Phase 3 trial is only indirectly related.
- The other top predictions are also weak. Most have no trials or literature, and the pulmonary hypertension match probably reflects proximity to pulmonary embolism, which is already an approved use.
- The one exception is rheumatoid arthritis, which has a plausible preclinical rationale (FXa-mediated JAK2/STAT3 signalling in an animal model, PMID 32141012). It has no human efficacy data and is best treated as a research question.

**To proceed, the following is needed:**
- Download and parse the SAHPRA package insert, which is a blocking gap for safety screening (warnings, contraindications).
- Retrieve the mechanism of action from DrugBank to allow mechanistic-link analysis.
- Confirm the approved indication text for Xarpix 2,5 and its Essential Medicines List status.
- Prospective, controlled data on apixaban in migraine before any further evaluation. This should include confirming whether apixaban was used in the antiphospholipid antibody study (PMID 33402037).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

