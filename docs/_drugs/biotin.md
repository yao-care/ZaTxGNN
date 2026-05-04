---
layout: default
title: Biotin
parent: 僅模型預測 (L5)
nav_order: 70
evidence_level: L5
indication_count: 10
---

# Biotin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Biotin: From Nutritional Supplement to Dyspepsia

## One-Sentence Summary

Biotin (Vitamin B7/H, DB00121) is a water-soluble B-vitamin that serves as an essential cofactor for five carboxylase enzymes and is used globally as a nutritional supplement and for the treatment of biotin deficiency states; it is currently **not registered with SAHPRA** and has no marketed products in South Africa.
The TxGNN model assigns its highest novel-indication score to **Dyspepsia** (99.43%), yet the available evidence consists of **no directly relevant clinical trials** and only **1 tangentially supportive publication**, placing this prediction at Evidence Level L4 with a **Hold** recommendation.
Healthcare professionals should note that two lower-ranked TxGNN predictions — **Biotin Metabolic Disease** (rank 8, L2 evidence) and **Vitamin Deficiency Disorder** (rank 7, L3 evidence) — carry substantially stronger evidence and both receive a "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No SAHPRA-registered indication (Biotin is used internationally as a nutritional supplement and for biotin deficiency; no approved indication text available) |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Biotin (Vitamin B7/H) is an essential water-soluble vitamin that functions as a covalently bound prosthetic group for five carboxylase enzymes: acetyl-CoA carboxylase 1 and 2 (fatty acid synthesis), pyruvate carboxylase (gluconeogenesis and TCA cycle anaplerosis), propionyl-CoA carboxylase, and methylcrotonyl-CoA carboxylase (branched-chain amino acid catabolism). These enzymes collectively regulate cellular energy metabolism, fatty acid homeostasis, and amino acid catabolism. Detailed mechanism of action data specific to gastrointestinal pathophysiology is not available in this Evidence Pack.

At a surface level, there is a biological association between biotin and the gastrointestinal tract: biotin deficiency can cause nausea, vomiting, and gastrointestinal distress, and PMID 25384804 reported observational benefit from a composite supplement containing B-group vitamins in functional dyspepsia patients following *Helicobacter pylori* eradication. However, that supplement contained multiple active ingredients (sodium alginate, calcium carbonate, pineapple, papaya, ginger, α-galactosidase, and fennel — product: Perdiges/Bioten), and any benefit cannot be isolated to biotin. No evidence exists to suggest biotin directly modulates gastric acid secretion, gastrointestinal motility, visceral hypersensitivity, or the other mechanisms implicated in dyspepsia.

The TxGNN high score likely reflects a broad knowledge-graph association between biotin and gastrointestinal symptoms rather than a specific therapeutic mechanism. **For context: two predictions within this same Evidence Pack carry far stronger mechanistic and clinical support** — Biotin Metabolic Disease (rank 8, evidence level L2; biotinidase and holocarboxylase synthetase deficiency are treated with high-dose biotin as standard of care) and Vitamin Deficiency Disorder (rank 7, evidence level L3; multiple completed RCTs and interventional studies directly support biotin supplementation). These are the clinically actionable repurposing candidates.

---

## Clinical Trial Evidence

