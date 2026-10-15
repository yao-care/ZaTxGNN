---
layout: default
title: Duloxetine
parent: Model Prediction Only (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
---

# Duloxetine
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

# Duloxetine: From Major Depressive Disorder to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

Duloxetine is an antidepressant (a serotonin-norepinephrine reuptake inhibitor, SNRI) used for depression, anxiety disorders, fibromyalgia and related pain or urinary conditions.
The TxGNN model predicts it may be effective for **benign paroxysmal torticollis of infancy**, but **no clinical trials and no publications** currently support this direction. The score is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder (also anxiety disorder, fibromyalgia, myofascial pain syndrome, female stress incontinence) |
| Predicted New Indication | Benign paroxysmal torticollis of infancy |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

The original indications come from the TxGNN knowledge graph, because the SAHPRA records compiled for this report contain no approved indication text.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Duloxetine belongs to the SNRI class, and its efficacy in depression and anxiety is established. However, no mechanistic route to benign paroxysmal torticollis of infancy is evident.

This condition is an episodic disorder of infancy, often linked to variants in the *CACNA1A* calcium channel gene. It is unrelated to depression or pain in any established way, and no plausible duloxetine mechanism has been identified. The high TxGNN score most likely reflects network proximity in the knowledge graph rather than a specific biological rationale.

Safety in this age group is also a serious concern. Duloxetine carries a boxed warning for suicidality in young patients, and it has no established paediatric use in infants.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 50/1.2/0849 | Duloxetine Xr 30 Biotech | Capsule | Not stated in the records compiled |
| Reg. No. 54/1.2/0590 | Duloxetine Mr 60 Unicorn | Capsule | Not stated in the records compiled |

Both registrations are valid single-ingredient products, and none are cancelled. No Essential Medicines List (EML) information was available.

## Safety Considerations

- **Boxed warning (class warning):** Antidepressants carry a boxed warning for increased suicidality in children, adolescents and young adults. This is highly relevant to any infant or paediatric use.
- **Contraindications and risk conditions (knowledge graph, not label text):** The knowledge graph links duloxetine to these conditions:
  - Cardiovascular and autonomic: hypertension, orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy.
  - Neurological and psychiatric: epilepsy, bipolar disorder and major affective disorder, serotonin syndrome, neuroleptic malignant syndrome, substance abuse/dependence.
  - Liver and gallbladder: liver disease, cirrhosis, fatty liver disease, hepatitis, gallbladder disease.
  - Other: angle-closure glaucoma, blood coagulation disease, hyperglycaemia, syndrome of inappropriate ADH secretion (including nephrogenic).
- **Drug interactions:** 100 interactions were recorded. The **Major** ones in the data reviewed are:
  - bupropion
  - lorcaserin
  - diethylpropion
  - dolasetron
  - dexfenfluramine

  **Moderate** interactions include:
  - acetylsalicylic acid (bleeding risk)
  - morphine
  - epinephrine
  - cimetidine
  - dronabinol
  - diphenoxylate and difenoxin
  - the bowel-preparation products picosulfuric acid and polyethylene glycol

  Interactions with the acid-suppressant drugs famotidine, ranitidine, rabeprazole and dexlansoprazole, and with the antacids aluminium hydroxide and calcium carbonate, are Minor.

Label warnings and contraindications from the SAHPRA Professional Information (PI) were not retrieved. Please refer to the SAHPRA-approved PI for full safety information. Report adverse drug reactions to SAHPRA.

## Other Predicted Indications Worth Noting

The top-ranked prediction has no supporting evidence, but two lower-ranked predictions do:

| Predicted Indication | Evidence Level | Supporting Evidence |
|------|------|------|
| Obsessive-compulsive disorder | L2 | A double-blind augmentation trial in resistant OCD ([PMID 27811556](https://pubmed.ncbi.nlm.nih.gov/27811556/)), an open-label study ([PMID 25637377](https://pubmed.ncbi.nlm.nih.gov/25637377/)), and a small completed Phase 4 trial ([NCT00464698](https://clinicaltrials.gov/study/NCT00464698), n=20). All are small, and there is no Phase 3 RCT. |
| Agoraphobia | L3 | Open-label and small clinical reports in panic disorder ([PMID 19228176](https://pubmed.ncbi.nlm.nih.gov/19228176/), [PMID 24294001](https://pubmed.ncbi.nlm.nih.gov/24294001/)). Nothing is specific to agoraphobia. |

Both are classed as research questions. The remaining predictions (personality disorders, Ohdo syndrome and variants, ligneous conjunctivitis) have no trials or literature and no supported mechanism.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials, no literature and no plausible mechanism. The target population is infants, for whom duloxetine has no established use and a boxed suicidality warning applies.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) and a testable biological hypothesis linking duloxetine to the condition
- The SAHPRA Professional Information (PI) warnings and contraindications
- Any preclinical or case-level evidence in this condition
- A paediatric safety assessment before any further consideration
- Consider prioritising the OCD prediction (L2), which has the most supporting evidence among the predictions reviewed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

