---
layout: default
title: Miconazole
parent: Moderate Evidence (L3-L4)
nav_order: 322
evidence_level: L4
indication_count: 10
---

# Miconazole
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

# Miconazole: From Topical Antifungal Use to Acne

## One-Sentence Summary

Miconazole is an azole antifungal, and in South Africa it is registered mainly as topical creams and gels.
The TxGNN model predicts it may be effective for **acne**, but the support is thin: **1 suspended clinical trial** (a multi-drug combination that involves clotrimazole, not miconazole) and **4 publications**, of which only one is a clinical study.
This is a research question, not a treatment recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | The registration records give no approved-indication text. Miconazole is a topical azole antifungal. |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 9 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Miconazole is an azole antifungal that disrupts fungal ergosterol synthesis and membrane integrity. Its efficacy against superficial fungal infections is well established, and topical safety is generally well characterised.

Three lines of reasoning link it to acne:
- **Antibacterial activity:** an in vitro study found that azole antifungals are active against *Propionibacterium acnes* (now *Cutibacterium acnes*), isolated from patients with acne vulgaris (PMID 20045949).
- **Anti-inflammatory effects:** a 2008 review describes reported effects of miconazole on skin disorders beyond fungal infection (PMID 18627330).
- **Malassezia folliculitis:** this condition looks like acne and is often misdiagnosed as acne vulgaris (PMID 8593718). Some of the model's signal may therefore reflect fungal folliculitis rather than true acne.

Laboratory activity against the acne bacterium and clinical benefit in acne are different things. No study in the Evidence Pack shows that miconazole improves acne in patients.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01218256) | Phase 2/3 | Suspended | 80 | Compared a combination of beclomethasone, gentamicin and clotrimazole cream in contaminated dermatosis with bilateral symmetrical lesions. The combination cannot isolate any single drug's effect, the drug involved is clotrimazole rather than miconazole, and no results are available. |

No SANCTR or PACTR registrations were found in the Evidence Pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Clinical study (split-face) | Skin Res Technol | Split-face assessment in mild inflammatory catamenial acne. The retrieved abstract does not report results or state whether miconazole was tested. |
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Review | Expert Opin Pharmacother | Reviews the multiple effects of miconazole nitrate on skin disorders. |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro study | Biol Pharm Bull | Azole antifungals tested against *P. acnes* isolates from acne vulgaris patients, as a possible alternative given rising antibiotic resistance. |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Clinical study | Clin Exp Dermatol | 62 patients with Malassezia (Pityrosporum) folliculitis, which is frequently misdiagnosed as acne vulgaris. |

---

## South Africa Market Information

Miconazole has 9 SAHPRA registrations. The 5 main ones are listed below. The records contain no approved-indication text or Essential Medicines List status for these products.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 34/13.9.2/0182 | Dermazole | Cream |
| Reg. No. 36/20.2.2/0233 | Vari miconazole 2% | "Geo" (as recorded) |
| Reg. No. 33/13.9.2/0124 | Covarex | Cream |
| Reg. No. 36/13.9.2/0509 | Sutharex Cream | Cream |
| Reg. No. X/13.12/292 | Acneclear | Cream |

The full record set also includes a vaginal cream.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the clinical evidence is very weak. The only trial is suspended, has no results, and involves clotrimazole in a combination product. The publications show laboratory activity against the acne bacterium but no proof of clinical benefit. Part of the signal may come from Malassezia folliculitis being mistaken for acne. Safety data from the SAHPRA package insert have not been reviewed.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications, which are currently a blocking gap for safety screening
- The labelled indications for the registered products and their EML status
- Detailed mechanism of action data from DrugBank
- Comparative clinical data in acne, with Malassezia folliculitis excluded or analysed separately
- Confirmation that the acne-related product (Acneclear) is not already registered with an acne-related claim

**Related note:** the model also ranks *superficial mycosis* highly (rank 7). This is very likely an existing labelled antifungal use rather than true repurposing, and it has the strongest evidence in the pack, including a 1989 comparative study of miconazole versus clotrimazole. Its label status should be verified before it is treated as a candidate. The other predicted indications (deep or hair-shaft dermatophyte infections, blastomycosis, gastrin secretion abnormality, papillary conjunctivitis) have weak or historical evidence and should stay on Hold.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

