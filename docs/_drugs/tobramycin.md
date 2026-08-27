---
layout: default
title: Tobramycin
parent: 僅模型預測 (L5)
nav_order: 438
evidence_level: L5
indication_count: 10
---

# Tobramycin
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

Using no additional tool orchestration for this one — this is a direct content-generation task against the Evidence Pack schema described in your report prompt, so I'm writing the report directly from the JSON provided.

A few notes on judgment calls made while drafting (flagging per the "動手前驗證/報告規則" discipline rather than silently guessing):

- `original_indications` and `taiwan_regulatory.licenses` are both empty, so there is no SAHPRA-approved indication text to extract. I did not fabricate one; instead I stated plainly that no registration/indication record exists, and used only the antibiotic-class background that the evidence pack's own `repurposing_rationale` fields repeatedly reference (Pseudomonas aeruginosa / aminoglycoside).
- `predicted_indications[0].scoring.recommendation` is `"Research Question"`, which isn't one of the three template buckets (Go / Hold / Proceed with Guardrails). I mapped it to **Hold** and said so explicitly, rather than silently renaming it.
- DG001 (TFDA/SAHPRA label data) is marked `Blocking` severity in `meta.data_gaps` — I surfaced this in the Conclusion since it directly limits how far this candidate can even be evaluated.

---

# Tobramycin: From Bacterial Infections to Exposure Keratitis

## One-Sentence Summary

Tobramycin is an aminoglycoside antibiotic historically used against serious gram-negative bacterial infections, most notably *Pseudomonas aeruginosa* (e.g. in cystic fibrosis and complicated urinary tract infections). The TxGNN model predicts it may be effective for **Exposure Keratitis**, but this direction is currently supported by only **2 clinical trials** (both of low, indirect relevance) and **7 publications** (mostly case reports and an in-vitro toxicity study) — and one of those publications specifically shows tobramycin can be toxic to corneal epithelial cells, which is the exact tissue already compromised in exposure keratitis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No SAHPRA registration record available (drug not marketed in South Africa). Internationally, tobramycin is indicated for serious bacterial infections, particularly *Pseudomonas aeruginosa* (e.g. cystic fibrosis, complicated UTI, malignant otitis externa) |
| Predicted New Indication | Exposure Keratitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, tobramycin is an aminoglycoside antibiotic; its efficacy against gram-negative bacterial infections (especially *Pseudomonas aeruginosa*) has been well established, and topical aminoglycoside formulations (including tobramycin eye drops) are already used clinically for bacterial keratitis.

Exposure keratitis, however, is primarily a **mechanical/desiccation injury** of the cornea caused by incomplete eyelid closure (lagophthalmos), not a primary infection. Its first-line management is lubrication and eyelid closure measures; antibiotics such as tobramycin would at most play a role in preventing or treating a *secondary* bacterial infection superimposed on an already-damaged corneal surface — not in treating the underlying condition itself.

