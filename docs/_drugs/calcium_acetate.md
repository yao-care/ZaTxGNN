---
layout: default
title: Calcium Acetate
parent: 僅模型預測 (L5)
nav_order: 88
evidence_level: L5
indication_count: 2
---

# Calcium Acetate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Calcium Acetate: From Hyperphosphataemia (CKD) to Calcium-Alkali Syndrome

## One-Sentence Summary

Calcium acetate is a well-established oral phosphate binder used in chronic kidney disease (CKD) to control hyperphosphataemia, though no SAHPRA registration records are available in this evidence pack.
The TxGNN model predicts it may be relevant to **Calcium-Alkali Syndrome**, with a high prediction score of **99.90%**.
However, **no supporting clinical trials or published literature** were identified, the evidence level is L5 (model prediction only), and a significant mechanistic paradox strongly calls this prediction into question.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from SAHPRA records (no current registration) |
| Predicted New Indication | Calcium-Alkali Syndrome |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmaceutical knowledge, calcium acetate is an oral calcium salt that acts as a phosphate binder: upon ingestion, it forms insoluble calcium phosphate complexes in the gastrointestinal tract, thereby reducing dietary phosphate absorption. This mechanism is exploited therapeutically in end-stage renal disease to prevent hyperphosphataemia and its downstream cardiovascular and skeletal complications. As a calcium salt, it also inherently supplies bioavailable calcium ions to the body.

The relationship between calcium acetate and calcium-alkali syndrome is, however, deeply counter-intuitive from a repurposing standpoint. Calcium-alkali syndrome (historically called milk-alkali syndrome) is characterised by the triad of hypercalcaemia, metabolic alkalosis, and renal insufficiency — and calcium acetate is itself a **recognised contributing cause** of this syndrome when used excessively or co-administered with vitamin D analogues, thiazide diuretics, or antacids. In other words, the drug does not oppose the pathophysiology of calcium-alkali syndrome; it shares a causal role in it.

The most plausible explanation for this TxGNN prediction is that the model identified a strong co-occurrence signal between calcium acetate and calcium-alkali syndrome within pharmacovigilance or adverse drug reaction databases, and misclassified a **causal/adverse relationship** as a **therapeutic one**. This is a known failure mode of knowledge graph models when pharmacovigilance edges and therapeutic edges are not clearly distinguished. On current evidence, using calcium acetate to treat calcium-alkali syndrome would be mechanistically paradoxical — analogous to treating the cause with the cause itself — and this prediction should not be pursued without extraordinary mechanistic justification.

---

## Clinical Trial Evidence

One trial was retrieved via automated keyword search. Upon review, it is not clinically relevant to this indication and is presented here solely for transparency:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03591471](https://clinicaltrials.gov/study/NCT03591471) | Phase 1/2 | Unknown | 500 | Investigates multi-step Traditional Chinese Medicine treatment (Tripterygium wilfordii glycosides) for Henoch-Schönlein Purpura Nephritis in children — **not related to calcium-alkali syndrome or calcium acetate**; assessed as a false-positive keyword match |

No trials directly investigating calcium acetate for calcium-alkali syndrome were identified in ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Calcium acetate is **not currently registered with SAHPRA** and has no marketing authorisation recorded for South Africa. No product licences, dosage forms, or approved indications were found in the evidence pack.

> Healthcare professionals wishing to use an unregistered medicine in South Africa must apply for a Section 21 (unregistered medicines) authorisation through SAHPRA prior to use.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> **Important contextual note:** As a calcium salt, calcium acetate carries a well-recognised risk of hypercalcaemia — the very metabolic disturbance that defines calcium-alkali syndrome. This further reinforces the concern that the TxGNN prediction represents a pharmacovigilance association rather than a therapeutic opportunity.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction presents a mechanistically paradoxical scenario: calcium acetate is a known causative agent for calcium-alkali syndrome, not a treatment candidate. With an evidence level of L5 (model prediction only), zero supporting clinical trials, zero supporting publications, and no SAHPRA registration, there is currently no basis to advance this candidate.

**To proceed, the following would be needed:**

- **Mechanistic clarification:** An independent pharmacological review to determine whether any credible therapeutic (rather than causative) role for calcium acetate in calcium-alkali syndrome has ever been proposed in the scientific literature
- **MOA data retrieval:** Query DrugBank API for the full mechanism of action profile (Data Gap DG002)
- **Safety profile retrieval:** Obtain the SAHPRA-equivalent Professional Information document to assess contraindications and warnings (Data Gap DG001)
- **Pharmacovigilance audit:** Review whether the TxGNN knowledge graph edge between this drug and this disease originates from adverse event/spontaneous reporting data rather than clinical efficacy data — if confirmed, flag the prediction as a false positive and exclude from further development
- **SAHPRA Section 21 pathway:** If any exploratory investigation is nonetheless contemplated, SAHPRA unregistered medicines authorisation must be obtained in advance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

