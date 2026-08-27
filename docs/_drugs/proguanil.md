---
layout: default
title: Proguanil
parent: 僅模型預測 (L5)
nav_order: 380
evidence_level: L5
indication_count: 10
---

# Proguanil
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

Using the report template directly — this is a single well-defined content-generation task, not one that needs a broader skill.

# Proguanil: From Malaria Chemoprophylaxis to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Proguanil is a biguanide antimalarial, traditionally used (alone or combined with atovaquone) for malaria chemoprophylaxis. The TxGNN model predicts a possible link to **Smouldering Systemic Mastocytosis**, but this direction is currently supported by **0 clinical trials** and **0 publications** — it rests solely on a statistical association in the TxGNN knowledge graph, and the evidence pack's own rationale states there is no known pharmacological link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malaria chemoprophylaxis (biguanide antimalarial class) — no South African regulatory indication text available, product not marketed |
| Predicted New Indication | Smouldering Systemic Mastocytosis |
| TxGNN Prediction Score | 92.12% |
| Evidence Level | L5 (model prediction only; no clinical or literature evidence) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Proguanil has not yet been retrieved from DrugBank (data gap). Based on general pharmacological knowledge, Proguanil is a biguanide antimalarial: its active metabolite cycloguanil inhibits the malaria parasite's dihydrofolate reductase (DHFR), blocking folate synthesis and parasite replication. This mechanism is well established for malaria prophylaxis and treatment, most often as part of the atovaquone-proguanil combination.

Smouldering systemic mastocytosis, by contrast, is driven mainly by activating KIT tyrosine kinase mutations (commonly KIT D816V) in mast cells; current investigational and approved therapies (e.g. midostaurin, avapritinib) act directly on this kinase pathway. Proguanil's antifolate/antimalarial mechanism has no known interaction with KIT signalling or mast cell biology.

The evidence pack's own repurposing rationale is explicit on this point: it states there is no pharmacological support for a mechanistic link, and describes the prediction as a pure knowledge-graph association. This should be read as a low-confidence, hypothesis-generating signal only, not a lead with biological plausibility behind it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Proguanil is currently **not marketed** in South Africa, with no SAHPRA product registrations on record in this evidence pack. No dosage form or approved-indication data is therefore available for the local market.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no supporting clinical trials or literature, the model's own mechanistic rationale finds no pharmacological plausibility, the score is L5 (graph prediction only), and the product is not currently registered or marketed in South Africa. This does not meet the threshold to advance.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data from DrugBank (currently a data gap)
- Regulatory PI/labelling safety data — warnings and contraindications (currently a blocking data gap)
- Any preclinical or mechanistic evidence connecting antifolate/antimalarial activity to KIT-driven mast cell disease biology
- Confirmation of SAHPRA registration status or an import/access pathway, since the product is not currently marketed in South Africa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

