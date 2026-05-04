---
layout: default
title: Benserazide
parent: 僅模型預測 (L5)
nav_order: 60
evidence_level: L5
indication_count: 10
---

# Benserazide
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

# Benserazide: From Parkinson's Disease (Levodopa Adjunct) to Congenital Hypotrichosis Milia

---

## One-Sentence Summary

Benserazide is a peripheral aromatic L-amino acid decarboxylase (DOPA decarboxylase, DDC) inhibitor, classically combined with levodopa (as Madopar®) to enhance central levodopa bioavailability for Parkinson's disease treatment.
The TxGNN model predicts it may be effective for **Congenital Hypotrichosis Milia**,
with **0 clinical trials** and **0 publications** currently supporting this direction — placing confidence at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease (peripheral DDC inhibitor, combined with levodopa; from general knowledge — no SAHPRA registration data available) |
| Predicted New Indication | Congenital Hypotrichosis Milia |
| TxGNN Prediction Score | 98.44% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacological knowledge, Benserazide is a peripheral inhibitor of aromatic L-amino acid decarboxylase (AADC/DDC) — the enzyme responsible for converting L-DOPA to dopamine in peripheral tissues. It is used exclusively as a combination partner with levodopa, preventing peripheral dopamine synthesis and increasing central availability of levodopa. It has no independent therapeutic indication.

Congenital hypotrichosis milia is a rare genetic developmental disorder characterised by sparse hair and milia formation present at or near birth. The established genetic basis involves mutations in **ABCA5** and **ST14**, which disrupt keratinocyte differentiation and hair follicle structural integrity. These are fundamentally structural developmental defects, not receptor-signalling abnormalities, and there is no recognised mechanistic bridge between peripheral DDC inhibition and these genetic pathways.

The TxGNN knowledge graph generated a high score (98.44%) for this prediction, but the mechanistic rationale within the evidence pack itself flags this as likely **knowledge graph topology noise** — the score likely arises from structural co-clustering of hair follicle developmental nodes within the graph, rather than any genuine pharmacological relationship. This is a recognised limitation of graph-based prediction models, and independent biological validation is required before this prediction can be taken further.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Benserazide is currently **not registered with SAHPRA** and is not marketed in South Africa. There are no active licences on record.

> **Note on market access:** Should any repurposing pathway proceed to clinical investigation in South Africa, a Section 21 (unregistered medicine) authorisation application to SAHPRA would be required prior to patient exposure.

---

## Safety Considerations

No safety data (warnings, contraindications, or drug interactions) was retrievable from the evidence pack for this analysis.

Please refer to the SAHPRA-approved Professional Information (PI) — or equivalent EMA/MHRA PI for Madopar® (levodopa + benserazide) — for the complete safety profile. Report any adverse drug reactions to SAHPRA via the MedSafety online reporting portal.

> ⚠️ **Important safety signal identified in adjacent prediction (Rank 7 — Headache Disorder):**
> A 1979 clinical observation study ([PMID 554794](https://pubmed.ncbi.nlm.nih.gov/554794/)) reported that benserazide administration triggered typical migraine attacks in migrainous women, independent of prolactin changes. The proposed mechanism involves peripheral DDC inhibition causing redistribution of tryptophan/tyrosine precursors, leading to disinhibition of the trigeminovascular system. This adverse signal is directly relevant to patient selection criteria and safety monitoring should **any** future repurposing study be designed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (congenital hypotrichosis milia, 98.44%) is unsupported by any clinical trials or literature, and the mechanistic rationale is absent — the high prediction score is most likely a knowledge graph structural artefact. Benserazide is additionally unregistered in South Africa, eliminating any near-term clinical pathway without SAHPRA Section 21 authorisation.

**To proceed, the following is needed:**

- **Recover safety data:** Obtain and review the EMA/MHRA Professional Information for Madopar® (levodopa + benserazide) to complete the safety profile assessment required for any S1 evaluation
- **Recover MOA data:** Query the DrugBank API for DB12783 to obtain mechanistic targets, pharmacology, and toxicity data; this is currently a high-severity data gap
- **Prioritise mechanistically plausible predictions:** The pheochromocytoma predictions (Rank 8 and Rank 10; TxGNN scores ~96.5–96.6%) carry the most coherent mechanistic hypothesis — DDC/AADC is a rate-limiting enzyme in catecholamine synthesis, and Benserazide's inhibitory activity is biochemically relevant to tumour hypersecretion states. A joint proof-of-concept study using PC12 cell models is recommended
- **Consider exploratory investigation for diffuse alopecia areata (Rank 3):** The dopamine receptor modulation hypothesis in follicular immune microenvironment warrants in vitro investigation via hair follicle co-culture models before any clinical consideration
- **Do not pursue headache disorder or trigeminal autonomic cephalalgia predictions (Ranks 7 and 9):** A published adverse signal confirming migraine induction by benserazide ([PMID 554794](https://pubmed.ncbi.nlm.nih.gov/554794/)) represents a direct contraindication to repurposing in this class
- **SAHPRA pathway:** All South African clinical investigations would require Section 21 authorisation given the current unregistered status

---

> **Disclaimer:** This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. This prediction was generated by the TxGNN model and must not be used to guide prescribing or patient management decisions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

