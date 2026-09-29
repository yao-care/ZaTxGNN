---
layout: default
title: Cefixime
parent: Model Prediction Only (L5)
nav_order: 103
evidence_level: L5
indication_count: 10
---

# Cefixime
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

# Cefixime: From Oral Cephalosporin Antibiotic to Ureaplasma Urethritis

## One-Sentence Summary

Cefixime is an oral third-generation cephalosporin antibiotic. The SAHPRA record supplied does not state an approved indication.
The TxGNN model ranks **Ureaplasma urethritis** as its top prediction, but there are **0 clinical trials** and **4 publications**, and none show cefixime treating Ureaplasma.
This is most likely a false-positive prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA record supplied |
| Predicted New Indication | Ureaplasma urethritis |
| TxGNN Prediction Score | 98.98% |
| Evidence Level | L5 (model prediction only; no study evaluates cefixime for this disease. The pack's pre-assigned level was L4) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the Evidence Pack. Cefixime belongs to the beta-lactam class. These drugs inhibit penicillin-binding proteins (PBPs), which cross-link the bacterial cell wall (peptidoglycan).

That mechanism argues against this prediction. Ureaplasma has no cell wall, so cefixime has no plausible target in it. The high TxGNN score most likely reflects the knowledge-graph link between cefixime and urethritis in general, not Ureaplasma specifically.

The retrieved literature supports this reading. It covers gonococcal or non-specific urethritis. One RCT reported that cefixime cured gonococcal urethritis but was ineffective against coexisting *Ureaplasma urealyticum* and *Chlamydia trachomatis*.

The best-supported prediction for cefixime is instead rank 2, **gonococcal urethritis** (see Conclusion).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2183719](https://pubmed.ncbi.nlm.nih.gov/2183719/) | 1990 | RCT (uncomplicated gonorrhoea, not Ureaplasma) | Antimicrob Agents Chemother | Single 800 mg cefixime cured 96 of 97 men with gonococcal urethritis (amoxicillin plus probenecid: 44 of 46). Neither regimen worked against coexisting *C. trachomatis* or *U. urealyticum*. |
| [20353145](https://pubmed.ncbi.nlm.nih.gov/20353145/) | 2010 | Review | Am Fam Physician | Diagnosis and treatment of urethritis in men. Main pathogens are *Chlamydia* and *Neisseria gonorrhoeae*. |
| [27025738](https://pubmed.ncbi.nlm.nih.gov/27025738/) | 2014 | Clinical study (azithromycin, not cefixime) | Antibiotics (Basel) | Single 2 g azithromycin extended-release dose gave a 90.9% eradication rate in gonococcal urethritis. Cefixime was tested only for susceptibility. |
| [35483632](https://pubmed.ncbi.nlm.nih.gov/35483632/) | 2022 | Case report/series | Infect Dis Now | First association of *Haemophilus pittmaniae* and *H. sputorum* with urethritis in men who have sex with men. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 51/20.1.1/0073 | Exsef | Tablet (oral) | Not stated in the record supplied |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no trials and no supporting literature, and cefixime has no plausible target in a cell-wall-deficient organism such as Ureaplasma.

**Other predictions in the pack:**

| Rank | Indication | Evidence Level | Pack Recommendation | Comment |
|------|------|------|------|------|
| 2 | Gonococcal urethritis | L2 | Proceed with Guardrails | Direct clinical evidence exists (PMID 2183719, 12673405). Treatment failures and rising cefixime MICs are documented, including in South Africa (PMID 23416957, 23299608). It should not be first-line where ceftriaxone-based regimens are recommended. |
| 3 | Uterine inflammatory disease | L4 | Research Question | One terminated Phase 3 trial ([NCT01072136](https://clinicaltrials.gov/study/NCT01072136), n=87) of empiric therapy for cervicitis. It is underpowered, and the cefixime arm is unconfirmed. |
| 4–10 | Xanthogranulomatous pyelonephritis, laryngitis, epiglottitis, laryngotracheitis, urogenital tuberculosis, tracheal disease, polyclonal hyperviscosity syndrome | L4–L5 | Hold | No supportive clinical evidence. Several are viral, non-infectious or intrinsically beta-lactam-resistant. |

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications and approved indications for Exsef), which is a blocking gap for safety screening.
- Mechanism of action data from DrugBank.
- For gonococcal urethritis: local South African susceptibility data, test-of-cure arrangements and a review of current national STI treatment guidelines. Trial designs for PMID 2183719 and 12673405 should also be verified against the full texts, because they were inferred from titles and abstracts only.

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

