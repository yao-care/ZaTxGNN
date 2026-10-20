---
layout: default
title: Zolpidem
parent: Model Prediction Only (L5)
nav_order: 482
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Zolpidem: predicted new indication Sleep disorder, initiating and maintaining sleep (evidence level L5). Approved use: Insomnia"
monitor_inn: "Zolpidem"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia", "acute encephalopathy with biphasic seizures and late reduced diffusion", "Wernicke-Korsakoff syndrome", "manic bipolar affective disorder", "alcohol withdrawal", "major affective disorder", "anxiety", "epilepsy, childhood absence, susceptibility to"]
---

# Zolpidem
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

# Zolpidem: From Insomnia to Sleep Disorder (Initiating and Maintaining Sleep)

## One-Sentence Summary

Zolpidem is a sedative-hypnotic originally used to treat insomnia.
The TxGNN model's top-ranked prediction is **sleep disorder, initiating and maintaining sleep**, with **20 publications** (including a network meta-analysis and a clinical practice guideline) supporting this direction. Note that this is essentially the drug's existing, approved use rather than true repurposing. The data compiled for this report also assessed nine other predicted indications, and none of them has solid supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Insomnia (no approved indication text is recorded in the SAHPRA registration data; the original indication comes from the TxGNN knowledge graph) |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L1 per the data compiled for this report (based on guidelines, systematic reviews and meta-analyses, plus two completed Phase 3 zolpidem MR insomnia trials; no trial is listed directly under this indication) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the structured drug record. From the literature compiled for this report, zolpidem is a non-benzodiazepine "Z-drug" that acts as a positive allosteric modulator of GABA-A receptors, binding preferentially to the alpha-1 subunit. This promotes sleep onset.

The predicted indication, a sleep disorder involving difficulty initiating and maintaining sleep, is essentially the same condition as insomnia, the drug's original indication. The prediction is therefore mechanistically coherent, but it is **on-label use, not new repurposing**.

Zolpidem's alpha-1 selectivity also explains why the other predicted indications (for example anxiety, agoraphobia, alcohol withdrawal and seizure-related conditions) are weakly supported. In those conditions zolpidem has little anxiolytic or anticonvulsant activity, and its dependence and sedation risks argue against use.

---

## Clinical Trial Evidence

