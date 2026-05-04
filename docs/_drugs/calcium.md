---
layout: default
title: Calcium
parent: 僅模型預測 (L5)
nav_order: 87
evidence_level: L5
indication_count: 10
---

# Calcium
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

# Calcium: From Electrolyte Supplementation to Thrombotic Disease

## One-Sentence Summary

Calcium (DrugBank ID: DB01373) is an essential mineral and electrolyte supplement used globally to correct hypocalcaemia, support bone mineralisation, and facilitate cardiac resuscitation in emergency settings.
The TxGNN model predicts it may have therapeutic relevance for **Thrombotic Disease** with a prediction score of **98.25%**,
supported by **40 clinical trial registrations** and **20 publications** — though critically, no study has directly tested calcium supplementation as a primary intervention specifically targeting thrombotic disease, and the mechanistic direction of the prediction remains ambiguous.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypocalcaemia / electrolyte supplementation (no SAHPRA-registered products identified) |
| Predicted New Indication | Thrombotic Disease |
| TxGNN Prediction Score | 98.25% |
| Evidence Level | L4 (Mechanistic and preclinical evidence only; no direct RCTs) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence package. Based on established physiology, calcium (Ca²⁺) plays a central role in haemostasis as **Coagulation Factor IV** — the only inorganic cofactor in the coagulation cascade. It is an obligate participant in the assembly of both the tenase complex (Factors VIIIa/IXa) and the prothrombinase complex (Factors Va/Xa) on activated platelet phospholipid surfaces, and is essential for prothrombin-to-thrombin conversion. Beyond coagulation factor activation, intracellular Ca²⁺ signalling drives platelet activation by mediating GPIIb/IIIa integrin conformational change, thromboxane A₂ synthesis, and dense granule exocytosis. A 2023 in vitro study (PMID 36453103) specifically demonstrated that plasma from patients with immune-mediated thrombotic thrombocytopenic purpura (iTTP) induces **calcium- and IgG-dependent** endothelial cell activation, directly implicating aberrant Ca²⁺ signalling as a trigger in a severe thrombotic microangiopathy. Calcium also serves as an obligate cofactor in the Protein C anticoagulant pathway: thrombomodulin-mediated activation of Protein C at the endothelial surface requires Ca²⁺, establishing calcium's role in both pro- and anticoagulant regulation (PMID 6099583).

The pathophysiological relationship between calcium and thrombotic disease is, however, bidirectional and clinically complex. The TxGNN prediction does not specify a therapeutic direction — it cannot distinguish between calcium as a target to *supplement*, *modulate*, or *inhibit* in the context of thrombosis. **Critically, hypercalcaemia is itself a recognised prothrombotic state**, and epidemiological data suggest that excessive calcium supplementation may increase cardiovascular risk in certain populations. The retrieved clinical trials involve predominantly other pharmacological agents (statins, anticoagulants) or employ nadroparin **calcium** as a low molecular weight heparin salt in which calcium functions only as an inert counterion. The 20 retrieved publications are predominantly mechanistic studies examining calcium signalling in platelets and endothelial cells — providing biological plausibility for calcium's involvement in thrombosis, but offering no directional evidence that calcium supplementation would reduce thrombotic risk.

---

## Clinical Trial Evidence

