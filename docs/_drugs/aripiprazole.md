---
layout: default
title: Aripiprazole
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 10
---

# Aripiprazole
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

# Aripiprazole: From Schizophrenia/Bipolar Disorder to Major Affective Disorder

## One-Sentence Summary

Aripiprazole is a second-generation (atypical) antipsychotic globally approved for schizophrenia and bipolar disorder, with established use as adjunctive therapy for treatment-resistant depression — but currently not registered with SAHPRA in South Africa.
The TxGNN model predicts it may be effective for **Major Affective Disorder** (encompassing major depressive disorder and bipolar disorder spectrum),
with **multiple completed Phase 3 RCTs** and over **20 publications** strongly supporting this direction, aligned with existing FDA and EMA approvals.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered with SAHPRA; globally approved for schizophrenia, bipolar I disorder, and MDD adjunctive therapy (FDA/EMA) |
| Predicted New Indication | Major Affective Disorder (MDD and bipolar disorder spectrum) |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved in this evidence pack; however, based on published global pharmacological data, aripiprazole functions as a **dopamine-serotonin system stabiliser**. Unlike conventional antipsychotics that fully block D2 receptors, aripiprazole acts as a **partial agonist at D2/D3 dopamine receptors**, producing a "stabiliser" effect — suppressing dopaminergic transmission when activity is excessive (as in psychosis or mania) and augmenting it when activity is deficient (as in depression). It also acts as a **partial agonist at 5-HT1A receptors**, a mechanism associated with antidepressant augmentation, and as an **antagonist at 5-HT2A receptors**, which improves affective regulation and reduces anxiety-related symptoms.

This receptor profile makes aripiprazole particularly well-suited to major affective disorders, where dysregulation of dopaminergic and serotonergic circuits underlies both the depressive and manic/mixed phases of illness. Critically, the drug's partial — rather than full — D2 blockade accounts for its lower extrapyramidal side-effect burden compared to first-generation antipsychotics, making it more tolerable for longer-term mood disorder management. Its modulation of the orbitofrontal cortex–striatum circuit via 5-HT2A antagonism also supports its use in impulsive and compulsive symptom dimensions common in affective disorders.

