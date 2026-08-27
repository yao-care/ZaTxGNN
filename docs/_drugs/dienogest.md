---
layout: default
title: Dienogest
parent: 僅模型預測 (L5)
nav_order: 172
evidence_level: L5
indication_count: 10
---

# Dienogest
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

Using the evaluation report template directly (this is a document-generation task with a fully specified format already provided — no additional skill invocation needed), here is the report generated from the Evidence Pack.

---

# Dienogest: From Endometriosis Treatment to Amenorrhea

## One-Sentence Summary

Dienogest (marketed internationally as VISANNE) is a progestin currently used in the treatment of endometriosis. The TxGNN model predicts it may be effective for **Amenorrhea**, with **4 clinical trials** and **6 publications** currently available as supporting context — though none of these studies were designed to test amenorrhea as a primary treatment target. This candidate should be treated as a research hypothesis rather than an actionable clinical indication at this stage.

> **Note on data completeness:** The Evidence Pack does not contain a formally registered "original indication" (`drug.original_indications` is empty, and no SAHPRA/regulatory license text is available). The "Endometriosis" context above is inferred from the clinical trial evidence itself (e.g., trial titles referencing "Treatment of Endometriosis With Dienogest" and the VISANNE brand), not from confirmed regulatory documentation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis *(inferred from clinical trial evidence; no confirmed SAHPRA license record available)* |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 (mechanistic/indirect evidence; no trial directly targets amenorrhea as primary endpoint) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, a formal mechanism-of-action record for Dienogest is not available in this Evidence Pack (flagged as a data gap, DG002). However, the evidence pack's own repurposing rationale provides substantial mechanistic context: Dienogest is described in the supporting literature (PMID 41329046) as a fourth-generation progestin with a "high inhibition ratio and transformation index" — properties that suppress the hypothalamic-pituitary-ovarian (HPO) axis and induce endometrial decidualization/atrophy. This pharmacologic profile is explicitly associated with inducing a hypoestrogenic, amenorrhoeic state, which is a well-recognized and often clinically desired effect during long-term endometriosis therapy (e.g., to reduce menstrual blood loss and pelvic pain).

Endometriosis and amenorrhea are mechanistically linked in this context: therapeutic amenorrhea is a known *secondary pharmacologic effect* of dienogest when used for endometriosis, not evidence of a standalone, independently studied treatment indication. All four clinical trials retrieved for this candidate (NCT07164183, NCT07204093, NCT04495855, NCT02425462) enrolled patients for endometriosis treatment, with amenorrhea/menstrual pattern changes appearing only as a secondary observation or safety parameter rather than a primary study endpoint — consistent with the "Grade B" relevance rating applied to each trial in the evidence pack.

Because no trial or publication was designed specifically to evaluate dienogest as a treatment *for* amenorrhea (as opposed to amenorrhea occurring as a side effect of endometriosis therapy), the mechanistic rationale is judged plausible but the direct clinical evidence is currently insufficient to support a standalone indication claim.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07164183](https://clinicaltrials.gov/study/NCT07164183) | Phase 3 | Recruiting | 290 | Randomized comparison of Indinol Forto 200 mg vs. Visanne (dienogest) 2 mg for endometriosis; amenorrhea is not the primary study endpoint, but menstrual pattern is a likely secondary outcome. |
| [NCT07204093](https://clinicaltrials.gov/study/NCT07204093) | N/A | Active, not recruiting | 138 | Compares transdermal estradiol + dienogest "add-back" therapy vs. drospirenone for endometriosis symptom control and patient satisfaction; not a direct amenorrhea trial. |
| [NCT04495855](https://clinicaltrials.gov/study/NCT04495855) | N/A | Completed | 968 | Real-world observational study of dienogest (VISANNE) in endometriosis; menstrual bleeding/amenorrhea patterns likely captured as safety data, not as the primary endpoint. |
| [NCT02425462](https://clinicaltrials.gov/study/NCT02425462) | N/A | Completed | 895 | Prospective cohort study on quality-of-life outcomes with dienogest in Asian women with endometriosis; not designed to test amenorrhea treatment efficacy. |

**Rule note:** No SANCTR or PACTR-registered trials for this candidate were found in the Evidence Pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Pharmacodynamic/Mechanistic | Eur J Contraception & Reproductive Health Care | Describes dienogest's high progestational potency and ability to induce amenorrhoea and a hypoestrogenic state as part of its endometriosis treatment mechanism — the most directly relevant mechanistic evidence for this candidate. |
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Systematic Review/Meta-analysis (Bayesian) | BMC Pharmacology & Toxicology | Summarizes adverse event prevalence associated with dienogest use, relevant to safety context around treatment-induced amenorrhea. |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Cohort (long-term) | Reproductive Sciences | Retrospective cohort (n=514) on long-term efficacy/safety of dienogest for ovarian endometrioma beyond 12 months. |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Review | Reviews in Endocrine & Metabolic Disorders | Reviews the endocrine background of hormonal endometriosis treatment, including estrogen-dependency/progesterone-resistance mechanisms relevant to dienogest's action. |

**Note:** Two additional records returned by the literature search (PMID 40543564 — a Müllerian anomaly imaging review, and PMID 34918698 — a granulosa cell tumor case report) were excluded from this table as they are not substantively related to dienogest or amenorrhea and appear to be search noise.

---

## South Africa Market Information

Currently no SAHPRA registration or marketing records are available for Dienogest in this Evidence Pack. `taiwan_regulatory.market_status` reports the product as **Not Marketed**, with **0** registered licenses on file.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Data gap flagged:** This Evidence Pack has a **Blocking**-severity data gap (DG001) for TFDA/product-label warnings and contraindications — this data must be obtained before any S1 safety pre-assessment can proceed. Drug interaction (DDI) data was queried but returned no results (`query_status: not_found`).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported only by indirect, mechanistic evidence (L4) — no trial or publication was designed to test amenorrhea as a primary treatment target, and all four retrieved trials studied endometriosis with amenorrhea as, at most, a secondary observation. Combined with a **Blocking** safety data gap (no TFDA/SAHPRA label warnings or contraindications available) and the drug's current unregistered/unmarketed status in South Africa (0 SAHPRA licenses), the evidence is not yet sufficient to proceed even under guardrails.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI), including warnings, contraindications, and drug interaction data (resolves DG001, Blocking)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent source (resolves DG002)
- Formal regulatory record of the drug's currently approved indication(s), since none is present in this pack
- A purpose-designed study evaluating dienogest specifically for amenorrhea (or a related menstrual disorder indication) rather than relying on endometriosis-trial secondary outcomes
- Verification of SAHPRA registration/market status, given the current "Not Marketed" / 0-license record

---

*Additional context: TxGNN generated 9 further candidate indications for Dienogest beyond amenorrhea (ranks 2–10), all scored Evidence Level L4–L5 with a "Hold" recommendation. Notably, the rank-7 candidate ("hypogonadotropic hypogonadism with or without anosmia") returned 20 literature results that were entirely COVID-19-related anosmia studies — flagged in the source pack as literature-search contamination unrelated to the drug or indication, and excluded from consideration. None of the lower-ranked candidates are included in this report as they did not meet the threshold for further evaluation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

