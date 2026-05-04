---
layout: default
title: Cloxacillin
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 10
---

# Cloxacillin
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

# Cloxacillin: From MSSA Staphylococcal Infections to Bacterial Arthritis

---

## One-Sentence Summary

Cloxacillin is a narrow-spectrum, penicillinase-resistant penicillin classically used to treat methicillin-susceptible *Staphylococcus aureus* (MSSA) infections of the skin, soft tissue, and bone.
The TxGNN model identifies **bacterial arthritis (septic arthritis)** as the highest-evidence repurposing candidate (TxGNN rank #5, score **97.68%**), backed by **2 clinical trials** and **20 publications**.
Although this indication is already recognised as the global standard-of-care for MSSA joint infections, Cloxacillin is currently **not registered with SAHPRA**, representing an administrative gap rather than a mechanistic or scientific one.

> **Note on TxGNN ranking:** The top-scored TxGNN prediction (rank #1 chronic rhinosinusitis, 98.31%) carries no clinical trial or literature evidence (Level L5, **Hold**). Bacterial arthritis ranks #5 by TxGNN score but holds the strongest evidence base (Level L2) and is the only indication recommended to **Proceed with Guardrails**. Ranks #2–4 (chronic ethmoidal sinusitis, paranasal sinus neoplasm, epiglottitis) and ranks #6–10 are all rated **Hold** due to weak mechanistic links and/or absent evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | MSSA skin, soft tissue, and bone infections (globally recognised standard-of-care; not formally registered in South Africa) |
| Predicted New Indication | Bacterial Arthritis (Septic Arthritis — MSSA) |
| TxGNN Prediction Score | 97.68% (TxGNN rank #5 among all predictions) |
| Evidence Level | L2 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on well-established pharmacological knowledge, Cloxacillin belongs to the isoxazolyl penicillin class and inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins (PBPs), making it intrinsically resistant to staphylococcal beta-lactamase. This renders it selectively and potently bactericidal against MSSA, while it remains inactive against MRSA and most Gram-negative organisms. The drug has decades of clinical use in this context in Europe, Australia, and many African countries, though it has never received formal SAHPRA registration.

*Staphylococcus aureus* is the leading causative pathogen in bacterial (septic) arthritis, accounting for approximately 40–50% of all cases in adults. In MSSA septic arthritis, Cloxacillin's mechanism of action — inhibiting the final transpeptidation step of peptidoglycan cross-linking, leading to bacterial cell lysis — directly targets the most common offending organism. Critically, adequate Cloxacillin drug concentrations in both synovial fluid and bone tissue have been confirmed in pharmacokinetic studies (PMID 10350394, PMID 30772469), establishing that therapeutic levels are achievable at the site of infection.

Multiple layers of preclinical and clinical evidence converge: Cloxacillin controlled MSSA-induced experimental septic arthritis in a mouse model by directly reducing bacterial burden and downregulating pro-inflammatory cytokines (PMID 26695535), and performed equivalently to vancomycin in a rabbit MSSA arthritis model (PMID 17576849). A completed nationwide Phase 4 RCT (NCT04563325) evaluated oral Cloxacillin/flucloxacillin as part of bone and joint infection management in children, directly validating the clinical framework. In global infectious disease guidelines (IDSA, BSAC, ESCMID), Cloxacillin or its analogue flucloxacillin represents the first-line recommended agent for confirmed MSSA septic arthritis. The TxGNN prediction for this indication therefore reflects an established therapeutic reality; the gap is regulatory, not scientific.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04563325](https://clinicaltrials.gov/study/NCT04563325) | Phase 4 | Completed | 180 | Nationwide multicentre, open-label, randomised non-inferiority trial in children with bone and joint infections (including septic arthritis). Compares oral-only antibiotics (cloxacillin/flucloxacillin as key candidates) versus standard initial IV-then-oral therapy over an identical total treatment duration. Directly addresses the primary predicted indication. |
| [NCT04141787](https://clinicaltrials.gov/study/NCT04141787) | Phase 4 | Unknown | 310 | Randomised non-inferiority trial comparing ceftriaxone home IV therapy against standard-of-care (typically cloxacillin/flucloxacillin IV) for deep-seated staphylococcal infections including bone and joint infections. Provides indirect clinical evidence positioning cloxacillin as the established reference comparator arm. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30772469](https://pubmed.ncbi.nlm.nih.gov/30772469/) | 2019 | Systematic Review | Int J Infectious Diseases | Comprehensive review of antibiotic penetration into bone and synovial tissues; confirms that cloxacillin achieves concentrations sufficient to exceed MSSA MIC values in joint compartments, supporting its pharmacokinetic rationale. |
| [27455444](https://pubmed.ncbi.nlm.nih.gov/27455444/) | 2016 | Multicentre Cohort | Pediatr Infect Dis J | Spanish multicentre study (n=multiple centres) describing aetiology, clinical characteristics, and antibiotic management of acute septic arthritis and osteomyelitis in children; anti-staphylococcal beta-lactams (including cloxacillin class) are central to treatment algorithms. |
| [26695535](https://pubmed.ncbi.nlm.nih.gov/26695535/) | 2016 | Animal Study (RCT model) | Cellular Microbiology | Cloxacillin directly controls SEC(+) MSSA-induced experimental arthritis in mice; demonstrates reduction in bacterial load, histopathological joint damage, and both local and systemic cytokine dysregulation — validating mechanistic efficacy in joint tissue. |
| [10350394](https://pubmed.ncbi.nlm.nih.gov/10350394/) | 1999 | PK/PD Study | J Antimicrob Chemother | Measured cloxacillin serum and synovial fluid concentrations following a single 2 g IV dose; satisfactory bactericidal activity against five MSSA isolates confirmed, directly supporting therapeutic adequacy at the joint infection site. |
| [17576849](https://pubmed.ncbi.nlm.nih.gov/17576849/) | 2007 | Animal Study | Antimicrob Agents Chemother | Head-to-head comparison of moxifloxacin, cloxacillin, and vancomycin in a rabbit MSSA arthritis model over 7 days; no significant difference between treatment arms, establishing cloxacillin as a valid and effective reference standard for MSSA septic arthritis. |
| [25104892](https://pubmed.ncbi.nlm.nih.gov/25104892/) | 2014 | Cohort | J Orthopaedics | Hospital-based cohort study of primary septic arthritis (no prosthetic joints); S. aureus identified as the predominant pathogen, with beta-lactam–based therapy as the cornerstone of treatment. |
| [12010570](https://pubmed.ncbi.nlm.nih.gov/12010570/) | 2002 | Animal Study | Arthritis Research | Combined systemic administration of cloxacillin and free radical trap PBN in MSSA arthritis model; cloxacillin effectively eradicates bacteria, but adjunctive anti-inflammatory treatment is needed to prevent cartilage destruction driven by the host inflammatory response. |
| [21742832](https://pubmed.ncbi.nlm.nih.gov/21742832/) | 2011 | Animal Study | J Infectious Diseases | Combination of TNF inhibitor and antibiotics (including cloxacillin) in murine MSSA staphylococcal arthritis and sepsis; joint inflammation and bone erosions reduced with combination therapy, supporting the concept of adjunctive immune modulation alongside cloxacillin. |
| [25365902](https://pubmed.ncbi.nlm.nih.gov/25365902/) | 2014 | Cohort | J Med Assoc Thailand | Evaluated first-line antibiotic success rates (including cloxacillin-based regimens) in culture-negative sub-acute and chronic septic arthritis; provides real-world outcome data on empirical cloxacillin use. |
| [3334740](https://pubmed.ncbi.nlm.nih.gov/3334740/) | 1988 | Animal Study | J Orthopaedic Research | Avian model of acute staphylococcal septic arthritis used to study different cloxacillin treatment regimens (frequency and timing of administration); established relationship between timely initiation and improved disease outcome. |

---

## South Africa Market Information

Cloxacillin is currently **not registered with SAHPRA** and has no active product registrations in South Africa. No license records were identified in the regulatory database.

| Registration Status | Details |
|---------------------|---------|
| SAHPRA Registrations | None (0 registered products) |
| Market Status | Not marketed |
| Essential Medicines List (EML) | Not listed |
| Comparable Registered Analogues | Flucloxacillin (a closely related isoxazolyl penicillin) may be available in some South African contexts; confirm with SAHPRA and local pharmacy supply chains |

> For clinical use in South Africa, a **Section 21 authorisation** (SAHPRA Regulation 21 — unregistered medicines) would be required, or a formal product registration application should be considered. Cloxacillin is registered and routinely used in the UK (MHRA), Australia (TGA), and multiple African countries with comparable regulatory frameworks.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. As Cloxacillin is not currently registered in South Africa, prescribers should consult the product information approved by a comparable regulatory authority (e.g., UK MHRA Summary of Product Characteristics, TGA Australia PI) prior to use. Key areas to review include penicillin hypersensitivity/anaphylaxis risk, hepatotoxicity (particularly with prolonged courses), and renal dosing adjustments.

Report adverse drug reactions to **SAHPRA** via the MedSafety reporting system.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bacterial arthritis caused by MSSA is a globally accepted, guideline-endorsed indication for Cloxacillin, supported by a completed Phase 4 RCT, multiple pharmacokinetic studies confirming joint penetration, and direct animal model validation. The complete absence of SAHPRA registration is an administrative barrier, not a reflection of any mechanistic doubt or unresolved safety signal — making this an actionable regulatory pathway rather than a research question.

**To proceed, the following is needed:**

- **Regulatory pathway**: Submit a Section 21 (unregistered medicine) application to SAHPRA, or initiate a full product registration dossier for Cloxacillin (or its analogue flucloxacillin)
- **Safety data package**: Obtain complete warnings, contraindications, and drug interaction data from MHRA or TGA-approved product information to fill current data gaps
- **Mechanism of action documentation**: Retrieve formal MOA data from DrugBank (DB01147) to support the regulatory dossier and prescriber information
- **Local microbiological data**: Establish the South African prevalence of MSSA vs. MRSA in septic arthritis cases (to confirm that empirical cloxacillin selection remains appropriate vs. vancomycin or daptomycin)
- **Antimicrobial stewardship alignment**: Review compatibility with South African Antibiotic Stewardship Programme (SAASP) guidelines and assess suitability for inclusion in the Essential Medicines List (EML)
- **Paediatric dosing protocol**: Leverage NCT04563325 outcome data to define oral step-down dosing guidance for the South African paediatric population
- **Supply chain assessment**: Confirm reliable procurement of a quality-assured Cloxacillin or flucloxacillin product from a WHO-prequalified or SAHPRA-approved manufacturer

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. For clinical decisions, consult the relevant approved Professional Information and applicable South African treatment guidelines.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

