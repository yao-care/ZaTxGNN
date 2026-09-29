---
layout: default
title: Brinzolamide
parent: Model Prediction Only (L5)
nav_order: 77
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Brinzolamide: From Glaucoma and Ocular Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Brinzolamide is a topical carbonic anhydrase inhibitor used in eye drops to lower intraocular pressure (IOP) in open-angle glaucoma and ocular hypertension. The TxGNN model predicts it may be useful for **primary hereditary glaucoma**, but **no clinical trials or publications** were retrieved for that specific condition, so the prediction rests on the model score alone. Brinzolamide is already used for glaucoma, with more than 40 registered trials in open-angle glaucoma, so this is mostly an extension of an existing use rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma and ocular hypertension (from published literature; indication text is not provided in the SAHPRA registration records retrieved) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 (model prediction only for this indication) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Brinzolamide is a highly specific carbonic anhydrase II inhibitor. It lowers IOP by reducing the rate of aqueous humour formation in the ciliary epithelium (Cvetkovic & Perry, PMID 14565787). It is given as a 1% ophthalmic suspension, alone or in fixed combinations with timolol (beta-blocker) or brimonidine (alpha-2 agonist).

Primary hereditary glaucoma is a raised-IOP disease, so aqueous suppression is mechanistically plausible. However, the same reasoning applies to almost any glaucoma subtype, which may partly explain the high score. Hereditary and congenital forms are mainly managed surgically, and paediatric safety of topical carbonic anhydrase inhibitors would need separate evaluation. No brinzolamide-specific data for this entity were found.

Other glaucoma-related predictions from the same run are more strongly supported, but most are on-label:
- **Open-angle glaucoma (three model entries):** on-label, with Phase 3 evidence (shown below).
- **Closed-angle glaucoma:** evidence is limited to one small terminated Phase 4 adjunct trial and a single RCT in acute primary angle closure (PMID 35026861, 131 eyes). It is best treated as a research question, because IOP lowering does not fix the angle obstruction.
- **Non-ocular predictions:** commissural lip fistula, osteoradionecrosis of the mandible, oral leukoedema and burning mouth syndrome have no plausible mechanistic link and are likely graph artefacts.

---

## Clinical Trial Evidence

Currently no clinical trials are registered for primary hereditary glaucoma. No SANCTR, PACTR or ICTRP records were retrieved for this drug.

