---
layout: default
title: Phenytoin
parent: Model Prediction Only (L5)
nav_order: 375
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
monitor_inn: "PHENYTOIN"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
description: "Phenytoin: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Phenytoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Phenytoin: Trigeminal nerve neoplasm
{: .text-alpha }

## One-Sentence Summary

Phenytoin is a long-established antiseizure medicine used for epilepsy, including generalised tonic-clonic seizures, partial seizures and status epilepticus.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but there are **0 registered clinical trials** and only **2 publications** for this prediction. Neither publication tests phenytoin as a treatment for a tumour, so the prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed (valid licences: 2 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Phenytoin is generally understood to work by blocking voltage-gated sodium channels, which stabilises overactive neurons. That explains its efficacy in epilepsy.

The link to a trigeminal nerve tumour is weak. Phenytoin has **no recognised anti-tumour mechanism**. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as *trigeminal neuralgia* and related neurological terms, not biological evidence that the drug shrinks or controls a tumour. At most, sodium channel blockade could ease nerve pain or seizures associated with a trigeminal lesion. That would be symptom control, not treatment of the neoplasm.

The two retrieved publications support this reading. One is a review of trigeminal neuralgia treatments, and the other is a case series on Sturge-Weber syndrome. Neither addresses neoplasm treatment.

Trigeminal neuralgia (a pain condition, not a tumour) appeared further down the same prediction list. It has more substantial literature, including guidelines, reviews and retrospective data on intravenous phenytoin in acute exacerbations. It is a more credible adjacent question than the neoplasm prediction. Even there, phenytoin is generally a second-line or historical option behind carbamazepine and oxcarbazepine.

---

## Clinical Trial Evidence

Currently no related clinical trials registered. No ClinicalTrials.gov, SANCTR or PACTR entries were identified for this prediction.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Overview of medical and surgical treatments for trigeminal neuralgia. It concerns a pain syndrome, not a tumour. |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | An Esp Pediatr | Experience with 14 cases of Sturge-Weber syndrome (clinical features, course and treatment response). It does not evaluate phenytoin for neoplasm. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| B0884 (ACT 101) | Phenytoin sod | Tablet | Not stated in the registration data compiled |
| B1624 (OLD MEDICNE) | Epanutin Ready Mixed Parenteral | Injection | Not stated in the registration data compiled |

Both registrations are valid single-ingredient products, and none are cancelled. Oral (tablet) and injectable forms are both available.

---

## Safety Considerations

SAHPRA package insert warnings and contraindications were not available for this report. Please refer to the SAHPRA-approved Professional Information (PI) for the authoritative safety information. Report adverse drug reactions to SAHPRA.

**Knowledge-graph contraindication signals** (these come from drug-disease links in the knowledge graph, not from label text, and should be verified against the PI):
- Cardiac: long QT syndrome (including familial), torsades de pointes, hypotensive disorder
- Hepatic: liver failure, liver disease, gallbladder disease, hepatic coma and encephalopathy
- Renal: kidney disease
- Metabolic: diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, inherited porphyria and related porphyrin metabolism disorders
- Haematological: thrombocytopenia, neutropenia, agranulocytosis
- Immunological: systemic lupus erythematosus (including paediatric)
- Respiratory/sleep: obstructive sleep apnoea, congenital central hypoventilation syndrome
- Psychiatric: anxiety disorder, neurotic disorder, dysthymic disorder, substance abuse/dependence

**Drug interactions:** The interaction screen returned 100 interacting drugs in total. Of the first 20 listed, 19 were rated Moderate and 1 Minor (acetylsalicylic acid). The Moderate-level examples included:
- Antidiabetics: acarbose, metformin, pioglitazone, alogliptin, albiglutide
- Acid suppressants: omeprazole, famotidine, ranitidine
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone
- Antimicrobials: doxycycline, metronidazole
- Others: bupropion, aprepitant, morphine, cholecalciferol, calcifediol

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction has no registered trials, no literature on phenytoin treating a tumour, and no recognised anti-tumour mechanism. The high score most likely reflects the model's proximity to trigeminal neuralgia. Phenytoin remains well established and marketed in South Africa for its approved seizure indications.

**To proceed, the following is needed:**
- Mechanism of action data to test whether any plausible anti-tumour or tumour-related symptom-control rationale exists
- Preclinical evidence of anti-tumour activity in trigeminal nerve tumour models
- Review of the SAHPRA-approved PI, since label warnings and contraindications were not available for this report
- A clearer clinical question. Redirecting the work towards trigeminal neuralgia or symptom control in patients with trigeminal lesions would be better supported than a neoplasm indication, and would need its own evidence review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

