---
layout: default
title: Cloxacillin
parent: Model Prediction Only (L5)
nav_order: 142
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

# Cloxacillin: From Staphylococcal Infections to Chronic Rhinosinusitis

## One-Sentence Summary

Cloxacillin is a beta-lactamase-stable penicillin, originally used for staphylococcal infections such as *Staphylococcus aureus* infection, pharyngitis, staphylococcal pneumonia and sinusitis.
The TxGNN model predicts it may be effective for **chronic rhinosinusitis**, but there are currently **no clinical trials and no publications** supporting this specific prediction.
The score largely reflects overlap with the existing sinusitis indication rather than a genuinely new use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Staphylococcal infections (including *S. aureus* infection, pharyngitis, staphylococcal pneumonia, sinusitis) |
| Predicted New Indication | Chronic rhinosinusitis |
| TxGNN Prediction Score | 98.31% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

*Note: The registration records compiled for this report contain no approved-indication text, so the original indications above come from the TxGNN knowledge graph, not from SAHPRA label text.*

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, cloxacillin is an isoxazolyl penicillin that is stable against staphylococcal beta-lactamase. Its efficacy in staphylococcal infections is established, and it may be mechanistically applicable to sinus infections caused by methicillin-susceptible *S. aureus*.

The high score most likely reflects the fact that sinusitis is already among cloxacillin's known indications. Chronic rhinosinusitis is typically biofilm-associated and often polymicrobial, and cloxacillin has a narrow, anti-staphylococcal spectrum. No trials or literature were found to support its use in the chronic form. The second-ranked prediction, chronic ethmoidal sinusitis (score 98.28%), is a subtype of sinusitis and largely overlaps with the existing use, so it is not a true repurposing candidate either.

### Other predictions reviewed

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 4 | Epiglottitis | 98.12% | L4 | Plausible anti-staphylococcal cover, but empirical therapy usually targets *H. influenzae* and streptococci with broader agents. Only a 1988 case series is available. |
| 5 | Bacterial arthritis | 97.68% | L4 | The most credible new direction. Cloxacillin is active against methicillin-susceptible *S. aureus*, the leading cause of septic arthritis. Support is indirect (see below). |
| 6 | Pneumonia | 97.22% | L4 | Mostly reflects the existing staphylococcal pneumonia indication. Retrieved literature is largely non-specific. |
| 7 | Laryngitis | 96.32% | L4 | Most laryngitis is viral. Only a case report of glottic *S. aureus* and unrelated studies are available. |
| 3, 8, 9, 10 | Paranasal sinus neoplasm, celiac trunk compression syndrome, abdominal ectopic pregnancy, abdominal cystic lymphangioma | 95.9–98.2% | L5 | No plausible antibacterial mechanism. Likely knowledge-graph artifacts. Three of these share an identical score, suggesting a non-informative prediction. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for chronic rhinosinusitis.

For the most plausible alternative prediction, **bacterial arthritis**, one trial was identified:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04141787](https://clinicaltrials.gov/study/NCT04141787) | Phase 4 | Unknown | 310 | Randomised non-inferiority trial of home intravenous ceftriaxone for deep-seated staphylococcal infections (bone, joint, spine). Cloxacillin is likely a standard-of-care comparator, not the experimental drug, so the evidence is indirect. |

No SANCTR or PACTR identifiers were found in the data compiled for this report.

---

## Literature Evidence

Currently no related literature available for chronic rhinosinusitis.

For **bacterial arthritis** (the strongest alternative direction), selected publications are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30772469](https://pubmed.ncbi.nlm.nih.gov/30772469/) | 2019 | Review | Int J Infect Dis | Updated review of antibiotic penetration into bone and joint tissue. |
| [10350394](https://pubmed.ncbi.nlm.nih.gov/10350394/) | 1999 | Pharmacokinetic study | J Antimicrob Chemother | Cloxacillin (2 g IV) and fusidic acid concentrations and bactericidal activity in serum and synovial fluid against MSSA and MRSA. |
| [27455444](https://pubmed.ncbi.nlm.nih.gov/27455444/) | 2016 | Cohort | Pediatr Infect Dis J | Spanish multicentre study of epidemiology and management of paediatric osteoarticular infection. |
| [26695535](https://pubmed.ncbi.nlm.nih.gov/26695535/) | 2016 | Preclinical (animal) | Cell Microbiol | Cloxacillin controlled experimental *S. aureus* arthritis and was associated with reduced local and systemic cytokines. |
| [3334740](https://pubmed.ncbi.nlm.nih.gov/3334740/) | 1988 | Preclinical (animal) | J Orthop Res | Effect of different cloxacillin regimens in an avian model of staphylococcal septic arthritis. |
| [17576849](https://pubmed.ncbi.nlm.nih.gov/17576849/) | 2007 | Preclinical (animal) | Antimicrob Agents Chemother | Moxifloxacin, cloxacillin and vancomycin showed no significant difference after 7 days in a rabbit *S. aureus* arthritis model. |
| [25104892](https://pubmed.ncbi.nlm.nih.gov/25104892/) | 2014 | Cohort | J Orthop | Clinical and microbiological characteristics of septic arthritis in a hospital cohort. |
| [6695158](https://pubmed.ncbi.nlm.nih.gov/6695158/) | 1984 | Clinical comparison | Scand J Infect Dis | Cefuroxime versus cloxacillin and/or ampicillin in acute septic arthritis. |

For **epiglottitis**, one 1988 case series is available ([3209935](https://pubmed.ncbi.nlm.nih.gov/3209935/), adult epiglottitis in Singapore, *J Laryngol Otol*), with no cloxacillin-specific efficacy data.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M/20.1.2/227 | Cloxacillin-fresenius powder for injection | Injection | Not stated in the data compiled |
| 27/11.4.3/0108 | Apen | Capsule | Not stated in the data compiled |
| Z/20.1.2/0355 | Megamox S | Suspension | Not stated in the data compiled |
| N/20.1.2/0014 | Cloxam | Capsule | Not stated in the data compiled |

All four registrations are valid single-ingredient products. Essential Medicines List (EML) status could not be confirmed from the data compiled for this report.

---

## Safety Considerations

**Contraindications from the knowledge graph** (these come from graph edges, not label text): kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, infectious mononucleosis, and chronic Epstein-Barr virus infection syndrome.

**Drug Interactions:** 17 interactions were identified.
- **Major:** methotrexate.
- **Moderate:** doxycycline, tetracycline, minocycline, demeclocycline, balsalazide, picosulfuric acid, iodide I-131, iodide I-123, warfarin, proguanil, chloramphenicol, ethinylestradiol, mycophenolic acid, pemetrexed.
- **Minor:** clarithromycin, erythromycin.

Label-based warnings and contraindications are not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, chronic rhinosinusitis, has no trials or literature and mostly overlaps with cloxacillin's existing sinusitis indication. Bacterial arthritis is the most credible genuine extension (L4, indirect evidence), but it is also not yet supported by direct clinical data.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications and approved indications). This is currently a blocking gap for safety screening.
- Mechanism of action data for cloxacillin.
- For bacterial arthritis, direct comparative clinical data on cloxacillin against current standard therapy, ideally from the South African setting with local MSSA/MRSA susceptibility patterns.
- For chronic rhinosinusitis, evidence of benefit in the chronic, biofilm-associated, polymicrobial form, or confirmation that the prediction is only a restatement of the labeled sinusitis use.
- Renal function considerations and a review of the major methotrexate interaction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

