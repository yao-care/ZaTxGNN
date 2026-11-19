---
layout: default
title: Griseofulvin
parent: Model Prediction Only (L5)
nav_order: 248
evidence_level: L5
indication_count: 5
monitor_inn: "Griseofulvin"
predicted_indications: ["myiasis", "furuncular myiasis", "creeping myiasis", "wound myiasis", "echinococcus granulosus infectious disease"]
last_modified_at: 2026-11-20
description: "Griseofulvin: predicted new indication Myiasis (evidence level L5). In South Africa: 6 SAHPRA registrations (6 valid)"
---

# Griseofulvin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Griseofulvin: Oral antifungal that disrupts fungal microtubules → Myiasis (myiasis)
{: .text-alpha }

## One-Sentence Summary

Griseofulvin is an oral antifungal medicine that acts on fungal cell division.
The TxGNN model predicts it may be effective for **myiasis** (fly larvae infestation of tissue), but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Myiasis (myiasis) |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 6 of 6; 2 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 6 (valid: 6, of which 2 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for griseofulvin: "The mechanism of griseofulvin consists of binding microtubular proteins, which are required for mitosis. […] The mechanism of griseofulvin consists of binding microtubular proteins, which are required for mitosis. Activity In Vivo Griseofulvin may be active against most strains of the following dermatophytes as described in the INDICATIONS AND USAGE section: Epidermophyton floccosum, Microsporum audouinii, Microsporum canis, Microsporum gypseum, Trichophyton crateriformis, Trichophyton gallinae, Trichophyton interdigitalis, Trichophyton megnini, Trichophyton mentagrophytes, Trichophyton rubrum, Trichophyton sulphureum, Trichophyton schoenleini, Trichophyton tonsurans and Trichophyton verrucosum." ([DailyMed: griseofulvin prescribing information, Sandoz Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98829d90-b289-4bec-a625-7af412a5cb2d), label version 2025-05-14; accessed 2026-11-19.) Griseofulvin is generally understood to be an antifungal that interferes with microtubule function and mitosis in fungi.

Myiasis is a parasitic infestation of tissue by fly larvae, which is a different kind of organism from fungi. No shared drug target or plausible mechanistic link is described in the data. The high TxGNN score (0.9941) is a model output only and has no clinical or published support. Related predictions of similar subtypes (furuncular, wound and creeping myiasis) carry identical scores, which suggests a shared model signal rather than disease-specific biology. Standard management of myiasis relies on wound care or removal of larvae and antiparasitic agents, and there is no rationale in the data for griseofulvin.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| K/20.1.7/0718 | Microcidal | tablet | Valid (status not confirmed by SAHPRA) |
| K/20.1.7/0719 | Microcidal | tablet | Valid (status not confirmed by SAHPRA) |
| K/20.1.7/218 | Microcidal - 125 | tablet | Valid |
| K/20.1.7/219 | Microcidal - 500 | tablet | Valid |
| A0371 | Fulcin 125 mg | Not recorded | Valid |

Showing 5 of 6 registrations (valid registrations first).

<!-- licenses:end -->

---

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 records; the main entries listed here are Moderate-level interactions with anticoagulants and antiplatelets (warfarin, apixaban, rivaroxaban, dicoumarol, ticagrelor), antidiabetic agents (saxagliptin, linagliptin, repaglinide), antiemetics (aprepitant, rolapitant), antimalarial/antiparasitic agents (artemether, mefloquine, praziquantel), and others (eliglustat, naloxegol, nitisinone, macimorelin, fostamatinib). Minor-level interactions include acetylsalicylic acid and liraglutide.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a model score, with no clinical trials, no literature and no plausible mechanistic link between a fungal-microtubule agent and fly larvae infestation. Evidence is at the lowest level (L5).

**To proceed, the following is needed:**
- Mechanism of action data for griseofulvin and any plausible target in fly larvae
- Preclinical (in vitro or in vivo) evidence of activity against myiasis-causing larvae
- Retrieval and review of the SAHPRA Professional Information for warnings and contraindications
- Comparison against established myiasis management (wound care, larval removal, antiparasitic agents) to define any added value

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not currently available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: griseofulvin prescribing information, Sandoz Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98829d90-b289-4bec-a625-7af412a5cb2d) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

