---
layout: default
title: Magnesium
parent: Model Prediction Only (L5)
nav_order: 304
evidence_level: L5
indication_count: 10
---

# Magnesium
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

# Magnesium: From Nutritional/Electrolyte Supplementation to Migraine Disorder

## One-Sentence Summary

Magnesium is an essential mineral and electrolyte. In South Africa it is registered mainly in parenteral nutrition and supplement products, although the data compiled for this report do not record an approved indication text.
The TxGNN model predicts it may be effective for **migraine disorder** (score 98.0%), with **8 clinical trials** and **20 publications** identified for this direction.
Only a few trials are completed, and none has reported results in the data compiled for this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA data compiled for this report (approved indication text is empty for all registrations) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 98.03% |
| Evidence Level | L2 (see note below) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 6 |
| Recommended Decision | Proceed with Guardrails |

**Evidence level note:** The strict rule for L1 is at least two completed Phase 3 RCTs. The data show one completed Phase 3 RCT (NCT05967442) and one completed Phase 2/3 RCT (NCT02322333). Both enrolled 157 participants, so they may be the same or related studies and should not be counted as independent evidence. For this reason the report assigns L2 rather than L1.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for the drug's original use is not available. Based on the mechanistic rationale compiled for migraine, magnesium acts as a physiological NMDA receptor blocker and calcium channel modulator.

Magnesium deficiency is linked to several processes implicated in migraine:
- cortical spreading depression
- increased neuronal excitability
- platelet aggregation
- release of CGRP and substance P

These mechanisms plausibly support both **prophylactic** (preventive) and **acute** (attack) use. The literature also describes reduced intracellular magnesium and disordered mitochondrial energy metabolism in people with migraine (e.g., Welch & Ramadan, 1995).

A formal "similarity to the original indication" analysis was not available. The case for migraine therefore rests on the pathophysiological link, not on similarity to a registered indication.

---

## Clinical Trial Evidence

