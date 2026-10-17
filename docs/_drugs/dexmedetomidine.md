---
layout: default
title: Dexmedetomidine
parent: Model Prediction Only (L5)
nav_order: 170
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dexmedetomidine: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not stated in the SAHPRA data compiled for this report. Dexmedetomidi…"
monitor_inn: "Dexmedetomidine"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "migraine disorder", "migraine with brainstem aura", "headache disorder", "trigeminal autonomic cephalalgia", "pulmonary hypertension", "hypotrichosis simplex of the scalp", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "congenital hypotrichosis milia"]
---

# Dexmedetomidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Dexmedetomidine: From Sedation to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Dexmedetomidine is an alpha-2 adrenergic agonist injectable that is registered in South Africa (Precedex concentrated solution vial). The TxGNN model's top-ranked prediction is **nephrogenic syndrome of inappropriate antidiuresis**, but there are **no clinical trials and no publications** for it. The best-supported direction among the lower-ranked predictions is **headache disorder** (specifically post-dural puncture headache), with **4 clinical trials** and **7 publications**. This report covers the rank 1 prediction and then notes the better-supported alternatives.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA data compiled for this report. Dexmedetomidine is generally known as a sedative for ICU and procedural sedation in adults. |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Dexmedetomidine is a selective alpha-2 adrenergic agonist, and as such it could plausibly influence renal water handling and vasopressin signalling.

Nephrogenic syndrome of inappropriate antidiuresis is a very rare genetic disorder caused by gain-of-function variants of the vasopressin V2 receptor. Any link to dexmedetomidine is biologically speculative. The prediction comes from the knowledge graph alone, with no supporting trials or publications.

**Better-supported alternatives among the other predictions:**

| Predicted Indication | Score | Evidence Level | Supporting Data |
|------|------|------|------|
| Headache disorder (post-dural puncture headache) | 99.30% | L1 | One completed Phase 3 trial, 3 other trials, and a 2025 systematic review |
| Migraine disorder | 99.49% | L4 | One recruiting trial of nebulized dexmedetomidine (n=146), no results |
| Pulmonary hypertension | 98.40% | L3 | Mainly haemodynamic safety data during sedation, not disease-modifying evidence |
| Migraine with brainstem aura, trigeminal autonomic cephalalgia, hypotrichosis simplex of the scalp, atrophoderma vermiculata, congenital hypotrichosis milia | 98.2–99.4% | L5 | Graph-based only, with no trials or literature |
| Migraine with or without aura, susceptibility to | 98.27% | L4 | Indirect preclinical literature only |

For post-dural puncture headache, nebulized dexmedetomidine is proposed to act through alpha-2 mediated modulation of nociception and cerebral vasculature. The evidence is limited to this narrow secondary headache setting. It does not extend to headache disorders in general.

---

## Clinical Trial Evidence

For the rank 1 prediction (nephrogenic syndrome of inappropriate antidiuresis), currently no related clinical trials are registered.

