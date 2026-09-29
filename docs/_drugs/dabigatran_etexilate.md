---
layout: default
title: Dabigatran Etexilate
parent: Model Prediction Only (L5)
nav_order: 160
evidence_level: L5
indication_count: 10
---

# Dabigatran Etexilate
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

# Dabigatran Etexilate: From Anticoagulation to Sclerosing Cholangitis

## One-Sentence Summary

Dabigatran etexilate is an oral direct thrombin inhibitor, an anticoagulant used for thromboembolic conditions. The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but there are **0 clinical trials** and **1 publication**, and that publication is not efficacy evidence. This is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anticoagulation (thromboembolic disease). The SAHPRA registration records in the pack contain no indication text. |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Dabigatran etexilate is an oral anticoagulant that acts through direct thrombin inhibition. Its efficacy in thromboembolic disease is established, but no data link this mechanism to a biliary disease.

The evidence pack finds no clear mechanistic link between dabigatran and sclerosing cholangitis. The high TxGNN score reflects a graph-based association, not clinical support. The only retrieved paper is a drug-drug interaction study of cilofexor, an FXR agonist in development for primary sclerosing cholangitis. It does not evaluate dabigatran as a treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36906733](https://pubmed.ncbi.nlm.nih.gov/36906733/) | 2023 | DDI evaluation (pharmacokinetic) | Clin Pharmacokinet | CYP450 and transporter-mediated drug interaction potential of cilofexor, an FXR agonist in development for primary sclerosing cholangitis. It is not efficacy evidence for dabigatran. |

---

## South Africa Market Information

Both registrations are oral capsules. The records in the pack do not include approved indication text or Essential Medicines List (EML) status.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 56/8.2/0690.687 | Dabitrin 110Mg | Capsule | Not stated in registry record |
| Reg. No. 56/8.2/0695 | Dabigatran 75 Drl | Capsule | Not stated in registry record |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials and no relevant literature. Nothing supports a mechanism in sclerosing cholangitis. Safety data from the SAHPRA package insert are also missing, which blocks progression to safety screening.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (download and parse the PI PDF from the SAHPRA website)
- Mechanism of action data (query the DrugBank API)
- A plausible mechanistic hypothesis for a role in cholestatic disease, supported by preclinical data
- The registered indication text for each SAHPRA licence

**Note on other predictions:** Across the other predicted indications for this drug, only rheumatoid arthritis has a biologically coherent signal. A rat study (PMID 36142208) reports benefit via the kallikrein-kinin system. It is animal data only and would be a research question, not a repurposing decision. The rest are model-only or reflect co-prescription rather than therapeutic effect.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

