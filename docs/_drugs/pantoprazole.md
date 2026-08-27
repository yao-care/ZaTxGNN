---
layout: default
title: Pantoprazole
parent: 僅模型預測 (L5)
nav_order: 352
evidence_level: L5
indication_count: 6
---

# Pantoprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Pantoprazole: From Acid-Related Disorders to Active Peptic Ulcer Disease

## One-Sentence Summary

Pantoprazole is a proton pump inhibitor (PPI) generally used for acid-related gastrointestinal conditions such as GERD and Helicobacter pylori eradication. The TxGNN model predicts it may be effective for **active peptic ulcer disease**, supported by **3 clinical trials** and **19 publications**. Detailed South African labelling and safety data are not yet on file for this dossier, so the recommendation below should be read alongside the outstanding data gaps noted at the end.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — pantoprazole has no SAHPRA-approved indication text in this dataset (drug is not currently marketed in South Africa) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L1 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dossier. Based on known pharmacology, pantoprazole belongs to the proton pump inhibitor (PPI) class, which irreversibly binds the gastric H⁺/K⁺-ATPase ("proton pump") in parietal cells to suppress acid secretion — a mechanism well documented in the supporting literature (e.g., PMID 19938880, 9017763).

Active peptic ulcer disease is not a distant repurposing target for a PPI — acid suppression is the standard pharmacological basis for both ulcer healing and prevention of ulcer bleeding, which is why the mechanistic link here is direct rather than inferred. As noted in the evidence rationale: *"PPI 抑制胃酸分泌為消化性潰瘍治療標準機轉，pantoprazole 已有多項 Phase 3/4 RCT 直接驗證於活動性潰瘍出血/癒合，機轉關聯明確非間接推論"* (PPI-mediated acid suppression is the standard mechanism for peptic ulcer treatment; pantoprazole already has multiple Phase 3/4 RCTs directly validating efficacy in active ulcer bleeding/healing — the mechanistic link is well-established, not indirect).

This is reflected in the trial evidence, which includes head-to-head Phase 3 comparisons against other acid-suppressing agents and Phase 4 studies in H. pylori eradication and ulcer bleeding — indications very close to, or overlapping with, established PPI use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | Multicenter, randomized, double-blind, active-controlled comparison of ilaprazole vs. pantoprazole triple therapy (7 days) for H. pylori eradication in gastric/duodenal ulcer patients |
| [NCT02197039](https://clinicaltrials.gov/study/NCT02197039) | N/A | Completed | 316 | Prospective study identifying risk factors for poor stigmata fading or early rebleeding in peptic ulcer haemorrhage after endoscopic hemostasis + high-dose PPI infusion |
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Evaluated effect of various PPIs (including pantoprazole) on platelet aggregation and interaction with clopidogrel in patients undergoing PCI |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18824852](https://pubmed.ncbi.nlm.nih.gov/18824852/) | 2008 | RCT | Digestion | Intermittent vs. continuous pantoprazole infusion for peptic ulcer bleeding — prospective randomized comparison |
| [10632647](https://pubmed.ncbi.nlm.nih.gov/10632647/) | 2000 | RCT | Aliment Pharmacol Ther | Pantoprazole + amoxicillin with azithromycin or clarithromycin for H. pylori eradication in duodenal ulcer |
| [12752349](https://pubmed.ncbi.nlm.nih.gov/12752349/) | 2003 | RCT | Aliment Pharmacol Ther | Comparison of three pantoprazole-based triple therapies for H. pylori eradication and gastric ulcer healing |
| [16677158](https://pubmed.ncbi.nlm.nih.gov/16677158/) | 2006 | RCT | J Gastroenterol Hepatol | Pantoprazole infusion as adjuvant to endoscopic treatment in peptic ulcer bleeding — RCT |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | RCT | Hepatogastroenterology | Lansoprazole vs. pantoprazole in active duodenal ulcer treatment and H. pylori eradication |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Investig | Overview of pantoprazole pharmacology, efficacy and drug-interaction profile as a PPI |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic Review/Meta-analysis | Am J Gastroenterol | Comparative efficacy of P-CAB vs. PPIs (including pantoprazole) for Grade C/D esophagitis |
| [22919877](https://pubmed.ncbi.nlm.nih.gov/22919877/) | 2012 | Cohort | Med Arch | Efficacy of PPI after endoscopic hemostasis in bleeding peptic ulcer, and role of H. pylori |
| [9017763](https://pubmed.ncbi.nlm.nih.gov/9017763/) | 1997 | Review | Pharmacotherapy | Mechanism of PPIs (including pantoprazole) in acid-related diseases |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | Preclinical/Animal | Inflammopharmacology | Combined pantoprazole + mesenchymal stem cell effect on experimentally induced gastric ulcer (rat model) |

---

## South Africa Market Information

Currently no SAHPRA registration on record — pantoprazole is not marketed in South Africa within this dossier (0 registrations, 0 licenses).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3/4 RCTs directly support pantoprazole's efficacy in active peptic ulcer disease and closely related indications (H. pylori eradication, ulcer bleeding prevention), giving an L1 evidence level. However, the drug is not currently registered/marketed in South Africa, and regulatory safety labelling and mechanism-of-action data are missing from this dossier, so proceeding requires guardrails rather than an unconditional Go.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings, contraindications, drug interactions) — currently a blocking data gap
- Confirmed mechanism of action documentation (e.g., via DrugBank) to support the mechanistic-relevance analysis
- Confirmation of registration/market-entry pathway in South Africa, since no SAHPRA licenses currently exist for this product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

