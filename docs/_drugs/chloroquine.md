---
layout: default
title: Chloroquine
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 10
---

# Chloroquine
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

# Chloroquine: From Malaria to RF-Positive Polyarticular Juvenile Idiopathic Arthritis

## One-Sentence Summary

Chloroquine is a well-established antimalarial agent with secondary immunomodulatory properties, historically used for malaria, rheumatoid arthritis, and systemic lupus erythematosus. The TxGNN model's highest-ranked prediction is its potential efficacy in **rheumatoid factor-positive polyarticular juvenile idiopathic arthritis (RF+ polyJIA)**, with **no registered clinical trials** and **2 publications** providing indirect supporting evidence, primarily through mechanistic analogy with its sister drug hydroxychloroquine. Across all 10 predicted indications in this report, **osteoarthritis (rank 5)** emerges as the most clinically actionable finding, backed by a completed Phase 4 direct Chloroquine trial and a systematic review.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Malaria; rheumatoid arthritis; systemic lupus erythematosus (not currently registered in South Africa) |
| Predicted New Indication (Rank 1) | RF-Positive Polyarticular Juvenile Idiopathic Arthritis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 — preclinical / mechanistic studies only |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the structured evidence pack. Based on established pharmacological knowledge, Chloroquine is a 4-aminoquinoline that alkalinises lysosomal pH, blocking antigen processing and MHC class II-mediated antigen presentation to autoreactive T cells. It additionally suppresses innate immune signalling by antagonising Toll-like receptors TLR7 and TLR9 in B cells and plasmacytoid dendritic cells, reducing downstream production of the pro-inflammatory cytokines TNF-α, IL-6, and IL-1β. It also inhibits phospholipase A2 and the NLRP3 inflammasome, broadening its anti-inflammatory reach.

RF-positive polyarticular JIA shares important pathobiological features with adult seropositive rheumatoid arthritis, including B-cell activation, rheumatoid factor production, and immune complex-mediated joint inflammation. These mechanisms are directly targeted by Chloroquine's immunomodulatory profile: TLR7/9 antagonism interrupts B-cell activation driving RF production, while lysosomal inhibition reduces antigen presentation that sustains autoreactive T-cell responses. The immune complex deposition characteristic of the RF+ subtype further aligns with the drug's mechanism of action.

