---
layout: default
title: Icodextrin
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 10
---

# Icodextrin
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

# Icodextrin: From Peritoneal Dialysis to Irritable Bowel Syndrome

## One-Sentence Summary

Icodextrin is a high-molecular-weight glucose polymer osmotic agent, best known internationally for its use in peritoneal dialysis solutions (brand names: Extraneal, Adept) and post-surgical adhesion prevention — however, it holds **no current SAHPRA registration** in South Africa.
The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome (IBS)**, based primarily on its osmotic and gut-microbiome-modulating properties.
This prediction is currently supported by **0 clinical trials** and **0 publications**, placing it at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in South Africa; internationally used as peritoneal dialysis osmotic agent (Extraneal) and post-surgical adhesion prevention (Adept) |
| Predicted New Indication | Irritable Bowel Syndrome (IBS) |
| TxGNN Prediction Score | 98.53% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this Evidence Pack. Based on known pharmacological information, Icodextrin is a starch-derived glucose polymer (molecular weight ~16,800 Da). Its primary clinical utility derives from two osmotic properties: in peritoneal dialysis, it creates a sustained oncotic gradient across the peritoneal membrane, enabling prolonged ultrafiltration during long dwell times; in gynaecological surgery (Adept), it acts as a viscous hydroflotation agent to separate tissue surfaces and reduce post-surgical adhesion formation.

The mechanistic rationale for IBS rests on two theoretical pillars. First, Icodextrin's constituent oligosaccharides (including maltose and short-chain glucose polymers produced during metabolism) could theoretically function as prebiotic substrates, modulating gut microbiota composition in a manner analogous to fructo-oligosaccharides. Second, its osmotic properties conceptually parallel those of osmotic laxatives such as polyethylene glycol (PEG), which are established treatments for certain IBS subtypes (IBS-C). These two properties together may have prompted the TxGNN knowledge graph to associate Icodextrin with IBS.

However, a fundamental and likely insurmountable obstacle exists: Icodextrin is not formulated for oral administration. It is administered intraperitoneally (peritoneal dialysis) or intrauterinely (adhesion prevention). Repurposing for IBS would require a completely novel oral dosage form and safety/bioavailability profile that has not been explored. The IBS connection remains a computational inference at the model-prediction-only tier, with no supporting experimental, clinical, or observational evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Icodextrin in irritable bowel syndrome.

---

## Literature Evidence

Currently no related literature available for Icodextrin in irritable bowel syndrome.

---

## South Africa Market Information

Icodextrin holds **no current SAHPRA registrations**. The drug is not available on the South African market as a registered product. Healthcare professionals should note:

- The drug is not listed on the South African Essential Medicines List (EML).
- Any future use would require SAHPRA Section 21 authorisation (unregistered medicine) or a full registration application.
- Internationally registered formulations include Extraneal (peritoneal dialysis solution, Baxter) and Adept (adhesion-reduction solution, Hana Biosciences/Baxter), neither of which is registered in South Africa.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. As Icodextrin is not currently registered with SAHPRA, prescribers should consult the manufacturer's international prescribing information (Extraneal or Adept PI) and international pharmacovigilance databases prior to any use. Report adverse drug reactions to SAHPRA via the MedSafety reporting portal.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is currently zero clinical or preclinical evidence supporting Icodextrin for irritable bowel syndrome, and a fundamental route-of-administration incompatibility exists — the drug is not available in oral form. The TxGNN score of 98.53% reflects computational graph topology rather than translatable biological plausibility, and the drug is not registered in South Africa, adding a substantial regulatory barrier before any clinical application could be considered.

**To proceed, the following would be needed:**

- **Preclinical proof of concept:** In vitro and animal studies demonstrating that Icodextrin (or its metabolites in oral form) modulates gut microbiota or intestinal motility in an IBS-relevant model.
- **Oral formulation feasibility:** Pharmaceutical studies to determine whether an oral form is safe, bioavailable, and metabolically distinct from existing osmotic agents (e.g., PEG 3350, lactulose).
- **Mechanism of action clarification:** Full DrugBank MOA data and pharmacodynamic characterisation via DrugBank API query (DG002 remediation).
- **Safety data retrieval:** Full SAHPRA/international PI warnings and contraindications (DG001 remediation), including known adverse effects in PD patients (hypersensitivity reactions, false glucose meter readings with maltose-sensitive devices, sterile peritonitis).
- **SAHPRA regulatory pathway:** Assessment of Section 21 or full registration requirements before any human use in South Africa.

> ⚠️ **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All predictions are generated by the TxGNN computational model and must be interpreted in the context of clinical evidence and regulatory requirements.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

