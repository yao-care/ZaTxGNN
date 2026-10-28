---
layout: default
title: Apixaban
parent: Model Prediction Only (L5)
nav_order: 40
evidence_level: L5
indication_count: 1
monitor_inn: "Apixaban"
predicted_indications: ["migraine disorder"]
last_modified_at: 2026-10-29
description: "Apixaban: predicted new indication migraine disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Apixaban
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Apixaban: Factor Xa inhibitor (direct oral anticoagulant) → migraine disorder
{: .text-alpha }

## One-Sentence Summary

Apixaban is a direct oral anticoagulant that inhibits factor Xa. The TxGNN model predicts it may be relevant to **migraine disorder**, but the supporting evidence is weak: **1 clinical trial** (not studying migraine) and **3 publications** (two case reports and one small retrospective study) are currently listed, and the case reports point in conflicting directions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | migraine disorder |
| TxGNN Prediction Score | 0.9902 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. In general terms, apixaban is an oral anticoagulant that blocks factor Xa and so reduces thrombin generation and clot formation.

The link to migraine is indirect and speculative. Migraine with aura, particularly in people with a patent foramen ovale (a right-to-left shunt), has been hypothesised to involve paradoxical microemboli, so anticoagulation could theoretically matter in selected patients. However, the available apixaban-specific reports contradict one another. One describes migraine with aura worsening after starting apixaban. Another describes symptoms that returned on apixaban and resolved on warfarin. No established mechanism supports apixaban as a migraine treatment.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | Compared PFO closure, anticoagulants and antiplatelet therapy to prevent recurrent stroke in patients with PFO. Migraine was not the studied indication or primary endpoint, and apixaban is not clearly the agent tested. This is not direct evidence for migraine. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Retrospective study (75 patients) | Lupus | Antithrombotic therapy in refractory migraine with antiphospholipid antibodies. Small, specific population, and not apixaban-specific. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Case report + literature review | The Neurologist | Migraine with aura worsened after starting apixaban. The review notes that literature on direct oral anticoagulants in migraine is scarce and controversial. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case report | Headache | Migraine with aura remained in remission for 12 years on warfarin, returned within 3 weeks of switching to apixaban, and resolved again after warfarin was resumed. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 56/8.2/0627.625 | Xarpix 2,5 | Fct | Not recorded in the local data |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in total. Examples of those rated **Major** include acetylsalicylic acid, cobicistat, deferasirox, ibritumomab tiuxetan and tositumomab. Examples rated **Moderate** include aprepitant, clarithromycin, clotrimazole, dexamethasone, miconazole and rolapitant.

Warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available in the data compiled for this report. Please refer to the PI for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No study cited here directly examines apixaban for migraine. The only trial is in stroke prevention with PFO, and the two apixaban case reports conflict, with one suggesting worsening. The high TxGNN score is not backed by clinical evidence.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological rationale for migraine
- Controlled studies of apixaban in migraine, ideally in defined subgroups such as migraine with aura and PFO
- Review of the SAHPRA Professional Information for warnings and contraindications
- Bleeding risk assessment, given the interactions identified and the chronic nature of migraine treatment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

