---
layout: default
title: Benzylpenicillin
parent: 僅模型預測 (L5)
nav_order: 64
evidence_level: L5
indication_count: 10
---

# Benzylpenicillin
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

# Benzylpenicillin: From Bacterial Infections to Pericoronitis

## One-Sentence Summary

Benzylpenicillin (Penicillin G) is a foundational beta-lactam antibiotic used globally for the treatment of susceptible bacterial infections caused by gram-positive cocci and anaerobic organisms, with more than 75 years of clinical application. The TxGNN model predicts it may be effective for **pericoronitis** — an acute bacterial infection of the soft tissue surrounding a partially erupted wisdom tooth — achieving a prediction score of **99.36%**. However, the current evidence dataset contains **0 registered clinical trials** and **0 indexed publications** specifically pairing this drug with this indication, reflecting a documentation gap rather than a true absence of clinical support.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Susceptible bacterial infections (no SAHPRA registration on record) |
| Predicted New Indication | Pericoronitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Benzylpenicillin belongs to the beta-lactam antibiotic class. Its efficacy in treating susceptible gram-positive and anaerobic bacterial infections is among the most established facts in clinical pharmacology, and mechanistically it is directly applicable to the oral pathogens responsible for pericoronitis.

Pericoronitis is an acute bacterial infection of the pericoronal operculum — the soft tissue flap overlying a partially erupted mandibular third molar. The primary causative organisms include oral streptococci (*Streptococcus spp.*), *Fusobacterium nucleatum*, *Prevotella intermedia*, and other anaerobes that constitute the mixed oral flora. All of these organisms are well within Benzylpenicillin's antimicrobial spectrum, particularly its activity against gram-positive cocci and its coverage of many penicillin-susceptible anaerobes.

The high TxGNN score of 99.36% reflects this deeply established pharmacological alignment. In current dental clinical guidelines (including those from the British National Formulary and the American Dental Association), penicillin-class antibiotics remain the recommended first-line adjunctive antibiotic for moderate-to-severe pericoronitis. The absence of formally indexed clinical trials in this dataset is best understood as a reflection of the fact that this indication is so clinically well-accepted that it rarely generates prospective randomised trials — clinicians proceed on the basis of longstanding consensus.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although Benzylpenicillin has a mechanistically compelling and clinically well-accepted rationale for pericoronitis, this evidence pack contains no indexed clinical trials or publications to formally support the drug-disease pair, and Benzylpenicillin is not currently registered with SAHPRA — making a direct clinical recommendation within South Africa premature without further regulatory and evidence review.

**To proceed, the following is needed:**
- Targeted literature search in dental medicine databases (Cochrane Oral Health, Journal of Dental Research, British Dental Journal) using "penicillin" and "pericoronitis" search terms to surface guideline recommendations not captured by the current ClinicalTrials.gov and PubMed queries
- Assessment of SAHPRA registration status for Benzylpenicillin (injectable) and its oral analogue phenoxymethylpenicillin (Penicillin V), which may be more practical in the South African primary dental care context
- Review of South African Essential Medicines List (EML) and Standard Treatment Guidelines (STGs) for oral infections to determine whether penicillin-class agents are already listed for pericoronitis at the primary care level
- Antimicrobial resistance surveillance data for oral pathogens in South Africa (SANRESIS / GERMS-SA) to confirm ongoing susceptibility of pericoronitis pathogens to Benzylpenicillin
- Penicillin allergy prevalence data in the South African population, with particular attention to communities where beta-lactam exposure history may affect prescribing decisions

> **Broader Evidence Landscape Note:** Of the 10 predicted indications in this evidence pack, **canker sore (recurrent aphthous stomatitis)** — ranked 3rd (TxGNN score 99.27%) — carries substantially stronger direct evidence (Evidence Level **L2**, recommended decision **"Proceed with Guardrails"**). Multiple randomised controlled trials directly evaluated topical Penicillin G potassium troches (Cankercillin) for recurrent aphthous ulcers, including a multicentre Chinese RCT (PMID [20188604](https://pubmed.ncbi.nlm.nih.gov/20188604/)) and a 2020 double-blind RCT (PMID [33273940](https://pubmed.ncbi.nlm.nih.gov/33273940/)). Healthcare professionals evaluating Benzylpenicillin repurposing in the oral medicine context should prioritise canker sore as the indication with the strongest drug-specific clinical evidence.

---

*This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. This document has been generated using the TxGNN drug repurposing prediction system (data cutoff: 2026-04-04). Clinicians are advised to consult the SAHPRA-approved Professional Information and current South African Standard Treatment Guidelines. Adverse drug reactions should be reported to SAHPRA via the MedSafety reporting system.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

