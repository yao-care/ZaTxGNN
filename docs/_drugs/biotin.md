---
layout: default
title: Biotin
parent: Model Prediction Only (L5)
nav_order: 71
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Biotin: predicted new indication Dyspepsia (evidence level L5). Approved use: Nutritional biotin deficiency"
monitor_inn: "Biotin"
predicted_indications: ["dyspepsia", "gastroparesis (disease)", "mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "familial visceral myopathy", "anemia of prematurity", "congenital prothrombin deficiency", "cystinosis"]
---

# Biotin
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

# Biotin: From Nutritional Biotin Deficiency to Dyspepsia

## One-Sentence Summary

Biotin (vitamin B7) is a water-soluble vitamin used to treat and prevent nutritional biotin deficiency. The TxGNN model predicts it may be effective for **dyspepsia**, with a very high score. However, there are **no registered clinical trials** and **no publications that test biotin as a treatment for dyspepsia**, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Nutritional biotin deficiency (from the TxGNN knowledge graph; the SAHPRA registration records compiled for this report contain no indication text) |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Biotin is a cofactor for carboxylase enzymes involved in fatty acid, glucose and amino acid metabolism. Its efficacy in correcting biotin deficiency is well established.

**The link to dyspepsia is weak.** There is no direct, plausible mechanism connecting biotin to dyspepsia. The retrieved literature does not test biotin as a dyspepsia treatment. It covers:

- A case of biotin deficiency in an infant fed only an amino acid formula, who had been labelled with "dyspepsia" as a neonate.
- Enteroendocrine cell studies in irritable bowel syndrome.
- Gut microbiota and *H. pylori* gastritis.

Any plausible link would be indirect, for example through biotin production by the gut microbiome. This is a hypothesis, not demonstrated evidence. The high TxGNN score reflects patterns in the knowledge graph and should not be read as clinical support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for biotin in dyspepsia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Cohort | Int J Mol Med | Stomach antral endocrine cells in 76 IBS patients vs 43 healthy controls. Not about biotin. |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Cohort | World J Gastrointest Endosc | Endocrine cells in the stomach's oxyntic mucosa in IBS. Not about biotin. |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Cohort | J Clin Pathol | Interleukin-10 in *H. pylori* gastritis. Not about biotin. |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Cohort | Kidney Int | Small bowel T cells and stress proteins in IgA nephropathy. Not about biotin. |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Review | Eksp Klin Gastroenterol | A prebiotic and vitamin supplement (including biotin among many components) for gut microbiota disorders in patients with lung disease receiving antibiotics. Biotin's individual effect cannot be separated. |
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Case report | J Dermatol | A 5-month-old infant on amino acid formula developed biotin deficiency (hair loss, scaly dermatitis). Shows deficiency causing a problem, not biotin treating dyspepsia. |

None of these publications is a trial of biotin for dyspepsia.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| U/22.1.4/200 | Soluvit novum 10ml vials | Injection | Not stated in the data compiled |
| 36/22.1/0508 | Cernevit | Infusion | Not stated in the data compiled |
| L/24/329 | Dextrose 20% in water 500ml | Infusion | Not stated in the data compiled |
| Exclusion under Section 36 & Section 14 | ITN neonatal TPN 150ml | TPN | Not stated in the data compiled |

All 4 registrations are valid, and none is cancelled. All are parenteral products (injection, infusion, total parenteral nutrition). No oral biotin product appears in the data compiled, which matters because dyspepsia would usually be treated with an oral product. Essential Medicines List status is not available in the data.

---

## Safety Considerations

- **Contraindications flagged by the knowledge graph** (these are model-derived drug–disease associations, not label text): kidney disease, nephrolithiasis (including SLC26A1-related susceptibility), nephrocalcinosis, acute urate nephropathy, pyoureter, sarcoidosis, hyperparathyroidism, osteitis fibrosa, hypercalcaemia, phosphorus metabolism disease, constipation disorder and lytic metastatic bone lesion. Their clinical relevance for biotin should be verified against the approved Professional Information.
- **Laboratory interference:** high-dose biotin is known to interfere with many immunoassays (for example troponin and thyroid tests). Any use at higher doses would need clear communication to laboratories and clinicians.
- **Drug interactions:** no interaction records were found.

For full safety information, please refer to the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5). There are no clinical trials and no publications testing biotin in dyspepsia, and no plausible direct mechanism is evident. The registered South African products are all parenteral nutrition products, so there is also no obvious route-appropriate product for this use.

**Other predictions for biotin:**
Of the other predictions for biotin, **biotin metabolic disease** (TxGNN 92.14%) is better supported. It has six trials, including a completed Phase 2/3 randomised placebo-controlled trial of high-dose biotin, and a strong mechanistic rationale. However, those trials tested neurological diseases (ALS, adrenomyeloneuropathy) and glycaemic or microbiome outcomes, not inherited biotin metabolic disease itself. It could be considered for "Proceed with Guardrails", with laboratory-interference monitoring, but it was not the primary prediction evaluated here.

**To proceed with dyspepsia, the following is needed:**
- Detailed mechanism of action data and a mechanistic hypothesis linking biotin to dyspepsia.
- Retrieval of the SAHPRA package insert to obtain warnings and contraindications.
- Any clinical evidence (even small pilot studies) of biotin in dyspepsia or functional gastrointestinal disorders.
- Assessment of route and formulation, given that only parenteral products are registered.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

