---
layout: default
title: Cilazapril
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 4
---

# Cilazapril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Cilazapril: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Cilazapril is an angiotensin-converting enzyme (ACE) inhibitor belonging to a well-established drug class used in the treatment of hypertension and heart failure.
The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism**,
with **0 clinical trials** and **0 publications** currently supporting this specific direction.
Evidence is limited to model prediction alone, placing this candidate at Evidence Level L5.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / Heart failure (ACE inhibitor class; no SAHPRA registration on record) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Cilazapril is not available in this Evidence Pack. Based on known information, Cilazapril belongs to the ACE (angiotensin-converting enzyme) inhibitor class. ACE inhibitors work by blocking the conversion of Angiotensin I to Angiotensin II — a potent vasoconstrictor — thereby reducing systemic vascular resistance, lowering blood pressure, and attenuating vascular remodelling. Their efficacy in systemic hypertension and heart failure is supported by decades of clinical evidence across multiple drug class members (e.g. enalapril, ramipril, lisinopril).

The theoretical rationale for exploring Cilazapril in pulmonary hypertension rests on the known contribution of the renin-angiotensin-aldosterone system (RAAS) to pulmonary vascular pathology. Angiotensin II promotes pulmonary vasoconstriction and fibrotic remodelling of the pulmonary vasculature, both of which are hallmarks of pulmonary arterial hypertension. ACE inhibitors could, in principle, interrupt this pathological cycle and reduce pulmonary vascular resistance.

However, the specific subtype targeted here — **pulmonary hypertension with unclear multifactorial mechanism** — presents a significant mechanistic barrier. By definition, the underlying drivers of this subtype remain poorly characterised, and there is currently no validated biomarker evidence confirming that RAAS overactivation is a dominant pathway. The mechanistic link between Cilazapril and this indication therefore represents an indirect, theoretical inference rather than a well-supported biological hypothesis. This substantially limits confidence in the prediction at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Cilazapril is **not currently marketed in South Africa**. No product registrations are held with SAHPRA (South African Health Products Regulatory Authority), and the drug does not appear on the current Essential Medicines List (EML). Prescribers wishing to use this agent would need to explore Section 21 (unregistered medicine) authorisation pathways under the Medicines and Related Substances Act.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. As Cilazapril is not currently registered in South Africa, clinicians should consult the full manufacturer prescribing information from a jurisdiction where the drug is registered (e.g. the European Medicines Agency or Health Canada monograph). Report any adverse drug reactions to SAHPRA via the MedSafety reporting portal.

> **Note for ACE inhibitor class:** As a class effect, ACE inhibitors carry well-known safety considerations including the risk of first-dose hypotension, hyperkalaemia, acute kidney injury (particularly in patients with bilateral renal artery stenosis or volume depletion), and ACE inhibitor-induced cough and angioedema. These class effects are especially relevant given the proposed repurposing target involves both pulmonary and renal vascular disease. Detailed drug-specific data for Cilazapril was not available in this Evidence Pack and must be verified before any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or published literature evidence supporting the use of Cilazapril specifically for pulmonary hypertension with unclear multifactorial mechanism. The current evidence base consists solely of a TxGNN computational model prediction (Evidence Level L5), and the proposed mechanistic link is theoretical, weakly supported, and complicated by the undefined pathological basis of this pulmonary hypertension subtype.

**To proceed, the following is needed:**

- **MOA data gap closure:** Retrieve full Cilazapril mechanism of action from the DrugBank API to enable a robust mechanistic plausibility assessment
- **Regulatory safety review:** Obtain and parse the full prescribing information (PI/SmPC) from a jurisdiction where Cilazapril is approved to characterise warnings, contraindications, and drug interactions
- **Patient population biomarker profiling:** Identify whether RAAS biomarkers (e.g. elevated plasma renin activity, elevated ACE levels) are measurable and elevated in patients with this multifactorial pulmonary hypertension subtype — this is the minimum biological prerequisite to justify further investigation
- **Broader ACE inhibitor class evidence review:** Conduct a targeted literature search across the ACE inhibitor class (enalapril, ramipril) in pulmonary hypertension to determine whether any class-level signal exists before attributing a drug-specific prediction
- **Regulatory feasibility check:** Assess SAHPRA Section 21 authorisation requirements given the complete absence of local registration
- **DDI assessment:** Perform a drug-drug interaction review, particularly relevant if target patients are on established pulmonary hypertension therapies (e.g. phosphodiesterase-5 inhibitors, endothelin receptor antagonists)

---

*This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All content should be reviewed by a qualified healthcare professional in the context of individual patient care.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

