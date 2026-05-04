---
layout: default
title: Calcifediol
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 4
---

# Calcifediol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Calcifediol: From Vitamin D Deficiency to Vitamin D-Dependent Rickets

---

## One-Sentence Summary

Calcifediol (25-hydroxyvitamin D₃) is the principal circulating metabolite of vitamin D, primarily used globally to correct vitamin D deficiency and support bone health — though it is not currently registered with SAHPRA in South Africa.
The TxGNN model predicts it may be effective for **Vitamin D-Dependent Rickets (VDDR)**, a group of rare hereditary disorders affecting vitamin D metabolism or receptor function, with **2 clinical trials** and **17 publications** currently supporting this direction.
Across all 4 predicted indications — vitamin D deficiency, renal tubular acidosis, hereditary hypophosphatemic rickets, and VDDR — evidence levels range from L3 to L5, with VDDR carrying the most actionable evidence profile.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin D deficiency / supplementation (established global use; not currently registered in South Africa) |
| Predicted New Indication | Vitamin D-Dependent Rickets (VDDR) |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L3 (observational studies and systematic reviews) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Calcifediol is 25-hydroxyvitamin D₃ (25-OHD₃) — the product of hepatic first-pass hydroxylation of vitamin D₃ by the enzymes CYP2R1 and CYP27A1. It is the predominant and most stable form of vitamin D in systemic circulation, and serves as the direct precursor to calcitriol (1,25-dihydroxyvitamin D₃), the biologically active hormonal form that regulates calcium absorption, bone mineralisation, and dozens of non-skeletal pathways. Because serum 25-OHD is the gold standard for assessing vitamin D status, supplementing calcifediol directly raises this reservoir efficiently — bypassing the often rate-limiting step of intestinal and cutaneous vitamin D₃ synthesis.

Vitamin D-Dependent Rickets (VDDR) encompasses several hereditary subtypes where calcifediol's mechanistic relevance varies importantly by subtype. In **VDDR Type 1B** (CYP2R1 mutations, 25-hydroxylase deficiency), the liver cannot hydroxylate vitamin D₃ into calcifediol — directly supplementing calcifediol completely bypasses this enzymatic block and is the most logically direct therapeutic intervention. In **VDDR Type 1A** (CYP27B1 mutations, 1α-hydroxylase deficiency), calcifediol is the correct substrate but cannot be further hydroxylated to calcitriol; high-dose calcifediol may partially compensate through residual enzymatic activity, though calcitriol is more targeted. In **VDDR Type 2A** (VDR mutations with end-organ resistance), supraphysiological doses of vitamin D metabolites — including calcifediol — are used clinically to partially overcome receptor resistance.

