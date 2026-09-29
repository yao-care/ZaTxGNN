---
layout: default
title: Colchicine
parent: Moderate Evidence (L3-L4)
nav_order: 145
evidence_level: L4
indication_count: 10
---

# Colchicine
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

# Colchicine: From Gout and Familial Mediterranean Fever to Plasmodium falciparum Malaria

## One-Sentence Summary

Colchicine is an established oral drug, described in the literature mainly for gout and familial Mediterranean fever (FMF).
The TxGNN model predicts it may be effective for **Plasmodium falciparum malaria**,
but there are **0 clinical trials** and only **6 publications**, all laboratory or observational work, and none of them tests colchicine itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data; literature describes gout and FMF |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Colchicine is a well-known tubulin binder that disrupts microtubule polymerisation. Several laboratory studies show that compounds binding to the parasite's cytoskeleton, including tubulin, can inhibit *P. falciparum* growth in vitro. This is the likely basis for the model's prediction.

The link is weak for three reasons:
- The retrieved papers mostly study other compounds (curcumin, tubulozoles) or cytoskeletal binders in general. One 1990 study notes that colcemid, a colchicine-related compound, affected parasite protein synthesis in a similar way to tubulozoles, but it is not a direct colchicine result.
- Colchicine has a narrow therapeutic index, so concentrations high enough to act on the parasite may be toxic to the host.
- Many effective antimalarials already exist, so the need for a new candidate is low.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro | PLoS One | Curcumin disrupts *P. falciparum* microtubules, giving indirect support to tubulin as a parasite target |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In vitro | Mol Cell Biol | Expressing the parasite *pfmdr1* gene in mammalian cells increased chloroquine susceptibility; relates to drug resistance, not colchicine |
| [2221861](https://pubmed.ncbi.nlm.nih.gov/2221861/) | 1990 | In vitro | Antimicrob Agents Chemother | Tubulozoles reduced parasite protein synthesis; colcemid had a similar effect |
| [2670249](https://pubmed.ncbi.nlm.nih.gov/2670249/) | 1989 | In vitro | Cell Biol Int Rep | Tubulin-binding compounds were active against *P. falciparum*; parasite tubulin appears different from mammalian tubulin (also indexed as PMID 2655935) |
| [6362934](https://pubmed.ncbi.nlm.nih.gov/6362934/) | 1984 | Observational | Clin Exp Immunol | Antibodies to intermediate filaments were found in 82% of 78 acute malaria patients; not a treatment study |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| C665 (ACT 101/1965) | Colchicine houde | Tablet | Not stated in supplied data |
| 41/3.3/0260 | Aspen colchicine ds | Tablet | Not stated in supplied data |
| C0822 (ACT 101) | Aspen colchicine | Tablet | Not stated in supplied data |

All three products are oral tablets. Essential Medicines List (EML) status is not included in the supplied data.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The literature in the Evidence Pack adds that colchicine has a narrow therapeutic index with no clear line between non-toxic, toxic and lethal doses. Accidental toxicity is common and often has a poor outcome ([PMID 20586571](https://pubmed.ncbi.nlm.nih.gov/20586571/)). This is a major concern for any use at higher antiparasitic doses.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score and indirect laboratory findings on other compounds. There are no clinical trials and no colchicine-specific antimalarial data, and its narrow safety margin and the availability of effective antimalarials weigh against further work.

**To proceed, the following is needed:**
- Colchicine-specific in vitro data against *P. falciparum*, including resistant strains, with a comparison of effective concentrations against human-tolerable exposure
- The SAHPRA package insert warnings and contraindications (currently a blocking data gap)
- Mechanism of action data from DrugBank

**Note:** The second-ranked prediction, familial Mediterranean fever (score 99.38%, evidence level L3, Proceed with Guardrails), is already the standard use of colchicine rather than true repurposing. The supplied evidence for it is reviews and a single-centre series, with no colchicine RCT.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

