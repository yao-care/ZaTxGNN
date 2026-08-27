---
layout: default
title: Lansoprazole
parent: 僅模型預測 (L5)
nav_order: 279
evidence_level: L5
indication_count: 10
---

# Lansoprazole
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

# Lansoprazole: From Acid-Related Gastrointestinal Disorders to Duodenogastric Reflux

## One-Sentence Summary

> Lansoprazole is a proton pump inhibitor (PPI), originally used for acid-related gastrointestinal disorders such as peptic ulcer disease and gastro-oesophageal reflux.
> The TxGNN model predicts it may be effective for **Duodenogastric Reflux**,
> but this direction is currently supported by only **0 clinical trials** and **2 publications** — and one of those publications raises a safety caution rather than a therapeutic benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acid-related disorders (peptic ulcer disease, GERD) — SAHPRA-specific approved indication text is not available; the drug is not currently marketed in South Africa |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap). Based on known information, Lansoprazole is a proton pump inhibitor (PPI) that irreversibly inhibits the gastric H⁺/K⁺-ATPase in parietal cells, thereby suppressing gastric acid secretion; its efficacy in peptic ulcer disease, erosive reflux oesophagitis, and NSAID-associated gastric injury is well established across decades of clinical literature.

Duodenogastric reflux, however, is a distinct pathology — it involves the backflow of bile and duodenal contents (not primarily acid) into the stomach. Reducing gastric acid secretion does not directly address this bile/alkaline component, so the mechanistic link to lansoprazole is indirect at best.

More importantly, the only preclinical evidence available in this pack (PMID 15052437) suggests that acid inhibition combined with duodenogastric reflux may *promote* gastric carcinogenesis in a rat model — this is a safety signal, not a supportive efficacy signal. As the evidence summary itself notes: *"Lansoprazole 抑制胃酸分泌，理論上可緩解相關症狀，但機轉未針對膽汁/十二指腸液逆流本身；動物實驗反顯示長期用藥可能促進伴隨十二指腸胃逆流的胃癌變，屬安全疑慮訊號而非療效訊號。"* This is why the evidence level is capped at L4 (preclinical/mechanistic only) and the recommendation is Hold rather than Proceed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Preclinical (rat study) | Gastric Cancer | Duodenogastric reflux increases gastric cancer frequency in rats; combined with acid inhibition (lansoprazole), the study examined whether acid suppression promotes gastric carcinogenesis in this setting — a cautionary rather than supportive finding |
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | European Journal of Clinical Pharmacology | General review of PPI clinical use and pharmacokinetics (peptic ulcer, H. pylori infection, GERD, NSAID-induced GI lesions, Zollinger-Ellison syndrome); does not specifically address duodenogastric reflux |

## South Africa Market Information

Lansoprazole is currently **not registered with SAHPRA** — 0 licenses on file, market status "Not marketed." No product-level registration data (registration number, product name, dosage form, approved indication) is available in this evidence pack.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for duodenogastric reflux consists solely of a preclinical/mechanistic literature base (L4) with zero clinical trials, and the strongest available data point (an animal study) flags a potential carcinogenesis risk rather than therapeutic benefit. The proposed mechanism (acid suppression) also does not directly target the underlying bile/duodenal-content reflux pathology.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank/primary pharmacology sources (currently a Blocking data gap)
- TFDA/SAHPRA-approved Professional Information (PI) — warnings, contraindications, and DDI data (currently a Blocking data gap)
- Dedicated clinical or observational studies evaluating lansoprazole specifically in duodenogastric reflux (ideally in post-gastrectomy or bile-reflux populations), rather than reflux oesophagitis in general
- Further characterization of the long-term gastric carcinogenesis signal identified in the rat model before any human indication is considered
- A South Africa regulatory pathway assessment, since the drug currently holds no SAHPRA registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

