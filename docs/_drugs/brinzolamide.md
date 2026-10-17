---
layout: default
title: Brinzolamide
parent: Model Prediction Only (L5)
nav_order: 78
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Brinzolamide: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Open-angle glaucoma"
monitor_inn: "Brinzolamide"
predicted_indications: ["hydrophthalmos", "commissural lip fistula", "osteoradionecrosis of the mandible", "oral leukoedema", "burning mouth syndrome"]
---

# Brinzolamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Brinzolamide: From Open-Angle Glaucoma and Ocular Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Brinzolamide is a topical carbonic anhydrase inhibitor, originally used to lower eye pressure in open-angle glaucoma and ocular hypertension.
The TxGNN model's top-ranked new prediction is **primary hereditary glaucoma** (score 99.48%), but **no clinical trials or publications** were found for it. The next-ranked predictions (open-angle glaucoma, glaucoma, closed-angle glaucoma) largely overlap with the existing labelled use, and the model also lists several unrelated conditions (oral and bone conditions) with no plausible mechanism.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma; ocular hypertension (the South African registration records did not include indication text) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 (model prediction only for this indication) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

**Note on the other predictions:** Open-angle glaucoma (96.7–97.7%), glaucoma (96.9%) and closed-angle glaucoma (96.6%) were also predicted. The first two are already-approved uses, supported by many Phase 3 trials (evidence level L1), so they are confirmation of existing use rather than true repurposing. Closed-angle glaucoma has limited evidence (L2).

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not available in the data compiled for this report. Based on known pharmacology, brinzolamide inhibits carbonic anhydrase II in the ciliary processes of the eye. This reduces aqueous humour production and lowers intraocular pressure (IOP). Its efficacy in open-angle glaucoma and ocular hypertension is well established.

Primary hereditary glaucoma is also characterised by raised IOP, so reducing aqueous humour production is mechanistically plausible. The TxGNN model probably learned this from the shared disease features of glaucoma-type conditions. However, this is a model-based inference only. No trials or literature support it, and inherited glaucoma often needs surgical or other specialist management.

Predictions of limited plausibility:
- **Closed-angle glaucoma:** Lowering aqueous production may help temporarily, and one randomised trial evaluated brinzolamide in acute primary angle closure. Angle closure, however, requires anatomical treatment (e.g. iridotomy), and there are case reports of brinzolamide-induced ciliary body effusion causing secondary angle closure.
- **Hydrophthalmos (congenital glaucoma):** Mechanistically plausible, but no data exist, and it is mainly treated surgically. Paediatric safety of systemic absorption would need evaluation.
- **Commissural lip fistula, osteoradionecrosis of the mandible, oral leukoedema, burning mouth syndrome:** No credible mechanistic link. These are likely graph-based artefacts.

## Clinical Trial Evidence

