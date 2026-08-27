---
layout: default
title: Mupirocin
parent: 僅模型預測 (L5)
nav_order: 326
evidence_level: L5
indication_count: 10
---

# Mupirocin
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

Using the report template above directly (no additional skill needed — this is a structured content-generation task matching the loaded system prompt).

**Note on candidate selection:** This evidence pack contains 10 predicted indications ranked by raw TxGNN score. `predicted_indications[0]` (pleural empyema) has zero supporting evidence and its own rationale states mupirocin *cannot* reach therapeutic concentration there — reporting it as the lead candidate would be clinically misleading. I've instead led with **rank 9, Staphylococcal Scalded Skin Syndrome (SSSS)**, the only candidate reaching evidence stage S2/L3 with a coherent mechanism. The other 9 candidates are summarized briefly at the end for completeness.

---

# Mupirocin: From Topical Skin Infections to Staphylococcal Scalded Skin Syndrome

## One-Sentence Summary

Mupirocin is a topical antibacterial agent used for skin infections (e.g., impetigo) and nasal *Staphylococcus aureus* decolonization; detailed original-indication and mechanism-of-action data were not available in this evidence pack. The TxGNN model predicts potential utility as an adjunct in **Staphylococcal Scalded Skin Syndrome (SSSS)**, a toxin-mediated *S. aureus* skin disease, supported by **14 publications** (no dedicated clinical trials). Mupirocin is currently **not marketed in South Africa (0 SAHPRA registrations)**, and safety/PI data are a **Blocking** data gap, so this remains a research-stage signal rather than a practice-ready finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in South African regulatory data (data gap); generally known as a topical antibacterial for skin infections and nasal *S. aureus* decolonization |
| Predicted New Indication | Staphylococcal Scalded Skin Syndrome (SSSS) |
| TxGNN Prediction Score | 95.57% (rank 16,549 of all drug-disease pairs) |
| Evidence Level | L3 (observational/cohort studies, no completed RCT) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in this evidence pack (data gap). Based on known pharmacology, mupirocin inhibits bacterial isoleucyl-tRNA synthetase, giving it potent activity against *Staphylococcus aureus*, including MRSA — the same organism responsible for SSSS.

SSSS is caused by exfoliative-toxin-producing strains of *S. aureus*, most often in neonates and young children. It is not a new disease class for mupirocin so much as a different clinical setting for the same target organism: rather than treating localized impetigo or decolonizing the nares, mupirocin here is used as a topical adjunct alongside systemic antibiotics, or for outbreak-control decolonization of affected/colonized patients and contacts.

This mechanistic continuity — same pathogen, same drug target, different clinical presentation of the toxin-mediated disease spectrum — is why multiple case series and cohort studies (summarized below) describe mupirocin ointment being used alongside IV antibiotics in SSSS management and in neonatal-unit outbreak control, even though no randomized trial has tested it as a standalone SSSS therapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37404367](https://pubmed.ncbi.nlm.nih.gov/37404367/) | 2023 | Cohort | Clinical, Cosmetic and Investigational Dermatology | Compared outcomes of different IV antibiotics combined with 2% mupirocin ointment in pediatric SSSS — most directly on-topic study |
| [15482208](https://pubmed.ncbi.nlm.nih.gov/15482208/) | 2004 | Review/Cohort | Expert Review of Anti-infective Therapy | Reviews treatment of bullous impetigo and SSSS in infants |
| [8435912](https://pubmed.ncbi.nlm.nih.gov/8435912/) | 1993 | Review | Dermatologic Clinics | Reviews staphylococcal skin disease control, notes topical mupirocin as a valuable addition |
| [16218885](https://pubmed.ncbi.nlm.nih.gov/16218885/) | 2005 | Review | Expert Opinion on Pharmacotherapy | Reviews treatment options for impetigo/staphylococcal skin infection in children |
| [19000857](https://pubmed.ncbi.nlm.nih.gov/19000857/) | 2008 | Review | Archives de Pédiatrie | Reviews management of pediatric skin and soft tissue infections including topical treatment role |
| [16009455](https://pubmed.ncbi.nlm.nih.gov/16009455/) | 2005 | Cohort (outbreak investigation) | Journal of Hospital Infection | Nosocomial SSSS outbreak in 13 neonates; epidemiological investigation and infection-control response |
| [31725120](https://pubmed.ncbi.nlm.nih.gov/31725120/) | 2020 | Cohort | Pediatric Infectious Disease Journal | Molecular epidemiology of ST121 *S. aureus* clone causing rising SSSS cases in Houston children |
| [9576389](https://pubmed.ncbi.nlm.nih.gov/9576389/) | 1998 | Cohort | Pediatric Infectious Disease Journal | Molecular epidemiology and infection-control strategies for SSSS in premature infants |
| [35358031](https://pubmed.ncbi.nlm.nih.gov/35358031/) | 2022 | Cohort | Journal of Medical Microbiology | Molecular epidemiology and antibiotic resistance of *S. aureus* (incl. SSSS-related) isolates in hospitalized children |
| [35901469](https://pubmed.ncbi.nlm.nih.gov/35901469/) | 2022 | Case Series | Advances in Neonatal Care | Case series on SSSS identification and wound care in neonates |

*Note:* Two publications specifically flag emerging **mupirocin-resistant** *S. aureus* clones associated with SSSS/skin infection outbreaks ([28592549](https://pubmed.ncbi.nlm.nih.gov/28592549/), [30418106](https://pubmed.ncbi.nlm.nih.gov/30418106/)) — relevant to antimicrobial stewardship if this indication is pursued further.

---

## South Africa Market Information

Mupirocin currently has **no SAHPRA registrations** and is **not marketed** in South Africa according to this evidence pack (0 licenses on file).

---

## Safety Considerations

**Key Warnings**: Not available — this is a **Blocking** data gap (TFDA/SAHPRA Professional Information has not been sourced), which prevents a formal S1 safety pre-assessment.

Please refer to the SAHPRA-approved Professional Information (PI) for safety information once available. Report adverse drug reactions to SAHPRA.

---

## Other Candidates Screened (Not Recommended)

The remaining 9 TxGNN-predicted indications in this evidence pack were also screened and are **not recommended to progress** — most have no clinical trial or literature evidence at all (L5, Hold), and several are explicitly flagged in their own rationale as mechanistically implausible (e.g., pleural empyema — topical mupirocin cannot reach therapeutic pleural concentrations; leukoplakia of vagina — non-infectious disease; "non-human animal disease" — a knowledge-graph labeling artifact, not a real indication). Two others (cutaneous candidiasis, bacterial vaginosis) reached only L4/S1 "Research Question" status due to single case reports with pathogen mismatches (antifungal vs. antibacterial; MRSA vaginitis vs. typical polymicrobial BV).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The SSSS candidate has a coherent mechanism and the best evidence in this pack (L3, cohort-level literature), but rests entirely on observational data with no dedicated RCT.
- Mupirocin is not currently registered or marketed in South Africa, and the safety/PI data gap is rated **Blocking** — a formal safety pre-assessment (S1) cannot be completed without it.

**To proceed, the following is needed:**
- SAHPRA/TFDA-sourced Professional Information (warnings, contraindications, DDI) to resolve the Blocking data gap
- Confirmed mechanism-of-action documentation from DrugBank
- A regulatory pathway assessment for an unmarketed drug (e.g., named-patient or compassionate-use access) if clinical use for SSSS is to be considered
- Ideally, a prospective or comparative study of topical mupirocin as SSSS adjunct therapy, given current evidence is limited to cohorts and case series
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