No clinical trials are listed directly under the top-ranked indication. Two completed Phase 3 trials of zolpidem MR in insomnia appear in the data under a different predicted indication (manic bipolar affective disorder). They are insomnia trials rather than bipolar trials, so they support the on-label insomnia use.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00374777](https://clinicaltrials.gov/study/NCT00374777) | Phase 3 | Completed | 450 | Double-blind, placebo- and nitrazepam-controlled study of zolpidem MR in insomnia associated with schizophrenia and manic-depressive psychosis |
| [NCT00999219](https://clinicaltrials.gov/study/NCT00999219) | Phase 3 | Completed | 55 | Double-blind crossover polysomnography study of zolpidem MR in insomnia, excluding schizophrenia and manic-depressive psychosis |
| [NCT00296790](https://clinicaltrials.gov/study/NCT00296790) | Phase 4 | Completed | 372 | Ambien CR vs placebo for insomnia associated with generalised anxiety disorder, given with escitalopram |
| [NCT06303076](https://clinicaltrials.gov/study/NCT06303076) | Phase 4 | Not yet recruiting | 90 | Tizanidine vs zolpidem 10 mg in primary insomnia (zolpidem as comparator; no results) |

No SANCTR or PACTR identifiers are available in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Systematic review / network meta-analysis | Lancet | Comparative effectiveness of drug treatments for acute and long-term management of insomnia disorder in adults |
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Clinical practice guideline | J Clin Sleep Med | American Academy of Sleep Medicine recommendations for drug treatment of chronic insomnia |
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | Phase 3 RCT | JAMA Netw Open | Lemborexant vs placebo and zolpidem extended release in older adults with insomnia |
| [22424586](https://pubmed.ncbi.nlm.nih.gov/22424586/) | 2012 | Review | Expert Opin Pharmacother | Zolpidem as a benzodiazepine-receptor agonist and the most widely prescribed hypnotic in the US |
| [29487083](https://pubmed.ncbi.nlm.nih.gov/29487083/) | 2018 | Review | Pharmacol Rev | Insomnia drugs beyond benzodiazepines; notes cognitive impairment, tolerance, falls and dependence with Z-drugs |
| [28671376](https://pubmed.ncbi.nlm.nih.gov/28671376/) | 2017 | Review | Am Fam Physician | Z-drugs reserved for use if first-line agents are ineffective; melatonin and doxepin preferred in older adults |
| [16696581](https://pubmed.ncbi.nlm.nih.gov/16696581/) | 2006 | Drug review | CNS Drugs | Zolpidem extended-release formulation for sleep onset and maintenance |
| [37549414](https://pubmed.ncbi.nlm.nih.gov/37549414/) | 2023 | Review | J Fam Pract | Insomnia management update for primary care |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | Clin Ther | Safety and efficacy of sleep medicines in older adults |
| [32406572](https://pubmed.ncbi.nlm.nih.gov/32406572/) | 2020 | Database study | J Sleep Res | Zolpidem overutilisation among Korean patients with insomnia |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. A40/2.2/0441 | Stilnox 12.5 MR | Tablet | Not recorded in the data compiled for this report |
| Reg. No. 37/2.2/0540 | Ivedal | Tablet | Not recorded in the data compiled for this report |
| Reg. No. A40/2.2/0041 | Stilnox MR | Srt (sustained-release tablet) | Not recorded in the data compiled for this report |

All three registrations are valid single-ingredient products. The data compiled for this report does not state Essential Medicines List (EML) status.

---

## Safety Considerations

SAHPRA package-insert warnings and contraindications were not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Knowledge-graph contraindication signals** (these come from drug-disease graph edges, not from label text, and must be verified against the PI): anxiety disorder, neurotic disorder, dysthymic disorder, liver disease, gallbladder disease, obstructive sleep apnoea, sleep apnoea syndrome, congenital central hypoventilation syndrome, amnestic disorder, retrograde amnesia, substance-related disorder, substance abuse/dependence, and attention deficit hyperactivity disorder.

**Drug interactions:** 100 interactions were identified; the first 20 retrieved are summarised below.
- **Major:** morphine and liposomal morphine (additive CNS and respiratory depression is the expected concern).
- **Moderate:** bupropion, aprepitant, dexamethasone, cimetidine, clarithromycin, dronabinol, nabilone, metoclopramide, miconazole, clotrimazole, glycerol phenylbutyrate, opium, sibutramine, troglitazone.
- **Unknown severity:** calcitriol, vitamin A, phentermine, pantoprazole.

**Safety signals in the literature:** reports of zolpidem dependence, abuse, withdrawal delirium, zolpidem-induced mania, and a population-based association with suicide, as well as falls and fractures in patients with cirrhosis.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top-ranked prediction coincides with zolpidem's established insomnia use. It is supported by a guideline, a network meta-analysis, reviews and completed Phase 3 insomnia trials, and the drug is already marketed in South Africa under three registrations. This is a confirmation of on-label use, not a new repurposing opportunity.

**Other predicted indications in the data compiled for this report:**

| Predicted Indication | Score | Evidence Level | Recommendation |
|------|------|------|------|
| Anxiety | 94.69% | L2 | Research Question (benefit is for anxiety-related insomnia, not anxiety itself) |
| Major affective disorder | 94.94% | L3 | Research Question (symptomatic sleep benefit as add-on to antidepressants) |
| Manic bipolar affective disorder | 95.93% | L4 | Hold (reports of zolpidem-induced mania) |
| Alcohol withdrawal | 95.00% | L4 | Hold (literature is mainly about withdrawal and dependence) |
| Benign paroxysmal torticollis of infancy, agoraphobia, acute encephalopathy with biphasic seizures, Wernicke-Korsakoff syndrome, childhood absence epilepsy | 92.8-99.3% | L5 | Hold (no clinical evidence) |

**To proceed, the following is needed:**
- The SAHPRA-approved package insert, to obtain warnings, contraindications, approved indications and complex-sleep-behaviour precautions.
- Mechanism of action data from DrugBank.
- Prescribing guardrails: short-term use, lowest effective dose, caution in older adults, hepatic impairment, sleep apnoea and substance-use history, and screening for interacting CNS depressants (especially opioids).
- If the sleep-in-comorbid-depression or anxiety questions are pursued, a properly designed trial with those conditions as the enrolled population.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

