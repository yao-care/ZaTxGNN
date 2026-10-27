---
layout: default
title: Griseofulvin
parent: Model Prediction Only (L5)
nav_order: 249
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Griseofulvin: predicted new indication Myiasis (evidence level L5). Approved use: Tinea pedis, tinea corporis…"
monitor_inn: "Griseofulvin"
predicted_indications: ["myiasis", "furuncular myiasis", "wound myiasis", "creeping myiasis", "echinococcus granulosus infectious disease", "toxoplasmosis", "alveolar echinococcosis", "blastomycosis", "Bacteroidaceae infectious disease"]
---

# Griseofulvin
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

## Griseofulvin: From Tinea Infections to Myiasis
{: .text-alpha }

## One-Sentence Summary

Griseofulvin is an oral antifungal originally used for dermatophyte infections such as tinea pedis, tinea corporis, tinea unguium and tinea of the scalp or beard.
The TxGNN model predicts it may be effective for **myiasis** (score 99.41%), but there are **no clinical trials** and **no publications** supporting this direction.
The prediction is model-derived only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, tinea corporis, tinea unguium and other dermatophyte infections (the SAHPRA registration record has no indication text) |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Griseofulvin is a known antifungal that is generally understood to disrupt fungal microtubule function and mitosis. Its efficacy in dermatophyte infections is established.

Myiasis is an infestation by fly larvae, a parasitic condition and not a fungal one. No plausible shared target between griseofulvin and fly larvae has been identified. Standard management is debridement and antiparasitic or larvicidal agents (for example ivermectin in some forms). The same score (99.34%) appears for furuncular, wound and creeping myiasis, which suggests the signal comes from the structure of the knowledge graph rather than disease-specific biology.

Other top-ranked predictions are also unsupported:
- **Other myiasis subtypes** (furuncular, wound, creeping): model prediction only.
- **Echinococcosis** (granulosus and alveolar): a loose tubulin-related hypothesis exists, since albendazole also targets tubulin, but griseofulvin acts on fungal microtubules and no helminth data are available.
- **Toxoplasmosis and Bacteroidaceae infection**: no mechanism or data. Griseofulvin has no recognised antibacterial activity.
- **Cutaneous candidiasis** (score 98.71%): biologically closest to the approved uses, but griseofulvin is generally considered ineffective against *Candida*. The publications retrieved are reviews of superficial mycoses and of comparator antifungals, and none show griseofulvin efficacy in candidiasis.
- **Blastomycosis** (score 97.08%): griseofulvin is not an established treatment. Amphotericin B and itraconazole are standard. Only three old, general reviews or notes (1963-1994) were found.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for myiasis.

---

## Literature Evidence

Currently no related literature available for myiasis.

For context, the closest-ranked prediction with literature is cutaneous candidiasis. The publications retrieved are reviews or general articles and give only indirect evidence:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15571501](https://pubmed.ncbi.nlm.nih.gov/15571501/) | 2004 | Review | Dermatologic Therapy | Therapy of common superficial fungal infections. Onychomycosis often needs systemic griseofulvin, itraconazole or terbinafine. |
| [8763460](https://pubmed.ncbi.nlm.nih.gov/8763460/) | 1996 | Review | Br J Dermatol | Cutaneous mycoses in children. Griseofulvin has been the main treatment in children but is only fungistatic and may cause interactions. |
| [10439936](https://pubmed.ncbi.nlm.nih.gov/10439936/) | 1999 | Review | Drugs | Terbinafine update in superficial mycoses (comparator antifungal). |
| [8706596](https://pubmed.ncbi.nlm.nih.gov/8706596/) | 1996 | Review | Drugs | Itraconazole in superficial fungal infections (comparator antifungal). |
| [1372222](https://pubmed.ncbi.nlm.nih.gov/1372222/) | 1992 | Review | Drugs | Terbinafine pharmacology and therapeutic potential in superficial mycoses. |
| [34898894](https://pubmed.ncbi.nlm.nih.gov/34898894/) | 2021 | Review | J Obstet Gynaecol India | Risks and precautions of common antifungal drugs in pregnancy. |
| [8077517](https://pubmed.ncbi.nlm.nih.gov/8077517/) | 1994 | Review | J Am Acad Dermatol | Treatment of tropical mycoses (retrieved for blastomycosis). |

None of these show griseofulvin efficacy for the predicted new indications.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| K/20.1.7/0718 | Microcidal | Tablet (oral) | Not available in the data compiled for this report |

Griseofulvin has one valid single-ingredient registration in South Africa and none cancelled. The data compiled for this report do not show Essential Medicines List (EML) status.

---

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these come from the TxGNN knowledge graph, not from label text, and must be verified against the Professional Information):
- Liver failure
- Porphyria (including inherited porphyria and porphyrin metabolism disease)
- Systemic lupus erythematosus (including paediatric SLE)
- Substance abuse/dependence
- Neutropenia and agranulocytosis (including cyclic hematopoiesis, severe congenital neutropenia and related congenital forms, adult idiopathic neutropenia, constitutional neutropenia)

**Drug Interactions:** The interaction screen returned 100 interacting drugs in total. The 20 listed are mostly Moderate, with a few Minor. Notable examples:
- **Anticoagulants and antiplatelets (Moderate):** warfarin, dicoumarol, apixaban, rivaroxaban, ticagrelor
- **Antidiabetic agents:** repaglinide, saxagliptin, linagliptin (Moderate); liraglutide (Minor)
- **Antimalarials and antiparasitics (Moderate):** artemether, mefloquine, praziquantel
- **Antiemetics (Moderate):** aprepitant, rolapitant
- **Other (Moderate):** eliglustat, naloxegol, nitisinone, macimorelin, fostamatinib
- **Acetylsalicylic acid:** Minor

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The myiasis prediction rests on the TxGNN score alone, with no clinical trials, no literature and no plausible mechanism. Established treatments exist, and the identical scores across myiasis subtypes point to a graph artefact rather than real biology.

**To proceed, the following is needed:**
- Mechanism of action data for griseofulvin, and a rationale for activity against fly larvae
- Any preclinical or in vitro evidence of antiparasitic activity
- The SAHPRA package insert (warnings, contraindications, approved indications), which is a blocking gap for safety screening
- If a different direction is of interest, a targeted review of the closer fungal candidates (cutaneous candidiasis, blastomycosis), noting that griseofulvin is not generally effective against *Candida* and is not an established treatment for blastomycosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

