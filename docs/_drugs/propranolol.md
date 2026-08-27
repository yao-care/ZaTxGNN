---
layout: default
title: Propranolol
parent: 僅模型預測 (L5)
nav_order: 382
evidence_level: L5
indication_count: 10
---

# Propranolol
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

# Propranolol: From Beta-Blocker Cardiovascular Therapy to Cardiomyopathy

## One-Sentence Summary

Propranolol is a long-established non-selective beta-adrenergic blocker; this evidence pack screened it against thousands of diseases via TxGNN and returned 10 candidate new indications, most with **no supporting clinical or literature evidence**. The one candidate with genuine, decades-deep support is **Cardiomyopathy** (specifically the hypertrophic cardiomyopathy phenotype), backed by **3 clinical trials** and **20 publications**, including a randomized double-blind trial. The model's single *highest*-scoring prediction (distal myopathy, Tateyama type) is explicitly flagged in the evidence pack itself as a likely knowledge-graph artifact rather than a real mechanistic signal — see the note below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (drug/company-level `original_indications` and SA licence data are both empty — data gap). Propranolol is internationally recognized as a non-selective β-blocker used across hypertension, arrhythmia, and angina. |
| Predicted New Indication | Cardiomyopathy (hypertrophic cardiomyopathy phenotype) |
| TxGNN Prediction Score | 99.12% (rank 4410 in full model output; rank 6 of 10 candidates in this pack) |
| Evidence Level | L1 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Important caveat:** This drug's *numerically top-ranked* TxGNN prediction is "distal myopathy, Tateyama type" (score 99.40%), not cardiomyopathy. The evidence pack's own rationale states this connection has "no known biological relationship to propranolol's β-adrenergic blocking mechanism" and is likely driven by knowledge-graph proximity to the general "myopathy" category rather than real mechanistic evidence (Evidence Level L5, decision stage S0, recommendation: **Hold**). We lead this report with cardiomyopathy instead because it is the only candidate with substantive trial and literature support — see the full ranking table below.

---

## Why is This Prediction Reasonable?

Detailed formal MOA data for propranolol is not present in this evidence pack (data gap). Based on the drug-level evidence that is available, propranolol is a **non-selective β1/β2-adrenergic receptor antagonist**. Its negative inotropic and negative chronotropic effects reduce myocardial contractility, heart rate, and myocardial oxygen consumption, and in obstructive cardiomyopathy this reduces the left ventricular outflow tract (LVOT) pressure gradient.

This mechanism is not a novel hypothesis — propranolol has been used empirically in hypertrophic cardiomyopathy (HCM) since at least the early 1970s, and the literature evidence below includes a randomized double-blind trial from 1973 through hemodynamic studies spanning five decades. The relationship between propranolol's original cardiovascular pharmacology and the cardiomyopathy indication is therefore direct and mechanistically explicit, rather than an extrapolation across unrelated organ systems.

By contrast, several of the other candidates flagged by TxGNN in this pack (distal myopathy, congenital myopathy with excess thin filaments, chondroma) involve structural/genetic pathologies (sarcomere protein defects, cartilage neoplasia) with **no known connection** to β-adrenergic blockade, and carry zero clinical trial or literature support — these are explicitly marked as Hold/S0 in the source rationale.

---

## Overview of All Predicted Indications (This Pack)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Distal myopathy, Tateyama type | 99.40% | L5 | S0 | Hold |
| 2 | Congenital myopathy with excess of thin filaments | 99.30% | L5 | S0 | Hold |
| 3 | Hypertrophic cardiomyopathy due to intensive athletic training | 99.17% | L4 | S1 | Research Question |
| 4 | Chondroma | 99.14% | L5 | S0 | Hold |
| 5 | Cirrhotic cardiomyopathy | 99.12% | L3 | S2 | Research Question |
| 6 | **Cardiomyopathy** (featured above) | 99.12% | **L1** | S3 | **Proceed with Guardrails** |
| 7 | Intramuscular hemangioma | 98.97% | L2 | S2 | Proceed with Guardrails |
| 8 | Maffucci syndrome | 98.97% | L4 | S1 | Research Question |
| 9 | Breast epithelioid hemangioma | 98.91% | L3 | S2 | Research Question |
| 10 | Breast capillary hemangioma | 98.90% | L2 | S3 | Proceed with Guardrails |

