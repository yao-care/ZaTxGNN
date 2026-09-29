---
layout: default
title: Terbinafine
parent: Model Prediction Only (L5)
nav_order: 438
evidence_level: L5
indication_count: 10
---

# Terbinafine
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

# Terbinafine: From Fungal Skin Infections to Creeping Myiasis

## One-Sentence Summary

Terbinafine is an allylamine antifungal marketed in South Africa as oral and topical products. The registry data supplied do not state its approved indication, so "fungal skin infections" here comes from general pharmacology.
The TxGNN model ranks **creeping myiasis** (a fly-larva skin infestation) first, but there are **0 clinical trials and 0 supporting publications** for it. The pack's own analysis judges it a likely knowledge-graph artifact.
Better-supported predictions are **tinea manuum** and **superficial mycosis**, which stay closer to terbinafine's antifungal mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA data provided (all approved-indication fields are empty) |
| Predicted New Indication | Creeping myiasis (rank 1 of 10 predictions) |
| TxGNN Prediction Score | 96.74% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 |
| Recommended Decision | Hold (for the top-ranked prediction; see the table below for others) |

### All Predictions at a Glance

| Rank | Predicted Indication | Score | Evidence Level | Decision |
|---|---|---|---|---|
| 1 | Creeping myiasis | 96.74% | L5 | Hold |
| 2 | Furuncular myiasis | 96.74% | L5 | Hold |
| 3 | Wound myiasis | 96.74% | L5 | Hold |
| 4 | Myiasis | 96.21% | L5 | Hold |
| 5 | Cutaneous candidiasis | 95.04% | L4 | Research question |
| 6 | Toxoplasmosis | 94.79% | L5 | Hold |
| 7 | Blastomycosis | 91.76% | L4 | Research question |
| 8 | Tinea manuum | 90.11% | L3 | Proceed with Guardrails |
| 9 | Echinococcus granulosus infectious disease | 86.06% | L5 | Hold |
| 10 | Superficial mycosis | 84.47% | L3 | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the pack. From general pharmacology, terbinafine inhibits fungal squalene epoxidase, an enzyme in ergosterol synthesis. This is fungicidal against dermatophytes.

**The top-ranked myiasis predictions are not mechanistically plausible.** Fly larvae have no comparable target, and the high scores (about 96–97%) probably reflect shared skin-infection neighbours in the knowledge graph.
The only retrieved papers are case reports of myiasis co-occurring with fungal infection (chromoblastomycosis) or a furuncle that did not respond to several drugs. Terbinafine is only mentioned as one failed treatment, so these are not evidence of efficacy.

**The lower-ranked fungal predictions are plausible.** Tinea manuum and superficial mycosis are caused mainly by *Trichophyton* dermatophytes, which are terbinafine's core target. Cutaneous candidiasis and blastomycosis are biologically possible but weaker: terbinafine is variable and largely fungistatic against *Candida*, and itraconazole and amphotericin B remain standard for blastomycosis.
Toxoplasmosis and echinococcosis involve protozoan and cestode biology with no established terbinafine target.

---

## Clinical Trial Evidence

The only registered trial found across all ten predictions relates to superficial mycosis (rank 10). None were found for the top-ranked myiasis prediction.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05578950](https://clinicaltrials.gov/study/NCT05578950) | Phase 1 (as registered) | Completed | 100 | Pulse oral itraconazole vs continuous oral terbinafine in onychomycosis. Terbinafine is the comparator arm, not the investigational agent. The Phase 1 label looks inconsistent with the design, so check the registry record. |

---

## Literature Evidence

No literature supports terbinafine for creeping myiasis. The table combines the most relevant papers across the predictions.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1911319](https://pubmed.ncbi.nlm.nih.gov/1911319/) | 1991 | Clinical study (placebo-controlled) | Br J Dermatol | 2-week oral terbinafine for moccasin tinea pedis and tinea manuum in 53 adults (28 evaluable) |
| [10940119](https://pubmed.ncbi.nlm.nih.gov/10940119/) | 2000 | Clinical study | Int J Dermatol | Tinea manus treated with 1-week itraconazole vs terbinafine |
| [15679673](https://pubmed.ncbi.nlm.nih.gov/15679673/) | 2005 | Case report | Mycoses | Tinea manuum bullosa cured clinically and mycologically with terbinafine 250 mg/day |
| [1372222](https://pubmed.ncbi.nlm.nih.gov/1372222/) | 1992 | Review | Drugs | Pharmacology and therapeutic potential in superficial mycoses; about 90% mycological cure in dermatophyte infections |
| [10439936](https://pubmed.ncbi.nlm.nih.gov/10439936/) | 1999 | Review | Drugs | Update on superficial mycoses; oral 250 mg/day achieves mycological cure in over 80% of dermatophyte infections; fungistatic against *C. albicans* |
| [9593126](https://pubmed.ncbi.nlm.nih.gov/9593126/) | 1998 | In vitro study | Antimicrob Agents Chemother | Activity against 350 cutaneous *Candida* isolates and other yeasts |
| [10886159](https://pubmed.ncbi.nlm.nih.gov/10886159/) | 2000 | Case report | Br J Dermatol | Paracoccidioidomycosis (South American blastomycosis) resolved on terbinafine; a distinct disease from North American blastomycosis |
| [38623728](https://pubmed.ncbi.nlm.nih.gov/38623728/) | 2024 | Review | Expert Opin Pharmacother | Rising antifungal resistance in dermatophytosis |
| [40613321](https://pubmed.ncbi.nlm.nih.gov/40613321/) | 2026 | Review | J Eur Acad Dermatol Venereol | *T. indotineae* epidemiology, resistance and stewardship |
| [25016125](https://pubmed.ncbi.nlm.nih.gov/25016125/) | 2014 | Case report | Turkiye Parazitol Derg | Furuncular myiasis unresponsive to several drugs including terbinafine; not evidence of efficacy |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. A40/20.2.2/0344 | Dermax 250 | Tablet (oral) | Not stated in data provided |
| Reg. No. 38/20.2.2/0148 | Terbicil | Cream (topical) | Not stated in data provided |
| Reg. No. 32/20.2.2/0564 | Lamisil derm gel | Gel (topical) | Not stated in data provided |
| Reg. No. Z/20.2.2/186 | Lamisil | Cream (topical) | Not stated in data provided |
| Reg. No. 42/20.2.2/0382 | Almatil | Cream (topical) | Not stated in data provided |

Essential Medicines List (EML) status could not be determined from the data provided.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

One safety-related point applies to the antifungal indications. Recent reviews document terbinafine-resistant dermatophytes (for example *Trichophyton indotineae* and resistant isolates in Japan), so susceptibility testing and antifungal stewardship are advised.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked myiasis predictions and the other L5 predictions). **Proceed with Guardrails** applies only to tinea manuum and superficial mycosis.

**Rationale:**
- The top four predictions are myiasis, which has no plausible mechanism, no trials, and no supporting literature. The high scores appear to be a knowledge-graph artifact.
- Tinea manuum and superficial mycosis have a plausible mechanism and supporting clinical literature, but no Phase 3 RCT was found. Use in dermatophytosis is probably established practice, and the empty original-indication field is probably a data gap.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications, approved indications, EML status). The pack marks this as a blocking gap for safety screening.
- Mechanism of action data from DrugBank.
- For tinea manuum and superficial mycosis: confirm the registry record for NCT05578950 and look for controlled trials, plus a local susceptibility and resistance surveillance plan.
- For cutaneous candidiasis and blastomycosis: comparative studies against azoles or polyenes before any further consideration.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

