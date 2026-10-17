---
layout: default
title: Cefazolin
parent: Model Prediction Only (L5)
nav_order: 103
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cefazolin: predicted new indication Infectious otitis media (evidence level L5). Approved use: Bacterial infections, including bacterial pneumonia, endocarditis…"
monitor_inn: "Cefazolin"
predicted_indications: ["infectious otitis media", "bronchitis", "middle ear disease", "chronic otitis media", "suppurative otitis media", "otosalpingitis", "non-suppurative otitis media", "allergic otitis media", "middle ear cholesterol granuloma", "urinary tract infection (disease)"]
---

# Cefazolin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Cefazolin: From Bacterial Infections (Pneumonia, Endocarditis, Bacterial Arthritis) to Infectious Otitis Media

## One-Sentence Summary

Cefazolin is a first-generation cephalosporin antibiotic, originally used for bacterial infections such as staphylococcal and streptococcal pneumonia, endocarditis, bacterial arthritis and cholangitis.
The TxGNN model predicts it may be effective for **infectious otitis media**,
but there are currently **no registered clinical trials** and only **2 publications** (a review and a case report), so the prediction rests mainly on the model and on antibacterial spectrum.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections, including bacterial pneumonia, endocarditis, bacterial arthritis and cholangitis (from the knowledge graph; the SAHPRA registration entry carries no indication text) |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L4 (no clinical trials; only a review and a case report, which are indirect) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, cefazolin is a first-generation cephalosporin that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins. It is active against gram-positive cocci such as streptococci and methicillin-susceptible *Staphylococcus aureus* (MSSA), which are plausible otitis media pathogens.

Cefazolin's existing indications (pneumococcal and staphylococcal pneumonia, endocarditis, bacterial arthritis) involve the same organisms, so extension to bacterial otitis media is a class-level extrapolation. The fit has important limits: cefazolin has poor activity against *Haemophilus influenzae* and *Moraxella catarrhalis*, which are common otitis media pathogens, and it exists only as an injectable, which is a poor match for a condition usually treated with oral agents. The high TxGNN score therefore likely reflects network proximity to existing antibacterial indications rather than a validated clinical signal.

Other top-ranked predictions in the data (bronchitis, middle ear disease, chronic and suppurative otitis media, and urinary tract infection) follow the same pattern. Suppurative otitis media is the only one that has a direct comparative study including cefazolin. Predictions such as allergic otitis media, non-suppurative otitis media and middle ear cholesterol granuloma have little mechanistic basis for an antibacterial agent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for infectious otitis media.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case report/series | Ann Otol Rhinol Laryngol | Ceftazidime-cefazolin empiric therapy for paediatric Gradenigo syndrome, a rare complication of acute otitis media; case-level evidence only |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Review | Clin Pharm | Management of Stevens-Johnson syndrome; otitis media appears only as the setting of the index patient, so relevance to cefazolin efficacy is minimal |

For related otitis media predictions, a 1982 Japanese comparative study ([PMID 6752467](https://pubmed.ncbi.nlm.nih.gov/6752467/)) compared cefmetazole with cefazolin in 172 evaluable patients with suppurative otitis media. Cefazolin served as the comparator, and the study is old, so it provides only a hypothesis-generating signal.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 36/20.1.1/0259 | Sabax cefazolin powder for injection | Injection | Not recorded in the data compiled for this report |

The only available route is injectable. Essential Medicines List (EML) status was not available in the data compiled for this report.

---

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: blood coagulation disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, congenital prothrombin deficiency.
- **Drug Interactions**: 100 interactions were identified. Moderate-level interactions were with the aminoglycosides kanamycin, neomycin and streptomycin, and with picosulfuric acid. Other listed interactions (e.g. calcitriol, epinephrine, amphotericin B, mannitol, acetylsalicylic acid, amoxicillin, metformin, omeprazole) have an unknown severity level.

Label warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there are no registered trials and no direct clinical evidence for cefazolin in otitis media. Its spectrum misses key otitis media pathogens (*H. influenzae*, *M. catarrhalis*), and it is injectable-only, whereas established oral first-line options exist.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Local susceptibility data (South African otitis media pathogens against cefazolin)
- Clinical evidence in human otitis media, ideally comparative data against standard-of-care agents
- Consideration of whether suppurative otitis media (the only prediction with a direct comparative study including cefazolin) or UTI (where cefazolin susceptibility is a recognised surrogate marker) is a better-supported research question than infectious otitis media
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

