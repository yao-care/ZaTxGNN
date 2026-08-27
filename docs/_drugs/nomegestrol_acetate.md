---
layout: default
title: Nomegestrol Acetate
parent: 僅模型預測 (L5)
nav_order: 336
evidence_level: L5
indication_count: 10
---

# Nomegestrol Acetate
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

# Nomegestrol Acetate: From Hormonal Contraception/HRT to Candidiasis

## One-Sentence Summary

> Nomegestrol acetate is a progestin (progesterone receptor agonist), commonly used in combined hormonal contraceptives and menopausal hormone therapy — though no original-indication or MOA data is on file here.
> The TxGNN model's top-ranked prediction is **Candidiasis**, with a raw score of **98.78%**, but this is supported by **0 clinical trials** and **0 publications**, and the drug's own known pharmacology points the opposite direction (hormonal contraceptives are associated with *increased*, not decreased, candidiasis risk).
> This candidate should be treated as an unverified model output, not a repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (general knowledge: progestin used in hormonal contraception / HRT) |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 98.78% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged in this evidence pack as a High-severity data gap). Based on known pharmacology, nomegestrol acetate is a third-generation progestin, typically combined with an estrogen (e.g. 17β-estradiol) in oral contraceptives and hormone therapy.

The link between hormonal contraception and candidiasis is real, but it runs the opposite way to what would be needed to support this prediction: estrogen–progestin combinations are known to alter vaginal flora and are associated with **increased** vaginal candidiasis risk, not treatment of it. The rationale attached to this candidate in the evidence pack states this explicitly — no clinical trial or literature evidence supports a therapeutic hypothesis, and the biological direction argues against one.

This appears to be a case where TxGNN's graph-similarity scoring picked up a real drug–disease *association* (adverse effect / risk signal) and surfaced it as if it were a treatment candidate. The same pattern recurs elsewhere in this evidence pack: predictions for antithrombin deficiency, heparin cofactor 2 deficiency, and factor V–related thrombosis are all conditions for which progestin/estrogen therapy is a **contraindication**, not a treatment — and the one candidate with actual trial and literature evidence ("thrombotic disease," rank 9) shows the drug **increasing** venous thromboembolism (VTE) risk (per Bińkowska et al., 2022, PMID 36254131), again the opposite of a therapeutic signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(Note: two Phase 2/3 trials — NCT01656434, NCT01709318 — exist for nomegestrol acetate but concern contraceptive efficacy/safety, not candidiasis, and are not evidence for this indication.)*

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

No SAHPRA registrations are on record — market status is "Not marketed" with 0 licenses. No product, dosage form, or approved-indication data is available to summarise.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Additional context from this evidence pack (not from the drug's formal safety fields, but directly relevant):** literature retrieved for a different predicted indication (thrombotic disease) documents that estrogen–progestin combinations containing nomegestrol acetate carry a known venous thromboembolism risk (Bińkowska et al., 2022). This is a class-level safety signal worth carrying forward into any future evaluation of this drug, regardless of which indication is ultimately pursued.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (candidiasis) has zero supporting clinical trials or literature, and the drug's known pharmacology suggests it would worsen rather than treat this condition — this is a model-only (L5) signal with a mechanistically implausible direction.
- A Blocking-severity data gap exists (TFDA/SAHPRA product-label warnings and contraindications are entirely missing), which by itself prevents any initial safety screening (S1) regardless of indication.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) — warnings, contraindications, DDI (currently a Blocking data gap)
- Confirmed mechanism of action data from DrugBank (currently a High-severity data gap)
- Original approved indication(s) for nomegestrol acetate, to properly assess similarity to any new candidate
- If this candidate is pursued further, a targeted literature/trial search specifically testing nomegestrol acetate *against* candidiasis (not merely co-occurrence data), since none currently exists
- Given the recurring risk-not-benefit pattern across this drug's top 10 predictions, a broader review of whether TxGNN's output for this drug reflects genuine repurposing signal or adverse-effect associations misclassified as efficacy signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

