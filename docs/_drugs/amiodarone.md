---
layout: default
title: Amiodarone
parent: Moderate Evidence (L3-L4)
nav_order: 27
evidence_level: L4
indication_count: 10
---

# Amiodarone
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

# Amiodarone: From Ventricular Arrhythmias to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Amiodarone is an established oral antiarrhythmic drug registered in South Africa. The SAHPRA data supplied do not state its approved indication.
The TxGNN model predicts it may be effective for **catecholaminergic polymorphic ventricular tachycardia (CPVT)**, with a very high score.
However, there are **0 registered clinical trials** and **10 publications** for this pairing, and none of the publications shows that amiodarone works in CPVT.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data supplied (amiodarone is an established antiarrhythmic for ventricular arrhythmias) |
| Predicted New Indication | Catecholaminergic polymorphic ventricular tachycardia (CPVT) |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the pack. Amiodarone is known as a multichannel blocker, acting on potassium, sodium and calcium channels and on beta-adrenergic receptors. CPVT is a rare inherited arrhythmia caused by unstable calcium release in heart muscle cells (RYR2 or CASQ2 gene variants), triggered by adrenaline surges during exercise or stress.

The two conditions are both ventricular arrhythmias, which likely explains the high model score. Any benefit from amiodarone in CPVT would be indirect, because it does not target the calcium-release defect. Guidelines favour beta-blockers and flecainide for CPVT. The retrieved literature does not support amiodarone efficacy in CPVT, so the score should be read as a similarity signal, not proof of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered for CPVT.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Review | Expert Opin Pharmacother | General review of drug treatment for ventricular arrhythmias. Antiarrhythmic drugs remain important for acute conversion and chronic prevention. Not CPVT-specific |
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Systematic review | Life (Basel) | Clinical features, genetics and arrhythmic outcomes of CPVT patients in China. Describes the disease, not amiodarone efficacy |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Cohort | Rev Cardiovasc Med | Retrospective cohort of CPVT in a Chinese city covering genetics, healthcare use and costs. No amiodarone efficacy data |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Case report | Pacing Clin Electrophysiol | Flecainide suppressed defibrillator-induced storming in a boy with CPVT (CASQ2 variant). Concerns flecainide, not amiodarone |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Case report | Front Cardiovasc Med | Right cardiac sympathetic denervation resolved CPVT in a teenager after left-sided denervation. Non-drug therapy |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case report | Medicine | CPVT with an RYR2 variant in a 9-year-old, diagnosed 6 years late. Highlights delayed diagnosis |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Case report | Turk Pediatri Arsivi | CPVT presenting as sudden cardiac arrest in a 2-year-old |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Case report | BMJ Case Reports | Young child with recurrent VT/VF arrest despite 40 shocks, illustrating when to deviate from standard resuscitation |
| [17125720](https://pubmed.ncbi.nlm.nih.gov/17125720/) | 2006 | Case report | Rev Esp Cardiol | Arrhythmic storm triggered by defibrillator discharge in a CPVT patient |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | Case report | Anesth Analg | Neonate with long QT syndrome and refractory VT treated with lidocaine, esmolol and amiodarone. This is not CPVT |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 32/6.2/0650 | Hexarone | Tablet | Not stated in supplied data |
| Reg. No. 56/6.2/0549 | Myorythm 100 | Tablet | Not stated in supplied data |

Only oral tablet forms are registered in the supplied data.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for CPVT is very high (99.78%), but there are no registered trials and no retrieved study supports amiodarone efficacy in CPVT. Beta-blockers and flecainide are the guideline-favoured options, and the mechanistic link is indirect.

**Other predictions in the pack:**
- **Ventricular tachycardia (rank 3)** is far better supported. It has L1 evidence, including the VANISH and PROCAMIO randomised trials and the OPTIC trial. The Phase 3 Early-Amio trial (NCT06680869) is still recruiting. It is effectively an established use rather than true repurposing, and it carries a "Proceed with Guardrails" recommendation. The guardrails are long-term pulmonary, thyroid and hepatic toxicity, QT prolongation and drug interactions.
- **Incessant infant ventricular tachycardia (rank 2)** is an L3 research question. Infant safety needs a dedicated review.
- **Rheumatoid arthritis, gout, trichotillomania, obsolete bundle branch block, and the three rare congenital syndromes** show no plausible mechanistic link. They should stay on Hold. In rheumatoid arthritis, the literature mainly reports amiodarone lung toxicity, which is a safety signal rather than efficacy.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indications) for Hexarone and Myorythm 100
- Detailed mechanism of action data (e.g. from DrugBank)
- CPVT-specific efficacy and safety data for amiodarone, for example comparative or registry studies against beta-blockers and flecainide
- A decision on whether to prioritise the ventricular tachycardia indication instead, with a safety monitoring plan

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

