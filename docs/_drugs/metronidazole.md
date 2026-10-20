---
layout: default
title: Metronidazole
parent: Model Prediction Only (L5)
nav_order: 323
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Metronidazole: predicted new indication Pneumocystosis (evidence level L5). Approved use: Anaerobic bacterial infections, giardiasis, bacterial vaginosis…"
monitor_inn: "Metronidazole"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis", "ulcerative proctosigmoiditis", "nocardiosis", "postmenopausal atrophic vaginitis", "Cryptococcal meningitis", "papillary conjunctivitis", "myiasis", "cap polyposis", "ulceration of vulva"]
---

# Metronidazole
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

# Metronidazole: From Anaerobic and Protozoal Infections to Pneumocystosis

## One-Sentence Summary

Metronidazole is an antibiotic and antiprotozoal drug originally used for anaerobic bacterial infections, giardiasis, bacterial vaginosis, peritonitis and rosacea.
The TxGNN model's top-ranked prediction is **pneumocystosis**, but there are **no registered clinical trials** and only **10 publications** (reviews and case reports, none with direct evidence for metronidazole in this condition).
The prediction is not mechanistically plausible, and the evidence supports a **Hold** decision for this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anaerobic bacterial infections, giardiasis, bacterial vaginosis, peritonitis, rosacea (the SAHPRA registration data compiled for this report contain no approved indication text) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, metronidazole is a nitroimidazole antimicrobial with established efficacy against anaerobic bacteria and protozoa.

For pneumocystosis, the mechanistic link is weak. Pneumocystis is a fungus that lacks the nitroreductase activation pathway that metronidazole depends on. The high TxGNN score most likely reflects network proximity to antiparasitic drugs rather than a true biological rationale. Standard therapy is trimethoprim-sulfamethoxazole.

### Other Predicted Indications Reviewed

Nine further predictions were assessed. Two show somewhat more support, though still limited:

| Rank | Predicted Indication | Evidence Level | Assessment |
|------|------|------|------|
| 9 | Cap polyposis | L3 | Case reports and case series report remission with metronidazole; one paper proposes an anti-inflammatory mechanism. No controlled trials. Candidate for a low-risk exploratory study. |
| 10 | Vulvar ulceration | L3 | Standard treatment for amoebic genital or cutaneous ulcers; used in vulvar Crohn's disease (retrospective study of 22 patients). Benefit depends on cause. |
| 8 | Myiasis | L4 | Used as an adjunct for anaerobic wound infection and odour control; ivermectin and mechanical removal are primary treatments. |
| 3 | Ulcerative proctosigmoiditis | L4 | Only general IBD reviews; metronidazole is proven in Crohn's disease, not ulcerative colitis. |
| 4 | Nocardiosis | L4 | Case reports of brain abscess only; standard therapy is TMP-SMX. |
| 2, 5, 6, 7 | Punctate epithelial keratoconjunctivitis, postmenopausal atrophic vaginitis, cryptococcal meningitis, papillary conjunctivitis | L5 | No plausible mechanism or supporting evidence. |

## Clinical Trial Evidence

Currently no related clinical trials registered. No SANCTR or PACTR entries were identified in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clin Proc | Overview of antiparasitic agents; no specific evidence for metronidazole in pneumocystosis |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | Am Fam Physician | Metronidazole is the drug of choice for amoebic colitis and trichomoniasis; trimethoprim-sulfamethoxazole is used for Pneumocystis pneumonia |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clin Pharmacokinet | Pharmacokinetic rationale for antiprotozoal therapy |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clin Pharm | Infectious complications of AIDS, including Pneumocystis pneumonia |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Top Antivir Med | HIV-related opportunistic infections remain relevant |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Rev Infect Dis | Critique of antimicrobial prophylaxis trials |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case report | Am Rev Respir Dis | Pneumocystis and CMV pneumonia in a patient previously treated with metronidazole for diarrhoea (not a treatment report) |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case report | Kansenshogaku Zasshi | Two AIDS patients; metronidazole used for amoebic dysentery, not for Pneumocystis |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case report | J Formos Med Assoc | AIDS patient with CMV and amoebic colitis causing colon perforation |
| [42178576](https://pubmed.ncbi.nlm.nih.gov/42178576/) | 2026 | Case report | J Med Case Rep | Streptococcus intermedius cerebellar abscess in sarcoidosis |

None of these papers shows that metronidazole treats pneumocystosis.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| S/20.2.6/153 | Sandoz Metronidazole | Tablet (oral) | Not available in the data compiled |
| 42/20.2/0567 | Bio metronidazole iv | Infusion (injectable) | Not available in the data compiled |
| 33/20.2.6/0243 | Metrogel v | Vaginal gel (topical) | Not available in the data compiled |

All three registrations are valid single-ingredient products. Essential Medicines List status was not included in the data compiled for this report.

## Safety Considerations

**Contraindication-related diseases (knowledge graph, not label text):** the knowledge graph links metronidazole to caution in liver failure and liver disease, epilepsy and brain disease, kidney disease, blood disorders (neutropenia, leukopenia, agranulocytosis, blood coagulation disease), peripheral neuropathy and other peripheral nervous system disease, optic nerve and visual pathway disease, non-infectious meningitis, congestive heart failure, diabetes and diabetic ketoacidosis, gout, gallbladder disease, dermatitis, pyoureter and substance abuse or dependence. These must be verified against the approved Professional Information.

**Drug interactions:** 100 interactions were identified (DDInter). Notable examples:
- **Major:** Ethanol
- **Moderate:** Paclitaxel, adalimumab, trastuzumab emtansine, ethinylestradiol, estradiol, butalbital, amobarbital, amiodarone, celecoxib, loperamide
- **Minor:** Abiraterone, tramadol, famotidine, salbutamol, alfuzosin, amisulpride, amitriptyline, anagrelide, propofol

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Pneumocystosis is predicted on model score alone (L5). There are no trials, no supporting literature, and no plausible mechanism, and effective standard therapy exists.
- If the portfolio is to be pursued, cap polyposis and etiology-specific vulvar ulceration (L3) are better candidates for exploratory research than the top-ranked prediction.

**To proceed, the following is needed:**
- Mechanism of action data for metronidazole
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- SAHPRA-approved indication text for each registration
- For cap polyposis or vulvar ulceration: a systematic literature review and a controlled or prospective study design
- Confirmation of route compatibility with the registered oral, intravenous and vaginal formulations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

