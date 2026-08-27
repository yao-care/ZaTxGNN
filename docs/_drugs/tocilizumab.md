---
layout: default
title: Tocilizumab
parent: 僅模型預測 (L5)
nav_order: 439
evidence_level: L5
indication_count: 10
---

# Tocilizumab
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

# Tocilizumab: From Rheumatoid Arthritis to Ankylosing Spondylitis

## One-Sentence Summary

Tocilizumab is a humanized anti-IL-6 receptor monoclonal antibody, globally established for the treatment of rheumatoid arthritis (RA) and juvenile idiopathic arthritis.
The TxGNN model assigns its highest repurposing score to **Ankylosing Spondylitis (AS)** (score 99.99%), but this is a case where the evidence base actively **contradicts** the prediction: **9 clinical trials** and **19 publications** are available, including two independent, completed Phase 3 RCTs that were **terminated early for lack of efficacy**.
This is presented as a cautionary example — a high model confidence score does not equate to clinical evidence of benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid Arthritis (RA) — well-established global indication, confirmed indirectly by supporting literature in this evidence pack; not currently SAHPRA-registered |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Tocilizumab is a humanized monoclonal antibody that binds the IL-6 receptor (IL-6R), blocking both membrane-bound and soluble receptor signalling. Its efficacy in rheumatoid arthritis and juvenile idiopathic arthritis has been well established internationally and is reflected throughout the supporting literature in this pack (e.g. PMID 28841363, 22315615).

Rheumatoid arthritis and ankylosing spondylitis are both chronic inflammatory joint diseases, and IL-6 is a pleiotropic pro-inflammatory cytokine implicated broadly across rheumatic conditions — which is the most plausible reason the TxGNN knowledge graph linked the two. However, the pathophysiology of AS is now understood to be driven predominantly by the **IL-23/IL-17 and TNF axes**, with IL-6 playing a much smaller role than it does in RA.

This mechanistic distinction is not just theoretical — it was tested directly. Two independent Phase 2/3 randomized, double-blind, placebo-controlled trials (NCT01209702 and NCT01209689) enrolled AS patients specifically to test this hypothesis, and **both were terminated early after interim analyses showed insufficient efficacy**. This makes the AS prediction a rare case of "high TxGNN score, high-quality evidence, but a *negative* result" — the mechanistic rationale for a shared inflammatory pathway did not translate into clinical benefit, reinforcing that IL-6 blockade alone is not an effective strategy for AS.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 2/3 | Terminated | 306 | Randomized, double-blind, placebo-controlled trial of tocilizumab in TNF-antagonist-naïve AS patients who failed NSAIDs; **terminated for lack of efficacy** — key negative pivotal evidence |
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | Terminated | 113 | Randomized, double-blind, placebo-controlled trial of tocilizumab in AS patients with inadequate response to prior TNF antagonists; **terminated for lack of efficacy**, consistent with the sister trial above |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | Completed | 1431 | Real-world observational registry of Infliximab (not tocilizumab); provides background comorbidity data only, not direct evidence |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | Recruiting | 2500 | Multi-centre biomarker/cytokine profiling study across systemic inflammatory diseases; not yet reporting efficacy data |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | Completed | 60 | Mechanistic study of tocilizumab's effect on T follicular helper cells in RA patients; supportive mechanism data, not AS-specific |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | Recruiting | 10000 | Korean biologics/targeted-therapy safety registry covering RA, AS and psoriatic arthritis patients; observational only |
| [NCT07477795](https://clinicaltrials.gov/study/NCT07477795) | Phase 2 | Not yet recruiting | 52 | Trial of secukinumab (not tocilizumab) in Takayasu arteritis; indicates continued research interest in IL-pathway inhibition for vasculitis, not direct AS evidence |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large registry study of incident immune-mediated inflammatory disease risk in biologic-treated patients; background epidemiology only |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management study in rheumatology patients undergoing shoulder arthroplasty; not an efficacy trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT | Annals of the Rheumatic Diseases | BUILDER-1/BUILDER-2 randomized, placebo-controlled trials assessing short-term symptomatic efficacy of tocilizumab in AS — the primary published account of the negative trial results |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Systematic Review / Network Meta-analysis | Medicine | Comparative effectiveness review of all available biologic regimens for AS |
| [28413099](https://pubmed.ncbi.nlm.nih.gov/28413099/) | 2017 | Review | Seminars in Arthritis and Rheumatism | Second-line biologic therapy optimization in RA, PsA and AS |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Meta-analysis (Cohort) | Clinical Rheumatology | Risk of serious infections with biologic treatment in AS and non-radiographic axial spondyloarthritis |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Review | Inflammation & Allergy Drug Targets | Short review on antagonizing IL-6 specifically in AS |
| [20959960](https://pubmed.ncbi.nlm.nih.gov/20959960/) | 2011 | Review | Osteoporosis International | Systemic bone effects of biologic therapies in RA and AS |
| [39963138](https://pubmed.ncbi.nlm.nih.gov/39963138/) | 2025 | Review | Frontiers in Immunology | TB risk screening and preventive therapy in patients on biologic/targeted immunosuppressive agents, including AS populations |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Case Report | Frontiers in Medicine | Two cases of AA amyloidosis secondary to AS successfully treated with tocilizumab |
| [20851032](https://pubmed.ncbi.nlm.nih.gov/20851032/) | 2010 | Case Report | Joint Bone Spine | Tocilizumab used in a patient with AS and Crohn's disease refractory to TNF antagonists |
| [27789989](https://pubmed.ncbi.nlm.nih.gov/27789989/) | 2009 | Review | Open Access Rheumatology | Comprehensive review of biologics in RA, AS and psoriatic arthritis |

---

## South Africa Market Information

Tocilizumab currently has **no SAHPRA registrations** and is **not marketed** in South Africa according to the data available in this evidence pack. No registration numbers, product names, or approved indication texts could be extracted.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Additionally, the literature evidence gathered for this indication flags a class-level safety signal worth noting: biologic disease-modifying agents, including IL-6 pathway inhibitors, are associated with increased infection risk, including tuberculosis reactivation, in patients with chronic inflammatory arthritis (PMID 39963138). This should be considered in any future risk-benefit assessment, particularly in a South African setting with a high TB burden.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Despite a very high TxGNN prediction score (99.99%), the direct clinical trial evidence for this indication is **negative**: two independent, adequately designed Phase 2/3 and Phase 3 RCTs (NCT01209702, NCT01209689) were terminated early due to insufficient efficacy, and this is corroborated by the published trial report (PMID 23765873). AS pathophysiology is now understood to be driven primarily by the IL-23/IL-17 and TNF axes rather than IL-6, which mechanistically explains the failure. Pursuing this indication is not supported by current evidence.

**To proceed, the following is needed:**
- Detailed mechanism of action (MOA) data for Tocilizumab (currently a data gap, flagged High severity in this pack)
- SAHPRA/TFDA-approved Professional Information (PI) warnings and contraindications (currently a Blocking data gap preventing safety pre-screening)
- Should renewed interest arise, a clear scientific rationale (e.g., a biomarker-defined IL-6-high subgroup) distinct from the mechanism already tested and found ineffective would be required before any further clinical investment
- Note: other predicted indications in this evidence pack (e.g., polyarticular JIA, rank 7 and rank 10) show much stronger, already-approved-adjacent evidence and may warrant separate evaluation rather than this AS signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

