---
layout: default
title: Amiodarone
parent: Model Prediction Only (L5)
nav_order: 27
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Amiodarone: predicted new indication Catecholaminergic polymorphic ventricular tachycardia (evidence level L5). Approved use: Ventricular fibrillation"
monitor_inn: "Amiodarone"
predicted_indications: ["catecholaminergic polymorphic ventricular tachycardia", "incessant infant ventricular tachycardia", "ventricular tachycardia", "obsolete bundle branch block", "rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "heparin cofactor 2 deficiency", "trichotillomania", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "gout"]
---

# Amiodarone
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

# Amiodarone: From Ventricular Fibrillation to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Amiodarone is an antiarrhythmic drug, originally used for life-threatening ventricular arrhythmias such as ventricular fibrillation.
The TxGNN model predicts it may be effective for **catecholaminergic polymorphic ventricular tachycardia (CPVT)**,
but there are currently **0 registered clinical trials** and **9 publications** on CPVT, none of which show amiodarone efficacy in this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ventricular fibrillation (from the knowledge-graph indication record; SAHPRA indication text was not available) |
| Predicted New Indication | Catecholaminergic polymorphic ventricular tachycardia |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 (mechanistic rationale only; no studies of amiodarone in CPVT) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Amiodarone blocks several ion channels (potassium, sodium and calcium) and also blocks beta-adrenergic receptors. Together these actions prolong repolarisation and refractoriness and suppress ventricular arrhythmias. Detailed mechanism-of-action data was not included in the data compiled for this report, so this description is based on the drug's general pharmacology.

CPVT is a rare inherited arrhythmia. It is caused by abnormal calcium release inside heart muscle cells (typically *RYR2* or *CASQ2* variants) and is triggered by exercise or adrenaline. Amiodarone's beta-blocking and partial calcium-channel effects could plausibly dampen this trigger, and CPVT is a ventricular arrhythmia like the drug's original indication.

The link is indirect, however. Beta-blockers and flecainide are the established CPVT therapies. None of the CPVT publications reviewed demonstrates a benefit from amiodarone. The prediction should therefore be treated as a hypothesis, not as supported use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Systematic review | Life (Basel) | Clinical features, genetics and arrhythmic outcomes of CPVT in patients from China. Does not address amiodarone. |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Cohort | Rev Cardiovasc Med | Retrospective cohort of CPVT: clinical features, genetics, healthcare use and costs. |
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Review | Expert Opin Pharmacother | Overview of drug treatment of ventricular arrhythmias; antiarrhythmics remain important for acute conversion and chronic prevention. |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Case report | Pacing Clin Electrophysiol | Flecainide suppressed defibrillator-induced storming in a boy with CPVT (a flecainide report, not amiodarone). |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | Case report | Anesth Analg | Neonate with long QT syndrome and refractory ventricular arrhythmia managed with lidocaine, esmolol and amiodarone. Not CPVT. |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Case report | Turk Pediatri Arsivi | CPVT presenting as sudden cardiac arrest in a 2-year-old. |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case report | Medicine | Six-year delayed CPVT diagnosis in a child with an *RYR2* variant. |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Case report | Front Cardiovasc Med | CPVT in a teenager resolved with right cardiac sympathetic denervation after left-sided denervation. |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Case report | BMJ Case Rep | Young child with cardiac arrest and recurrent VT/VF; diagnostic dilemma and departure from standard resuscitation guidelines. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 32/6.2/0650 | Hexarone | Tablet | Indication text not available in the compiled data |
| Reg. No. 56/6.2/0549 | Myorythm 100 | Tablet | Indication text not available in the compiled data |

Both registrations are valid, single-ingredient oral tablets. Only the oral route is registered.

---

## Safety Considerations

SAHPRA package-insert warnings and contraindications were not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for these, and report adverse drug reactions to SAHPRA.

**Knowledge-graph contraindication signals** (these come from a research knowledge graph, not label text, and must be checked against the PI):
- **Cardiac conduction and rhythm:** long QT syndrome (including familial), torsades de pointes, atrioventricular block, sick sinus syndrome
- **Thyroid:** hypothyroidism, myxedema, congenital hypothyroidism, hyperthyroidism, Graves disease, thyrotoxicosis
- **Lung:** interstitial lung disease, eosinophilic pneumonia, pulmonary eosinophilia, hypersensitivity pneumonitis (extrinsic allergic alveolitis, farmer's lung)
- **Liver and gallbladder:** liver disease, drug-induced liver injury, gallbladder disease
- **Eye:** optic neuritis, optic nerve disease, visual pathway disease, corneal deposit
- **Nerves:** peripheral neuropathy, peripheral nervous system disease
- **Other:** potassium deficiency disease

**Drug interactions:** 100 interactions were identified; the first 20 returned are summarised here.
- **Major:** agalsidase beta, hydrocortisone, dexamethasone, amphotericin B (including cholesteryl sulfate, lipid complex and liposomal forms), cisapride, clarithromycin, clotrimazole, dolasetron, eliglustat
- **Moderate:** famotidine, cimetidine, aprepitant, bisacodyl, budesonide (including nasal), castor oil
- **Minor:** fidaxomicin

Many of the major interactions involve QT prolongation or electrolyte disturbance, so they matter in any arrhythmia setting. The full interaction list should be reviewed before any use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The CPVT prediction rests on an indirect mechanistic argument. There are no registered trials and no publication showing that amiodarone helps CPVT, and beta-blockers and flecainide are already the established therapies.
- Amiodarone's toxicity profile (thyroid, lung, liver and eye effects, QT prolongation, many interactions) raises the bar for using it without evidence of benefit.

**To proceed, the following is needed:**
- Evidence of amiodarone's effect specifically in CPVT, such as cohort data or comparison with beta-blockers and flecainide
- The SAHPRA Professional Information (warnings, contraindications and approved indications), so a safety screen can be completed
- Detailed mechanism-of-action data for amiodarone, to assess how it would act on *RYR2*/*CASQ2*-driven calcium leak
- A monitoring plan for thyroid, liver, lung and QT effects, and for interactions

**Other predictions for this drug (for context):**
- **Ventricular tachycardia (rank 3):** This is the best-supported prediction (L1, Proceed with Guardrails). It is essentially an on-label or near-label use, backed by Phase 3 trials such as AVID (NCT00000531) and ALPS (NCT01401647) and a randomised comparison with procainamide (PMID 27354046). It is a more productive direction than CPVT.
- **Incessant infant ventricular tachycardia (rank 2):** There is a randomised paediatric trial of IV amiodarone (PMID 16316969), but the cohorts mix supraventricular and ventricular rhythms and no trial is registered. This is a research question, with neonatal safety concerns.
- **Ranks 4–10 (obsolete bundle branch block, rheumatoid arthritis, brachydactyly-syndactyly syndrome, heparin cofactor 2 deficiency, trichotillomania, colobomatous microphthalmia-rhizomelic dysplasia syndrome, gout):** These have no supporting therapeutic evidence and appear to be model or knowledge-graph artefacts. For rheumatoid arthritis, the literature mainly describes amiodarone lung toxicity. All are recommended as Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

