---
layout: default
title: Pravastatin
parent: Moderate Evidence (L3-L4)
nav_order: 381
evidence_level: L4
indication_count: 9
---

# Pravastatin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **9** 
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

# Pravastatin: From Lipid-Lowering Therapy to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Pravastatin is a statin (HMG-CoA reductase inhibitor) marketed in South Africa for lipid lowering. The registration records provided do not state the approved indication text.
The TxGNN model predicts it may be useful for **homozygous familial hypercholesterolemia (HoFH)**, but the only linked trial studies a different drug (alirocumab), so there is **no direct pravastatin evidence** for this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA records provided (statin class use: lipid lowering) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the Evidence Pack. Pravastatin belongs to the statin class. Statins inhibit HMG-CoA reductase, which lowers hepatic cholesterol synthesis and upregulates LDL receptors. Its efficacy in common hypercholesterolaemia is established, and mechanistically it could apply to familial hypercholesterolemia.

There is an important limit for the homozygous form. In HoFH, patients have little or no functional LDL-receptor activity, and statins depend on that receptor. Response is therefore expected to be limited. Heterozygous FH is the mechanistically stronger fit (see the note below).

The high model score reflects a strong link in the knowledge graph. It is not evidence that pravastatin works in HoFH.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label alirocumab in children and adolescents (8–17 years) with HoFH; primary endpoint is LDL-C change at Week 12. Pravastatin is not the studied drug and at most part of background therapy. |

No SANCTR or PACTR registrations were identified in the data provided.

## Literature Evidence

All items are indirect. There is no pravastatin RCT for HoFH in the data provided.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Statins in children with familial hypercholesterolemia; only indirectly relevant to HoFH |
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Earlier version of the same Cochrane review |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guidelines for dyslipidaemia management and cardiovascular prevention |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review | Drugs | Rosuvastatin review; reports superior lipid improvement versus atorvastatin, simvastatin and pravastatin (a different statin) |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clin Ther | Rosuvastatin in hyperlipidaemia, including its HoFH indication (a different statin) |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Review | Am J Cardiovasc Drugs | Ezetimibe review (a different drug) |
| [31358055](https://pubmed.ncbi.nlm.nih.gov/31358055/) | 2019 | Preclinical | Stem Cell Res Ther | iPSC-derived LDLR-deficient hepatocytes as an FH model; no pravastatin-specific data |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. A40/7.5/0749 | Novales 20 | Tablet | Not stated in the data provided |
| Reg. No. A39/7.5/0358 | Arrow Pravastatin | Tablet | Not stated in the data provided |
| Reg. No. 42/7.5/0372 | Pixeta | Tablet | Not stated in the data provided |
| Reg. No. 52/7.5/0769 | Pravafen 40/160Mg | Capsule | Not stated in the data provided (the name suggests a fixed-dose combination; verify against the PI) |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only trial linked to HoFH tests alirocumab, and the literature consists of reviews of other lipid-lowering drugs. Mechanistically, response in HoFH is expected to be limited by residual LDL-receptor activity. This should be treated as a research question, not a repurposing candidate.

**To proceed, the following is needed:**
- Pravastatin-specific HoFH data (trials or case series)
- The approved indication text from the SAHPRA Professional Information, to confirm what is already labelled
- Safety information from the SAHPRA Professional Information

**Note on other predicted indications:**
- **HIV-associated dyslipidaemia and cardiovascular risk** is a stronger candidate (rank 2, L2, Proceed with Guardrails). It has a Phase 2 pravastatin trial in HIV patients on HAART (NCT00221754), several RCTs, and a Phase 3 trial with a pravastatin comparator (NCT00006412; the arm is inferred from a truncated title). The supported use is lipid and cardiovascular risk management, not antiviral activity. Antiretroviral interactions (for example darunavir/ritonavir and raltegravir) need checking before use.
- **Heterozygous familial hypercholesterolemia** (rank 6, L4) is mechanistically strong, but none of the trials provided study pravastatin.
- The remaining predictions (ranks 3–5 and 7–9) have no supporting clinical evidence and are on Hold. Ranks 4 and 5 are veterinary or animal-model diseases.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

