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

# Zolpidem: From Insomnia to Sleep Disorder, Initiating and Maintaining Sleep

## One-Sentence Summary

Zolpidem is an internationally established non-benzodiazepine hypnotic ("Z-drug") used for short-term treatment of insomnia. The TxGNN model's top prediction — **Sleep Disorder, Initiating and Maintaining Sleep** — is clinically synonymous with insomnia, i.e. Zolpidem's own established use, so this result should be read as a **model-validation signal rather than a novel repurposing candidate**. No clinical trials were retrieved under this exact search term, but **20 publications**, including Phase 3 RCTs and meta-analyses, directly support Zolpidem's efficacy for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Insomnia (internationally established Z-drug indication; no local approved-label text available — product is not currently registered in this market) |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep (clinically equivalent to insomnia) |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L3 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (Data Gap DG002). Based on known pharmacology, Zolpidem is a member of the Z-drug class (imidazopyridines), a positive allosteric modulator selective for the α1 subunit of the GABA-A receptor. This mechanism directly promotes sedation and sleep initiation/maintenance, and is well characterized in the supporting literature (e.g. cryo-EM structural work on GABA-A receptor pharmacology, PMID 37730991; reviews of Z-drug pharmacology, PMID 29487083).

The key finding here is that the "predicted new indication" — sleep disorder, initiating and maintaining sleep — is not a distinct disease from Zolpidem's original indication; it is the standard clinical/ontology term for insomnia itself. This explains the very high TxGNN score (99.87%, rank 1031): the model is correctly recovering ground-truth knowledge rather than surfacing a genuinely new therapeutic hypothesis. This is corroborated by the literature set, which includes head-to-head Phase 3 RCTs comparing Zolpidem against newer hypnotics (e.g. lemborexant, PMID 31880796; daridorexant, PMID 31953863) and a dedicated meta-analysis of RCTs on Zolpidem's efficacy/safety in insomnia (PMID 34688027).

For contrast, the evidence pack's lower-ranked predictions (e.g. alcohol withdrawal, manic bipolar affective disorder, anxiety) are the ones that represent actual candidate repurposing signals — but these carry substantially weaker evidence (L4–L5, decision stage S0–S1, "Hold") and, in at least one case, mismatched trial evidence (the two Phase 3 trials retrieved for "manic bipolar affective disorder" actually evaluated general insomnia populations, not manic bipolar patients).

---

## Clinical Trial Evidence

Currently no related clinical trials registered under this specific disease term.

*(Note: substantial Zolpidem-vs-insomnia RCT evidence exists in the literature set below; the targeted clinical-trials query for this exact term returned zero hits — see query_log id 2.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | RCT (Phase 3) | JAMA Network Open | Compared lemborexant with placebo and zolpidem tartrate ER in older adults with insomnia disorder; zolpidem used as active comparator |
| [34688027](https://pubmed.ncbi.nlm.nih.gov/34688027/) | 2021 | Meta-analysis (RCT) | Sleep Medicine | Meta-analysis of a randomized placebo-controlled trial evaluating efficacy/safety of zolpidem for insomnia over one month |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Systematic Review / Network Meta-analysis | Lancet | Estimated comparative effectiveness of pharmacological treatments (including zolpidem) for acute and long-term insomnia |
| [39374004](https://pubmed.ncbi.nlm.nih.gov/39374004/) | 2024 | RCT | JAMA Internal Medicine | Evaluated masked-taper behavioral intervention for discontinuing benzodiazepine receptor agonists (incl. zolpidem) |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | Systematic Review / Network Meta-analysis | J Managed Care Spec Pharm | Compared efficacy/safety of lemborexant against other insomnia treatments including zolpidem |
| [31953863](https://pubmed.ncbi.nlm.nih.gov/31953863/) | 2020 | RCT (dose-response) | Annals of Neurology | Evaluated daridorexant dose-response on sleep variables in insomnia disorder |
| [36472134](https://pubmed.ncbi.nlm.nih.gov/36472134/) | 2023 | RCT subanalysis | J Clin Sleep Medicine | Compared lemborexant vs. zolpidem tartrate ER across polysomnography-defined insomnia subtypes |
| [29487083](https://pubmed.ncbi.nlm.nih.gov/29487083/) | 2018 | Review | Pharmacological Reviews | Reviews Z-drugs (incl. zolpidem) pharmacology, clinical use, and limitations vs. novel non-GABAergic agents |
| [37549414](https://pubmed.ncbi.nlm.nih.gov/37549414/) | 2023 | Review | The Journal of Family Practice | Update on insomnia management in primary care, including pharmacological options |
| [16696581](https://pubmed.ncbi.nlm.nih.gov/16696581/) | 2006 | Review | CNS Drugs | Reviews efficacy/safety data for zolpidem extended-release formulation in insomnia |

---

## South Africa Market Information

No SAHPRA registration records are present in this evidence pack — `taiwan_regulatory.total_licenses = 0` and the market status is recorded as **Not marketed**. Zolpidem currently has no documented local product license, dosage form, or approved-indication text in this dataset.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Local key warnings, contraindications, and DDI data are flagged as a blocking data gap — DG001 — and could not be sourced from this evidence pack.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predicted indication is clinically equivalent to Zolpidem's already-established use, so it does not represent a genuine repurposing signal requiring a go/guardrails decision — it primarily validates the TxGNN model's calibration. Combined with a blocking gap in local safety/label data (DG001) and the fact that the product has zero current SAHPRA registrations, no safety or market-access determination can be made yet.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI): warnings, contraindications, DDI (DG001, blocking)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent (DG002)
- Re-examination of lower-ranked candidates (e.g. alcohol withdrawal, anxiety, bipolar mania) as the actual novel-repurposing signals, since these currently sit at L4–L5 evidence with "Hold" recommendations and weaker/mismatched trial support
- If local market entry is being considered for the established insomnia indication, a standard SAHPRA registration dossier, since no license currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

