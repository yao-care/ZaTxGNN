---
layout: default
title: Amiodarone
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 10
---

# Amiodarone
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

# Amiodarone: From Cardiac Arrhythmia to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Amiodarone is a broad-spectrum Class III antiarrhythmic agent with decades of clinical use in life-threatening ventricular and supraventricular arrhythmias, including ventricular tachycardia and fibrillation.
The TxGNN model predicts it may be effective for **Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)** — a rare inherited arrhythmia syndrome triggered by adrenergic stimulation — with **0 registered clinical trials** and **10 publications** currently informing this direction.
The available evidence positions amiodarone primarily as a salvage agent in β-blocker- and flecainide-refractory CPVT rather than a genuinely novel first-line repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Life-threatening ventricular tachycardia/fibrillation and supraventricular arrhythmias (Class III antiarrhythmic) |
| Predicted New Indication | Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L3 |
| South Africa Market Status | Not Marketed (per current dataset; independent verification strongly recommended) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data is not available in the current evidence pack. Based on established pharmacological knowledge, amiodarone is a Class III antiarrhythmic agent that primarily blocks IKr/IKs potassium channels, prolonging cardiac action potential duration and the effective refractory period across both atrial and ventricular tissue. Uniquely among antiarrhythmics, it also carries Class I (sodium channel blockade), Class II (non-competitive β-adrenergic blockade), and Class IV (calcium channel blockade) properties — making it the broadest-spectrum antiarrhythmic in routine clinical use.

CPVT is caused by gain-of-function mutations in the RYR2 gene (cardiac ryanodine receptor) or loss-of-function mutations in CASQ2 (calsequestrin-2), which result in abnormal spontaneous calcium release from the sarcoplasmic reticulum during catecholaminergic stimulation. This generates delayed afterdepolarisations (DADs) and triggered ventricular arrhythmias. Amiodarone's multi-modal mechanism theoretically targets CPVT through at least three distinct pathways: its β-blocking effect suppresses the adrenergic trigger; sodium channel blockade inhibits DAD propagation; and calcium channel blockade reduces triggered activity at the cellular level.

Despite this plausible mechanistic rationale, β-blockers (particularly nadolol) and flecainide — which directly suppresses pathological RYR2-mediated calcium leakage — remain the established first-line therapies for CPVT according to current international guidelines. Amiodarone is used clinically only as a rescue agent in refractory cases or during ICD-triggered electrical storms. The TxGNN model's high prediction score (99.78%) reflects genuine mechanistic overlap and existing salvage-use precedent, but does not represent discovery of a new primary indication.

---

## Clinical Trial Evidence

