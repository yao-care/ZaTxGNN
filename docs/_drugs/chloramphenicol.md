---
layout: default
title: Chloramphenicol
parent: Model Prediction Only (L5)
nav_order: 111
evidence_level: L5
indication_count: 10
---

# Chloramphenicol
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

# Chloramphenicol: From Broad-Spectrum Antibacterial to Conjunctivitis

## One-Sentence Summary

Chloramphenicol is a broad-spectrum bacteriostatic antibiotic, and it is already marketed in South Africa in ophthalmic and other topical products.
The TxGNN model predicts it may be effective for **conjunctivitis**, with a score of 99.66%.
No clinical trials or publications currently support this indication, so the prediction rests on the model alone. Because topical eye use is already established, it may not be true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

The SAHPRA records supplied contain no approved indication text, so the original indication is not shown.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from DrugBank. Chloramphenicol is generally described as a bacteriostatic antibiotic that inhibits the bacterial 50S ribosomal subunit, and this mechanism fits bacterial conjunctivitis.

Topical ophthalmic use of chloramphenicol is a well-established existing use, and one registered South African product is an eye ointment. The prediction may therefore reflect a use that is already established rather than a new one.

Because the original indication field is empty, we cannot assess how far conjunctivitis differs from the labelled indications. The prediction should be read as a plausible mechanism match, not as evidence of a new therapeutic use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. V/15.1/294 | Chlorphen 3.5g | Eye ointment |
| Reg. No. H1278 (OM) | Spersadex comp 5ml | Drops |
| Reg. No. H1236 (OM) | Covomycin 7.5ml | "Een" (as recorded) |
| Reg. No. H1237 (OM) | Covomycin D | "Een" (as recorded) |

Only Chlorphen 3.5g is recorded as an ophthalmic dosage form. The other three entries are not classified as ophthalmic in the register data, so their suitability for eye use needs checking against the Professional Information (PI).

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

A drug interaction query returned no results.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The conjunctivitis prediction has no supporting trials or literature (L5), and topical ophthalmic chloramphenicol is already a registered use, so this is not clearly repurposing. Safety information is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- SAHPRA PI warnings and contraindications for each registered product, downloaded and parsed
- The SAHPRA-approved indications for each product, to confirm whether conjunctivitis is already labelled
- Mechanism of action data from DrugBank
- Any interventional trials or clinical literature on chloramphenicol in conjunctivitis
- Ophthalmic route confirmation for the products not recorded as eye formulations

**Other predictions:** The model's other top predictions (scleroderma, post-infectious vasculitis, Chagas cardiomyopathy and others) have no supporting evidence, and some are contradicted by it. The "post-bacterial disorder" prediction has one possible lead, a Phase 2/3 rickettsial clearance study ([NCT05972772](https://clinicaltrials.gov/study/NCT05972772)). Whether chloramphenicol is an arm of that trial has not been verified.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

