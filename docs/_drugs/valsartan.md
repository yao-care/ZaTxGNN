---
layout: default
title: Valsartan
parent: 僅模型預測 (L5)
nav_order: 456
evidence_level: L5
indication_count: 7
---

# Valsartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Valsartan: Evaluating Malignant Hypertensive Renal Disease as a New Indication

## One-Sentence Summary

Valsartan (DrugBank DB00177) is a well-established angiotensin II receptor blocker (ARB); however, this evidence pack does not contain documented original-indication text or mechanism-of-action data for this candidate, and the drug is currently **not marketed in South Africa** (0 SAHPRA registrations). The TxGNN model's top-ranked prediction is **Malignant Hypertensive Renal Disease**, but the only supporting literature discusses a different drug (avosentan, an endothelin receptor antagonist), so direct evidence for valsartan in this indication is currently minimal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no indication text or MOA provided in evidence pack (data gap, see DG002) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for this candidate is not available in the evidence pack (original_moa: data gap). Based on the pharmacological class information captured in the repurposing rationale, valsartan is an angiotensin II type 1 (AT1) receptor blocker (ARB) — a class that forms the standard of care for renal-protective therapy in hypertensive kidney disease, acting by lowering intraglomerular pressure and reducing proteinuria. This provides a plausible mechanistic rationale for a role in malignant hypertensive renal disease.

However, the only literature citation retrieved for this specific indication (PMID 24368192) studies **avosentan**, an endothelin receptor antagonist, not valsartan or any ARB. It is a disease-model (rat) study, not a clinical trial, and does not test the drug under evaluation. It should therefore be read as indirect support for the disease model (hypertensive nephropathy), not as direct evidence for valsartan's efficacy in this indication.

No clinical trials of valsartan in malignant hypertensive renal disease were identified in this search.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Preclinical/Animal (avosentan, not valsartan) | Pharmacological research | In a rat model of hypertensive nephropathy, avosentan (an endothelin receptor antagonist) was renoprotective at doses that did not cause fluid retention. Note: this study does not involve valsartan or the ARB class. |

---

## South Africa Market Information

Valsartan currently has **no SAHPRA product registrations** recorded in this evidence pack (market status: not marketed; total licenses: 0). No product-level data (registration number, dosage form, approved indication text) is available for South Africa.

---

## Safety Considerations

A blocking data gap (DG001) means no SAHPRA-approved Professional Information (warnings, contraindications) or drug-interaction data is currently available for this candidate — this precludes even an initial (S1) safety screening.

Please refer to the SAHPRA-approved Professional Information (PI) for safety information once available. Report adverse drug reactions to SAHPRA.

---

## Other Candidates in This Evidence Pack

This evidence pack evaluated valsartan against 7 predicted indications. The top-ranked one (above) has the weakest direct evidence of the set. One candidate further down the TxGNN ranking shows notably stronger, drug-specific support and may warrant a dedicated evaluation:

| Rank | Predicted Indication | Evidence Level | Decision Stage | Recommendation | Key Support |
|------|----------------------|-----------------|-----------------|-----------------|--------------|
| 6 | Chronic pulmonary heart disease (cor pulmonale) | L2 | S2 | Proceed with Guardrails | 7 clinical trials incl. a completed Phase 4 RCT (NCT02768298, sacubitril/valsartan vs. enalapril, N=201) and 20 literature items on sacubitril/valsartan in HFrEF with COPD/pulmonary comorbidity |
| 2 | Malignant renovascular hypertension | L4 | S1 | Research Question | Class-effect preclinical study directly on AT1 blockade (PMID 11560862), but no human trials |

Indications ranked 3, 4, 5, and 7 (pulmonary hypertension subtypes, Braddock syndrome, Prinzmetal angina) had either no relevant literature/trials or literature judged unrelated to valsartan's mechanism, and are not recommended for further evaluation at this time.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (malignant hypertensive renal disease) rests on a high TxGNN score but only one indirect, non-valsartan preclinical citation, with no clinical trials. A blocking data gap (missing SAHPRA PI/warnings/contraindications) also prevents the initial safety screening required before this candidate can advance.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings, contraindications, DDI) to clear the S1 safety gate
- Original indication and mechanism-of-action documentation for valsartan (currently absent from the evidence pack)
- Valsartan/ARB-class-specific preclinical or clinical data in malignant hypertensive renal disease, rather than reliance on an endothelin-antagonist study
- If prioritization is needed across candidates, consider redirecting evaluation effort toward **chronic pulmonary heart disease**, which already has Phase 4 RCT-level, drug-relevant evidence (sacubitril/valsartan)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

