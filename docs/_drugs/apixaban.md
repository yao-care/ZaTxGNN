---
layout: default
title: Apixaban
parent: 僅模型預測 (L5)
nav_order: 41
evidence_level: L5
indication_count: 10
---

# Apixaban
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Apixaban: From Atrial Fibrillation / Venous Thromboembolism to Migraine Disorder

## One-Sentence Summary

Apixaban (Eliquis®) is a direct oral Factor Xa inhibitor, globally approved for stroke prevention in non-valvular atrial fibrillation and for the treatment and prevention of venous thromboembolism — though it is not currently registered with SAHPRA in South Africa.
The TxGNN model predicts it may have activity in **Migraine Disorder** (prediction score 99.02%), with **1 indirectly relevant clinical trial** and **4 publications** currently identified.
Critically, the most directly relevant case reports suggest that apixaban may be **inferior to warfarin** in this setting, raising important questions about class-level versus drug-specific anticoagulant effects on migraine.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Stroke prevention in non-valvular atrial fibrillation; treatment and prevention of deep vein thrombosis and pulmonary embolism (globally approved; not registered with SAHPRA) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L4 |
| South Africa Market Status | Not Registered |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Apixaban is a direct, selective inhibitor of activated coagulation Factor Xa (FXa). By blocking FXa, it prevents the conversion of prothrombin to thrombin, thereby interrupting the final common pathway of the coagulation cascade. Detailed mechanism of action data was not available in this evidence pack; the pharmacological context above draws on published pharmacology. Detailed MOA confirmation should be sought from the DrugBank database.

The mechanistic bridge between anticoagulation and migraine rests on two principal biological hypotheses. The first is **PFO-associated embolic migraine**: patent foramen ovale (PFO) is found in approximately 25–45% of patients with migraine with aura compared to ~25% in the general population. Micro-emboli passing through an incompletely closed PFO may cross into the systemic circulation and trigger cortical spreading depression (CSD) — the neurophysiological basis of migraine aura. Anticoagulation could theoretically reduce this embolic burden and suppress PFO-mediated migraine. The second hypothesis is **antiphospholipid antibody syndrome (APS)-related migraine**: elevated antiphospholipid antibodies create a pro-thrombotic state that may cause cerebral microvascular thrombosis, contributing to refractory migraine, and anticoagulant therapy may attenuate this pathological process. A retrospective study (PMID 33402037) in 75 patients with refractory migraine and antiphospholipid antibodies provides limited but biologically coherent support for this hypothesis.

A critical and clinically important caveat from the available literature is that **apixaban may not be equivalent to warfarin** in migraine suppression. Two case reports directly compare the two agents: one documents complete remission of migraine with aura on warfarin for 12 years, with recurrence within 3 weeks of switching to apixaban and re-resolution upon resuming warfarin (PMID 28960288); a second reports migraine with aura worsening after apixaban initiation (PMID 37582651). This discrepancy may reflect warfarin's broader inhibition across multiple coagulation factors (II, VII, IX, X, Protein C/S) compared to apixaban's highly selective Factor Xa inhibition, suggesting that the specific coagulation target — not merely anticoagulation as a class effect — is pharmacologically relevant to migraine modulation. This negative drug-specific signal substantially tempers enthusiasm for apixaban in this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | Randomised trial comparing PFO transcatheter closure versus oral anticoagulation versus antiplatelet therapy for prevention of stroke recurrence. Primary endpoint is stroke recurrence, not migraine. Relevant because PFO is strongly linked to migraine with aura (prevalence ~45% in this population), and the trial tests anticoagulation as a PFO-related vascular intervention. However, apixaban was not the specified anticoagulant, and migraine was not a reported outcome. Indirect (Grade B) relevance only. |

