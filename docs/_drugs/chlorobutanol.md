---
layout: default
title: Chlorobutanol
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 10
---

# Chlorobutanol
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

# Chlorobutanol: From Pharmaceutical Preservative to Erectile Dysfunction

## One-Sentence Summary

Chlorobutanol is a halogenated alcohol compound used primarily as an antimicrobial preservative in pharmaceutical injections and ophthalmic preparations, with mild CNS depressant properties; it has no formally registered therapeutic indication.
The TxGNN model predicts it may be effective for **Erectile Dysfunction (ED)**, however **no clinical trials or published literature** directly link Chlorobutanol to this condition.
Current evidence is at the lowest confidence level (**L5 — model prediction only**), and this candidate is not recommended for further development at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered therapeutic indication; used as a pharmaceutical preservative and mild sedative/anaesthetic excipient |
| Predicted New Indication | Erectile Dysfunction |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 (model prediction only — no direct clinical or preclinical studies) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Chlorobutanol in this evidence pack. Based on known pharmacological literature, Chlorobutanol is a tertiary alcohol with broad CNS depressant activity, thought to act through enhancement of GABAergic inhibition and non-selective suppression of voltage-gated ion channels (Na⁺/K⁺). Historically it has been used as a mild sedative-hypnotic and local anaesthetic, though it is now employed almost exclusively as a preservative in multi-dose injectable and ophthalmic formulations at sub-therapeutic concentrations.

The core pathophysiology of erectile dysfunction involves the nitric oxide–cGMP signalling pathway, vascular endothelial function, and the hypothalamic-pituitary-gonadal axis. There is no established mechanistic bridge between Chlorobutanol's CNS depressant properties and these pathways. Indeed, the direction of effect is likely adverse rather than beneficial: generalised CNS inhibition, as seen with benzodiazepines and alcohol, is associated with **impaired** erectile function rather than improved function.

The TxGNN model's high prediction score most likely reflects topological proximity within the knowledge graph (e.g., shared CNS-related nodes) rather than a true pharmacological relationship. The absence of any supporting preclinical data, clinical trials, or published literature reinforces this interpretation. This prediction should be treated as a hypothesis-generating signal only, requiring substantial experimental validation before any clinical consideration.

---

## Clinical Trial Evidence

Two trials were retrieved by the database search; however, both are confirmed false positives (relevance grade C) — they investigate **Bipolar Androgen Therapy (testosterone cycling)** versus enzalutamide in castration-resistant prostate cancer. Erectile dysfunction may appear as a secondary quality-of-life endpoint, but Chlorobutanol plays no role in either study.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT02286921](https://clinicaltrials.gov/study/NCT02286921) | Phase 2 | Completed | 222 | Compares intramuscular testosterone (BAT) vs. enzalutamide in asymptomatic metastatic CRPC post-abiraterone. **Not related to Chlorobutanol.** ED is a secondary endpoint only. |
| [NCT02090114](https://clinicaltrials.gov/study/NCT02090114) | Phase 2 | Completed | 112 | Sequential BAT followed by enzalutamide or abiraterone in metastatic CRPC. **Not related to Chlorobutanol.** ED assessed as a quality-of-life measure only. |

> ⚠️ **Neither trial provides any evidence supporting Chlorobutanol use in erectile dysfunction.** These results represent keyword-indexing false positives and should not be counted as supportive evidence.

---

## Literature Evidence

Currently no related literature available linking Chlorobutanol to erectile dysfunction.

---

## South Africa Market Information

Chlorobutanol has **no SAHPRA registrations** and is not marketed as a standalone therapeutic product in South Africa. It may be present as a preservative excipient in registered multi-dose injectable or ophthalmic products, but is not approved as an active pharmaceutical ingredient for any indication.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for any product containing Chlorobutanol as an excipient. Chlorobutanol is known to have CNS depressant properties and may accumulate with repeated dosing due to its relatively long half-life. Report any adverse drug reactions to SAHPRA via [https://www.sahpra.org.za](https://www.sahpra.org.za).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score to Chlorobutanol for erectile dysfunction, but this is contradicted by the complete absence of supporting clinical trials, published literature, or preclinical studies; moreover, the drug's known CNS depressant mechanism is pharmacologically misaligned with the treatment of ED. The two trials retrieved from ClinicalTrials.gov are confirmed false positives unrelated to Chlorobutanol.

**To proceed, the following would be needed:**

- **Establish MOA data**: Obtain full DrugBank mechanism-of-action data (DG002) to assess whether any molecular targets could plausibly interact with NO–cGMP or vascular pathways relevant to ED.
- **Preclinical validation**: At minimum, a peer-reviewed in vitro or animal study demonstrating Chlorobutanol activity in an ED-relevant model before any clinical consideration.
- **Safety profile clarification**: Obtain full prescriber safety information (DG001) including CNS toxicity thresholds, as CNS depression is the primary pharmacological concern and a likely confounder in ED assessment.
- **Reformulation strategy**: If a preclinical signal were found, identify a viable therapeutic formulation and dose range distinct from preservative concentrations, and confirm systemic exposure is achievable without unacceptable toxicity.
- **SAHPRA registration pathway**: Given zero current SAHPRA registrations, a de novo registration dossier would be required prior to any South African clinical development.

> *This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. YMYL disclaimer: all predictions are model-generated hypotheses and must not inform clinical decisions without independent expert review.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

