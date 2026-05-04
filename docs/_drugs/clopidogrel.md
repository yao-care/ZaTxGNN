---
layout: default
title: Clopidogrel
parent: 僅模型預測 (L5)
nav_order: 135
evidence_level: L5
indication_count: 10
---

# Clopidogrel
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

# Clopidogrel: From Thrombotic Event Prevention to Migraine with Brainstem Aura

---

## One-Sentence Summary

Clopidogrel is a widely used P2Y12 receptor antagonist (antiplatelet agent) originally approved for prevention of thrombotic cardiovascular and cerebrovascular events — including acute coronary syndrome, ischaemic stroke, and peripheral arterial disease.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** (formerly known as basilar-type migraine), a subtype closely linked to cardiac right-to-left shunts such as patent foramen ovale (PFO).
With **no registered clinical trials** specific to this brainstem aura subtype but **16 relevant publications** and a biologically coherent mechanistic rationale, the current evidence base sits at **Level L3**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of thrombotic events: acute coronary syndrome, ischaemic stroke/TIA, peripheral arterial disease |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| South Africa Market Status | Not marketed (no SAHPRA registrations identified) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Clopidogrel irreversibly blocks the P2Y12 receptor on platelets, inhibiting ADP-mediated platelet aggregation and the formation of platelet microemboli. This mechanism is directly relevant to a well-established hypothesis for migraine with aura: in patients with patent foramen ovale (PFO) or other right-to-left cardiac shunts, venous platelet aggregates and vasoactive substances such as serotonin bypass the pulmonary "filter" and enter the cerebral circulation intact. These emboli are thought to trigger cortical spreading depression (CSD) — the neurophysiological substrate of migraine aura. In brainstem aura specifically, the CSD originates in the brainstem territory, a region supplied by the posterior circulation that is particularly sensitive to vasoactive embolic events.

A second, central mechanism adds further plausibility. P2Y12 receptors are expressed not only on platelets but also on microglia in the central nervous system, including the trigeminal nucleus caudalis and brainstem. Basic science data shows that microglial P2Y12 activation drives neuroinflammation via the RhoA/ROCK pathway, contributing to chronic migraine sensitisation (PMID 31722730). Clopidogrel's blockade of P2Y12 could therefore act on both the peripheral platelet arm and the central neuroinflammatory arm of migraine pathogenesis — a dual mechanism that is mechanistically coherent, though not yet validated in a dedicated trial for this specific subtype.

It is important to note that existing clinical evidence derives from the broader **migraine with aura** and **migraine disorder** populations, not from brainstem aura specifically. The TxGNN model extrapolates from this body of evidence, which is biologically plausible but represents an unvalidated subtype extension. The most directly applicable clinical trial — the CANOA Phase 4 RCT — demonstrated that clopidogrel plus aspirin significantly reduced new-onset migraine after transcatheter atrial septal defect (ASD) closure versus aspirin alone (PMID 26551304, PMID 32965476), providing proof-of-concept for the overall hypothesis.

---

## Clinical Trial Evidence

