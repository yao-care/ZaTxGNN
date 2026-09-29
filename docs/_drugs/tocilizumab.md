---
layout: default
title: Tocilizumab
parent: Model Prediction Only (L5)
nav_order: 447
evidence_level: L5
indication_count: 10
---

# Tocilizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Tocilizumab: From Rheumatoid Arthritis to Ankylosing Spondylitis

## One-Sentence Summary

Tocilizumab is an interleukin-6 receptor (IL-6R) antibody, mainly used for rheumatoid arthritis and juvenile idiopathic arthritis according to the literature. The SAHPRA indication text was not supplied in the data.
The TxGNN model predicts it may be effective for **Ankylosing Spondylitis**. **Two randomised placebo-controlled trials** exist, but **both were terminated early**, and the reasons and outcomes are not in the supplied data.
Of the **8 trials** and **19 publications** retrieved, only these two trials and one trial report test tocilizumab directly in this disease.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Ankylosing spondylitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 (see note below) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

**Evidence level note:** The upstream scoring labelled this L1. The L1 rule requires at least two *completed* Phase 3 RCTs, and both AS trials (NCT01209702, NCT01209689) are *terminated*, so I graded conservatively at L3. The supporting evidence is meta-analyses, reviews and case reports, plus RCT reports whose results are not verified here.

## Why is This Prediction Reasonable?

Tocilizumab is a humanised monoclonal antibody that blocks the IL-6 receptor. IL-6 is a pro-inflammatory cytokine linked to systemic inflammation and bone turnover. Reviews in the evidence set (for example PMID 22452603) describe IL-6 as one of the cytokines implicated in the pathogenesis of ankylosing spondylitis, alongside TNF-α.

Rheumatoid arthritis and ankylosing spondylitis are both chronic inflammatory rheumatic diseases with overlapping cytokine pathways. Blocking IL-6 is therefore biologically plausible in axial spondyloarthritis. This plausibility is not proof: the pathogenesis of the two diseases differs (PMID 19822066), and the dedicated AS trials were stopped early. Detailed mechanism-of-action data from DrugBank were not available in the pack.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 2/3 | Terminated | 306 | Randomised, double-blind, placebo-controlled study of tocilizumab 8 mg/kg IV in AS patients who failed NSAIDs and were TNF-naïve. Termination reason not supplied |
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | Terminated | 113 | Randomised, double-blind, placebo-controlled study of tocilizumab 8 mg/kg or 4 mg/kg IV in AS patients with inadequate response to TNF antagonists. Termination reason not supplied |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | Completed | 60 | Mechanistic study of tocilizumab's effect on T follicular helper cells in RA. No AS efficacy endpoint |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | Recruiting | 10,000 | Korean registry of biologics safety in RA, AS and PsA. No hypothesis testing |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | Completed | 1,431 | Real-world observational study of an infliximab biosimilar. Not tocilizumab |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | Recruiting | 2,500 | Cytokine and biomarker profiling cohort in systemic inflammatory diseases |

The termination reasons and outcomes of the two AS trials should be checked directly on ClinicalTrials.gov before any further action. The remaining trials retrieved are observational or unrelated and add no efficacy evidence.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT report | Ann Rheum Dis | BUILDER-1 and BUILDER-2 placebo-controlled trials of tocilizumab in AS. Only the aim is in the supplied excerpt, so outcomes need verification |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Network meta-analysis | Medicine | Comparative effectiveness of biologic regimens in AS |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Meta-analysis | Clin Rheumatol | Serious infection risk with biologics in AS and nr-axSpA |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Review | Inflamm Allergy Drug Targets | Short review of IL-6 antagonism in AS |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Review | Curr Opin Rheumatol | Alternatives for AS patients refractory to TNF inhibition |
| [39963138](https://pubmed.ncbi.nlm.nih.gov/39963138/) | 2025 | Review | Front Immunol | Tuberculosis risk, screening and preventive therapy with biologics in chronic autoimmune arthritis |
| [31852268](https://pubmed.ncbi.nlm.nih.gov/31852268/) | 2020 | Review | Expert Rev Clin Immunol | Infection risk with biologics versus csDMARDs in inflammatory arthritis |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Case report | Front Med | Two AS patients with AA amyloidosis treated successfully with tocilizumab |
| [20851032](https://pubmed.ncbi.nlm.nih.gov/20851032/) | 2010 | Case report | Joint Bone Spine | Tocilizumab in one patient with AS and Crohn's disease refractory to TNF antagonists |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 48/30.1/0370 | Actemra sc prefilled syringe 0.9 ml | Injection |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The supplied literature also highlights serious infection and tuberculosis risk with biologics (PMIDs 29290076, 39963138). This is particularly relevant in South Africa, given the high TB burden.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The IL-6 rationale is plausible and randomised trials exist, but both dedicated AS trials were terminated with no efficacy outcomes in the supplied data. The pack lists the SAHPRA safety review as a blocking data gap. Ankylosing spondylitis also has well-established alternatives (TNF and IL-17 inhibitors), so the benefit case would need to be clear.

**To proceed, the following is needed:**
- The termination reasons and published results of NCT01209702 and NCT01209689, and the full BUILDER-1/2 outcomes (PMID 23765873)
- The SAHPRA Professional Information (warnings, contraindications, approved indications)
- Formal mechanism-of-action data from DrugBank
- A TB screening and infection-monitoring plan, if the candidate is reconsidered

**Note on other predictions:** The pack ranks polyarticular JIA and RF-positive polyarticular JIA (both L1, Phase 3 data) as candidates. These are probably existing labelled uses rather than new repurposing candidates, and should be checked against the SAHPRA label.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

