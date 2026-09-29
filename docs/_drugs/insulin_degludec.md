---
layout: default
title: Insulin Degludec
parent: High Evidence (L1-L2)
nav_order: 262
evidence_level: L1
indication_count: 10
---

# Insulin Degludec
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Insulin Degludec: From Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin degludec is an ultra-long-acting basal insulin analogue. It is registered in South Africa in three products, but the retrieved SAHPRA records do not state the approved indication.
The TxGNN model predicts it for **type 1 diabetes mellitus**, which is effectively an on-label use rather than a true repurposing.
The prediction is supported by **50 clinical trials** and **20 publications**, including completed Phase 3 trials and randomised trials in the literature.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the retrieved SAHPRA records; the published literature describes use in type 1 and type 2 diabetes |
| Predicted New Indication | Type 1 diabetes mellitus |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L1 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Published reviews describe degludec as forming soluble multihexamers after subcutaneous injection. These slowly release monomers into the blood, giving a flat, ultra-long action profile with no pronounced peak (PMID 23890782). It binds the insulin receptor and replaces the endogenous insulin that is absent in type 1 diabetes.

The link between the "original" and predicted indication is therefore direct. Insulin replacement is the cornerstone of type 1 diabetes management, and degludec is used there as a basal insulin. The high TxGNN score reflects a well-established use, not a novel one.

The other nine predicted indications do not share this support:

- **Pancreatic agenesis:** insulin replacement is biologically plausible, but no degludec-specific evidence was found. It is a research question only.
- **Localised lipodystrophy and lipoatrophy entries:** these most likely reflect known injection-site adverse effects. They should be treated as safety associations, not indications.
- **Autoimmune oophoritis, stiff person syndrome spectrum, opsismodysplasia, thiamine-responsive dysfunction syndrome and centrifugal lipodystrophy:** these appear to arise from graph proximity or comorbidity with type 1 diabetes, with no therapeutic rationale or evidence.

## Clinical Trial Evidence

