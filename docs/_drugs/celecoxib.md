---
layout: default
title: Celecoxib
parent: Model Prediction Only (L5)
nav_order: 109
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Celecoxib: predicted new indication Inflammatory spondylopathy (evidence level L5). Approved use: Rheumatoid arthritis, ankylosing spondylitis, osteoarthritis…"
monitor_inn: "Celecoxib"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "hypermobility of coccyx", "brachyolmia", "rheumatoid nodulosis", "inflammatory spondylopathy", "WHIM syndrome"]
---

# Celecoxib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Celecoxib: From Rheumatoid Arthritis and Other Arthritides to Inflammatory Spondylopathy
{: .text-alpha }

## One-Sentence Summary

Celecoxib is a COX-2 selective NSAID, originally used for rheumatoid arthritis, osteoarthritis, ankylosing spondylitis and juvenile idiopathic arthritis.
The TxGNN model's top-ranked predictions are mostly rare genetic or poorly evidenced conditions. The only prediction with substantial supporting evidence is **Inflammatory Spondylopathy** (axial spondyloarthritis and ankylosing spondylitis), with **11 clinical trials** and **20 publications**.
This is largely a confirmation of existing use, since ankylosing spondylitis is already an original indication, rather than a novel repurposing.

Note: the first-ranked TxGNN prediction (acromesomelic dysplasia, Hunter-Thompson type) has no supporting evidence and no credible mechanistic link. This report therefore focuses on the best-supported candidate, inflammatory spondylopathy (rank 9). The other candidates are summarised under Conclusion and Next Steps.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, ankylosing spondylitis, osteoarthritis, juvenile idiopathic arthritis (the SAHPRA registration record has no indication text, so this comes from the TxGNN knowledge graph) |
| Predicted New Indication | Inflammatory spondylopathy (rank 9 of the top 10; the best-supported candidate) |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L1 (see note below) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

*Evidence level note:* Of the trials listed, one completed Phase 3 RCT is directly relevant (NCT00648141), and a second completed Phase 3 trial (NCT00762463) has not yet been assessed for relevance. Several Phase 4 randomised trials and a published RCT (PMID 38228361) add further support. Together this supports L1, but the indication overlaps with an existing one.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, celecoxib selectively inhibits COX-2, which reduces prostaglandin E2-driven inflammation and pain.

Inflammatory spondylopathy covers axial spondyloarthritis and ankylosing spondylitis. NSAIDs are first-line therapy for these conditions, and celecoxib is a guideline-supported option. Ankylosing spondylitis is already among celecoxib's original indications, so this prediction mainly confirms existing use.

