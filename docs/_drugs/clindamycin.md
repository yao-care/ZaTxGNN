---
layout: default
title: Clindamycin
parent: Model Prediction Only (L5)
nav_order: 131
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Clindamycin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Acne, streptococcal and staphylococcal infections…"
monitor_inn: "Clindamycin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "neurotrophic keratopathy", "epidemic keratoconjunctivitis", "postmenopausal atrophic vaginitis", "superior limbic keratoconjunctivitis", "keratomalacia", "ophthalmia nodosa", "toxic maculopathy due to antimalarial drugs"]
---

# Clindamycin
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

# Clindamycin: From Bacterial Infections and Acne to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Clindamycin is a lincosamide antibiotic, originally used for bacterial infections (streptococcal, staphylococcal and anaerobic infections, pneumonia, bacterial vaginosis) and acne.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. It is a model-based prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne, streptococcal and staphylococcal infections, anaerobic bacterial infections, bacterial vaginosis (from the knowledge graph; SAHPRA indication text is not available) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Clindamycin is a lincosamide antibiotic, and this class is generally known to inhibit bacterial protein synthesis by binding the 50S ribosomal subunit. Its efficacy in Gram-positive and anaerobic infections is established, so in principle it could act on bacterial disease of the ocular surface.

The prediction is weak mechanistically. Punctate epithelial keratoconjunctivitis is often viral or non-infectious, so an antibacterial rationale does not fit well. Systemic or topical ocular use of clindamycin is not an established practice. The very high score (99.97%) reflects proximity in the knowledge graph, not clinical evidence.

Other top-ranked predictions are also mostly eye conditions. The most notable are:
- **Exposure keratitis** (score 99.80%, evidence level L4): only indirect literature, such as keratitis case series and cohort studies of *S. aureus* and *Bacillus cereus*, which describe organisms and antibiotic susceptibility rather than treatment with clindamycin.
- **Postmenopausal atrophic vaginitis** (99.03%): this is caused by oestrogen deficiency, not infection, so antibacterial therapy does not address the cause.
- **Non-human animal disease** (99.69%): a non-specific category, not a valid human indication. The retrieved papers concern *C. difficile*, which is a known adverse consequence of clindamycin.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

For reference, indirect literature was retrieved for the second-ranked prediction (exposure keratitis). It does not test clindamycin for that condition:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24244625](https://pubmed.ncbi.nlm.nih.gov/24244625/) | 2013 | Cohort | PLoS One | Review of hospital cases of *S. aureus* keratitis, comparing MRSA and MSSA |
| [22880135](https://pubmed.ncbi.nlm.nih.gov/22880135/) | 2012 | Cohort | PLoS One | Prevalence, clinical features and antibiotic susceptibility of ocular MRSA vs MSSA infections |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case report | Ophthalmology | Contact lens-related *Bacillus cereus* keratitis |

## South Africa Market Information

Clindamycin is marketed in South Africa with 5 valid single-ingredient registrations. Approved indication text and Essential Medicines List status were not available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| P/20.1.6/63 | Dalacin T Solution | Solution | Not available |
| F/20.1.1/169 | Dalacin C 600Mg | Injection | Not available |
| 42/13.11/0441 | Clindoxyl | Gel | Not available |
| A.682 | Daraprim | Tablet | Not available |
| 49/13.12/0499 | Treclin Gel | Gel | Not available |

Note: the register entry for Daraprim (tablet) is listed under clindamycin in the compiled data. This should be verified against the SAHPRA register, as Daraprim is normally associated with pyrimethamine.

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** liver failure, sunburn, Crohn disease, inflammatory bowel disease, ulcerative colitis, Crohn's colitis, atopic eczema and other dermatitis (including exfoliative dermatitis), diarrhoeal disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, and vulvovaginal candidiasis. These should be confirmed against the approved Professional Information (PI).
- **Drug interactions:** 100 interactions were identified in total; the first 20 returned are summarised here. Moderate-level interactions: balsalazide, clarithromycin, picosulfuric acid, attapulgite, kaolin. Other listed agents have an unclassified severity level, including amphotericin B, acetylsalicylic acid, amoxicillin, bupropion, pantoprazole, glimepiride, doxycycline, clotrimazole, morphine, metformin, omeprazole, sucralfate, rosiglitazone, lansoprazole and vancomycin.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on graph proximity alone, with no clinical trials or supporting literature. The antibacterial mechanism is a poor fit for a condition that is often viral or non-infectious. Clindamycin also carries a recognised risk of *C. difficile* colitis, and ocular use is not established practice.

**To proceed, the following is needed:**
- Clinical or preclinical evidence of clindamycin efficacy in punctate epithelial keratoconjunctivitis, or a clear bacterial aetiology in the target population
- Detailed mechanism of action data
- SAHPRA package insert warnings and contraindications, and approved indication text for each registration
- Assessment of ocular-compatible formulations and routes (currently none identified)
- Verification of the Daraprim registration entry against the SAHPRA register
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

