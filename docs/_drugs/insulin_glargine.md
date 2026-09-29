---
layout: default
title: Insulin Glargine
parent: Model Prediction Only (L5)
nav_order: 264
evidence_level: L5
indication_count: 10
---

# Insulin Glargine
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

# Insulin Glargine: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin glargine is a long-acting basal insulin analog that acts on the insulin receptor and is marketed in South Africa under 3 SAHPRA registrations.
The TxGNN model predicts it may be effective for **autoimmune oophoritis** (score 99.88%), but there are **0 clinical trials** and **0 publications** for this indication.
The prediction is model-only (L5) and no mechanistic link could be identified, so we recommend **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Basal insulin therapy for diabetes mellitus (the registration records supplied contain no approved-indication text) |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Insulin glargine is a long-acting basal insulin analog that acts on the insulin receptor to lower blood glucose.

Nothing in the supplied data connects this action to ovarian autoimmunity. The very high TxGNN score is most likely a graph-based artefact, for example driven by shared autoimmune or endocrine neighbours such as autoimmune polyendocrine syndromes. Any real connection would be indirect, via co-occurring autoimmune diabetes rather than treatment of the oophoritis itself.

The other nine predicted indications show a similar pattern:
- **Thiamine-responsive dysfunction syndrome, focal stiff limb syndrome and classic stiff person syndrome**: insulin would manage only the coexisting diabetes, not the underlying disorder.
- **Localized lipodystrophies** (drug-induced, centrifugal, pressure-induced, idiopathic): injection-site lipoatrophy and lipohypertrophy are known adverse effects of subcutaneous insulin. These predictions are better read as a safety signal than as a repurposing opportunity.
- **Opsismodysplasia**: SHIP2 (INPPL1) regulates PI3K/insulin signalling, so a speculative pathway link exists, but the direction of effect is unknown.
- **Pancreatic agenesis** (rank 6, score 99.43%): this is the only biologically well-founded candidate. It causes absolute insulin deficiency, so insulin replacement is standard supportive care. This is hormone replacement, not a new mechanism. It is classed L4 with a "Research Question" recommendation, and the open question is whether glargine offers a specific advantage over other insulins, such as basal coverage in neonates and infants.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for autoimmune oophoritis.

For context, the six papers retrieved for pancreatic agenesis are all indirect, and none is specific to insulin glargine in that condition:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11727406](https://pubmed.ncbi.nlm.nih.gov/11727406/) | 2001 | Review | Endocrinol Metab Clin North Am | Insulin therapy in type 2 diabetes |
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Review | J Am Pharm Assoc | Practical aspects of starting insulin in type 2 diabetes |
| [19322513](https://pubmed.ncbi.nlm.nih.gov/19322513/) | 2009 | Review | Acta Diabetol | Secondary diabetes with endocrinopathies |
| [32871938](https://pubmed.ncbi.nlm.nih.gov/32871938/) | 2020 | Case report | Medicine | MODY5 treated with a GLP-1 receptor agonist |
| [25818213](https://pubmed.ncbi.nlm.nih.gov/25818213/) | 2015 | Cohort (veterinary) | J Vet Intern Med | Pancreatic enzymes and ultrasound findings in diabetic cats |
| [18518815](https://pubmed.ncbi.nlm.nih.gov/18518815/) | 2008 | Case report (veterinary) | J Am Vet Med Assoc | Chronic pancreatitis with secondary diabetes in a sea lion, treated with insulin |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 49/21.1/1230 | Toujeo pen 1.5ml | Injection |
| Reg. No. 51/21.1/0729 | Endulin Select | Solution |
| Reg. No. 41/21.1/0363 | Optisulin cartridge 3ml | Injection |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Localized lipoatrophy and lipohypertrophy at subcutaneous injection sites are known effects of insulin. These are relevant when interpreting the lipodystrophy-related predictions above.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, autoimmune oophoritis, has no trials, no literature and no plausible mechanistic link, so the high TxGNN score is not clinically meaningful. All other candidates either reflect comorbid diabetes or represent adverse effects of insulin, apart from pancreatic agenesis. There, insulin is already standard replacement, so it is not a true repurposing case.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications and approved indications) for the 3 registered products
- Mechanism of action data from DrugBank
- For pancreatic agenesis only: a targeted literature review or comparative data on glargine versus other basal insulins in neonatal and infant patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