No clinical trials were found for the top-ranked prediction (primary hereditary glaucoma). The table below shows selected trials for the closely related, already-approved open-angle glaucoma indication, which is the best available context for brinzolamide's efficacy in raised IOP.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02512042](https://clinicaltrials.gov/study/NCT02512042) | Phase 3 | Completed | 973 | Bioequivalence study of generic brinzolamide 1% vs Azopt in open-angle glaucoma/ocular hypertension |
| [NCT01297920](https://clinicaltrials.gov/study/NCT01297920) | Phase 3 | Completed | 1062 | Brinzolamide/brimonidine fixed combination vs its components, three times daily |
| [NCT01297517](https://clinicaltrials.gov/study/NCT01297517) | Phase 3 | Completed | 1001 | Efficacy and safety of the same fixed combination vs its components |
| [NCT01309204](https://clinicaltrials.gov/study/NCT01309204) | Phase 3 | Completed | 1184 | Fixed combination vs brinzolamide plus brimonidine given separately |
| [NCT01310777](https://clinicaltrials.gov/study/NCT01310777) | Phase 3 | Completed | 771 | Safety and IOP-lowering of the fixed combination vs individual components |
| [NCT05022004](https://clinicaltrials.gov/study/NCT05022004) | Phase 3 | Completed | 599 | Therapeutic equivalence of generic brinzolamide 1% vs Azopt |
| [NCT04024072](https://clinicaltrials.gov/study/NCT04024072) | Phase 3 | Completed | 495 | Generic brinzolamide 1% vs Azopt, double-masked, active-controlled |
| [NCT04944290](https://clinicaltrials.gov/study/NCT04944290) | Phase 3 | Completed | 447 | Generic brinzolamide/brimonidine vs Simbrinza |
| [NCT01357616](https://clinicaltrials.gov/study/NCT01357616) | Phase 3 | Completed | 328 | Brinzolamide/timolol vs brinzolamide and timolol in Chinese patients |
| [NCT00061516](https://clinicaltrials.gov/study/NCT00061516) | Phase 3 | Completed | 78 | Brinzolamide (Azopt) and Betaxon in paediatric glaucoma/ocular hypertension |

For closed-angle glaucoma, the only listed trial, [NCT00758342](https://clinicaltrials.gov/study/NCT00758342) (Phase 4, terminated, n=37), tested brinzolamide as add-on to travoprost, and its evidence is weak.

## Literature Evidence

No publications were found for primary hereditary glaucoma. Selected literature for related indications:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26526633](https://pubmed.ncbi.nlm.nih.gov/26526633/) | 2016 | Systematic review/network meta-analysis | Ophthalmology | Comparative effectiveness of first-line medications for primary open-angle glaucoma |
| [31293419](https://pubmed.ncbi.nlm.nih.gov/31293419/) | 2019 | Meta-analysis | Front Pharmacol | Efficacy and safety of brinzolamide as add-on to prostaglandin analogues or β-blockers |
| [39677168](https://pubmed.ncbi.nlm.nih.gov/39677168/) | 2024 | RCT | Cureus | Brinzolamide/timolol vs dorzolamide/timolol in Indian patients (Phase 3) |
| [25430900](https://pubmed.ncbi.nlm.nih.gov/25430900/) | 2014 | RCT | Adv Ther | Fixed-combination brinzolamide/brimonidine vs concomitant use |
| [35026861](https://pubmed.ncbi.nlm.nih.gov/35026861/) | 2022 | RCT | J Clin Pharm Ther | Brinzolamide in the initial management of acute primary angle closure |
| [14565787](https://pubmed.ncbi.nlm.nih.gov/14565787/) | 2003 | Review | Drugs Aging | Brinzolamide in primary open-angle glaucoma and ocular hypertension |
| [25732405](https://pubmed.ncbi.nlm.nih.gov/25732405/) | 2015 | Review | Drugs Aging | Brinzolamide/brimonidine review in open-angle glaucoma or ocular hypertension |
| [28656780](https://pubmed.ncbi.nlm.nih.gov/28656780/) | 2017 | Review | Expert Opin Drug Saf | Safety evaluation of brimonidine and brinzolamide |
| [39870471](https://pubmed.ncbi.nlm.nih.gov/39870471/) | 2025 | Case report | BMJ Case Rep | Brinzolamide-induced ciliary body effusion with secondary angle closure |
| [30134369](https://pubmed.ncbi.nlm.nih.gov/30134369/) | 2018 | Case report | J Glaucoma | Brinzolamide-induced follicular conjunctivitis |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 50/15.4/0358 | Simbrinza | Drops | Not available in the registration records |
| Reg. No. 44/15.4/0046 | Azarga 5ml | Drops | Not available in the registration records |

Both registrations are valid, and both are fixed-combination products (brinzolamide with brimonidine, and with timolol, respectively). No single-ingredient brinzolamide product appears among the records compiled. Essential Medicines List status was not available.

## Safety Considerations

**Drug Interactions:** 32 potential interactions were identified in the interaction database, but none has a severity rating (all "Unknown"). Examples include pantoprazole, omeprazole, lansoprazole, prednisone, prednisolone, dexamethasone, simvastatin, rosuvastatin, warfarin, clopidogrel, famotidine and salbutamol. Their clinical significance should be checked against the Professional Information (PI).

**Safety signals in the literature:** Case reports describe brinzolamide-induced ciliary body effusion with secondary angle closure and follicular conjunctivitis. Brinzolamide is a sulfonamide derivative.

Warnings and contraindications from the SAHPRA-approved PI were not available. Please refer to the PI for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold** (for primary hereditary glaucoma)

**Rationale:**
- The top predicted new indication has a high model score and a plausible mechanism (IOP lowering), but no trials or publications support it, so it is a prediction only (L5).
- The better-supported predictions (open-angle glaucoma, glaucoma) are existing approved uses (L1, Proceed with Guardrails) and do not represent new repurposing. Closed-angle glaucoma is a research question (L2), with a safety concern about angle closure. The remaining predictions have no credible mechanism.

**To proceed, the following is needed:**
- Clinical data on brinzolamide in hereditary and congenital glaucoma, including paediatric safety and systemic absorption
- Review of the SAHPRA-approved PI for warnings, contraindications and approved indication text
- Confirmation of mechanism-of-action data and of whether a single-ingredient brinzolamide product is registered in South Africa
- Severity grading of the listed drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

