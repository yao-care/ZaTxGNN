---
layout: default
title: Diazepam
parent: 僅模型預測 (L5)
nav_order: 169
evidence_level: L5
indication_count: 10
---

# Diazepam
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

# Diazepam: From Anxiety/Seizure Management to Insomnia

## One-Sentence Summary

Diazepam is a classic benzodiazepine, long established for anxiety, seizures, muscle spasm, and alcohol withdrawal management. The TxGNN model's top-ranked new signal is **Insomnia**, currently associated with **24 clinical trials** and **18 publications** — though most of this evidence concerns the safe tapering or discontinuation of diazepam-class hypnotics rather than proving new efficacy, so this should be read as a re-affirmation of an already-known sedative-hypnotic use rather than a novel discovery.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorders, seizures/status epilepticus, muscle spasm, alcohol withdrawal (benzodiazepine class) — no SAHPRA-approved indication text available, as the drug is not currently registered in South Africa |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.9997% |
| Evidence Level | L1 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed DrugBank-sourced mechanism-of-action data is not yet available for this evidence pack (flagged as a High-severity data gap). Based on well-established pharmacological knowledge, Diazepam is a positive allosteric modulator (PAM) of the GABA-A receptor, enhancing inhibitory GABAergic neurotransmission in the central nervous system. This action underlies its long-standing clinical roles in anxiety, seizure control, muscle relaxation, and alcohol withdrawal.

Sedation and sleep induction are intrinsic, well-documented consequences of the same GABA-A mechanism, so Insomnia is not a mechanistically distant indication from diazepam's original uses — it is essentially an extension of a sedative-hypnotic property that diazepam already exhibits and that is used clinically (on- or off-label) in several markets. In that sense, the TxGNN signal is best understood as recovering an already-known pharmacological fact rather than surfacing a genuinely new therapeutic hypothesis.

