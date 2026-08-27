---
layout: default
title: Procaine
parent: 僅模型預測 (L5)
nav_order: 378
evidence_level: L5
indication_count: 10
---

# Procaine
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

# Procaine: From Local Anaesthesia to Methemoglobinemia

## One-Sentence Summary

Procaine (DrugBank DB00721) is an ester-type local anaesthetic historically used for infiltration, nerve block, and intravenous regional anaesthesia. The TxGNN model's top prediction links it to **Methemoglobinemia** with a 99.50% score, but the **8 supporting publications** (no clinical trials) describe procaine as a documented **cause** of methemoglobinemia, not a treatment — the mechanistic direction is inverted, and this candidate does not currently support a repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local anaesthesia (ester-type local anaesthetic; no SAHPRA-registered product/indication text available) |
| Predicted New Indication | Methemoglobinemia |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L4 (case reports/experimental data only; no controlled trials) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for procaine is not available in this evidence pack (data gap DG002, severity High). Based on the classification notes attached to the literature evidence, procaine is an ester-type local anaesthetic that blocks voltage-gated sodium channels for its anaesthetic effect; its hydrolysis produces para-aminobenzoic acid (PABA) and diethylaminoethanol, and aromatic-amine metabolites of this type are known oxidisers of haemoglobin iron (Fe²⁺ → Fe³⁺) — the mechanism underlying **drug-induced** methemoglobinemia.

This is the key issue with the top-ranked prediction: all 8 associated publications describe procaine as the causative agent of methemoglobinemia (including a case in a newborn after subcutaneous infiltration, and a direct experimental study on IV procaine raising methemoglobin levels), not as a therapeutic agent for the condition. The relationship between the original use (local anaesthesia) and the predicted indication is therefore an **adverse-effect association**, not a repurposing signal. This pattern is consistent with a known limitation of knowledge-graph-based prediction: it can learn drug–disease co-occurrence without capturing causal direction, so a strong "drug causes disease X" literature signal can surface as a high-scoring "drug treats disease X" candidate. The same inverted pattern appears in ranks 2–6 of this evidence pack (methemoglobinemia subtype, anaphylaxis, hyperthyroidism), where procaine is documented as a risk factor or diagnostic-test reagent rather than a treatment.

By contrast, two lower-ranked candidates in this pack — fibromyalgia (rank 7) and tendinitis (rank 8) — point in the correct therapeutic direction: procaine has historically been injected into myofascial trigger points ("neural therapy") to interrupt nociceptive signalling and pain-spasm cycles, and their literature includes an RCT for supraspinatus tendinopathy (PMID 35480510). These are mechanistically more coherent, though evidence quality remains low (L3, uncontrolled/dated case series), and they are flagged as "Research Question" rather than repurposing candidates ready for further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5529388](https://pubmed.ncbi.nlm.nih.gov/5529388/) | 1970 | Case Report | Acta physiologica latino americana | Methemoglobinemia due to intravenous procaine — procaine identified as the causative agent |
| [3691245](https://pubmed.ncbi.nlm.nih.gov/3691245/) | 1987 | Observational/Experimental | Zhonghua wai ke za zhi | IV procaine anaesthesia raises methemoglobin levels |
| [6705717](https://pubmed.ncbi.nlm.nih.gov/6705717/) | 1984 | Review | Drugs | General review of rational local anaesthetic use; not procaine/methemoglobinemia-specific |
| [5118947](https://pubmed.ncbi.nlm.nih.gov/5118947/) | 1971 | Review | Laval medical | General review of local anaesthetics |
| [705003](https://pubmed.ncbi.nlm.nih.gov/705003/) | 1978 | Case Report (newborn) | Revista espanola de anestesiologia y reanimacion | Methemoglobinemia in a newborn after subcutaneous novocaine infiltration during general anaesthesia |
| [5644303](https://pubmed.ncbi.nlm.nih.gov/5644303/) | 1968 | PK study | American journal of obstetrics and gynecology | Placental transfer of procaine HCl and PABA; not a treatment study |
| [14246695](https://pubmed.ncbi.nlm.nih.gov/14246695/) | 1965 | Case Report (lignocaine, not procaine) | Lancet | Methaemoglobinaemia following lignocaine — different drug, limited relevance |
| [6745527](https://pubmed.ncbi.nlm.nih.gov/6745527/) | 1984 | Review (organophosphate mechanism) | Fundamental and Applied Toxicology | Organophosphate-ester toxicology interactions; not directly about procaine |

All procaine-specific entries describe methemoglobinemia as an **adverse reaction to procaine**, not a treatment indication.

---

## South Africa Market Information

Procaine is currently **not marketed** in South Africa, with 0 SAHPRA-registered products in this evidence pack. No registration numbers, product names, or approved-indication text are available for South Africa at this time.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for formal safety information; PI warnings and contraindications data are not available in this evidence pack (data gap DG001, severity Blocking). Report adverse drug reactions to SAHPRA.

Note: independent of the formal PI data gap, the literature reviewed for this repurposing signal itself documents two safety-relevant patterns for procaine — (1) drug-induced methemoglobinemia, particularly with IV/high-dose or neonatal exposure, and (2) pseudoanaphylactic/anaphylactoid reactions (Hoigné's syndrome), most often with procaine-penicillin formulations. These should be treated as safety signals for any future clinical use of procaine, not as supporting evidence for repurposing.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN-predicted indication (methemoglobinemia) is contradicted by its own supporting literature, which documents procaine as a cause of the condition rather than a treatment; no clinical trials exist for this or any of the other 9 predicted indications in this pack, and two Blocking/High-severity data gaps (PI safety data, formal MOA) remain unresolved.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings, contraindications) — currently a Blocking data gap
- Formal mechanism-of-action documentation from DrugBank or equivalent — currently a High-severity data gap
- If pursuing the mechanistically plausible secondary signals (fibromyalgia, tendinitis — "neural therapy" use), contemporary controlled trials confirming efficacy against modern comparators, since existing evidence predates current diagnostic criteria and is largely uncontrolled case-series data
- Re-evaluation of the methemoglobinemia, anaphylaxis, and hyperthyroidism signals as potential **safety flags** rather than repurposing candidates, given the directionality of the underlying evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

