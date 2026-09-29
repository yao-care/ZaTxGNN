---
layout: default
title: Sulfadoxine
parent: Model Prediction Only (L5)
nav_order: 425
evidence_level: L5
indication_count: 10
---

# Sulfadoxine
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

# Sulfadoxine: From Malaria (Fansidar) to Gout

## One-Sentence Summary

Sulfadoxine is a long-acting sulfonamide antifolate, registered in South Africa as the tablet product Fansidar.
The TxGNN model predicts it may be effective for **gout** (score 99.10%), but **no clinical trials and no supporting publications** were found for this direction.
This is a model-only prediction with no plausible mechanism, so it should be treated as a likely graph artefact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA record; Fansidar is a sulfadoxine-pyrimethamine antimalarial (malaria) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 99.10% (rank 4,455) |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Sulfadoxine is a sulfonamide antifolate that inhibits dihydropteroate synthase (DHPS), a pathway central to folate synthesis in microbes and malaria parasites. It has no known effect on urate metabolism.

Gout is a disorder of uric acid metabolism and crystal-driven inflammation. It has no biological relationship to malaria or to antifolate antimicrobial activity. The high TxGNN score most likely reflects connections in the knowledge graph rather than a real pharmacological link. A related obsolete "hyperuricemia" term also appears in the predictions, which supports the artefact interpretation.

**Conclusion:** no plausible mechanistic rationale can be identified for gout.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR or PACTR).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22285617](https://pubmed.ncbi.nlm.nih.gov/22285617/) | 2012 | Case series | J Am Acad Dermatol | Five years of toxic epidermal necrolysis (TEN) treatment experience in a burn unit. It is a drug-eruption paper and does not evaluate sulfadoxine for gout, so it is likely a keyword match and offers no efficacy support. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| K/20.2.6/68 | Fansidar | Tablet (oral) | Not listed in the retrieved record |

---

## Safety Considerations

The SAHPRA package insert warnings and contraindications could not be retrieved, and no drug-interaction records were found. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Signals from the retrieved literature and predictions, which are not a substitute for the PI:
- **Severe skin reactions:** Publications on other predicted indications report Stevens-Johnson syndrome and toxic epidermal necrolysis, with serious ocular sequelae, after sulfadoxine-pyrimethamine.
- **Renal risk:** Sulfonamides carry crystalluria and nephrotoxicity risk. This matters for any use in renally impaired patients.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The gout prediction rests on the model score alone, with no trials, no relevant literature and no plausible mechanism. Sulfadoxine also carries known serious skin and renal safety risks, which weigh against exploring it for a non-infectious indication.

**Other predictions reviewed (none support progression):**
- **Conjunctivitis** is the only prediction with any historical signal. Sulfadoxine (Ro 4-4393) was studied in the 1960s as intermittent systemic therapy for trachoma, but design and outcomes are unverified and azithromycin is now standard. It is best treated as a research question rather than a repurposing candidate.
- **Bronchitis, peritonitis and appendicitis:** antibacterial activity is theoretically relevant, but no sulfadoxine studies were found.
- **Diabetic nephropathy:** no supporting evidence, and a renal safety concern.
- **Genetic and metabolic disorders** (brain small vessel disease, the hematuria-retinal syndrome, Lesch-Nyhan syndrome): no plausible mechanism.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings and contraindications), which is a blocking gap for safety screening.
- Mechanism of action data from DrugBank.
- Any mechanistic or preclinical evidence linking sulfadoxine to urate metabolism. Without it, no further evaluation for gout is warranted.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

