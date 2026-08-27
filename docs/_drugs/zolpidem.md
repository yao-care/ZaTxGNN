---
layout: default
title: Zolpidem
parent: 僅模型預測 (L5)
nav_order: 470
evidence_level: L5
indication_count: 10
---

# Zolpidem
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

# Zolpidem: From Unregistered in South Africa to Insomnia (Sleep Initiation and Maintenance Disorder)

## One-Sentence Summary

Zolpidem is a globally established non-benzodiazepine hypnotic (a "Z-drug") that is currently **not registered or marketed in South Africa** (0 SAHPRA licenses on file). The TxGNN model predicts/confirms it is effective for **Insomnia (sleep disorder, initiating and maintaining sleep)**, with a very high prediction score and **20 supporting publications**, though **no registered clinical trials** are captured in this evidence pack for this specific indication. Importantly, this is not a novel repurposing signal — it corresponds to zolpidem's well-established global indication, so the practical question here is market registration/access rather than new clinical use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented — no SAHPRA registration on file for this drug |
| Predicted New Indication | Insomnia (Sleep disorder, initiating and maintaining sleep) |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L1 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed original-indication and mechanism-of-action records for this drug are not present in the current evidence pack for South Africa (the drug has no SAHPRA license on file). Based on the pharmacological rationale accompanying this prediction, zolpidem is a selective **GABA-A receptor α1-subunit positive allosteric modulator** (imidazopyridine class), which enhances GABAergic inhibitory neurotransmission to induce sedation and sleep onset.

This is the drug's core, well-established pharmacological action, and it maps directly onto the predicted indication — insomnia. In other words, the TxGNN model here is essentially **reproducing zolpidem's known, globally approved use** (it is marketed elsewhere as a first-line short-term insomnia treatment) rather than surfacing a genuinely novel repurposing candidate. The clinical relevance is therefore less about discovering a new mechanism-disease link and more about whether this well-characterized drug should be registered and made available in South Africa.

The supporting literature (below) is dominated by comparative-effectiveness studies of zolpidem against newer agents (lemborexant, daridorexant) for insomnia, along with structural pharmacology of the GABA-A receptor target — consistent with a mature, extensively studied drug-indication pairing rather than an exploratory one.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | RCT (Phase 3) | JAMA Network Open | Compared lemborexant, placebo, and zolpidem tartrate extended-release in older adults with insomnia disorder |
| [39374004](https://pubmed.ncbi.nlm.nih.gov/39374004/) | 2024 | RCT | JAMA Internal Medicine | Masked-taper behavioral intervention outperformed standard taper for discontinuing benzodiazepine receptor agonists (including zolpidem) |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Network Meta-analysis | Lancet | Compared pharmacological interventions for acute and long-term management of insomnia disorder |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | Network Meta-analysis | J Manag Care Spec Pharm | Compared comparative efficacy of lemborexant against other insomnia treatments, including zolpidem |
| [39879708](https://pubmed.ncbi.nlm.nih.gov/39879708/) | 2025 | RCT (comparator) | Sleep Medicine | Evaluated effects on sleep architecture in insomnia with comorbid mild obstructive sleep apnea (zolpidem-class comparator context) |
| [37549414](https://pubmed.ncbi.nlm.nih.gov/37549414/) | 2023 | Review | The Journal of Family Practice | Review and update on insomnia management in primary care |
| [29487083](https://pubmed.ncbi.nlm.nih.gov/29487083/) | 2018 | Review | Pharmacological Reviews | Reviewed non-benzodiazepine insomnia drugs (Z-drugs) including zolpidem's pharmacology, efficacy, and side-effect profile |
| [28845958](https://pubmed.ncbi.nlm.nih.gov/28845958/) | 2017 | Review | FP Essentials | Overview of insomnia diagnosis and management, including pharmacological options |
| [31953863](https://pubmed.ncbi.nlm.nih.gov/31953863/) | 2020 | Review | Annals of Neurology | Reviewed daridorexant, a new dual orexin receptor antagonist, positioned against existing hypnotics such as zolpidem |
| [37730991](https://pubmed.ncbi.nlm.nih.gov/37730991/) | 2023 | Mechanistic/structural | Nature | Cryo-EM structures of native GABA-A receptor assemblies — the direct pharmacological target of zolpidem |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note: although no structured safety data (warnings/contraindications/DDI) is on file for this jurisdiction, the broader literature set in this evidence pack (associated with other candidate indications) repeatedly flags zolpidem-specific risks — dependence/abuse potential, withdrawal delirium, rare stimulant/manic reactions, and a population-based association with suicide risk. These should be explicitly confirmed against the manufacturer's PI once available (see Data Gap DG001 below).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for zolpidem in insomnia is mature and extensive (L1, 20 supporting publications including RCTs and network meta-analyses), but this reflects confirmation of an already well-established indication rather than a novel repurposing finding — and the drug is currently unregistered and unavailable in South Africa, so no local safety dossier exists yet.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings/precautions, contraindications) — currently a **Blocking** data gap (DG001), required before any S1 safety assessment
- Formal mechanism-of-action documentation from DrugBank — currently a **High**-severity data gap (DG002)
- A registered clinical trial or local pharmacovigilance pathway if market entry is pursued
- Explicit dependence/abuse-risk monitoring plan, given repeated withdrawal/dependence signals in the wider literature

*Lower-ranked candidates (e.g., alcohol withdrawal, anxiety, major affective disorder) carry weaker evidence (L2–L4) and remain at Hold/Research-Question stage; several others (L5, TxGNN score only, e.g., torticollis of infancy, agoraphobia, Wernicke-Korsakoff syndrome) have no supporting trials or literature and should not be pursued without further evidence.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

