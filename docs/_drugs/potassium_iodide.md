---
layout: default
title: Potassium Iodide
parent: Model Prediction Only (L5)
nav_order: 378
evidence_level: L5
indication_count: 10
---

# Potassium Iodide
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

# Potassium Iodide: From Parenteral Trace Element Products to Nasal Cavity Disease

## One-Sentence Summary

Potassium iodide (KI) is registered in South Africa as an ingredient of three infusion products (Peditrace, Addaven and Nutryelt), whose names suggest parenteral trace-element supplementation. The registered indication text was not supplied. The TxGNN model predicts it may be useful for **nasal cavity disease**, but there are **0 clinical trials** and only **4 case reports** (3 veterinary, 1 human), so the evidence is anecdotal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not supplied in the SAHPRA records |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 (case-report level only; no trials) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. KI is a long-established iodide salt. In the retrieved literature it has been used empirically against fungal and fungus-like infections, which is the only plausible link to nasal disease in this data.

The four case reports describe KI given for rhinofacial pythiosis in sheep, mycotic rhinitis in a horse, and a *Pseudallescheria boydii* nasal infection in a horse (as sodium iodide IV, alongside miconazole). The one human report is a nasofacial zygomycosis case that responded rapidly to KI. The pattern is infectious or fungal nasal disease, not nasal disease in general.

The TxGNN score is very high (99.95%), but a model score is not clinical evidence. The prediction should be treated as a research question, not a treatment recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34902797](https://pubmed.ncbi.nlm.nih.gov/34902797/) | 2022 | Case report (veterinary) | J Mycol Med | Successful KI treatment of rhinofacial pythiosis in sheep |
| [39576399](https://pubmed.ncbi.nlm.nih.gov/39576399/) | 2024 | Case report (veterinary) | Vet Res Commun | Mycotic rhinitis (*Aspergillus fumigatus*) in a mare treated with topical clotrimazole plus oral KI |
| [10976304](https://pubmed.ncbi.nlm.nih.gov/10976304/) | 2000 | Case report (veterinary) | J Am Vet Med Assoc | *Pseudallescheria boydii* nasal cavity infection in a horse; treated with intranasal miconazole and IV sodium iodide |
| [7997795](https://pubmed.ncbi.nlm.nih.gov/7997795/) | 1994 | Case report (human) | Rev Inst Med Trop Sao Paulo | Nasofacial zygomycosis in a 64-year-old woman with rapid response to KI |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 29/24/0462 | Peditrace 10ml pdp100010 | Infusion |
| Reg. No. 49/24/0996 | Addaven | Infusion |
| Reg. No. 52/24/0031 | Nutryelt | Infusion |

All three are injectable infusions. No intranasal or oral KI products appear in the registrations supplied, so the route used in the case reports (oral or topical) is not covered by any listed product.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Two safety signals appeared in the retrieved literature for other predicted indications and are relevant to any repurposing use:
- **Iodide hypersensitivity** is a known adverse reaction.
- A 1972 case report describes **congenital goiter after maternal iodide ingestion**, which is relevant to use in pregnancy.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is four case reports, mostly veterinary, in fungal nasal infections, with no clinical trials. A high model score alone does not justify moving forward, and the SAHPRA safety information has not yet been reviewed.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications, which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- The registered indication text for the three infusion products
- A clear target: fungal (e.g. zygomycosis, sporotrichosis-type) versus non-infectious nasal disease
- Human clinical evidence for the nasal indication, since no trials are currently registered
- A route-compatibility assessment, because the registered products are infusions only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

