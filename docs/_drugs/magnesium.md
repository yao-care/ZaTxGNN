---
layout: default
title: Magnesium
parent: 僅模型預測 (L5)
nav_order: 296
evidence_level: L5
indication_count: 10
---

# Magnesium
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

# Magnesium: From Electrolyte/Nutritional Supplementation to Migraine Prophylaxis

## One-Sentence Summary

Magnesium (DrugBank DB14513) is an essential physiological cation traditionally used for electrolyte replacement and conditions such as hypomagnesemia, eclampsia/pre-eclampsia, and cardiac arrhythmia. The TxGNN model predicts it may be effective for **Migraine Disorder**, with **28 clinical trials** and **20 publications** currently supporting this direction. The product is not currently registered with SAHPRA, so any clinical application in South Africa would need to be built from imported or compounded magnesium preparations.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No SAHPRA-registered indication text available (product not marketed in South Africa); magnesium is broadly used as an electrolyte/mineral supplement |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 98.03% |
| Evidence Level | L1 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action (MOA) data for magnesium is not available in this evidence pack. Based on known pharmacology, magnesium is the body's second most abundant intracellular cation and a cofactor for over 300 enzymatic reactions; clinically it is well established for electrolyte replacement, eclampsia/pre-eclampsia, cardiac arrhythmia, and severe asthma, and this general efficacy record is well documented even though a formal "original indication" is not captured in this dataset.

Specific to migraine, the mechanistic rationale is strong: Mg²⁺ acts as a physiological antagonist at the NMDA receptor and at voltage-gated calcium channels, which can suppress cortical spreading depression (CSD) and trigeminovascular activation, and it also relaxes vascular smooth muscle. Migraine patients frequently show low serum or intracellular free magnesium, giving a clear mechanistic link. This is not a purely theoretical connection — IV magnesium sulfate is already used in emergency departments for acute migraine, and oral magnesium is a long-standing option for migraine prophylaxis in clinical practice.

