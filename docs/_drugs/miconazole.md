---
layout: default
title: Miconazole
parent: 僅模型預測 (L5)
nav_order: 316
evidence_level: L5
indication_count: 10
---

# Miconazole
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

# Miconazole: From Fungal Infections to Acne (Disease)

## One-Sentence Summary

> Miconazole is a long-established imidazole antifungal used to treat cutaneous and mucosal fungal infections. TxGNN's top-ranked prediction proposes potential efficacy for **Acne**, but this is currently supported by only **1 clinical trial** (suspended, low relevance) and **4 publications**, none of which directly test miconazole in acne. A lower-ranked but far better-supported candidate in this same evidence pack — superficial mycosis — has notably stronger evidence and a much more direct mechanistic fit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on SAHPRA file (product not currently registered/marketed in South Africa); globally recognized as an antifungal for cutaneous and mucosal fungal infections |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L4 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for miconazole is not available in this evidence pack. Based on general pharmacological knowledge, miconazole is an imidazole-class antifungal whose established mechanism involves inhibition of fungal ergosterol synthesis (14α-demethylase) and fungal peroxidases, disrupting the fungal cell membrane. Its efficacy in fungal skin and mucosal infections is well proven through decades of clinical use.

For the top-ranked predicted indication, **acne**, the supporting rationale in this evidence pack notes in-vitro data showing miconazole has inhibitory activity against *Propionibacterium acnes* and *Malassezia* — organisms implicated in acneiform folliculitis — giving a partial antimicrobial/antifungal rationale. However, this mechanism only partially overlaps with the primary pathophysiology of acne vulgaris (sebum overproduction, follicular inflammation, and *C. acnes* bacterial proliferation), so the link is indirect rather than core. The single associated clinical trial tested an unrelated combination product (not miconazole alone) and was suspended, further weakening the case.

Notably, several lower-ranked candidates in this pack (superficial mycosis, tinea profunda, Majocchi granuloma, blastomycosis) sit squarely within miconazole's known antifungal mechanism and are supported by comparative clinical studies — these represent more clinically actionable "repurposing" signals than the acne prediction, even though they scored lower on TxGNN's novelty-weighted ranking.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Compared a combination cream (beclometasone 0.025% + gentamicin 0.1% + clotrimazole 1%) — not miconazole — in patients with contaminated dermatosis/acne-like lesions. Trial suspended; graded C relevance (different drug combination, cannot attribute efficacy to miconazole). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Clinical/Split-face study | Skin Research and Technology | Split-face assessment of catamenial acne management; does not directly test miconazole. |
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Review | Expert Opinion on Pharmacotherapy | Reviews miconazole's broader effects on skin disorders as a "time-honored" imidazole antifungal. |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Cohort | Clinical and Experimental Dermatology | Describes Pityrosporum (Malassezia) folliculitis, frequently misdiagnosed as acne vulgaris; supports differential-diagnosis rationale rather than direct treatment evidence. |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro | Biological & Pharmaceutical Bulletin | In-vitro activity of azole antifungals, including miconazole, against *Propionibacterium acnes* isolates. |

---

## South Africa Market Information

No SAHPRA registrations are on file for this product (`total_licenses: 0`, market status: Not Marketed), so no registration table can be produced. Should this candidate advance, a South African market-entry pathway (new registration or import authorization) would need to be established before clinical use.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: key warnings, contraindications, and drug–drug interaction data were not available in this evidence pack — this is flagged internally as a **Blocking** data gap that must be closed before any safety pre-assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (acne) rests on L4 evidence — a single suspended, low-relevance trial testing an unrelated combination product, plus in-vitro and indirect literature. The mechanistic overlap with acne pathophysiology is partial, not core. Combined with the absence of any SAHPRA registration and a Blocking gap in label/safety data, this candidate is not ready to advance past a research question.

**To proceed, the following is needed:**
- Official SAHPRA/manufacturer Professional Information (PI) — warnings, contraindications, DDI (Blocking gap)
- Confirmed mechanism-of-action data via DrugBank (High-priority gap)
- A dedicated trial testing miconazole (not combination products) specifically in acne
- Consideration of re-scoping this candidate toward **superficial mycosis** (evidence level L2, decision stage S2, "Proceed with Guardrails"), which has a completed comparative cohort study (miconazole vs. clotrimazole) and a direct mechanistic fit — a more immediately actionable repurposing signal within this same evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

