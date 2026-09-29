---
layout: default
title: Citalopram
parent: Model Prediction Only (L5)
nav_order: 124
evidence_level: L5
indication_count: 5
---

# Citalopram
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Citalopram: From Depression to Obsessive-Compulsive Disorder

## One-Sentence Summary

Citalopram is a selective serotonin reuptake inhibitor (SSRI) marketed in South Africa, generally used as an antidepressant.
The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)**, with **30 registered clinical trials** and **15 publications** retrieved. Only 2 of the trials are graded as directly relevant, and most trial evidence concerns escitalopram, the S-enantiomer of citalopram, rather than citalopram itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression (SSRI class use; the SAHPRA records provided contain no approved-indication text) |
| Predicted New Indication | Obsessive-compulsive disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 (per Evidence Pack scoring; the supporting trials are mainly escitalopram or class-level) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, citalopram is an SSRI. Serotonergic dysfunction is a well-established mechanism in OCD, and SSRIs are first-line drug treatment for it. The high TxGNN score is consistent with this.

Depression and OCD are both treated with serotonergic drugs, which explains why the model links them. OCD often needs higher SSRI doses than depression, so dose escalation needs particular care with citalopram (see Safety Considerations).

Most of the trial evidence is for escitalopram. It supports the class and the molecule but does not directly prove efficacy of racemic citalopram in OCD. Direct citalopram OCD evidence is limited to small, older studies (see Literature Evidence).

## Clinical Trial Evidence

Of the 30 trials retrieved, the 10 most relevant are listed below. No SANCTR or PACTR identifiers were found in the Evidence Pack.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00708240](https://clinicaltrials.gov/study/NCT00708240) | Phase 4 | Unknown | 40 | Escitalopram in adolescent OCD, looking at efficacy, safety, executive function and brain activation |
| [NCT00116532](https://clinicaltrials.gov/study/NCT00116532) | Phase 4 | Completed | 30 | Escitalopram efficacy and optimal dose in OCD |
| [NCT00723060](https://clinicaltrials.gov/study/NCT00723060) | Phase 4 | Completed | 176 | Randomised, double-blind comparison of 20 mg vs 40 mg escitalopram (Y-BOCS-based); the title is truncated, so the target condition is not fully confirmed |
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Completed | 78 | ERP, SSRIs and their combination in OCD; psychotherapy is a confounder |
| [NCT00305500](https://clinicaltrials.gov/study/NCT00305500) | Phase 3 | Completed | 100 | Open-label high-dose escitalopram (up to 50 mg/day) in adult OCD, 18 weeks |
| [NCT00215137](https://clinicaltrials.gov/study/NCT00215137) | Phase 2 | Completed | 14 | Pilot study of escitalopram safety and effectiveness in OCD |
| [NCT00456937](https://clinicaltrials.gov/study/NCT00456937) | Phase 4 | Completed | 15 | Open-label escitalopram for OCD symptoms in schizophrenia |
| [NCT00680602](https://clinicaltrials.gov/study/NCT00680602) | Phase 4 | Completed | 158 | Group CBT vs fluoxetine in OCD; class-level context only |
| [NCT00086645](https://clinicaltrials.gov/study/NCT00086645) | Phase 2 | Completed | 149 | Citalopram vs placebo for repetitive behaviours in children with autism (a different condition) |
| [NCT00609531](https://clinicaltrials.gov/study/NCT00609531) | Phase 1 | Completed | 12 | fMRI study of citalopram on restricted repetitive behaviours in autism (a different condition) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35121274](https://pubmed.ncbi.nlm.nih.gov/35121274/) | 2022 | Network meta-analysis | J Psychiatr Res | Compares drug therapy, psychological therapy and their combination in children and adolescents with OCD |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Meta-review | Front Psychiatry | Efficacy, tolerability and suicidality of antidepressants across paediatric disorders, including OCD |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Meta-analysis | J Affect Disord | OCD shows a reduced placebo and antidepressant response compared with other anxiety disorders |
| [38703743](https://pubmed.ncbi.nlm.nih.gov/38703743/) | 2024 | Systematic review | Compr Psychiatry | Long-term safety and tolerability of off-label high-dose serotonin reuptake inhibitors in OCD |
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | Randomised open-label trial | Eur Psychiatry | Citalopram alone vs citalopram plus clomipramine in treatment-resistant OCD (16 adults, 90 days) |
| [12839522](https://pubmed.ncbi.nlm.nih.gov/12839522/) | 2003 | Open-label study | Psychiatry Clin Neurosci | Citalopram (20-30 mg/day) in 15 children and adolescents with OCD, 8 weeks |
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | Review/commentary | Int Clin Psychopharmacol | Citalopram for OCD in the context of the long link between serotonin reuptake inhibitors and OCD |
| [12607204](https://pubmed.ncbi.nlm.nih.gov/12607204/) | 2000 | Review | World J Biol Psychiatry | OCD responds to serotonergic medication and psychological treatment; neurobiology overview |
| [34313207](https://pubmed.ncbi.nlm.nih.gov/34313207/) | 2022 | Pharmacogenetic study | CNS Spectrums | Effect of the BDNF Val66Met polymorphism on response to escitalopram or paroxetine in OCD |
| [30973183](https://pubmed.ncbi.nlm.nih.gov/30973183/) | 2019 | Imaging study | Psychiatry Clin Neurosci | Brain neurochemistry in unmedicated OCD and its change after 12 weeks of escitalopram |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 36/1.2/0469 | Citalopram 20 Oethmaan | Fct (as recorded) |
| Reg. No. A39/1.2/0548 | Cilate | Tablet |
| Reg. No. 41/1.2/0458 | Drl Citalopram 20 | Tablet |
| Reg. No. A38/1.2/0548 | Tamomilt | Tablet |

Approved-indication text was not captured for any of these registrations, so the original indication should be confirmed against the SAHPRA-approved Professional Information (PI).

## Safety Considerations

- **QT prolongation:** Citalopram has a dose-dependent QT-prolongation limit. The maximum dose is 40 mg/day, and lower in older adults and CYP2C19 poor metabolisers. OCD often needs higher SSRI doses, so any dose escalation must be paired with an ECG and an interaction review.

Otherwise, please refer to the SAHPRA-approved Professional Information (PI) for warnings, contraindications and drug interactions. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is well established and OCD is a recognised SSRI-responsive condition. Multiple completed trials in OCD support escitalopram, and small studies exist for citalopram itself. However, direct evidence for racemic citalopram is limited and dated, and safety data for this pack are missing.

**To proceed, the following is needed:**
- SAHPRA package-insert warnings and contraindications (a blocking gap for safety screening)
- Citalopram-specific OCD efficacy data, or an explicit decision to extrapolate from escitalopram
- A dosing and monitoring plan covering the 40 mg/day ceiling, ECG monitoring, CYP2C19 status and interaction review
- Confirmation of the approved indications for the 4 SAHPRA registrations

The other predicted indications (histrionic, schizotypal, paranoid and schizoid personality disorders) have no supporting trials or relevant literature and are on **Hold**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

