---
layout: default
title: Potassium Chloride
parent: Model Prediction Only (L5)
nav_order: 381
evidence_level: L5
indication_count: 1
---

# Potassium Chloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Potassium Chloride: From Potassium Deficiency to Renal Tubular Acidosis

## One-Sentence Summary

Potassium chloride is an electrolyte replacement originally used to treat potassium deficiency and constipation disorder.
The TxGNN model predicts it may be useful for **renal tubular acidosis (RTA)**, mainly as supportive treatment of the hypokalaemia that accompanies it.
There are **no registered clinical trials** and **18 publications** (mostly case reports and reviews) supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Potassium deficiency disease; constipation disorder (the SAHPRA registrations compiled for this report list no approved indication text) |
| Predicted New Indication | Renal tubular acidosis |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 (see note below) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 14 |
| Recommended Decision | Hold |

*Note on evidence level:* Under the standard rules, a prediction with no clinical trials and only case reports, reviews and small cohorts would be L5 (model prediction only). The L4 grade comes from the mechanistic rationale (potassium repletion for hypokalaemia in RTA), not from preclinical or mechanism studies.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Potassium is the main intracellular cation. Replacing it restores normal nerve, muscle and cardiac function when levels are low.

The link to renal tubular acidosis is supportive and symptomatic, not disease-modifying. In distal (type 1) RTA, the kidney cannot secrete hydrogen ions properly, which leads to urinary potassium wasting and hypokalaemia. Potassium chloride corrects this low potassium. Several case reports describe patients with RTA, often linked to Sjögren's syndrome, who presented with severe hypokalaemia and muscle paralysis and were treated with intravenous or oral potassium chloride.

The primary treatment for RTA remains alkali therapy (bicarbonate or citrate), and potassium is an adjunct. In type 4 (hyperkalaemic) RTA, potassium supplementation is hazardous and should be avoided. The high TxGNN score probably reflects this adjunctive relationship with the existing potassium deficiency indication, not a new therapeutic action.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the publications is an RCT. The table lists the most relevant ones, with reviews and cohorts first and then case reports.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [786013](https://pubmed.ncbi.nlm.nih.gov/786013/) | 1976 | Review | Am J Med Sci | Causes, consequences and correction of hypokalaemia |
| [6277192](https://pubmed.ncbi.nlm.nih.gov/6277192/) | 1982 | Review | Am J Med | Disorders of distal nephron function, including distal acidification defects |
| [38445406](https://pubmed.ncbi.nlm.nih.gov/38445406/) | 2023 | Cohort | La Tunisie Médicale | Genotype-phenotype study of distal RTA, a rare genetic disorder with hypokalaemia and nephrocalcinosis |
| [10213645](https://pubmed.ncbi.nlm.nih.gov/10213645/) | 1999 | Cohort | Am J Kidney Dis | Metabolic acidosis in advanced renal failure, diabetic vs non-diabetic patients (not specific to RTA or potassium) |
| [25447623](https://pubmed.ncbi.nlm.nih.gov/25447623/) | 2015 | Clinical study | Am J Med | Causes and treatment of hypokalaemic nonperiodic paralysis |
| [40288831](https://pubmed.ncbi.nlm.nih.gov/40288831/) | 2025 | Case report with review | Nefrologia | Primary RTA during pregnancy and perinatal outcomes |
| [34748193](https://pubmed.ncbi.nlm.nih.gov/34748193/) | 2022 | Case report | J Nephrol | Distal RTA with hypokalaemic periodic paralysis in pregnancy |
| [34595212](https://pubmed.ncbi.nlm.nih.gov/34595212/) | 2021 | Case report | Case Rep Nephrol Dial | Type 1 RTA with severe hypokalaemia (K 1.6 mEq/L) treated with potassium chloride infusion |
| [40654398](https://pubmed.ncbi.nlm.nih.gov/40654398/) | 2024 | Case report | JNMA | Sjögren's syndrome presenting with severe hypokalaemia and acidosis, treated with intravenous potassium chloride |

Other retrieved items are less relevant: a veterinary hyperkalaemia review, a literary-diagnosis article on "Tiny Tim", and several case reports of RTA with Sjögren's syndrome or pregnancy.

---

## South Africa Market Information

None of the 14 valid registrations has approved indication text in the data compiled for this report. All are single-ingredient products, and no information on Essential Medicines List (EML) inclusion is available. Five main registrations are shown below.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H1888 (ACT 101) | Urirex-k 50mg/300mg | Tablet | Not stated |
| E875 (ACT 101/1965) | Plasmalyte B 1000ml | Infusion | Not stated |
| F/24/271 | Maintelyte 10% 1000ml | Infusion | Not stated |
| 34/24/0371 | Euromed Lactated Ringer's Solution | Solution | Not stated |
| 36/34/0485 | Combibic Electrolyte Solution with Potassium | Infusion | Not stated |

The other nine registrations are mostly infusion or solution products (for example Ringer-lactate, cardioplegic solutions, a dialysis concentrate and a veterinary plasma product). Only one oral product (a tablet) appears. Oral formulations are therefore scarcely represented, although oral potassium is commonly used for chronic hypokalaemia.

---

## Safety Considerations

Detailed label warnings and contraindications from SAHPRA Professional Information (PI) were not available. Please refer to the SAHPRA-approved PI and report adverse drug reactions to SAHPRA.

- **Contraindications from knowledge graph (not label text):** Associations include kidney disease, anuria, hypertension, congestive heart failure, coronary artery disease, peptic ulcer disease, pancreatitis, liver disease, hypercalcaemia and nephrocalcinosis. Several are particularly relevant to RTA, where kidney function and nephrocalcinosis are common. Treat this list as a prompt for clinical review, not as confirmed label contraindications.
- **Hyperkalaemic RTA (type 4):** Potassium supplementation is hazardous and generally avoided.
- **Drug interactions:** The interaction screen returned 100 interacting drugs. The main ones are listed below.
  - *Major:* amiloride (potassium-sparing diuretic); ACE inhibitors and ARBs (benazepril, olmesartan, valsartan, azilsartan), which raise the risk of hyperkalaemia; anticholinergics and antihistamines (atropine, hyoscyamine, homatropine, glycopyrronium, benzatropine, biperiden, chlorpheniramine, brompheniramine, acrivastine, phenyltoloxamine); amitriptyline.
  - *Moderate:* NSAIDs (ibuprofen, ketorolac) and aliskiren.
  - *Minor:* cyanocobalamin.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible, but only as adjunctive correction of hypokalaemia in distal RTA, not as treatment of the underlying condition. No trials are registered, there are no RCTs, and the evidence is limited to case reports and reviews. Potassium repletion for hypokalaemia is already established practice. The main safety information is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications, to complete safety screening
- Mechanism of action data
- Clarification of the RTA subtype (type 1 and type 2 vs type 4) and clear exclusion criteria for hyperkalaemic patients
- Clinical guideline review to confirm the adjunct role of potassium alongside alkali therapy
- Serum potassium, renal function and ECG monitoring plans, including checks of interacting drugs such as ACE inhibitors, ARBs and potassium-sparing diuretics
- A review of oral potassium formulations available on the South African market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

