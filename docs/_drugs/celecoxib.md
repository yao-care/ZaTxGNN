---
layout: default
title: Celecoxib
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 10
---

# Celecoxib
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

# Celecoxib: From Osteoarthritis/Rheumatoid Arthritis to Inflammatory Spondylopathy

> **Reporting note:** This report focuses on **Inflammatory Spondylopathy** (TxGNN rank 9), which carries the strongest evidence profile in this Evidence Pack (L1, 19 clinical trials, 20 publications) and the only actionable "Proceed with Guardrails" recommendation. Eight of the ten predicted indications are L5/Hold with no supporting evidence and are summarised in the Conclusion for completeness.

---

## One-Sentence Summary

Celecoxib is the first selective cyclooxygenase-2 (COX-2) inhibitor introduced into clinical practice, globally approved for osteoarthritis and rheumatoid arthritis, but not currently registered with SAHPRA in South Africa.
The TxGNN model predicts it may be effective for **Inflammatory Spondylopathy** (axial spondyloarthritis / ankylosing spondylitis), with **19 clinical trials** and **20 publications** currently supporting this direction — the strongest evidence profile across all ten predicted indications in this pack.
This prediction carries an **L1 evidence level** backed by multiple completed Phase 3 and Phase 4 RCTs, and Celecoxib is already approved for ankylosing spondylitis in the EU and other jurisdictions.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoarthritis; Rheumatoid Arthritis (globally approved; no SAHPRA registration available) |
| Predicted New Indication | Inflammatory Spondylopathy (axial spondyloarthritis / ankylosing spondylitis) |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L1 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Celecoxib belongs to the "coxib" class — selective cyclooxygenase-2 (COX-2) inhibitors. While detailed mechanism of action data is not available in the current Evidence Pack, Celecoxib's anti-inflammatory mechanism is well-characterised in the published literature: it selectively inhibits COX-2, reducing the synthesis of prostaglandin E2 (PGE2) — a key mediator of inflammation, pain, and tissue swelling — while largely sparing COX-1. This selectivity accounts for its reduced gastrointestinal adverse event profile compared to non-selective NSAIDs such as diclofenac or naproxen. Celecoxib is approved in one or more countries for osteoarthritis, rheumatoid arthritis, juvenile rheumatoid arthritis (≥2 years), ankylosing spondylitis, acute pain in adults, and primary dysmenorrhoea.

Inflammatory spondylopathy encompasses axial spondyloarthritis (axSpA) and ankylosing spondylitis (AS) — chronic immune-mediated diseases of the axial skeleton. The transition from osteoarthritis/RA to inflammatory spondylopathy is mechanistically straightforward: all three conditions share a COX-2/PGE2-driven inflammatory pathway, with COX-2 highly expressed in the synovial tissue of spondyloarthritis. Crucially, PGE2 not only mediates inflammatory pain and morning stiffness but also drives entheseal ossification (pathological new bone formation at tendon/ligament-to-bone junctions), a hallmark of AS progression. PGE2 modulates the Wnt/β-catenin signalling pathway that governs bone formation, suggesting that COX-2 inhibition may retard radiographic spinal progression — a potentially disease-modifying effect. Importantly, a 2025 study (PMID 39757202) demonstrated that Celecoxib is the **only** NSAID to show this bone-progression-inhibitory effect in spondyloarthritis, likely reflecting a COX-2-specific mechanism beyond the general class effect.

