---
layout: default
title: Citric Acid
parent: 僅模型預測 (L5)
nav_order: 125
evidence_level: L5
indication_count: 10
---

# Citric Acid
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

# Citric Acid: From Food Additive & Diagnostic Adjunct to Stomach Disease

## One-Sentence Summary

Citric acid (DrugBank DB04272) has no formal approved pharmaceutical indication; it is widely recognised as a food additive (E330), a natural intermediate of the tricarboxylic acid (TCA) cycle, a standardised test-meal component for the ¹³C-urea breath test (*H. pylori* detection), and an anticoagulant agent (as citrate) in dialysis and catheter-lock solutions.
The TxGNN model predicts it may be therapeutically relevant for **Stomach Disease** based on its deep biochemical integration with the gastric environment, with **0 directly relevant clinical trials** and a small number of mechanistic and observational publications providing supporting context.
Overall, the evidence base for active therapeutic repurposing in stomach disease remains at **Level 4** (preclinical/mechanistic studies), and a **Hold** decision is recommended pending a clearly defined therapeutic hypothesis and further investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formal approved indication; known clinical roles include diagnostic adjunct (¹³C-UBT test meal), regional anticoagulant (as citrate, in dialysis and catheter-lock solutions), and food additive |
| Predicted New Indication | Stomach Disease |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for citric acid as a pharmaceutical agent is not available from this evidence pack. Based on known biochemical and clinical information, citric acid is a naturally occurring tricarboxylic acid that serves as both a food additive and a central intermediate of cellular energy metabolism. It is a natural component of human gastric juice — its gastric concentrations were quantified as early as 1967 — and this intrinsic presence in the gastric milieu provides the structural basis for the TxGNN model to associate it with stomach disease.

The most established clinical role of citric acid in stomach disease management is as a **standardised test-meal component** for the ¹³C-urea breath test (¹³C-UBT). By acidifying the intragastric environment, citric acid prevents *H. pylori* — which possesses urease activity — from relocating to non-antral, acid-protected regions of the stomach during the test. This improves the sensitivity and specificity of *H. pylori* detection, a critical step in managing *H. pylori*-related stomach diseases including gastritis, peptic ulcer disease, and gastric cancer prevention. A 2019 clinical study specifically investigated whether a citric acid meal enhances ¹³C-UBT accuracy in Asian populations, directly linking citric acid to the stomach disease diagnostic pathway.

From a metabolomics perspective, two additional mechanistic connections have been identified. First, elevated serum citric acid levels have been detected in Korean subjects **before** gastric cancer onset, suggesting a potential role as a pre-diagnostic metabolic biomarker and indicating that citric acid metabolism is perturbed in gastric carcinogenesis. Second, gastric cancer metabolomic research consistently identifies dysregulation of the TCA cycle — of which citric acid is a key node — as a defining feature of tumour subtypes with distinct clinical outcomes. Additionally, MX1, a compound combining a roxatidine metabolite with a bismuth-citrate complex (containing citric acid), demonstrated gastroprotective effects against stress-induced gastric ulcers in rat models. These converging lines of evidence explain the model's high prediction score, but it is important to recognise that they reflect a **physiological and diagnostic** role rather than an established pharmacological treatment effect.

---

## Clinical Trial Evidence

