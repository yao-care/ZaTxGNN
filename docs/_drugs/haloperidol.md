---
layout: default
title: Haloperidol
parent: Model Prediction Only (L5)
nav_order: 251
evidence_level: L5
indication_count: 10
---

# Haloperidol
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

# Haloperidol: From Psychotic Disorders to Congenital Disorder of Glycosylation with Defective Fucosylation

## One-Sentence Summary

Haloperidol is an established antipsychotic, originally used for psychotic disorders, schizophrenia and Tourette syndrome.
The TxGNN model predicts it may be effective for **congenital disorder of glycosylation with defective fucosylation**, but there are currently **no clinical trials and no publications** supporting this prediction. It is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psychotic disorder, schizophrenia, schizoaffective disorder, Tourette syndrome (from the knowledge graph; the SAHPRA registrations do not state an approved indication text) |
| Predicted New Indication | Congenital disorder of glycosylation with defective fucosylation |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Haloperidol is a dopamine D2 receptor antagonist (a typical antipsychotic), and its efficacy in psychotic disorders is well established.

For this predicted indication, **no plausible mechanistic link could be identified**. Defective fucosylation is a disorder of glycosylation, typically linked to GDP-fucose transport (for example the SLC35C1 gene). Nothing in dopamine D2 blockade connects to that pathway. The high score (0.999) reflects a pattern in the knowledge graph, not biological or clinical support. Without trials, literature or a mechanistic rationale, this prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Q/2.6.5/170 | Haloperidol 5 oethmaan | Tablet (oral) | Not stated in the registration data |
| Q/2.6.5/169 | Haloperidol 1.5 oethmaan | Tablet (oral) | Not stated in the registration data |

Both registrations are single-ingredient products and currently valid. No registrations are cancelled. Only oral tablets are registered in the data compiled for this report.

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text):**
  - Cardiac: long QT syndrome (including familial), torsades de pointes
  - Neurological: epilepsy, basal ganglia disease, focal hand dystonia, blepharospasm, neuroleptic malignant syndrome
  - Haematological: neutropenia (including multiple congenital forms), agranulocytosis, leukopenia
  - Hepatic and biliary: liver disease, gallbladder disease
  - Endocrine and metabolic: hypothyroidism, myxedema, congenital hypothyroidism, potassium deficiency
  - Other: hypotensive disorder, female breast carcinoma
- **Drug Interactions:** 100 interactions are recorded. Major-level examples include **bupropion, morphine, clarithromycin and dolasetron**. Moderate-level examples include famotidine, epinephrine, hydrocortisone, amphotericin B, atropine, loperamide and aprepitant.

The SAHPRA package insert warnings and contraindications have not yet been reviewed. Please refer to the SAHPRA-approved Professional Information (PI) for authoritative safety information. Report adverse drug reactions to SAHPRA.

---

## Other Predicted Indications Worth Noting

The top-ranked prediction has no supporting evidence. Among the other predictions in the data compiled for this report, one has substantially more support:

| Predicted Indication | Evidence Level | Key Points | Decision |
|------|------|------|------|
| Manic bipolar affective disorder | L1 | A Phase 3, randomised, double-blind trial (NCT00129220, n=224, olanzapine with a haloperidol comparator arm) plus network meta-analyses of acute mania treatments. This is largely an extension within the psychiatric spectrum of haloperidol's original use. | Proceed with Guardrails |
| Retinal dystrophy | L4 | Two preclinical rat studies (PMID 31181134, 27788033) on retinal ganglion cell responses. They do not show benefit and may indicate a risk of altering visual function. | Hold |

The remaining predictions (including hydranencephaly, several myopia entries, Charcot-Marie-Tooth type 1G, and others) have no trials, no literature and no identified mechanistic link (L5, Hold).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based on model score alone. There are no clinical trials, no publications and no plausible mechanistic link between dopamine D2 antagonism and fucosylation defects. Safety data from the package insert are also still outstanding.

**To proceed, the following is needed:**
- A mechanistic rationale connecting haloperidol to the fucosylation or GDP-fucose pathway, ideally with preclinical data
- Detailed mechanism of action data (MOA)
- The SAHPRA package insert, with warnings and contraindications reviewed
- Any case reports, registry data or trials in congenital disorders of glycosylation
- If the goal is a near-term repurposing opportunity, a separate evaluation of the better-supported manic bipolar disorder prediction. This would need monitoring for extrapyramidal symptoms, QTc prolongation and sedation, interaction screening, and consideration of alternatives with a better tolerability profile.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

