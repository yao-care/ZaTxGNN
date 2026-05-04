---
layout: default
title: Bismuth Subcarbonate
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L5
indication_count: 10
---

# Bismuth Subcarbonate
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

# Bismuth Subcarbonate: From Gastrointestinal Protection to Insomnia

## One-Sentence Summary

Bismuth subcarbonate is a bismuth salt with established gastrointestinal protective and antibacterial properties, historically used as an antacid and antidiarrheal agent.
The TxGNN model predicts it may be effective for **Insomnia**, however this prediction is supported by **no clinical trials** and **no published literature** — it rests entirely on computational modelling.
The biological plausibility of this prediction is low, as no known mechanism connects bismuth compounds to the neurological pathways governing sleep.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gastrointestinal protective agent / antacid / antidiarrheal (no formal indication on file; no SAHPRA registration) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for bismuth subcarbonate. Based on established pharmacology, bismuth subcarbonate is a bismuth(III) salt whose activity is concentrated in the gastrointestinal tract: bismuth ions (Bi³⁺) form a protective protein-bismuth complex that coats the gut mucosa, provide broad-spectrum antibacterial activity against gastrointestinal pathogens (including *Helicobacter pylori*) by disrupting bacterial enzyme activity and cell-wall synthesis, and suppress pro-inflammatory cytokines (IL-1β, TNF-α) within the intestinal mucosa. A class-effect analogy is bismuth subsalicylate (Pepto-Bismol), which shares these gastrointestinal mechanisms and has documented human use in acute diarrhoea and enteritis.

Insomnia involves dysregulation of sleep-promoting neurological pathways including GABAergic neurotransmission (benzodiazepine-sensitive GABA-A receptors), melatonin signalling (MT1/MT2 receptors), adenosine homeostasis, and orexin receptor antagonism (OX1R/OX2R). None of these pathways have any known intersection with bismuth ion pharmacology, and bismuth compounds have no documented central nervous system activity at therapeutic doses.

The high TxGNN score of 99.38% most likely reflects non-specific co-morbidity linkages in the knowledge graph — insomnia commonly co-occurs with gastrointestinal conditions such as irritable bowel syndrome and functional dyspepsia — rather than a genuine mechanistic drug-disease relationship. The simultaneous appearance of two near-identical sleep indications (insomnia, rank 1; "sleep disorder, initiating and maintaining sleep", rank 6) in the top predictions further points to a topological bias in the model rather than a specific pharmacological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Bismuth subcarbonate is **not currently marketed in South Africa** and holds **no SAHPRA registrations**. It does not appear on the South African Essential Medicines List (EML). There are no registered products to list.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> **Important safety note for this candidate review:** Although full contraindication and warning data are not available in this Evidence Pack (identified as a Blocking data gap), clinicians should be aware that **bismuth toxicity (bismuth encephalopathy)** is a well-documented risk associated with prolonged or high-dose bismuth use. Clinical manifestations include tremor, ataxia, confusion, and muscle weakness. This toxicological profile is directly relevant to evaluating the full TxGNN prediction set: several predicted indications involve the neuromuscular junction and peripheral nervous system — conditions for which bismuth compounds may pose **harm rather than benefit** (see Conclusion below).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no plausible biological mechanism linking bismuth subcarbonate to sleep regulation, and the prediction is entirely unsupported by clinical trials or published literature (L5). The current evidence base does not meet the minimum threshold for any further investigation in this indication.

**Broader context across the full prediction set:**

Of the 10 TxGNN-predicted indications, the most biologically coherent signal is **enterocolitis (rank 2, score 96.94%)**, which directly aligns with bismuth's known gastrointestinal mechanism — mucosal protection, antimicrobial activity, and anti-inflammatory cytokine suppression. One veterinary uncontrolled study (PMID [6247810](https://pubmed.ncbi.nlm.nih.gov/6247810/), 1980) exists, placing it at L4. Class-effect evidence from bismuth subsalicylate in human enteritis provides additional indirect support. This direction represents the only scientifically viable repurposing hypothesis in this dataset and may warrant escalation to a targeted systematic review.

Three predicted indications — **adult-onset myasthenia gravis (rank 7)**, **myasthenia gravis with thymus hyperplasia (rank 8)**, and **autoimmune disease of the peripheral nervous system (rank 10)** — carry a **reverse harm signal**: documented bismuth neurotoxicity (bismuth encephalopathy, bismuth neuropathy) targets precisely the neuromuscular junction and peripheral nervous system involved in these diseases. These directions should be formally flagged as contraindicated for repurposing research.

**To progress the enterocolitis direction (rank 2), the following is needed:**

- **Mechanism of action data:** Obtain full DrugBank entry for bismuth subcarbonate (DB11281) to confirm Bi³⁺ pharmacodynamic targets
- **Class-effect literature review:** Systematic search for bismuth subsalicylate and bismuth subnitrate in human enterocolitis and infectious diarrhoea RCTs to establish indirect class-level evidence
- **Regulatory landscape review:** Document global markets (e.g., USA, EU, Japan) where bismuth salts hold approved gastrointestinal indications, to inform a SAHPRA Section 21 or new drug application pathway
- **Full safety data:** Retrieve complete contraindication and drug interaction profile from the DrugBank API and available international product monographs before any human study is considered

> *This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All findings should be interpreted alongside SAHPRA-approved prescribing information.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

