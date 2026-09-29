---
layout: default
title: Leucine
parent: Model Prediction Only (L5)
nav_order: 288
evidence_level: L5
indication_count: 10
---

# Leucine
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

# Leucine: From Amino Acid Nutrition Products to Congenital Prothrombin Deficiency

## One-Sentence Summary

Leucine is an essential amino acid. In South Africa it is registered as an ingredient of parenteral nutrition and peritoneal dialysis products, and no formal original indication is recorded.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but this rests on a graph-based score alone, with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data (registered products are amino acid-containing infusion and nutrition formulations) |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.00% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Leucine is a component of amino acid-based nutrition and dialysis products, but none of the registrations carries an approved indication text.

No plausible mechanism linking leucine to prothrombin (Factor II) synthesis or function was identified. Congenital prothrombin deficiency is a rare inherited coagulation disorder caused by *F2* gene defects, and there is no established biological reason for an amino acid supplement to correct it.
The high score (rank 4,808 in the model output) is therefore best read as a statistical artefact of the knowledge graph, not as a mechanistic signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other Predicted Indications Worth Noting

The top-ranked prediction is the weakest. Among the other nine, only one has a plausible, if indirect, rationale:

| Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|---------|
| Postmenopausal osteoporosis | 97.42% | L4 | Plausible but indirect. Leucine activates mTORC1 and protein synthesis, which may help preserve lean mass and bone during energy restriction. Metabolomic studies ([PMID 33293818](https://pubmed.ncbi.nlm.nih.gov/33293818/), [PMID 40703670](https://pubmed.ncbi.nlm.nih.gov/40703670/)) link amino acid metabolism to bone density, but these are associations, not treatment effects. |
| Acne | 98.42% | L4 | Direction of effect is more likely adverse. Literature on Western diet and mTORC1 signalling ([PMID 22870349](https://pubmed.ncbi.nlm.nih.gov/22870349/), [PMID 22419445](https://pubmed.ncbi.nlm.nih.gov/22419445/)) implicates leucine-dependent mTORC1 activation as a driver of acne. |
| Pregnancy associated osteoporosis | 96.57% | L4 | Weak. One animal study of HMB, a leucine metabolite ([PMID 34768327](https://pubmed.ncbi.nlm.nih.gov/34768327/)), and no human evidence for leucine itself. |
| Gastroparesis, Paget disease of bone, sclerosing cholangitis, albinism-deafness syndrome, Worth syndrome | 96.3–98.8% | L5 | No supportive mechanism or evidence. The literature retrieved for Paget disease and sclerosing cholangitis is matched on gene/protein names or the word "leucine". |
| Obsolete vitamin D deficiency | 97.67% | L5 | The disease term is obsolete in the ontology and should be remapped to a current vitamin D deficiency concept before re-evaluation. |

The only relevant trial found is [NCT01757340](https://clinicaltrials.gov/study/NCT01757340), a completed study (n=43, phase not applicable) of calorie restriction with leucine supplementation in obese postmenopausal women. Bone outcomes were among its stated aims, but results were not confirmed in the supplied data, and the calorie-restriction background confounds attribution to leucine.
[NCT07277075](https://clinicaltrials.gov/study/NCT07277075) (acne) is a false-positive match. It measures leucine-rich alpha-2 glycoprotein 1, a protein unrelated to the amino acid.

---

## South Africa Market Information

Showing 5 of 12 registrations:

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 37/34/0243 | Nutrineal PD4 with 1.1% amino acids 2.5L | Infusion | Not stated in registration data |
| Reg. No. 33/10.2.1/0271 | Adco-ipratropium (ni201) | Vial | Not stated in registration data |
| Reg. No. 38/34/0172 | Extraneal 2L single bag | Infusion | Not stated in registration data |
| Reg. No. 37/25.2/0503 | Oliclinomel N6 900E 2000ml 3blog1r79sa | Infusion | Not stated in registration data |
| Reg. No. 41/25/0757 | Nutriflex Lipid Peri | Infusion | Not stated in registration data |

Adco-ipratropium is an ipratropium product and looks like a mapping anomaly, so the registration-to-ingredient link should be verified.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for congenital prothrombin deficiency has no trials, no literature and no identifiable mechanism. It is a model output only (L5). Among the other predictions, only postmenopausal osteoporosis (L4) merits follow-up as a research question.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for leucine (for example from DrugBank)
- Verification of the 12 registrations, including product-to-ingredient mapping
- Remapping of the obsolete vitamin D deficiency term
- For postmenopausal osteoporosis, retrieval of bone outcome results from NCT01757340 and a focused literature review on leucine or HMB and bone density
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

