---
layout: default
title: Valine
parent: Moderate Evidence (L3-L4)
nav_order: 466
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-29
description: "Valine: predicted new indication Sclerosing cholangitis (evidence level L4). Approved use: Not available. The SAHPRA registrations in the data compiled for this…"
monitor_inn: "Valine"
predicted_indications: ["sclerosing cholangitis", "angle-closure glaucoma", "hyperthyroidism", "traumatic glaucoma", "aqueous misdirection", "neovascular glaucoma", "glaucomatous atrophy of optic disc", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "obsolete bundle branch block", "hyperthyroxinemia"]
---

# Valine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Valine: From Parenteral Nutrition Amino Acid Component to Sclerosing Cholangitis
{: .text-alpha }

## One-Sentence Summary

Valine is a branched-chain amino acid (BCAA) that is registered in South Africa only as a component of parenteral nutrition and dialysis solutions. The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but there are currently **no registered clinical trials** and only **2 publications**, both observational or associative (a cohort study and a Mendelian randomization study), and neither tests valine as a treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available. The SAHPRA registrations in the data compiled for this report carry no indication text. All 11 products are amino-acid-containing infusion, parenteral nutrition or dialysis solutions. |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 0.9942 |
| Evidence Level | L4 |
| South Africa Market Status | Marketed (valid licences: 11 of 11) |
| Number of SAHPRA Registrations | 11 (valid: 11) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, valine is an essential branched-chain amino acid supplied as part of amino acid mixtures in parenteral nutrition. Its nutritional role is established, but a specific therapeutic mechanism in sclerosing cholangitis has not been demonstrated.

The link to sclerosing cholangitis is indirect. Altered BCAA and aromatic amino acid patterns are described in chronic cholestatic liver disease. One cohort study examined plasma tyrosine and fatigue in primary biliary cirrhosis and primary sclerosing cholangitis. A Mendelian randomization study connected blood metabolites and metabolic pathways to cholestatic liver diseases. These findings show that amino acid metabolism is associated with the disease. They do not show that valine supplementation treats it.

The high TxGNN score is a model prediction. No clinical data support it, and it should be read as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39015781](https://pubmed.ncbi.nlm.nih.gov/39015781/) | 2024 | Mendelian randomization | Frontiers in Medicine | Investigated causal links between blood metabolites and the risk of primary biliary cholangitis and primary sclerosing cholangitis. |
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohort | BMC Gastroenterology | Examined amino acid patterns, in particular plasma tyrosine, in relation to fatigue in primary biliary cirrhosis and primary sclerosing cholangitis. |

Neither paper evaluates valine as a treatment.

## South Africa Market Information

All 11 registrations are valid single-ingredient-category entries. The data compiled for this report contain no approved indication text or Essential Medicines List (EML) information for them. The first 5 are listed below.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 37/34/0243 | Nutrineal PD4 with 1.1% amino acids 2.5L | Infusion | Not stated |
| Reg. No. 33/10.2.1/0271 | Adco-ipratropium (ni201) | Vial | Not stated |
| Reg. No. 38/34/0172 | Extraneal 2L single bag | Infusion | Not stated |
| Reg. No. 37/25.2/0503 | Oliclinomel N6 900E 2000ml | Infusion | Not stated |
| Reg. No. 41/25/0757 | Nutriflex Lipid Peri | Infusion | Not stated |

Six further registrations exist, including Numeta G13E, Numeta G16E, Smofkabiven, Smofkabiven Peripheral, Nutriflex Omega Specialized and Nutriflex Lipid Special 625ml. Note that the product name "Adco-ipratropium" does not obviously match an amino acid product and should be verified against the SAHPRA register.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Other Predicted Indications (For Reference)

The remaining top predictions have no clinical trials and no supportive therapeutic evidence.

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Angle-closure glaucoma | 0.9940 | L5 | The only paper is a PRPH2 mutation pedigree report, unrelated to valine. No plausible mechanism. |
| Hyperthyroidism | 0.9932 | L4 | One cross-sectional study links BCAAs to thyroid function. Most other papers are TSH receptor mutation reports where valine is only a residue name. This is a biomarker association, not therapeutic evidence. |
| Traumatic glaucoma | 0.9928 | L5 | Model prediction only. |
| Aqueous misdirection | 0.9928 | L5 | Model prediction only. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. |
| Neovascular glaucoma | 0.9926 | L5 | Model prediction only. Driven by ischaemia-induced VEGF, with no link to valine. |
| Glaucomatous atrophy of optic disc | 0.9923 | L5 | Model prediction only. No neuroprotective mechanism demonstrated. |
| Resistance to thyroid hormone (TR beta mutation) | 0.9921 | L5 | Papers are mutation reports naming valine as a residue. This is a text-matching artifact. |
| Obsolete bundle branch block | 0.9919 | L5 | Obsolete ontology term. Likely a prediction artifact. |
| Hyperthyroxinemia | 0.9907 | L5 | Same THRB mutation papers as above. No therapeutic rationale. |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for sclerosing cholangitis rests on a model score and indirect metabolic associations. There are no clinical trials, no interventional studies of valine, and no established mechanism. The other predictions are weaker; their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**To proceed, the following is needed:**
- SAHPRA Professional Information (PI) for the registered products, covering approved indications, warnings and contraindications. This is a blocking gap for any safety screening.
- Detailed mechanism of action data (for example from DrugBank).
- A focused literature review of BCAA supplementation in cholestatic liver disease, to show whether any interventional evidence exists.
- Mechanistic and preclinical evidence that valine specifically, rather than BCAAs or amino acid status in general, is relevant to sclerosing cholangitis.
- Clinical review of whether supplementation is safe in cholestatic liver disease, given that hepatic amino acid handling is altered in these patients.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