Currently no clinical trials specifically studying amiodarone in catecholaminergic polymorphic ventricular tachycardia are registered on ClinicalTrials.gov or the WHO International Clinical Trials Registry Platform (ICTRP).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Review | Expert Opin Pharmacother | Comprehensive review of pharmacotherapy for ventricular arrhythmias; discusses amiodarone's multi-channel properties and its role as a broad-spectrum rescue agent in refractory arrhythmia syndromes, including channelopathies |
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Cohort | Life (Basel) | Systematic review of CPVT clinical characteristics, genetic basis (RYR2/CASQ2), and arrhythmic outcomes in Chinese patients; provides reference data on management patterns and outcomes across different populations |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Cohort | Rev Cardiovasc Med | Retrospective cohort of CPVT patients examining genetic basis, healthcare resource utilisation, and costs — relevant for understanding the burden of this rare disease in resource-constrained healthcare settings |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Case Series | Pacing Clin Electrophysiol | Flecainide successfully suppressed ICD-triggered arrhythmic storms in a CPVT patient with CASQ2 mutation after prior therapies including amiodarone failed; directly illustrates the clinical treatment hierarchy |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Case Report | BMJ Case Rep | Paediatric out-of-hospital cardiac arrest with suspected CPVT requiring 40 defibrillation shocks; amiodarone administered as part of advanced resuscitation, illustrating its role in acute haemodynamic rescue |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Case Report | Front Cardiovasc Med | Teenager with CPVT refractory to left cardiac sympathetic denervation, subsequently treated with right denervation; describes the full escalating treatment ladder in which pharmacotherapy — including amiodarone — precedes invasive intervention |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | Case Report | Anesth Analg | Neonatal long QT syndrome with compound mutation and refractory polymorphic VT; multimodal pharmacotherapy including amiodarone, lidocaine, and esmolol required — highlights amiodarone's utility in neonatal refractory arrhythmia |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case Report | Medicine | 9-year-old with 6-year delayed CPVT diagnosis (RYR2 c.7580T>G mutation); highlights the diagnostic challenges in paediatric patients and the consequences of delayed recognition |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Case Report | Turk Pediatri Arsivi | CPVT presenting as sudden cardiac arrest in a 2-year-old in the absence of structural heart disease; underscores the severity and age of onset, and the need for rapid antiarrhythmic intervention |
| [17125720](https://pubmed.ncbi.nlm.nih.gov/17125720/) | 2006 | Case Report | Rev Esp Cardiol | Arrhythmic storm triggered by ICD discharge in a CPVT patient; amiodarone used in managing ICD-induced hyperadrenergic state — defines the specific clinical niche where amiodarone has documented CPVT utility |

---

## South Africa Market Information

No active SAHPRA product registrations for amiodarone were identified in the current dataset. This likely represents a data gap rather than a true absence from the South African market.

> **Important**: Amiodarone (both intravenous and oral formulations) is included on the **South African National Essential Medicines List (NEML)** and is stocked in most South African public sector hospitals for resuscitation and arrhythmia management. Healthcare professionals should verify current registered products directly through the [SAHPRA online medicines register](https://www.sahpra.org.za) before prescribing, and confirm local availability with their pharmacy and therapeutics committee.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for complete safety information. Report adverse drug reactions to SAHPRA via the MedSafety portal (medwatch.sahpra.org.za).

> The source dataset does not contain formal safety data for this drug. The following safety considerations are well-documented in published medical literature and are particularly relevant for CPVT, which predominantly affects children and young adults requiring long-term treatment:
>
> - **Pulmonary toxicity**: Amiodarone-induced interstitial pneumonitis or pulmonary fibrosis is a serious dose- and duration-dependent toxicity; annual chest X-ray and pulmonary function testing are recommended
> - **Thyroid dysfunction**: Amiodarone contains approximately 37% iodine by weight and causes hypothyroidism or hyperthyroidism in up to 15–20% of patients; thyroid function tests every 6 months are mandatory
> - **Hepatotoxicity**: Elevated transaminases are common; periodic liver function monitoring is required
> - **Corneal microdeposits**: Occur in virtually all long-term users; annual ophthalmological review is recommended
> - **QT prolongation**: Risk of torsades de pointes, particularly when co-administered with other QT-prolonging agents; regular ECG monitoring required
> - **Paediatric considerations**: Pharmacokinetic data in neonates and infants is limited; paediatric dosing and monitoring should be guided by a specialist in paediatric electrophysiology

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While amiodarone's broad-spectrum multi-channel mechanism provides a pharmacologically plausible basis for activity in CPVT, no dedicated randomised clinical trials have been conducted, and all available evidence consists of case reports and observational cohorts that consistently describe amiodarone as a secondary or rescue agent after established first-line therapies have failed. Furthermore, amiodarone's well-documented long-term toxicity burden — including pulmonary, thyroid, and hepatic effects — raises significant concerns for use in the predominantly paediatric CPVT population, where treatment is typically lifelong.

**To proceed, the following is needed:**
- Independent verification of current SAHPRA registration status and local availability of amiodarone formulations in South Africa
- Prospective case series or multi-centre registry data specifically evaluating amiodarone in β-blocker- and flecainide-refractory CPVT to define its clinical benefit in this niche rescue role
- Formal mechanism of action data from DrugBank (DB01118) to complete the pharmacological risk–benefit assessment
- Paediatric-specific safety, pharmacokinetic, and dosing data for long-term amiodarone use in CPVT
- Consideration of a formal position within local treatment guidelines that defines amiodarone's role relative to cardiac sympathetic denervation, ICD implantation, and emerging therapies in the CPVT management algorithm

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All content should be interpreted in conjunction with current SAHPRA-approved prescribing information and relevant clinical guidelines.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

