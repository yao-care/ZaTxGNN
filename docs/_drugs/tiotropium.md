---
layout: default
title: Tiotropium
parent: Model Prediction Only (L5)
nav_order: 449
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-05
monitor_inn: "TIOTROPIUM"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome", "hyperlucent lung", "tracheal stenosis"]
description: "Tiotropium: predicted new indication Respiratory malformation (evidence level L5). Approved use: Not recorded in the local data"
---

# Tiotropium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Tiotropium: Respiratory malformation
{: .text-alpha }

## One-Sentence Summary

Tiotropium is an inhaled long-acting muscarinic antagonist (anticholinergic bronchodilator). The TxGNN model predicts it may be useful for **respiratory malformation**. The 3 linked clinical trials and 5 publications do not study this condition directly, so the prediction rests mainly on the model score.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Respiratory malformation |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 6 of 9) |
| Number of SAHPRA Registrations | 9 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Tiotropium belongs to the class of long-acting muscarinic antagonists. These drugs block muscarinic receptors in the airways, relax airway smooth muscle and reduce cholinergic bronchoconstriction.

Respiratory malformations are structural abnormalities of the airways or lungs. Some patients have secondary airflow obstruction or excess cholinergic tone, and bronchodilation might ease these. This is a theoretical link only. Structural defects themselves would not respond to a bronchodilator, and no evidence in the supplied data shows benefit in patients with these malformations.

## Clinical Trial Evidence

The linked trials were done in cystic fibrosis, not in patients with respiratory malformations. They are only indirectly relevant. They do give some safety, tolerability and dose information for inhaled tiotropium in a different chronic lung condition.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01179347](https://clinicaltrials.gov/study/NCT01179347) | Phase 3 | Completed | 464 | Placebo-controlled 12-week study of tiotropium 5 mcg once daily via Respimat in cystic fibrosis, assessing efficacy and safety |
| [NCT00737100](https://clinicaltrials.gov/study/NCT00737100) | Phase 2 | Completed | 510 | Placebo-controlled 12-week dose-finding study (2.5 and 5 mcg) of lung function, safety and pharmacokinetics in cystic fibrosis |
| [NCT02172534](https://clinicaltrials.gov/study/NCT02172534) | Phase 1 | Completed | 113 | Safety, tolerability and pharmacokinetics of single and 28-day multiple doses in children, adolescents and adults with cystic fibrosis |

No SANCTR or PACTR registrations were identified in the data compiled for this report.

## Literature Evidence

None of these publications addresses respiratory malformation treated with tiotropium.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26229457](https://pubmed.ncbi.nlm.nih.gov/26229457/) | 2015 | Review | Int J Chron Obstruct Pulmon Dis | Role of dual bronchodilation (indacaterol-glycopyrronium) in chronic airway disease, covering patient-reported outcomes and quality of life |
| [31522031](https://pubmed.ncbi.nlm.nih.gov/31522031/) | 2019 | Clinical trial (physiological) | Respir Med | Lung deflation with tiotropium/olodaterol altered cardiocirculatory responses to exertion in hyperinflated patients |
| [22608352](https://pubmed.ncbi.nlm.nih.gov/22608352/) | 2012 | Observational (mechanistic) | Respir Med | Nasal ciliary beating was depressed in chronic airway disease, linked to disease severity |
| [40850565](https://pubmed.ncbi.nlm.nih.gov/40850565/) | 2025 | Preclinical | Chem Biol Interact | Cholinergic mechanisms of ventilatory dysfunction in mice exposed to a nerve agent |
| [33787023](https://pubmed.ncbi.nlm.nih.gov/33787023/) | 2021 | Case report | Rev Fac Cien Med Univ Nac Cordoba | COVID-19 in a young patient with pectus excavatum, a chest-wall deformity with altered lung function |

## South Africa Market Information

Tiotropium is marketed in South Africa. The indication text is not recorded in the local data for any of them.

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 36/10.2.1/0044 | Spiriva inh.caps 30 with handihaler | Kit | Valid |
| 36/10.2.1/0045 | Forvent handihaler complete with 30 inh | Kit | Valid |
| 50/10.2.1/0671 | Tiores | capsule | Valid |
| 51/10.2.1/0143 | Neumotropio | capsule | Valid |
| 57/10.2.1/0007 | Fibrotiem | capsule | Valid |

Showing 5 of 9 registrations (valid registrations first).

Essential Medicines List status is not available in the data compiled for this report.

## Safety Considerations

SAHPRA package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

- **Conditions needing caution with anticholinergic bronchodilators** (not taken from label text; confirm against the PI):
  - benign prostatic hyperplasia
  - bladder neck obstruction
  - angle-closure (closed-angle) glaucoma
  - impaired renal function
- **Drug Interactions**: 100 interactions were found. The main concern is additive anticholinergic effects with other antimuscarinic drugs. Moderate-level interactions include:
  - hyoscyamine
  - atropine
  - glycopyrronium (including topical)
  - clidinium
  - dicyclomine
  - trospium
  - mepenzolate
  - methscopolamine
  - propantheline
  - scopolamine
  - eluxadoline
  - prucalopride
  - inhaled human insulin

  Cimetidine is a minor interaction.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction score is high, but no trial or publication studies tiotropium in respiratory malformation. The evidence is model prediction only (L5).
- Structural defects are unlikely to respond to bronchodilation, and the benefit would be limited to any secondary airflow obstruction.

**To proceed, the following is needed:**
- Clinical or observational data in patients with respiratory malformations showing a measurable bronchodilator response
- Definition of which malformation types and patient subgroups could plausibly benefit
- Mechanism of action data and the SAHPRA Professional Information (warnings, contraindications, approved indication text)
- A safety review for paediatric use, since many malformations present in children

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

