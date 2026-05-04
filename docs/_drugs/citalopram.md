---
layout: default
title: Citalopram
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 5
---

# Citalopram
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Citalopram: From Depression to Obsessive-Compulsive Disorder

## One-Sentence Summary

Citalopram is a Selective Serotonin Reuptake Inhibitor (SSRI) established internationally as a treatment for major depressive disorder, though it is not currently registered in South Africa. The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)**, supported by multiple completed clinical trials using its pharmacologically active enantiomer (escitalopram) and by **direct clinical evidence** of citalopram itself in treatment-resistant OCD. Given the well-characterised serotonergic neurobiology of OCD and SSRIs' recognised first-line status in international guidelines, this prediction is mechanistically compelling.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major Depressive Disorder (established international use; no SAHPRA registration on record) |
| Predicted New Indication | Obsessive-Compulsive Disorder (OCD) |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 |
| South Africa Market Status | Not registered in South Africa |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Citalopram acts by blocking the serotonin transporter (SERT), which increases synaptic serotonin (5-HT) concentrations throughout the brain. Although detailed mechanism of action data is not available from the current Evidence Pack, citalopram's pharmacology as an SSRI is well established, and its antidepressant activity is the foundation upon which this repurposing hypothesis builds.

OCD has a well-characterised neurobiological basis: dysfunction within the cortico-striato-thalamo-cortical (CSTC) circuit, driven by serotonergic dysregulation, gives rise to the disorder's hallmark obsessions and compulsions. Raising synaptic 5-HT via SERT blockade directly modulates this circuit, which is why SSRIs — including fluoxetine, fluvoxamine, sertraline, and paroxetine — are recognised as first-line pharmacotherapy for OCD in APA, NICE, and WFSBP guidelines. The mechanistic leap from depression to OCD is therefore not speculative: it is the same drug class mechanism applied to a disorder whose biology shares a common serotonergic thread.

Critically, the pharmacological bridge between citalopram and escitalopram (its active S-enantiomer) is robust and well-accepted. Most clinical trials in this Evidence Pack involve escitalopram, which retains the same SERT-inhibition mechanism with higher selectivity. Beyond this proxy evidence, two published clinical studies document citalopram being used directly for treatment-resistant OCD (PMID 10572334; PMID 10471169), and a paediatric open-label study further supports citalopram's efficacy in children and adolescents with OCD (PMID 12839522). This convergence of mechanistic rationale, class-level clinical evidence, and direct citalopram data provides a strong foundation for the TxGNN prediction.

---

## Clinical Trial Evidence