The table below shows the largest completed Phase 3 trials for the closely related, on-label indication of open-angle glaucoma and ocular hypertension. It shows that brinzolamide works in glaucoma generally. It is not evidence for the predicted indication.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01309204](https://clinicaltrials.gov/study/NCT01309204) | Phase 3 | Completed | 1184 | Brinzolamide/brimonidine fixed combination vs unfixed combination for IOP lowering |
| [NCT01297920](https://clinicaltrials.gov/study/NCT01297920) | Phase 3 | Completed | 1062 | Brinzolamide/brimonidine vs each component, three times daily, with a 3-month safety extension |
| [NCT01297517](https://clinicaltrials.gov/study/NCT01297517) | Phase 3 | Completed | 1001 | Brinzolamide/brimonidine vs each component, three times daily, 3-month efficacy and safety |
| [NCT02512042](https://clinicaltrials.gov/study/NCT02512042) | Phase 3 | Completed | 973 | Bioequivalence study with clinical endpoint, generic brinzolamide 1% vs Azopt |
| [NCT01310777](https://clinicaltrials.gov/study/NCT01310777) | Phase 3 | Completed | 771 | Brinzolamide/brimonidine fixed combination vs each component alone |
| [NCT05022004](https://clinicaltrials.gov/study/NCT05022004) | Phase 3 | Completed | 599 | Therapeutic equivalence of generic brinzolamide 1% vs Azopt |
| [NCT04024072](https://clinicaltrials.gov/study/NCT04024072) | Phase 3 | Completed | 495 | Perrigo brinzolamide 1% vs Azopt in POAG or ocular hypertension |
| [NCT02339584](https://clinicaltrials.gov/study/NCT02339584) | Phase 3 | Completed | 493 | Brinzolamide/brimonidine fixed combination vs unfixed combination, twice daily |
| [NCT04944290](https://clinicaltrials.gov/study/NCT04944290) | Phase 3 | Completed | 447 | Perrigo brinzolamide/brimonidine vs Simbrinza |
| [NCT01357616](https://clinicaltrials.gov/study/NCT01357616) | Phase 3 | Completed | 328 | Brinzolamide/timolol vs brinzolamide and timolol alone in Chinese patients (graded A for relevance) |

---

## Literature Evidence

No publications were retrieved for primary hereditary glaucoma. The table below shows key publications on brinzolamide in glaucoma more broadly.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41697795](https://pubmed.ncbi.nlm.nih.gov/41697795/) | 2026 | Systematic review/meta-analysis | Eur J Ophthalmol | Brinzolamide/timolol vs dorzolamide/timolol; 12 studies (11 RCTs), 1,885 patients; outcomes were IOP reduction, adverse events and patient preference |
| [31293419](https://pubmed.ncbi.nlm.nih.gov/31293419/) | 2019 | Systematic review/meta-analysis | Front Pharmacol | Brinzolamide as add-on to prostaglandin analogues or β-blockers in glaucoma or ocular hypertension |
| [26526633](https://pubmed.ncbi.nlm.nih.gov/26526633/) | 2016 | Network meta-analysis | Ophthalmology | Comparative effectiveness of first-line medications for POAG |
| [39677168](https://pubmed.ncbi.nlm.nih.gov/39677168/) | 2024 | RCT (Phase 3) | Cureus | Brinzolamide/timolol vs dorzolamide/timolol in Indian patients with POAG or ocular hypertension |
| [35026861](https://pubmed.ncbi.nlm.nih.gov/35026861/) | 2022 | RCT | J Clin Pharm Ther | IOP-lowering effect of brinzolamide in the initial management of acute primary angle closure (131 eyes) |
| [25064721](https://pubmed.ncbi.nlm.nih.gov/25064721/) | 2014 | RCT | Ophthalmology | Twice-daily brinzolamide/brimonidine vs each monotherapy |
| [25430900](https://pubmed.ncbi.nlm.nih.gov/25430900/) | 2014 | RCT | Adv Ther | Brinzolamide/brimonidine fixed combination vs concomitant brinzolamide plus brimonidine |
| [32158181](https://pubmed.ncbi.nlm.nih.gov/32158181/) | 2020 | RCT | Clin Ophthalmol | Non-inferiority of the fixed combination to concomitant use, with safety assessed |
| [14565787](https://pubmed.ncbi.nlm.nih.gov/14565787/) | 2003 | Review | Drugs & Aging | Brinzolamide lowers IOP by reducing aqueous humour formation; indicated for POAG and ocular hypertension |
| [39870471](https://pubmed.ncbi.nlm.nih.gov/39870471/) | 2025 | Case report | BMJ Case Rep | Topical brinzolamide-induced ciliary body effusion with secondary angle closure and myopic shift; resolved after stopping the drug |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 50/15.4/0358 | Simbrinza (brinzolamide/brimonidine) | Eye drops | Indication text not provided in the retrieved record |
| Reg. No. 44/15.4/0046 | Azarga 5ml (brinzolamide/timolol) | Eye drops | Indication text not provided in the retrieved record |

Both registrations are fixed-combination eye drops. No single-ingredient brinzolamide product appeared in the retrieved records. Essential Medicines List (EML) status was not included in the data reviewed.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

One safety signal appeared in the literature. Brinzolamide is a sulfonamide-derived agent, and a 2025 case report described ciliary body effusion with secondary angle closure after topical use (PMID 39870471). This matters if the drug were considered in angle-closure or other anatomically abnormal eyes. No drug interactions were found in the interaction query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication, primary hereditary glaucoma, has a very high model score (99.48%) but no trials or publications behind it.
- The strong evidence in this pack (multiple Phase 3 RCTs) concerns on-label open-angle glaucoma and ocular hypertension, which does not support a repurposing claim.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (warnings, contraindications, approved indications), which is a blocking gap for any safety screening.
- A targeted literature and trial search for brinzolamide or carbonic anhydrase inhibitors in hereditary and congenital glaucoma, including clarification of which subtypes "primary hereditary glaucoma" covers.
- A paediatric safety assessment, since congenital and hereditary forms present early in life.
- Confirmation of the SAHPRA approved-indication wording and any single-ingredient brinzolamide registration.
- A mechanism-of-action record from DrugBank to complete the mechanistic analysis.

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