> No clinical trials directly evaluating apixaban for migraine disorder were identified in ClinicalTrials.gov, ICTRP, SANCTR, or PACTR.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Pilot Trial (Retrospective) | *Lupus* | Retrospective study of 75 patients with refractory migraine and antiphospholipid antibodies receiving antithrombotic therapy. Provides the strongest current evidence that anticoagulation may benefit a specific migraine subpopulation (APS-positive). Not specific to apixaban. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Case Report + Literature Review | *The Neurologist* | **Negative signal**: Migraine with aura worsened after starting apixaban. The accompanying literature review confirms the evidence base for DOACs in migraine is scarce and contradictory. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case Report | *Headache* | **Key comparative negative signal**: 55-year-old female with complete migraine-with-aura remission on warfarin for 12 years; symptoms returned within 3 weeks of switching to apixaban and resolved again upon warfarin resumption. The most directly informative case against apixaban specifically. |
| [29611190](https://pubmed.ncbi.nlm.nih.gov/29611190/) | 2018 | Case Report | *Headache* | Vestibular migraine resolving on warfarin and topiramate. Does not address apixaban directly, but supports a possible anticoagulant class effect (via a non-apixaban agent) in PFO/vascular-mechanism migraine subtypes. |

---

## South Africa Market Information

Apixaban is **not currently registered with SAHPRA** and holds no approved licences in South Africa. No product registration table is available.

For reference, apixaban is marketed internationally as **Eliquis®** (Bristol-Myers Squibb / Pfizer) and is approved by the US FDA, EMA, Health Canada, and other major regulatory authorities for:
- Prevention of stroke and systemic embolism in non-valvular atrial fibrillation
- Treatment of acute DVT and PE
- Prevention of recurrent DVT and PE
- VTE prophylaxis following elective hip or knee replacement surgery

Any South African repurposing trial or compassionate use application would first require SAHPRA regulatory engagement, given the absence of an existing local registration dossier.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Since apixaban is not currently registered with SAHPRA, healthcare providers should consult international prescribing information (e.g., FDA Prescribing Information or EMA Summary of Product Characteristics for Eliquis®). Report any suspected adverse drug reactions to SAHPRA via the MedSafety reporting system.

> **Class-level safety note relevant to migraine context**: As a direct oral anticoagulant, apixaban carries inherent bleeding risk. Migraine patients frequently use NSAIDs (e.g., ibuprofen, naproxen) and triptans — concurrent use with anticoagulants may increase gastrointestinal and intracranial bleeding risk, requiring careful individual risk-benefit assessment before any off-label trial.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
The evidence for apixaban specifically in migraine disorder is at Level L4 — confined to case reports and one retrospective pilot trial — and the most directly relevant case evidence points in a **negative direction for apixaban**, demonstrating that warfarin (but not apixaban) suppresses migraine with aura. While the anticoagulation-migraine biological hypothesis is coherent for PFO-related and APS-associated migraine subtypes, current data are insufficient to support apixaban as having migraine-specific efficacy, and drug-specific negative signals are present.

**To proceed, the following is needed:**

- **Subgroup clarification**: Prospective evaluation should be restricted to mechanistically defined subpopulations — specifically PFO-positive migraine with aura patients and/or those with confirmed antiphospholipid antibodies — where the biological rationale is strongest
- **Head-to-head comparison**: Controlled data comparing apixaban directly against warfarin in migraine patients are essential to establish whether selective Factor Xa inhibition is sufficient, given the current case-report signal suggesting it is not
- **Mechanism of action data**: Formal MOA documentation from DrugBank should be retrieved to support or refine the mechanistic hypothesis (currently a data gap)
- **Safety profile in migraine patients**: A formal drug-drug interaction assessment is needed given frequent co-use of NSAIDs and other analgesics in this population
- **SAHPRA registration pathway**: Apixaban has no existing SAHPRA registration; any South African clinical repurposing trial would require a parallel regulatory strategy

> *This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All patient management decisions should follow SAHPRA-approved prescribing information and current clinical guidelines.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

