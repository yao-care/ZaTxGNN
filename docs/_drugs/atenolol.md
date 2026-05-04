---
layout: default
title: Atenolol
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 9
---

# Atenolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Atenolol: From Hypertension and Angina to Posterolateral Myocardial Infarction

---

## One-Sentence Summary

Atenolol is a cardioselective β1-adrenergic receptor blocker with well-established use in hypertension, angina pectoris, and acute myocardial infarction. The TxGNN model ranks **Posterolateral Myocardial Infarction** as the top predicted new indication (score: 99.87%), though no specific clinical trials or publications currently address this anatomical MI subtype in isolation. This evidence pack covers **9 predicted indications** in total; **Chronic Pulmonary Heart Disease** (rank 9, Evidence Level L3) has the strongest supporting evidence with **1 clinical trial** and **15 publications**, warranting a "Proceed with Guardrails" decision.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in evidence pack — atenolol is broadly established for hypertension, angina pectoris, and acute myocardial infarction |
| Predicted New Indication | Posterolateral Myocardial Infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 (mechanistic extrapolation; no posterolateral-specific trials) |
| South Africa Market Status | Not marketed (0 SAHPRA registrations found — see verification note below) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

> ⚠️ **SAHPRA Verification Required**: The evidence pack reports 0 SAHPRA registrations for atenolol. This almost certainly reflects a data completeness gap, as atenolol is included on the **South African Essential Medicines List (EML)** and the **WHO Essential Medicines List** as a widely used generic medicine. Healthcare professionals must confirm the current registration status and approved indications directly via the [SAHPRA Online Enquiry System](https://www.sahpra.org.za/) before any prescribing decision.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacological information, atenolol is a selective β1-adrenergic receptor blocker — it competitively inhibits catecholamine binding at cardiac beta-1 receptors, reducing heart rate, myocardial contractility, and systolic blood pressure. This lowers myocardial oxygen demand and blunts adrenergic activation, effects that are directly beneficial in the context of acute and post-myocardial infarction management. At therapeutic doses, its β1-selectivity minimises effects on β2-receptors in the lungs and peripheral vasculature.

Posterolateral myocardial infarction is an anatomical MI subtype most commonly caused by occlusion of the left circumflex artery (LCX), affecting the posterior and lateral walls of the left ventricle. While this subtype is not routinely separated in large beta-blocker trials, its underlying pathophysiology — acute coronary occlusion, ischaemia, myocyte necrosis, and ventricular remodelling — is identical to other MI types. The TxGNN knowledge graph most likely generated this prediction by identifying the shared pathophysiological nodes connecting β1-blockade to myocardial protection across all MI anatomical subtypes.

The overall class evidence supporting beta-blockers (including atenolol) in MI is extensive: landmark trials such as ISIS-1, COMMIT/CCS-2, and CAPRICORN have demonstrated reductions in mortality, reinfarction, and ventricular remodelling. This body of evidence supports extrapolation to posterolateral MI by class effect. However, no specific trials or publications exist for atenolol in posterolateral MI as a distinct indication — this TxGNN prediction is best interpreted as confirming mechanistic consistency rather than identifying a genuinely novel repurposing opportunity.

---

## Clinical Trial Evidence

Currently no clinical trials specifically registered for Atenolol in Posterolateral Myocardial Infarction.

> **Context**: The absence of trials for this subtype reflects standard MI trial methodology — large RCTs enrol all MI types without anatomical subtype stratification. Beta-blocker benefit across MI is robustly supported by multiple Phase 3 trials not specific to posterolateral MI (see Conclusion section).

---

## Literature Evidence

Currently no specific literature available for Atenolol in Posterolateral Myocardial Infarction.

> **Related evidence from adjacent indication**: For **Posteroinferior Myocardial Infarction** (rank 2, same TxGNN score of 99.87%), one directly relevant publication exists:
>
> | PMID | Year | Type | Journal | Key Findings |
> |------|------|------|---------|-------------|
> | [3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) | 1985 | RCT (crossover, single-blind) | La Revue de medecine interne | Compared anti-ischaemic activity of atenolol 200 mg vs diltiazem 240 mg in 23 patients undergoing rehabilitation 4 weeks after a limited postero-inferior or anterior MI. Exercise testing via bicycle ergometer with computerised analysis (CASE-Marquette). Directly relevant to beta-blocker efficacy in inferior MI subtype. |

---

## South Africa Market Information

According to the evidence pack, atenolol currently has **no SAHPRA registrations** on record, with market status listed as **Not marketed**.

> ⚠️ **Important — likely data gap**: Atenolol is an off-patent generic medicine first approved in the 1970s, included on the South African and WHO Essential Medicines Lists. The absence of registration data in this evidence pack is inconsistent with its established availability in South Africa. Healthcare professionals should:
> - Verify current SAHPRA registration and approved indications at [www.sahpra.org.za](https://www.sahpra.org.za/)
> - Note that the Essential Medicines List designation supports access in the public sector
> - Contact the SAHPRA Medicines Regulatory Affairs office if registration information cannot be confirmed

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA via [www.sahpra.org.za](https://www.sahpra.org.za/).

> The evidence pack did not return SAHPRA-specific safety data. The following are well-documented class considerations for atenolol based on its pharmacological profile — healthcare professionals must consult the approved PI for complete guidance:
> - **Abrupt withdrawal risk**: Do not stop suddenly — may precipitate rebound angina, acute MI, or severe hypertension; taper dose gradually
> - **Contraindicated** in cardiogenic shock, decompensated heart failure, severe bradycardia (< 45–50 bpm), second- or third-degree AV block without pacemaker, and sick sinus syndrome
> - **Reactive airways disease**: Bronchospasm risk even with β1-selective agents; use with extreme caution in asthma; COPD requires individualised risk-benefit assessment
> - **Diabetes mellitus**: May mask tachycardia as a warning sign of hypoglycaemia; prolonged hypoglycaemic episodes possible
> - **Renal impairment**: Atenolol is renally cleared — dose reduction required in significant renal dysfunction

---

## All Predicted Indications Summary

This evidence pack evaluates 9 TxGNN-predicted indications for atenolol (candidate ID: TW-DB00335-multi). The table below summarises all predictions with their evidence levels and recommended decisions:

| Rank | Disease | TxGNN Score | Evidence Level | Trials / Publications | Decision |
|------|---------|-------------|----------------|-----------------------|---------|
| 1 | Posterolateral Myocardial Infarction | 99.87% | L4 | 0 / 0 | Hold |
| 2 | Posteroinferior Myocardial Infarction | 99.87% | L4 | 0 / 1 | Hold |
| 3 | Malignant Hypertensive Renal Disease | 99.85% | L5 | 0 / 0 | Hold |
| 4 | Malignant Renovascular Hypertension | 99.85% | L4 | 0 / 1 | Hold |
| 5 | Pulmonary Hypertension — Multifactorial | 99.84% | L5 | 0 / 0 | Hold |
| 6 | Pulmonary Hypertension — Lung Disease/Hypoxia | 99.84% | L5 | 0 / 0 | Hold |
| 7 | Septal Myocardial Infarction | 99.84% | L4 | 0 / 0 | Hold |
| 8 | Braddock Syndrome | 99.80% | L5 | 0 / 0 | Hold |
| **9** | **Chronic Pulmonary Heart Disease** | **99.04%** | **L3** | **1 / 15** | **Proceed with Guardrails ⭐** |

⭐ Highest evidence level among all predicted indications — detailed evidence tables follow below.

**Notes on specific "Hold" decisions:**
- **Pulmonary hypertension subtypes (ranks 5 & 6)**: The negative inotropic effect of atenolol poses genuine risk in right ventricular pressure overload; β-blockade is not mechanistically supported and may be harmful in Group 3 PH.
- **Braddock syndrome (rank 8)**: An extremely rare genetic syndrome (intellectual disability with congenital anomalies); no plausible mechanistic link to β1-adrenergic blockade. The high TxGNN score likely reflects indirect graph traversal via cardiovascular comorbidity nodes rather than a true pharmacological relationship.
- **Malignant renovascular hypertension (rank 4)**: RAAS-targeted agents (ACEi/ARB) are the mechanistic first choice in renin-dependent hypertension; beta-blockers have a secondary adjunctive role at best.

---

## Supplementary Evidence: Chronic Pulmonary Heart Disease (Rank 9)

**Mechanistic Rationale**: Chronic pulmonary heart disease (cor pulmonale) patients frequently carry cardiovascular comorbidities — coronary artery disease, systemic hypertension, and heart failure. In this setting, atenolol's cardiac-protective effects (reduced heart rate, lower myocardial oxygen demand, attenuation of ventricular remodelling) may deliver net clinical benefit. At low-to-moderate doses, β1-selectivity substantially reduces bronchospasm risk compared to non-selective agents. Multiple observational studies suggest improved cardiovascular outcomes in COPD patients treated with cardioselective beta-blockers, with the most relevant direct evidence coming from studies of atenolol, metoprolol, and bisoprolol in concurrent COPD/IHD populations.

### Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03278509](https://clinicaltrials.gov/study/NCT03278509) | Phase 4 | Active, Not Recruiting | 5,000 | **REDUCE-SWEDEHEART**: Registry-based RCT (Sweden) evaluating long-term beta-blocker therapy after MI with preserved left ventricular ejection fraction. Primary endpoint: composite of all-cause death or new MI. Although not designed specifically for chronic pulmonary heart disease, this large Phase 4 trial provides critical evidence on continued beta-blocker safety and efficacy in a population that may include patients with cardiopulmonary comorbidity. Estimated completion: December 2025. |

### Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11219471](https://pubmed.ncbi.nlm.nih.gov/11219471/) | 2001 | RCT | Clinical Therapeutics | Telmisartan vs atenolol (± HCTZ) for mild-to-moderate hypertension over 26 weeks; multicenter, randomised design. Atenolol reference arm provides controlled efficacy and tolerability data in a broad cardiovascular population. |
| [14520850](https://pubmed.ncbi.nlm.nih.gov/14520850/) | 2003 | Clinical Trial | Terapevticheskii Arkhiv | Direct comparison of atenolol, metoprolol, and bisoprolol in isolated systolic hypertension with comorbid diabetes and/or COPD. **Directly addresses the target population** — key efficacy and safety evidence for atenolol in this cardiopulmonary overlap setting. |
| [15881093](https://pubmed.ncbi.nlm.nih.gov/15881093/) | 2005 | Review | Terapevticheskii Arkhiv | Long-term atenolol use in IHD patients with COPD: systematic evaluation of respiratory function changes. Characterises the specific respiratory safety profile of atenolol in patients with obstructive airways disease and ischaemic heart disease. |
| [31524](https://pubmed.ncbi.nlm.nih.gov/31524/) | 1978 | Clinical Research | Lille Medical | Foundational early study of atenolol in chronic pulmonary patients with airway obstruction — among the earliest direct evidence for atenolol use in this specific population. |
| [6673339](https://pubmed.ncbi.nlm.nih.gov/6673339/) | 1983 | Comparative Study | Vutreshni Bolesti | Acebutolol vs Falicard in 30 COPD patients with concomitant IHD. Provides comparative beta-blocker tolerability data in the cardiopulmonary comorbidity context directly relevant to this indication. |
| [28982831](https://pubmed.ncbi.nlm.nih.gov/28982831/) | 2017 | Observational Study | BMJ Open | Population-based retrospective cohort: ACOS (asthma-COPD overlap) associated with significantly increased risk of coronary artery disease, cardiac dysrhythmia, and heart failure. Establishes the epidemiological burden of cardiovascular disease in obstructive lung disease — the patient population for this indication. |
| [30191469](https://pubmed.ncbi.nlm.nih.gov/30191469/) | 2018 | Retrospective Cohort | Cardiology and Therapy | Comparative cardiovascular hospitalisation risk: nebivolol vs atenolol and metoprolol in hypertensive patients. Provides real-world safety differentiation between atenolol and newer-generation β1-selective agents relevant to prescribing decisions. |
| [38700308](https://pubmed.ncbi.nlm.nih.gov/38700308/) | 2023 | Review | J Assoc Physicians India | Beta-blockers as first-line hypertension therapy: evolving role in IHD, tachyarrhythmias, and heart failure management. Current contextual review supporting beta-blocker positioning in complex cardiovascular patients. |
| [1686421](https://pubmed.ncbi.nlm.nih.gov/1686421/) | 1991 | Clinical Study | Cardiologia | Atenolol 50 mg/day for 1 year in 15 chronic heart failure patients of varied aetiology: improved ejection fraction (radionuclide angiography), increased exercise time, and higher VO2 max. Supports use in the heart failure component of chronic pulmonary heart disease. |
| [20354044](https://pubmed.ncbi.nlm.nih.gov/20354044/) | 2010 | Survey / Registry | Postgraduate Medical Journal | European Heart Survey: examination of resting heart rate in stable angina in relation to beta-blocker treatment, comorbidities, and outcomes. Provides real-world context for beta-blocker heart rate control in complex cardiovascular patients. |

---

## Conclusion and Next Steps

**Decision: Hold (Posterolateral Myocardial Infarction — Primary Prediction) / Proceed with Guardrails (Chronic Pulmonary Heart Disease — Rank 9)**

**Rationale:**

For **posterolateral myocardial infarction** (top TxGNN rank), the mechanistic basis for beta-blockade is robust and guideline-supported across all MI types, but the specific anatomical subtype designation carries no distinct evidence base — this TxGNN prediction likely reflects the model capturing generalised MI-beta-blocker relationships rather than identifying a new clinical opportunity. A "Hold" decision is appropriate; no new clinical trial or prescribing action is indicated beyond existing MI management guidelines.

For **chronic pulmonary heart disease** (rank 9), multiple observational studies and one large active Phase 4 trial (REDUCE-SWEDEHEART) provide indirect but coherent supporting evidence. The cardioprotective rationale is plausible, and low-to-moderate dose atenolol with close respiratory monitoring represents a considered clinical approach in patients where cardiovascular benefit may outweigh bronchospasm risk. A "Proceed with Guardrails" decision is justified.

**To proceed with Chronic Pulmonary Heart Disease (priority action items):**

1. **Confirm SAHPRA registration status** — verify atenolol's current registration and approved indications before any prescribing decision
2. **Obtain approved Professional Information (PI)** — review complete SAHPRA-approved warnings, contraindications, and dosing for relevant comorbidities
3. **Establish respiratory monitoring protocol** — baseline spirometry (FEV1, FVC), with follow-up at 4 and 12 weeks; pre-defined stopping rules for > 15% FEV1 decline or new respiratory symptoms
4. **Low-dose initiation** — begin at 25 mg daily with gradual titration; avoid standard 100 mg doses in patients with significant obstructive lung disease
5. **Multidisciplinary co-management** — cardiology and pulmonology input recommended; clear escalation pathway for respiratory deterioration
6. **Retrieve DrugBank MOA data** (Data Gap DG002) to support mechanistic analysis and pharmacovigilance reporting
7. **Consider local registry or observational study** — South African-specific data on cardioselective beta-blocker outcomes in chronic pulmonary heart disease would add valuable LMIC evidence

**To address evidence gaps for MI subtypes (Ranks 1, 2, 7):**

- Request subgroup analyses from existing large-scale MI beta-blocker trials (ISIS-1, COMMIT/CCS-2, REDUCE-SWEDEHEART) stratified by anatomical MI subtype
- No novel clinical programme for these indications is indicated; standard post-MI beta-blocker guidelines apply to posterolateral, posteroinferior, and septal MI

---

> *This report is produced for research purposes only and does not constitute medical advice. All drug repurposing candidates identified by TxGNN require clinical validation before application. South African healthcare professionals should consult SAHPRA-approved product information and current clinical guidelines. Adverse drug reactions should be reported to SAHPRA.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

