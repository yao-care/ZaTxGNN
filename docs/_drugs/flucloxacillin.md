---
layout: default
title: Flucloxacillin
parent: Moderate Evidence (L3-L4)
nav_order: 234
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Flucloxacillin: predicted new indication Conjunctivitis (evidence level L4). Approved use: Not stated in the SAHPRA registration data compiled for this report (…"
monitor_inn: "Flucloxacillin"
predicted_indications: ["conjunctivitis", "rheumatoid arthritis", "leprosy", "Prinzmetal angina", "conjunctivitis (disease)", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "thrombotic disease", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis"]
---

# Flucloxacillin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Flucloxacillin: From Bacterial Infections to Conjunctivitis

## One-Sentence Summary

Flucloxacillin is an anti-staphylococcal penicillin antibiotic that is marketed in South Africa under six SAHPRA registrations.
The TxGNN model predicts it may be effective for **conjunctivitis**,
but there are currently **no registered clinical trials** and only **1 publication** (a case report on a different pathogen), so this remains a model prediction with very limited support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data compiled for this report (flucloxacillin is generally used for staphylococcal infections) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, flucloxacillin is a penicillinase-resistant penicillin (a beta-lactam), and it is used against infections caused by Gram-positive bacteria such as *Staphylococcus aureus*. Mechanistically, it may be applicable to bacterial conjunctivitis caused by susceptible organisms.

However, the support is weak. The only paper retrieved is a case report on gonococcal dacryoadenitis. That involves a different pathogen (*Neisseria gonorrhoeae*) and a different site (the lacrimal gland), so it gives no direct evidence for flucloxacillin in conjunctivitis. The high TxGNN score is a prediction only. The model also returned a duplicate "conjunctivitis (disease)" entry (score 99.69%) with the same single reference; the two entries should be consolidated.

Other top-ranked predictions have no plausible mechanistic link or no supporting evidence:
- **Rheumatoid arthritis (99.83%)**: the literature shows flucloxacillin used for joint infections in RA patients, a methotrexate interaction study (no clinically significant interaction), and adverse event reports. None shows efficacy against RA itself.
- **Leprosy, Prinzmetal angina, brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome, antithrombin deficiency type 2, factor 5 excess with spontaneous thrombosis**: prediction only, with no trials or literature.
- **Thrombotic disease (99.66%)**: the papers retrieved concern *S. aureus* infections and an adverse event with a different drug, and are not repurposing evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41884366](https://pubmed.ncbi.nlm.nih.gov/41884366/) | 2026 | Case report | Case Reports in Ophthalmology | Gonococcal dacryoadenitis, a rare lacrimal gland complication of hyperacute bacterial conjunctivitis caused by *N. gonorrhoeae*. Does not involve flucloxacillin |

For context, the literature on the second-ranked prediction (rheumatoid arthritis) is limited to safety and pharmacology findings:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8866922](https://pubmed.ncbi.nlm.nih.gov/8866922/) | 1996 | Clinical pharmacology study | Br J Clin Pharmacol | No clinically significant pharmacokinetic interaction between flucloxacillin and methotrexate in 10 RA patients |
| [8610477](https://pubmed.ncbi.nlm.nih.gov/8610477/) | 1995 | Case report (adverse event) | Acta Haematol | Agranulocytosis in an RA patient on long-term flucloxacillin, with relapse on re-challenge |
| [40755703](https://pubmed.ncbi.nlm.nih.gov/40755703/) | 2025 | Case report (adverse event) | Cureus | Fatal SJS/TEN linked to doxycycline or flucloxacillin in a 77-year-old woman |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A50/2.6.5/0687 | Septapen | Tablet | Not listed in the data compiled |
| 44/20.1.2/0816 | Flucloxacillin 250 oethmaan | Capsule | Not listed in the data compiled |
| J/20.1.2/0437 | Suprapen 500 | Capsule | Not listed in the data compiled |
| Z/20.1.2/0354 | Megapen S | Suspension | Not listed in the data compiled |
| 27/20.1.2/0106 | Macropen | Capsule | Not listed in the data compiled |

A sixth registration, 27/20.1.2/0107 (Macropen s, suspension), is also valid. All six registrations are single-ingredient products. Essential Medicines List status was not available in the data compiled for this report.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Published case reports found while searching for repurposing evidence describe serious adverse reactions, including agranulocytosis with long-term use and severe cutaneous reactions (SJS/TEN). These are individual reports and do not replace the PI.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted conjunctivitis indication rests on a model score alone. There are no registered trials, and the single publication concerns a different pathogen and site. The package insert safety data are also missing, so safety screening cannot yet proceed.

**To proceed, the following is needed:**
- SAHPRA package insert (warnings, contraindications and approved indications), obtained and reviewed
- Mechanism of action data for flucloxacillin
- Evidence specific to flucloxacillin in bacterial conjunctivitis, such as susceptibility data for common ocular pathogens and any trials
- Assessment of route suitability, since the registered products are oral (tablet, capsule, suspension) and the predicted indication would typically require topical ocular delivery
- Consolidation of the duplicate conjunctivitis entries in the prediction list
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

