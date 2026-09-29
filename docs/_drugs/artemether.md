---
layout: default
title: Artemether
parent: Model Prediction Only (L5)
nav_order: 46
evidence_level: L5
indication_count: 10
---

# Artemether
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

# Artemether: From Malaria Treatment to Acquired Angioedema

## One-Sentence Summary

Artemether is an artemisinin-derivative antimalarial, registered in South Africa as part of the combination product Coartem (artemether-lumefantrine). The TxGNN model ranks **acquired angioedema** as its top predicted new indication, but **no clinical trials and no publications** support this prediction, so it is a graph-based signal only. The highest-evidence predictions for this drug are the malaria indications (ranks 2 and 3), which are its established use and not true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data; artemether is an antimalarial (Coartem) |
| Predicted New Indication | Acquired angioedema |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Artemether is an artemisinin derivative whose endoperoxide bridge is thought to generate free radicals that kill *Plasmodium* parasites. It is used with lumefantrine as artemether-lumefantrine (AL).

Acquired angioedema is driven by bradykinin and complement pathways. There is **no documented link** between these pathways and artemether's antiparasitic mechanism. The very high score (0.999) most likely reflects the model's knowledge-graph neighbourhood, not a biological rationale. The same applies to the other angioedema predictions (angioedema, hereditary angioedema, RAAS-blocker-induced angioedema), which share this pattern.

The evidence pack rates all of these non-malaria predictions L5 with a Hold recommendation, including nephrogenic syndrome of inappropriate antidiuresis, acute contagious conjunctivitis, conjunctivitis and scleroderma. None has trials or literature behind it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for acquired angioedema.

---

## Literature Evidence

Currently no related literature available for acquired angioedema.

---

## Supporting Evidence for the Established Malaria Indications (Ranks 2–3)

These are not evidence for the primary prediction. They are shown because they are the only substantial evidence in this pack for artemether.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05842954](https://clinicaltrials.gov/study/NCT05842954) | Phase 3 | Completed | 1720 | KLU156 (ganaplacide + lumefantrine-SDF) vs Coartem in uncomplicated *P. falciparum* malaria; AL is the comparator |
| [NCT00344006](https://clinicaltrials.gov/study/NCT00344006) | Phase 3 | Completed | 1395 | Chlorproguanil-dapsone-artesunate vs artemether-lumefantrine in African children and adolescents |
| [NCT00316329](https://clinicaltrials.gov/study/NCT00316329) | Phase 3 | Completed | 1032 | Artesunate-amodiaquine (1 or 2 intakes a day) vs Coartem, non-inferiority at day 28 |
| [NCT01845701](https://clinicaltrials.gov/study/NCT01845701) | Phase 3 | Completed | 720 | Artesunate-amodiaquine and dihydroartemisinin-piperaquine vs AL over 42 days in Cameroon |
| [NCT01916954](https://clinicaltrials.gov/study/NCT01916954) | Phase 3 | Completed | 96 | Two AL regimens in pregnant women with uncomplicated *P. falciparum* malaria, DRC |
| [NCT00885287](https://clinicaltrials.gov/study/NCT00885287) | Phase 4 | Completed | 830 | AL efficacy, safety and PK interaction with nevirapine-based ART in HIV-infected patients, Tanzania |

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31210357](https://pubmed.ncbi.nlm.nih.gov/31210357/) | 2019 | Cochrane systematic review | Cochrane Database Syst Rev | Intramuscular artemether compared with quinine and artesunate in severe malaria |
| [22548983](https://pubmed.ncbi.nlm.nih.gov/22548983/) | 2012 | Systematic review | Malar J | Safety and efficacy of AL for uncomplicated *P. falciparum* malaria in pregnancy |
| [37979594](https://pubmed.ncbi.nlm.nih.gov/37979594/) | 2023 | RCT | Lancet | PRIMA: primaquine radical cure in *P. falciparum* malaria in areas co-endemic with *P. vivax* |
| [38705163](https://pubmed.ncbi.nlm.nih.gov/38705163/) | 2024 | Phase 2 RCT | Lancet Microbe | AL with or without single-dose primaquine, effect on gametocyte carriage and transmission, Mali |
| [40138574](https://pubmed.ncbi.nlm.nih.gov/40138574/) | 2025 | Molecular study | J Infect Dis | AL treatment selects *pfmdr1* increased copy number in African infections; reduced AL efficacy is emerging in Africa |

The evidence is for the fixed-dose combination with lumefantrine, not artemether alone.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 34/20.2.6 /0161 | Coartem | Tablet (oral) | Not provided in the registration data |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Two points from the supporting malaria trials are relevant to AL use:
- Antiretroviral co-treatment can change antimalarial exposure. One example is the efavirenz interaction studied in [NCT04708496](https://clinicaltrials.gov/study/NCT04708496).
- Artemisinin-resistance surveillance is needed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Acquired angioedema is a model-only prediction at L5. It has no trials, no literature and no plausible mechanistic link to artemether. The malaria predictions are well supported (L1), but they are artemether's established use and not repurposing.

**To proceed, the following is needed:**
- A targeted literature search on artemisinins and bradykinin or complement-mediated disease, to test whether any rationale exists
- Detailed mechanism of action data (MOA) from DrugBank
- SAHPRA Professional Information (warnings and contraindications), which is currently missing and blocks safety screening
- Confirmation of the approved indication text for the Coartem registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