Both trials retrieved for the dyspepsia query are classified as Grade C (not directly relevant):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT05389813](https://clinicaltrials.gov/study/NCT05389813) | Phase 2/3 | Unknown | 150 | Comparison of oxycodone vs pregabalin as pre-emptive analgesia for post-operative pain in elective surgical procedures (laparoscopic cholecystectomy, breast lumpectomy, etc.) at An-Najah National University Hospital. No connection to biotin or dyspepsia. |
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | Observational study of transdermal vitamin absorption in post-bariatric surgery patients comparing serum micronutrient concentrations with a transdermal patch. Biotin is one of many vitamins measured; the gastrointestinal context is the patient background, not a dyspepsia intervention. |

> Neither trial provides evidence for biotin as a treatment for dyspepsia. The absence of Grade A or B trials confirms the L4 evidence classification.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [25384804](https://pubmed.ncbi.nlm.nih.gov/25384804/) | 2014 | Interventional Observational | Minerva Gastroenterologica e Dietologica | Open multicentric study: composite supplement (alginate, calcium, pineapple, papaya, ginger, α-galactosidase, fennel — trade name Perdiges/Bioten) showed quality-of-life benefit in functional dyspepsia after H. pylori eradication. Biotin is a component of the product formulation but the effect cannot be attributed to biotin alone. |
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Case Report | The Journal of Dermatology | Biotin deficiency in a 5-month-old infant who had been diagnosed neonatally with dyspepsia and fed only amino acid formula; dyspepsia was the clinical context leading to biotin deficiency (low serum/urine biotin, normal zinc and biotinidase), not a treatment target. |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Review/Intervention | Experimental & Clinical Gastroenterology | Stimbifid supplement (inulin, oligofructose, vitamins C/B1/B6/B12/E/PP/folic acid/pantothenic acid/biotin, zinc, selenium) improved intestinal microbiota in patients with bronchopulmonary pathology receiving antibiotic therapy (n=50); biotin effect cannot be isolated from the complex formulation. |

> The remaining 4 retrieved publications (PMIDs 25110039, 24891930, 11304845, 10354275) concern irritable bowel syndrome endocrine cells, H. pylori gastritis cytokine localisation, and IgA nephropathy small bowel findings — none address biotin as a treatment for dyspepsia and are not included in the evidence table.

---

## South Africa Market Information

Biotin is **not currently registered with SAHPRA** and has no marketed pharmaceutical products in South Africa under this active ingredient. There are no SAHPRA-approved Product Information or Professional Information documents available through this data source.

Biotin may be commercially available in South Africa as an **unregistered nutritional supplement or as part of multivitamin formulations** regulated under the Complementary Medicines framework. Any clinical use should be guided by appropriate evidence-based guidelines. If formal therapeutic use is being considered, a SAHPRA registration pathway assessment would be required.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> **Important clinical note:** High-dose biotin supplementation (≥5 mg/day, and particularly at pharmacological doses of 100–300 mg/day as used in neurological conditions) can **interfere with immunoassay-based laboratory tests** that rely on the biotin–streptavidin interaction. This includes thyroid function tests (TSH, free T4, free T3), cardiac troponin, parathyroid hormone, vitamin D, and fertility hormone assays, potentially producing spuriously abnormal results in either direction. Patients should be instructed to withhold biotin supplementation for at least 24–72 hours before such tests. This is a recognised patient safety issue flagged by the US FDA (2017) and multiple pharmacovigilance authorities.

---

## Conclusion and Next Steps

**Decision: Hold** (for Dyspepsia — predicted_indications[0])

**Rationale:**
The evidence base for biotin in dyspepsia is effectively absent at the therapeutic level: both retrieved clinical trials are entirely unrelated to biotin or dyspepsia, and the sole potentially supportive publication (PMID 25384804) involves a multi-component supplement where biotin's individual contribution cannot be determined. There is no established mechanistic pathway linking biotin to the pathophysiology of dyspepsia.

---

**Summary of all ranked predictions for clinical prioritisation:**

| Rank | Indication | TxGNN Score | Evidence Level | Decision |
|------|------------|-------------|----------------|----------|
| 1 | Dyspepsia | 99.43% | L4 | **Hold** |
| 2 | Gastroparesis | 99.42% | L5 | Hold |
| 3 | Mitochondrial OXPHOS Disorder (nuclear DNA) | 96.14% | L5 | Research Question ✦ |
| 4 | Familial Visceral Myopathy | 95.05% | L5 | Hold |
| 5 | Anemia of Prematurity | 94.47% | L5 | Hold ⚠️ (data artefact) |
| 6 | Congenital Prothrombin Deficiency | 92.28% | L5 | Hold |
| **7** | **Vitamin Deficiency Disorder** | **92.25%** | **L3** | **Proceed with Guardrails ★** |
| **8** | **Biotin Metabolic Disease** | **92.14%** | **L2** | **Proceed with Guardrails ★** |
| 9 | Cystinosis | 91.97% | L5 | Hold |
| 10 | Contact Dermatitis (poison oak) — obsolete term | 91.54% | L5 | Hold |

> ⚠️ **Rank 5 (Anemia of Prematurity)**: All retrieved evidence uses biotin as a **red blood cell labelling tool** (biotin-labelled RBCs), not as a therapeutic agent. This is a data artefact — this indication should be excluded from any repurposing pipeline.
>
> ★ **Ranks 7 and 8** are the clinically actionable candidates and should be the focus of next-step evaluation.
>
> ✦ **Rank 3 (Mitochondrial OXPHOS Disorder)** has a mechanistically compelling hypothesis (biotin as cofactor for pyruvate carboxylase directly involved in TCA cycle anaplerosis and mitochondrial energy metabolism; PMID 26343941) and is suitable for formal research programme development.

---

**To proceed with the dyspepsia indication (should a clinical team wish to pursue it), the following is needed:**
- A preclinical mechanistic study demonstrating biotin's direct effect on gastric motility, acid secretion, or visceral hypersensitivity
- A well-designed prospective clinical trial specifically testing biotin monotherapy in functionally defined dyspepsia patients
- Resolution of the biotin MOA data gap (DrugBank API query recommended)
- SAHPRA registration pathway assessment for biotin as a medicinal product rather than a nutritional supplement

**For the higher-priority indications (Ranks 7 and 8), the recommended next steps are:**
- Convene a clinical advisory group to review the Phase 1/2 biotinidase deficiency trial data (NCT03269045, n=20, Completed) and the RCT evidence for biotin deficiency in end-stage renal disease (NCT02011191, n=49, Completed)
- Assess SAHPRA Named Patient Supply or Section 21 authorisation pathways for patients with confirmed biotinidase or holocarboxylase synthetase deficiency
- Establish a pharmacovigilance plan addressing high-dose biotin immunoassay interference as a priority safety monitoring item

---

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All findings should be interpreted in conjunction with SAHPRA-approved product information where available.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

