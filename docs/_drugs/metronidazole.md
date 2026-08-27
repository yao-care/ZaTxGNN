---
layout: default
title: Metronidazole
parent: 僅模型預測 (L5)
nav_order: 315
evidence_level: L5
indication_count: 10
---

# Metronidazole
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

# Metronidazole: From Anaerobic/Protozoal Infections to Pneumocystosis

## One-Sentence Summary

Metronidazole is a nitroimidazole antimicrobial internationally established for anaerobic bacterial and protozoal infections; specific South African regulatory indication text is not available in this evidence pack because the product currently has **no SAHPRA registrations on record**. The TxGNN model's top-ranked prediction is **Pneumocystosis** (score **99.99%**), but the **23 clinical trials** and **10 publications** returned show no direct evidence linking metronidazole to Pneumocystis treatment — this appears to be a knowledge-graph co-occurrence artifact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack — no SAHPRA licenses on record |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed (未上市) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for metronidazole is not provided in this evidence pack. Based on well-established pharmacology, metronidazole is a nitroimidazole that is reduced intracellularly by anaerobic and microaerophilic organisms to generate cytotoxic free-radical intermediates that damage microbial DNA — this underlies its activity against anaerobic bacteria (e.g., *Bacteroides*, *Clostridium*) and protozoa (e.g., *Entamoeba*, *Giardia*, *Trichomonas*).

This mechanism does **not** provide a plausible link to *Pneumocystis jirovecii*, the causative organism of pneumocystosis, which is currently classified as a fungus rather than an anaerobic bacterium or protozoan. Metronidazole has no established antifungal or anti-*Pneumocystis* activity; the standard of care for pneumocystosis is trimethoprim-sulfamethoxazole (TMP-SMX), not nitroimidazoles.

Reviewing the supporting evidence confirms this gap: none of the 23 retrieved clinical trials investigate metronidazole for pneumocystosis, and the retrieved literature consists of general reviews of antiparasitic drugs or HIV-related opportunistic infections, plus incidental case reports where a patient received metronidazole for an unrelated condition (e.g., amebic dysentery) and separately developed pneumocystosis. The most likely explanation for the high TxGNN score is that metronidazole and pneumocystosis co-occur frequently in the same literature/knowledge-graph context (HIV/immunocompromised-host infections) without a genuine causal or therapeutic relationship.

---

## Clinical Trial Evidence

**No clinical trials directly evaluating metronidazole for pneumocystosis were identified.** The broad search query returned 23 trials, but on review none investigate metronidazole treatment of pneumocystosis — the majority concern unrelated primary-care, opioid-management, diabetes-education, or care-delivery interventions. Representative examples, with their relevance grading, are shown for transparency:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02571673](https://clinicaltrials.gov/study/NCT02571673) | N/A | Completed | 65 | Head-and-neck cancer survivorship tool feasibility study — **not related** to metronidazole or pneumocystosis |
| [NCT03466866](https://clinicaltrials.gov/study/NCT03466866) | Phase 3 | Completed | 156 | Diabetes emergency-visit reduction education trial — **not related**; surfaced only via Phase 3 tag |
| [NCT02208947](https://clinicaltrials.gov/study/NCT02208947) | Phase 3 | Terminated | 77 | Advance care planning financial-incentive trial — **not related** |

---

## Literature Evidence

None of the retrieved publications directly evaluate metronidazole as a treatment for pneumocystosis. Most are general antiparasitic-drug reviews or incidental case reports where metronidazole was used for a different infection in a patient who also had (or later developed) pneumocystosis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review (pharmacokinetics) | Clinical Pharmacokinetics | General review of antiprotozoal drug regimens; does not address metronidazole for PCP |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Topics in Antiviral Medicine | General review of HIV-related opportunistic infections; TMP-SMX (not metronidazole) is standard PCP therapy |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clinical Pharmacy | Reviews AIDS-related infectious complications; metronidazole not discussed as PCP therapy |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case report | American Review of Respiratory Disease | Patient received metronidazole for diarrheal illness and separately developed PCP/CMV pneumonia — incidental co-occurrence, not treatment evidence |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case report | Kansenshogaku Zasshi | Patient treated with metronidazole for amebic dysentery/liver abscess, later diagnosed with PCP on a separate admission — incidental co-occurrence |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case report | J Formosan Medical Association | Colon perforation case involving CMV and amoebic colitis in an AIDS patient; metronidazole used for amoebiasis, not PCP |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | American Family Physician | Lists metronidazole for amebic colitis/trichomoniasis and TMP-SMX for PCP as separate drug-of-choice entries |

---

## South Africa Market Information

Currently no SAHPRA registrations are on record for this product (0 licenses; market status: not marketed). Regulatory indication and dosage form data cannot be extracted from this evidence pack.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (pneumocystosis) has no mechanistic plausibility — metronidazole has no known activity against *Pneumocystis jirovecii*, and none of the 23 clinical trials or 10 publications retrieved provide direct supporting evidence. This is assessed as a likely knowledge-graph co-occurrence artifact rather than a genuine repurposing signal (Evidence Level L4, Decision Stage S0).

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) covering warnings, contraindications, and DDI — this is a **Blocking** data gap (DG001) that must be resolved before any Stage 1 safety screening
- Confirmed mechanism of action data (DG002, High severity) to properly evaluate any future repurposing candidates for this drug
- If South African market entry is being considered independent of this prediction, formal SAHPRA registration status should be established

**Note:** This evidence pack contains 9 additional TxGNN-predicted indications for metronidazole. Two show notably stronger, mechanistically coherent evidence and warrant separate evaluation — **cap polyposis** (rank 9, evidence level L3, decision stage S2, recommendation "Proceed with Guardrails," with direct literature discussing metronidazole's anti-inflammatory mechanism in this condition) and **ulceration of vulva** (rank 10, evidence level L3, "Research Question," supported by case-level evidence for cutaneous amebiasis and vulvar Crohn's disease). These may be more productive candidates for further review than the top-ranked pneumocystosis signal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

