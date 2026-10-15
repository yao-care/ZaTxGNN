---
layout: default
title: Benzylpenicillin
parent: Model Prediction Only (L5)
nav_order: 65
evidence_level: L5
indication_count: 10
---

# Benzylpenicillin
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

# Benzylpenicillin: From Streptococcal and Other Bacterial Infections to Pericoronitis

## One-Sentence Summary

Benzylpenicillin (penicillin G) is an injectable antibiotic originally used for bacterial infections such as streptococcal infection, pneumococcal meningitis, meningococcal infection, anthrax and endocarditis.
The TxGNN model predicts it may be effective for **pericoronitis** (infection around a partially erupted tooth), but **no clinical trials and no publications** were found to support this prediction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Streptococcal infection, meningococcal infection, pneumococcal meningitis, anthrax, endocarditis and other bacterial infections (the SAHPRA registration records compiled for this report contain no indication text, so this list comes from the TxGNN knowledge graph) |
| Predicted New Indication | Pericoronitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, benzylpenicillin is a penicillin-class antibacterial. Its efficacy against streptococci and other susceptible organisms is established, and mechanistically it may be applicable to pericoronitis.

Pericoronitis is a mixed infection of streptococci and anaerobic bacteria around a partially erupted tooth. Benzylpenicillin is active against streptococci and many oral anaerobes, so the prediction is biologically plausible.

Penicillin-class drugs are already used for odontogenic infections. This prediction is therefore probably an extension of the existing antibacterial use rather than true repurposing. The high score (99.36%) is a model output and is not clinical evidence.

Other predictions in the top 10 are weaker. For example, gingival recession, canker sore, gingival leukoplakia and denture stomatitis (mainly Candida-related, where penicillin has no antifungal activity) have little or no mechanistic rationale. Cat-scratch disease (Bartonella) is not typically treated with penicillins.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for pericoronitis.

For the lower-ranked prediction of conjunctivitis, six publications were retrieved. None provides human efficacy data for benzylpenicillin in conjunctivitis. They cover allergy testing, congenital syphilis, microbial keratitis, staphylococcal susceptibility, an animal keratoconjunctivitis model and penicillin concentrations in bovine conjunctival fluid. They are not counted as support for the lead prediction.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A/20.1.2/626 | Benzyl Penicillin Fresenius 1Mu | Injection | Not recorded in the data compiled for this report |
| A/20.1.2/444 | Bio-Pen 1Mu | Injection | Not recorded in the data compiled for this report |

Both registrations are valid single-ingredient injectable products. Essential Medicines List (EML) inclusion status was not available in the data compiled for this report.

## Safety Considerations

- **Contraindication-related conditions (from a knowledge graph, not label text):** kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, infectious mononucleosis, chronic Epstein-Barr virus infection syndrome.
- **Drug Interactions:** 21 interactions were identified.
  - **Major:** methotrexate (penicillins can reduce methotrexate clearance and raise toxicity risk).
  - **Moderate:** tetracyclines (doxycycline, minocycline, tetracycline, demeclocycline, oxytetracycline), chloramphenicol, warfarin, dicoumarol, ethinylestradiol, mycophenolic acid, picosulfuric acid, iodide I-123 and I-131.
  - **Minor:** clarithromycin, erythromycin.
  - **Unknown severity:** salbutamol, acyclovir, gentamicin, levothyroxine.

Label-based warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible, because benzylpenicillin acts on streptococci and oral anaerobes. However, no trials or literature support it, the evidence level is L5, and it is likely an extension of existing antibacterial use rather than a new indication. Label safety data are also missing.

**To proceed, the following is needed:**
- Download and review the SAHPRA package insert (warnings, contraindications and approved indications). This is a blocking data gap for safety screening.
- Obtain detailed mechanism of action data (for example from DrugBank).
- Review guidelines and literature on penicillin use in odontogenic infections and pericoronitis. Clarify whether oral or parenteral penicillins already cover this use.
- Confirm the EML status and the approved indication wording of the two registered products.
- Compare with standard options in South African practice, and define the route and setting (parenteral benzylpenicillin versus oral agents).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

