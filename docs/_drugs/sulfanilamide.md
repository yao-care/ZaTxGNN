---
layout: default
title: Sulfanilamide
parent: 僅模型預測 (L5)
nav_order: 419
evidence_level: L5
indication_count: 10
---

# Sulfanilamide
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

# Sulfanilamide: From Bacterial Infections to Infective Vaginitis

## One-Sentence Summary

Sulfanilamide is a first-generation sulfonamide antibacterial; historical evidence gathered in this evidence pack points to prior use as a **topical/vaginal antibacterial (suppository/pessary form)**, though no formal original-indication record is available. Among 10 TxGNN-predicted indications, three reached the "Research Question" evaluation stage, the most advanced being **Infective Vaginitis**, supported by **20 PubMed articles including one multicenter RCT of a sulfanilamide-containing vaginal suppository**. Note: TxGNN's single highest-scoring prediction (postmenopausal atrophic vaginitis, 99.93%) has **no supporting literature or trials** and is flagged in this pack's own analysis as a likely knowledge-graph false positive — it is not the basis for this report's recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record in this evidence pack (drug identity: sulfonamide-class systemic/topical antibacterial); Sulfanilamide is **not currently marketed** in South Africa |
| Predicted New Indication | Infective Vaginitis |
| TxGNN Prediction Score | 91.87% |
| Evidence Level | L3 (observational/cohort/review-level evidence; includes one older RCT of a related combination product) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Sulfanilamide is not available in this evidence pack (DrugBank query returned no MOA record). Based on known pharmacology referenced throughout the evidence, Sulfanilamide is a **sulfonamide-class antibacterial** — it inhibits bacterial folate synthesis and has historically been formulated as vaginal suppositories/pessaries for bacterial vaginal discharge and mixed genital infections, as documented in older obstetrics/gynaecology literature within this pack (e.g., "Treatment of vaginal discharge by sulfonamide pessaries," "Leukorrhea therapy with sulfonamides").

The mechanistic link to **infective vaginitis** is therefore direct: vaginitis with a bacterial component is a plausible target for a topical antibacterial. The strongest single piece of evidence is a multicenter RCT (PMID 9132982) comparing clotrimazole, oral metronidazole, and a vaginal suppository containing **sulfanilamide + aminacrine + allantoin** for symptomatic trichomoniasis — a direct clinical test of a sulfanilamide-containing product in a vaginal infection context, though it is a combination product rather than sulfanilamide alone.

It is important to distinguish this from TxGNN's numerically highest-scoring prediction, **postmenopausal atrophic vaginitis** (score 99.93%, rank 612 in the model's global ranking). That association has zero supporting trials or literature, and the pack's own mechanistic assessment explicitly calls it a likely false positive driven by graph proximity to other vaginal-disease nodes rather than a genuine pharmacological signal — atrophic vaginitis is hormone-deficiency driven, not infectious, and has no plausible link to an antibacterial's mechanism. Two related predictions — **vaginal discharge** (L3, 20 references) and **trichomonal vulvovaginitis** (L3, 6 references) — cluster around the same infective-vaginitis theme and reinforce this as the most evidence-consistent repurposing signal, even though Trichomonas itself is a protozoan and not directly susceptible to sulfonamide activity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the 10 TxGNN-predicted indications (ClinicalTrials.gov and ICTRP searches returned zero results across all candidates, including Infective Vaginitis).

---

## Literature Evidence (Infective Vaginitis)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9132982](https://pubmed.ncbi.nlm.nih.gov/9132982/) | 1997 | RCT | Sexually Transmitted Diseases | Multicenter trial comparing clotrimazole, oral metronidazole, and a vaginal suppository containing sulfanilamide, aminacrine HCl, and allantoin for symptomatic trichomoniasis |
| [29190037](https://pubmed.ncbi.nlm.nih.gov/29190037/) | 2017 | RCT/Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Review of routine antibiotic prophylaxis after normal vaginal birth for reducing maternal infectious morbidity |
| [38393801](https://pubmed.ncbi.nlm.nih.gov/38393801/) | 2024 | Review | American Family Physician | Rapid evidence review of acute uncomplicated UTI diagnosis, noting vaginal discharge as a differentiating symptom |
| [29305250](https://pubmed.ncbi.nlm.nih.gov/29305250/) | 2018 | Review | American Journal of Obstetrics and Gynecology | UTI diagnosis across age groups; vaginal discharge as a key differentiating symptom |
| [18547131](https://pubmed.ncbi.nlm.nih.gov/18547131/) | 2008 | Review | Drugs | Contemporary management of uncomplicated urinary tract infections in women |
| [3522800](https://pubmed.ncbi.nlm.nih.gov/3522800/) | 1986 | Review | The Journal of Family Practice | Clinical review of vaginitis, cystitis, urethritis, and cervicitis diagnosis and management |
| [38577704](https://pubmed.ncbi.nlm.nih.gov/38577704/) | 2024 | Cohort | BioMed Research International | Antimicrobial resistance patterns in vaginal swab samples, Eritrea, 2019–2022 |
| [36310046](https://pubmed.ncbi.nlm.nih.gov/36310046/) | 2023 | Cohort | Japanese Journal of Infectious Diseases | Antimicrobial resistance profiles of bacteria isolated from vaginal/urine samples, Togo |
| [14107752](https://pubmed.ncbi.nlm.nih.gov/14107752/) | 1963 | Review | Bulletin of the World Health Organization | Gonorrhoea laboratory diagnosis methods; notes atypical L-forms after sulfanilamide treatment |
| [40391646](https://pubmed.ncbi.nlm.nih.gov/40391646/) | 2025 | Preclinical (in vitro) | Journal of Antimicrobial Chemotherapy | Repurposing antimalarials (pyrimethamine) against Gardnerella (bacterial vaginosis) vs. metronidazole — analogous repurposing precedent |

*Related candidate indications with additional literature: vaginal discharge (L3, 20 refs) and trichomonal vulvovaginitis (L3, 6 refs) — largely overlapping/older sources not duplicated here.*

---

## South Africa Market Information

Sulfanilamide has **no SAHPRA registrations** and is **not currently marketed** in South Africa (0 licenses on record). No product, dosage form, or approved indication text is available to summarize.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note: this evidence pack flags a **Blocking-severity data gap** — TFDA/SAHPRA label warnings and contraindications could not be retrieved, which by itself prevents this candidate from entering formal safety screening (Stage S1 safety review).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Sulfanilamide is unregistered and unmarketed in South Africa, and a Blocking-severity data gap (missing label warnings/contraindications) prevents any formal safety review. While three predicted indications (Infective Vaginitis, Vaginal Discharge, Trichomonal Vulvovaginitis) reached the "Research Question" evidence stage with historically relevant literature — including one directly relevant RCT of a sulfanilamide-containing vaginal suppository — the supporting evidence is largely decades old, small in scale, and mechanistically only partially aligned (e.g., Trichomonas is a protozoan, not a target of sulfonamide activity). TxGNN's top raw-score prediction (postmenopausal atrophic vaginitis) has no evidentiary support and should not be acted on.

**To proceed, the following is needed:**
- TFDA/SAHPRA-approved Professional Information (PI): warnings, contraindications, drug interactions (currently Blocking gap)
- Mechanism of action data from DrugBank (currently High-severity gap)
- Confirmation of any pathway to South African registration, given current "Not Marketed" / 0-license status
- If pursuing the infective vaginitis/vaginal discharge signal: an updated literature and modern-trial search, since existing supporting evidence predates current standard-of-care antimicrobial therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