No clinical trials directly evaluate **citric acid as a therapeutic intervention** for stomach disease. Trials retrieved are testing other active agents for *H. pylori* eradication or stomach-adjacent conditions (Grade B relevance at the disease level only), or contain citrate as a salt/excipient component. The most contextually relevant trials are listed below:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT05196945](https://clinicaltrials.gov/study/NCT05196945) | Phase 4 | Unknown | 316 | Vonoprazan fumarate + Amoxicillin dual therapy vs. bismuth quadruple regimen for first-line *H. pylori* eradication; multicenter RCT in gastritis/peptic ulcer context. Citric acid not an active agent. |
| [NCT06760065](https://clinicaltrials.gov/study/NCT06760065) | Phase 3 | Not Yet Recruiting | 316 | Keverprazan + Amoxicillin dual therapy vs. susceptibility-guided quadruple therapy for rescue *H. pylori* eradication after prior failure; addresses antibiotic resistance challenge. Citric acid not an active agent. |
| [NCT03812380](https://clinicaltrials.gov/study/NCT03812380) | Phase 3 | Terminated | 62 | Effervescent Calcium Magnesium **Citrate** to avert PPI-associated complications (osteoporosis, hypomagnesaemia, CKD) in patients on long-term proton pump inhibitors for gastric conditions. Contains citrate component; terminated early. |
| [NCT03342456](https://clinicaltrials.gov/study/NCT03342456) | Phase 4 | Completed | 184 | Ilaprazole/Doxycycline-based bismuth quadruple therapy for *H. pylori*-infected duodenal ulcers; multicenter RCT addressing antibiotic resistance. Citric acid not an active agent. |
| [NCT03320538](https://clinicaltrials.gov/study/NCT03320538) | N/A | Completed | 360 | Jiangzhong Hou Gu® Mi Xi™ (TCM preparation) for peptic ulcer disease with spleen qi deficiency; double-blind RCT assessing symptom improvement. Not related to citric acid. |

> **Note:** Trials graded C (unrelated chemotherapy, orthopaedic, or other non-stomach indications) have been excluded from this table. None of the above trials test standalone citric acid as a treatment for stomach disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31505905](https://pubmed.ncbi.nlm.nih.gov/31505905/) | 2019 | Clinical Study | *Gut and Liver* | Directly evaluates whether a **citric acid test meal** improves accuracy of the ¹³C-UBT for *H. pylori* detection in Asian populations — the most clinically direct evidence of citric acid's role in stomach disease diagnostics |
| [35900644](https://pubmed.ncbi.nlm.nih.gov/35900644/) | 2022 | Cohort | *Metabolomics* | **High serum citric acid levels** (and L-carnitine), inversely correlated with alkaline phosphatase, detected in Korean subjects prior to gastric cancer onset; supports citric acid as a potential pre-diagnostic biomarker of gastric carcinogenesis risk |
| [6027230](https://pubmed.ncbi.nlm.nih.gov/6027230/) | 1967 | Observational | *Gastroenterology* | Foundational biochemical study quantifying **citric acid concentration in human gastric juice** alongside lactic, pyruvic, and uric acids; establishes citric acid as a natural constituent of the gastric environment |
| [9379358](https://pubmed.ncbi.nlm.nih.gov/9379358/) | 1997 | Preclinical | *J Pharmacy & Pharmacology* | **Gastroprotective effect of MX1** — a novel compound combining roxatidine's active metabolite with a bismuth-citrate (citric acid) complex — against restraint stress-induced gastric ulcers in rats; indirect evidence involving a citrate-containing compound |
| [38959111](https://pubmed.ncbi.nlm.nih.gov/38959111/) | 2024 | Molecular/Cohort | *Cell Reports* | Metabolic signature clustering of gastric cancer identifies **TCA cycle upregulation** (MSC1 subtype, with better prognosis) alongside TP53/RHOA mutations; contextualises citric acid's metabolic role in gastric tumour biology |
| [26088916](https://pubmed.ncbi.nlm.nih.gov/26088916/) | 2015 | Metabolomics | *Applied Biochemistry & Biotechnology* | LC/MS metabolomics analysis in gastric cancer identifies dysregulated metabolic pathways as biomarker candidates; TCA cycle intermediates including citric acid implicated in gastric cancer metabolic reprogramming |

---

## South Africa Market Information

Citric acid (DrugBank ID: DB04272) is **not currently registered with SAHPRA** as a standalone pharmaceutical product, and there are no approved medicinal products listed under this identity on the South African market.

> **Important context:** Citric acid is ubiquitous as an excipient and salt-forming agent in numerous registered pharmaceutical products available in South Africa (e.g., effervescent formulations, calcium citrate supplements, oral electrolyte solutions, anticoagulant blood collection tubes [3.2% sodium citrate]). It also holds GRAS (Generally Recognised As Safe) status as a food additive (E330). However, no standalone therapeutic registration exists under SAHPRA for any medicinal indication. Inclusion on the Essential Medicines List (EML) as a standalone therapeutic agent has not been identified.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for any registered products containing citric acid as an active or excipient component. Report adverse drug reactions to SAHPRA via the MedSafety reporting system.

> **General safety note:** At food-grade concentrations, citric acid is well-tolerated in the general population with an excellent safety profile. At higher pharmaceutical concentrations or via parenteral routes (e.g., intravenous regional citrate anticoagulation [RCA] in dialysis), careful monitoring of **serum ionised calcium** is essential, as citrate chelates calcium and can cause clinically significant **hypocalcaemia** if citrate elimination is impaired (e.g., in hepatic failure). Specific pharmaceutical-grade safety data for standalone oral or systemic citric acid use in stomach disease indications is not available from this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.74%) to citric acid for stomach disease, reflecting its deep physiological integration with the gastric environment as a natural juice component and TCA cycle intermediate. However, no clinical trials test citric acid as an active therapeutic agent for stomach disease, and the mechanistic evidence reflects a well-established **diagnostic and physiological** role rather than a pharmacological treatment effect. With evidence at Level 4, a Hold decision is appropriate until a credible therapeutic hypothesis and corresponding evidence are developed.

**To proceed, the following is needed:**
- **Define the therapeutic hypothesis**: Clearly distinguish whether the proposed repurposing targets citric acid as a *treatment* (e.g., bacteriostatic effect on *H. pylori* via intragastric pH reduction, mucosal cytoprotection) or an *enhanced diagnostic tool* (¹³C-UBT test meal — already in clinical practice and not requiring regulatory repurposing)
- **Safety consideration for acid-peptic disease**: Citric acid's intragastric acidification properties may be counter-therapeutic in acid-peptic disorders (e.g., gastritis, peptic ulcer disease, GORD) where *reducing* gastric acidity is the therapeutic goal; this pharmacological paradox must be addressed in any repurposing strategy
- **Systematic review**: Commission a systematic review of citric acid's gastric pharmacology, including any *in vitro* evidence for direct activity against *H. pylori* or gastric mucosal protection
- **MOA data retrieval**: Obtain detailed mechanism-of-action data from DrugBank API and published pharmacology literature (Data Gap DG002)
- **Regulatory consultation**: Given zero SAHPRA registrations and no original indication, any therapeutic repurposing would require a de novo registration pathway

---

> **Secondary Indication Alert — Higher Priority Finding:** Among all ten TxGNN-predicted indications for citric acid, **Thrombotic Disease (Rank 9)** presents the **strongest and most actionable evidence** (Evidence Level L3, Recommendation: **Proceed with Guardrails**). The CLiCK trial ([NCT04548713](https://clinicaltrials.gov/study/NCT04548713), N=1,449, Completed, Grade A) directly tested a KiteLock formulation containing citric acid as a central venous catheter lock solution for preventing catheter-related thrombosis and bloodstream infections in ICU patients. The mechanism is well-established — citrate chelates ionised calcium (Ca²⁺), interrupting the coagulation cascade — and is already routinely applied in regional citrate anticoagulation (RCA) for continuous renal replacement therapy (CRRT). A separate evaluation report specifically addressing the **Thrombotic Disease** indication is strongly recommended as the highest-priority repurposing candidate for citric acid.

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All content is subject to the YMYL disclaimer: results are for research reference only and should not be applied clinically without appropriate regulatory approval and clinical evidence.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

