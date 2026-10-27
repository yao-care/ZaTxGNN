---
layout: default
title: Diclofenac
parent: Model Prediction Only (L5)
nav_order: 175
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Diclofenac: predicted new indication Juvenile idiopathic arthritis (evidence level L5). Approved use: Arthritis (rheumatoid arthritis, osteoarthritis…"
monitor_inn: "Diclofenac"
predicted_indications: ["hypotrichosis simplex of the scalp", "acromesomelic dysplasia, Hunter-Thompson type", "pseudoachondroplasia", "brachyolmia", "brachyolmia-amelogenesis imperfecta syndrome", "congenital hypotrichosis milia", "myosclerosis", "diffuse alopecia areata", "juvenile idiopathic arthritis", "WHIM syndrome"]
---

# Diclofenac
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

## Diclofenac: From Osteoarthritis and Rheumatoid Arthritis to Juvenile Idiopathic Arthritis
{: .text-alpha }

## One-Sentence Summary

Diclofenac is a non-steroidal anti-inflammatory drug (NSAID) originally used for arthritic conditions (rheumatoid arthritis, osteoarthritis, ankylosing spondylitis) and for actinic keratosis when applied topically.
The TxGNN model's top-ranked predictions are mostly rare genetic disorders with no supporting evidence. The only prediction with a credible evidence base is **juvenile idiopathic arthritis (JIA)**, supported by **0 clinical trials** and **14 publications** (mostly older, small or indirect studies).
This report focuses on JIA, the most plausible candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Arthritis (rheumatoid arthritis, osteoarthritis, ankylosing spondylitis) and actinic keratosis (from the knowledge graph; the registration records compiled for this report contain no approved indication text) |
| Predicted New Indication | Juvenile idiopathic arthritis (rank 9 of the top 10 predictions; the top-ranked prediction, hypotrichosis simplex of the scalp, has no evidence and no mechanistic link) |
| TxGNN Prediction Score | 99.25% (JIA); 99.69% for the top-ranked prediction |
| Evidence Level | L3 (JIA); L5 for the other nine predictions |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 14 |
| Recommended Decision | Hold overall; JIA is flagged as a research question (Proceed with Guardrails only if the data needs below are met) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, diclofenac is a COX-1/COX-2 inhibitor. It reduces prostaglandin-mediated inflammation, pain and swelling, which is the same basis for its use in rheumatoid arthritis and osteoarthritis.

JIA is an inflammatory arthritis of childhood, and NSAIDs are an established symptomatic therapy for it. The mechanistic fit is therefore strong. Importantly, the benefit is symptomatic rather than disease-modifying, and the long-term safety of NSAIDs in children (gastrointestinal, renal, hepatic) needs consideration.

The other nine top predictions (for example hypotrichosis simplex, pseudoachondroplasia, brachyolmia, WHIM syndrome, alopecia areata) are monogenic or autoimmune conditions in which COX inhibition has no plausible disease-modifying role. Their high scores reflect graph-based patterns only and should not be acted on.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Selected publications on JIA (priority given to diclofenac-specific clinical studies):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3052965](https://pubmed.ncbi.nlm.nih.gov/3052965/) | 1988 | Crossover study | Clin Exp Rheumatol | Single-blind 12-week comparison of naproxen, tolmetin and diclofenac (2 mg/kg/day) in 28 children with seronegative juvenile chronic arthritis |
| [6361986](https://pubmed.ncbi.nlm.nih.gov/6361986/) | 1983 | Clinical study | Scand J Rheumatol | Diclofenac sodium in juvenile rheumatoid arthritis, including pharmacokinetics in children aged 2-7 |
| [2235663](https://pubmed.ncbi.nlm.nih.gov/2235663/) | 1990 | Open-label study | Pediatr Med Chir | Open non-comparative study of diclofenac in 26 patients (aged 2-16) with polyarticular juvenile chronic arthritis |
| [10756785](https://pubmed.ncbi.nlm.nih.gov/10756785/) | 1997 | Comparative study | Rev Med Chir Soc Med Nat Iasi | 100 children with juvenile chronic arthritis given diclofenac, paduden or aspirin; long-term clinical and laboratory follow-up |
| [8422565](https://pubmed.ncbi.nlm.nih.gov/8422565/) | 1993 | Review | Br J Rheumatol | Diclofenac, ibuprofen, tolmetin and naproxen are reported as equal in efficacy and tolerance for joint symptoms in children; salicylates and indomethacin are no more effective but more toxic |
| [11735667](https://pubmed.ncbi.nlm.nih.gov/11735667/) | 2001 | Review | Paediatr Drugs | Risks and benefits of NSAIDs in children compared with paracetamol |
| [1884567](https://pubmed.ncbi.nlm.nih.gov/1884567/) | 1991 | Review | Clin Pharmacokinet | Pharmacokinetics of drugs used in juvenile arthritis |
| [17474954](https://pubmed.ncbi.nlm.nih.gov/17474954/) | 2007 | Survey | Paediatr Anaesth | Diclofenac is licensed (in the UK) for children over 1 year for juvenile rheumatoid arthritis; paediatric PK/PD data in infants are lacking |

The evidence is old, small-scale and largely uncontrolled. The remaining retrieved papers are indirect (for example reviews on nabumetone or naproxen, or a case series on JIA presenting with alveolar hemorrhage).

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A39/3.1/0588 | Cataflam | Sachet | Not available in the compiled data |
| 32/3.1/0353 | Arthrotec | Tablet | Not available in the compiled data |
| 42/3.1/0831 | Voltaren Acti-Go soft gel capsules | Capsule | Not available in the compiled data |
| U/3.1/77 | Voltaren Emulgel | Gel (topical) | Not available in the compiled data |
| 31/3.1/0334 | Diclofenac injection Unimed 3 ml | Injection | Not available in the compiled data |

All 14 registrations are valid single-ingredient licences (none cancelled), across oral, injectable, suppository, sachet and topical forms. Several other products are also registered (K-Fenak OTC, Panamor, Adco-Diclofenac, Arthrotec 50). Some entries in the register (for example Sandoz Lamotrigine 25 and Ibugesic Plus) look like mismatches and should be verified against the SAHPRA register. Essential Medicines List status could not be determined from the data compiled.

---

## Safety Considerations

**Contraindications / conditions of concern (from the knowledge graph, not label text):** hypertension, liver disease and liver failure, drug-induced liver injury, congestive heart failure, cardiovascular disease, myocardial infarction, stroke and cerebrovascular disorders, active peptic ulcer disease, inflammatory bowel disease, asthma, diabetes mellitus and diabetic ketoacidosis, blood coagulation disorders, anaemia, hemoglobinopathy, gallbladder disease, substance abuse/dependence and keratitis.

**Drug Interactions** (100 interactions recorded; examples):
- **Moderate:** acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), metformin, sulfonylureas (glimepiride, glipizide, chlorpropamide, acetohexamide), aprepitant, mesalazine, balsalazide, exenatide, fenfluramine.
- **Minor:** famotidine, ranitidine, cimetidine.

Please refer to the SAHPRA-approved Professional Information (PI) for formal warnings and contraindications, which were not available in the data compiled. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold** (the JIA prediction is a research question rather than a new repurposing opportunity)

**Rationale:**
- Nine of the ten top predictions are model-only (L5) with no plausible mechanism, and should not be pursued.
- JIA is mechanistically sound and has L3-level literature, but there are no registered trials. NSAIDs are already used symptomatically in JIA, so this largely confirms existing practice rather than identifying a new indication.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications, approved indications and any paediatric dosing or age limits), which is a blocking gap for safety screening
- Confirmation of whether the registered South African labels already include juvenile arthritis
- Detailed mechanism of action data
- Contemporary controlled paediatric data and a paediatric safety plan (GI, renal, hepatic monitoring)
- Verification of the suspect registrations (Sandoz Lamotrigine 25, Ibugesic Plus) and of EML status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