This mechanistic link is further complicated by a genuine safety signal in the evidence: an in-vitro study (PMID 2707046) found that aminoglycosides, including tobramycin, are directly cytotoxic to corneal epithelial cells. Since exposure keratitis already involves compromised corneal epithelium, using tobramycin in this population could plausibly worsen epithelial injury rather than help it. This is a case where the TxGNN score is high, but the biological rationale argues for caution rather than confidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05313828](https://clinicaltrials.gov/study/NCT05313828) | N/A | Unknown | 40 | Compared treatment modalities for dendritic (herpes simplex virus) corneal ulcer — a viral condition, not exposure keratitis, and tobramycin was not the primary intervention studied. Evidence-pipeline relevance grade: **C (low)**. |
| [NCT06200727](https://clinicaltrials.gov/study/NCT06200727) | N/A | Unknown | 170 | Evaluated platelet-rich fibrin (PRF) membrane across four ophthalmic conditions (macular hole, pterygium, corneal ulcer, post-trabeculectomy glaucoma); not focused on tobramycin or on exposure keratitis. Evidence-pipeline relevance grade: **C (low)**. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34987857](https://pubmed.ncbi.nlm.nih.gov/34987857/) | 2021 | Case report | Oxford Medical Case Reports | Bacterial keratitis (multi-drug-resistant *Shewanella algae*) in a bedridden, vegetative-state patient unable to close his eyes — clinically relevant to the exposure/lagophthalmos-plus-infection scenario, but tobramycin efficacy was not directly tested in this case. |
| [2707046](https://pubmed.ncbi.nlm.nih.gov/2707046/) | 1989 | In-vitro toxicity study | Current Eye Research | Compared corneal epithelial cytotoxicity of four aminoglycosides (neomycin, gentamicin, **tobramycin**, amikacin) in cultured rabbit corneal epithelial cells — shows direct epithelial toxicity, a safety signal directly relevant to applying tobramycin on an already-damaged exposure-keratitis cornea. |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case report | Ophthalmology | Contact lens-associated *Bacillus cereus* keratitis — a general bacterial keratitis case, not specific to exposure keratitis. |
| [12861116](https://pubmed.ncbi.nlm.nih.gov/12861116/) | 2003 | Case report | Eye & Contact Lens | Bilateral MRSA keratitis following photorefractive keratectomy — general post-surgical bacterial keratitis, not exposure-related. |
| [17228760](https://pubmed.ncbi.nlm.nih.gov/17228760/) | 2006 | In-vitro comparison study | Nippon Ganka Gakkai Zasshi | MIC and postantibiotic effect of antibiotic eye drops against Japanese infectious-keratitis isolates — general susceptibility data, not exposure-keratitis specific. |
| [33847093](https://pubmed.ncbi.nlm.nih.gov/33847093/) | 2021 | Retrospective case series (veterinary) | Polish Journal of Veterinary Sciences | Feline ocular toxoplasmosis outcomes — veterinary data, not directly applicable to human tobramycin use. |
| [14574976](https://pubmed.ncbi.nlm.nih.gov/14574976/) | 2003 | Case report | Yan Ke Xue Bao (Eye Science) | Corneal dellen as a rare sign of Graves ophthalmopathy — unrelated to tobramycin or infection. |

## South Africa Market Information

Tobramycin currently has **no SAHPRA registrations on record** in this evidence pack (`market_status: Not marketed`, `total_licenses: 0`). No product/registration table can be produced until SAHPRA registration data becomes available.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Structured safety fields (key warnings, contraindications, drug-drug interactions) are all marked as data gaps in this evidence pack — this is itself flagged as a **Blocking** gap (DG001: TFDA/SAHPRA label warnings and contraindications), meaning a formal safety (S1) evaluation cannot proceed until this is resolved. Separately, the mechanistic evidence reviewed above (PMID 2707046) indicates aminoglycosides as a class, including tobramycin, carry known corneal epithelial toxicity — a signal worth flagging for clinical judgment even though it does not come from a formal PI source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The evidence pack itself scores this candidate as "Research Question" (decision stage S1), the earliest and least confident recommendation tier.
- Supporting evidence is weak and mostly off-target (grade-C trials, case reports, veterinary/in-vitro studies) rather than direct evidence of tobramycin efficacy in exposure keratitis.
- A genuine mechanistic concern exists: the drug's own class-level corneal epithelial toxicity could plausibly worsen the condition it is being proposed to treat.
- A **Blocking** data gap (DG001 — TFDA/SAHPRA label warnings/contraindications) prevents this candidate from formally entering safety evaluation at all.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) — warnings, contraindications, and DDI data (currently blocking).
- Confirmed mechanism of action data from DrugBank (currently a data gap).
- A dedicated pharmacology/toxicology assessment of topical aminoglycoside use on compromised corneal epithelium before any clinical exploration.
- Direct clinical evidence (even preclinical) specifically evaluating tobramycin — rather than other agents or unrelated ophthalmic interventions — in exposure keratitis.

**Note on other candidates in this evidence pack:** Exposure keratitis was evaluated here because it is `predicted_indications[0]` (highest TxGNN score). However, rank 3 in the same pack — **otitis externa** (TxGNN score 99.81%, Evidence Level L3, decision stage S2, recommendation "Proceed with Guardrails") — has materially stronger literature support, including cohort-level toxicity follow-up data for tobramycin in malignant otitis externa (an established off-label use pattern), and may warrant a separate, dedicated evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

