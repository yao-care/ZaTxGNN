---
layout: default
title: Phenoxymethylpenicillin
parent: Model Prediction Only (L5)
nav_order: 370
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
monitor_inn: "Phenoxymethylpenicillin"
predicted_indications: ["epiglottitis", "laryngitis"]
description: "Phenoxymethylpenicillin: predicted new indication Epiglottitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Phenoxymethylpenicillin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Phenoxymethylpenicillin: Epiglottitis
{: .text-alpha }

## One-Sentence Summary

Phenoxymethylpenicillin (penicillin V) is an oral penicillin antibiotic, originally used for streptococcal and staphylococcal infections, pharyngitis, otitis media, erysipelas and scarlet fever.
The TxGNN model predicts it may be effective for **epiglottitis**, with a very high score. However, **no clinical trials and no publications** currently support this direction, so the prediction is based on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, penicillin V is a beta-lactam antibiotic with activity against streptococci. Its efficacy in streptococcal throat and respiratory infections is established, and mechanistically it may be applicable to epiglottitis, which is often caused by bacteria.

Epiglottitis is caused by *Haemophilus influenzae* type b, *Streptococcus pneumoniae* and group A streptococci. The streptococcal link gives the prediction some biological basis, and it overlaps with the drug's original upper-airway infection indications.

There are important limits:
- Penicillin V is not reliable against beta-lactamase-producing *H. influenzae*.
- Epiglottitis is an acute airway emergency, where parenteral therapy is standard. An oral tablet is not suitable.

The high score is therefore a model output only and should be interpreted cautiously.

### Other Predicted Indications (for context)

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Laryngitis | 0.9985 | L5 | Mostly viral. The only retrieved paper tested erythromycin, not penicillin V. Its abstract notes phenoxymethylpenicillin had no effect on the clinical course in earlier studies. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top prediction (epiglottitis), currently no related literature is available.

For context, the most relevant publications found for the other predicted indications are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1632252](https://pubmed.ncbi.nlm.nih.gov/1632252/) | 1992 | Clinical trial (laryngitis) | Acta Oto-Laryngologica Suppl. | 106 adults with acute laryngitis treated with erythromycin or placebo. Erythromycin reduced *B. catarrhalis* isolation. This tested erythromycin, not penicillin V, and notes that phenoxymethylpenicillin had no effect on the clinical course in earlier studies. |
| [2497823](https://pubmed.ncbi.nlm.nih.gov/2497823/) | 1989 | Clinical study (UTI) | BMJ | Effect of phenoxymethylpenicillin and erythromycin on urinary isolates in girls with untreated asymptomatic bacteriuria. Indirect evidence for symptomatic UTI. |
| [8722932](https://pubmed.ncbi.nlm.nih.gov/8722932/) | 1996 | Clinical report | Clin Infect Dis | Erythema migrans in pregnancy, with a few patients treated with phenoxymethylpenicillin. Not related to UTI. |

The other papers retrieved for urinary tract infection concern different drugs (cefetamet, cefuroxime, cefpodoxime), prescribing patterns or risk associations, and give no support for efficacy.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G/20.1.2/145 | Incil Vk | Tablet (oral) | Not recorded in the data compiled for this report |

Essential Medicines List (EML) inclusion status could not be determined from the data compiled for this report.

---

## Safety Considerations

**Contraindications from the knowledge graph** (drug-disease contraindication links, not label text): kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, infectious mononucleosis, chronic Epstein-Barr virus infection syndrome.

**Drug Interactions** (32 recorded in total; main ones listed):
- **Moderate:** doxycycline, minocycline, tetracycline, neomycin, balsalazide, picosulfuric acid, warfarin, dicoumarol, iodide I-123, iodide I-131
- **Minor:** clarithromycin
- **Unknown severity:** omeprazole, lansoprazole, simvastatin, prednisolone, dexamethasone, acetylsalicylic acid, clopidogrel, heparin, ibuprofen

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The epiglottitis prediction has a high model score but no trials or publications behind it. The oral route is unsuitable for an acute airway emergency, and penicillin V is unreliable against beta-lactamase-producing *H. influenzae*. Several other predictions (Ureaplasma, gonococcal, tuberculosis and non-infectious conditions) conflict with known microbiology and are likely false positives.

**To proceed, the following is needed:**
- Retrieval and review of the SAHPRA package insert (warnings, contraindications, approved indications). This is currently a blocking data gap.
- Mechanism of action data (for example from DrugBank).
- Clinical evidence specific to penicillin V in epiglottitis, and an assessment of whether any role exists beyond parenteral therapy (e.g. step-down oral treatment).
- Local resistance data in South Africa for *H. influenzae* and streptococci.
- Confirmation of EML status and an analysis of route compatibility.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

