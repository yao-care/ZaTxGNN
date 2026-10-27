---
layout: default
title: Fentanyl
parent: Model Prediction Only (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Fentanyl: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not stated in the SAHPRA registration data compiled for this report"
monitor_inn: "Fentanyl"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome", "trichotillomania", "myofascial pain syndrome", "manic bipolar affective disorder", "migraine with brainstem aura", "methemoglobinemia", "myositis fibrosa", "idiopathic granulomatous myositis", "tendinitis"]
---

# Fentanyl
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

## Fentanyl: From Pain Management to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Fentanyl is a potent mu-opioid analgesic registered in South Africa as an injection and as an effervescent buccal tablet.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but **no clinical trials and no publications** currently support this prediction, so it is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data compiled for this report |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Fentanyl is a well-known synthetic mu-opioid receptor agonist used for analgesia and anaesthesia.

NSIAD is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2), which leads to water retention and low sodium despite suppressed vasopressin. Fentanyl has no established mechanistic link to this pathway. Opioids can modulate antidiuretic hormone release in general, but that acts upstream of the receptor, which is the defect in NSIAD. The high score is therefore best treated as a hypothesis-generating output of the model rather than a rational therapeutic lead.

Other top-ranked predictions were also reviewed. They are summarised below to give context.

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Tourette syndrome | 99.05% | L5 | No studies. Abuse liability and respiratory depression argue against use |
| 3 | Trichotillomania | 98.87% | L4 | One 2002 mechanistic study only. Opioid antagonists are the more plausible direction |
| 4 | Myofascial pain syndrome | 98.09% | L4 | Mechanistically plausible for pain, but the only Phase 3 trial is unverified |
| 5 | Manic bipolar affective disorder | 97.73% | L5 | Keyword matches only (overdose, case reports, "bipolar scissors") |
| 6 | Migraine with brainstem aura | 97.71% | L5 | A single unrelated case report. Opioids are not recommended in migraine |
| 7 | Methemoglobinemia | 97.22% | L5 | Co-occurrence hits only |
| 8–9 | Myositis fibrosa and idiopathic granulomatous myositis | 97.04% | L5 | No studies. Identical scores suggest shared graph neighbours |
| 10 | Tendinitis | 97.04% | L4 | Postoperative analgesia only, not treatment of tendinitis |

Myofascial pain syndrome is the only alternative with a plausible mechanism (mu-opioid analgesia), and it is the one flagged for follow-up research. However, long-term opioid use for myofascial pain is generally discouraged because benefit is limited and risk is substantial.

---

## Clinical Trial Evidence

For the primary prediction (NSIAD), currently no related clinical trials are registered.

For the secondary candidate, myofascial pain syndrome, one trial was retrieved:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00343733](https://clinicaltrials.gov/study/NCT00343733) | Phase 3 | Completed | 120 | 12-week open-label study with within-patient double-blind placebo-controlled periods of OraVescent fentanyl for breakthrough pain in opioid-tolerant patients with noncancer chronic pain. Relevance to myofascial pain is unconfirmed (grade C) |

No SANCTR or PACTR identifiers were found.

---

## Literature Evidence

For the primary prediction (NSIAD), currently no related literature is available.

Selected publications for secondary candidates:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12369265](https://pubmed.ncbi.nlm.nih.gov/12369265/) | 2002 | Mechanistic challenge study | Prog Neuropsychopharmacol Biol Psychiatry | Fentanyl-induced prolactin response used as an opiate sensitivity test in stereotypic movement disorder and trichotillomania. Suggests endogenous opioid involvement but no therapeutic benefit shown |
| [21419546](https://pubmed.ncbi.nlm.nih.gov/21419546/) | 2011 | Review | J Oral Maxillofac Surg | Long-term opioid use in temporomandibular joint dysfunction can be neither supported nor refuted by current evidence |
| [23809446](https://pubmed.ncbi.nlm.nih.gov/23809446/) | 2013 | RCT | Arthroscopy | Transdermal fentanyl patch versus subacromial bupivacaine infusion for pain after arthroscopic shoulder surgery (postoperative pain, not tendinitis itself) |
| [11097669](https://pubmed.ncbi.nlm.nih.gov/11097669/) | 2000 | RCT | Reg Anesth Pain Med | Intra-articular morphine, fentanyl or sufentanil added to bupivacaine for pain after rotator cuff repair |
| [16923824](https://pubmed.ncbi.nlm.nih.gov/16923824/) | 2007 | RCT | Am J Sports Med | Patient-controlled analgesia after arthroscopic rotator cuff repair: subacromial catheter versus intravenous |

The remaining retrieved papers (opioid overdose, drug screening, methemoglobinemia case reports, veterinary and antiemetic studies) are keyword matches and do not show therapeutic benefit.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 29/2.7/0605 | Pharma-q fentanyl ampoule 2ml | Injection | Not available in the compiled data |
| Reg. No. 48/2.9/0054 | Effentora 100 | Effervescent tablet | Not available in the compiled data |

Both registrations are valid single-ingredient products. Essential Medicines List (EML) status could not be determined from the compiled data.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (these are model-graph associations, not label text):
Hypertension and hypotensive disorders, orthostatic hypotension, long QT syndrome and torsades de pointes, chronic obstructive pulmonary disease, asthma, liver and kidney disease, liver failure, pancreatitis, gallbladder disease, inflammatory bowel disease, benign prostatic hyperplasia, anxiety and related disorders, potassium deficiency, and substance abuse/dependence.

**Drug Interactions** (100 interactions recorded; examples):
- **Major:** alvimopan, aprepitant, bupropion, clarithromycin, clotrimazole, dexamethasone, dolasetron, granisetron, fenfluramine, dexfenfluramine, lorcaserin
- **Moderate:** atropine, cimetidine, clidinium, dicyclomine, dronabinol, eluxadoline, glycopyrronium, hyoscyamine, glycerol phenylbutyrate

Please refer to the SAHPRA-approved Professional Information (PI) for authoritative warnings and contraindications. Report adverse drug reactions to SAHPRA. Abuse liability and respiratory depression are well-recognised opioid concerns.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The NSIAD prediction rests only on a model score, with no trials, no literature, and no plausible mechanism, since the disease arises at the vasopressin V2 receptor. Fentanyl also carries significant safety risks that are not justified by this evidence.

**To proceed, the following is needed:**
- Fentanyl mechanism of action data and the SAHPRA PI warnings and contraindications (currently missing and blocking safety screening)
- Approved indication text for the two SAHPRA registrations
- Any preclinical or mechanistic evidence linking mu-opioid signalling to AVPR2-driven antidiuresis
- Manual verification of NCT00343733 (intervention and condition) if myofascial pain is pursued as a research question
- Route compatibility assessment against available injectable and buccal formulations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

