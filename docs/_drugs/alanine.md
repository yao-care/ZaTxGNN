---
layout: default
title: Alanine
parent: Model Prediction Only (L5)
nav_order: 19
evidence_level: L5
indication_count: 10
---

# Alanine
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

# Alanine: From Parenteral Nutrition Component to Gastroparesis

## One-Sentence Summary

Alanine is a non-essential amino acid. In South Africa it is registered mainly as an ingredient of parenteral nutrition infusions, and no approved indication text is recorded for it.
The TxGNN model predicts it may be effective for **Gastroparesis** (score 99.4%), but **none of the 9 retrieved clinical trials tests alanine** and there are **0 supporting publications**.
This is a model prediction only, with no direct evidence behind it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA registration data. The registered products are infusion products, mostly parenteral nutrition |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for alanine. Alanine is a non-essential amino acid that takes part in the glucose-alanine cycle and gluconeogenesis. In South Africa it is supplied mainly as a component of parenteral nutrition formulations.

No established mechanism links alanine to gastric motility or gastric emptying. The original indication is also missing from the registration data, so the relationship between the original and predicted indications cannot be assessed. The high TxGNN score comes from the knowledge graph alone. It does not show that alanine works in gastroparesis.

The other top predictions (dyspepsia, congenital prothrombin deficiency, renal tubular acidosis and others) are also L5 with no supporting evidence.

---

## Clinical Trial Evidence

The trials below matched on the disease term "gastroparesis". All were graded C (not relevant) because none tests alanine.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06452966](https://clinicaltrials.gov/study/NCT06452966) | N/A | Recruiting | 350 | Traditional Chinese medicine for organ failure in ICU patients. Not relevant to alanine |
| [NCT02793154](https://clinicaltrials.gov/study/NCT02793154) | Phase 4 | Terminated | 4 | Albiglutide vs exenatide on gastric emptying in type 2 diabetes. Too small to be informative |
| [NCT01149369](https://clinicaltrials.gov/study/NCT01149369) | Phase 2 | Completed | 126 | Aprepitant vs placebo for chronic nausea and vomiting of presumed gastric origin |
| [NCT01934192](https://clinicaltrials.gov/study/NCT01934192) | Phase 2 | Terminated | 91 | Motilin agonist GSK962040 for enteral feeding tolerance in critically ill patients |
| [NCT03587142](https://clinicaltrials.gov/study/NCT03587142) | Phase 2 | Completed | 96 | Buspirone vs placebo for early satiety and symptoms of gastroparesis |
| [NCT01602549](https://clinicaltrials.gov/study/NCT01602549) | Phase 2 | Completed | 58 | GSK962040 and L-DOPA pharmacokinetics in Parkinson's disease with delayed gastric emptying |
| [NCT07270939](https://clinicaltrials.gov/study/NCT07270939) | N/A | Not yet recruiting | 150 | Enteral feeding cycle duration (18/20/24 h) in ICU patients |
| [NCT03941288](https://clinicaltrials.gov/study/NCT03941288) | Phase 2 | Completed | 92 | Cannabidiol in gastroparesis and functional dyspepsia |
| [NCT01262898](https://clinicaltrials.gov/study/NCT01262898) | Phase 2 | Completed | 79 | GSK962040 vs placebo in diabetic gastroparesis |

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Ten registrations exist and the five main ones are listed. Approved indication text is not recorded for any of them. One entry, Adco-ipratropium, is a vial product that does not look like an amino acid formulation, so its match to alanine should be checked.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 33/10.2.1/0271 | Adco-ipratropium (ni201) | Vial | Not recorded |
| Reg. No. 37/25.2/0503 | Oliclinomel N6 900E 2000ml | Infusion | Not recorded |
| Reg. No. 41/25/0757 | Nutriflex Lipid Peri | Infusion | Not recorded |
| Reg. No. 52/25/0739 | Numeta G13E | Infusion | Not recorded |
| Reg. No. 52/25/0740 | Numeta G16E | Infusion | Not recorded |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the TxGNN score alone. None of the retrieved trials tests alanine, no literature was found, and no mechanism links alanine to gastric motility. The original indication and safety data are also missing, so the case does not pass the first screening stage.

**To proceed, the following is needed:**
- SAHPRA Professional Information (PI) for the alanine-containing products, covering approved indications, warnings and contraindications
- Confirmation that the Adco-ipratropium registration really contains alanine
- Mechanism of action data (for example from DrugBank) and a plausible pathway to gastric emptying
- Any preclinical or clinical study that tests alanine or amino acid formulations in gastroparesis
- A check of alanine's relevance to gastroparesis against the enteral and parenteral nutrition literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

