---
layout: default
title: Oxytetracycline
parent: 僅模型預測 (L5)
nav_order: 351
evidence_level: L5
indication_count: 10
---

# Oxytetracycline
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

# Oxytetracycline: From Broad-Spectrum Antibacterial Use to Otitis Externa

## One-Sentence Summary

> Oxytetracycline is a broad-spectrum tetracycline-class antibiotic; this evidence pack profiles 10 TxGNN-predicted indications for it, and among these, **Otitis Externa** stands out as the only candidate with real supporting evidence rather than a bare model score.
> The TxGNN model gives it a **99.27%** prediction score, and **20 publications** (including 4 randomized trials) document decades of topical use for this indication — no dedicated clinical trials are currently registered.
> Note: the model's single highest-scoring prediction, chronic rhinosinusitis (99.61%), has **zero** supporting trials or literature and is not the focus of this report (see appendix table below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this evidence pack (broad-spectrum tetracycline antibacterial; original_moa/original_indications are data gaps) |
| Predicted New Indication | Otitis Externa (external ear infection) |
| TxGNN Prediction Score | 99.27% |
| Evidence Level | L2 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed original-indication and mechanism-of-action data for this drug were not available in the source fields (`original_moa`, `original_indications` are both data gaps). However, the repurposing rationale attached to the otitis externa prediction confirms the known pharmacology: **oxytetracycline is a broad-spectrum tetracycline antibiotic that inhibits bacterial 30S ribosomal protein synthesis**, giving it activity against the organisms most commonly implicated in otitis externa — *Staphylococcus aureus* and *Pseudomonas aeruginosa*.

Topical formulations combining oxytetracycline with hydrocortisone (and often polymyxin B) — sold historically as "Terra-Cortril" — have been used for external ear infections since at least the 1950s, treating both the bacterial infection and the accompanying inflammation in a single application. This is less a novel repurposing "discovery" and more a case where TxGNN has correctly re-identified a well-established, long-standing clinical use.

By contrast, the model's top-ranked prediction by score alone — chronic rhinosinusitis (99.61%) — has no clinical trial or literature evidence at all in this pack, and several other candidates (paranasal sinus neoplasm, Chagas cardiomyopathy) have mechanistic rationales explicitly flagged as weak or likely noise. This is why otitis externa, despite a marginally lower TxGNN score, is the clinically actionable candidate here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for otitis externa.

*(Note: a separate, lower-ranked prediction in this pack — "post-bacterial disorder" — is linked to [NCT02099240](https://clinicaltrials.gov/study/NCT02099240), a terminated, 11-patient osteomyelitis trial. This does not pertain to otitis externa and is listed for completeness in the appendix below.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2415098](https://pubmed.ncbi.nlm.nih.gov/2415098/) | 1985 | RCT | Archives of Oto-Rhino-Laryngology | 55 patients with acute external otitis; oxytetracycline/hydrocortisone/polymyxin B vs. framycetin/gramicidin — 78% cured, no significant difference between regimens |
| [1782715](https://pubmed.ncbi.nlm.nih.gov/1782715/) | 1991 | RCT | Clinical Otolaryngology and Allied Sciences | 10 patients, bilateral disease; compared dressing vs. "sump filling" application of topical antibiotic/steroid — 9/10 ears improved in each group |
| [2156538](https://pubmed.ncbi.nlm.nih.gov/2156538/) | 1990 | RCT | European Archives of Oto-Rhino-Laryngology | 46 patients with acute external otitis; oxytetracycline/hydrocortisone/polymyxin B vs. hydrocortisone-17-butyrate — 80% overall cure rate, no significant efficacy difference |
| [15949095](https://pubmed.ncbi.nlm.nih.gov/15949095/) | 2005 | RCT | The Journal of Laryngology and Otology | 51 patients, multicentre open randomized trial; steroid-only vs. hydrocortisone+oxytetracycline+polymyxin B — comparable outcomes, questions necessity of the antibiotic component |
| [8222746](https://pubmed.ncbi.nlm.nih.gov/8222746/) | 1993 | Comparative | Current Medical Research and Opinion | 30 patients; ciprofloxacin drops vs. oxytetracycline/polymyxin B/hydrocortisone, compared clinically and bacteriologically over 8 days |
| [12564664](https://pubmed.ncbi.nlm.nih.gov/12564664/) | 2002 | Comparative | Current Medical Research and Opinion | Comparison of two antibacterial/anti-inflammatory formulations (otic powder vs. drops) for otitis externa |
| [40981334](https://pubmed.ncbi.nlm.nih.gov/40981334/) | 2025 | Case report | Infectious Disease Reports | Case report of *Vibrio alginolyticus* (rare pathogen) isolated from external otitis in an immunocompromised patient |
| [6451857](https://pubmed.ncbi.nlm.nih.gov/6451857/) | 1980 | Review | Otolaryngology–Head and Neck Surgery | Review of drug therapy for *Aspergillus* otitis externa (fungal aetiology) |
| [14412537](https://pubmed.ncbi.nlm.nih.gov/14412537/) | 1959 | Case series | Monatsschrift für Ohrenheilkunde und Laryngo-Rhinologie | Early case series on oxytetracycline + hydrocortisone treatment of otitis externa |
| [13447965](https://pubmed.ncbi.nlm.nih.gov/13447965/) | 1957 | Case series | Eye, Ear, Nose & Throat Monthly | Early case series treating otitis externa with Terra-Cortril (oxytetracycline/hydrocortisone) suspension |

10 additional lower-priority publications (mostly veterinary/in-vitro studies) exist in the source pack but are omitted here as less clinically relevant to human use.

---

## Other TxGNN-Predicted Indications (Reference Only)

For context, this evidence pack scored oxytetracycline against 10 candidate indications. Only otitis externa and "post-bacterial disorder" have any supporting evidence; the remaining 8 are model score only.

| Disease | TxGNN Score | Evidence Level | Recommendation |
|---|---|---|---|
| Chronic rhinosinusitis | 99.61% | L5 | Hold |
| Chronic ethmoidal sinusitis | 99.61% | L5 | Hold |
| Paranasal sinus neoplasm | 99.58% | L5 | Hold |
| Punctate epithelial keratoconjunctivitis | 99.52% | L5 | Hold |
| Postinfectious vasculitis | 99.37% | L5 | Hold |
| Post-bacterial disorder | 99.35% | L3 | Research Question |
| Post-infectious syndrome | 99.33% | L5 | Hold |
| Infective urethral stricture | 99.28% | L5 | Hold |
| Chagas cardiomyopathy | 99.27% | L5 | Hold |

---

## South Africa Market Information

Oxytetracycline is currently **Not Marketed** in South Africa under this evidence pack — no SAHPRA registrations are on file (0 licenses). Any repurposing pathway would require a new or amended registration submission.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Key warnings, contraindications, and drug interaction data were all marked as data gaps in this evidence pack.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Otitis externa is supported by four small-to-moderate randomized trials and a long documented history of clinical use (oxytetracycline/hydrocortisone combinations), giving it L2 evidence — the strongest of the 10 candidates in this pack. However, the trials are decades old, none are registered on ClinicalTrials.gov, and the drug currently has no SAHPRA registration or PI on file in South Africa.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) — warnings, contraindications, and DDI data are all currently gaps
- Confirmation of whether a suitable topical (otic) formulation is registrable/available in South Africa
- A modern systematic review or updated RCT, given existing evidence predates 2005
- Registration/regulatory pathway assessment given current "Not Marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

