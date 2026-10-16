---
layout: default
title: Chloroquine
parent: Model Prediction Only (L5)
nav_order: 114
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Chloroquine: predicted new indication Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis (evidence level L5). Approved use: Malaria, rheumatoid arthritis, systemic lupus erythemat…"
monitor_inn: "Chloroquine"
predicted_indications: ["rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "rheumatoid nodulosis", "juvenile chronic polyarthritis", "juvenile idiopathic arthritis", "osteoarthritis", "pseudoachondroplasia", "Quinquaud's folliculitis decalvans", "Smouldering systemic mastocytosis", "telogen effluvium", "alopecia antibody deficiency"]
---

# Chloroquine
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

# Chloroquine: From Rheumatoid Arthritis and Malaria to Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis

## One-Sentence Summary

Chloroquine is an established antimalarial and immunomodulatory drug, originally used for malaria, rheumatoid arthritis and lupus erythematosus.
The TxGNN model predicts it may be effective for **rheumatoid factor-positive polyarticular juvenile idiopathic arthritis (JIA)**,
but there are currently **no registered clinical trials** and only **1 publication** (a leflunomide cohort study that does not evaluate chloroquine) for this top-ranked prediction. The evidence is model-based only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malaria, rheumatoid arthritis, systemic lupus erythematosus (from the knowledge graph; the SAHPRA registration record contains no indication text) |
| Predicted New Indication | Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, chloroquine's immunomodulatory effects (lysosomal and autophagy inhibition, reduced antigen presentation, inhibition of Toll-like receptor signalling) are the likely basis of its benefit in rheumatoid arthritis and lupus.

RF-positive polyarticular JIA closely resembles adult seropositive rheumatoid arthritis, an established chloroquine indication. The high TxGNN score probably reflects this disease similarity. Antimalarials were also historically used as slow-acting antirheumatic agents in juvenile arthritis.

However, no direct clinical evidence for chloroquine in this specific condition was found. Modern practice favours methotrexate and biologic agents.

**Other predicted indications (for context):**

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Rheumatoid nodulosis | 99.33% | L5 | Case reports only; none evaluate chloroquine |
| 3 | Juvenile chronic polyarthritis | 99.32% | L4 | Old literature (1962-1991); includes a cardiac safety signal |
| 4 | Juvenile idiopathic arthritis | 99.22% | L4 | Historical use; no chloroquine-specific trial |
| 5 | Osteoarthritis | 98.66% | L3 | One completed Phase 4 trial (combination design); strongest direct evidence |
| 6-10 | Pseudoachondroplasia, folliculitis decalvans, smouldering systemic mastocytosis, telogen effluvium, alopecia antibody deficiency | 98.0-98.3% | L5 | Computational prediction only, no trials or literature |

Of these, osteoarthritis is the only candidate with a registered trial. Telogen effluvium is mechanistically implausible, since chloroquine has been reported to cause hair loss.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction (RF-positive polyarticular JIA).

For the fifth-ranked prediction, osteoarthritis, one trial is registered:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00805519](https://clinicaltrials.gov/study/NCT00805519) | Phase 4 | Completed | 230 | Prednisolone and chloroquine add-on to glucosamine plus chondroitin sulfate in knee osteoarthritis (2009-2010). The combination design means chloroquine's effect cannot be isolated, and outcome data were not available. |

No SANCTR or PACTR identifiers were found in the data compiled for this report.

---

## Literature Evidence

Literature for the top-ranked prediction (RF-positive polyarticular JIA):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24334641](https://pubmed.ncbi.nlm.nih.gov/24334641/) | 2014 | Cohort | J Rheumatol | Long-term real-life experience with leflunomide in JIA; does not evaluate chloroquine |

Selected literature for the closely related JIA predictions (ranks 3-4):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18021335](https://pubmed.ncbi.nlm.nih.gov/18021335/) | 2007 | Cohort | J Clin Pharm Ther | Pharmacokinetics of methotrexate alone vs methotrexate plus chloroquine in JIA |
| [2047820](https://pubmed.ncbi.nlm.nih.gov/2047820/) | 1991 | Review | Schweiz Med Wochenschr | Therapeutic strategy in 119 juvenile chronic arthritis patients; chloroquine discussed among disease-modifying drugs |
| [7409700](https://pubmed.ncbi.nlm.nih.gov/7409700/) | 1980 | Review | Fortschr Med | Benefits and adverse effects of gold, D-penicillamine, chloroquine and azathioprine in juvenile rheumatoid arthritis |
| [9523387](https://pubmed.ncbi.nlm.nih.gov/9523387/) | 1998 | Case report | Rev Rhum (Engl Ed) | Third-degree atrioventricular block in a patient on chloroquine (safety signal) |
| [1450810](https://pubmed.ncbi.nlm.nih.gov/1450810/) | 1992 | Case report | Br J Rheumatol | Chloroquine-induced vitiligo in a patient with juvenile-onset rheumatoid arthritis |

For osteoarthritis, a 2015 review of hydroxychloroquine and chloroquine in SLE, RA and related conditions including OA ([26246395](https://pubmed.ncbi.nlm.nih.gov/26246395/), *Inflammopharmacology*) is the most relevant. Most other OA papers are preclinical studies on autophagy and are not about chloroquine as a treatment.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Z/20.2.6/127 | Plasmoquine | Capsule (oral) | Not recorded in the data compiled for this report |

Chloroquine has one valid single-ingredient registration in South Africa. Essential Medicines List (EML) status was not available in the data compiled for this report.

---

## Safety Considerations

**Contraindication-related conditions (from knowledge graph associations, not label text):**
epilepsy, porphyria, liver disease, eye and retinal disease, vision disorders, hearing disorders, psoriasis, neutropenia, agranulocytosis, leukopenia, anaemia, G6PD deficiency, substance abuse/dependence, glycogen storage disease, cystinuria and galactosemia.

**Drug Interactions:** 100 interactions were identified. Examples of **Major** interactions:
- Agalsidase beta
- Bupropion
- Cisapride
- Clarithromycin
- Dolasetron
- Granisetron

Several QT-prolonging agents appear in this list. **Moderate** interactions include antacids (aluminium hydroxide, calcium carbonate, attapulgite), cimetidine, famotidine, metronidazole, loperamide, aprepitant, sulfonylureas (glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide) and insulin, where hypoglycaemia is a concern.

**Literature safety signals:** atrioventricular block (case report) and QTc prolongation, vitiligo.

For full warnings and contraindications, please refer to the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction rests on disease similarity to adult RA and has no supporting trials or chloroquine-specific literature (L5). Standard JIA treatment has moved to methotrexate and biologics, and chloroquine carries cardiac, retinal and haematological safety concerns, which are especially important in children. Among all ten predictions, osteoarthritis has the most evidence (L3, one Phase 4 trial), but it is a combination study and a research question rather than a decision-ready indication.

**To proceed, the following is needed:**
- Retrieval of the SAHPRA package insert to complete warnings, contraindications and approved indications (a blocking data gap)
- Mechanism of action data from DrugBank
- Published results of NCT00805519, with chloroquine's contribution separated from the combination
- Comparative evidence versus current JIA standards (methotrexate, biologics), including paediatric dosing and a retinal and cardiac (QTc) monitoring plan
- Verification of Essential Medicines List status and local clinical-trial registrations (SANCTR, PACTR)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

