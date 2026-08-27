---
layout: default
title: Pravastatin
parent: 僅模型預測 (L5)
nav_order: 373
evidence_level: L5
indication_count: 9
---

# Pravastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Pravastatin: From Hypercholesterolemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Pravastatin is an HMG-CoA reductase inhibitor (statin) established for cholesterol lowering and cardiovascular risk reduction. The TxGNN model predicts it may also be relevant for **Homozygous Familial Hypercholesterolemia (HoFH)**, but currently only **1 clinical trial** and **13 publications** touch on this space, and none directly test pravastatin in an HoFH population — the evidence is indirect and mechanistic rather than confirmatory.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia / dyslipidemia (statin class); specific SAHPRA-registered indication text is a data gap in this evidence pack |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data from the source pack is marked as a data gap. Based on known pharmacology, pravastatin is an HMG-CoA reductase inhibitor: it lowers endogenous cholesterol synthesis in hepatocytes and upregulates LDL-receptor expression, which is the basis of its established cholesterol-lowering effect.

HoFH is caused by near-complete loss of functional LDL receptors. Because pravastatin's LDL-lowering effect depends on the LDL-receptor pathway it upregulates, its efficacy in HoFH is expected to be limited on its own — in practice, statins are used in HoFH mainly as background/adjunct therapy alongside PCSK9 inhibitors or LDL apheresis, not as monotherapy. The mechanistic link is therefore plausible but indirect, which is consistent with the L3 evidence level assigned to this prediction.

The single associated clinical trial (NCT03510715) reinforces this caveat: it studies alirocumab, not pravastatin, in the HoFH population — it supports that HoFH is an active trial area, but does not provide direct efficacy evidence for pravastatin itself.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Evaluated alirocumab (PCSK9 inhibitor), not pravastatin, for LDL-C reduction in children/adolescents (8–17y) with HoFH on top of background therapy. Population-relevant only; not direct pravastatin evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Review (Cochrane) | Cochrane Database Syst Rev | Systematic review of statins in children with familial hypercholesterolemia, including homozygous cases. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guideline for management of dyslipidemia and cardiovascular disease prevention. |
| [34425670](https://pubmed.ncbi.nlm.nih.gov/34425670/) | 2021 | Genetic study | Iran Biomed J | Identifies a novel LDLRAP1 splice-site variant causing familial hypercholesterolemia. |
| [31358055](https://pubmed.ncbi.nlm.nih.gov/31358055/) | 2019 | Preclinical/mechanistic | Stem Cell Res Ther | iPSC-derived LDL-receptor-deficient hepatocytes used to model familial hypercholesterolemia and test gene correction. |
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | RCT | Lancet HIV | Phase 4 RCT comparing pitavastatin vs pravastatin in dyslipidemia (HIV population, not HoFH — general statin comparator data). |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review | Drugs | Rosuvastatin review noting it outperformed pravastatin/atorvastatin/simvastatin on lipid profile in trials up to 52 weeks. |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clin Ther | Rosuvastatin review covering use in primary hypercholesterolemia and HoFH, with pravastatin as a class comparator. |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | Review | Ann Pharmacother | Atorvastatin efficacy/safety review in primary hypercholesterolemia and mixed dyslipidemia. |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Atorvastatin pharmacology and therapeutic potential review in hyperlipidaemia management. |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Review | Am J Cardiovasc Drugs | Ezetimibe review; cholesterol absorption inhibitor class, relevant as an adjunct in refractory hypercholesterolemia. |

Most entries above are general statin/lipid-lowering class reviews returned by the literature search rather than studies specifically testing pravastatin in HoFH — this tangential nature is a key reason the evidence level is capped at L3.

---

## South Africa Market Information

Pravastatin is currently **not marketed** in South Africa, with **0 SAHPRA registrations** recorded in this evidence pack. No product listing is available to summarize.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note: retrieval of TFDA/SAHPRA label warnings and contraindications is flagged as a **Blocking** data gap in this evidence pack — this must be resolved before any safety pre-assessment (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking data gap on label warnings/contraindications currently prevents any safety pre-assessment (S1).
- The drug has no SAHPRA registration in South Africa (not marketed), and clinical evidence for HoFH specifically is indirect — the one related trial tested a different drug (alirocumab), and most literature hits are general statin-class reviews rather than pravastatin-in-HoFH studies. Mechanistically, statin efficacy in HoFH is inherently limited by the near-total loss of LDL-receptor function in this population.

**To proceed, the following is needed:**
- Resolution of the Blocking safety data gap (TFDA/SAHPRA PI warnings and contraindications)
- Confirmed mechanism-of-action data (DrugBank or equivalent)
- Direct clinical evidence for pravastatin (not other statins/PCSK9 inhibitors) specifically in HoFH, ideally as adjunct to PCSK9 inhibitor/apheresis therapy
- Confirmation of South Africa registration pathway, given the drug currently has no SAHPRA license
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

