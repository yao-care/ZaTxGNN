---
layout: default
title: Digoxin
parent: Model Prediction Only (L5)
nav_order: 178
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Digoxin: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Atrial fibrillation"
---

# Digoxin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Digoxin: From Atrial Fibrillation to Prinzmetal Angina

## One-Sentence Summary

Digoxin is a cardiac glycoside, originally used to treat **atrial fibrillation** and **digitalis poisoning**.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but there are currently **0 clinical trials** and only **1 loosely related publication** (a 1999 review that does not address digoxin in vasospastic angina). This prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation; digitalis poisoning (from the TxGNN knowledge graph, as the registration record contains no indication text) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Digoxin is known to inhibit the Na+/K+-ATPase pump, which raises intracellular calcium and increases heart muscle contractility. Its efficacy in atrial fibrillation (rate control) is established.

**The mechanistic link to Prinzmetal angina is weak.** Prinzmetal angina is caused by coronary artery vasospasm. Increased intracellular calcium and contractility could, in theory, make vasospasm *more* likely rather than less. No credible mechanism supporting benefit has been identified. The very high model score (0.998) is not backed by clinical data.

For context, the other predictions for this drug also lack support: duodenal obstruction, duodenal ulcer, duodenogastric reflux, hypoalphalipoproteinemia, and an obsolete ontology term for ischemic stroke susceptibility. None has a trial or a supportive publication. The stroke term is an obsolete entry and not an actionable indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiol Pharmacol Bulg | Chronopharmacology and antihypertensive treatment (circadian rhythms in drug response). It does not address digoxin in vasospastic angina, so it is not evidence of efficacy. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G.2846 | Lanoxin | Tablet (oral) | Not available in the registration record |

Essential Medicines List (EML) inclusion status could not be confirmed from the data compiled for this report.

## Safety Considerations

**Contraindications or disease associations (from knowledge graph, not label text):** The TxGNN knowledge graph links digoxin to the following conditions as contraindications. Those most relevant to a cardiac repurposing context include:
- Myocardial infarction and coronary thrombosis
- Sick sinus syndrome and atrioventricular block
- Wolff-Parkinson-White syndrome
- Ventricular fibrillation
- Hypertrophic and restrictive cardiomyopathy, cor pulmonale, myocarditis, constrictive pericarditis
- Kidney disease
- Electrolyte disorders: potassium deficiency, hypercalcaemia, phosphorus metabolism disease
- Thyroid disorders: hypothyroidism, myxoedema
- Other: nephrocalcinosis, pyoureter, hemoglobinopathy

These come from a knowledge graph and should be verified against the approved label.

**Drug interactions:** The interaction screen returned 100 interactions in total. Examples of those listed:
- Moderate: acarbose, rabeprazole, doxycycline, tetracycline, epinephrine, metformin, bupropion, acetylsalicylic acid, amphotericin B, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone), cholecalciferol, calcium phosphate
- Minor: albiglutide, atropine, hyoscyamine, glycopyrronium

Digoxin has a narrow therapeutic index, so interacting drugs and electrolyte changes (especially potassium and calcium) need careful attention.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials, the only linked publication is unrelated, and the known pharmacology (increased intracellular calcium) may even work against use in vasospastic angina. Evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible pharmacological rationale for vasospastic angina
- Review of the SAHPRA package insert for warnings and contraindications (currently unavailable and blocking safety screening)
- A targeted literature search for digoxin in coronary vasospasm, including any adverse-effect reports
- Preclinical or mechanistic studies before considering any clinical study
- Review of the other predicted indications, with the obsolete stroke term excluded or remapped
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

