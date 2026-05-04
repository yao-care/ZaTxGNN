---
layout: default
title: Dorzolamide
parent: 僅模型預測 (L5)
nav_order: 185
evidence_level: L5
indication_count: 10
---

# Dorzolamide
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

# Dorzolamide: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Dorzolamide is a topical carbonic anhydrase inhibitor (ophthalmic solution) established for the management of open-angle glaucoma and elevated intraocular pressure.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**,
with **1 clinical trial** currently supporting this direction and no published literature identified for this specific indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / Ocular hypertension (based on established pharmacology; no SAHPRA registration data available) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| South Africa Market Status | Not registered with SAHPRA |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from the regulatory database is not available. Based on established pharmacological knowledge, Dorzolamide is a highly selective inhibitor of carbonic anhydrase isoenzyme II (CA-II) in the ciliary body epithelium of the eye. By blocking CA-II, Dorzolamide reduces bicarbonate ion secretion, which decreases aqueous humour production and consequently lowers intraocular pressure (IOP). This is the foundational mechanism by which it manages open-angle glaucoma and ocular hypertension, typically as a 2% ophthalmic solution (known internationally as Trusopt®, or in fixed combination with timolol as Cosopt®).

Primary hereditary glaucoma encompasses genetically determined forms of glaucoma — including conditions linked to MYOC and OPTN gene mutations — where abnormal aqueous drainage leading to elevated IOP remains the core pathological event. Because the shared pathophysiological endpoint (raised IOP) is identical to that in open-angle glaucoma, Dorzolamide's CA-II inhibitory mechanism is directly applicable. The TxGNN knowledge graph model has identified this pharmacological overlap, which underpins the high prediction score.

That said, different genetic subtypes of hereditary glaucoma may exhibit variable responses to IOP-lowering therapies, and the structural angle abnormalities in hereditary forms may limit drug efficacy relative to surgical approaches. Clinical evidence in genetically confirmed hereditary glaucoma populations remains limited, consisting of a single small Phase 2 paediatric trial. Individual patient assessment and genetic subtyping are strongly recommended before therapeutic decisions.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Compared the IOP-lowering effect of latanoprost vs dorzolamide in paediatric glaucoma patients (including primary hereditary cases) who were refractory to surgical procedures. Safety outcomes were co-assessed. Protocol was later amended to reduce the target enrolment to 68 eyes. Small sample size limits generalisability; this is the only directly relevant trial identified. |

---

## Literature Evidence

Currently no related literature available specifically linking Dorzolamide to primary hereditary glaucoma.

---

## South Africa Market Information

Dorzolamide is **not currently registered with SAHPRA** and holds no active product licences in South Africa.

Prescribers should be aware of the following:

- Dorzolamide (Trusopt® and Cosopt®) is registered and routinely used in the European Union, United States, and multiple other African countries
- Access for individual patients in South Africa may be explored via **SAHPRA Section 21** (unregistered medicines) for compelling clinical need
- Dorzolamide is **not currently listed on the South African Essential Medicines List (EML)**
- No SAHPRA-approved Professional Information (PI) document is available locally — international prescribing information (e.g., EMA/FDA labels) should be consulted

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> **Important note for prescribers:** No SAHPRA-specific warnings, contraindications, or drug interaction data were available in this evidence pack. Based on internationally published information, Dorzolamide is a **sulfonamide derivative** — clinicians should screen for sulfonamide hypersensitivity before prescribing. No drug-drug interaction data was identified in this evidence pack for Dorzolamide.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Only one small Phase 2 completed RCT (n=37, paediatric patients) supports the use of Dorzolamide specifically in primary hereditary glaucoma. While the IOP-lowering mechanism is pharmacologically plausible and directly applicable to hereditary forms of elevated-pressure glaucoma, the limited and indirect evidence base — combined with the absence of any SAHPRA registration — does not support clinical adoption at this stage.

**Important broader context:** This evidence pack separately identifies that Dorzolamide has very strong Level L1 evidence for primary open-angle glaucoma (TxGNN ranks 6 and 7 in this pack), supported by multiple Phase 3/4 completed RCTs with hundreds of patients. A SAHPRA registration application for the established open-angle glaucoma indication may represent a more immediately actionable pathway and should be evaluated in parallel.

**To proceed, the following is needed:**

- **SAHPRA registration pathway:** Initiate a registration application for the established glaucoma indication, or apply for Section 21 access for individual patients with compelling clinical need
- **Genetic subtype evidence:** Larger Phase 2/3 RCTs specifically recruiting patients with genetically confirmed primary hereditary glaucoma are required before an indication-specific decision can be made
- **Mechanism of action (MOA) data:** Retrieve complete CA-II inhibition profile from DrugBank to confirm mechanistic relevance across specific hereditary glaucoma subtypes (e.g., MYOC vs OPTN mutation carriers)
- **Safety data package:** Obtain complete sulfonamide allergy risk profile, contraindications list, and drug interaction data; populate SAHPRA-format PI document
- **Paediatric dosing guidance:** Primary hereditary glaucoma frequently presents in childhood — age-appropriate dosing, pharmacokinetic data, and safety data in the paediatric population must be confirmed before use
- **Local needs assessment:** Evaluate prevalence of primary hereditary glaucoma in the South African population to support clinical and economic justification for SAHPRA registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

