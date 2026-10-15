---
layout: default
title: Azathioprine
parent: Model Prediction Only (L5)
nav_order: 54
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azathioprine: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Azathioprine is an immunosuppressive purine antimetabolite, listed in the data compiled for this report with rheumatoid arthritis as its original indication.
The TxGNN model's top-ranked prediction is **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare developmental malformation syndrome, with **0 clinical trials** and **0 publications** supporting it.
The model's lower-ranked predictions for **inflammatory bowel disease** and **ulcerative colitis** have substantial supporting evidence, but these are already established uses of azathioprine rather than new repurposing findings.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (from the knowledge-graph indication data; no approved indication text is available in the SAHPRA records compiled) |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Azathioprine is known to be metabolised to 6-thioguanine nucleotides. These inhibit purine synthesis and induce T-cell apoptosis, which gives it its immunosuppressive effect.

For the top-ranked prediction, **no plausible mechanistic link can be established.** The very high score (99.999%) comes from the knowledge-graph model alone. Colobomatous microphthalmia-rhizomelic dysplasia syndrome is a rare developmental and skeletal malformation condition. Immunosuppression is not expected to modify its pathogenesis. The same applies to the other highly ranked skeletal and limb malformation predictions (brachydactyly-syndactyly syndrome, acromesomelic dysplasia Hunter-Thompson type).

A high TxGNN score therefore does not by itself indicate clinical plausibility. The predictions with real biological and clinical support are the immune-mediated gut diseases covered below.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for colobomatous microphthalmia-rhizomelic dysplasia syndrome. Trials for the better-supported predictions are listed in the section below.

## Literature Evidence

Currently no related literature is available for this predicted indication. Publications for the better-supported predictions are listed in the section below.

---

## Better-Supported Predictions: Inflammatory Bowel Disease and Ulcerative Colitis

Two lower-ranked predictions carry strong evidence (Evidence Level L1, recommendation Proceed with Guardrails):

- **Inflammatory bowel disease** (TxGNN score 99.52%; 25 trials and 20 publications retrieved)
- **Ulcerative colitis** (TxGNN score 99.33%; 15 trials and 20 publications retrieved)

**Mechanism:** Azathioprine's T-cell apoptosis and purine synthesis inhibition suppress the T-cell-driven mucosal inflammation of IBD. It is a long-established thiopurine for maintaining remission. This is largely confirmation of existing clinical use, not novel repurposing.

**Important caveat:** Many of the trials below use azathioprine as a comparator or as part of a combination (for example with infliximab). They support its established role rather than proving a new indication. The pivotal SONIC-type Phase 3 trials are not in this dataset.

