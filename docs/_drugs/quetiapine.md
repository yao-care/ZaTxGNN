---
layout: default
title: Quetiapine
parent: Model Prediction Only (L5)
nav_order: 397
evidence_level: L5
indication_count: 10
---

# Quetiapine
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

# Quetiapine: From Bipolar Disorder and Schizophrenia to Trichotillomania

## One-Sentence Summary

Quetiapine is an atypical antipsychotic, originally used to treat bipolar disorder (including manic episodes, major affective disorder) and schizophrenia.
The highest-scoring TxGNN prediction (retinal dystrophy) has no supporting evidence. The best-supported prediction is **trichotillomania** (rank 8), with **0 registered clinical trials** and **6 publications**, mostly case reports and reviews.

*Note: The top-ranked prediction, retinal dystrophy with or without extraocular anomalies, has no trials or literature and no plausible mechanism. This report therefore focuses on trichotillomania, the only prediction among the top 10 with any supporting publications.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bipolar disorder, major affective disorder, manic bipolar affective disorder, schizophrenia (from the knowledge graph; SAHPRA indication text is not available) |
| Predicted New Indication | Trichotillomania (rank 8); the rank 1 prediction is retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.38% (trichotillomania); 99.57% (rank 1, retinal dystrophy) |
| Evidence Level | L4 (trichotillomania); L5 for the rank 1 prediction |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 |
| Recommended Decision | Hold (overall); trichotillomania is a research question only |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, quetiapine is an atypical antipsychotic that blocks dopamine D2 and serotonin 5-HT2A receptors, with additional histamine H1 and alpha-1 adrenergic blockade.

Trichotillomania (hair-pulling disorder) belongs to the obsessive-compulsive spectrum. Atypical antipsychotics with 5-HT2A and D2 antagonism are used as augmentation in OCD and related conditions, so a symptom-level link is plausible. The quetiapine-specific publications are small case reports or series, and one report describes quetiapine *worsening* obsessive-compulsive symptoms in a patient with trichotillomania, so the direction of effect is not consistent.

For the other top-ranked predictions (retinal dystrophy, congenital disorder of glycosylation, hydranencephaly, 17p13.3 microdeletion syndrome, polymicrogyria syndrome, X-linked myopias, Charcot-Marie-Tooth type 1G), no mechanistic link to quetiapine can be established. They are structural, chromosomal or inherited metabolic conditions, and the high scores are most likely knowledge-graph artefacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (for trichotillomania or any of the other top 10 predicted indications).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12405081](https://pubmed.ncbi.nlm.nih.gov/12405081/) | 2002 | Review / case report | Psychiatry | Overview of trichotillomania; a 33-year-old woman responded favourably to quetiapine |
| [19142421](https://pubmed.ncbi.nlm.nih.gov/19142421/) | 2008 | Case report/series | Rev Bras Psiquiatr | Quetiapine for the treatment of trichotillomania (no abstract available) |
| [11212595](https://pubmed.ncbi.nlm.nih.gov/11212595/) | 2001 | Case report / review | J Psychiatry Neurosci | Quetiapine exacerbated obsessive-compulsive symptoms in a patient with OCD, trichotillomania and bipolar features; review of antipsychotic-induced OCS |
| [38797877](https://pubmed.ncbi.nlm.nih.gov/38797877/) | 2025 | Review | Int J Dermatol | Pharmacological treatment of trichotillomania; no common treatment guidelines exist |
| [20833945](https://pubmed.ncbi.nlm.nih.gov/20833945/) | 2010 | Case report / review | Psychosomatics | Recurrent Rapunzel syndrome and trichotillomania; background on the disorder |
| [27840761](https://pubmed.ncbi.nlm.nih.gov/27840761/) | 2016 | Case report | Case Rep Psychiatry | Trichotillomania as a manifestation of dementia; not specific to quetiapine |

No randomised controlled trials were found.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 36/2.6.5/0070 | Seroquel | Tablet | Not available |
| Reg. No. 44/2.6.5/1085 | Truvalin Xr 150 | Tablet | Not available |
| Reg. No. 43/2.6.5/0429 | Dopaquel 25 | Film-coated tablet (Fct) | Not available |
| Reg. No. 45/2.6.5/0642 | Kizofrin | Tablet | Not available |
| Reg. No. 45/2.6.5/0212 | Quetiapine biotech | Tablet | Not available |

All five registrations are valid single-ingredient products, and none is cancelled. Essential Medicines List (EML) status was not available in the data compiled for this report.

---

## Safety Considerations

Label-based warnings and contraindications were not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Contraindication signals from the knowledge graph (not label text):** The knowledge graph links quetiapine to several conditions where caution may be needed. Examples include:
- **Cardiovascular:** long QT syndrome (including familial), torsades de pointes, orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy, hypertension, myocardial infarction
- **Metabolic:** diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, hyperlipidaemia, hypertriglyceridaemia, obesity, hypothyroidism, potassium deficiency
- **Haematological:** neutropenia, agranulocytosis
- **Neurological:** epilepsy, basal ganglia disease, dystonia, blepharospasm
- **Other:** liver disease, gallbladder disease, female breast carcinoma

**Drug interactions:** The interaction query returned 100 interactions in total; 20 are listed in the data compiled for this report. Two are rated **Major**:
- **Bupropion**
- **Morphine**

The rest are rated Moderate, including:
- **Antidiabetic agents** (metformin, pioglitazone, alogliptin, albiglutide, canagliflozin, acarbose, chlorpropamide), where glucose control may be affected
- **Anticholinergic agents** (atropine, hyoscyamine, glycopyrronium, clidinium)
- **Others**: epinephrine, famotidine, loperamide, aprepitant, dexamethasone, lorcaserin, bisacodyl

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The highest-scoring predictions have no trials, no literature and no plausible mechanism, so they should not be pursued.
- Trichotillomania has a plausible symptom-level rationale, but the evidence is limited to small case reports, with one report of worsening compulsive symptoms and no controlled data. It remains a research question rather than a candidate for clinical adoption.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking data gap for safety screening)
- Mechanism of action data from DrugBank
- A controlled study (or systematic review) of quetiapine in trichotillomania, compared against established options
- A risk–benefit assessment of quetiapine's metabolic, cardiac (QT) and sedative adverse effects in this population
- SAHPRA-approved indication text for the five registered products, and EML status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

