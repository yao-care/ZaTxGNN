---
layout: default
title: Magnesium
parent: Model Prediction Only (L5)
nav_order: 302
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

# Magnesium: From Parenteral Nutrition Component to Migraine Disorder

## One-Sentence Summary

Magnesium is an essential mineral. In South Africa it is registered mainly as a component of parenteral nutrition (TPN) products.
The TxGNN model predicts it may be effective for **Migraine Disorder** (score 98.0%), with **28 clinical trials** retrieved (only a few test magnesium directly) and **20 publications** supporting this direction.
Magnesium is already a guideline-listed migraine option, so this prediction largely confirms existing practice rather than opening a new therapeutic area.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA data. The listed products are parenteral nutrition (TPN) products. |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 98.03% |
| Evidence Level | L2 (see note below) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 20 |
| Recommended Decision | Proceed with Guardrails |

**Evidence level note:** The evidence pack labels this L1. Only one completed Phase 3 RCT tests magnesium directly (NCT05967442). The other completed Phase 3 or Phase 2/3 migraine trials in the pack test other agents. Under the stated rules this gives L2. A published meta-analysis of RCTs (PMID 26752497) supports the same direction.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the record. Magnesium is a physiological electrolyte and an enzyme cofactor. It is given in South Africa mainly as part of parenteral nutrition, where it corrects or prevents deficiency.

The link to migraine is mechanistic and clinical:

- Magnesium modulates NMDA receptor activity and cortical spreading depression, a process thought to underlie migraine aura.
- It also influences CGRP and serotonin release and vascular tone.
- Low serum and intracellular magnesium are repeatedly reported in people with migraine.

This fits the high TxGNN score. The "original" use (deficiency correction) and the "new" use (migraine) differ, but the biology links them. Magnesium deficiency lowers the threshold for neuronal hyperexcitability, which is relevant to migraine.

---

## Clinical Trial Evidence

