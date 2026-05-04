---
layout: default
title: Cefazolin
parent: 僅模型預測 (L5)
nav_order: 101
evidence_level: L5
indication_count: 10
---

# Cefazolin
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

# Cefazolin: From Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Cefazolin is a first-generation cephalosporin antibiotic with well-established clinical use for surgical prophylaxis and the treatment of gram-positive bacterial infections.
The TxGNN model predicts it may be effective for **Infectious Otitis Media**, with **0 clinical trials** and **3 publications** currently supporting this specific direction.
At an evidence level of L4, the current recommendation is to **Hold** — however, a separate prediction for urinary tract infection (UTI, Rank 10) carries an L3 evidence base and warrants a **Proceed with Guardrails** decision, making it the highest-priority repurposing candidate in this pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections — surgical prophylaxis, skin and soft-tissue infections, UTI |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L4 (preclinical / mechanistic reasoning only; no clinical trials) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this Evidence Pack. Based on established pharmacology, Cefazolin is a first-generation cephalosporin that inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins (PBPs), disrupting peptidoglycan cross-linking and ultimately causing bactericidal cell lysis. Its activity profile is strongest against gram-positive organisms — particularly methicillin-sensitive *Staphylococcus aureus* (MSSA) and streptococcal species — and it provides modest coverage against a limited range of gram-negative organisms.

The mechanistic link to infectious otitis media is partial but not sufficient for clinical repurposing. The dominant bacterial pathogens in acute otitis media (AOM) are *Streptococcus pneumoniae* (~40%), *Haemophilus influenzae* (~25%), *Moraxella catarrhalis* (~12%), and *Streptococcus pyogenes* (~10–15%). Cefazolin covers *S. pneumoniae* and *S. pyogenes* well, but its activity against *H. influenzae* and *M. catarrhalis* is negligible — these two organisms together account for approximately 35–40% of AOM cases and represent a critical antimicrobial gap.

Beyond the spectrum gap, cefazolin's intravenous (IV) route of administration is a practical barrier: AOM is almost exclusively managed in outpatient or primary care settings where oral therapy is standard. Current AOM guidelines (AAP 2013) recommend high-dose amoxicillin or amoxicillin-clavulanate as first-line therapy precisely because of their broader oral coverage. The TxGNN model likely identified the shared gram-positive pathogen overlap between cefazolin's established uses and AOM pathogens, but this overlap is insufficient to support a repurposing recommendation without addressing the spectrum and route limitations.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cefazolin in infectious otitis media.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case Report | Annals of Otology, Rhinology & Laryngology | Ceftazidime + Cefazolin used as empiric combination therapy in a paediatric case of Gradenigo Syndrome (petrous apicitis, a rare complication of acute otitis media); highlights Cefazolin's role in covering gram-positive organisms in otological infection contexts |
| [877649](https://pubmed.ncbi.nlm.nih.gov/877649/) | 1977 | Narrative Review | Southern Medical Journal | Reviews cephalosporins in paediatric infections; notes potential utility of first-generation cephalosporins (including Cefazolin) in otitis media for patients with penicillin hypersensitivity, acknowledging the gram-positive coverage rationale |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Case Series | Clinical Pharmacy | Case of Stevens-Johnson syndrome in a child treated with multiple antibiotics for upper airway infection and otitis media; Cefazolin mentioned in the sequential antibiotic treatment context |

---

## South Africa Market Information

Cefazolin is currently **not registered with SAHPRA** and is **not marketed in South Africa**. There are no active product licences on record. Any clinical procurement or use would require a special access pathway (e.g., Section 21 Authorisation under the Medicines and Related Substances Act). This is a critical regulatory barrier that must be resolved before any repurposing initiative can advance.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> **Note for prescribers:** Cefazolin is a beta-lactam antibiotic. Clinicians should be aware of the potential for cross-hypersensitivity in patients with known penicillin allergy (estimated 1–2% cross-reactivity), and the risk of serious allergic reactions including anaphylaxis. No specific South African PI safety data was available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold** *(for infectious otitis media as the primary predicted indication)*

**Rationale:**
Despite a high TxGNN model score (99.44%), Cefazolin's antimicrobial spectrum does not adequately cover *H. influenzae* and *M. catarrhalis* — two pathogens responsible for approximately 35–40% of AOM cases — making it a suboptimal candidate for infectious otitis media treatment. Its IV-only formulation is impractical for the outpatient AOM setting, and current international guidelines already exclude it from AOM algorithms. The evidence base is limited to three peripheral literature references (evidence level L4), with no clinical trials.

**Broader landscape note:** Across all 10 TxGNN predictions in this Evidence Pack, the **Urinary Tract Infection (UTI)** indication (Rank 10, score 98.91%) is the most clinically mature, with 11 clinical trials (including directly Cefazolin-focused studies) and 20 publications — supporting an **L3 evidence level** and a **"Proceed with Guardrails"** recommendation. IDSA and EAU guidelines already recognise IV Cefazolin as a first-line or alternative agent for acute uncomplicated pyelonephritis caused by susceptible organisms. This indication should be prioritised for further evaluation.

**To proceed with any indication, the following is needed:**

- **SAHPRA registration or Section 21 authorisation:** Cefazolin's absence from the South African market must be addressed before any clinical repurposing programme can commence
- **Mechanism of action data:** Query DrugBank API (DB01327) to complete the MOA and pharmacokinetic profile
- **Safety data:** Download and parse the SAHPRA or originator Professional Information (PI) document to identify formal warnings, contraindications, and drug interactions
- **For UTI (recommended priority):** Conduct local antibiogram analysis of South African community-acquired UTI pathogens to establish current cefazolin susceptibility rates (ESBL-producing strains represent the primary resistance risk)
- **For otitis media (if continued):** Clarify whether a reformulated product (e.g., IM administration in hospitalised children) could address the route-of-administration barrier, and obtain South African paediatric AOM pathogen susceptibility data

---

*This report is generated from computational model predictions and available published evidence. Results are for research reference only and do not constitute medical advice. All repurposing candidates require clinical validation before application. Data cut-off: 5 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

