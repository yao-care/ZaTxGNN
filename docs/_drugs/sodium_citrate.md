---
layout: default
title: Sodium Citrate
parent: Model Prediction Only (L5)
nav_order: 423
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Sodium Citrate: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Peptic ulcer disease, gastro-oesophageal reflux disease, oesophagitis…"
---

# Sodium Citrate
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

# Sodium Citrate: From Peptic Ulcer Disease and Reflux to Papillary Conjunctivitis

## One-Sentence Summary

Sodium citrate is a buffering and antacid agent, originally associated with peptic ulcer disease, gastro-oesophageal reflux disease and dyspepsia, and also found in cough and cold preparations.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, its top-ranked prediction.
There are **no clinical trials and no publications** for this prediction, so the signal is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, gastro-oesophageal reflux disease, oesophagitis, dyspepsia, pharyngitis, common cold, rhinitis (from the knowledge graph; no approved indication text is available in the SAHPRA records compiled for this report) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 14 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sodium citrate acts as an antacid and buffering agent. Its use in gastric acid-related conditions is plausible, and it appears in several cough and cold products.

No plausible mechanism links this buffering action to papillary conjunctivitis, which is usually driven by contact lens or foreign-body irritation and allergic mechanisms. The high score (99.95%, model rank 522) most likely reflects proximity in the knowledge graph rather than a biological rationale.

Other predictions in the list are also weakly supported:

- **Nasal cavity disease and acute laryngopharyngitis** sit close to the cold, rhinitis and pharyngitis indications. They are likely graph neighbours and have no trials or publications.
- **Stomach disease** (the only prediction with some biologically plausible mechanism, acid buffering) has only indirect literature, mostly preclinical gastric cancer work combining 3-bromopyruvate with sodium citrate.
- **Gastroduodenitis and intestinal obstruction** have only weak or off-topic literature.
- **Postgastrectomy syndrome, familial visceral myopathy, rosacea conjunctivitis and allergic urticaria** have no evidence and no supported mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered for papillary conjunctivitis. No trials were found for any of the other top-ranked predictions either.

## Literature Evidence

Currently no related literature available for papillary conjunctivitis.

For the best-supported alternative prediction (stomach disease), the retrieved literature is mostly indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1777551](https://pubmed.ncbi.nlm.nih.gov/1777551/) | 1991 | Clinical study | Aliment Pharmacol Ther | A glucose and sodium citrate formulation of azapropazone reduced gastric mucosal damage in rats, with a trend to less faecal blood loss in volunteers; therapeutic efficacy was unchanged |
| [25316860](https://pubmed.ncbi.nlm.nih.gov/25316860/) | 2014 | Community RCT | J Infect Dis | Buffer solution given to counter stomach acidity and improve the response to oral poliovirus vaccine in Bangladesh |
| [26708213](https://pubmed.ncbi.nlm.nih.gov/26708213/) | 2016 | Preclinical | Oncol Rep | 3-bromopyruvate plus sodium citrate inhibited glycolysis and induced apoptosis in gastric cancer cells and slowed orthotopic tumour growth |
| [27163639](https://pubmed.ncbi.nlm.nih.gov/27163639/) | 2016 | In vitro | Biochem Biophys Res Commun | The same combination induced apoptosis in a gastric cancer cell line |
| [29115645](https://pubmed.ncbi.nlm.nih.gov/29115645/) | 2018 | Animal xenograft | Oncol Rep | 18F-FDG PET/CT in a mouse gastric xenograft model used to assess glycolysis-targeted therapy |
| [7086102](https://pubmed.ncbi.nlm.nih.gov/7086102/) | 1982 | Clinical study | J Clin Gastroenterol | Most patients with active duodenal ulcers did not develop ulcer-type pain on gastroduodenal acidification |

These items do not demonstrate efficacy of sodium citrate for any predicted indication. Several other retrieved items were off-topic and are not listed.

## South Africa Market Information

All 14 registrations are valid single-ingredient entries. Approved indication text and manufacturer are not available in the data compiled for this report, and Essential Medicines List status was not available either. Most products are syrups, which suggests sodium citrate is mainly marketed as an ingredient in cough and cold preparations.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 43/2.6.5/0042 | Rispevon | Tablet | Not available |
| Y/2.8/306 | Paincodein | Tablet | Not available |
| G/10.1/1112 | Broncleer & cod unboxed | Syrup | Not available |
| G998 (OM) | Tussilinct cough | Syrup | Not available |
| G1053 (ACT 101 OF 1965) | Phenorant with codeine | Syrup | Not available |

The remaining nine registrations include further cough syrups (Tussitot cough, Alcophyllex, Diatussin, Actophlem, Coughcod senior and junior, Mucosolv expectorant), Astrapain forte tablets, and Sabax balanced ophthalmic salt solution.

## Safety Considerations

**Drug Interactions** (100 interactions were recorded; those shown are from the first 20 reviewed):

- **Major:** aluminium hydroxide.
- **Moderate:** doxycycline, minocycline, tetracycline, levofloxacin, iron, acetylsalicylic acid, rosuvastatin, acalabrutinib, ephedrine (including nasal) and pseudoephedrine.
- **Minor:** sulfonylureas (acetohexamide, chlorpropamide, glipizide, glyburide, tolazamide, tolbutamide), lactulose and misoprostol.

**Conditions flagged in the knowledge graph as contraindications** (not label text; confirm against the PI):

- Hypertension.
- Impaired renal function and anuria.
- Metabolic acidosis.
- Adrenal insufficiency, including Addison disease.
- Coronary artery disease and myocardial infarction.
- Angle-closure glaucoma and ocular hypertension.
- Benign prostatic hyperplasia.
- Pancreatitis.
- Hypercalcaemia and nephrocalcinosis.
- Rhabdomyolysis.

Several of these may reflect the other components of combination products (for example sympathomimetics) rather than sodium citrate itself.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for papillary conjunctivitis rests only on a graph-based score. There are no trials or publications, and no plausible mechanism. The evidence level is L5. Even the better-supported gastric predictions have only indirect or preclinical evidence (L4).

**To proceed, the following is needed:**
- Mechanism of action data for sodium citrate.
- SAHPRA package insert warnings and contraindications, which are currently missing and block safety screening.
- Approved indication text for each registration, to clarify which products are single-agent and which are combinations.
- A mechanistic rationale and preclinical or clinical evidence for the ocular indication, or a review of whether a gastric or upper airway indication would be a better-supported candidate.
- Assessment of route compatibility, since an ophthalmic indication would need an appropriate formulation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