For reference, the trials below relate to the best-supported alternative, headache disorder (post-dural puncture headache):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04910477](https://clinicaltrials.gov/study/NCT04910477) | Phase 3 | Completed | 90 | Nebulized dexmedetomidine vs neostigmine/atropine vs saline for post-dural puncture headache after caesarean section |
| [NCT04327726](https://clinicaltrials.gov/study/NCT04327726) | Not applicable | Completed | 43 | Randomized study of nebulized dexmedetomidine for post-dural puncture headache in parturients under spinal anaesthesia |
| [NCT06470854](https://clinicaltrials.gov/study/NCT06470854) | Not applicable | Completed | 50 | Non-randomized comparison of nebulized dexmedetomidine vs bilateral greater occipital nerve block for post-dural puncture headache |
| [NCT03513757](https://clinicaltrials.gov/study/NCT03513757) | Phase 4 | Completed | 40 | Propofol vs dexmedetomidine plus propofol sedation for paediatric MRI (only tangentially related to headache) |

Migraine: [NCT07769255](https://clinicaltrials.gov/study/NCT07769255) (not applicable, recruiting, n=146) is a randomized trial of nebulized dexmedetomidine on central sensitization in migraine. It has no results yet.

No SANCTR or PACTR identifiers were available in the data compiled for this report.

---

## Literature Evidence

For the rank 1 prediction, currently no related literature is available.

For reference, the most relevant publications for the headache disorder prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36651373](https://pubmed.ncbi.nlm.nih.gov/36651373/) | 2023 | RCT | Minerva Anestesiologica | Double-blind RCT comparing nebulized dexmedetomidine with neostigmine/atropine for post-dural puncture headache after caesarean section |
| [33993346](https://pubmed.ncbi.nlm.nih.gov/33993346/) | 2021 | RCT | Journal of Anesthesia | Nebulized dexmedetomidine added to conservative management of post-dural puncture headache, with cerebral haemodynamics assessed by trans-cranial Doppler |
| [41120897](https://pubmed.ncbi.nlm.nih.gov/41120897/) | 2025 | Systematic review | BMC Anesthesiology | Meta-analysis of the efficacy and safety of nebulized dexmedetomidine for post-dural puncture headache after caesarean delivery |
| [39799300](https://pubmed.ncbi.nlm.nih.gov/39799300/) | 2025 | Case report | BMC Anesthesiology | Two cases of nebulized dexmedetomidine for obstetric post-dural puncture headache |
| [31345663](https://pubmed.ncbi.nlm.nih.gov/31345663/) | 2019 | Editorial | Int J Obstet Anesth | Commentary on dexmedetomidine nebulization for post-dural puncture headache |

For pulmonary hypertension, relevant publications include a haemodynamic study in children with and without pulmonary hypertension ([23960035](https://pubmed.ncbi.nlm.nih.gov/23960035/), 2013) and a caution article ([24945133](https://pubmed.ncbi.nlm.nih.gov/24945133/), 2014). These address haemodynamic safety during sedation rather than disease modification.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 34/2.9/0239 | Precedex concentrated solution vial 2ml | Injection | Not stated in the data compiled for this report |

Essential Medicines List (EML) inclusion status is not stated in the data compiled for this report. The only registered route is injectable. Nebulized use, as studied in the headache trials, is not an approved route.

---

## Safety Considerations

**Contraindications flagged by the knowledge graph:** The TxGNN knowledge graph (not label text) lists these disease associations: hypertensive disorder, hypertension, kidney disease, pyoureter, liver disease, gallbladder disease, diabetes mellitus, diabetic ketoacidosis, hypotensive disorder and atrioventricular block. These should be verified against the SAHPRA-approved Professional Information (PI).

**Drug Interactions:** 59 interactions were identified in total. Those listed as Moderate include:
- Opioids and related drugs: morphine (including liposomal), opium, diphenoxylate
- Cannabinoids: dronabinol, nabilone
- Ethanol
- Vasodilators: amyl nitrite, diazoxide, phentolamine
- Papaverine and sibutramine

Several others (for example pantoprazole, lansoprazole, vancomycin, atropine, amphotericin B and famotidine) have an unclassified severity level.

**Other safety signals from the literature:** Haemodynamic effects, including systemic and pulmonary vasoconstriction after loading doses, are reported in children with pulmonary hypertension. Case reports describe asystole during infusion in two paediatric patients.

Please refer to the SAHPRA-approved Professional Information (PI) for the full warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rank 1 prediction rests on knowledge-graph similarity alone. There are no trials or publications, and the link to dexmedetomidine is biologically speculative for a very rare genetic disorder. The one direction with real clinical data (nebulized dexmedetomidine for post-dural puncture headache, L1) concerns an unregistered route and small, mostly single-centre trials. It is best treated as a research question rather than a registration-ready indication.

**To proceed, the following is needed:**
- SAHPRA package insert warnings, contraindications and approved indication text, which are blocking for safety screening
- Mechanism of action data
- For post-dural puncture headache: larger multicentre confirmatory trials, and a review of whether nebulized administration would need a new route or formulation registration
- For migraine: results from the ongoing trial NCT07769255
- For nephrogenic syndrome of inappropriate antidiuresis: preclinical evidence of any effect on V2 receptor signalling before further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