---

## Clinical Trial Evidence — Cardiomyopathy

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04767061](https://clinicaltrials.gov/study/NCT04767061) | Phase 4 | Completed | 9 | N-of-1 trials of beta-blocker deprescribing in HFpEF (a cardiomyopathy phenotype); directly relevant, completed, but very small sample. |
| [NCT05019027](https://clinicaltrials.gov/study/NCT05019027) | Phase 4 | Enrolling by invitation | 20 | N-of-1 deprescribing trials in older adults with transthyretin cardiac amyloidosis; indirectly relevant to beta-blocker use in cardiomyopathy populations. |
| [NCT05427474](https://clinicaltrials.gov/study/NCT05427474) | Phase 3 | Unknown | 90 | Propranolol + gabapentin for paroxysmal sympathetic hyperactivity after traumatic brain injury; supports autonomic-modulating role, not a cardiomyopathy efficacy trial. |

## Literature Evidence — Cardiomyopathy

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4586631](https://pubmed.ncbi.nlm.nih.gov/4586631/) | 1973 | RCT | British Heart Journal | Double-blind trial of propranolol vs. practolol in hypertrophic cardiomyopathy. |
| [7200796](https://pubmed.ncbi.nlm.nih.gov/7200796/) | 1982 | Cohort | British Heart Journal | Combined nifedipine + propranolol superior to nifedipine alone for hemodynamics in hypertrophic obstructive cardiomyopathy (HOCM). |
| [1611637](https://pubmed.ncbi.nlm.nih.gov/1611637/) | 1992 | Cohort | Cardiology | Propranolol and disopyramide effects on LV function at rest/exercise in HCM. |
| [7192151](https://pubmed.ncbi.nlm.nih.gov/7192151/) | 1980 | Cohort | British Heart Journal | Propranolol effects on myocardial oxygen consumption and hemodynamics in HOCM. |
| [6686544](https://pubmed.ncbi.nlm.nih.gov/6686544/) | 1983 | Cohort | European Heart Journal | Propranolol vs. verapamil effects on diastolic stiffness in HCM. |
| [3673167](https://pubmed.ncbi.nlm.nih.gov/3673167/) | 1987 | Cohort | Zeitschrift für Kardiologie | Combined nifedipine + propranolol treatment in HCM over 6–24 months. |
| [8989641](https://pubmed.ncbi.nlm.nih.gov/8989641/) | 1996 | Cohort | Journal of Cardiac Failure | Hemodynamic predictors of propranolol tolerance and long-term effects in dilated cardiomyopathy. |
| [3189143](https://pubmed.ncbi.nlm.nih.gov/3189143/) | 1988 | Cohort | American Heart Journal | Acute hemodynamic effects of pindolol vs. propranolol in dilated cardiomyopathy. |
| [36104228](https://pubmed.ncbi.nlm.nih.gov/36104228/) | 2022 | Case Report | International Heart Journal | Infantile mitochondrial cardiomyopathy with LVOT stenosis treated with low-dose propranolol + cibenzoline. |
| [10460081](https://pubmed.ncbi.nlm.nih.gov/10460081/) | 1999 | Case Report | Pediatric Emergency Care | Acute dilated cardiomyopathy and CNS toxicity following propranolol overdose — safety signal relevant to dosing. |

---

## Other Predicted Indications (Condensed)

**Breast capillary hemangioma** (L2, Proceed with Guardrails) — Supported by [NCT04105517](https://clinicaltrials.gov/study/NCT04105517) (completed post-marketing surveillance of Hemangiol®/oral propranolol, n=500, in proliferative infantile hemangioma) and [NCT02732678](https://clinicaltrials.gov/study/NCT02732678) (Phase 1/2, propranolol + cyclophosphamide in angiosarcoma, status unknown). One supporting meta-analysis: [PMID 32647928](https://pubmed.ncbi.nlm.nih.gov/32647928/) (beta-antagonist + laser combination therapy for infantile hemangioma). Propranolol (as Hemangiol®) is an internationally approved therapy for infantile hemangioma; breast location is an anatomical subtype, not a distinct disease.

**Intramuscular hemangioma** (L2, Proceed with Guardrails) — No dedicated trials, but supported by a randomized double-blind trial of topical propranolol gel ([PMID 34719577](https://pubmed.ncbi.nlm.nih.gov/34719577/)) and multiple cohort studies of infantile hemangioma at deep/subglottic sites ([PMID 35512856](https://pubmed.ncbi.nlm.nih.gov/35512856/), [PMID 35988523](https://pubmed.ncbi.nlm.nih.gov/35988523/)). Mechanistic extrapolation from established infantile hemangioma indication; no intramuscular-subtype-specific trial registered.

**Cirrhotic cardiomyopathy** (L3, Research Question) — Propranolol is already standard therapy for variceal bleeding prophylaxis in cirrhosis. Evidence is mixed: [PMID 38738176](https://pubmed.ncbi.nlm.nih.gov/38738176/) reports correction of prolonged QTc, while [PMID 32446716](https://pubmed.ncbi.nlm.nih.gov/32446716/) reports non-selective beta-blockers can impair circulatory homeostasis and renal function in refractory ascites — a genuine safety trade-off requiring caution.

**Breast epithelioid hemangioma** (L3, Research Question) — 8 literature citations, predominantly cohort/case reports on infantile hemangioma of the breast generally ([PMID 38196847](https://pubmed.ncbi.nlm.nih.gov/38196847/), [PMID 20615772](https://pubmed.ncbi.nlm.nih.gov/20615772/)); no subtype-specific controlled trials.

**Hypertrophic cardiomyopathy due to intensive athletic training** (L4, Research Question) — Mechanistically plausible extension of the standard HCM rationale, but this athlete-specific subtype has distinct exercise-induced remodeling pathophysiology, competitive-eligibility implications, and zero direct trials or literature.

**Maffucci syndrome** (L4, Research Question) — Mechanistic extrapolation from the hemangioma indication only; the syndrome also involves non-vascular chondroma components. No direct evidence.

**Distal myopathy (Tateyama type), congenital myopathy with excess thin filaments, chondroma** (all L5, Hold) — No clinical trials, no literature, and the evidence pack's own rationale states these connections lack biological plausibility relative to propranolol's known pharmacology.

---

## South Africa Market Information

No SAHPRA registrations are recorded in this evidence pack (`total_licenses: 0`, market status: **Not Marketed**). No approved indication text, product name, or dosage form data is therefore available for this jurisdiction.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for the Cardiomyopathy indication specifically; **Hold** for the majority of other candidates in this pack, including the model's top-scoring prediction)

**Rationale:**
- Cardiomyopathy (HCM phenotype) is supported by an RCT and multiple cohort studies spanning 50 years, and reflects a mechanistically direct, already-practiced use of propranolol — evidence is sufficient to proceed cautiously.
- The TxGNN model's single highest-scoring candidate (distal myopathy, Tateyama type) has no clinical or literature support and is explicitly flagged in the source rationale as likely a knowledge-graph artifact; it should not be pursued on the strength of score alone.
- Breast/intramuscular hemangioma indications are reasonable secondary candidates given propranolol's approved status for infantile hemangioma (Hemangiol®), but lack subtype-specific trials.

**To proceed, the following is needed:**
- Formal mechanism-of-action (MOA) documentation for propranolol (currently a data gap)
- TFDA/SAHPRA-approved Professional Information (PI), including warnings, contraindications, and drug interactions (currently all data gaps)
- If pursuing the cirrhotic cardiomyopathy or hemangioma directions, a formal risk-benefit review given the conflicting renal/hemodynamic safety signals in cirrhosis and the pediatric population exposure profile for hemangioma indications
- Local SAHPRA registration status confirmation, since this evidence pack shows zero current licenses for this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