No ICTRP, SANCTR or PACTR records were identified in the evidence pack.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05967442](https://clinicaltrials.gov/study/NCT05967442) | Phase 3 | Completed | 157 | Randomised, placebo-controlled, double-blind. IV magnesium sulfate vs IV metoclopramide and prochlorperazine for acute migraine in the emergency department. Direct evidence. Results are not in the pack. |
| [NCT06904287](https://clinicaltrials.gov/study/NCT06904287) | Phase 3 | Recruiting | 100 | Magnesium added to prochlorperazine for migraine in the emergency department. |
| [NCT07147972](https://clinicaltrials.gov/study/NCT07147972) | Phase 3 | Not yet recruiting | 100 | Nutraceuticals (magnesium, riboflavin, coenzyme Q10) vs conventional prophylaxis. Magnesium is likely a component. |
| [NCT01756209](https://clinicaltrials.gov/study/NCT01756209) | Phase 4 | Completed | 160 | Acetaminophen and ibuprofen with and without magnesium prophylaxis in childhood migraine. |
| [NCT03190044](https://clinicaltrials.gov/study/NCT03190044) | N/A | Unknown | 82 | Fixed combination containing magnesium (PACR) for prophylaxis. Magnesium's own effect cannot be isolated. |
| [NCT04463875](https://clinicaltrials.gov/study/NCT04463875) | N/A | Completed | 113 | Open-label, real-world study of a magnesium-containing combination for episodic migraine prophylaxis. Uncontrolled. |
| [NCT02901756](https://clinicaltrials.gov/study/NCT02901756) | N/A | Completed | 132 | Observational study of coenzyme Q10, feverfew and magnesium for prophylaxis over 3 months. |
| [NCT04759040](https://clinicaltrials.gov/study/NCT04759040) | N/A | Completed | 120 | Randomised, placebo-controlled, double-blind trial of a supplement containing CoQ10, magnesium, riboflavin and feverfew. |
| [NCT06274255](https://clinicaltrials.gov/study/NCT06274255) | N/A | Unknown | 60 | Serum magnesium levels compared between children with migraine and controls. Observational. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26752497](https://pubmed.ncbi.nlm.nih.gov/26752497/) | 2016 | Meta-analysis of RCTs | Pain Physician | Assessed IV and oral magnesium for acute migraine and prevention. Earlier studies had given equivocal findings. |
| [39404918](https://pubmed.ncbi.nlm.nih.gov/39404918/) | 2025 | Systematic review and dose-response meta-analysis | Neurol Sci | Dietary supplements for migraine prophylaxis. Prior evidence was conflicting. |
| [29131326](https://pubmed.ncbi.nlm.nih.gov/29131326/) | 2018 | Systematic review | Headache | Systematically evaluated the evidence base for magnesium in migraine prophylaxis. |
| [25916335](https://pubmed.ncbi.nlm.nih.gov/25916335/) | 2015 | RCT | J Headache Pain | Randomised, placebo-controlled, double-blind, multicentre trial of a fixed riboflavin, magnesium and Q10 supplement for prophylaxis. |
| [40005053](https://pubmed.ncbi.nlm.nih.gov/40005053/) | 2025 | Review | Nutrients | Links magnesium deficiency to migraine. |
| [35268064](https://pubmed.ncbi.nlm.nih.gov/35268064/) | 2022 | Review | Nutrients | Magnesium deficiency may contribute to cortical depression and abnormal glutamatergic transmission. |
| [31691193](https://pubmed.ncbi.nlm.nih.gov/31691193/) | 2020 | Review | Biol Trace Elem Res | Role of magnesium in migraine pathophysiology and treatment, including maintenance of neuronal electric potential. |
| [32878232](https://pubmed.ncbi.nlm.nih.gov/32878232/) | 2020 | Review | Nutrients | Mechanisms, bioavailability and efficacy of magnesium (including magnesium pidolate) in headache. Notes that oral magnesium is recommended for headache relief in several guidelines. |
| [35190383](https://pubmed.ncbi.nlm.nih.gov/35190383/) | 2022 | Narrative review | Arch Dis Child | New migraine management options in children and young people. Covers nutraceuticals including magnesium. |
| [40378325](https://pubmed.ncbi.nlm.nih.gov/40378325/) | 2025 | Review | Am Fam Physician | Migraine prophylaxis overview. |

---

## South Africa Market Information

The pack records 20 registrations. The five main ones are shown. None has a standard registration number. They are exclusions under Sections 36 and 14, or an Article 21B entry. No approved indication text or manufacturer is recorded. Essential Medicines List (EML) status is not provided in the data.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Exclusion under Section 36 & Section 14 | ITN8011XA 1520ml adult | TPN | Not recorded |
| Exclusion under Section 36 & Section 14 | ITN 3014Xa 750ml | TPN | Not recorded |
| Article 21B (N/A) | TPN non-specific | Infusion | Not recorded |
| Exclusion under Section 36 & Section 14 | ITN 8807a 2390ml | TPN | Not recorded |
| Exclusion under Section 36 & Section 14 | ITN 5501a 2240ml | TPN | Not recorded |

Other dosage forms in the pack are oral capsule and inhaler. Products are not confirmed as migraine-indicated.

---

## Safety Considerations

Guardrails from the repurposing assessment:

- Check renal function before use, because magnesium is renally cleared.
- Watch for diarrhoea and hypermagnesaemia.
- Check interactions with other medicines.

No drug interactions were found in the DDI query. For full warnings and contraindications, please refer to the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 3 RCT and a meta-analysis of RCTs support magnesium in migraine. Ongoing Phase 3 trials add to this, and the mechanism is plausible. Much of the evidence comes from combination supplements, so magnesium's own effect is hard to isolate, and earlier findings were equivocal.

**To proceed, the following is needed:**
- The SAHPRA package insert, to confirm warnings, contraindications and approved indications. The safety screen cannot be completed without it.
- Results of NCT05967442 (and the ongoing Phase 3 trials as they report), to confirm efficacy.
- Route and formulation compatibility. Registered South African products are TPN and infusion forms, while much migraine evidence uses IV or oral magnesium.
- A renal function and hypermagnesaemia monitoring plan.
- A check for South African registry entries (SANCTR, PACTR), since none were retrieved.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

