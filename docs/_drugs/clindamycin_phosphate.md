---
layout: default
title: Clindamycin Phosphate
parent: 僅模型預測 (L5)
nav_order: 129
evidence_level: L5
indication_count: 0
---

# Clindamycin Phosphate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Clindamycin Phosphate: Repurposing Evaluation — Insufficient Data to Proceed

---

## One-Sentence Summary

Clindamycin phosphate is a lincosamide antibiotic prodrug, rapidly hydrolysed in vivo to clindamycin, and widely used for bacterial infections including acne vulgaris, bacterial vaginosis, and serious anaerobic infections.
The current Evidence Pack contains **no TxGNN repurposing predictions**, no SAHPRA registration records, and multiple blocking data gaps.
This evaluation **cannot advance to a full repurposing analysis** until the identified gaps are remediated.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (acne vulgaris, bacterial vaginosis, anaerobic/serious soft-tissue infections) |
| Predicted New Indication | Not available — `predicted_indications` array is empty |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not determinable (no predictions present) |
| South Africa Market Status | Not marketed (0 SAHPRA registrations recorded) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN predictions are present in this Evidence Pack, so a mechanism-based repurposing rationale for a specific new indication cannot be evaluated at this stage.

What is known about the drug itself: clindamycin phosphate is the phosphate ester prodrug of clindamycin. After administration — whether intravenous, intramuscular, or topical — it is rapidly dephosphorylated to the active moiety clindamycin. Clindamycin binds to the 50S ribosomal subunit of susceptible bacteria, blocking translocation and inhibiting peptide bond formation. This mechanism is effective against Gram-positive cocci, anaerobes, and certain protozoa (e.g., *Plasmodium falciparum* in combination regimens).

Beyond direct antibacterial activity, clindamycin has documented anti-inflammatory effects that have been explored in inflammatory dermatological conditions. Some early-phase research has also investigated its potential in protozoan infections and, mechanistically, in oncology-adjacent contexts — however, without TxGNN model output in the current pack, no specific repurposing target can be assessed or recommended.

> **Note on SAHPRA registrations:** The Evidence Pack records zero SAHPRA registrations. In practice, clindamycin-containing products (capsules, injectables, topical gels/solutions) are widely registered and used in South Africa. The zero-registration finding most likely reflects a data retrieval gap rather than a genuine absence from the South African market. Direct verification against the SAHPRA Product Register is strongly recommended before drawing regulatory conclusions.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered in this Evidence Pack.

---

## Literature Evidence

Currently no related literature is available in this Evidence Pack.

---

## South Africa Market Information

No SAHPRA-registered products were returned for Clindamycin Phosphate in the current Evidence Pack. See the note above regarding likely data retrieval issues.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA via the MedSafety online portal.

Key safety domains to verify when the PI is retrieved include:
- **Antibiotic-associated colitis / *Clostridioides difficile*-associated diarrhoea** — a class-level concern for all lincosamides
- **Hypersensitivity reactions** — cross-reactivity with lincomycin
- **Neuromuscular blockade potentiation** — relevant in surgical and ICU settings
- **Pregnancy and lactation cautions**

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack contains no TxGNN repurposing predictions, no mechanism of action data, no SAHPRA regulatory records, and no safety information — all of which are prerequisites for a meaningful repurposing evaluation. Proceeding without these inputs would produce conclusions with no evidentiary basis.

**To proceed, the following is needed:**

- [ ] **TxGNN model run** — resubmit with a confirmed DrugBank ID so that `predicted_indications` can be populated
- [ ] **DrugBank ID resolution** — `drugbank_id` is currently null; confirm whether the correct entry is DB00268 (clindamycin) or a separate phosphate-specific record
- [ ] **MOA data retrieval** — query DrugBank API once the DrugBank ID is confirmed (Data Gap DG002)
- [ ] **SAHPRA Product Register verification** — manually search [SAHPRA Product Search](https://www.sahpra.org.za/) for "clindamycin" and "clindamycin phosphate" to obtain accurate registration numbers and approved indications
- [ ] **Professional Information (PI) retrieval** — download and parse the SAHPRA-approved PI PDF to populate warnings and contraindications (Data Gap DG001, severity: Blocking)
- [ ] **DDI data** — once DrugBank ID is confirmed, requery the DrugBank interaction database

---

*This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require prospective clinical validation before therapeutic application. All predictions and analyses must be interpreted by qualified healthcare professionals.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