Chloroquine's sister compound hydroxychloroquine (HCQ) has been used safely in children with chronic inflammatory diseases including JIA over a 12-year observational period (PMID 33548956), and a 1996 case series documented that addition of HCQ arrested methotrexate-induced accelerated nodulosis specifically in two RF+ polyarticular JRA patients (PMID 8627446). While this constitutes indirect class evidence rather than Chloroquine-specific data, the mechanistic overlap is sufficient to justify further investigation. Direct Chloroquine clinical data in RF+ polyJIA remains entirely absent, limiting the evidence base to Level 4.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Chloroquine in rheumatoid factor-positive polyarticular juvenile idiopathic arthritis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24334641](https://pubmed.ncbi.nlm.nih.gov/24334641/) | 2014 | Prospective Cohort | The Journal of Rheumatology | Long-term real-world leflunomide experience in JIA (n not specified); provides treatment landscape context for refractory polyarticular JIA subtypes |
| [8627446](https://pubmed.ncbi.nlm.nih.gov/8627446/) | 1996 | Case Series | The Journal of Pediatrics | Two RF+ polyarticular-onset JRA patients developed accelerated nodulosis on methotrexate; nodules arrested by addition of hydroxychloroquine in one patient, suggesting antimalarial class activity specifically in this subtype |

---

## South Africa Market Information

Chloroquine is **not registered with SAHPRA** and is **not commercially marketed in South Africa**. No registration records were identified. Prescribers wishing to access this drug would require **Section 21 (unregistered medicine) authorisation** from SAHPRA prior to use.

> **Contextually relevant:** A case report (PMID 32386648) describes a 48-year-old South African woman with seropositive rheumatoid arthritis treated with Chloroquine 150 mg four times per week combined with methotrexate 30 mg weekly at a South African centre, with well-controlled symptoms over several years. This confirms the drug has been clinically used in South Africa despite its unregistered status. Hydroxychloroquine — the closely related sister compound — may have separate registration status and could represent a more accessible alternative with a better-characterised ophthalmological safety profile.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. As Chloroquine is unregistered in South Africa, consult the WHO Model Formulary or the manufacturer's prescribing information from a jurisdiction where it is registered. Report any adverse drug reactions to SAHPRA at www.sahpra.org.za.

The following clinically important safety signals are identified from literature included in this evidence pack:

- **Cardiac toxicity (serious):** Third-degree atrioventricular block documented in a patient on long-term Chloroquine for juvenile chronic arthritis (PMID 9523387); a separate case reports a rheumatoid nodule in the interventricular septum causing complete heart block in a patient on Chloroquine 200 mg daily (PMID 15222243). Baseline ECG and periodic cardiac monitoring are advised.
- **QTc prolongation:** Chloroquine carries a recognised QT interval prolongation risk (PMID 18078640); avoid concurrent use with other QT-prolonging agents and check for pre-existing conduction abnormalities.
- **Retinal toxicity:** Dose-dependent and cumulative; Chloroquine carries a higher retinal toxicity burden than hydroxychloroquine at standard antirheumatic doses. Annual ophthalmological review including fundoscopy is required.
- **Toxic myopathy:** HCQ-induced toxic myopathy causing diaphragmatic weakness and respiratory failure requiring prolonged mechanical ventilation was reported in a JIA patient (PMID 32787461); Chloroquine shares this risk.

---

## All Predicted Indications: Summary Overview

The TxGNN model identified 10 candidate indications for Chloroquine repurposing. The table below summarises findings across all predictions to support prioritisation decisions:

| Rank | Indication | TxGNN Score | Evidence Level | Clinical Trials | Publications | Decision |
|------|-----------|------------|---------------|----------------|-------------|---------|
| 1 | RF+ Polyarticular Juvenile Idiopathic Arthritis | 99.41% | L4 | 0 | 2 | Hold |
| 2 | Rheumatoid Nodulosis | 99.33% | L4 | 1 (indirect) | 15 | Hold |
| 3 | Juvenile Chronic Polyarthritis | 99.32% | L3 | 0 | 20 | Research Question |
| 4 | Juvenile Idiopathic Arthritis | 99.22% | L3 | 1 (indirect) | 20 | Research Question |
| **5** | **Osteoarthritis** | **98.66%** | **L2** | **5 (1 direct CQ trial)** | **20** | **Proceed with Guardrails** |
| 6 | Pseudoachondroplasia | 98.33% | L5 | 0 | 0 | Hold |
| 7 | Folliculitis Decalvans | 98.21% | L4 | 0 | 1 | Hold |
| 8 | Smouldering Systemic Mastocytosis | 98.05% | L5 | 0 | 0 | Hold |
| 9 | Telogen Effluvium | 98.04% | L5 | 0 | 0 | Hold |
| 10 | Alopecia Antibody Deficiency | 98.02% | L5 | 0 | 0 | Hold |

---

## Highlighted Finding: Osteoarthritis (Rank 5 — Strongest Evidence)

Although ranked 5th by TxGNN prediction score, **osteoarthritis** represents the most clinically actionable repurposing opportunity with Level 2 evidence, including a completed Phase 4 trial that directly tested Chloroquine in knee osteoarthritis.

**Mechanistic rationale:** Chloroquine inhibits the NLRP3 inflammasome, NF-κB, and TLR4 signalling pathways, reducing IL-1β, IL-6, and TNF-α-mediated expression of cartilage-degrading enzymes (MMP-3/13, ADAMTS-5). Lysosomal alkalinisation also modulates macrophage polarisation and autophagy — pathways increasingly implicated in age- and trauma-related OA (PMID 41035432, 2026). Inhibition of phospholipase A2 reduces arachidonic acid metabolites that contribute to synovial inflammation. The 2025 experimental study (PMID 40701030) directly demonstrates Chloroquine's anti-inflammatory cellular mechanisms, supporting biological plausibility.

### Clinical Trial Evidence (Osteoarthritis)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00805519](https://clinicaltrials.gov/study/NCT00805519) | Phase 4 | Completed | 230 | **Direct CQ evidence** — Prednisolone + Chloroquine add-on to glucosamine/chondroitin in knee OA; primary efficacy and safety study; highest relevance (Grade A) |
| [NCT01645176](https://clinicaltrials.gov/study/NCT01645176) | Phase 2 | Completed | 21 | Hydroxychloroquine + Atorvastatin for inflammation and pain in knee OA; indirect class evidence for antimalarial agents |
| [NCT01148043](https://clinicaltrials.gov/study/NCT01148043) | Phase 3 | Completed | 200 | Pharmacological treatment in OA; HCQ arm evaluated for hand OA — full results required to confirm CQ applicability |
| [NCT06768294](https://clinicaltrials.gov/study/NCT06768294) | Phase 2 | Not Yet Recruiting | 32 | Baricitinib (JAK inhibitor) in calcium pyrophosphate deposition disease (CPPD); related crystal arthropathy, provides mechanistic context |
| [NCT03975790](https://clinicaltrials.gov/study/NCT03975790) | N/A | Completed | 479 | Observational study of tofacitinib + MTX in RA; indirect disease management background only |

### Literature Evidence (Osteoarthritis — Selected)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33882635](https://pubmed.ncbi.nlm.nih.gov/33882635/) | 2022 | Systematic Review & Meta-analysis | Korean J Internal Medicine | Efficacy and safety of HCQ in OA evaluated across RCTs; foundational evidence synthesis for the antimalarial class in OA |
| [35000374](https://pubmed.ncbi.nlm.nih.gov/35000374/) | 2022 | RCT / Clinical Trial | Korean J Internal Medicine | HCQ efficacy in knee OA; direct comparator evidence for the antimalarial class |
| [34215704](https://pubmed.ncbi.nlm.nih.gov/34215704/) | 2021 | RCT (OA-TREAT) | RMD Open | Randomised double-blind multicentre trial of HCQ in inflammatory and erosive hand OA; most rigorous design for class evaluation |
| [26246395](https://pubmed.ncbi.nlm.nih.gov/26246395/) | 2015 | Narrative Review | Inflammopharmacology | Comprehensive pharmacology review of HCQ and CQ in SLE, RA, and OA; explicitly covers both compounds and OA evidence |
| [40701030](https://pubmed.ncbi.nlm.nih.gov/40701030/) | 2025 | Experimental (in vivo) | Cellular Immunology | Chloroquine (not HCQ) ameliorates autoimmune encephalomyelitis by inhibiting T-cell differentiation and pDC accumulation; directly demonstrates CQ immunomodulatory mechanism |
| [41035432](https://pubmed.ncbi.nlm.nih.gov/41035432/) | 2026 | Experimental (in vivo) | Bioactive Materials | Senescent macrophage remodelling in OA synovium alleviates joint damage; mechanistic rationale for CQ lysosomal effects in macrophage-driven OA pathology |
| [25348033](https://pubmed.ncbi.nlm.nih.gov/25348033/) | 2014 | RCT Protocol | Trials | OA-TREAT study protocol — HCQ in inflammatory erosive hand OA; describes outcome measures relevant to CQ trials |
| [18078640](https://pubmed.ncbi.nlm.nih.gov/18078640/) | 2007 | Safety Study | Clin Exp Rheumatology | Chloroquine and QTc interval in rheumatological patients — essential safety reference for OA use |
| [15918998](https://pubmed.ncbi.nlm.nih.gov/15918998/) | 2005 | Review | Current Rheumatology Reports | Calcium-containing crystals and OA; clinical implications for crystal-related OA pathology that CQ lysosomal effects may address |
| [12954956](https://pubmed.ncbi.nlm.nih.gov/12954956/) | 2003 | Review | Postgraduate Medical Journal | Intra-articular therapy in OA; treatment landscape context |

---

## Conclusion and Next Steps

### Primary Prediction — RF+ Polyarticular JIA

**Decision: Hold**

**Rationale:**
The TxGNN model's top-ranked prediction (RF+ polyarticular JIA, score 99.41%) is mechanistically plausible given Chloroquine's immunomodulatory profile against B-cell-driven autoimmune inflammation. However, no clinical trials and only 2 indirectly relevant publications exist, Chloroquine is unregistered in South Africa, and all key safety and MOA data fields remain outstanding. This combination of evidence gaps and regulatory barriers prevents clinical advancement at this stage.

**To proceed, the following is needed:**
- Full MOA documentation from DrugBank to complete mechanistic analysis
- Systematic literature search specifically targeting Chloroquine (not HCQ) in RF+ polyJIA
- SAHPRA Section 21 authorisation application if clinical use is being considered
- Evaluation of hydroxychloroquine as a more accessible, better-characterised registered alternative
- Paediatric dosing data and weight-based safety thresholds for South African children
- Ophthalmological and cardiac monitoring protocol development prior to any trial initiation

---

### Most Actionable Finding — Osteoarthritis (Rank 5)

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 4 trial (NCT00805519, n=230) directly tested Chloroquine add-on therapy in knee OA, and a systematic review with meta-analysis (PMID 33882635) supports the antimalarial class in OA. This evidence base meets Level 2 criteria. In the South African context, where access to biologic agents is often limited by cost (as documented in PMID 32386648), Chloroquine's low cost and oral administration make it a pragmatically attractive candidate for OA patients who have not responded to standard analgesics.

**To proceed, the following is needed:**
- Obtain and critically appraise full results from NCT00805519 to determine efficacy effect size and safety profile in OA
- Review PMID 33882635 meta-analysis to assess whether HCQ data can be extrapolated to CQ
- Develop a SAHPRA regulatory pathway — either a named-patient application or a Phase 3 registration trial
- Implement mandatory cardiac monitoring (baseline ECG, 6-monthly review) and annual ophthalmological review
- Consider a comparative effectiveness study: Chloroquine vs hydroxychloroquine in South African OA patients, to directly compare efficacy, safety, and affordability in the local context
- Ensure all clinical sites include standard YMYL disclaimer: *This research is for investigational purposes only and does not constitute medical advice; clinical use requires regulatory authorisation and specialist oversight*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

