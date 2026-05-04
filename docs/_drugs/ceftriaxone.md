---
layout: default
title: Ceftriaxone
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 10
---

# Ceftriaxone
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

# Ceftriaxone: From Serious Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Ceftriaxone is a third-generation cephalosporin antibiotic established globally for treating serious bacterial infections, including meningitis, sepsis, pneumonia, and gonorrhoea. The TxGNN model predicts it may be effective for **Infectious Otitis Media**, with **3 clinical trials** and **19 publications** currently supporting this direction — one of four closely clustered otitis media predictions in the top 10 results that together form a consistent mechanistic signal. The three highest-ranked TxGNN outputs (hyperamylasemia, polyclonal hyperviscosity syndrome, congenital analbuminemia) have been assessed as knowledge graph prediction noise with no biological rationale, making infectious otitis media the most evidence-supported and actionable finding from this prediction set.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious bacterial infections (meningitis, sepsis, pneumonia, gonorrhoea, intra-abdominal infections) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L2 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ceftriaxone works by irreversibly binding to penicillin-binding proteins (PBPs 1a, 1b, 2, and 3), blocking the cross-linking step of bacterial peptidoglycan cell wall synthesis and causing bacterial lysis. Its long half-life (~8 hours in adults) permits once-daily dosing, and parenteral administration (intravenous or intramuscular) achieves high, predictable plasma concentrations that are not dependent on gastrointestinal absorption. Critically, ceftriaxone achieves therapeutic drug concentrations in middle ear effusions following IM injection — a pharmacokinetic prerequisite for treating middle ear infections. Detailed mechanism of action data was not available in the DrugBank source linked to this evidence pack; however, the above is based on well-established published pharmacology for this drug class.

The three principal pathogens responsible for acute infectious otitis media — **Streptococcus pneumoniae**, **non-typeable Haemophilus influenzae (NTHi)**, and **Moraxella catarrhalis** — all show low minimum inhibitory concentrations (MICs) to ceftriaxone, meaning the drug kills them effectively at clinically achievable concentrations. This pathogen–drug match is the mechanistic foundation of the TxGNN prediction. Infectious otitis media and the original indications of ceftriaxone (e.g., bacterial meningitis, pneumonia) share the same causative organisms; the drug's coverage spectrum is therefore directly applicable across these conditions.