> **Important note:** No clinical trials were identified that directly test calcium supplementation (e.g., calcium chloride, calcium gluconate) as a primary intervention for thrombotic disease. Trials are presented for contextual relevance. Trials labelled "nadroparin calcium" refer to a low molecular weight heparin salt in which calcium is the pharmacologically inert counterion, not the active agent.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00951574](https://clinicaltrials.gov/study/NCT00951574) | Phase 3 | Completed | 1,166 | Nadroparin calcium (LMWH, one subcutaneous injection/day) vs placebo for VTE prevention in patients with lung, breast, GI, ovarian, or H&N cancer on chemotherapy for up to 4 months; calcium here is the salt counterion only |
| [NCT00421538](https://clinicaltrials.gov/study/NCT00421538) | Phase 3 | Completed | 260 | CACTUS-PTS: therapeutic-dose nadroparin vs placebo for 6 weeks in first symptomatic isolated distal (calf) DVT; primary endpoints were proximal DVT and symptomatic PE rates at 6 weeks |
| [NCT04173429](https://clinicaltrials.gov/study/NCT04173429) | Phase 4 | Completed | 64 | Nadroparin calcium–warfarin sequential anticoagulation in cirrhotic patients with portal vein thrombosis; evaluated recanalization rate, rebleeding incidence, and safety |
| [NCT05621915](https://clinicaltrials.gov/study/NCT05621915) | Observational | Completed | 43 | Prospective pharmacokinetic study of nadroparin calcium across COVID-19 severity stages; developed LMWH dosing model for critically ill patients with high thrombotic risk |
| [NCT01528800](https://clinicaltrials.gov/study/NCT01528800) | Phase 2 | Completed | 85 | iPACK-HD: Vitamin K supplementation three times weekly to reduce coronary artery **calcification** progression in dialysis patients over 12 months vs placebo; calcium deposition measured as primary endpoint — indirectly relevant to calcium metabolism |
| [NCT07164300](https://clinicaltrials.gov/study/NCT07164300) | N/A | Recruiting | 150 | Comparative tranexamic acid dosage regimens in cardiac surgery with cardiopulmonary bypass; intravenous calcium is routinely administered during bypass circuits but is not the study intervention |
| [NCT01153243](https://clinicaltrials.gov/study/NCT01153243) | Phase 4 | Unknown | 117 | Vitamin D supplementation in African Americans with hypovitaminosis D and Type 2 DM; evaluates effect on thrombotic markers including high-sensitivity CRP — calcium–vitamin D metabolic axis studied indirectly |
| [NCT00732576](https://clinicaltrials.gov/study/NCT00732576) | N/A | Completed | 57 | Omega-3 fatty acids combined with menaquinone-7 (Vitamin K2) on thrombotic tendency; investigates interaction between vascular calcification prevention and platelet-mediated thrombosis — calcium-vascular calcification axis |
| [NCT04319627](https://clinicaltrials.gov/study/NCT04319627) | Phase 3 | Recruiting | 2,700 | SAVER: rosuvastatin vs placebo to prevent recurrent VTE in patients with DVT or PE; large ongoing Phase 3 trial illustrating the current therapeutic landscape — no calcium intervention |
| [NCT04833764](https://clinicaltrials.gov/study/NCT04833764) | Phase 1/2 | Unknown | 30 | Adjunctive rosuvastatin with standard Factor Xa inhibitor anticoagulation for lower extremity DVT; evaluates prevention of post-thrombotic syndrome — no direct calcium involvement |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39796525](https://pubmed.ncbi.nlm.nih.gov/39796525/) | 2024 | Review | Nutrients | Vitamin D deficiency and thrombotic disease risk; VD regulates calcium and phosphate metabolism; VD deficiency linked to heightened thrombosis risk through modulation of coagulation factor expression, platelet reactivity, and endothelial function |
| [36453103](https://pubmed.ncbi.nlm.nih.gov/36453103/) | 2023 | Mechanistic/In vitro | Haematologica | iTTP patient plasma induces **calcium- and IgG-dependent** endothelial cell activation; prospective study of 25 patients during acute iTTP identifies Ca²⁺-mediated endothelial response as a disease trigger in thrombotic microangiopathy |
| [38880165](https://pubmed.ncbi.nlm.nih.gov/38880165/) | 2024 | Review/Mechanistic | Life Sciences | Altered Ca²⁺ flux dynamics and mitochondrial metabolism in platelet activation–related disease and ageing; Ca²⁺-dependent procoagulant phenotype formation highlighted as a potential therapeutic target in atherothrombosis |
| [37563135](https://pubmed.ncbi.nlm.nih.gov/37563135/) | 2023 | Mechanistic/Animal | Nature Communications | MTH1 (nucleotide pool enzyme) regulates platelet mitochondria under oxidative stress; MTH1 deficiency impairs thrombin-induced Ca²⁺ mobilisation and reduces arterial/venous thrombus formation in vivo — demonstrates Ca²⁺ signalling as a key effector in thrombosis |
| [26972052](https://pubmed.ncbi.nlm.nih.gov/26972052/) | 2016 | Mechanistic/Animal | Cell | Gut microbial metabolite TMAO enhances platelet hyperreactivity and thrombosis risk through Ca²⁺ release pathways; predicts incident thrombosis at 3 years in >4,000 subjects, linking microbiome to Ca²⁺-dependent platelet activation |
| [22283597](https://pubmed.ncbi.nlm.nih.gov/22283597/) | 2012 | Review | Am J Cardiovasc Drugs | Calcium intake and CVD risk; laboratory studies show calcium may affect thrombotic mechanisms via vasodilation, inflammatory mediator modulation, and coagulation; epidemiological and RCT evidence remains inconclusive and shows potential for harm with excess supplementation |
| [35165707](https://pubmed.ncbi.nlm.nih.gov/35165707/) | 2022 | Translational | European Heart Journal | Galectin-3 activates platelets via Dectin-1 receptor and downstream Ca²⁺ mobilisation; translational study in cardiovascular disease demonstrates Ca²⁺ as an obligate effector of platelet aggregation and arterial thrombus formation |
| [31192861](https://pubmed.ncbi.nlm.nih.gov/31192861/) | 2019 | Cohort/Pathological | Am J Surgical Pathology | Vascular **calcium deposition and thrombosis** are hallmarks of calciphylaxis; fine vessel-wall calcium deposits (von Kossa stain) highly specific for calciphylaxis-associated thrombotic vasculopathy compared to other vascular diseases |
| [6099583](https://pubmed.ncbi.nlm.nih.gov/6099583/) | 1984 | Review | Prog Hemostasis Thrombosis | Protein C anticoagulant pathway; activation of Protein C at the endothelial surface by thrombin–thrombomodulin complex requires Ca²⁺, establishing calcium as an obligate cofactor in physiological anticoagulation |
| [36334396](https://pubmed.ncbi.nlm.nih.gov/36334396/) | 2022 | Cohort | Thrombosis Research | SCUBE1 — a calcium-dependent signal peptide-CUB-EGF adhesion protein — is significantly elevated and independently associated with thrombotic complications, disease severity, and in-hospital mortality in COVID-19 patients |

---

## South Africa Market Information

No SAHPRA-registered products were identified for Calcium (DrugBank ID: DB01373) in this evidence pack (0 licences retrieved; market status: not marketed under this DrugBank entry).

Calcium-containing formulations are, however, broadly available in South Africa through various regulatory pathways:

- **Parenteral calcium** (calcium gluconate, calcium chloride) is included on the **South African Essential Medicines List (EML)** for hospital use in the management of hypocalcaemia, hyperkalaemia, hypermagnesaemia, and as an adjunct in cardiac resuscitation.
- **Oral calcium supplements** (alone or in combination with vitamin D) are widely available in South Africa as pharmacy supplements and scheduled medicines, though individual SAHPRA licence numbers were not retrieved in this search.

Healthcare professionals requiring specific product information should consult the SAHPRA online medicines register at [sahpra.org.za](https://www.sahpra.org.za).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> **Prescriber alert:** Based on available pharmacological evidence, **high-dose calcium supplementation has been associated with increased cardiovascular risk in some epidemiological studies and meta-analyses** (excess calcium intake promoting arterial calcification and prothrombotic states). The use of supplemental calcium as a targeted therapy for thrombotic disease is not supported by current clinical evidence and may be potentially counterproductive. Any investigational use in this indication should include rigorous monitoring of ionised serum calcium levels.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's high prediction score (98.25%) for calcium in thrombotic disease is biologically grounded in calcium's obligatory biochemical role as Coagulation Factor IV and its critical function in platelet Ca²⁺ signalling. However, this reflects calcium as a *mechanistic participant* in coagulation rather than as a *therapeutic drug candidate* for thrombosis. No Phase 2 or higher clinical trial has directly tested calcium supplementation for thrombotic disease, the mechanistic direction of any therapeutic hypothesis remains unresolved, and hypercalcaemia is itself a recognised prothrombotic condition — meaning supplementation could worsen rather than improve outcomes in this indication.

**To proceed, the following would be needed:**

- **Clearly defined mechanistic hypothesis:** Identify the specific clinical context in which calcium replacement may correct coagulation dysfunction (e.g., ionised hypocalcaemia in massive transfusion protocol, post-cardiac surgery, or severe sepsis-associated coagulopathy) — these represent the most pharmacologically defensible niches
- **Preclinical proof-of-concept data:** Demonstrate that targeted calcium supplementation at physiological replacement doses modulates thrombotic risk in a relevant disease model, without inducing hypercalcaemia or paradoxical prothrombotic effects
- **Review of calcium pharmacodynamics in the target population:** Clarify ionised vs. total calcium, route of administration, and monitoring parameters
- **SAHPRA registration pathway assessment:** Determine the applicable regulatory category for the specific calcium formulation and indication in South Africa
- **Population-level safety data:** Assess calcium supplementation and cardiovascular/thrombotic outcomes specific to South African patients, including nutrient-deficient or high-risk subgroups

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All website pages must include appropriate YMYL disclaimers. Data cut-off: 4 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

