---
layout: default
title: Levofloxacin
parent: Moderate Evidence (L3-L4)
nav_order: 292
evidence_level: L4
indication_count: 10
---

# Levofloxacin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Levofloxacin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Levofloxacin is a broad-spectrum fluoroquinolone antibiotic, used to treat bacterial infections.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but the evidence is very thin: **0 clinical trials** and **1 publication**, an outbreak report that does not test levofloxacin. The mechanism is not plausible for the organism described in that report, so this prediction should be treated as a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (general antibacterial use; the SAHPRA registration records provided contain no indication text) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Levofloxacin kills bacteria by inhibiting DNA gyrase and topoisomerase IV. Detailed mechanism-of-action data are not available in the DrugBank record supplied, so this description reflects the known pharmacology of the fluoroquinolone class.

The only linked paper describes an outbreak of **microsporidial** keratoconjunctivitis linked to swimming pool water in Taiwan. Microsporidia are eukaryotic organisms, not bacteria, and are not a recognised target of fluoroquinolones. Any benefit would be indirect, for example covering a bacterial co-infection of the eye. Nothing in the data shows this.

The high TxGNN score (99.92%) is therefore not backed by a plausible pharmacological rationale. It probably reflects proximity in the knowledge graph rather than demonstrated benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Outbreak report | American Journal of Ophthalmology | Reports an outbreak of microsporidial keratoconjunctivitis linked to water contamination in swimming pools in Taiwan. It does not evaluate levofloxacin as a treatment. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 44/20.1.1/0249 | Zybact 250 Mg | Tablet | Not stated in the registration data |
| A39/20.1.1/0578 | Levofloxacin-winthrop IV sol for infusion | Infusion | Not stated in the registration data |
| 42/20.1.1/0632 | Lintrip 250 | Tablet | Not stated in the registration data |
| 46/20.1.1/0978 | Levojub 500 | Film-coated tablet (Fct) | Not stated in the registration data |

The available registrations cover oral tablets and an intravenous infusion. No ophthalmic (eye drop) product appears among them. This matters for the predicted eye indication.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug interaction records were found in the data provided. Fluoroquinolone class warnings (tendon, QT prolongation, CNS effects, peripheral neuropathy) apply in general, so check the PI before any use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a single outbreak report about a non-bacterial pathogen, with no trials and no plausible mechanism. Model output alone does not justify further work on this indication.

**To proceed, the following is needed:**
- Evidence that levofloxacin has clinical benefit in punctate epithelial keratoconjunctivitis, such as ophthalmic studies or trials
- Confirmation of a suitable ophthalmic formulation, since only oral and IV products are registered locally
- The SAHPRA Professional Information, to complete the safety review

**Other predicted indications for this drug (for reference):**
- **Monoclonal gammopathy (myeloma infection prophylaxis)**: L1 evidence, including the TEAMM phase 3 RCT (PMID 31668592). Levofloxacin prevents infections here rather than treating the plasma-cell disorder. Decision: Proceed with Guardrails.
- **Septicemic plague**: L4 evidence, from animal models only. Decision: Proceed with Guardrails.

These two are much better supported than the eye indication and may be the better candidates to pursue.

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

