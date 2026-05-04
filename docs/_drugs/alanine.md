---
layout: default
title: Alanine
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 10
---

# Alanine
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

# Alanine: From Amino Acid Supplement to Gastroparesis

---

## One-Sentence Summary

Alanine (L-Alanine) is a non-essential endogenous amino acid with no currently approved standalone therapeutic indication registered in South Africa.
The TxGNN model predicts it may have potential in **Gastroparesis**, with a prediction score of **99.37%**.
However, **no clinical trials or publications directly investigating Alanine for this indication** were identified; all 9 retrieved trials studied other drugs in gastroparesis patients, placing this prediction at **Evidence Level L5** — model-driven only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None — no approved therapeutic indication identified (endogenous amino acid; no SAHPRA-registered standalone product) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Alanine as a pharmaceutical agent. L-Alanine is a naturally occurring non-essential amino acid and a central participant in several metabolic pathways — most notably the **glucose–alanine cycle**, which shuttles nitrogen between peripheral muscle and the liver and serves as a key gluconeogenic substrate during fasting states.

The mechanistic hypothesis embedded in the TxGNN knowledge graph rests on the observation that luminal amino acids, including L-Alanine, can stimulate enteroendocrine cells in the small intestine to secrete gut hormones — particularly **GLP-1 (glucagon-like peptide-1)** and **CCK (cholecystokinin)** — which modulate gastric motility and emptying rate. Since delayed gastric emptying is the pathophysiological hallmark of gastroparesis, the model may have identified this indirect chain of events as a potential therapeutic link. In addition, the glucose–alanine cycle engages gastrointestinal energy metabolism in ways that could theoretically influence enteric neuromuscular function.

However, this connection is **highly indirect and unvalidated**. The pathway from exogenous Alanine supplementation → meaningful enteroendocrine hormone release → clinically measurable improvement in gastric emptying has not been demonstrated in any preclinical model or human study. Furthermore, because Alanine carries no established approved therapeutic indication globally, this represents a hypothesis for an endogenous metabolite rather than a conventional drug repurposing scenario. Caution is warranted in interpreting the high TxGNN score as biological signal, as knowledge graph predictions for non-drug endogenous molecules may reflect metabolic co-occurrence patterns rather than pharmacological mechanism.

---

## Clinical Trial Evidence

> **Important caveat:** The 9 trials retrieved below were identified by searching ClinicalTrials.gov using the disease term "gastroparesis." **None of these trials investigated Alanine.** They are provided solely as contextual reference for the gastroparesis treatment landscape and to illustrate the state of clinical research in this area.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03587142](https://clinicaltrials.gov/study/NCT03587142) | Phase 2 | Completed | 96 | Buspirone (5-HT1A agonist) vs placebo for early satiety and gastroparesis symptoms. Study drug: Buspirone — not Alanine. |
| [NCT01149369](https://clinicaltrials.gov/study/NCT01149369) | Phase 2 | Completed | 126 | Aprepitant (NK1 receptor antagonist) vs placebo for chronic nausea and vomiting of presumed gastric origin. Study drug: Aprepitant — not Alanine. |
| [NCT03941288](https://clinicaltrials.gov/study/NCT03941288) | Phase 2 | Completed | 92 | Cannabidiol (CBD) pharmacodynamics and efficacy for gastroparesis and functional dyspepsia. Study drug: CBD — not Alanine. |
| [NCT01262898](https://clinicaltrials.gov/study/NCT01262898) | Phase 2 | Completed | 79 | GSK962040 (motilin receptor agonist), 28-day dosing in Type 1 and Type 2 diabetic gastroparesis. Study drug: GSK962040 — not Alanine. |
| [NCT01602549](https://clinicaltrials.gov/study/NCT01602549) | Phase 2 | Completed | 58 | GSK962040 effect on L-DOPA pharmacokinetics in Parkinson's disease patients with delayed gastric emptying. Study drug: GSK962040 — not Alanine. |
| [NCT01934192](https://clinicaltrials.gov/study/NCT01934192) | Phase 2 | Terminated | 91 | GSK962040 to enhance enteral nutrition delivery in critically ill ICU patients with feeding intolerance. Trial terminated early; study drug: GSK962040 — not Alanine. |
| [NCT02793154](https://clinicaltrials.gov/study/NCT02793154) | Phase 4 | Terminated | 4 | Albiglutide vs exenatide effect on gastric myoelectrical activity and gastric emptying in T2DM. Terminated after enrolling only 4 subjects; minimal statistical value. |
| [NCT06452966](https://clinicaltrials.gov/study/NCT06452966) | N/A | Recruiting | 350 | Traditional Chinese medicine interventions for organ failure prevention in ICU patients (multi-centre). No direct relevance to Alanine. |
| [NCT07270939](https://clinicaltrials.gov/study/NCT07270939) | N/A | Not Yet Recruiting | 150 | Comparison of 18-hour, 20-hour, and 24-hour enteral feeding cycles in critically ill patients. Not yet recruiting; no relevance to Alanine. |

**No clinical trials directly investigating Alanine as a treatment for gastroparesis are currently registered.**

---

## Literature Evidence

Currently no related literature available for Alanine in gastroparesis.

---

## South Africa Market Information

Alanine (DrugBank ID: DB00160) is **not currently registered or marketed as a standalone therapeutic product in South Africa**. No SAHPRA product licences were identified.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|--------------------|--------------|-------------|---------------------|
| — | No registered products found | — | — |

> **Note:** L-Alanine is present as a component in multi-ingredient parenteral nutrition (TPN) amino acid solutions registered in South Africa; however, these are multi-component formulations and not single-ingredient Alanine medicines. No Essential Medicines List (EML) inclusion applies for standalone Alanine.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> As no SAHPRA-registered standalone Alanine product exists, no PI document is currently available. General safety principles for amino acid supplementation apply. Consultation with relevant clinical pharmacology references is recommended for any research use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is driven entirely by TxGNN knowledge graph topology (Evidence Level L5), with **no clinical trials, observational studies, or published literature** directly investigating Alanine as a treatment for gastroparesis or any of the other 9 predicted indications (all also rated L5/Hold). The proposed mechanistic link is theoretically plausible but completely unvalidated at every level — preclinical and clinical. Alanine carries no approved therapeutic indication globally, and is not registered in South Africa, making repurposing evaluation distinctly premature at this stage.

**To proceed, the following is needed:**
- **Preclinical proof-of-concept:** In vitro and animal model studies demonstrating that exogenous L-Alanine supplementation produces measurable improvement in gastric emptying or gastroparesis-relevant outcomes
- **Mechanistic validation:** Characterisation of the specific pathway from Alanine dosing → enteroendocrine hormone stimulation → gastric motility improvement, including dose–response relationships
- **Pharmacokinetic profiling:** Determination of what route, dose, and formulation of Alanine would achieve therapeutic concentrations at the relevant gastrointestinal sites
- **Safety and tolerability data:** Assessment of any risks associated with therapeutic-dose (as opposed to nutritional) Alanine administration, particularly for chronically ill patients
- **Clinical differentiation:** A clear rationale for why Alanine would offer advantages over established gastroparesis pharmacotherapies (e.g., metoclopramide, domperidone, erythromycin)
- **SAHPRA registration pathway:** If evidence accumulates, a regulatory strategy for obtaining SAHPRA registration for a standalone Alanine product would need to be defined

---

> **Disclaimer:** This report is intended for research reference only and does not constitute medical advice. Drug repurposing candidates identified by the TxGNN model require clinical validation before any therapeutic application. This document is not a substitute for the SAHPRA-approved Professional Information (PI) or independent clinical judgement.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

