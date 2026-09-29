---
layout: default
title: Clonazepam
parent: Model Prediction Only (L5)
nav_order: 136
evidence_level: L5
indication_count: 3
---

# Clonazepam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Clonazepam: From Benzodiazepine Therapy to Restless Legs Syndrome

## One-Sentence Summary

Clonazepam is a benzodiazepine marketed in South Africa as tablets (Clonam), but the registration data supplied does not state its approved indication.
The TxGNN model predicts it may be useful for **restless legs syndrome (RLS)**, with a very high score of **99.65%**.
Support comes from **0 registered clinical trials** and **18 publications**, mostly guidelines, reviews and small older studies, so this is a question of evidence quality rather than a new discovery. Clonazepam is already used off-label for RLS.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA registration data supplied |
| Predicted New Indication | Restless legs syndrome |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L3 by the rubric (a Cochrane systematic review exists). The pack's internal scoring lists L4, and the primary studies are unverified. |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Clonazepam is a GABA-A positive allosteric modulator. The proposed benefit in RLS is symptomatic: reduced sensory arousal and better sleep continuity. It does not act through the dopaminergic or alpha-2-delta pathways that are the mainstream RLS treatment targets. Detailed mechanism of action data is not available in the source record, so this description is the pack's working rationale rather than a sourced MOA entry.

Benzodiazepines induce and maintain sleep, so they are intuitively thought to help people whose RLS mainly disrupts sleep. A 1984 double-blind crossover trial (n=6) and a placebo-controlled sleep laboratory study support this. Guideline and review literature discusses clonazepam in this role, and a 2024 overview found 17 articles on its use in RLS and periodic limb movements in sleep.

The high TxGNN score is a knowledge-graph prediction only. Because clonazepam is already used off-label in RLS, the practical question is where it sits in current guidelines. The direction of the 2025 AASM recommendation has not been verified from the full text and must be checked before any decision.

## Clinical Trial Evidence

Currently no related clinical trials registered for restless legs syndrome. No SANCTR or PACTR entries were found in the data supplied.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6380197](https://pubmed.ncbi.nlm.nih.gov/6380197/) | 1984 | RCT (double-blind crossover, n=6) | Acta Neurol Scand | Clonazepam significantly improved subjective sleep quality and leg dysaesthesia versus placebo. Long-term efficacy needs confirmation. |
| [11313161](https://pubmed.ncbi.nlm.nih.gov/11313161/) | 2001 | Placebo-controlled sleep laboratory study | Eur Neuropsychopharmacol | Measured acute effects of 1 mg clonazepam on objective and subjective sleep in RLS/PLMD. Results are not in the supplied abstract. |
| [31942156](https://pubmed.ncbi.nlm.nih.gov/31942156/) | 2019 | Open-label randomized study | J Midlife Health | Compared clonazepam with nortriptyline for RLS rate, frequency and severity in women over 40. Results are not in the supplied abstract. |
| [39324694](https://pubmed.ncbi.nlm.nih.gov/39324694/) | 2025 | Guideline | J Clin Sleep Med | AASM clinical practice guideline on treating RLS and PLMD. The recommendation on clonazepam is not in the supplied abstract and needs full-text review. |
| [28319266](https://pubmed.ncbi.nlm.nih.gov/28319266/) | 2017 | Systematic review | Cochrane Database Syst Rev | Reviews benzodiazepines for RLS, noting clonazepam is used despite limited evidence. Conclusions need full-text review. |
| [36692194](https://pubmed.ncbi.nlm.nih.gov/36692194/) | 2023 | Systematic review / meta-analysis | J Clin Sleep Med | Assesses which drug categories suppress periodic limb movements in sleep in RLS patients. |
| [38708125](https://pubmed.ncbi.nlm.nih.gov/38708125/) | 2024 | Review | Tremor Other Hyperkinet Mov | Historical overview: about 25% of 16,694 treated RLS patients in a survey received benzodiazepines. It identified 17 articles on clonazepam in RLS/PLMS. |
| [18925578](https://pubmed.ncbi.nlm.nih.gov/18925578/) | 2008 | Evidence-based review | Mov Disord | Movement Disorder Society task force classified the efficacy of RLS therapies. The clonazepam grading is not in the supplied abstract. |
| [24363103](https://pubmed.ncbi.nlm.nih.gov/24363103/) | 2014 | Review | Neurotherapeutics | General overview of how RLS treatment has changed over recent years. |
| [17876423](https://pubmed.ncbi.nlm.nih.gov/17876423/) | 2007 | Expert opinion | Arq Neuropsiquiatr | Brazilian expert group conclusions on RLS diagnosis and management. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 45/2.5/0820 | Clonam | Tablet | Not recorded in data supplied |
| Reg. No. 45/2.5/0820 | Clonam 0,5 | Tablet | Not recorded in data supplied |

Both entries are oral tablets. Essential Medicines List (EML) inclusion status was not available in the data and has not been verified.

## Safety Considerations

- **Class-level concerns (from the pack's assessment, not from the PI):** Dependence, falls and cognitive risks weigh against long-term use. Any use in RLS should be weighed against these and against existing RLS options.

No drug interactions were found in the interaction query. Please refer to the SAHPRA-approved Professional Information (PI) for warnings, contraindications and full interaction information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no registered trials for RLS, and the support is guideline and review literature plus small older studies. The SAHPRA package insert safety data, which is a blocking gap, has not been retrieved, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Retrieve the SAHPRA Professional Information for the Clonam registrations, covering approved indication, warnings and contraindications.
- Read the full text of the 2025 AASM guideline and the 2017 Cochrane review to confirm the direction and strength of their recommendations on clonazepam in RLS.
- Confirm the mechanism of action from DrugBank.
- Check the current South African guideline and Essential Medicines List position for RLS treatment.
- Decide whether a long-term safety comparison against first-line RLS agents is needed, given the dependence and fall risks.

Two lower-ranked predictions were also generated but are not evaluated in detail here. Insomnia (score 99.32%) is supported by no trial of clonazepam for primary insomnia, and only one small trial (n=34) in a different sleep disorder. Trigeminal nerve neoplasm (score 99.30%) should be treated as a symptom-level mapping artifact, with only two case reports and no plausible antineoplastic mechanism.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