Aripiprazole has **already received regulatory approval from the FDA and EMA** for adjunctive treatment of major depressive disorder (when response to antidepressants is inadequate) and for bipolar I disorder (manic/mixed episodes and maintenance). The TxGNN prediction score of 99.62% therefore reflects established pharmacological reality strongly embedded in the knowledge graph, rather than a speculative hypothesis. For South Africa, the clinical question is not whether aripiprazole works for major affective disorder — it does — but how to expedite SAHPRA registration to make it legally available to patients.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00876343](https://clinicaltrials.gov/study/NCT00876343) | Phase 3 | Completed | 586 | Aripiprazole vs placebo as adjunctive therapy to SSRI/SNRI in MDD — core pivotal RCT demonstrating efficacy and safety of aripiprazole augmentation |
| [NCT00095823](https://clinicaltrials.gov/study/NCT00095823) | Phase 3 | Completed | 1,200 | 14-week double-blind placebo-controlled RCT of aripiprazole adjunctive to ongoing antidepressant in MDD — the largest pivotal study in this indication |
| [NCT02046564](https://clinicaltrials.gov/study/NCT02046564) | Phase 3 | Completed | 412 | ASC-01 (aripiprazole/sertraline fixed combination) vs sertraline monotherapy in MDD patients with incomplete SSRI response |
| [NCT00277212](https://clinicaltrials.gov/study/NCT00277212) | Phase 4 | Completed | 1,169 | Aripiprazole + lamotrigine vs placebo + lamotrigine for long-term maintenance in Bipolar I disorder following manic/mixed episode |
| [NCT00080314](https://clinicaltrials.gov/study/NCT00080314) | Phase 3 | Completed | 400 | Flexible-dose aripiprazole (5–30 mg) vs placebo in patients with Bipolar I disorder with a major depressive episode |
| [NCT00107939](https://clinicaltrials.gov/study/NCT00107939) | Phase 3 | Completed | 453 | Licarbazepine adjunctive to atypical antipsychotics (including aripiprazole) in Bipolar I manic episodes — double-blind RCT with aripiprazole as one of five permitted backbone agents |
| [NCT02305823](https://clinicaltrials.gov/study/NCT02305823) | Phase 4 | Completed | 203 | Real-world effectiveness comparison of aripiprazole vs quetiapine vs ziprasidone in first-episode non-affective psychosis (3-year follow-up) |
| [NCT01111565](https://clinicaltrials.gov/study/NCT01111565) | Phase 3 | Terminated | 137 | Aripiprazole/escitalopram combination in MDD with incomplete escitalopram response — terminated early but provides safety and tolerability data |
| [NCT03423680](https://clinicaltrials.gov/study/NCT03423680) | Phase 3 | Recruiting | 390 | Aripiprazole (Abilify®) adjunctive to mood stabiliser for Bipolar I or II disorder with major depressive episode — 8-week double-blind RCT |
| [NCT07153406](https://clinicaltrials.gov/study/NCT07153406) | Phase 3 | Not Yet Recruiting | 220 | Esketamine nasal spray vs aripiprazole (both combined with SSRI/SNRI) in treatment-resistant MDD in elderly patients (>60 years) — active comparison RCT |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38669232](https://pubmed.ncbi.nlm.nih.gov/38669232/) | 2024 | Systematic Review + Meta-analysis (RCTs) | *PLoS One* | First and largest meta-analysis of RCTs evaluating aripiprazole or bupropion augmentation in TRD/MDD — directly quantifies aripiprazole's efficacy and safety advantage |
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Systematic Review + Network Meta-analysis | *J Affect Disord* | Network meta-analysis of augmentation agents in adult TRD; aripiprazole ranked among the most studied and efficacious options |
| [38219278](https://pubmed.ncbi.nlm.nih.gov/38219278/) | 2024 | Systematic Review + Network Meta-analysis | *Neuropsychopharmacology Reports* | Head-to-head comparison of brexpiprazole, aripiprazole, and placebo for MDD patients inadequately responsive to antidepressants in Japanese population |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Systematic Review + Meta-analysis | *Psychological Medicine* | Comprehensive meta-analytic assessment of antipsychotics as monotherapy and adjunctive therapy in MDD — aripiprazole prominently evaluated |
| [34167174](https://pubmed.ncbi.nlm.nih.gov/34167174/) | 2021 | Systematic Review + Meta-analysis | *Prim Care Companion CNS Disord* | Long-term (≥6 months) efficacy and tolerability of adjunctive aripiprazole in MDD; primary outcome: depression remission rates |
| [37746943](https://pubmed.ncbi.nlm.nih.gov/37746943/) | 2023 | Systematic Review + Network Meta-analysis | *Medicine* | Comparative ranking of 4 atypical antipsychotics (including aripiprazole) for adjuvant treatment of MDD in patients with inadequate antidepressant response |
| [37149344](https://pubmed.ncbi.nlm.nih.gov/37149344/) | 2023 | Narrative Review | *Psychiatr Clin North Am* | Atypical antipsychotics identified as the most widely studied augmentation class in TRD; aripiprazole and brexpiprazole highlighted as first-line options |
| [36855876](https://pubmed.ncbi.nlm.nih.gov/36855876/) | 2023 | Review | *Am J Psychiatry* | Role of antipsychotics, including aripiprazole, in the rapidly evolving TRD therapeutic landscape alongside newer agents (esketamine, psilocybin) |
| [35861202](https://pubmed.ncbi.nlm.nih.gov/35861202/) | 2023 | Systematic Review + Meta-analysis | *J Psychopharmacol* | Augmentation and combination treatments for early-stage TRD; aripiprazole among the evaluated agents with favourable evidence profile |
| [25963405](https://pubmed.ncbi.nlm.nih.gov/25963405/) | 2016 | Review | *Asia-Pacific Psychiatry* | Mechanistic review of second-generation antipsychotics as antidepressants; aripiprazole (FDA-approved adjunctive) effective at subantipsychotic doses with receptor-profile rationale |

---

## South Africa Market Information

Aripiprazole is currently **not registered with SAHPRA** and has no approved products on the South African market.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|--------------------|-------------|------------|-------------------|
| — | No SAHPRA-registered products | — | — |

> **Note for clinicians**: Aripiprazole (brand name Abilify®; also available as Abilify Maintena® long-acting injectable) is available in over 90 countries. It holds FDA approval for schizophrenia (adults and adolescents ≥13 years), bipolar I disorder (acute manic/mixed episodes and maintenance), MDD adjunctive therapy, irritability associated with autism spectrum disorder (ages 6–17), and Tourette's disorder. SAHPRA registration is required for legal supply in South Africa. Clinicians in South Africa requiring access for individual patients may explore Section 21 authorisation (unregistered medicine) via SAHPRA while a formal dossier is submitted.

---

## Safety Considerations

Please refer to the internationally recognised prescribing information (FDA label, EMA Summary of Product Characteristics) and, once registered, the SAHPRA-approved Professional Information (PI) for full safety information. Report all adverse drug reactions to SAHPRA at [pharmacovigilance@sahpra.org.za](mailto:pharmacovigilance@sahpra.org.za).

**Notable safety signal from the literature**: A 2024 systematic review (PMID [38227009](https://pubmed.ncbi.nlm.nih.gov/38227009/), *Psychopharmacology*) identified impulse control disorders — including problem gambling, hypersexuality, and compulsive behaviours — as adverse effects associated with aripiprazole administration or dose increases. This is mechanistically plausible given its D2 partial agonist activity in the mesolimbic reward pathway. Clinicians should proactively screen for these behaviours at each follow-up visit, particularly in patients with a prior history of impulsive behaviour or substance use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs — including large pivotal trials (n=586 and n=1,200) — establish aripiprazole's efficacy as adjunctive therapy in major affective disorder, supported by an extensive network meta-analytic literature and confirmed by FDA and EMA approvals. Evidence quality is L1. For South Africa, this is a regulatory access gap rather than an evidence gap, and the priority action is SAHPRA registration.

**To proceed, the following is needed:**

- **SAHPRA registration dossier**: Submit an abridged application (referencing FDA/EMA dossier) to SAHPRA; Section 21 authorisation may be considered as an interim measure for individual patients in need
- **Full prescribing information retrieval**: Obtain the FDA label or EMA SmPC to formally document the complete safety profile, contraindications (including known hypersensitivity), and drug interaction data (CYP2D6 and CYP3A4 metabolism)
- **Drug interaction assessment**: Conduct a formal DDI review before clinical deployment — aripiprazole is a CYP2D6 and CYP3A4 substrate; co-administration with strong inhibitors/inducers requires dose adjustment
- **Impulse control disorder monitoring protocol**: Establish a structured screening protocol for impulse control disorders (gambling, hypersexuality, compulsive shopping/eating) at baseline and each follow-up, as an institutional guardrail
- **Local pharmacoeconomic analysis**: Assess cost-effectiveness of aripiprazole augmentation versus currently used alternatives (e.g., quetiapine, lithium, lamotrigine) in South Africa's public and private healthcare contexts
- **Essential Medicines List (EML) submission**: Evaluate aripiprazole against South Africa's Standard Treatment Guidelines and EML criteria for psychiatric formulary inclusion, given the strength of its evidence base for treatment-resistant major depressive disorder

---

> ⚠️ **Disclaimer**: This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All information should be interpreted by qualified healthcare professionals in the context of individual patient care and current South African regulatory requirements.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