This nuance matters for interpretation of the evidence base below: the majority of identified trials focus on how to safely **taper or substitute** long-term benzodiazepine hypnotics (managing dependence/withdrawal risk), not on establishing new efficacy for insomnia. The single directly comparative efficacy trial identified in this pack (PMID 6113175) actually found diazepam **inferior** to a newer benzodiazepine (lormetazepam) for insomnia outcomes. Any recommendation should weigh this critically rather than treat the high TxGNN score as new proof of efficacy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244711](https://clinicaltrials.gov/study/NCT01244711) | Phase 4 | Terminated | 1 | Pilot study substituting quetiapine for benzodiazepines in treatment-refractory anxiety/GAD with chronic BZD use and insomnia; terminated with only 1 participant — indirectly relevant, evidence too sparse to interpret |
| [NCT04050176](https://clinicaltrials.gov/study/NCT04050176) | Phase 3 | Active, not recruiting | 260 | Blinded hypnotic-tapering protocol combined with CBT-Insomnia (CBTI) to improve discontinuation rates for BZD-class hypnotics — relevant to safe diazepam discontinuation, not to insomnia efficacy |
| [NCT03687086](https://clinicaltrials.gov/study/NCT03687086) | N/A | Completed | 188 | Novel behavioral mechanism to help older adults discontinue hypnotic ("sleeping pill") use — relevant to the deprescribing side of BZD hypnotic use in insomnia patients |
| [NCT03405493](https://clinicaltrials.gov/study/NCT03405493) | N/A | Completed | 60 | Sleep/light therapy for depression; does not involve diazepam — likely a keyword false-positive |
| [NCT01893632](https://clinicaltrials.gov/study/NCT01893632) | Phase 2 | Terminated | 2 | Gabapentin for benzodiazepine dependence — addresses BZD withdrawal, not insomnia treatment efficacy |
| [NCT05935553](https://clinicaltrials.gov/study/NCT05935553) | Phase 2/3 | Recruiting | 93 | Baclofen to assist benzodiazepine dose titration during BZD withdrawal — no direct link to diazepam's insomnia efficacy |
| [NCT04205682](https://clinicaltrials.gov/study/NCT04205682) | Early Phase 1 | Unknown | 52 | Cannabidiol for alcohol withdrawal — not diazepam-related |
| [NCT00678691](https://clinicaltrials.gov/study/NCT00678691) | Phase 4 | Completed | 55 | Armodafinil augmentation for fibromyalgia-related fatigue — not relevant |
| [NCT05646693](https://clinicaltrials.gov/study/NCT05646693) | Phase 2 | Unknown | 58 | Antioxidant therapy in chronic tinnitus using a fixed combination (amitriptyline + perphenazine + diazepam, "Adepsique") — diazepam present only as part of a combination product, not tested for insomnia |
| [NCT03461042](https://clinicaltrials.gov/study/NCT03461042) | Phase 4 | Completed | 17 | Ramelteon (melatonin receptor agonist) added to assist dose reduction/interruption of BZD and non-BZD hypnotics in chronic insomnia — again a discontinuation-support trial, not an efficacy trial for diazepam |

**Overall assessment:** none of the 24 identified trials directly test diazepam's efficacy for treating insomnia; nearly all instead address the safe tapering, substitution, or discontinuation of benzodiazepine hypnotics — reinforcing that the “new indication” signal largely reflects diazepam's existing, cautioned sedative-hypnotic role.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | RCT | J Int Med Res | Head-to-head trial (n=100): lormetazepam 1 mg significantly outperformed diazepam 5 mg on sleep-latency reduction and sleep-duration prolongation (p<0.05) — direct evidence diazepam is an inferior hypnotic versus a newer benzodiazepine |
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Review | Bioorganic Chemistry | Reviews clinical applications of small-molecule GABA-A receptor modulators, naming diazepam as a representative PAM used for epilepsy, anxiety, insomnia, and depression, alongside its known sedation-related side effects |
| [35228700](https://pubmed.ncbi.nlm.nih.gov/35228700/) | 2022 | Preclinical (mouse) | Nature Neuroscience | Long-term diazepam impairs dendritic spine plasticity and cognitive performance via microglial engulfment linked to mitochondrial TSPO — an important chronic-use safety signal |
| [40583063](https://pubmed.ncbi.nlm.nih.gov/40583063/) | 2025 | Clinical + mechanistic | Cellular & Molecular Biology Letters | Long-term use of benzodiazepines (diazepam) and Z-drugs is associated with exacerbated breast cancer risk, with proposed molecular mechanisms — a notable long-term safety concern for chronic insomnia use |
| [37776625](https://pubmed.ncbi.nlm.nih.gov/37776625/) | 2023 | Preclinical (rat) | J Pharmaceutical and Biomedical Analysis | Metabolomics study of a Chinese patent medicine for insomnia used diazepam as the positive control comparator in a PCPA-induced insomnia rat model |
| [6114852](https://pubmed.ncbi.nlm.nih.gov/6114852/) | 1981 | Pharmacology review | Drugs | Review of triazolam positions it against longer-acting benzodiazepines (including diazepam) as hypnotics, discussing relative half-life and suitability for insomnia |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharmaceutica | Meta-analysis of tranquilizer (including benzodiazepine) use in elderly patients with chronic non-communicable disease, assessing dose and adverse effects |
| [40350874](https://pubmed.ncbi.nlm.nih.gov/40350874/) | 2025 | Preclinical (mouse) | China J of Chinese Materia Medica | Ziziphi Spinosae Semen extract evaluated against a diazepam (2 mg/kg) positive control in a chronic-stress depression/insomnia mouse model |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opinion on Drug Metabolism & Toxicology | Reviews pharmacokinetics of anxiolytic drugs, noting benzodiazepines (including diazepam) remain among the most prescribed psychoactive agents |
| [29479317](https://pubmed.ncbi.nlm.nih.gov/29479317/) | 2018 | Review | Frontiers in Pharmacology | Review of a Chinese herbal formula for insomnia, discussing conventional pharmacotherapy (including benzodiazepines) as the treatment context/comparator |

## South Africa Market Information

Diazepam is currently **not marketed** in South Africa under this evidence pack (0 SAHPRA registrations; market status: Not Marketed). No product registration record or approved indication text is available for local reference. Any clinical use would need to proceed via an appropriate regulated pathway (e.g., Section 21 authorization or new SAHPRA registration), not via an existing local license.

## Safety Considerations

All structured safety fields in this evidence pack — key warnings, contraindications, and drug-drug interactions — are currently unavailable.

> Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

This gap is flagged in the underlying evidence pack as **Blocking** severity (missing PI warnings/contraindications), with the stated impact that the candidate cannot formally enter the S1 safety pre-assessment stage until it is resolved. This should be treated as the top-priority outstanding item, not a routine data gap.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Diazepam's GABA-A PAM mechanism is pharmacologically coherent with an insomnia indication, and this reflects an already-recognized (non-novel) sedative-hypnotic use pattern — the L1 evidence level here largely reflects diazepam's long clinical track record rather than a new discovery.
- The only directly comparative efficacy study identified (PMID 6113175) found diazepam **inferior** to a newer benzodiazepine for insomnia, and the bulk of trial evidence concerns safe discontinuation/tapering of BZD hypnotics rather than confirming new efficacy — so clinical utility should be regarded as limited, and mainly relevant to short-term or adjunctive use rather than first-line therapy.
- A **Blocking** data gap (missing SAHPRA-approved PI safety information) currently prevents this candidate from formally clearing safety pre-assessment. "Guardrails" specifically means: do not advance further until PI-derived warnings, contraindications, and interaction data are obtained.

**To proceed, the following is needed:**
- SAHPRA Professional Information (PI) / package insert — warnings, contraindications, and drug-interaction data (Blocking gap, DG001)
- DrugBank-verified mechanism-of-action confirmation (High-severity gap, DG002)
- Clarification of the regulatory pathway in South Africa, given diazepam is currently unregistered (Section 21 import vs. new SAHPRA registration)
- A dependence/withdrawal risk-management plan specific to benzodiazepine-class hypnotics, particularly for elderly patients, before any insomnia-related use is considered
- Head-to-head efficacy data against current standard-of-care hypnotics (e.g., Z-drugs, orexin antagonists such as lemborexant) to justify clinical positioning

*Note: this evidence pack also assessed nine other candidate indications for diazepam (e.g., sleep-initiation/maintenance disorder, barbiturate abuse substitution, cauda equina syndrome, ADHD subtypes, developmental disorder, neurogenic bladder). Only two others reached "Proceed with Guardrails" — sleep disorder (initiating/maintaining sleep) and barbiturate-abuse substitution — both reflecting the same underlying GABA-A sedative mechanism rather than independent new indications. The remaining candidates were rated "Hold" (no credible mechanistic or clinical support) or, in one case, "Research Question" (likely ontology/labeling mismatch requiring clarification before further evaluation).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

