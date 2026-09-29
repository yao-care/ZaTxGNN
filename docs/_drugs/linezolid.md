---
layout: default
title: Linezolid
parent: Model Prediction Only (L5)
nav_order: 296
evidence_level: L5
indication_count: 10
---

# Linezolid
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

# Linezolid: From Gram-Positive Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Linezolid is an oxazolidinone antibiotic used against resistant Gram-positive bacterial infections. The SAHPRA records supplied do not include approved-indication text, so this describes the drug class rather than the registered wording.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but **0 clinical trials** and **0 publications** support this prediction, and no plausible mechanism links the two.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 92.45% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Linezolid is known to be an oxazolidinone that blocks bacterial protein synthesis by binding the 50S ribosomal subunit. This makes it an antibacterial agent.

Polyclonal hyperviscosity syndrome is a condition of raised serum viscosity linked to excess immunoglobulins. Linezolid has no known effect on serum viscosity or immunoglobulin levels, so no plausible mechanistic link could be identified. The high TxGNN score (0.92) reflects a pattern in the knowledge graph, not biological or clinical evidence, and should not be read as a treatment signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 35/20.1.1/0312 | Zyvoxid 200Mg/100Ml | Injection |
| Reg. No. 48/20.1.1/0223 | Linezolid specpharm | Tablet |
| Reg. No. 50/20.1.1/0184 | Zenilid Iv 600 Mg/300 Ml | Infusion |

Both oral (tablet) and intravenous (injection, infusion) presentations are registered.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The Evidence Pack contains no drug interaction records for linezolid. Separately, the prediction-level notes flag two known risks of prolonged linezolid use that matter for any haematology-related use: myelosuppression, and peripheral and optic neuropathy.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph-based score alone, with no trials, no literature and no plausible mechanism. Linezolid's known myelosuppressive potential adds a safety concern in patients with haematological disorders.

**To proceed, the following is needed:**
- Mechanism of action data (currently missing) and a defensible biological rationale linking linezolid to serum viscosity or immunoglobulin biology
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Any clinical or preclinical study specific to this condition

**Other predictions for this drug:** Of the 10 predicted indications, only **pyelonephritis** reached the next screening stage (evidence level L4, "Research Question"). The support is indirect. Linezolid is active against resistant Gram-positive urinary pathogens such as vancomycin-resistant enterococci, but most pyelonephritis is caused by Gram-negative bacteria, against which it is inactive. A pathogen-restricted question (resistant Gram-positive pyelonephritis or urinary tract infection) is more defensible than pyelonephritis in general. The other predictions, including hyperamylasemia and hematological disease with peripheral neuropathy, may reflect adverse-effect signals rather than treatment opportunities.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

