---
layout: default
title: Flucloxacillin
parent: Moderate Evidence (L3-L4)
nav_order: 232
evidence_level: L4
indication_count: 10
---

# Flucloxacillin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Flucloxacillin: From Staphylococcal Infections to Conjunctivitis

## One-Sentence Summary

Flucloxacillin is an anti-staphylococcal beta-lactam antibiotic. The SAHPRA indication text was not supplied in the input, so "staphylococcal infections" reflects the drug class rather than a registered label.
The TxGNN model predicts it may be effective for **conjunctivitis**, but there are **0 clinical trials** and only **2 indirectly related publications** (both reviews, neither testing flucloxacillin in conjunctivitis).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied SAHPRA data; staphylococcal infections is inferred from the drug class |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 6 (5 listed in the data) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Flucloxacillin belongs to the anti-staphylococcal beta-lactam class. It is expected to act by inhibiting bacterial cell-wall synthesis, so activity against *Staphylococcus aureus*-related bacterial conjunctivitis is biologically plausible.

The linked literature does not test this directly. The staphylococcal scalded skin syndrome (SSSS) review lists conjunctivitis as a clinical feature of a staphylococcal toxin-mediated disease. The second paper, on atypical herpes simplex presentations, is unrelated to flucloxacillin.

The 99.84% score is a graph-based prediction only. A second entry, "conjunctivitis (disease)", is a duplicate concept with the same single supporting paper, so it should not be counted as an independent signal.

One practical point: the registered South African products are oral tablets, capsules and a suspension. None of the listed products is an ophthalmic preparation, so route compatibility for a topical eye indication is unresolved.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12627992](https://pubmed.ncbi.nlm.nih.gov/12627992/) | 2003 | Review | American Journal of Clinical Dermatology | Diagnosis and management of staphylococcal scalded skin syndrome. Conjunctivitis is mentioned as a possible early sign. It does not evaluate flucloxacillin for conjunctivitis. |
| [1286123](https://pubmed.ncbi.nlm.nih.gov/1286123/) | 1992 | Review | International Journal of STD & AIDS | Atypical presentations of herpes simplex virus infection. No abstract is available, and the paper is not relevant to flucloxacillin. |

## South Africa Market Information

The data lists 5 of the 6 registrations. Manufacturer and approved indication text were not provided, and Essential Medicines List status is not available in the data.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. A50/2.6.5/0687 | Septapen | Tablet |
| Reg. No. 44/20.1.2/0816 | Flucloxacillin 250 oethmaan | Capsule |
| Reg. No. J/20.1.2/0437 | Suprapen 500 | Capsule |
| Reg. No. Z/20.1.2/0354 | Megapen S | Suspension |
| Reg. No. 27/20.1.2/0106 | Macropen | Capsule |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug interaction records were found in the queried source. Publications linked to the other predicted indications (rheumatoid arthritis) report the following:
- **Agranulocytosis:** a case report, with relapse on re-introduction of flucloxacillin.
- **Stevens-Johnson syndrome / toxic epidermal necrolysis:** a fatal case (2025) attributed to doxycycline or flucloxacillin.
- **Methotrexate:** two small studies found no clinically significant pharmacokinetic interaction.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible for staphylococcal bacterial conjunctivitis. However, there are no trials, and the only linked literature is indirect. The pack classifies this as a research question, not an actionable repurposing candidate. Licensed oral forms are also a poor fit for an eye indication.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (indications, warnings, contraindications), which is currently a blocking gap
- Mechanism of action data (e.g. from DrugBank)
- Direct evidence for flucloxacillin in bacterial conjunctivitis (clinical trials or comparative studies)
- Assessment of route and formulation, since only oral and suspension products are registered
- A review of the safety signals above (agranulocytosis, SJS/TEN)
- Merging the duplicate "conjunctivitis" entries in downstream reporting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

