---
layout: default
title: Ivermectin
parent: 僅模型預測 (L5)
nav_order: 273
evidence_level: L5
indication_count: 10
---

# Ivermectin
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

Using the evidence pack as given — all 10 candidate indications for Ivermectin carry `evidence_level: L5`, `decision_stage: S0`, and `recommendation: Hold`, so I'm writing this as a cautionary/negative-signal report rather than forcing a positive framing.

# Ivermectin: From Parasitic Infections to Vulvovaginal Candidiasis

## One-Sentence Summary

> Ivermectin is an avermectin-class antiparasitic agent, and its documented pharmacology has no known mechanism against fungal pathogens.
> The TxGNN model predicts a possible link to **Vulvovaginal Candidiasis** with a **99.95%** prediction score,
> but this is currently supported by **0 clinical trials** and **0 relevant publications**, and the drug's own mechanism-of-action profile argues against biological plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parasitic infections (specific approved-indication text not available — drug is not registered in South Africa) |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 (model prediction only, no supporting clinical or observational studies) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Structured mechanism-of-action data for Ivermectin was not available in this evidence pack. Based on the mechanistic notes attached to each candidate indication, Ivermectin is an avermectin-class antiparasitic that acts by binding invertebrate glutamate-gated chloride channels, causing paralysis and death of the target parasite. This is a channel-binding mechanism specific to invertebrate nervous systems.

Candida infections, by contrast, are fungal, and susceptible to agents acting on ergosterol synthesis or β-glucan cell wall synthesis — pathways structurally and mechanistically unrelated to Ivermectin's target. The evidence pack's own rationale for every one of the 10 ranked candidates (vulvovaginal candidiasis, esophageal candidiasis, HPV infection, vulvovaginitis, congenital/neonatal candidiasis, *C. glabrata*, postmenopausal atrophic vaginitis, invasive candidiasis, vulvitis) states there is **no established mechanistic link** to Ivermectin's known pharmacology.

The consistent assessment across all 10 candidates is that the high TxGNN scores likely reflect clustering of "infection"-related nodes in the knowledge graph, rather than genuine pharmacological signal. Two candidates carry attached literature (PMID 35835488, PMID 10098288), but both concern Ivermectin's established use for helminth/mite infections in immunocompromised patients — background comorbidity context, not evidence of antifungal or antiviral efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Ivermectin is currently **not marketed** in South Africa under this evidence pack, with **0 SAHPRA registrations** on file. No product, dosage form, or approved-indication data is available to tabulate.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note: the underlying evidence pack flags TFDA/label warnings and contraindications as a **Blocking** data gap (DG001) — this alone is sufficient to prevent any safety pre-assessment (S1 stage) regardless of the efficacy question.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (vulvovaginal candidiasis) has no clinical trial or literature support, and Ivermectin's documented mechanism of action has no known relevance to fungal pathogens. All 10 candidate indications in this evidence pack carry the lowest evidence tier (L5) and are already flagged "Hold" by the underlying scoring.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information / label warnings and contraindications (currently a Blocking data gap)
- Confirmed original approved indication(s) and formal mechanism-of-action documentation for Ivermectin
- If this signal is to be pursued further: in-vitro/preclinical antifungal or antiviral activity data, since no current mechanistic or clinical rationale supports advancing to a safety review stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

