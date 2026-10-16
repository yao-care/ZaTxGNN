---
layout: default
title: Lorazepam
parent: Model Prediction Only (L5)
nav_order: 302
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Lorazepam: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Anxiety disorder and seizure conditions (status epilepticus…"
---

# Lorazepam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Lorazepam: From Anxiety and Epilepsy Indications to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Lorazepam is a benzodiazepine originally used for anxiety disorders and several seizure conditions, including status epilepticus, absence epilepsy and Lennox-Gastaut syndrome.
The TxGNN model's top-ranked prediction is **trigeminal nerve neoplasm**, but **no clinical trials and no publications** support it, so it is a model prediction only.
Among the other predicted indications, **insomnia** has the most direct supporting literature (two older small clinical studies), and the predicted reflex-seizure conditions are extensions of existing seizure uses.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorder and seizure conditions (status epilepticus, absence epilepsy, Lennox-Gastaut syndrome and others). SAHPRA indication text was not available in the data compiled for this report. |
| Predicted New Indication | Trigeminal nerve neoplasm (top-ranked prediction) |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

**Other predicted indications reviewed**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 1 | Trigeminal nerve neoplasm | 99.87% | L5 | Hold |
| 2 | Insomnia | 99.80% | L3 | Research Question |
| 3 | Reading seizures | 99.64% | L4 | Hold |
| 4 | Audiogenic seizures | 99.63% | L4 | Hold |
| 5 | Eating seizures | 99.63% | L5 | Hold |
| 6 | Orgasm-induced seizures | 99.63% | L5 | Hold |
| 7 | Thinking seizures | 99.63% | L4 | Hold |
| 8 | Startle epilepsy | 99.63% | L5 | Hold |
| 9 | Micturition-induced seizures | 99.63% | L4 | Hold |
| 10 | Acute encephalopathy with biphasic seizures and late reduced diffusion | 99.47% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Lorazepam is known to be a benzodiazepine that enhances GABA-A receptor-mediated inhibition, which produces sedative, anxiolytic and anticonvulsant effects.

**Trigeminal nerve neoplasm (top prediction):** No mechanistic rationale supports this prediction. The high score comes from the graph-based model alone, and there is no plausible anti-tumour link. At most, lorazepam could treat symptoms such as anxiety or seizures in a patient with a tumour, and these uses are already covered by existing indications.

**Insomnia:** Enhanced GABA-A inhibition is a well-established mechanism for sedative-hypnotic effects, so the prediction is plausible. Insomnia is also close to the existing anxiety indications, so this is more a question of labelling and regional use than true repurposing. Benzodiazepines are generally reserved for short-term use because of dependence, tolerance, cognitive impairment and fall risk, especially in older adults.

**Seizure-related predictions (reading, audiogenic, eating, orgasm-induced, thinking, startle and micturition-induced seizures):** These are reflex or trigger-specific seizure types. GABAergic potentiation is a reasonable class-level rationale, and lorazepam is already used in status epilepticus, absence epilepsy and Lennox-Gastaut syndrome. These predictions are therefore extensions within the same therapeutic area, but none has direct supporting evidence.

**Acute encephalopathy with biphasic seizures and late reduced diffusion:** Lorazepam could control acute seizures symptomatically. It would not address the underlying excitotoxic injury.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted indications in the data compiled for this report.

---

## Literature Evidence

**Trigeminal nerve neoplasm:** Currently no related literature available.

**Insomnia (most relevant publications)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3280615](https://pubmed.ncbi.nlm.nih.gov/3280615/) | 1988 | Double-blind crossover study (8 chronic insomniacs) | J Clin Pharmacol | Lorazepam 2 mg performed better than flurazepam 30 mg on most sleep parameters over 3 weeks |
| [10220122](https://pubmed.ncbi.nlm.nih.gov/10220122/) | 1999 | Clinical study | Int Clin Psychopharmacol | Compared lorazepam 0.5 mg TID (24-hour treatment) with 1.5 mg at bedtime in primary insomnia; the study design could not be confirmed from the data |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Review | Med Lett Drugs Ther | Overview of drugs for chronic insomnia |
| [35087274](https://pubmed.ncbi.nlm.nih.gov/35087274/) | 2022 | Review | J Multidiscip Healthc | Insomnia therapy and drug interactions in COVID-19 patients |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | Pharmacokinetics of anxiolytic drugs |

**Reading seizures**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11593256](https://pubmed.ncbi.nlm.nih.gov/11593256/) | 2001 | Case series | Neurol India | Lorazepam as adjuvant therapy in five patients with photosensitive epilepsy and heliotaxis (a related reflex epilepsy, not reading seizures) |
| [21951369](https://pubmed.ncbi.nlm.nih.gov/21951369/) | 2011 | Review | CNS Neurosci Ther | Acute drug administration in epilepsy |
| [30877186](https://pubmed.ncbi.nlm.nih.gov/30877186/) | 2019 | Phase 2a study | Neurology | Selective GABA potentiator PF-06372865 in photosensitive epilepsy (a different drug, not lorazepam) |

**Audiogenic seizures:** Only animal studies are available. Examples are [6127668](https://pubmed.ncbi.nlm.nih.gov/6127668/) (1981, Pol J Pharmacol Pharm), in which lorazepam depressed audiogenic seizures in rodents, and four rat lorazepam-withdrawal studies (PMIDs [10744342](https://pubmed.ncbi.nlm.nih.gov/10744342/), [11526976](https://pubmed.ncbi.nlm.nih.gov/11526976/), [10225031](https://pubmed.ncbi.nlm.nih.gov/10225031/) and [8707372](https://pubmed.ncbi.nlm.nih.gov/8707372/)). These address dependence and withdrawal, not treatment of human audiogenic seizures.

**Micturition-induced seizures (indirect evidence only):** The retrieved papers address benzodiazepines in status epilepticus and seizure clusters, not this specific condition.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22335736](https://pubmed.ncbi.nlm.nih.gov/22335736/) | 2012 | RCT | N Engl J Med | Intramuscular vs intravenous therapy for prehospital status epilepticus |
| [21967361](https://pubmed.ncbi.nlm.nih.gov/21967361/) | 2011 | RCT design paper | Epilepsia | RAMPART: IM midazolam vs IV lorazepam in prehospital status epilepticus |
| [35971024](https://pubmed.ncbi.nlm.nih.gov/35971024/) | 2022 | Review | CNS Drugs | Benzodiazepine routes of delivery, efficacy and tolerability in seizures |
| [35333156](https://pubmed.ncbi.nlm.nih.gov/35333156/) | 2022 | Evidence synthesis | Health Technol Assess | Pre-hospital and emergency treatment of convulsive status epilepticus in adults |

**Thinking seizures:** Only indirect papers were retrieved, including [30764](https://pubmed.ncbi.nlm.nih.gov/30764/) (1978, pharmacology of lorazepam) and [22926232](https://pubmed.ncbi.nlm.nih.gov/22926232/) (2014, a case report of propylene glycol toxicity, a safety signal relevant to parenteral lorazepam formulations).

**Eating seizures:** The single retrieved paper concerns a different drug (cyamemazine) in rodent ethanol withdrawal and is not relevant.

**Orgasm-induced seizures, startle epilepsy, and acute encephalopathy with biphasic seizures and late reduced diffusion:** Currently no related literature available.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| R/2.6/319 | Ativan SL | Sublingual tablet | Not available in the data compiled for this report |
| D/2.6/128 | Ativan | Tablet | Not available in the data compiled for this report |
| X/2.6/82 | Ativan | Tablet | Not available in the data compiled for this report |

All three registrations are valid single-ingredient products. Essential Medicines List (EML) inclusion status was not available in the data compiled for this report. The approved indication text and the packaged warnings from the SAHPRA Professional Information (PI) still need to be retrieved.

---

## Safety Considerations

**Contraindications and conditions of concern (from the knowledge graph, not from label text):**
Liver failure, liver disease, hepatic encephalopathy and hepatic coma; kidney disease; respiratory failure, obstructive sleep apnoea and congenital central hypoventilation syndrome; open-angle and angle-closure glaucoma; porphyria; substance-related disorders and substance abuse/dependence; gallbladder disease; pyoureter. The knowledge graph also lists anxiety disorder, neurotic disorder and dysthymic disorder, which appear inconsistent with lorazepam's own anxiety indication. These entries should be verified against the PI.

**Drug interactions:** The interaction screen returned 100 interactions in total. Of the 20 listed in the data compiled for this report, the main ones are:
- **Major:** Morphine, and liposomal morphine (additive central nervous system and respiratory depression)
- **Moderate:** Bupropion, dronabinol, nabilone, metoclopramide, opium, sibutramine, teduglutide
- **Minor:** Antacids and magnesium or aluminium salts (magnesium oxide, aluminium hydroxide, calcium carbonate, magaldrate, magnesium carbonate, magnesium hydroxide)

**Other safety signals from the literature:**
- Benzodiazepines carry risks of dependence, tolerance, cognitive impairment and falls, especially in older adults.
- Propylene glycol toxicity has been reported with intravenous lorazepam infusion.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction, trigeminal nerve neoplasm, has no trials, no literature and no plausible mechanism, so it should not be pursued.
- Insomnia is the only prediction with direct human data on lorazepam (two small, dated studies). It is better treated as a research question about labelling and short-term use than as true repurposing.
- The seizure-related predictions extend existing seizure uses but have no direct evidence.

**To proceed, the following is needed:**
- Retrieve the SAHPRA Professional Information to obtain approved indications, warnings and contraindications. This is a blocking gap for safety screening.
- Obtain mechanism of action data from DrugBank.
- For insomnia, review current guidelines, short-term use limits and fall and dependence risks, particularly in older adults, and confirm whether insomnia is already covered by the registered indications.
- For the seizure-related predictions, seek condition-specific clinical evidence beyond general status epilepticus data.
- Confirm Essential Medicines List status and route compatibility for any new indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