Some literature also suggests celecoxib may inhibit radiographic progression (new bone formation) in spondyloarthritis. A 2025 meta-analysis (PMID 39757202) reports that celecoxib is the only NSAID to show this effect, and the CONSUL RCT (PMID 38228361) tested adding celecoxib to anti-TNF therapy. These findings are interesting but still need confirmation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00648141](https://clinicaltrials.gov/study/NCT00648141) | Phase 3 | Completed | 458 | Celecoxib 200 mg QD and BID vs diclofenac SR over 12 weeks in ankylosing spondylitis |
| [NCT00762463](https://clinicaltrials.gov/study/NCT00762463) | Phase 3 | Completed | 240 | Celecoxib vs diclofenac SR in Chinese patients with ankylosing spondylitis, 6 weeks plus 6-week extension |
| [NCT02528201](https://clinicaltrials.gov/study/NCT02528201) | Phase 4 | Completed | 330 | Celecoxib 200 mg and 400 mg vs diclofenac over 12 weeks in ankylosing spondylitis |
| [NCT02758782](https://clinicaltrials.gov/study/NCT02758782) | Phase 4 | Completed | 156 | CONSUL: celecoxib added to golimumab vs golimumab alone, effect on spinal structural damage over 2 years |
| [NCT01934933](https://clinicaltrials.gov/study/NCT01934933) | Phase 4 | Completed | 150 | Etanercept and celecoxib alone or combined in active ankylosing spondylitis over 54 weeks |
| [NCT04115098](https://clinicaltrials.gov/study/NCT04115098) | Phase 2 | Terminated | 42 | N-of-1 trials comparing COX-2 selective and nonselective NSAIDs in axial spondyloarthritis (limited power) |
| [NCT03473665](https://clinicaltrials.gov/study/NCT03473665) | Phase 4 | Terminated | 9 | Pilot comparison of four NSAIDs in axial spondyloarthritis (too small to inform efficacy) |
| [NCT03190603](https://clinicaltrials.gov/study/NCT03190603) | Phase 4 | Completed | 12 | Effect of NSAIDs on MRI inflammatory lesions in axial spondyloarthritis |
| [NCT00813241](https://clinicaltrials.gov/study/NCT00813241) | Phase 1 | Completed | 16 | Pharmacokinetic study of enhanced-bioavailability celecoxib formulations in healthy volunteers |
| [NCT02638896](https://clinicaltrials.gov/study/NCT02638896) | Phase 4 | Unknown | 100 | Etanercept dose reduction in ankylosing spondylitis (celecoxib is not the primary intervention) |

No SANCTR or PACTR identifiers are available in the data compiled for this report. Two further registry entries (NCT01709656, NCT05960864) were omitted because they do not test celecoxib.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38228361](https://pubmed.ncbi.nlm.nih.gov/38228361/) | 2024 | RCT | Ann Rheum Dis | CONSUL trial: celecoxib added to golimumab vs golimumab alone, radiographic spinal progression over 2 years in r-axSpA |
| [39757202](https://pubmed.ncbi.nlm.nih.gov/39757202/) | 2025 | Systematic review/Meta-analysis | BMB Rep | Celecoxib was the only NSAID found to inhibit bone progression in spondyloarthritis |
| [40911151](https://pubmed.ncbi.nlm.nih.gov/40911151/) | 2025 | Umbrella review | Drugs | Synthesis of meta-analyses on celecoxib safety in chronic musculoskeletal conditions |
| [16960941](https://pubmed.ncbi.nlm.nih.gov/16960941/) | 2006 | Clinical trial | J Rheumatol | Celecoxib was efficacious and well tolerated for signs and symptoms of ankylosing spondylitis |
| [40676732](https://pubmed.ncbi.nlm.nih.gov/40676732/) | 2025 | N-of-1 trials | Rheumatology (Oxford) | Bayesian N-of-1 comparison of celecoxib, meloxicam and naproxen in axSpA |
| [40028763](https://pubmed.ncbi.nlm.nih.gov/40028763/) | 2025 | Retrospective cohort | Scand J Rheumatol | Cardiovascular and GI bleeding risk comparable between celecoxib and nonselective NSAIDs in ankylosing spondylitis |
| [36800138](https://pubmed.ncbi.nlm.nih.gov/36800138/) | 2023 | Clinical study | Clin Rheumatol | Imrecoxib and celecoxib affected bone metabolism markers and angiogenesis related to sacroiliac joint inflammation in axSpA |
| [18613804](https://pubmed.ncbi.nlm.nih.gov/18613804/) | 2008 | Review | Expert Opin Drug Saf | Safety of celecoxib in ankylosing spondylitis treatment |
| [17196469](https://pubmed.ncbi.nlm.nih.gov/17196469/) | 2007 | Meta-analysis | Am J Cardiol | Cardiovascular event risk in patients receiving celecoxib across randomised trials |
| [22141388](https://pubmed.ncbi.nlm.nih.gov/22141388/) | 2011 | Review | Drugs | Celecoxib for symptomatic relief in osteoarthritis, rheumatoid arthritis and ankylosing spondylitis |

For the lower-ranked candidates, the only publications are a case report on spinal rheumatoid vasculitis (PMID 34847873) and a JIA safety registry comparing celecoxib with nonselective NSAIDs (PMID 25057265).

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 33/3.1/0333 | Celebrex | Capsule (oral) | Not available in the data compiled for this report |

Essential Medicines List (EML) inclusion status is not available in the data compiled for this report.

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these come from TxGNN graph edges, not from approved label text):
hypertension, kidney disease, liver disease, gallbladder disease, congestive heart failure, peptic ulcer disease (including active), asthma, stroke and cerebrovascular disorders, myocardial infarction and other cardiovascular or heart disease, anaemia and hemoglobinopathy, and substance abuse/dependence.

**Drug interactions** (100 interactions recorded; the main ones are listed):
- **Major:** eliglustat
- **Moderate:** hydrocortisone, metformin and several sulfonylureas (glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide), nateglinide, exenatide, cimetidine, mesalazine, balsalazide, olsalazine, levofloxacin, metronidazole, kanamycin, naltrexone, fenfluramine and dexfenfluramine

**Additional safety literature:** The 2025 nationwide cohort (PMID 40028763) found cardiovascular and GI bleeding risk in ankylosing spondylitis was comparable between celecoxib and nonselective NSAIDs. A 2007 meta-analysis (PMID 17196469) examined cardiovascular risk with celecoxib.

Label warnings and contraindications from the SAHPRA-approved Professional Information (PI) are not available in the data compiled for this report. Please refer to the PI for authoritative safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for inflammatory spondylopathy / axial spondyloarthritis)

**Rationale:**
- Multiple completed Phase 3 and Phase 4 randomised trials and a published RCT support celecoxib in ankylosing spondylitis and axial spondyloarthritis. This is a confirmation of an existing indication rather than a new one, and the safety profile (cardiovascular, GI, renal) calls for careful patient selection.

**Other predicted candidates (all Hold):**
- Acromesomelic dysplasia Hunter-Thompson type, brachyolmia-amelogenesis imperfecta syndrome, brachyolmia, myosclerosis, WHIM syndrome: no evidence and no credible mechanistic link. The high scores likely reflect graph proximity artefacts.
- Rheumatoid vasculitis: only a case report; not a disease-modifying therapy, and cardiovascular risk is a concern.
- Rheumatoid nodulosis and hypermobility of coccyx: no clinical evidence.
- RF-positive polyarticular JIA: already within celecoxib's labelled JIA use, with only a safety registry available (Research Question).

**To proceed, the following is needed:**
- The SAHPRA Professional Information, including approved indications, warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of whether the SAHPRA-approved label covers ankylosing spondylitis or axial spondyloarthritis
- Review of the two unassessed Phase 3 trials and the unclassified publications
- A monitoring plan for cardiovascular, GI and renal risk, using the lowest effective dose, with caution when combined with anti-TNF therapy and in patients with cardiovascular risk factors
- Local data, such as any SANCTR or PACTR registered studies and EML status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

