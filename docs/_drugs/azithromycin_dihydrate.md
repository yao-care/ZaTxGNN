---
layout: default
title: Azithromycin Dihydrate
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 0
---

# Azithromycin Dihydrate
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

# Azithromycin Dihydrate: Evaluation Report — Incomplete Evidence Pack

## One-Sentence Summary

Azithromycin dihydrate is a broad-spectrum macrolide antibiotic (azalide subclass) widely used in treating bacterial infections, including community-acquired pneumonia, sexually transmitted infections, and skin infections.
**This Evidence Pack is critically incomplete**: no TxGNN drug repurposing predictions were generated, and both regulatory and safety data are absent, preventing a meaningful evaluation.
A **Hold** decision is recommended until all identified data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections — respiratory, STI, skin (based on pharmacological class; no SAHPRA record retrieved in this pack) |
| Predicted New Indication | None — TxGNN predictions not generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | Not assessable |
| South Africa Market Status | Not found in this dataset (see note below) |
| Number of SAHPRA Registrations | 0 (likely a data retrieval failure — see note) |
| Recommended Decision | **Hold** |

> **⚠️ Important Note on Market Status**: The Evidence Pack reports 0 SAHPRA registrations and "not marketed" status for Azithromycin. This is almost certainly a **data collection failure**, not the true regulatory situation. Azithromycin is a well-established antibiotic that appears on the South African Standard Treatment Guidelines and Essential Medicines List (EML). Direct SAHPRA database verification is required before this field can be relied upon.

---

## Why No Prediction Was Generated

The `predicted_indications` array in this Evidence Pack is **empty**. This prevents the core repurposing analysis from proceeding. There are two likely causes:

1. **Missing DrugBank ID**: The field `drugbank_id` is `null`. The TxGNN knowledge graph uses DrugBank IDs as the primary node identifier. Without one, the model cannot locate the drug within the graph and therefore cannot generate repurposing candidates.

2. **Salt form mismatch**: The submitted query used `"AZITHROMYCIN DIHYDRATE"` (a specific salt/hydrate form). The knowledge graph likely indexes this compound under its INN `"Azithromycin"` (DrugBank: **DB00207**). A simple name normalisation mismatch may be causing the lookup to fail.

**Recommended fix**: Confirm DrugBank ID as **DB00207**, update the candidate record, and re-run the TxGNN prediction pipeline.

---

## Why This Prediction Would Be Pharmacologically Reasonable (Background)

Even without TxGNN output, Azithromycin is an active drug repurposing research target. For context when re-running the pipeline:

Azithromycin inhibits bacterial protein synthesis by binding to the **50S ribosomal subunit** (23S rRNA), blocking peptide translocation. Beyond its bacteriostatic/bactericidal activity, it exhibits well-documented **immunomodulatory and anti-inflammatory effects** — reducing pro-inflammatory cytokines (IL-6, IL-8, TNF-α), modulating neutrophil function, and inhibiting biofilm formation. These properties have prompted investigation in non-infectious conditions.

Its original indication in bacterial infection overlaps mechanistically with conditions driven by dysregulated inflammation and microbial-host interaction, which is why the TxGNN model would be expected to generate predictions in areas such as respiratory inflammatory disease, autoimmune conditions, and protozoal infections once the pipeline runs correctly.

---

## Safety Considerations

Safety data were not retrieved in this Evidence Pack. Two gaps are flagged:

| Data Gap ID | Item | Severity | Impact |
|-------------|------|----------|--------|
| DG001 | SAHPRA-approved PI — warnings and contraindications | **Blocking** | Cannot complete safety screening |
| DG002 | Mechanism of Action (MOA) from DrugBank | High | Cannot complete mechanistic rationale analysis |

Please refer to the **SAHPRA-approved Professional Information (PI)** for full safety information. Report adverse drug reactions to SAHPRA via the MedWatch SA platform.

Key safety areas to review when PI is retrieved include: QTc prolongation risk, hepatotoxicity, drug-drug interactions (particularly with other QT-prolonging agents and anticoagulants), and contraindications in patients with macrolide hypersensitivity.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN predictions were generated due to a missing DrugBank ID, and both safety and SAHPRA regulatory data are absent. There is insufficient information to evaluate this candidate for repurposing at this time.

**To proceed, the following is needed:**

- [ ] **Confirm DrugBank ID** as DB00207 ("Azithromycin") and re-run TxGNN prediction pipeline with the correct identifier
- [ ] **Retrieve SAHPRA registration records** directly from the [SAHPRA online portal](https://www.sahpra.org.za/) to establish true South African market status
- [ ] **Obtain and parse the SAHPRA-approved PI** to populate warnings, contraindications, and MOA fields (resolves DG001 and DG002)
- [ ] **Verify EML status** and confirm alignment with current South African Standard Treatment Guidelines
- [ ] **Re-submit Evidence Pack** once drug name normalisation (INN vs. salt form) is resolved at the data ingestion layer to prevent similar lookup failures for other dihydrate/salt-form submissions

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. This evaluation was prepared in accordance with YMYL standards for South African healthcare professionals.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

