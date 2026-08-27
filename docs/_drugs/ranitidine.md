---
layout: default
title: Ranitidine
parent: 僅模型預測 (L5)
nav_order: 389
evidence_level: L5
indication_count: 10
---

# Ranitidine
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

# Ranitidine: From Established Peptic Ulcer Therapy to Active Peptic Ulcer Disease

## One-Sentence Summary

Ranitidine is a histamine H2-receptor antagonist historically used to treat and prevent peptic ulcer disease; this evidence pack does not record its original indication text, so the top TxGNN prediction — **Active Peptic Ulcer Disease** — is not a novel repurposing hypothesis but effectively confirms the drug's own established label use. The signal is supported by **1 clinical trial** and **19 literature references**, though most address related H2-antagonist comparisons rather than a direct interventional trial of ranitidine specifically for this diagnosis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record in this evidence pack (drug class: histamine H2-receptor antagonist, historically indicated for peptic ulcer disease) |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L1 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned for this candidate (DG002, High severity). Based on well-established pharmacology, ranitidine is an H2-receptor antagonist that competitively blocks histamine at parietal cell H2 receptors, reducing basal and stimulated gastric acid secretion — the classic mechanism underlying its use in acid-peptic disease.

Critically, "active peptic ulcer disease" is not a mechanistically distant new use for ranitidine — it is the condition the drug was originally developed and approved to treat. The evidence pack's `original_indications` field is empty (a data gap), which is why this appears here as a "prediction" rather than a known indication. The reasonableness of the mechanism is therefore not in question; what is in question is whether this candidate represents genuine repurposing value at all, versus simply re-confirming known pharmacology.

Several lower-ranked candidates in this pack (peptic ulcer perforation, gastrojejunal/marginal ulcer, gastroduodenitis) extend the same acid-suppression rationale to related but distinct clinical scenarios, with progressively weaker and mostly indirect evidence (L2–L3). Others (e.g., mastocytosis subtypes, glucagon secretion abnormality) have no mechanistic or literature support in this pack and are flagged Hold/L5 — likely knowledge-graph artifacts rather than credible hypotheses.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Evaluated the effect of various PPIs (not ranitidine itself) on clopidogrel antiplatelet activity in PCI patients; relevance to ranitidine/PUD is indirect (drug-interaction context, Grade C relevance per evidence pack). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3909374](https://pubmed.ncbi.nlm.nih.gov/3909374/) | 1985 | RCT | Scandinavian Journal of Gastroenterology | Ranitidine 300mg/day healed 91% of duodenal, 68% of prepyloric, and 81% of gastric corporeal ulcers at 4 weeks; maintenance therapy reduced relapse vs placebo. |
| [3104657](https://pubmed.ncbi.nlm.nih.gov/3104657/) | 1986 | RCT | Klinische Wochenschrift | Compared nocturnal rioprostil (prostaglandin E1 analogue) vs ranitidine for duodenal ulcer healing. |
| [2491360](https://pubmed.ncbi.nlm.nih.gov/2491360/) | 1989 | RCT | Journal of Gastroenterology and Hepatology | Double-blind, 270-patient trial: omeprazole (10/20mg) vs ranitidine 150mg BID for duodenal ulcer healing and relapse. |
| [2877570](https://pubmed.ncbi.nlm.nih.gov/2877570/) | 1986 | RCT | The American Journal of Medicine | Multicentre, double-blind, 1,031-patient international trial comparing famotidine vs ranitidine for active duodenal ulcer. |
| [2092029](https://pubmed.ncbi.nlm.nih.gov/2092029/) | 1990 | RCT | Journal of the Association of Physicians of India | Double-blind trial of famotidine vs ranitidine in endoscopically diagnosed peptic ulcer. |
| [1863945](https://pubmed.ncbi.nlm.nih.gov/1863945/) | 1991 | RCT | Clinical Therapeutics | 160-patient multicenter trial: famotidine vs ranitidine healing rates in active duodenal ulcer, including NSAID/aspirin-related ulcers. |
| [12749277](https://pubmed.ncbi.nlm.nih.gov/12749277/) | 2003 | Prospective controlled study | Hepato-Gastroenterology | Ranitidine + ecabet vs ranitidine alone for inhibiting peptic ulcer relapse, independent of H. pylori eradication. |
| [6317325](https://pubmed.ncbi.nlm.nih.gov/6317325/) | 1983 | Review | Drug Intelligence & Clinical Pharmacy | Overview of ranitidine's approval for active duodenal ulcer and gastric hypersecretory conditions; potency vs cimetidine. |
| [2905237](https://pubmed.ncbi.nlm.nih.gov/2905237/) | 1988 | Review | Drugs | Reviews prostaglandins and H2-antagonists in peptic ulcer disease pathophysiology and treatment. |
| [1976583](https://pubmed.ncbi.nlm.nih.gov/1976583/) | 1990 | Review | Hepato-Gastroenterology | Reviews acid secretion/suppression in peptic ulcer pathogenesis and healing. |

## South Africa Market Information

Currently no SAHPRA registrations are on record for ranitidine in this evidence pack (`total_licenses = 0`, `market_status = 未上市 / Not Marketed`).

**Background context (not sourced from this evidence pack, requires verification):** ranitidine products were withdrawn globally in 2019–2020 after regulators detected NDMA (a probable human carcinogen) contamination in the active substance. This is a plausible explanation for the current absence of South African registrations, but it should be confirmed against SAHPRA's official withdrawal/market-status records before this candidate is advanced.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No key warnings, contraindications, or drug-drug interaction data were retrievable for this candidate. This is flagged in the evidence pack as a **Blocking** data gap (DG001: TFDA/SAHPRA labelling warnings/contraindications), meaning the candidate currently **cannot enter S1 safety pre-assessment**.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (active peptic ulcer disease) mechanistically matches ranitidine's own historical, well-established use rather than representing a genuine novel repurposing hypothesis — its apparent "prediction" status stems from a data gap in the `original_indications` field, not a new discovery.
- A Blocking safety data gap (no PI, warnings, or contraindications) and zero current SAHPRA registrations (drug not marketed in South Africa) mean the candidate cannot proceed past initial safety screening regardless of the strength of efficacy evidence.

**To proceed, the following is needed:**
- Retrieve the current (or most recent) SAHPRA-approved PI, or formally confirm the product holds no active SA registration, to close DG001
- Obtain authoritative DrugBank/mechanism-of-action data to close DG002
- Verify ranitidine's current global regulatory status (NDMA contamination recalls) and whether SAHPRA has an official withdrawal record
- Clarify whether this candidate should be reclassified as "known original indication, market re-entry question" rather than a repurposing opportunity
- Complete literature classification/relevance tagging (currently marked "pending" for most entries) to firm up the evidence-level determination
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

