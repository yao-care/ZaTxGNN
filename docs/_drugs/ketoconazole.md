---
layout: default
title: Ketoconazole
parent: Model Prediction Only (L5)
nav_order: 281
evidence_level: L5
indication_count: 1
monitor_inn: "KETOCONAZOLE"
predicted_indications: ["acne (disease)"]
last_modified_at: 2026-10-27
description: "Ketoconazole: predicted new indication acne (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Ketoconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Ketoconazole: azole antifungal (CYP-inhibiting imidazole) → acne (disease)
{: .text-alpha }

## One-Sentence Summary

Ketoconazole is an azole antifungal that is registered in South Africa as single-ingredient topical and other products.
The TxGNN model predicts it may be useful for **acne (disease)**, but the supporting evidence is thin: **1 clinical trial** (topical, active but not yet reporting) and **no published study that directly tests ketoconazole in acne in patients**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | acne (disease) |
| TxGNN Prediction Score | 0.9980 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 2 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. The reasoning below rests on general pharmacology of azole antifungals rather than on a supplied record.

Ketoconazole inhibits *Malassezia* (*Pityrosporum*) yeasts, which have been linked to folliculitis and acne-like eruptions, including neonatal *Malassezia* pustulosis. At higher systemic doses it also inhibits steroid-synthesis enzymes (such as CYP17A1), lowering androgen production, which could matter in hyperandrogenic acne, for example in polycystic ovary syndrome. Laboratory work also reports that it inhibits the growth and lipase activity of *Cutibacterium (Propionibacterium) acnes*, the bacterium involved in acne inflammation.

These are plausible links, but they remain mechanistic or laboratory observations. The high TxGNN score is a computational ranking only and is not clinical evidence. Systemic use for acne would also be limited by serious safety concerns (see below), so any realistic exploration would be topical.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07237763](https://clinicaltrials.gov/study/NCT07237763) | Not applicable | Active, not recruiting | 52 | Randomised comparison of topical ketoconazole 2% cream vs topical adapalene 2% cream in mild comedonal and papulopustular acne over about 12 weeks; no results available yet |

No SANCTR or PACTR registrations were identified in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28111792](https://pubmed.ncbi.nlm.nih.gov/28111792/) | 2017 | Laboratory study | Microbiol Immunol | Ketoconazole inhibits *P. acnes* lipase activity and growth, suggesting a possible alternative for acne |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | Laboratory study | Biol Pharm Bull | In vitro activity of azole antifungals against *P. acnes* isolates from acne patients |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Clinical series | Clin Exp Dermatol | *Pityrosporum* folliculitis is often misdiagnosed as acne vulgaris; diagnosis and treatment trials in 62 patients |
| [8629828](https://pubmed.ncbi.nlm.nih.gov/8629828/) | 1996 | Case report | Arch Dermatol | Neonatal *Malassezia furfur* pustulosis associated with acne-like facial eruptions |
| [8255067](https://pubmed.ncbi.nlm.nih.gov/8255067/) | 1993 | Review | Keio J Med | *Pityrosporum ovale* in skin diseases, including folliculitis and seborrhoeic dermatitis |
| [12566804](https://pubmed.ncbi.nlm.nih.gov/12566804/) | 2003 | Review | Dermatology | Systemic acne treatment overview (not specific to ketoconazole) |

The other retrieved publications concern related topics (polycystic ovary syndrome, Cushing's syndrome, adapalene, infant rashes) and do not test ketoconazole in acne.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 33/20.2.2/0503 | Ketazol | Cream | Not recorded in the local data |
| Reg. No. 34/20.2.2/0244 | Adco-dermed | Sha | Not recorded in the local data |

Both registrations are single-ingredient products and currently valid. Essential Medicines List status is not recorded in the data compiled for this report.

---

## Safety Considerations

- **Contraindication-type conditions (database associations, not label text):** long QT syndrome (including familial), torsades de pointes, liver disease, gallbladder disease, adrenocortical insufficiency/Addison disease, skin atrophy, telangiectasia and related capillary disease, peripheral vascular disease, and achlorhydria. These should be verified against the SAHPRA Professional Information.
- **Drug Interactions:** 100 interactions are recorded. Major-level examples include loperamide, triamcinolone and budesonide. Moderate examples include famotidine, ranitidine, omeprazole, rabeprazole, hydrocortisone, dexamethasone, betamethasone, pioglitazone, aprepitant and alosetron. Acid-suppressing drugs are notable because they may reduce oral ketoconazole absorption.
- **Systemic-use concerns:** serious hepatotoxicity, adrenal suppression and QT prolongation limit any systemic use for acne.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings, and report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only trial directly addressing acne is a small, topical, active-comparator study without results, and the remaining support is laboratory or indirect. The very high model score is not clinical evidence, and systemic use carries significant safety risks.

**To proceed, the following is needed:**
- Results from NCT07237763 and any further randomised trials of topical ketoconazole in acne
- Mechanism of action data and confirmation of the approved label indications and warnings from the SAHPRA package inserts
- Clarity on the route of administration (topical only) and a comparison against current first-line acne treatments in the South African setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

