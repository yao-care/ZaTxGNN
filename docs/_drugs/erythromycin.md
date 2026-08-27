---
layout: default
title: Erythromycin
parent: 僅模型預測 (L5)
nav_order: 210
evidence_level: L5
indication_count: 10
---

# Erythromycin
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

# Erythromycin: From Bacterial Infections to Lymphogranuloma Venereum

## One-Sentence Summary

Erythromycin is a macrolide antibiotic historically used to treat gram-positive and atypical bacterial infections; formal SAHPRA-registered indication text is not available in this evidence pack, and the drug is currently **not marketed in South Africa**.
TxGNN's single highest-scoring prediction (punctate epithelial keratoconjunctivitis, 99.89%) has **zero** supporting clinical trials or literature and is rated **Hold**. Among the 10 candidate indications surveyed, **Lymphogranuloma Venereum (LGV)** is the only one reaching a substantive evidence tier — **L3**, backed by **20 publications** and an existing place in international STI treatment guidelines — and is therefore the focus of this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no SAHPRA licenses on file; drug status "not marketed"). Generally known use: gram-positive and atypical bacterial infections. |
| Predicted New Indication | Lymphogranuloma Venereum (LGV) |
| TxGNN Prediction Score | 99.05% (rank 4659 of predicted candidates) |
| Evidence Level | L3 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

### Full List of TxGNN-Predicted Indications (this candidate pack)

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|------|------|------|------|
| 1 | Punctate epithelial keratoconjunctivitis | 99.89% | L5 | S0 | Hold |
| 2 | Acute contagious conjunctivitis | 99.55% | L4 | S1 | Research Question |
| 3 | Exposure keratitis | 99.50% | L5 | S0 | Hold |
| **4** | **Lymphogranuloma venereum** | **99.05%** | **L3** | **S2** | **Proceed with Guardrails** |
| 5 | Necrotizing ulcerative gingivitis | 99.00% | L3 | S1 | Research Question |
| 6 | Polyclonal hyperviscosity syndrome | 98.84% | L5 | S0 | Hold |
| 7 | Hyperamylasemia | 98.84% | L5 | S0 | Hold |
| 8 | Postinfectious vasculitis | 98.77% | L5 | S0 | Hold |
| 9 | Post-bacterial disorder | 98.75% | L4 | S0 | Hold |
| 10 | Post-infectious syndrome | 98.71% | L4 | S1 | Research Question |