### Selected Clinical Trials

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00537316](https://clinicaltrials.gov/study/NCT00537316) | Phase 3 | Terminated | 242 | Infliximab alone or with azathioprine vs azathioprine alone in moderate-to-severe UC |
| [NCT00976690](https://clinicaltrials.gov/study/NCT00976690) | Phase 3 | Completed | 83 | Azathioprine vs mesalazine for preventing postoperative recurrence in Crohn's disease |
| [NCT00098111](https://clinicaltrials.gov/study/NCT00098111) | Phase 3 | Terminated | 31 | Dose-ranging study of azathioprine (Imuran) in active Crohn's disease |
| [NCT00984568](https://clinicaltrials.gov/study/NCT00984568) | Phase 3 | Terminated | 28 | Conventional step-up (including azathioprine) vs infliximab monotherapy in UC |
| [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) | Phase 3 | Unknown | 84 | Low-dose azathioprine plus allopurinol vs azathioprine monotherapy in UC |
| [NCT02177071](https://clinicaltrials.gov/study/NCT02177071) | Phase 4 | Completed | 211 | Infliximab with antimetabolites vs each alone in Crohn's patients in steroid-free remission |
| [NCT02425852](https://clinicaltrials.gov/study/NCT02425852) | Phase 4 | Completed | 65 | Early infliximab plus azathioprine vs corticosteroids plus azathioprine in acute severe UC |
| [NCT07235904](https://clinicaltrials.gov/study/NCT07235904) | Phase 4 | Recruiting | 300 | Top-down mirikizumab vs standard care with azathioprine in newly diagnosed UC |
| [NCT02247258](https://clinicaltrials.gov/study/NCT02247258) | Phase 2 | Terminated | 63 | Systematic vs endoscopy-directed azathioprine to prevent postoperative Crohn's recurrence |
| [NCT07424040](https://clinicaltrials.gov/study/NCT07424040) | N/A | Not yet recruiting | 154 | Infliximab alone or with azathioprine in paediatric Crohn's disease |

### Selected Literature

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | Cochrane review | Cochrane Database Syst Rev | Updated review of azathioprine and 6-mercaptopurine for maintaining remission in UC |
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | RCT | Gut | ACTIVE trial: top-down infliximab plus azathioprine vs azathioprine alone in steroid-responsive acute severe UC |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | Cochrane review | Cochrane Database Syst Rev | Earlier version of the review of thiopurines for UC remission maintenance |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | Meta-analysis | Aliment Pharmacol Ther | Efficacy of azathioprine and mercaptopurine in UC |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Review | J Crohns Colitis | State-of-the-art overview of thiopurine treatment in IBD |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | Review | Expert Rev Gastroenterol Hepatol | Molecular insights into azathioprine in IBD and clinical implications |
| [16048561](https://pubmed.ncbi.nlm.nih.gov/16048561/) | 2005 | Review | J Gastroenterol Hepatol | Pharmacogenetics and metabolite monitoring of azathioprine and 6-MP |
| [15177535](https://pubmed.ncbi.nlm.nih.gov/15177535/) | 2004 | Review | Gastroenterol Clin North Am | Critical review of efficacy and toxicity of azathioprine and 6-MP in IBD |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 37/26/0692 | Azathioprine 50 pch | Tablet (oral) | Not provided in the data compiled |
| D/26/98 | Imuran | Tablet (oral) | Not provided in the data compiled |

Both registrations are valid single-ingredient products. Essential Medicines List status could not be confirmed from the data compiled.

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** pancreatitis, thrombocytopenia, anaemia (including macrocytic anaemia), impaired renal function, infectious disease, fungal infection, dermatophytosis, lymphoma (including primary CNS lymphoma, lymphosarcoma and hepatosplenic T-cell lymphoma), hepatic vein thrombosis and Budd-Chiari syndrome.
- **Drug interactions (100 recorded; the main ones are shown):**
  - Moderate: mesalazine, balsalazide, olsalazine and sulfasalazine.
  - Minor: zinc acetate, zinc gluconate and zinc sulfate.
  - Other interactions are recorded without a severity grade, including aspirin, omeprazole, pantoprazole, metformin, doxycycline, amphotericin B and morphine.
- **Population-specific concerns:** Azathioprine is myelosuppressive and immunosuppressive. It could worsen leukopenia and infection risk in phagocyte or neutropenic immunodeficiencies (for example WHIM syndrome, chronic granulomatous disease), where the model also made predictions.
- **Recommended guardrails for IBD use:** TPMT/NUDT15 genotyping, metabolite monitoring, and surveillance for myelosuppression, hepatotoxicity, and malignancy (lymphoma, skin cancer).

Label warnings and contraindications were not available in the data compiled. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, colobomatous microphthalmia-rhizomelic dysplasia syndrome)

**Rationale:**
- The prediction rests on a knowledge-graph score alone. It has no trials, no literature and no plausible mechanism.
- Azathioprine's immunosuppressive action has no expected relevance to a developmental malformation syndrome.
- By contrast, inflammatory bowel disease and ulcerative colitis are supported by Cochrane reviews and multiple trials, and merit **Proceed with Guardrails**. They are existing uses rather than new repurposing opportunities.

**To proceed, the following is needed:**
- Mechanistic or preclinical evidence for any of the rare syndromes predicted, before any further consideration.
- The SAHPRA package insert (warnings, contraindications and approved indications), which is currently missing.
- Detailed mechanism of action data from DrugBank.
- For the IBD and UC indications, confirmation of whether they are already within the SAHPRA-approved indications, and a monitoring plan covering TPMT/NUDT15 testing, blood counts, liver function, and malignancy and infection surveillance.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