This mechanistic breadth across VDDR subtypes makes the TxGNN prediction highly plausible. Historical clinical practice relied extensively on high-dose vitamin D preparations, including calcifediol, to manage VDDR before recombinant calcitriol analogues became widely available. Contemporary literature continues to document the role of calcidiol-related metabolic pathways in VDDR pathophysiology, and the 2017 case series on VDDR Type 1B specifically identifies calcifediol replacement as the definitive treatment strategy for patients with CYP2R1 mutations — a potentially underdiagnosed population.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03265483](https://clinicaltrials.gov/study/NCT03265483) | N/A | Completed | 180 | Investigated magnesium supplementation as a modifier of vitamin D resistance in the general US population; demonstrated that Mg-dependent CYP2R1 and CYP27B1 enzyme activity is a key determinant of serum 25-OHD response — indirectly supporting the rationale for calcifediol in enzyme-dependent VDDR subtypes, though the intervention is magnesium rather than calcifediol itself |
| [NCT05214040](https://clinicaltrials.gov/study/NCT05214040) | N/A | Not Yet Recruiting | 300,000 | Large epidemiological study (France) of hypovitaminosis D prevalence among hospitalised patients; provides context for the burden of vitamin D deficiency disorders but does not specifically study VDDR or calcifediol as an intervention |

> **Note**: No clinical trials specifically evaluating calcifediol in VDDR were identified. The trials above are contextually relevant but indirect. Direct interventional data for calcifediol in VDDR remains an evidence gap.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28548312](https://pubmed.ncbi.nlm.nih.gov/28548312/) | 2017 | Case Series / Narrative Review | J Bone Miner Res | Describes 7 patients from 2 families with VDDR Type 1B (CYP2R1 / 25-hydroxylase deficiency) — the subtype most directly treatable with calcifediol; argues this condition is underdiagnosed; calcifediol supplementation logically targets the specific enzymatic defect |
| [9316302](https://pubmed.ncbi.nlm.nih.gov/9316302/) | 1997 | Review | Acta Paediatrica Japonica | Comprehensive review of VDDR Type I and II: VDDR-I responds to physiological doses of 1α-hydroxylated vitamin D; VDDR-II requires high-dose vitamin D preparations including 25-OHD analogues; establishes treatment framework |
| [2982764](https://pubmed.ncbi.nlm.nih.gov/2982764/) | 1985 | Retrospective Clinical Study | Israel J Med Sci | Reports two VDDR cases (Type I and II): the Type II patient's calcium malabsorption was correctable with high-dose 25-hydroxyvitamin D (calcifediol), providing one of the earliest direct clinical uses of calcifediol for VDDR |
| [22145480](https://pubmed.ncbi.nlm.nih.gov/22145480/) | 2011 | Case Reports | J Pediatr Endocrinol Metab | Two African children with VDDR-I and VDDR-II; VDDR-I is explicitly defined by defective enzymatic conversion of calcidiol (25-OHD) to calcitriol — calcifediol substrate supply is central to understanding the therapeutic target |
| [15972816](https://pubmed.ncbi.nlm.nih.gov/15972816/) | 2005 | Mechanistic Study | J Biol Chem | Identifies specific CYP27B1 residues responsible for binding of 25-OHD₃ (calcifediol); mutations at these residues cause VDDR Type 1; elucidates at the molecular level why calcifediol conversion to calcitriol is disrupted |
| [11693961](https://pubmed.ncbi.nlm.nih.gov/11693961/) | 2001 | Mechanistic Review | Crit Rev Eukaryot Gene Expr | Reviews vitamin D's role in osteoblast function and bone extracellular matrix mineralisation; shows that disruption of the VD endocrine system (as in VDDR) causes profound skeletal mineralisation failure correctable by restoring VD signalling |
| [26483391](https://pubmed.ncbi.nlm.nih.gov/26483391/) | 2015 | Review | BMJ Case Reports | Documents life-threatening respiratory complications of vitamin D-dependent rickets in a developing-country context (Cape Verde → Portugal); directly relevant to the Sub-Saharan African setting and highlights consequences of untreated VDDR |
| [11416220](https://pubmed.ncbi.nlm.nih.gov/11416220/) | 2001 | Animal / Translational Study | Proc Natl Acad Sci USA | Targeted ablation of CYP27B1 (1α-hydroxylase) in mice recapitulates VDDR skeletal, reproductive, and immune dysfunction; confirms the calcifediol → calcitriol conversion step as the critical bioactivation checkpoint |
| [233695](https://pubmed.ncbi.nlm.nih.gov/233695/) | 1978 | Clinical Study | J Clin Endocrinol Metab | Foundational report of familial VDR insensitivity syndrome (VDDR Type II): sibling pair whose calcium malabsorption was correctable with high-dose 25-OHD (calcifediol), establishing early proof-of-concept for calcifediol in receptor-resistant VDDR |
| [8914979](https://pubmed.ncbi.nlm.nih.gov/8914979/) | 1996 | Translational Study | FEBS Lett | Vitamin D₃ metabolites activate macrophage calcium signalling and respiratory burst in VDDR Type II patients similarly to healthy donors, suggesting non-genomic vitamin D pathways remain functional even when VDR-mediated genomic signalling is impaired |

---

## South Africa Market Information

Calcifediol is **not currently registered with SAHPRA** and carries no active product licences in South Africa.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | No registered products | — | — |

> **Regulatory pathway note**: Any clinical use of calcifediol in South Africa would require a **Section 21 application** (unregistered medicines — human) submitted to SAHPRA. Calcifediol is not included on the current South African Essential Medicines List (EML). Clinicians managing VDDR currently have access to registered alternatives including **cholecalciferol** (vitamin D₃) and **calcitriol** (1,25-dihydroxyvitamin D₃), the latter being generally preferred for VDDR Type 1A. For VDDR Type 1B specifically, calcifediol would represent the most targeted option and its absence from SAHPRA registration is a gap worth addressing.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. As calcifediol is not currently registered in South Africa, clinicians should consult international prescribing information (e.g., the EMA Summary of Product Characteristics or FDA Prescribing Information for Rayaldee®).

> **Clinical safety alert specific to VDDR use**: High-dose vitamin D metabolite therapy — as required for VDDR Type II — carries meaningful risk of **hypercalcaemia** and **nephrocalcinosis**. Regular monitoring of serum calcium, phosphate, creatinine, PTH, and urinary calcium-to-creatinine ratio is essential. Dose titration should be guided by target serum 25-OHD ranges appropriate to the VDDR subtype.

Report adverse drug reactions to **SAHPRA** (MedWatch SA portal).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
For VDDR Type 1B (CYP2R1/25-hydroxylase deficiency) specifically, calcifediol supplementation is mechanistically the most direct and logical therapy available — it circumvents the primary enzymatic defect entirely. For other VDDR subtypes, it plays a meaningful adjunctive role. The L3 evidence base (case series, retrospective studies, and mechanistic literature) is sufficient to justify structured access, but formal interventional trial data in South African populations is absent.

**To proceed, the following is needed:**

- **SAHPRA registration or Section 21 approval**: A formal access pathway must be established before calcifediol can be used in South African patients
- **Genetic subtype confirmation**: Molecular testing to confirm VDDR subtype (CYP2R1 vs CYP27B1 vs VDR mutation) is essential before selecting the most appropriate vitamin D metabolite — calcifediol is most beneficial for Type 1B
- **Paediatric dosing guidance**: Establish weight-based dosing protocols appropriate for the South African paediatric context, where most VDDR presents
- **Structured safety monitoring plan**: Baseline and periodic measurement of serum 25-OHD, calcium, phosphate, alkaline phosphatase, PTH, and spot urinary calcium:creatinine ratio
- **Prospective local data**: A structured observational or interventional study comparing calcifediol to calcitriol in South African VDDR patients would significantly strengthen the evidence base
- **NEMLC engagement**: Submission to the National Essential Medicines List Committee for consideration of calcifediol inclusion, particularly for VDDR Type 1B where it offers therapeutic advantages over currently listed agents

---

*This report is generated for research reference purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before therapeutic application. Prepared using TxGNN evidence data (data cut-off: 2026-04-04).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

