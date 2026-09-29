---
layout: default
title: Zolpidem
parent: High Evidence (L1-L2)
nav_order: 478
evidence_level: L2
indication_count: 10
---

# Zolpidem
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Zolpidem: From Insomnia (Established Use) to Sleep Disorder, Initiating and Maintaining Sleep

## One-Sentence Summary

Zolpidem is a non-benzodiazepine hypnotic. The SAHPRA records supplied contain no indication text, so its established use as a sleep aid comes from general pharmacology. The TxGNN model predicts it for **sleep disorder, initiating and maintaining sleep**, backed by **19 publications** (including several systematic reviews and network meta-analyses) but **no registered clinical trials** attached to this prediction. This is a rediscovery of zolpidem's existing insomnia use rather than true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L3 by this report's rubric (systematic reviews and meta-analyses; no completed trials attached). The upstream pack labelled it L1. |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. From general pharmacology, zolpidem is a positive allosteric modulator of GABA-A receptors at the benzodiazepine site, with preferential affinity for the alpha1 subunit. This produces its sedative-hypnotic effect.

Difficulty falling or staying asleep is exactly what alpha1-mediated sedation treats, so the high score is expected. Zolpidem is an existing hypnotic, and the literature reviews it as a standard option for insomnia, including the extended-release form. The model has effectively rediscovered the drug's label use, which is a useful sanity check but adds no new therapeutic direction.

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific prediction.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | RCT (Phase 3) | JAMA Netw Open | Lemborexant vs placebo and zolpidem ER in older adults with insomnia disorder; zolpidem ER is the active comparator |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Network meta-analysis | Lancet | Comparative effectiveness of drug treatments for acute and long-term management of adult insomnia |
| [34688027](https://pubmed.ncbi.nlm.nih.gov/34688027/) | 2021 | Meta-analysis | Sleep Med | Efficacy and safety of zolpidem over one month in insomnia disorder, pooling randomized placebo-controlled trials |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | Network meta-analysis | J Manag Care Spec Pharm | Compares lemborexant with other insomnia treatments on efficacy and safety |
| [36472134](https://pubmed.ncbi.nlm.nih.gov/36472134/) | 2023 | Comparative analysis | J Clin Sleep Med | Lemborexant vs zolpidem ER 6.25 mg vs placebo in short and normal sleep-duration insomnia subtypes |
| [37477771](https://pubmed.ncbi.nlm.nih.gov/37477771/) | 2023 | Post hoc analysis | CNS Drugs | Effect of daridorexant and zolpidem on night-time wake bouts in insomnia |
| [29487083](https://pubmed.ncbi.nlm.nih.gov/29487083/) | 2018 | Review | Pharmacol Rev | Z-drugs, including zolpidem, are approved for insomnia with a strong evidence base but carry cognitive impairment, tolerance, rebound insomnia, falls and dependence risks |
| [16696581](https://pubmed.ncbi.nlm.nih.gov/16696581/) | 2006 | Review | CNS Drugs | Zolpidem extended-release (dual-layer tablet) for sleep onset and maintenance difficulties |
| [22424586](https://pubmed.ncbi.nlm.nih.gov/22424586/) | 2012 | Review | Expert Opin Pharmacother | Zolpidem acts as a benzodiazepine receptor agonist and is the most widely prescribed hypnotic in the US |
| [38551874](https://pubmed.ncbi.nlm.nih.gov/38551874/) | 2024 | Review | Rev Prat | CBT is first-line; Z-drugs taken at the right time and dose help sleep initiation with fewer harms than long-acting benzodiazepines |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. A40/2.2/0441 | Stilnox 12.5 Mr | Tablet |
| Reg. No. 37/2.2/0540 | Ivedal | Tablet |
| Reg. No. A40/2.2/0041 | Stilnox mr | Srt (as recorded) |

Approved indication text is not included in the registration records supplied.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The supplied literature also repeatedly flags dependence, withdrawal and misuse (for example PMIDs 29487083 and 39496046), so duration and dose limits matter.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top prediction matches zolpidem's established hypnotic use and is supported by systematic reviews and meta-analyses. Safety data from the SAHPRA package insert is still missing, so the drug should be used only with short-term, lowest-effective-dose safeguards.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings and contraindications), which blocks the safety screening step
- Mechanism-of-action data from DrugBank
- Confirmation of the approved indication wording on each of the 3 registrations

**Other predicted indications (not recommended for advancement):**

| Predicted Indication | Evidence Level | Decision | Note |
|------|------|------|------|
| Major affective disorder | L2 | Research Question | Supports zolpidem ER as an adjunct for insomnia with depression, not for depression itself |
| Anxiety | L2 | Research Question | Supports zolpidem ER for insomnia with generalized anxiety disorder, not as an anxiolytic |
| Manic bipolar affective disorder | L3 | Research Question | Evidence concerns comorbid insomnia and dependence reports, with no effect shown on mania |
| Alcohol withdrawal | L4 | Hold | Mostly zolpidem withdrawal and dependence reports; cross-tolerance and misuse concerns |
| Benign paroxysmal torticollis of infancy | L5 | Hold | No evidence; likely a graph-proximity artifact |
| Agoraphobia | L5 | Hold | No evidence; weak anxiolytic activity and dependence risk |
| Acute encephalopathy with biphasic seizures and late reduced diffusion | L5 | Hold | No evidence or supported rationale |
| Wernicke-Korsakoff syndrome | L5 | Hold | No evidence; sedative-hypnotics may worsen confusion in this population |
| Childhood absence epilepsy, susceptibility to | L5 | Hold | No evidence; some GABAergic agents can aggravate absence seizures |

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