No clinical trials specifically enrolling patients with **migraine with brainstem aura** have been registered. The table below lists the most relevant trials from the closely related **migraine disorder** evidence base (predicted_indications rank 2), which provide the strongest indirect support for this mechanistic pathway.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) | Phase 4 | Completed | 220 | **CANOA trial**: Clopidogrel + aspirin vs aspirin alone for prevention of new-onset migraine after transcatheter ASD closure. Primary endpoint met; results published in JAMA (2015) and updated in JAMA Cardiology (2021). Highest-quality direct evidence for clopidogrel in migraine prevention. |
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) | Phase 4 | Unknown | 1,000 | **COMPETE trial**: Head-to-head comparison of anticoagulation vs antiplatelet therapy (including clopidogrel) vs standard migraine preventive medications in patients with PFO-associated migraine. Study design published (PMID 38109984). High relevance if results become available. |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Phase 4 | Unknown | 50 | Prospective evaluation of clopidogrel efficacy specifically in migraineurs with right-to-left shunt — the most directly relevant mechanistic design. Small sample limits interpretability. |
| [NCT04946734](https://clinicaltrials.gov/study/NCT04946734) | Phase 3 | Active, not recruiting | 440 | **SPRING trial**: PFO closure vs medication (including antiplatelet agents) with migraine relief as primary endpoint. Ongoing; results will be pivotal for the field. |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | PFO closure vs anticoagulation vs antiplatelet therapy for stroke recurrence prevention; migraine relief was a secondary endpoint. Provides safety and indirect efficacy data for antiplatelet use in PFO populations. |
| [NCT02777359](https://clinicaltrials.gov/study/NCT02777359) | Phase 2 | Unknown | 100 | PFO closure for migraine in high-risk PFO; clopidogrel used as standard post-procedural antiplatelet therapy. Indirect evidence only. |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | N/A | Terminated | 7 | GORE® CARDIOFORM device study for migraine relief; terminated early due to very low enrolment. No usable data. |

*No trials are registered with SANCTR (South African National Clinical Trials Register) or PACTR (Pan African Clinical Trials Registry) for this indication.*

---

## Literature Evidence

The following publications were identified for the **migraine with brainstem aura** indication, prioritised by study type and direct relevance.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | Pilot RCT | *Cephalalgia* | First randomised pilot trial of clopidogrel as prophylactic treatment for migraine; provides early controlled evidence for the repurposing hypothesis |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic Review | *Headache* | Most recent systematic review of antithrombotic drugs (including clopidogrel) as migraine preventive medication; highest-level evidence synthesis available |
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT | *European Heart Journal* | **PRIMA trial**: Percutaneous PFO closure in migraine with aura refractory to medical treatment; clopidogrel administered post-procedure; directly relevant to the aura-PFO mechanistic axis |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Cohort | *J Investigative Medicine* | Clopidogrel 75 mg/day added as complementary prophylaxis for drug-refractory migraine with PFO; PFO found in 56.8% of enrolled migraineurs; positive signal at 3 and 6 months |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Prospective Observational | *Heart* | Earliest observational report: clopidogrel reduces migraine with aura after transcatheter closure of PFO and ASDs; led to subsequent clinical interest |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Open-label Pilot | *Neurology* | **TRACTOR study**: Explores ticagrelor (non-thienopyridine P2Y12 inhibitor) for refractory migraine/PFO following prior observations of clopidogrel and prasugrel benefit; supports the P2Y12 class effect hypothesis |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Retrospective Cohort | *Neurology* | Retrospective review of thienopyridine therapy (clopidogrel and prasugrel) in migraineurs with PFO; positive migraine headache reduction signal across the drug class |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Retrospective Cohort | *Cephalalgia* | Retrospective review of clopidogrel as primary therapy in migraineurs with right-to-left shunt; supports mechanistic link between platelet activation, paradoxical embolisation, and migraine |
| [15966922](https://pubmed.ncbi.nlm.nih.gov/15966922/) | 2005 | Case Series | *J Interventional Cardiology* | Intense migraine developed after percutaneous ASD closure in 5/13 consecutive patients; dramatic relief achieved with 300 mg clopidogrel load — an early clinical anecdote that generated the research hypothesis |
| [22992406](https://pubmed.ncbi.nlm.nih.gov/22992406/) | 2012 | Case Series | *Cephalalgia* | De novo migraine after ASD closure; antiplatelet drugs including clopidogrel associated with migraine amelioration; also reports exclusive ticlopidine (clopidogrel analogue) efficacy in one case |

---

## South Africa Market Information

No SAHPRA registrations for Clopidogrel were identified in the current dataset.

> **Important note for prescribers:** Clopidogrel (Plavix® and multiple generics) is a widely used cardiovascular drug globally and is listed on the WHO Essential Medicines List. The absence of registrations in this dataset may reflect a data gap rather than genuine non-availability. Healthcare professionals should verify current SAHPRA registration and availability directly via the SAHPRA Medicines Control database (www.sahpra.org.za) and consult the approved Professional Information (PI) document before prescribing. The Standard Treatment Guidelines and Essential Medicines List (STG/EML) of South Africa should also be consulted for approved cardiovascular indications.

---

## Safety Considerations

Detailed safety data for this report could not be retrieved from the available dataset. Please refer to the SAHPRA-approved Professional Information (PI) for comprehensive safety information. Report suspected adverse drug reactions to SAHPRA via the MedSafety online reporting system (www.medsafety.org.za).

**Key points for prescribers based on established pharmacology:**
- **Bleeding risk:** Clopidogrel significantly increases the risk of major bleeding, including intracranial and gastrointestinal haemorrhage. Risk is substantially elevated when co-administered with aspirin, NSAIDs, anticoagulants, or SSRIs.
- **CYP2C19 pharmacogenomics:** Clopidogrel is a prodrug requiring hepatic bioactivation by CYP2C19. Patients who are CYP2C19 poor metabolisers (common in some South African population groups) may show markedly reduced antiplatelet efficacy. Pharmacogenomic testing should be considered in high-stakes settings.
- **Drug interactions:** Proton pump inhibitors (especially omeprazole), CYP2C19 inhibitors (fluconazole, fluoxetine, fluvoxamine), and some anticonvulsants can reduce clopidogrel efficacy. Refer to the current PI for a full interaction list.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
The mechanistic case for clopidogrel in migraine with brainstem aura is biologically coherent — PFO-mediated right-to-left shunting and P2Y12-dependent neuroinflammation provide two plausible pathways — and indirect clinical evidence from the broader migraine-with-aura and migraine disorder literature is accumulating. However, **no clinical trial has specifically enrolled patients with confirmed brainstem aura**, and this subtype may behave differently from other migraine-with-aura forms. The evidence is currently insufficient to support routine use, off-label prescribing, or a formal clinical programme without additional foundational data.

**To proceed, the following is needed:**

- **Targeted clinical sub-group data:** Request sub-group analysis of ongoing trials (especially SPRING, NCT04946734, and COMPETE, NCT05546320) specifically for patients with brainstem aura features
- **PFO prevalence mapping:** Prospective echocardiographic or TCD bubble study documentation of PFO prevalence in the South African brainstem aura patient population
- **MOA data gap closure:** Obtain complete DrugBank pharmacology data for clopidogrel (DrugBank API query — DG002) to formalise the mechanism-of-action section
- **SAHPRA registration verification:** Confirm current approved indications, available formulations, and market status of clopidogrel in South Africa through SAHPRA directly
- **PI / safety data gap closure:** Download and parse the SAHPRA-approved PI document (DG001, currently blocking entry to S1 safety screening) for formal contraindication and warning analysis
- **Pharmacogenomic consideration:** Assess CYP2C19 poor metaboliser frequency in South African population sub-groups to determine whether standard 75 mg dosing is appropriate in the target population
- **Hypothesis generation protocol:** If moving toward a research question, design a prospective pilot study (n ≈ 30–50) enrolling PFO-confirmed patients with brainstem aura, using validated migraine burden endpoints (HIT-6, MIDAS), with clopidogrel 75 mg/day for 3–6 months

---

*This report is generated for research purposes only and does not constitute medical advice. Repurposing candidates require clinical validation before application. All pages should include the disclaimer: this information is for research reference only and does not constitute medical advice.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

