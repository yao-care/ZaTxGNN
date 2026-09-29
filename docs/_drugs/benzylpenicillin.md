---
layout: default
title: Benzylpenicillin
parent: Model Prediction Only (L5)
nav_order: 64
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

# Benzylpenicillin: From Bacterial Infection to Pericoronitis

## One-Sentence Summary

Benzylpenicillin is an injectable penicillin antibacterial, marketed in South Africa under 2 SAHPRA registrations.
The TxGNN model predicts it may be effective for **pericoronitis** (score 99.36%), but this is a model prediction only, with **0 clinical trials** and **0 publications** for this pairing.
Among the other predicted indications, **recurrent aphthous stomatitis (canker sore)** has the strongest support, including a 2020 randomized controlled trial of topical penicillin.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied SAHPRA registration data (injectable antibacterial) |
| Predicted New Indication | Pericoronitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, benzylpenicillin is a penicillin-class antibacterial. Its efficacy in bacterial infections is established, and mechanistically it may be applicable to pericoronitis.

Pericoronitis is a polymicrobial infection of the gum around a partly erupted tooth, so an antibacterial is biologically plausible. Two factors weigh against it. Benzylpenicillin is given by injection and has a short half-life, which is a poor fit for a mostly local dental condition. No trials or literature support this specific drug-disease pairing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered. No SANCTR or PACTR identifiers were found.

---

## Literature Evidence

Currently no related literature available.

---

## Other Predicted Indications Worth Noting

The first-ranked prediction has no evidence. The table below shows the other predictions in the pack that have the most relevant evidence.

| Predicted Indication | TxGNN Score | Evidence Level | Decision Stage / Recommendation | Evidence Summary |
|------|------|------|------|------|
| Canker sore (recurrent aphthous stomatitis) | 99.27% | L2 | S2 / Research Question | A randomized double-blind trial of topical penicillin ([PMID 33273940](https://pubmed.ncbi.nlm.nih.gov/33273940/), 2020) and two penicillin G potassium troche studies ([14676759](https://pubmed.ncbi.nlm.nih.gov/14676759/), 2003; [20188604](https://pubmed.ncbi.nlm.nih.gov/20188604/), 2010). Effect sizes were not visible in the input and need verification. The only registered trial (NCT02750800) is an adalimumab study and is irrelevant. |
| Ulcerative stomatitis | 99.26% | L4 | S1 / Hold | Only uncontrolled 1940s clinical reports and narrative reviews. No modern controlled evidence. |
| Conjunctivitis | 97.94% | L4 | S0 / Hold | General reviews and resistance literature only. No controlled benzylpenicillin study. |
| Chronic ethmoidal sinusitis | 97.63% | L4 | S0 / Hold | Studies concern other agents (amoxicillin-clavulanate, ciprofloxacin). Indirect at best. |
| Gingival recession | 99.31% | L4 | S0 / Hold | Studies test amoxicillin/metronidazole in periodontitis, not benzylpenicillin. Recession is an outcome measure, not an infection. |
| Denture stomatitis | 99.26% | L4 | S0 / Hold | Mainly Candida-associated, and penicillin has no antifungal activity. Only preclinical and indirect records. |
| Chemotherapy-induced oral mucositis, gingival leukoplakia, cat-scratch disease | 97.78–99.26% | L5 | S0 / Hold | Prediction only. No trials or literature, and no plausible mechanistic link. |

Note that the canker sore studies use **topical** penicillin G. This differs from the injectable products registered in South Africa.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. A/20.1.2/626 | Benzyl Penicillin Fresenius 1Mu | Injection | Not stated in supplied record |
| Reg. No. A/20.1.2/444 | Bio-Pen 1Mu | Injection | Not stated in supplied record |

Both registrations are injectable only. No topical or oral benzylpenicillin product appears in the supplied data. Essential Medicines List (EML) status was not included in the supplied data.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pericoronitis prediction rests on the model score alone, and no trials or literature support it. The injectable-only South African registrations also limit how well this drug fits a dental indication.

**To proceed, the following is needed:**
- SAHPRA Professional Information (PI) for both registrations, to confirm approved indications, warnings and contraindications (this is a blocking gap for safety screening)
- Mechanism of action data (e.g. from DrugBank)
- Full-text review of the three topical penicillin G studies in recurrent aphthous stomatitis to verify outcomes. If they hold up, this is a better research question than pericoronitis.
- For any topical-use idea, a check on whether a suitable topical formulation exists in South Africa, since current registrations are injectable only
- Comparison against current guidelines for oral infections, where other agents are often preferred

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

