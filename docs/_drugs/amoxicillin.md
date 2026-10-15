---
layout: default
title: Amoxicillin
parent: Model Prediction Only (L5)
nav_order: 35
evidence_level: L5
indication_count: 10
---

# Amoxicillin
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

# Amoxicillin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Amoxicillin is a beta-lactam antibiotic, originally used to treat bacterial infections such as urinary tract infection, otitis media, streptococcal infection and bacterial pneumonia.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but **no clinical trials and no publications** currently support this prediction.
The score comes from a graph-based computation only, so this prediction should be treated as a hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, infectious otitis media, streptococcal infection, bacterial pneumonia (SAHPRA indication text not available; taken from the TxGNN knowledge graph) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 14 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Amoxicillin is a beta-lactam antibiotic with established efficacy in many bacterial infections.

Polyclonal hyperviscosity syndrome is caused by raised polyclonal immunoglobulin levels that thicken the blood. It is not a bacterial infection. No plausible mechanistic link between an antibacterial and this condition was identified. The high score (0.996) reflects network-based association only and should not be read as biological support.

**Other predictions reviewed** (all with the same Hold or Research Question status):
- **Epiglottitis** (score 98.70%, L4): the most plausible by mechanism. It is mainly caused by *Haemophilus influenzae* and streptococci, which amoxicillin already covers in related upper respiratory tract infections, so it is closer to a label extension than true repurposing. Evidence is limited to reviews, guidelines, epidemiology and case reports. Beta-lactamase production in *H. influenzae* limits use, and empirical therapy usually relies on third-generation cephalosporins.
- **Septicaemic plague** (score 99.13%, L4): there is a biological rationale, but evidence is limited to a mouse model and in vitro studies. Beta-lactams are not first-line for plague, and no human trials exist.
- **Other candidates** (hyperamylasaemia, congenital analbuminaemia, premalignant haematological disease, monoclonal gammopathy, congenital haematological disorder and others): no therapeutic mechanism or direct evidence was found. For congenital haematological disorder, the only relevant literature is an adverse-event report of amoxicillin-induced haemolytic anaemia, which is a safety signal.

## Clinical Trial Evidence

Currently no related clinical trials registered for polyclonal hyperviscosity syndrome.

## Literature Evidence

Currently no related literature available for polyclonal hyperviscosity syndrome.

## South Africa Market Information

Amoxicillin is marketed in South Africa with 14 valid single-ingredient registrations, in oral, injectable and other forms. Approved indication text and manufacturer details were not available in the data compiled for this report. Essential Medicines List (EML) status could not be confirmed from the available data.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 36/20.1.2/0115 | Zaloxy | Suspension | Not available |
| Reg. No. Z/20.1.2/327 | Spectramox C 250 | Capsule | Not available |
| Reg. No. J/20.1.2/0437 | Suprapen 500 | Capsule | Not available |
| Reg. No. 41/20.1.2/0532 | Bindoclav | Tablet | Not available |
| Reg. No. 34/20.1.2/0251 | Ranclav | Suspension | Not available |

Nine further registrations exist, including Austell-co-amoxiclav, Auro-amoxiclav (tablet and suspension), Apoclav (injection), Amoxil D (drops) and others.

## Safety Considerations

SAHPRA package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Contraindication-related conditions in the knowledge graph** (not label text): liver disease and liver failure, cholestasis, kidney disease, porphyria, Clostridium difficile colitis, myasthenia gravis, infectious mononucleosis (including chronic Epstein-Barr virus infection syndrome), long QT syndrome, torsades de pointes, ventricular tachycardia, osteoporosis and bone fracture, and gallbladder disease. These should be verified against the PI.

**Drug Interactions** (100 interactions recorded; selected examples):
- **Major**: methotrexate (reduced renal clearance, raising methotrexate toxicity risk), and live oral cholera vaccine (*Vibrio cholerae* CVD 103-HgR).
- **Moderate**: doxycycline, minocycline, demeclocycline, ethinylestradiol, estradiol, dicoumarol, anisindione, mycophenolate mofetil, entecavir, balsalazide, and probiotic preparations (*Lactobacillus acidophilus*, *Bifidobacterium longum infantis*).
- **Minor**: allopurinol, amiloride, azithromycin, clarithromycin, erythromycin.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for polyclonal hyperviscosity syndrome rests on a graph-based score alone (L5). There is no clinical, preclinical or mechanistic support, and no plausible mechanism linking an antibacterial to this condition. Safety data from the SAHPRA PI are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Retrieval and review of the SAHPRA package insert (warnings, contraindications, approved indications)
- Mechanism of action data (for example from DrugBank)
- Any mechanistic or preclinical rationale for an effect on polyclonal hyperviscosity
- If the team wishes to pursue a more credible direction, a focused review of epiglottitis (label extension within the infection class) or septicaemic plague (research question, requiring clinical data beyond animal and in vitro studies)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