No SANCTR or PACTR identifiers were found in the data compiled for this report.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05967442](https://clinicaltrials.gov/study/NCT05967442) | Phase 3 | Completed | 157 | Randomised, placebo-controlled, double-blind. IV magnesium sulfate vs IV metoclopramide and prochlorperazine for acute migraine in the emergency department. No results available; enrollment matches NCT02322333 |
| [NCT02322333](https://clinicaltrials.gov/study/NCT02322333) | Phase 2/3 | Completed | 157 | Multicentre, randomised, double-blind, placebo-controlled study of MLD10 for migraine prevention in adults. The magnesium-specific effect needs verification |
| [NCT01756209](https://clinicaltrials.gov/study/NCT01756209) | Phase 4 | Completed | 160 | Acetaminophen and ibuprofen with and without magnesium prophylaxis in children and adolescents with primary migraine. Combination design, so the magnesium effect is partly confounded |
| [NCT06904287](https://clinicaltrials.gov/study/NCT06904287) | Phase 3 | Recruiting | 100 | Magnesium added to prochlorperazine for acute migraine in the emergency department. No results yet |
| [NCT07779486](https://clinicaltrials.gov/study/NCT07779486) | N/A | Recruiting | 300 | IV magnesium sulfate vs paracetamol for acute non-traumatic headache in the emergency department. Not specific to migraine |
| [NCT07147972](https://clinicaltrials.gov/study/NCT07147972) | Phase 3 | Not yet recruiting | 100 | Nutraceuticals (magnesium, riboflavin, coenzyme Q10) vs conventional prophylaxis. Magnesium is likely one component |
| [NCT04463875](https://clinicaltrials.gov/study/NCT04463875) | N/A | Completed | 113 | Open-label, real-world study of a fixed combination supplement containing magnesium for episodic migraine prophylaxis. Uncontrolled and confounded |
| [NCT03132233](https://clinicaltrials.gov/study/NCT03132233) | N/A | Completed | 42 | Exogenous ketone bodies for migraine prevention. Magnesium is not the main intervention, so relevance is indirect |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26752497](https://pubmed.ncbi.nlm.nih.gov/26752497/) | 2016 | Meta-analysis of RCTs | Pain Physician | Evaluates IV and oral magnesium for acute migraine and prevention; earlier studies had produced equivocal findings |
| [29131326](https://pubmed.ncbi.nlm.nih.gov/29131326/) | 2018 | Systematic review | Headache | Systematically assesses the evidence base for magnesium in migraine prophylaxis |
| [39404918](https://pubmed.ncbi.nlm.nih.gov/39404918/) | 2025 | Systematic review and dose-response meta-analysis of RCTs | Neurol Sci | Examines dietary supplements for migraine prophylaxis; existing evidence described as conflicting |
| [25916335](https://pubmed.ncbi.nlm.nih.gov/25916335/) | 2015 | RCT (combination) | J Headache Pain | Randomised, placebo-controlled, double-blind multicentre trial of a riboflavin, magnesium and Q10 supplement for migraine prophylaxis |
| [41216917](https://pubmed.ncbi.nlm.nih.gov/41216917/) | 2025 | Cochrane protocol | Cochrane Database Syst Rev | Protocol to assess the benefits and harms of magnesium supplementation for migraine prevention in children and adults; no results yet |
| [40005053](https://pubmed.ncbi.nlm.nih.gov/40005053/) | 2025 | Review | Nutrients | Reviews the link between magnesium status and migraine |
| [35268064](https://pubmed.ncbi.nlm.nih.gov/35268064/) | 2022 | Review | Nutrients | Magnesium in migraine pathogenesis and treatment; discusses cortical spreading depression and glutamatergic neurotransmission |
| [39853578](https://pubmed.ncbi.nlm.nih.gov/39853578/) | 2025 | Review | Curr Pain Headache Rep | Nutraceuticals for headache, including magnesium, riboflavin, coenzyme Q10 and feverfew |
| [22211870](https://pubmed.ncbi.nlm.nih.gov/22211870/) | 2012 | Review | Headache | Rescue therapy for acute migraine in emergency and urgent care settings, covering triptans, DHE and magnesium |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline / evidence assessment | Headache | American Headache Society assessment of acute migraine pharmacotherapies |

---

## South Africa Market Information

Six registrations are listed in total (6 valid, none cancelled). The first five are shown below. Approved indication text is not recorded for any registration.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EXCLUSION UNDER SECTION 36 & SECTION 14 | ITN8011XA 1520ml adult | TPN | Not recorded |
| ARTICLE 21B N/A | TPN non-specific | Infusion | Not recorded |
| G2667 (ACT 101/1965) | Gericomplex | Capsule | Not recorded |
| 41/10.2.1/0849 | Spiriva Respimat inhaler 60 doses | Inhaler | Not recorded |
| H2062 (ACT 101) | Filibon | Capsule | Not recorded |

Available forms are parenteral (TPN, infusion), oral (capsule) and inhaled. The inhaler entry looks unusual for a magnesium product and should be checked against the register. No registration is a stand-alone magnesium product indicated for migraine.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug interaction records were found in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- There is a plausible mechanism and a body of trials and systematic reviews specific to migraine, including completed randomised trials of IV magnesium.
- However, no trial results are available in the data compiled for this report, the two key completed trials may overlap, and several trials use combination products. Safety information for the South African products is also missing.

**To proceed, the following is needed:**
- Review of the SAHPRA-approved PI (warnings, contraindications, interactions) for the relevant magnesium product. This is a blocking gap for safety screening.
- Detailed mechanism of action data from DrugBank.
- Published results and confirmation of whether NCT05967442 and NCT02322333 are independent studies.
- Magnesium-specific efficacy data separated from combination supplements, ideally from the Cochrane review (currently protocol stage) and the meta-analyses above.
- A decision on formulation and route (oral prophylaxis vs IV acute use), including which registered or unregistered product would be used. Route compatibility has not been assessed.
- Clarification of the registered indications of the South African products and their Essential Medicines List status.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

