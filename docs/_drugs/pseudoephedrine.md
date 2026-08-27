---
layout: default
title: Pseudoephedrine
parent: 僅模型預測 (L5)
nav_order: 383
evidence_level: L5
indication_count: 3
---

# Pseudoephedrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Using the report structure specified in the prompt (this is a direct document-generation task with the full spec already provided — no additional skill needed).

# Pseudoephedrine: From Nasal Decongestant to Nasal Cavity Disease

## One-Sentence Summary

> Pseudoephedrine (DrugBank DB00852) is an oral α-adrenergic agonist long used as a systemic nasal decongestant.
> The TxGNN model predicts high relevance for **Nasal Cavity Disease** (score **99.75%**),
> supported by **19 clinical trials** (1 rated directly relevant) and **7 publications** identified in this search.
> Note: this largely confirms an already-established pharmacological use rather than revealing a genuinely novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in SAHPRA licensing data (drug not currently registered in South Africa); pharmacologically established as an oral systemic nasal decongestant per the evidence rationale |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L2 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation (e.g., a DrugBank MOA monograph entry) is not available in this evidence pack. Based on the pharmacological rationale captured alongside the prediction, pseudoephedrine is an **α-adrenergic agonist** that acts directly on α1 receptors in the vascular smooth muscle of the nasal mucosa, producing vasoconstriction that reduces mucosal congestion and swelling. This is the classic mechanism of an oral, systemically-acting nasal decongestant.

Because this mechanism directly targets nasal mucosal blood flow, the high TxGNN score (0.9975) for "nasal cavity disease" is mechanistically unsurprising — it converges with pseudoephedrine's long-standing real-world use rather than pointing to a truly novel therapeutic application. Clinicians should read this prediction as **confirmatory validation of known pharmacology**, not as a discovery of new drug-disease biology.

Two lower-ranked TxGNN predictions for this drug — acute laryngopharyngitis (L5, no supporting trials or literature) and allergic urticaria (L4, indirect evidence only from combination products) — were reviewed but are not carried forward in this report given weak or absent supporting evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | Double-blind, double-dummy, 4-way crossover in seasonal allergic rhinitis testing an H3-antagonist decongestant effect via acoustic rhinometry after nasal allergen challenge; directly relevant to nasal decongestion pharmacology (relevance grade A) |
| [NCT00804687](https://clinicaltrials.gov/study/NCT00804687) | Phase 2 | Completed | 53 | Randomized, single-blind, double-dummy, 3-way crossover directly comparing JNJ-39220675 vs. **pseudoephedrine** vs. placebo for allergic rhinitis in an environmental exposure chamber |
| [NCT00015795](https://clinicaltrials.gov/study/NCT00015795) | Phase 1 | Completed | 30 | Airflow/laryngeal resistance study in abductor spasmodic dysphonia; low relevance, disease-area overlap only (grade C) |
| [NCT03979209](https://clinicaltrials.gov/study/NCT03979209) | Phase 1 | Completed | 16 | Cortisol suppression risk with high-volume nasal mometasone irrigation; different drug class (corticosteroid), disease-area overlap only (grade C) |
| [NCT00939393](https://clinicaltrials.gov/study/NCT00939393) | N/A | Completed | 72 | Endoscopic sinus surgery performed in-office vs. operating room; surgical, not a drug trial (grade C) |
| [NCT04048174](https://clinicaltrials.gov/study/NCT04048174) | N/A | Completed | 27 | Probiotic bacteria (L. lactis) for chronic rhinosinusitis refractory to standard therapy; unrelated mechanism (grade C) |
| [NCT04645511](https://clinicaltrials.gov/study/NCT04645511) | N/A | Recruiting | 120 | Balloon sinuplasty vs. placebo in chronic/recurrent maxillary rhinosinusitis; device, not drug (grade C) |
| [NCT05494346](https://clinicaltrials.gov/study/NCT05494346) | N/A | Recruiting | 101 | Decongestant seawater spray device with essential oils for acute rhinitis; device, not oral decongestant (grade C) |
| [NCT06010316](https://clinicaltrials.gov/study/NCT06010316) | N/A | Unknown | 200 | Prospective cohort on surgical treatment of chronic rhinosinusitis; disease-area overlap only (grade C) |
| [NCT03725956](https://clinicaltrials.gov/study/NCT03725956) | N/A | Unknown | 30 | Endoscopic sinus surgery effect on sleep disorder in nasal polyposis; surgical, not a drug trial (grade C) |

*Note: Only the first two trials directly test pseudoephedrine or a comparable decongestant mechanism. The remaining eight (all graded "C" — low relevance) are included for completeness because they share the nasal cavity disease area, but represent surgical, device, or unrelated-drug interventions, not pharmacological evidence for pseudoephedrine itself.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11345158](https://pubmed.ncbi.nlm.nih.gov/11345158/) | 2001 | Comparative human study | American Journal of Rhinology | Direct human comparison of oral phenylpropanolamine vs. d-pseudoephedrine decongestant effect using acoustic rhinometry to measure nasal cavity dimensions |
| [22794679](https://pubmed.ncbi.nlm.nih.gov/22794679/) | 2012 | Review | Allergy and Asthma Proceedings | Review chapter on nonallergic rhinitis pathophysiology and management, contextualizing decongestant therapy |
| [19769798](https://pubmed.ncbi.nlm.nih.gov/19769798/) | 2009 | Animal model (feline) | American Journal of Rhinology & Allergy | Feline model showing decongestant action of D-pseudoephedrine alone and combined with desloratadine |
| [24492651](https://pubmed.ncbi.nlm.nih.gov/24492651/) | 2014 | Animal model (pharmacological evaluation) | Journal of Pharmacology and Experimental Therapeutics | Pharmacological characterization of α2c-adrenergic agonists in animal nasal congestion models, contextual to adrenergic decongestant mechanism |
| [12962193](https://pubmed.ncbi.nlm.nih.gov/12962193/) | 2003 | Animal model (canine) | American Journal of Rhinology | Canine ragweed-sensitized allergic nasal congestion model using acoustic rhinometry |
| [12387934](https://pubmed.ncbi.nlm.nih.gov/12387934/) | 2002 | Animal model (canine) | Journal of Pharmacological and Toxicological Methods | Chronic canine model developed to study nasal decongestant drug mechanisms |
| [11895194](https://pubmed.ncbi.nlm.nih.gov/11895194/) | 2002 | Animal model (canine) | American Journal of Rhinology | Acoustic rhinometry validation in a canine model of nasal congestion |

---

## South Africa Market Information

Pseudoephedrine is **not currently registered or marketed in South Africa** according to the data available (0 SAHPRA registrations on file). No product/registration-level information can be reported.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link is strong and well-established (α1-adrenergic vasoconstriction of nasal mucosa), and one directly relevant Phase 2 comparative trial exists (NCT00804687), supporting an L2 evidence level. However, this largely reconfirms pseudoephedrine's known decongestant use rather than a novel indication, and a **Blocking** data gap exists: SAHPRA-approved PI warnings/contraindications are not yet available, which prevents a full safety (S1) evaluation.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) — warnings and contraindications (Blocking gap; required before safety sign-off)
- Formal DrugBank/manufacturer mechanism-of-action documentation
- Confirmation of whether a South African registration/import pathway is being pursued, since the drug is currently unmarketed locally
- Drug-drug interaction review, given the "not_found" DDI query status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

