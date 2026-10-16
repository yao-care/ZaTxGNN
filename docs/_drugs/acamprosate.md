---
layout: default
title: Acamprosate
parent: Model Prediction Only (L5)
nav_order: 12
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Acamprosate: predicted new indication Progressive encephalopathy with leukodystrophy due to DECR deficiency (evidence level L5). Approved use: Substance abuse/dependence"
---

# Acamprosate
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

# Acamprosate: From Substance Dependence to Progressive Encephalopathy with Leukodystrophy due to DECR Deficiency

## One-Sentence Summary

Acamprosate was originally used to treat substance (alcohol) dependence.
The TxGNN model predicts it may be effective for **progressive encephalopathy with leukodystrophy due to DECR deficiency**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
This is a graph-based prediction only, and the mechanistic link is not identifiable.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Substance abuse/dependence (the SAHPRA registration record has no indication text) |
| Predicted New Indication | Progressive encephalopathy with leukodystrophy due to DECR deficiency |
| TxGNN Prediction Score | 98.53% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Acamprosate is generally understood to act on glutamatergic and GABAergic neurotransmission, and its efficacy in alcohol dependence is established.

The predicted new indication is a different kind of disease. DECR deficiency is a mitochondrial fatty acid oxidation disorder, and acamprosate has no known action on that pathway. The high TxGNN score reflects a pattern in the knowledge graph, not a demonstrated biological or clinical connection. Without supporting trials or literature, this prediction should be treated as a computational signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other Predicted Indications With Supporting Evidence

The highest-ranked prediction has no evidence. Several lower-ranked predictions have some, and the strongest is alcohol withdrawal.

| Predicted Indication | TxGNN Score | Evidence Level | Supporting Evidence |
|------|------|------|------|
| Alcohol withdrawal | 90.61% | L2 | [NCT00106106](https://clinicaltrials.gov/study/NCT00106106): completed Phase 2 trial (n=56) of acamprosate for CNS hyperexcitability in alcohol withdrawal; results not provided in the compiled data. [NCT00466661](https://clinicaltrials.gov/study/NCT00466661): completed Phase 4 placebo-controlled trial (n=33) in alcohol-dependent patients with bipolar disorder. [PMID 11524307](https://pubmed.ncbi.nlm.nih.gov/11524307/): double-blind placebo-controlled study (n=296) in Spain, with acamprosate started during withdrawal. Guidelines and reviews mainly support its use for relapse prevention after detoxification, not as a primary withdrawal treatment. |
| Tourette syndrome | 92.57% | L5 | [NCT02217007](https://clinicaltrials.gov/study/NCT02217007): Phase 2a open-label trial, withdrawn with 0 enrolled, so no efficacy data. |
| Wernicke-Korsakoff syndrome | 98.07% | L4 | Only a general review on alcohol dependence management ([PMID 17716602](https://pubmed.ncbi.nlm.nih.gov/17716602/)); evidence is indirect. |
| Attention deficit-hyperactivity disorder | 91.85% | L4 | Only indirect reviews, with no acamprosate efficacy data for ADHD. |

The remaining predictions (trichotillomania, alcohol amnestic disorder, glaucoma, absence epilepsy, faciodigitogenital syndrome) have no trials or literature (L5).

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 32/9/0097 | Besobrial | Tablet (oral) | Not stated in the compiled registration record |

Acamprosate has one valid single-ingredient registration and no cancelled registrations.

---

## Safety Considerations

- **Contraindications (knowledge-graph derived, not label text)**: impaired renal function.
- **Drug Interactions**: 15 interacting drugs were identified, but the severity level of each is unclassified. They are pantoprazole, doxycycline, omeprazole, lansoprazole, prednisone, simvastatin, lactulose, naltrexone, ranitidine, bupropion, budesonide, warfarin, ibuprofen, doxepin and levothyroxine.

Please refer to the SAHPRA-approved Professional Information (PI) for the full warnings and contraindications, which were not available in the compiled data. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for DECR deficiency has no clinical or literature support and no plausible mechanistic link, so it rests on the model score alone (L5). Of the other predicted indications, alcohol withdrawal has the most support (L2) and is the most credible direction for further work.

**To proceed, the following is needed:**
- Mechanistic or preclinical evidence linking acamprosate to the DECR deficiency pathway, if this indication is to be pursued at all
- Consideration of alcohol withdrawal as the priority research question, including review of the NCT00106106 results
- The SAHPRA Professional Information (warnings, contraindications, approved indication text)
- Detailed mechanism of action data
- Severity classification of the identified drug interactions, particularly for warfarin and naltrexone
- Renal function considerations for any new patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