> **Note:** The majority of trials below employed escitalopram (the active S-enantiomer of citalopram). Pharmacological translation to citalopram is considered high-fidelity, as both share the SERT-inhibition mechanism. No SANCTR (South African National Clinical Trials Register) or PACTR (Pan African Clinical Trials Registry) trials were identified in the search.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00723060](https://clinicaltrials.gov/study/NCT00723060) | Phase 4 | Completed | 176 | Prospective randomised double-blind multi-centre comparison of conventional (20 mg) vs high-dose (40 mg) escitalopram in OCD patients; outcomes measured by Y-BOCS, HAM-D, HAM-A, CGI-S/I, and GAF |
| [NCT03993535](https://clinicaltrials.gov/study/NCT03993535) | Phase 4 | Completed | 250 | Multi-country (US, Brazil, India, Netherlands) naturalistic OCD follow-up investigating clinical, neurocognitive, and neuroimaging predictors of pharmacological treatment response |
| [NCT00680602](https://clinicaltrials.gov/study/NCT00680602) | Phase 4 | Completed | 158 | Randomised open trial comparing group cognitive behavioural therapy (GCBT) vs SSRI (fluoxetine) for OCD, including patients with psychiatric comorbidities; confirms SSRI class-level efficacy across a broad OCD population |
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Completed | 78 | Evaluates SSRI monotherapy, exposure and response prevention (ERP), and their combination for OCD in a Chinese population; identifies biological and psychological predictors of treatment response |
| [NCT00305500](https://clinicaltrials.gov/study/NCT00305500) | Phase 3 | Completed | 100 | Open-label prospective study of high-dose escitalopram (up to 50 mg/day over 18 weeks) in outpatients with OCD; provides dose-escalation tolerability and efficacy data relevant to treatment-refractory cases |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | Evaluates CBT augmentation of SRI treatment in children with OCD; supports the combined pharmacological–behavioural approach as optimal first-line management |
| [NCT00708240](https://clinicaltrials.gov/study/NCT00708240) | Phase 4 | Unknown | 40 | Escitalopram in adolescents with OCD; investigates effects on executive function, metacognition, and regional brain activation — mechanistically directly relevant to citalopram |
| [NCT00116532](https://clinicaltrials.gov/study/NCT00116532) | Phase 4 | Completed | 30 | Assesses escitalopram efficacy in OCD and determines optimal therapeutic dose; pharmacological proxy for citalopram |
| [NCT00115011](https://clinicaltrials.gov/study/NCT00115011) | Phase 4 | Completed | 30 | Evaluates escitalopram in self-injurious skin picking, an OC-spectrum disorder; supports the serotonergic mechanism underpinning compulsive behaviour broadly |
| [NCT00215137](https://clinicaltrials.gov/study/NCT00215137) | Phase 2 | Completed | 14 | Pilot study assessing safety and effectiveness of escitalopram for OCD symptoms; provides early-phase tolerability data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | Clinical Trial (Direct Citalopram) | European Psychiatry | 90-day randomised open-label trial of **citalopram** vs citalopram + clomipramine in 16 adults with treatment-resistant OCD (failed prior clomipramine and fluoxetine); directly demonstrates citalopram efficacy in refractory OCD |
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | Clinical Report (Direct Citalopram) | International Clinical Psychopharmacology | Reviews **citalopram's** specific role in OCD treatment; links SERT-blockade selectivity to OCD neurobiology and positions citalopram as an OCD agent beyond its antidepressant use |
| [12839522](https://pubmed.ncbi.nlm.nih.gov/12839522/) | 2003 | Open-label Study (Direct Citalopram) | Psychiatry and Clinical Neurosciences | 8-week open-label study of **citalopram** (20–30 mg/day) in 15 children and adolescents with OCD (mean age 12.1 years); CY-BOCS scores significantly improved, supporting paediatric application |
| [35121274](https://pubmed.ncbi.nlm.nih.gov/35121274/) | 2022 | Network Meta-analysis | Journal of Psychiatric Research | Network meta-analysis comparing pharmacological and psychological treatments (alone and combined) in children and adolescents with OCD; SSRIs confirmed as effective first-line agents, with combination therapy superior to either alone |
| [38703743](https://pubmed.ncbi.nlm.nih.gov/38703743/) | 2024 | Systematic Review | Comprehensive Psychiatry | Evaluates long-term safety and tolerability of off-label high-dose SRIs (beyond standard doses) in OCD; identifies acceptable safety profiles at higher doses, relevant to treatment-refractory strategies |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Meta-Review | Frontiers in Psychiatry | Comprehensive meta-review of antidepressants in children and adolescents across multiple disorders including OCD; addresses efficacy, tolerability, and suicidality signals — important for risk-benefit framing |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Meta-analysis | Journal of Affective Disorders | Demonstrates OCD has a reduced placebo (and antidepressant) response compared to other anxiety-related disorders; highlights the genuine and specific pharmacological signal of SRIs in OCD |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | Review | BMJ Clinical Evidence | Population-level review of OCD epidemiology (~1–2.7% prevalence) and evidence base for treatment options; provides clinical context for SSRI use across episodic and chronic OCD presentations |
| [35818708](https://pubmed.ncbi.nlm.nih.gov/35818708/) | 2022 | Systematic Review | Expert Opinion on Pharmacotherapy | Systematic review of pharmacotherapy for obsessive-compulsive personality disorder (OCPD); contextualises SRI use across the OC-spectrum and highlights the evidence gap for personality-spectrum disorders |
| [12607204](https://pubmed.ncbi.nlm.nih.gov/12607204/) | 2000 | Review | World Journal of Biological Psychiatry | Foundational review of OCD neurobiology (frontal-basal-thalamo-cortical circuit) and the role of serotonergic medications; mechanistic rationale for why SSRI-class drugs — including citalopram — are appropriate for OCD |

---

## South Africa Market Information

Citalopram currently has **no SAHPRA-registered products** in South Africa.

| Item | Detail |
|------|--------|
| SAHPRA Registrations | None found |
| Market Status | Not registered in South Africa |
| Essential Medicines List (EML) | Not listed |

> Clinicians should verify the current status of related products (e.g., escitalopram, which shares the same mechanism) on the SAHPRA online register. Importation or use of unregistered citalopram would require a Section 21 authorisation from SAHPRA.

---

## Safety Considerations

Safety-specific data (warnings, contraindications, and drug interaction profile) for citalopram was not available in the current Evidence Pack.

> Please refer to the SAHPRA-approved Professional Information (PI) for safety information. As citalopram is not currently registered in South Africa, clinicians should consult international prescribing information (e.g., FDA Prescribing Information, EMA SmPC) as an interim reference. Adverse drug reactions should be reported to SAHPRA at [www.sahpra.org.za](https://www.sahpra.org.za).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Citalopram's SSRI mechanism directly targets the serotonergic dysfunction underlying OCD; SSRIs are already the pharmacological cornerstone of OCD treatment internationally. Direct published evidence of citalopram use in treatment-resistant OCD, combined with an extensive body of Phase 3–4 escitalopram OCD trials (a pharmacologically valid proxy), places this prediction at Evidence Level L2 — sufficient to warrant a carefully monitored clinical pathway, but requiring regulatory and safety data gaps to be resolved first.

**To proceed, the following is needed:**

- **SAHPRA regulatory pathway**: Citalopram is unregistered in South Africa; evaluate whether a Section 21 unregistered medicine application is appropriate, or whether the registered enantiomer (escitalopram, if SAHPRA-registered) should be substituted
- **Full PI / prescribing information retrieval**: Download and parse the SAHPRA or international (FDA/EMA) PI to formally document contraindications, warnings, and drug interaction profile — currently a blocking data gap
- **QTc safety monitoring protocol**: Citalopram carries a known dose-dependent QTc-prolonging effect (greater than other SSRIs); a cardiac safety monitoring plan (baseline ECG, dose limits, drug interaction screening) is required before clinical use
- **Mechanism of action data (MOA)**: Retrieve from DrugBank (DB00215) to support the formal mechanistic dossier and pharmacovigilance documentation
- **OCD-specific dose titration guidance**: Establish dose equivalence between citalopram and escitalopram (approximately 2:1 ratio) and define safe dose escalation thresholds for OCD (which often requires higher doses than depression)
- **Paediatric safety considerations**: If use in children or adolescents is intended, additional regulatory requirements, informed consent protocols, and monitoring for suicidality (black box warning in many jurisdictions) must be addressed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