The TxGNN prediction therefore aligns closely with real-world regulatory approvals: Celecoxib holds an AS indication in the EU (EMA) and multiple other jurisdictions, and the trial evidence base (Phase 3 RCTs NCT00762463 and NCT00648141; Phase 4 RCTs NCT02758782 and NCT01934933) directly validates the model's output. The absence of SAHPRA registration in South Africa — not a lack of evidence — is the primary barrier to implementation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00762463](https://clinicaltrials.gov/study/NCT00762463) | Phase 3 | Completed | 240 | Multi-centre, double-blind RCT comparing Celecoxib 200 mg QD vs Diclofenac 75 mg SR QD in Chinese patients with ankylosing spondylitis, with a 6-week extension at Celecoxib 400 mg QD. Primary efficacy and safety evaluation; directly establishes AS efficacy in Asian populations. |
| [NCT00648141](https://clinicaltrials.gov/study/NCT00648141) | Phase 3 | Completed | 458 | 12-week double-blind RCT comparing Celecoxib 200 mg QD, Celecoxib 200 mg BID, and Diclofenac 75 mg SR BID in ankylosing spondylitis. Directly evaluates symptom relief and safety of once-daily vs twice-daily dosing regimens. |
| [NCT02758782](https://clinicaltrials.gov/study/NCT02758782) | Phase 4 | Completed | 156 | CONSUL trial: Randomised controlled trial assessing whether adding Celecoxib to anti-TNF therapy (Golimumab) reduces spinal structural damage progression over 2 years in AS, compared to anti-TNF monotherapy. Provides data for step-up combination therapy decisions. |
| [NCT01934933](https://clinicaltrials.gov/study/NCT01934933) | Phase 4 | Completed | 150 | Multi-centre, open-label, 3-arm RCT comparing Etanercept + Celecoxib vs Etanercept alone vs Celecoxib alone in active AS over 54 weeks. Primary endpoint: MRI SPARCC score of the sacroiliac joint. Key head-to-head combination vs monotherapy data. |
| [NCT02528201](https://clinicaltrials.gov/study/NCT02528201) | Phase 4 | Completed | 330 | 12-week double-blind RCT: Celecoxib 200 mg QD vs Celecoxib 400 mg QD vs Diclofenac TID in ankylosing spondylitis. Dose-finding and confirmatory study extending the results of a prior 6-week trial. |
| [NCT03190603](https://clinicaltrials.gov/study/NCT03190603) | Phase 4 | Completed | 12 | Pilot study evaluating the effects of NSAIDs (including Celecoxib) on MRI inflammatory lesions in axial spondyloarthritis. Small sample; provides mechanistic and imaging endpoint data. |
| [NCT04115098](https://clinicaltrials.gov/study/NCT04115098) | Phase 2 | Terminated | 42 | N-of-1 crossover trial comparing selective COX-2 inhibitors vs non-selective COX inhibitors in axial spondyloarthritis, measuring disease activity improvement without unacceptable side effects. Terminated early; conclusions incomplete — interpret with caution. |
| [NCT01709656](https://clinicaltrials.gov/study/NCT01709656) | N/A | Completed | 120 | Prospective open-label trial comparing mesenchymal stem cell injection vs NSAIDs (as active comparator) in active AS. Collected peripheral blood mononuclear cell gene expression and serum biomarkers, providing mechanistic context for NSAID use in AS pathogenesis. |
| [NCT01572675](https://clinicaltrials.gov/study/NCT01572675) | N/A | Completed | 547 | Post-marketing pharmacoepidemiological study of Etoricoxib and Celecoxib use in France under real-world conditions. Provides comparative class-level safety evidence for COX-2 inhibitors in routine clinical practice. |
| [NCT02355236](https://clinicaltrials.gov/study/NCT02355236) | Phase 4 | Unknown | 106 | Double-blind, double-dummy RCT comparing Naxozol (naproxen + esomeprazole) vs Celecoxib in osteoarthritis/RA/ankylosing spondylitis; examines gastrointestinal protection and pain relief, with Celecoxib as active comparator. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39757202](https://pubmed.ncbi.nlm.nih.gov/39757202/) | 2025 | RCT / Meta-analysis | BMB Reports | Celecoxib is the **only** NSAID demonstrated to inhibit radiographic bone progression in spondyloarthritis; diclofenac failed to replicate this effect, suggesting a COX-2-specific mechanism (not shared by all NSAIDs) in limiting entheseal ossification. |
| [36800138](https://pubmed.ncbi.nlm.nih.gov/36800138/) | 2023 | RCT | Clinical Rheumatology | Imrecoxib vs Celecoxib in axial spondyloarthritis: analysed changes in sacroiliac joint bone metabolism markers (osteocalcin, PINP, β-CTX) and angiogenesis after treatment; evaluated correlation with clinical efficacy scores. |
| [38228361](https://pubmed.ncbi.nlm.nih.gov/38228361/) | 2024 | RCT | Annals of the Rheumatic Diseases | CONSUL trial primary publication: Adding Celecoxib to Golimumab (anti-TNF) did not significantly reduce radiographic spinal progression vs anti-TNF alone over 2 years in radiographic axSpA. Important for combination therapy decision-making in the South African context. |
| [28626213](https://pubmed.ncbi.nlm.nih.gov/28626213/) | 2017 | RCT | Medical Science Monitor | Randomised comparison of Imrecoxib vs Celecoxib in 60 axSpA patients over 12 weeks; evaluated MRI SPARCC imaging scores and serum DKK-1 levels (a Wnt pathway inhibitor and bone formation marker), providing mechanistic insight into celecoxib's bone effects. |
| [38832489](https://pubmed.ncbi.nlm.nih.gov/38832489/) | 2024 | RCT | Scandinavian Journal of Rheumatology | Double-blind, placebo-controlled RCT of iguratimod combined with Celecoxib in active axial spondyloarthritis; evaluates safety and efficacy of combination disease-modifying + COX-2 inhibitor therapy. |
| [16960941](https://pubmed.ncbi.nlm.nih.gov/16960941/) | 2006 | RCT | Journal of Rheumatology | Early pivotal trial demonstrating Celecoxib is efficacious and well tolerated in treating signs and symptoms of ankylosing spondylitis; foundational evidence for AS indication in multiple jurisdictions. |
| [22141388](https://pubmed.ncbi.nlm.nih.gov/22141388/) | 2011 | Systematic Review | Drugs | Comprehensive systematic review of Celecoxib across osteoarthritis, rheumatoid arthritis, and ankylosing spondylitis; summarises EU-approved indications, efficacy trial data, and full safety profile. |
| [40028763](https://pubmed.ncbi.nlm.nih.gov/40028763/) | 2025 | Comparative Safety | Scandinavian Journal of Rheumatology | Nationwide retrospective cohort: cardiovascular disease and gastrointestinal bleeding risk with Celecoxib vs non-selective NSAIDs in ankylosing spondylitis — comparable risk profiles. Directly relevant for risk-benefit assessment in South African AS patients. |
| [25623277](https://pubmed.ncbi.nlm.nih.gov/25623277/) | 2015 | Population Cohort | Arthritis Care & Research | Swedish national population-based cohort: rates of gastrointestinal, renovascular, and cardiovascular adverse events with Etoricoxib, Celecoxib, and non-selective NSAIDs in AS/SpA — provides real-world comparative safety reference data. |
| [40911151](https://pubmed.ncbi.nlm.nih.gov/40911151/) | 2025 | Umbrella Review | Drugs | Umbrella review (systematic review of meta-analyses) of Celecoxib safety in adults with chronic musculoskeletal disorders; the most current and comprehensive safety synthesis available — recommended as primary safety reference pending SAHPRA PI. |

---

## South Africa Market Information

Celecoxib is **not currently registered with SAHPRA** and is not available on the South African market through standard channels. There are **no current SAHPRA licence records** for any Celecoxib product (brand or generic).

> **Regulatory pathways available to South African clinicians:**
> - **Section 21 authorisation** (unregistered medicine): Available for individual patients with exceptional clinical need, subject to SAHPRA approval. Application requires motivation by a registered healthcare professional.
> - **SAHPRA registration application**: Given L1 evidence and existing EU/FDA approval, a formal registration dossier (CTD format) could be submitted. Generic equivalents of Celebrex® are available internationally.
> - **Essential Medicines List (EML)**: Not currently listed. The L1 evidence base and global approval status would support a future EML submission for the axial spondyloarthritis / ankylosing spondylitis indication.
> - In the interim, healthcare professionals should consult the current FDA or EMA Prescribing Information / Summary of Product Characteristics (SmPC) for dosing, contraindications, and monitoring guidance.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. As Celecoxib is not currently SAHPRA-registered, healthcare professionals should consult the current Prescribing Information from an authorised regulatory body (FDA, EMA) as an interim reference. Report any adverse drug reactions to SAHPRA via the **MedSafety** online reporting system (www.sahpra.org.za).

> **Class-level safety considerations for South African clinicians** (based on published literature, pending local PI):
> The 2025 umbrella review (PMID 40911151) and the 2025 nationwide cohort study (PMID 40028763) provide the most current evidence synthesis on Celecoxib safety in chronic musculoskeletal conditions. As a COX-2 selective inhibitor, key monitoring considerations include cardiovascular risk (particularly in patients with established cardiovascular disease or multiple cardiovascular risk factors), renal function, and blood pressure. Long-term safety in AS patients on NSAIDs, including liver and kidney function monitoring, is addressed in PMID 39315555.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 and Phase 4 RCTs directly demonstrate Celecoxib's efficacy and safety in ankylosing spondylitis/inflammatory spondylopathy, and the drug is already approved for this indication in the EU, US, and other jurisdictions; the primary barrier to implementation in South Africa is the absence of SAHPRA registration — not a lack of clinical evidence.

**To proceed, the following is needed:**

- **Regulatory**: Initiate SAHPRA registration for Celecoxib (Celebrex® or an approved generic equivalent); alternatively, apply for Section 21 unregistered medicine authorisation for specific patients with confirmed axial spondyloarthritis/AS requiring COX-2 selective therapy
- **Safety documentation**: Obtain current, authorised PI from FDA or EMA as interim prescribing reference; establish an adverse drug reaction monitoring and reporting plan via SAHPRA MedSafety
- **Formulary and cost assessment**: Conduct a South African-specific health technology assessment comparing Celecoxib against currently SAHPRA-registered NSAIDs (e.g., diclofenac, meloxicam) for axSpA/AS, accounting for GI risk reduction benefits
- **Guidelines alignment**: Engage the South African Rheumatism and Arthritis Association (SARAA) to assess alignment with or inclusion in local spondyloarthritis treatment guidelines
- **EML submission**: Given L1 evidence and the global regulatory precedent, prepare a submission for inclusion on the Essential Medicines List under the spondyloarthritis/AS indication
- **MOA data gap**: Obtain complete mechanism of action data from DrugBank (DB00482) to support the pharmacological rationale in the SAHPRA registration dossier

---

> **Other TxGNN-predicted indications in this pack:** Eight additional indications (acromesomelic dysplasia Hunter-Thompson type, brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, hypermobility of coccyx, brachyolmia, rheumatoid nodulosis, WHIM syndrome, and rheumatoid vasculitis) all scored **L5/Hold** with no supporting clinical trials or literature. These predictions appear to reflect knowledge graph pathway proximity rather than biological specificity and are not recommended for further investigation at this time. The exception is **RF-positive polyarticular juvenile idiopathic arthritis** (rank 8, L3, Research Question), which has one relevant cohort safety study (PMID 25057265) and a plausible mechanistic link via synovial COX-2 overexpression; this warrants a dedicated paediatric evidence review before any prescribing decision.

---
*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. Healthcare professionals should exercise independent clinical judgement. Adverse drug reactions should be reported to SAHPRA.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