Six of the ten candidates (ranks 1, 3, 6, 7, 8, 9) have no supporting clinical trial or literature evidence at all and are classified Hold — these appear to reflect knowledge-graph embedding noise (e.g., candidate #7, hyperamylasemia, likely reflects a known adverse-effect edge being read as a treatment edge) rather than plausible repurposing hypotheses. LGV is the only candidate that reaches "Proceed with Guardrails."

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for erythromycin is not available in this evidence pack (Data Gap DG002, pending DrugBank API lookup). Based on general pharmacological knowledge, erythromycin is a macrolide antibiotic that binds the bacterial 50S ribosomal subunit and blocks peptide chain translocation, inhibiting protein synthesis. This activity extends to *Chlamydia trachomatis* serovars L1–L3, the causative organism of LGV.

LGV is itself a chlamydial sexually transmitted infection, so this is less a "novel" mechanistic leap than an extension within erythromycin's already-recognized antimicrobial spectrum. Erythromycin base has long been listed in CDC and WHO sexually transmitted infection treatment guidelines as an **alternative regimen to doxycycline** for LGV, specifically for patients who are pregnant or doxycycline-intolerant — this is established clinical practice, not a new hypothesis generated purely by the TxGNN model.

This pre-existing guideline-level recognition is what elevates LGV to L3/S2 status relative to the other nine candidates in this pack, none of which have any comparable clinical grounding. The literature base is dominated by reviews and case reports rather than erythromycin-specific randomized trials, so the evidence should be read as supportive of a known-but-secondary treatment role, not as newly discovered efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for erythromycin in lymphogranuloma venereum.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25870512](https://pubmed.ncbi.nlm.nih.gov/25870512/) | 2015 | Review | Infection and Drug Resistance | LGV caused by *C. trachomatis* serovars L1–L3; outbreaks in MSM populations across North America, Europe, and Australia over the past decade; diagnosis is often difficult on clinical grounds alone. |
| [27773504](https://pubmed.ncbi.nlm.nih.gov/27773504/) | 2016 | Review | Annales de Dermatologie et de Vénéréologie | French-language clinical review of LGV (no abstract available). |
| [22459660](https://pubmed.ncbi.nlm.nih.gov/22459660/) | 2012 | Review | Gastrointestinal Endoscopy | Review of LGV proctitis presentation and endoscopic findings (no abstract available). |
| [30518587](https://pubmed.ncbi.nlm.nih.gov/30518587/) | 2018 | Systematic Review | BMJ Open | Systematic review of non-standard treatment options for uncomplicated *C. trachomatis* urogenital infections. |
| [33462582](https://pubmed.ncbi.nlm.nih.gov/33462582/) | 2021 | Cohort | Clinical Infectious Diseases | Weekly oral azithromycin 1g for 3 weeks evaluated as LGV proctitis treatment in MSM in an endemic European setting (comparator macrolide, not erythromycin). |
| [40815293](https://pubmed.ncbi.nlm.nih.gov/40815293/) | 2025 | Cohort | Sexually Transmitted Diseases | Alberta, Canada surveillance program (2018–2022) on LGV serovar prevalence, treatment, and follow-up among gbMSM attending STI clinics. |
| [13239093](https://pubmed.ncbi.nlm.nih.gov/13239093/) | 1955 | Case Series | Antibiotic Medicine & Clinical Therapy | Historical report of an erythromycin–triple sulfonamide combination used to treat early-stage LGV — the only entry in this list directly reporting erythromycin use. |
| [22760150](https://pubmed.ncbi.nlm.nih.gov/22760150/) | 2012 | Case Report | Revista da Sociedade Brasileira de Medicina Tropical | 17-year-old treated with erythromycin for LGV; recurrent lesion 3 months later diagnosed as diffuse large B-cell non-Hodgkin lymphoma. |
| [24216037](https://pubmed.ncbi.nlm.nih.gov/24216037/) | 2014 | Case Report | International Journal of STD & AIDS | Bubonic (inguinal) LGV case with treatment failure across doxycycline, azithromycin, and moxifloxacin. |
| [24787368](https://pubmed.ncbi.nlm.nih.gov/24787368/) | 2014 | Case Series | Sexually Transmitted Infections | Four inguinal LGV cases highlighting diagnostic and management pitfalls, since current guidelines focus mainly on anorectal LGV. |

---

## South Africa Market Information

No SAHPRA registration records were found for erythromycin in this evidence pack (market status: **not marketed**, 0 licenses on file).

---

## Safety Considerations

Key warnings, contraindications, and drug-interaction data for erythromycin were not available in this evidence pack (Data Gap DG001, marked **Blocking** — TFDA/SAHPRA-approved Professional Information warnings and precautions have not yet been retrieved). Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Erythromycin's use in LGV is grounded in an established, guideline-recognized alternative role (versus doxycycline) rather than a novel mechanistic hypothesis, and is supported by 20 publications — though none are erythromycin-specific RCTs and no clinical trials for this combination are registered. This places the candidate above the "Hold" threshold but short of routine adoption without further safety and access review, particularly since the drug is not currently marketed in South Africa.

**To proceed, the following is needed:**
- Retrieval of TFDA/SAHPRA-approved Professional Information (warnings, contraindications, DDI) — currently a Blocking data gap (DG001)
- Confirmation of erythromycin's detailed mechanism-of-action data via DrugBank (DG002)
- A regulatory/import pathway assessment, since erythromycin currently holds no SAHPRA registration in South Africa
- Consideration of an erythromycin-specific (not azithromycin-extrapolated) clinical evaluation in LGV, given the guideline evidence is largely doxycycline/azithromycin-centered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

