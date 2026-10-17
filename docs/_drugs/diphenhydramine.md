---
layout: default
title: Diphenhydramine
parent: Model Prediction Only (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Diphenhydramine: predicted new indication Rosacea conjunctivitis (evidence level L5). Approved use: Insomnia, vasomotor rhinitis, allergic rhinitis…"
monitor_inn: "Diphenhydramine"
predicted_indications: ["cauda equina syndrome", "nasopharyngitis", "neuralgia", "trigeminal autonomic cephalalgia", "glossodynia"]
---

# Diphenhydramine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Diphenhydramine: From Allergic and Vasomotor Rhinitis to Rosacea Conjunctivitis

## One-Sentence Summary

Diphenhydramine is a first-generation H1 antihistamine, originally used for insomnia, allergic and vasomotor rhinitis, and several forms of allergic conjunctivitis (atopic, papillary, vernal).
The TxGNN model's top-ranked prediction is **rosacea conjunctivitis**, but **no clinical trials or publications** support it. The best-supported predicted indications are **rhinitis** (5 trials, 19 publications) and **allergic urticaria** (1 trial, 19 publications), and both largely confirm existing use rather than represent true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Insomnia, vasomotor rhinitis, allergic rhinitis, atopic/papillary/vernal conjunctivitis (the SAHPRA records compiled for this report contain no approved indication text) |
| Predicted New Indication | Rosacea conjunctivitis (rank 1) |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 (rank 1). Other predictions: rhinitis L1, allergic urticaria L3 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 19 |
| Recommended Decision | Hold (rank 1). Proceed with Guardrails for rhinitis and allergic urticaria |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, diphenhydramine is an H1-receptor antagonist with marked anticholinergic and sedative effects, and its efficacy in allergic rhinitis and allergic conjunctivitis is established.

**Rank 1, rosacea conjunctivitis:** The link is weak. H1 blockade may relieve histamine-mediated ocular itch and redness, as in the approved conjunctivitis indications. However, rosacea-related eye inflammation is mainly driven by meibomian gland dysfunction and innate immune and microbial factors, which antihistamines do not address. The high score is therefore a model output without supporting clinical data.

**Better-supported predictions:**
- **Rhinitis (score 98.3%):** H1 blockade reduces histamine-driven sneezing, rhinorrhoea and itching, and anticholinergic activity dries nasal secretions. This overlaps with existing labelled use.
- **Allergic urticaria (score 98.2%):** Mast-cell histamine drives wheal and flare, so H1 antagonism is mechanistically sound and guideline-recognised.
- **Cold urticaria (95.9%):** Plausible mechanism, but evidence is limited to case reports and old overviews.

Several lower-ranked predictions have no plausible mechanistic basis: cauda equina syndrome, viral conjunctivitis, and glossodynia.

---

## Clinical Trial Evidence

The table covers the rank 1 prediction (no trials) and the main supported predictions.

**Rosacea conjunctivitis:** Currently no related clinical trials registered.

**Rhinitis**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00648973](https://clinicaltrials.gov/study/NCT00648973) | Phase 4 | Completed | 1021 | Randomised, double-blind, placebo- and pseudoephedrine-controlled study of diphenhydramine 25 mg and 50 mg for nasal congestion in seasonal allergic rhinitis. Large and directly relevant. |
| [NCT00762749](https://clinicaltrials.gov/study/NCT00762749) | Phase 1 | Completed | 36 | Single-dose pharmacokinetics in children and adolescents. Supports dosing, not efficacy. |
| [NCT01177852](https://clinicaltrials.gov/study/NCT01177852) | Phase 3 | Withdrawn | 0 | Fixed-dose combination with dropropizine and pseudoephedrine for cough and nasal symptoms in children. Withdrawn with no participants, so provides no evidence. |
| [NCT05586477](https://clinicaltrials.gov/study/NCT05586477) | Phase 4 | Completed | 20 | Thermoregulation during exercise. Not about rhinitis efficacy. |
| [NCT06217367](https://clinicaltrials.gov/study/NCT06217367) | Phase 4 | Unknown | 16 | Thermoregulation during passive heat stress. Not about rhinitis efficacy. |

**Allergic urticaria**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Completed | 36 | Pilot study of IV cetirizine versus IV diphenhydramine 50 mg in acute urticaria. A feasibility pilot, not a definitive efficacy trial. |

**Other predictions:** Single trials exist for trigeminal autonomic cephalalgia ([NCT01406860](https://clinicaltrials.gov/study/NCT01406860), terminated, n=19, droperidol versus metoclopramide plus diphenhydramine in primary headache) and neuralgia (two trials of IV lidocaine and an analgesic study, neither testing diphenhydramine). No trials were found for cold urticaria, nasopharyngitis, viral conjunctivitis, cauda equina syndrome, or glossodynia.

No SANCTR or PACTR identifiers were available.

---

## Literature Evidence

**Rosacea conjunctivitis:** Currently no related literature available.

**Rhinitis and allergic urticaria (most relevant)**

| PMID | Year | Type | Journal | Key Findings |
|---------|------|------|------|---------|
| [16680933](https://pubmed.ncbi.nlm.nih.gov/16680933/) | 2006 | RCT | Ann Allergy Asthma Immunol | Diphenhydramine versus desloratadine and placebo in moderate-to-severe seasonal allergic rhinitis. |
| [14582817](https://pubmed.ncbi.nlm.nih.gov/14582817/) | 2003 | RCT | Ann Allergy Asthma Immunol | Diphenhydramine versus desloratadine on vigilance and cognition during ragweed-induced allergic rhinitis. |
| [8634878](https://pubmed.ncbi.nlm.nih.gov/8634878/) | 1996 | RCT | Ann Allergy Asthma Immunol | Effects of acrivastine/pseudoephedrine and diphenhydramine on learning in seasonal allergic rhinitis. |
| [36420548](https://pubmed.ncbi.nlm.nih.gov/36420548/) | 2022 | Pilot study | Tokai J Exp Clin Med | Transdermal diphenhydramine through the nasal ala in allergic rhinitis with asthma. |
| [12113226](https://pubmed.ncbi.nlm.nih.gov/12113226/) | 2002 | Review | Clin Allergy Immunol | H1-antihistamines in children; strong evidence for allergic rhinoconjunctivitis, not for upper respiratory infections. |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | First- versus newer-generation antihistamines in allergic rhinitis and chronic urticaria. |
| [31582993](https://pubmed.ncbi.nlm.nih.gov/31582993/) | 2019 | Position statement | Allergy Asthma Clin Immunol | Newer-generation antihistamines are safer and should be first-line over diphenhydramine and hydroxyzine. |
| [40717751](https://pubmed.ncbi.nlm.nih.gov/40717751/) | 2025 | Review | J Pediatr Pharmacol Ther | Clinical applications and adverse effect profile of diphenhydramine. |
| [34862952](https://pubmed.ncbi.nlm.nih.gov/34862952/) | 2022 | Review | Adv Ther | Role of IV cetirizine versus IV diphenhydramine, the only IV first-generation antihistamine still approved in the USA. |
| [28913986](https://pubmed.ncbi.nlm.nih.gov/28913986/) | 2017 | Review | Allergy Asthma Immunol Res | Chronic spontaneous urticaria starts with second-generation antihistamines at higher doses. |

**Cold urticaria:** Evidence is limited to a 1979 single-patient treatment report ([475987](https://pubmed.ncbi.nlm.nih.gov/475987/)), which found that H1 antagonists including diphenhydramine suppressed wealing, plus recent case reports.

**Other predictions:** Neuralgia literature is indirect (diphenhydramine mostly used as an active placebo). Nasopharyngitis has one indirect combination-product RCT ([17560664](https://pubmed.ncbi.nlm.nih.gov/17560664/)). Trigeminal autonomic cephalalgia has a 1952 historical report ([14909468](https://pubmed.ncbi.nlm.nih.gov/14909468/)).

---

## South Africa Market Information

All 19 registrations are valid single-ingredient licences. The data compiled for this report contains no approved indication text, manufacturer, or Essential Medicines List (EML) status, so these are not shown. The first five registrations are listed:

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 28/2.8/0729 | Tylenol Nightpain | Tablet | Not available |
| M/10.1/248 | Flemex | Syrup | Not available |
| 30/7.1/0183 | Adco-Zildem SR | Src | Not available |
| 43/2.6.5/0042 | Rispevon | Tablet | Not available |
| 28/10.1/0249 | Expectalin with Cod | Syrup | Not available |

Dosage forms across all registrations are tablets, capsules, and syrups (oral route). The remaining 14 registrations include cough syrups and analgesic or headache tablets, such as Benylin & Codeine, Tussilinct Cough, Tensolve Tension Headache Tablets, and Propain.

---

## Safety Considerations

**Drug Interactions:** The interaction screen returned 100 interactions in total. The following were listed:
- **Major:** Potassium citrate, eliglustat.
- **Moderate:** Anticholinergic agents (hyoscyamine, atropine, glycopyrronium, dicyclomine, clidinium, mepenzolate, methscopolamine), opioids and CNS-active agents (morphine, loperamide, eluxadoline, dronabinol, nabilone), bupropion, lorcaserin, metoclopramide, and glycerol phenylbutyrate.

**Class-related cautions from the literature:** Sedation, cognitive and psychomotor impairment, dry mouth, dizziness, orthostatic hypotension, and additive anticholinergic burden. Rapid IV administration or large doses may cause toxicity. Newer-generation antihistamines are preferred for chronic use. The use of cough and cold medicines in young children is also questioned.

Warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available. Please refer to the PI and report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold** for rosacea conjunctivitis (the top prediction).
**Proceed with Guardrails** for rhinitis and allergic urticaria.

**Rationale:**
- Rosacea conjunctivitis has a high model score but no trials, no literature, and a weak mechanistic link, so it remains a model prediction only (L5).
- Rhinitis has the strongest evidence (L1 per the scoring; a large completed Phase 4 trial and several RCTs), and allergic urticaria has reasonable support (L3). Both largely confirm existing use, and guidelines favour second-generation antihistamines because of diphenhydramine's sedation and anticholinergic effects. Cold urticaria and trigeminal autonomic cephalalgia are research questions only.

**To proceed, the following is needed:**
- SAHPRA package insert warnings, contraindications, and approved indications (a blocking data gap)
- Mechanism of action data
- For rosacea conjunctivitis: any clinical or mechanistic evidence, ideally a pilot trial in an appropriate ocular formulation
- For rhinitis and urticaria: a South African positioning against second-generation antihistamines, with sedation and anticholinergic safeguards for elderly patients, children, and those on interacting medicines
- Route and formulation compatibility assessment (not yet completed)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

