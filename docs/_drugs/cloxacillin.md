---
layout: default
title: Cloxacillin
parent: Model Prediction Only (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Cloxacillin
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

# Cloxacillin: From Antibacterial Therapy to Chronic Rhinosinusitis

## One-Sentence Summary

Cloxacillin is a beta-lactamase-resistant penicillin active against *Staphylococcus aureus*, and it is marketed in South Africa. The TxGNN model predicts it may be useful for **chronic rhinosinusitis**, but **no clinical trials and no publications** were found for this specific indication, so the prediction rests on the model score alone. The best-supported prediction in this pack is actually **bacterial arthritis**, which has 2 related trials and preclinical and pharmacokinetic literature. That is close to established anti-staphylococcal use rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA data supplied (anti-staphylococcal penicillin antibiotic) |
| Predicted New Indication | Chronic rhinosinusitis |
| TxGNN Prediction Score | 98.31% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the Evidence Pack. Cloxacillin is a beta-lactamase-resistant penicillin that acts on penicillin-susceptible and methicillin-susceptible *S. aureus* (MSSA). Because *S. aureus* can contribute to chronic sinus disease, a bacterial component in chronic rhinosinusitis is plausible.

This link is weak. Chronic rhinosinusitis is often driven by inflammation rather than infection alone, and no study in the pack tests cloxacillin for it. The sister prediction, chronic ethmoidal sinusitis (98.28%), has the same weak rationale and also no clinical evidence.

Several high-scoring predictions have little or no plausible mechanism and are probably artefacts of the knowledge graph:
- Paranasal sinus neoplasm (98.17%): a narrow-spectrum antibacterial has no known antineoplastic activity.
- Celiac trunk compression syndrome, abdominal ectopic pregnancy and abdominal cystic lymphangioma (all 95.93%): non-infectious conditions with identical scores.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for chronic rhinosinusitis.

For **bacterial arthritis** (rank 5, score 97.68%), the most relevant trials retrieved were:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04563325](https://clinicaltrials.gov/study/NCT04563325) | Phase 4 | Completed | 180 | Oral-only vs initial IV-then-oral antibiotics for paediatric bone and joint infections. Cloxacillin as a study arm is not confirmed in the data. |
| [NCT04141787](https://clinicaltrials.gov/study/NCT04141787) | Phase 4 | Unknown | 310 | Home IV ceftriaxone for deep-seated staphylococcal infections. Cloxacillin is a likely comparator, but this is unconfirmed. |

No SANCTR or PACTR identifiers were found in the pack.

---

## Literature Evidence

Currently no related literature is available for chronic rhinosinusitis.

For **bacterial arthritis**, the most relevant publications retrieved were:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30772469](https://pubmed.ncbi.nlm.nih.gov/30772469/) | 2019 | Review | Int J Infect Dis | Updated review of antibiotic penetration into bone and joint tissue against common pathogens |
| [27455444](https://pubmed.ncbi.nlm.nih.gov/27455444/) | 2016 | Cohort | Pediatr Infect Dis J | Spanish multicentre study of the epidemiology and management of acute septic arthritis and osteomyelitis |
| [26695535](https://pubmed.ncbi.nlm.nih.gov/26695535/) | 2016 | Preclinical (animal) | Cell Microbiol | Cloxacillin controlled experimental *S. aureus* arthritis and reduced local and systemic cytokines |
| [17576849](https://pubmed.ncbi.nlm.nih.gov/17576849/) | 2007 | Preclinical (rabbit) | Antimicrob Agents Chemother | Moxifloxacin, cloxacillin and vancomycin showed no significant difference after 7 days in *S. aureus* arthritis |
| [10350394](https://pubmed.ncbi.nlm.nih.gov/10350394/) | 1999 | Pharmacokinetic study | J Antimicrob Chemother | Serum and synovial fluid concentrations and bactericidal activity of cloxacillin and fusidic acid against MSSA and MRSA isolates |
| [12010570](https://pubmed.ncbi.nlm.nih.gov/12010570/) | 2002 | Preclinical (animal) | Arthritis Res | Cloxacillin combined with a free radical trap (PBN) was effective against *S. aureus* septic arthritis |
| [3334740](https://pubmed.ncbi.nlm.nih.gov/3334740/) | 1988 | Preclinical (avian model) | J Orthop Res | Effect of different cloxacillin regimens on experimental staphylococcal septic arthritis |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. M/20.1.2/227 | Cloxacillin-fresenius powder for injecti | Injection |
| Reg. No. 27/11.4.3/0108 | Apen | Capsule |
| Reg. No. Z/20.1.2/0355 | Megamox S | Suspension |
| Reg. No. N/20.1.2/0014 | Cloxam | Capsule |

Approved indication text and manufacturer details were not available in the data supplied.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction (chronic rhinosinusitis, L5) has no trials or literature, and its mechanistic rationale is weak. Safety data from the SAHPRA PI are also missing.
- Bacterial arthritis is the most credible signal (L3), but it largely reflects existing anti-staphylococcal use and should be treated as a research question, not a new indication.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indications), to confirm label status and enable safety screening.
- Mechanism-of-action data (e.g. from DrugBank).
- For chronic rhinosinusitis: any clinical or microbiological evidence linking MSSA to the disease and cloxacillin response, before further consideration.
- For bacterial arthritis: confirmation of whether cloxacillin was used in the retrieved trials, and a check against current South African guideline status.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

