---
layout: default
title: Dextromethorphan
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 6
---

# Dextromethorphan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Dextromethorphan: From Antitussive Use to Nasal Cavity Disease

## One-Sentence Summary

Dextromethorphan is a centrally-acting cough suppressant, widely known and used for cough relief, though formal original-indication and mechanism-of-action records are not present in this evidence pack.
The TxGNN model predicts it may be effective for **Nasal Cavity Disease**,
but this is currently supported by only **1 ongoing clinical trial** (not yet completed, and targeting a different indication) and **no published literature**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antitussive / cough suppression (based on known pharmacological classification; formal indication and MOA records are not available in this evidence pack) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 (mechanism-based reasoning only; the one registered trial is still recruiting and targets a different indication — see caveat below) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for dextromethorphan is not available in this evidence pack (flagged as a High-severity data gap). Based on generally known pharmacology, dextromethorphan is a centrally-acting antitussive that acts on the medullary cough center, and it is commonly formulated in combination with antihistamines for relief of upper-respiratory and nasal symptoms accompanied by cough (e.g., rhinorrhea, nasal congestion). On this basis, the mechanistic link to "nasal cavity disease" is biologically plausible — cough suppression is frequently bundled with symptomatic relief of nasal/upper-airway complaints in existing over-the-counter combination products.

However, an important caveat must be raised: the single clinical trial retrieved as supporting evidence (NCT06958692) is a Phase 3 trial of a **dextromethorphan–bupropion** combination for **Major Depressive Disorder** — not nasal cavity disease. The evidence pack's own rationale appears to have inferred a connection to an antihistamine combination ("Dextromethorphan and B...") based on the trial title, but the actual trial title clearly specifies "Bupropion," which is pharmacologically unrelated to nasal/antihistamine therapy. This means the clinical trial evidence currently on file does **not** directly substantiate the nasal cavity disease prediction, and the mechanistic rationale for this indication rests on general pharmacological reasoning rather than disease-specific data.

Given that no completed trials, no literature, and no directly relevant trial evidence exist for this specific indication, this prediction should be treated as a research hypothesis rather than an actionable clinical signal at this time.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06958692](https://clinicaltrials.gov/study/NCT06958692) | Phase 3 | Recruiting | 388 | Multicenter, randomized, double-blind, placebo-controlled trial of dextromethorphan + bupropion sustained-release tablets in Chinese adults with major depressive disorder. **Note: this trial targets major depressive disorder, not nasal cavity disease** — it does not directly support the predicted indication and is included here only because it was the sole trial retrieved for this drug. |

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Dextromethorphan currently holds **no SAHPRA registrations** and has a market status of **Not Marketed** in South Africa. No product-level registration data (registration number, product name, dosage form, or approved indication) is available in this evidence pack.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: this evidence pack contains a Blocking-severity data gap on SAHPRA labeling — key warnings, contraindications, and drug-drug interaction data are all currently unavailable, which prevents any formal safety pre-screening.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only clinical trial retrieved does not actually correspond to the predicted indication (it targets major depressive disorder, not nasal cavity disease, and is still recruiting with no results), and the drug has no South African market presence (0 SAHPRA registrations). Combined with a Blocking-severity gap in SAHPRA safety/label data, this candidate cannot yet proceed past initial safety screening.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings, contraindications) — currently a Blocking data gap
- Formal mechanism-of-action documentation (e.g., via DrugBank) — currently a High-severity data gap
- Clinical trial or literature evidence that directly investigates dextromethorphan (or a relevant combination product) for nasal cavity disease specifically, rather than relying on an unrelated MDD trial
- Results from the ongoing Phase 3 trial (NCT06958692) once completed, to clarify whether it has any bearing on this drug's broader safety/efficacy profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

