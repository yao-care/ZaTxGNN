---
layout: default
title: Magnesium Hydroxide
parent: Moderate Evidence (L3-L4)
nav_order: 305
evidence_level: L3
indication_count: 6
---

# Magnesium Hydroxide
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **6** 
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

# Magnesium Hydroxide: From Antacid Use to Active Peptic Ulcer Disease

## One-Sentence Summary

Magnesium hydroxide is an antacid that neutralises gastric acid, and it is registered in South Africa in products such as Mucaine suspension. The TxGNN model predicts it may be effective for **active peptic ulcer disease**, but this is closer to confirming a classic antacid use than to a genuine repurposing signal. It currently has **0 registered clinical trials** and **20 publications** for this indication. Most of the publications are older reviews, small studies and animal work, and most of the human data cover aluminium/magnesium combinations rather than magnesium hydroxide alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 entries (2 distinct registration numbers; Mucaine is listed twice) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on the literature, magnesium hydroxide is an antacid. It neutralises secreted gastric acid, raises intragastric pH and reduces pepsin activity.

Peptic ulcer is the classic use of antacids, so the prediction is plausible mainly because it matches the drug class. Animal studies of aluminium/magnesium hydroxide antacids also suggest a gastroprotective effect through endogenous prostaglandins (PMID 2595273). Small human mucosal studies point in the same direction, but they used combination products.

Antacids are now mostly adjunctive or symptomatic therapy next to proton pump inhibitors (PPIs) and H2 blockers. The literature is also dominated by aluminium/magnesium combinations, so the effect of magnesium hydroxide on its own is not separated out.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for active peptic ulcer disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT | Scand J Gastroenterol | 12-week double-blind trial in 72 duodenal or prepyloric ulcer patients. Antacid suspension plus hyoscyamine gave a 50% healing rate at 3 weeks, versus 67% with cimetidine and placebo as the third arm. The abstract is truncated, so the antacid-versus-placebo result needs full-text review. |
| [3018068](https://pubmed.ncbi.nlm.nih.gov/3018068/) | 1986 | RCT | J Clin Gastroenterol | Compared sodium bicarbonate with aluminium/magnesium hydroxide for postprandial gastric acid buffering in duodenal ulcer patients. This is a pharmacodynamic endpoint, not ulcer healing. |
| [3003883](https://pubmed.ncbi.nlm.nih.gov/3003883/) | 1985 | Randomised trial | Scand J Gastroenterol | 80 duodenal ulcer patients on an antacid tablet were randomised to a high- or low-fibre diet. Healing was 67.5% versus 60%. The antacid was background therapy, not the tested variable. |
| [37146](https://pubmed.ncbi.nlm.nih.gov/37146/) | 1979 | Review | Fortschr Med | Antacid use in peptic ulcer rests on acid neutralisation and pepsin inhibition. Dosing of 40-80 mval of acid-neutralising capacity, taken 1 and 3 hours after meals, is recommended. |
| [22950493](https://pubmed.ncbi.nlm.nih.gov/22950493/) | 2013 | Review | Curr Pharm Des | Updates the mucosal-protective and ulcer-healing actions of antacids beyond acid neutralisation. |
| [6086186](https://pubmed.ncbi.nlm.nih.gov/6086186/) | 1984 | Review | Clin Gastroenterol | Reviews antacids and anticholinergics in duodenal ulcer treatment. |
| [8260735](https://pubmed.ncbi.nlm.nih.gov/8260735/) | 1993 | Review | J Physiol Pharmacol | Antacids reduce gastric acidity and peptic activity. Aluminium-containing antacids may also enhance mucosal defence via prostaglandins. |
| [2401189](https://pubmed.ncbi.nlm.nih.gov/2401189/) | 1990 | Retrospective clinical study | Drugs Exp Clin Res | 267 children with peptic symptoms, comparing the efficacy of several drug types in acute disease and relapse. |
| [2595273](https://pubmed.ncbi.nlm.nih.gov/2595273/) | 1989 | Preclinical (animal) | Scand J Gastroenterol | In rats, an Al/Mg hydroxide antacid dose-dependently prevented gastric lesions, similar to a PGE2 analogue. Endogenous prostanoids are involved. |
| [35720246](https://pubmed.ncbi.nlm.nih.gov/35720246/) | 2022 | In vitro product analysis | Med Pharm Rep | Evaluated the acid-neutralising capacity of antacids marketed in Morocco. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. E/11.4.3/1223 | Mucaine | Suspension |
| Reg. No. 41/1.2/0373 | Voxra Xl 150 | Tablet |

Approved indication text and Essential Medicines List (EML) status are not available in the source data, so they are not shown. The Mucaine entry appears twice in the source data under the same registration number.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Signals from the retrieved evidence that should guide guardrails:
- **Drug interactions:** A Phase 1 study (NCT00446316) examined the effect of an Mg/Al antacid on imatinib pharmacokinetics. Chelation-type interactions should be checked, even though the interaction database returned no entries. One small study found no interaction between an Al/Mg hydroxide antacid and cimetidine (PMID 6613216).
- **Renal impairment:** Hypermagnesaemia risk should be considered in patients with reduced renal function.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Antacid use in peptic ulcer is long established, and the drug is already marketed in South Africa. The evidence is limited to older reviews, small mostly combination-product studies and animal data, with no registered trials. It should be positioned only as adjunctive or symptomatic relief alongside PPIs or H2 blockers.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- Full-text review of the 1980s controlled studies (such as PMID 7034155) to confirm design and product composition, which may raise the evidence level
- A modern controlled study, or a subgroup analysis, that separates the magnesium hydroxide effect from the aluminium component
- Confirmation of the active ingredients and approved indications of the registered products

Results are for research reference only and do not constitute medical advice. Predicted indications require clinical validation before use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