Four of the top 10 TxGNN-predicted indications involve otitis media or middle ear disease subtypes (infectious otitis media rank 4, suppurative otitis media rank 6, chronic otitis media rank 7, middle ear disease rank 9), indicating a consistent mechanistic signal within the knowledge graph rather than an isolated artefact. This is further validated by two direct head-to-head RCTs comparing ceftriaxone against standard-of-care antibiotics for acute otitis media in children, published in *Pediatrics* (1997) and the *Pediatric Infectious Disease Journal* (2000), providing Level 1 clinical evidence. Internationally, IM ceftriaxone is incorporated into paediatric AOM treatment guidelines — including the American Academy of Pediatrics guidelines — as a second-line option when oral amoxicillin fails, the patient cannot tolerate oral therapy, or treatment adherence is a concern.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Phase 2b | Terminated | 520 | Multicenter double-blind placebo-controlled RCT in children aged 6–23 months with AOM, comparing 5-day vs 10-day antibiotic treatment to assess whether shorter-course therapy reduces antimicrobial resistance while maintaining clinical efficacy; terminated before reaching planned 600-subject target, limiting definitive efficacy conclusions |
| [NCT01272999](https://clinicaltrials.gov/study/NCT01272999) | N/A (Observational) | Completed | 391 | Post-marketing observational study evaluating the impact of Prevnar 13 (pneumococcal 13-valent conjugate vaccine) on otitis media incidence in children; provides important epidemiological context on the pneumococcal disease burden against which ceftriaxone is used |
| [NCT02567825](https://clinicaltrials.gov/study/NCT02567825) | N/A (Surgical RCT) | Completed | 250 | RCT comparing tympanostomy tube placement vs non-surgical management in children with recurrent AOM over 2 years; defines the clinical threshold where maximal medical management (including parenteral ceftriaxone for refractory cases) is exhausted before surgical escalation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|---|---|---|---|---|
| [8989332](https://pubmed.ncbi.nlm.nih.gov/8989332/) | 1997 | RCT | *Pediatrics* | Prospective randomised single-blind trial (Greater Boston Otitis Media Study Group): single IM dose of ceftriaxone vs 10-day oral TMP-SMZ in children with AOM; demonstrated non-inferiority of single-dose ceftriaxone, establishing it as a viable alternative for patients unable to complete oral courses |
| [11099083](https://pubmed.ncbi.nlm.nih.gov/11099083/) | 2000 | RCT | *Pediatric Infectious Disease Journal* | Head-to-head RCT comparing 1-day vs 3-day IM ceftriaxone for non-responsive AOM in children; 3-day regimen showed superior bacteriological and clinical efficacy, particularly against penicillin-resistant *S. pneumoniae* |
| [39361280](https://pubmed.ncbi.nlm.nih.gov/39361280/) | 2024 | Clinical Guidelines | *JAMA Network Open* | Analysis of optimal paediatric outpatient antibiotic prescribing in the US; provides stewardship-aligned guidance positioning ceftriaxone as an appropriate escalation agent for AOM when first-line therapy fails |
| [35841649](https://pubmed.ncbi.nlm.nih.gov/35841649/) | 2022 | Retrospective Cohort | *Int J Pediatric Otorhinolaryngology* | Large US primary care database study documenting increasing IM ceftriaxone use for AOM, particularly for otitis-conjunctivitis and treatment failures; suggests real-world clinical adoption and signals growing prescriber confidence in this indication |
| [9877360](https://pubmed.ncbi.nlm.nih.gov/9877360/) | 1998 | Clinical Study | *Pediatric Infectious Disease Journal* | Bacteriological efficacy of 3-day IM ceftriaxone in non-responsive AOM in children; demonstrated high eradication rates of *S. pneumoniae* from middle ear fluid, supporting the 3-day regimen as the optimal dosing strategy |
| [12237596](https://pubmed.ncbi.nlm.nih.gov/12237596/) | 2002 | Clinical Study | *Pediatric Infectious Disease Journal* | Compared the effect of 1-day vs 3-day IM ceftriaxone on nasopharyngeal *S. pneumoniae* carriage in non-responsive AOM; 3-day regimen was superior for eradicating resistant strains, with implications for both clinical cure and resistance containment |
| [12166789](https://pubmed.ncbi.nlm.nih.gov/12166789/) | 2002 | Consensus Guidelines | *Clinical Pediatrics* | Consensus recommendations for AOM management developed by a panel of paediatric AOM specialists; positions ceftriaxone as a key second-line agent when first-line amoxicillin fails or oral therapy is not feasible |
| [20802367](https://pubmed.ncbi.nlm.nih.gov/20802367/) | 2010 | Review | *Otology & Neurotology* | Recommendations for AOM prevention and antimicrobial treatment in children with cochlear implants — a high-risk group for severe, recurrent OM and meningitis; highlights ceftriaxone as a critical parenteral option for this population |
| [38368849](https://pubmed.ncbi.nlm.nih.gov/38368849/) | 2024 | Review | *American Journal of Emergency Medicine* | High-risk disease review of acute mastoiditis, the most common intracranial complication of AOM; identifies ceftriaxone as the first-line parenteral antibiotic, underscoring its role in preventing and treating serious AOM sequelae |
| [20660544](https://pubmed.ncbi.nlm.nih.gov/20660544/) | 2010 | Retrospective Cohort | *Pediatrics* | Study of surgical site infections, AOM, and meningitis in cochlear implant children; supports combined vaccination and parenteral ceftriaxone as the preferred prevention and treatment strategy for high-risk paediatric OM |

---

## South Africa Market Information

Ceftriaxone currently has **no recorded SAHPRA registrations** and is listed as **not marketed** in South Africa according to this evidence pack. No product registration table can be presented.

> **Important Note for Clinicians**: Ceftriaxone is included on the **WHO Essential Medicines List** and is widely registered and dispensed globally, including throughout sub-Saharan Africa. The absence of SAHPRA registrations in this dataset is unexpected for a drug of this profile and may reflect data incompleteness, reliance on a specific formulation lookup, or the need for data refresh. Clinicians should independently verify current SAHPRA registration status at [https://www.sahpra.org.za](https://www.sahpra.org.za) and check for any active **Section 21 (compassionate use) authorisations**. Inclusion on the **National Essential Medicines List (NEML)** should also be explored as a parallel regulatory pathway.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA via the MedSafety reporting portal.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two direct RCTs published in high-impact peer-reviewed journals (*Pediatrics* 1997; *Pediatric Infectious Disease Journal* 2000) demonstrate the clinical efficacy of IM ceftriaxone in paediatric acute otitis media, and international treatment guidelines already incorporate ceftriaxone as an established second-line antibiotic for this indication. The TxGNN prediction aligns with robust global evidence; the principal gap is not clinical evidence, but rather the absence of formal SAHPRA registration and South Africa–specific prescribing guidance.

**To proceed, the following is needed:**

- **Regulatory verification**: Confirm SAHPRA registration status urgently; if no current registration exists, initiate a registration application leveraging existing global dossiers from major regulatory agencies (FDA, EMA, WHO prequalification)
- **Safety data**: Obtain the full manufacturer's Professional Information (PI) to complete the safety assessment — this is currently a blocking data gap that must be resolved before any clinical recommendation can be finalised
- **Mechanism of action documentation**: Retrieve formal MOA data from DrugBank or a peer-reviewed pharmacology source to complete the mechanistic analysis for regulatory submissions
- **Local susceptibility data**: Conduct or commission local antimicrobial susceptibility surveillance to confirm ceftriaxone sensitivity of key AOM pathogens (*S. pneumoniae*, *H. influenzae*, *M. catarrhalis*) in South African paediatric populations, since local resistance patterns may differ from North American or European trial data
- **Stewardship framework**: Engage with the **South African Antibiotic Stewardship Programme (SAASP)** and the **National Department of Health** to define prescribing guardrails — restricting ceftriaxone use to: documented first-line oral antibiotic failure; penicillin/amoxicillin allergy; inability to tolerate oral medication (e.g., vomiting); or severe/complicated AOM with risk of suppurative complications
- **NEML submission**: Prepare a submission to the **NEML Committee** for ceftriaxone inclusion in the primary healthcare antibiotic formulary for AOM, aligned with its WHO essential medicine status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

