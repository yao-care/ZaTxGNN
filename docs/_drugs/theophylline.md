---
layout: default
title: Theophylline
parent: Model Prediction Only (L5)
nav_order: 444
evidence_level: L5
indication_count: 6
monitor_inn: "THEOPHYLLINE"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
last_modified_at: 2026-10-29
description: "Theophylline: predicted new indication Thrombotic disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Theophylline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Theophylline: Thrombotic disease
{: .text-alpha }

## One-Sentence Summary

Theophylline is a bronchodilator whose knowledge-graph-recorded uses are asthma, bronchitis, emphysema and related airway diseases.
The TxGNN model predicts it may be useful for **thrombotic disease**, but there are **0 registered clinical trials** and **no publication that directly tests theophylline in thrombosis**. This prediction rests on the computational score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 8 of 8) |
| Number of SAHPRA Registrations | 8 (valid: 8) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Theophylline is generally known as a non-selective phosphodiesterase (PDE) inhibitor and adenosine receptor antagonist.

In theory, PDE inhibition raises cyclic AMP (cAMP) in platelets, which could reduce platelet aggregation. This gives a weak mechanistic rationale for thrombosis. However, adenosine antagonism may work against the antiplatelet effect of adenosine, so the net effect is uncertain.

The retrieved literature does not test theophylline in thrombosis. Most items concern platelet biology, blood sampling methods or other drugs (such as ticlopidine and milrinone). The high TxGNN score is a computational prediction only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the retrieved publications directly studies theophylline for thrombotic disease. The items below are the most relevant indirect ones.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clin Pharmacokinet | Pharmacokinetics of ticlopidine, an antiplatelet drug; not about theophylline |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Crit Rev Biochem | Prostaglandins, platelets and atherosclerosis; prostacyclin raises platelet cAMP |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Other | Gen Pharmacol | Milrinone, a PDE inhibitor, reduces platelet aggregation via cAMP and interacts with adenosine |
| [4776567](https://pubmed.ncbi.nlm.nih.gov/4776567/) | 1973 | Other | Minerva Cardioangiol | Theophylline nicotinate derivative in chronic obliterating peripheral arteriopathy (no abstract) |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Other | Br J Haematol | Theophylline used only as an anticoagulant additive in a platelet factor 4 assay |

---

## South Africa Market Information

Approved indication text is not available in the local licence records. All 8 registrations are single-ingredient products with valid status. The data compiled for this report does not state Essential Medicines List (EML) status.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G721 (OM) | Alcophyllin | Syrup | Not stated |
| S/10.2/126 | Nuelin liquid | Syrup | Not stated |
| M/10.2/0533 | Theophen | Syrup | Not stated |
| G892 (OM) | Adco-Metaxol | Suspension | Not stated |
| N/10.1/98 | Theophen Compound Elixir | Syrup | Not stated |

Three further valid registrations are not shown: Alcophyllex (G720 (OM)), Diatussin (biotussin) (G1276 (OM)) and Actophlem (W/10.1/0194).

---

## Safety Considerations

- **Contraindication-type relations recorded in the knowledge graph (not label text)**: hypertension, liver failure and liver disease, epilepsy, anxiety and other mental disorders, porphyria, kidney disease, hypothyroidism, peptic ulcer disease, open-angle glaucoma, psychotic disorders, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, thrombocytopenia, neutropenia and agranulocytosis, among others.
- **Drug Interactions** (100 interactions recorded; examples shown):
  - **Major**: bupropion.
  - **Moderate**: H2 blockers and proton pump inhibitors (famotidine, ranitidine, cimetidine, omeprazole, rabeprazole), macrolides (clarithromycin), tetracyclines (doxycycline, minocycline, tetracycline), corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), activated charcoal and some bowel preparations.
  - **Minor**: ephedrine.
- Theophylline has a narrow therapeutic window, and its blood levels are affected by many interacting drugs.

Please refer to the SAHPRA-approved Professional Information (PI) for official warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a computational score. There are no trials, no literature directly studying theophylline in thrombotic disease, and the mechanism is conflicting (PDE inhibition versus adenosine antagonism). The safety data, including many drug interactions and a narrow therapeutic window, call for caution.

**To proceed, the following is needed:**
- Preclinical or clinical data on theophylline's effect on platelet function or thrombosis
- Mechanism of action data and a clearer analysis of the net antiplatelet effect
- SAHPRA Professional Information warnings and contraindications
- Review of safety in patients with thrombosis, who often take interacting drugs

---

## Other Predicted Indications (Brief Note)

For context, the other predictions in the data compiled for this report are:
- **Nasal cavity disease** (score 0.9953): one small clinical study of slow-release theophylline on nasal allergen challenge in allergic rhinitis (PMID 9648963). The design could not be confirmed, so this is a research question only.
- **Tracheal disease** (0.9949): in vitro tracheal relaxation data, a retrospective veterinary series in dogs, and reviews of methylxanthines for preterm extubation. No human trials in tracheal disease.
- **Laryngotracheitis, pharyngitis and acute laryngopharyngitis** (0.9951, 0.9946 and 0.9935): computational predictions only, with no supporting clinical evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