The 10 trials below are the most relevant to type 1 diabetes. No SANCTR or PACTR identifiers were found in the Evidence Pack. In NCT05463744 and NCT03952130, degludec is a comparator or background insulin, not the investigational product.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05463744](https://clinicaltrials.gov/study/NCT05463744) | Phase 3 | Completed | 692 | Weekly basal insulin efsitora alfa vs degludec in type 1 diabetes on multiple daily injections; efficacy and safety |
| [NCT01835431](https://clinicaltrials.gov/study/NCT01835431) | Phase 3 | Completed | 362 | Degludec/aspart once daily plus mealtime aspart vs detemir plus aspart in children and adolescents with type 1 diabetes |
| [NCT03952130](https://clinicaltrials.gov/study/NCT03952130) | Phase 3 | Completed | 354 | LY900014 vs insulin lispro, each combined with glargine or degludec, in adults with type 1 diabetes |
| [NCT04075513](https://clinicaltrials.gov/study/NCT04075513) | Phase 4 | Completed | 343 | Glargine U300 vs degludec U100 on glycaemic control and variability using continuous glucose monitoring |
| [NCT05434559](https://clinicaltrials.gov/study/NCT05434559) | N/A | Completed | 475 | Retrospective real-world study of glycaemic control 12 months before vs after switching to degludec |
| [NCT04450407](https://clinicaltrials.gov/study/NCT04450407) | Phase 2 | Completed | 266 | LY3209590 vs a comparator insulin in type 1 diabetes on multiple daily injections (degludec's role needs confirmation) |
| [NCT04623086](https://clinicaltrials.gov/study/NCT04623086) | Phase 4 | Completed | 59 | Switching from glargine to degludec with a bridging glargine dose vs direct conversion |
| [NCT03668808](https://clinicaltrials.gov/study/NCT03668808) | Phase 4 | Completed | 25 | Degludec vs glargine U100 in adults with type 1 diabetes flying across multiple time zones (pilot) |
| [NCT00961324](https://clinicaltrials.gov/study/NCT00961324) | Phase 1 | Completed | 54 | Within-subject variability of glucose-lowering effect, degludec vs glargine |
| [NCT00964964](https://clinicaltrials.gov/study/NCT00964964) | Phase 1 | Completed | 18 | Hypoglycaemic episodes and glycaemic variability with two degludec regimens |

The Evidence Pack's own rationale notes that its trial list contains no Phase 3 entry, but this is incorrect. NCT05463744, NCT01835431 and NCT03952130 are completed Phase 3 trials in type 1 diabetes, which is consistent with the L1 grade.

NCT04692415 was graded as a type 1 diabetes study but actually enrolled insulin-naïve adults with type 2 diabetes, so it is excluded here.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6: phase 3a, open-label, treat-to-target trial of weekly icodec vs daily degludec in adults with type 1 diabetes |
| [39270686](https://pubmed.ncbi.nlm.nih.gov/39270686/) | 2024 | RCT | Lancet | QWINT-5: phase 3 non-inferiority trial of weekly efsitora vs daily degludec in adults with type 1 diabetes |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT: degludec vs detemir, each with aspart, in pregnant women with type 1 diabetes |
| [34643020](https://pubmed.ncbi.nlm.nih.gov/34643020/) | 2022 | RCT | Diabetes Obes Metab | HypoDeg: degludec vs glargine U100 in patients with type 1 diabetes prone to nocturnal severe hypoglycaemia |
| [36516429](https://pubmed.ncbi.nlm.nih.gov/36516429/) | 2023 | RCT | Diabetes Technol Ther | ULTRAFLEXI-1: glargine U300 vs degludec U100 around spontaneous exercise, comparing time below range |
| [34763071](https://pubmed.ncbi.nlm.nih.gov/34763071/) | 2022 | RCT | Endocr Pract | BIGLEAP: crossover comparison of degludec with pump-delivered aspart, using continuous glucose monitoring |
| [36800034](https://pubmed.ncbi.nlm.nih.gov/36800034/) | 2023 | RCT | Eur J Pediatr | Degludec and glargine vs NPH in 60 toddlers and preschoolers with type 1 diabetes, assessed by glycaemic variability and time in range |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Meta-analysis | Clin Ther | Efficacy and tolerability of degludec vs glargine and detemir in type 1 and type 2 diabetes |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Network meta-analysis | Value Health | Relative efficacy and safety of basal insulin regimens in adults with type 1 diabetes |
| [31055056](https://pubmed.ncbi.nlm.nih.gov/31055056/) | 2020 | Review | Diabetes Metab | Controlled trials show comparable HbA1c reductions vs comparators, better fasting glucose control, and fewer (nocturnal) hypoglycaemic episodes |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 47/21.1/0108 | Tresiba Penfill 3 ml | Injection | Not stated in the retrieved record |
| Reg. No. 50/21.13/0985 | Xultophy | Pen set | Not stated in the retrieved record |
| Reg. No. 47/21.1/0165 | Ryzodeg FlexTouch pre-filled pen 3 ml | Injection | Not stated in the retrieved record |

Xultophy and Ryzodeg are combination products (degludec with liraglutide, and degludec with aspart, respectively). Their indications may differ from that of single-agent Tresiba.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Completed Phase 3 trials and several randomised trials in the literature support degludec in type 1 diabetes, and the use is well established. The evidence is strong, but the SAHPRA labelled indication and safety information were not available. Predictions other than type 1 diabetes have no supporting evidence and should stay on Hold.

**To proceed, the following is needed:**
- Download and review the SAHPRA package inserts to confirm the labelled indication and obtain warnings and contraindications. This is a blocking gap for safety screening.
- Retrieve mechanism of action data from DrugBank.
- Put in place hypoglycaemia monitoring and dose titration guidance.
- Check the Phase 3 study designs against their full texts, particularly the trials in which degludec is only a comparator.
- Run a targeted evidence search for pancreatic agenesis.
- Reclassify the lipodystrophy and lipoatrophy predictions as adverse-event associations.

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