In this sense, the prediction extends an existing, informal pattern of clinical use into a more structured therapeutic indication rather than proposing an entirely novel mechanism. The main caveat is that many trials in the evidence set use magnesium as one component of a multi-ingredient nutraceutical (e.g., with riboflavin, CoQ10, feverfew), which dilutes the strength of monotherapy evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05967442](https://clinicaltrials.gov/study/NCT05967442) | Phase 3 | Completed | 157 | Randomized, double-blind, placebo-controlled comparison of IV magnesium sulfate vs. IV metoclopramide/prochlorperazine for acute migraine in the ED |
| [NCT06904287](https://clinicaltrials.gov/study/NCT06904287) | Phase 3 | Recruiting | 100 | Evaluates whether adding magnesium to prochlorperazine improves migraine pain relief in the ED |
| [NCT03190044](https://clinicaltrials.gov/study/NCT03190044) | N/A | Unknown | 82 | RCT of fixed combination PACR (magnesium, partenium, andrographis, CoQ10, riboflavin) for migraine prophylaxis |
| [NCT07147972](https://clinicaltrials.gov/study/NCT07147972) | Phase 3 | Not yet recruiting | 100 | Compares nutraceuticals (magnesium, riboflavin, CoQ10) vs. conventional prophylactic therapy for migraine |
| [NCT04463875](https://clinicaltrials.gov/study/NCT04463875) | N/A | Completed | 113 | Real-world prospective study of a fixed magnesium/vitamin B2/feverfew/andrographis/CoQ10 combination (Vivinor®) for episodic migraine prophylaxis |
| [NCT01756209](https://clinicaltrials.gov/study/NCT01756209) | Phase 4 | Completed | 160 | Compared acetaminophen/ibuprofen with vs. without magnesium prophylaxis for acute primary migraine in children |
| [NCT02901756](https://clinicaltrials.gov/study/NCT02901756) | N/A | Completed | 132 | Prospective observational study of CoQ10 + feverfew + magnesium for migraine prophylaxis |
| [NCT04491474](https://clinicaltrials.gov/study/NCT04491474) | Phase 4 | Completed | 128 | RCT of occipital/supraorbital nerve block vs. placebo for acute migraine in the ED; IV magnesium noted as a standard comparator therapy |
| [NCT04759040](https://clinicaltrials.gov/study/NCT04759040) | N/A | Completed | 120 | RCT of MigraineGuard™ supplement (CoQ10, magnesium, riboflavin, feverfew, skullcap, black pepper) for migraine severity/frequency |
| [NCT01010711](https://clinicaltrials.gov/study/NCT01010711) | N/A | Unknown | 76 | Dietary supplement study (CoQ10, minerals including magnesium, antioxidants) for migraine in children/adolescents |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26752497](https://pubmed.ncbi.nlm.nih.gov/26752497/) | 2016 | Meta-analysis of RCTs | Pain Physician | IV and oral magnesium show benefit in reducing acute and preventive migraine outcomes |
| [25916335](https://pubmed.ncbi.nlm.nih.gov/25916335/) | 2015 | RCT | J Headache Pain | Randomized, double-blind, placebo-controlled multicenter trial of riboflavin + magnesium + CoQ10 improves migraine symptoms |
| [29131326](https://pubmed.ncbi.nlm.nih.gov/29131326/) | 2018 | Systematic Review | Headache | Systematically evaluates the evidence base for magnesium in migraine prophylaxis |
| [40005053](https://pubmed.ncbi.nlm.nih.gov/40005053/) | 2025 | Review | Nutrients | Overview of magnesium deficiency's role in migraine pathophysiology and management |
| [31691193](https://pubmed.ncbi.nlm.nih.gov/31691193/) | 2020 | Review | Biol Trace Elem Res | Reviews magnesium's role in migraine pathophysiology and treatment |
| [35268064](https://pubmed.ncbi.nlm.nih.gov/35268064/) | 2022 | Review | Nutrients | Magnesium deficiency linked to cortical spreading depression and glutamatergic dysregulation in migraine |
| [32878232](https://pubmed.ncbi.nlm.nih.gov/32878232/) | 2020 | Review | Nutrients | Reviews mechanisms, bioavailability, and therapeutic efficacy of magnesium for headache/migraine |
| [30600979](https://pubmed.ncbi.nlm.nih.gov/30600979/) | 2019 | Review | American Family Physician | Migraine prophylaxis guideline overview including nutraceutical options |
| [26404370](https://pubmed.ncbi.nlm.nih.gov/26404370/) | 2015 | Review | Nutrients | General review of magnesium's role in prevention and therapy across conditions |
| [23674807](https://pubmed.ncbi.nlm.nih.gov/23674807/) | 2013 | Review | Advances in Nutrition | Reviews magnesium's broad role in disease prevention and overall health |

---

## South Africa Market Information

Magnesium currently has **no SAHPRA product registrations** and is classified as **Not Marketed** in South Africa. There is no locally approved Professional Information (PI) or registered indication text to draw from at this time.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(No structured warnings, contraindications, or drug-interaction data were returned for this candidate — a locally validated PI/label review is a Blocking data gap that must be resolved before any safety assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Migraine disorder has the strongest evidence among all predicted indications (L1, 28 trials including a completed Phase 3 RCT of IV magnesium for acute migraine, plus a supportive meta-analysis of RCTs), and the mechanism (NMDA/calcium-channel antagonism, CSD suppression) is well established and already reflected in real-world emergency and prophylactic practice.
- However, the absence of any SAHPRA-registered magnesium product in South Africa, combined with unresolved safety-labeling data, means this cannot move forward as a simple "Go" — it requires guardrails around sourcing, local registration, and PI-based safety review before clinical guidance is issued.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI), including warnings, contraindications, and drug interactions (currently a Blocking data gap)
- Confirmed DrugBank/formal mechanism-of-action documentation for magnesium (currently a High-severity data gap)
- Clarification of the local regulatory/import pathway, since there are zero current SAHPRA registrations
- Additional trials isolating magnesium monotherapy (rather than multi-ingredient nutraceutical combinations) to strengthen the evidence specific to magnesium itself
- Route and dosage-form compatibility assessment (IV vs. oral) for the intended clinical use case, which is currently unassessed (pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

