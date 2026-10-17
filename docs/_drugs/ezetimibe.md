---
layout: default
title: Ezetimibe
parent: High Evidence (L1-L2)
nav_order: 222
evidence_level: L1
indication_count: 4
last_modified_at: 2026-10-15
description: "Ezetimibe: predicted new indication Hyperlipoproteinaemia (evidence level L1). Approved use: Hyperlipidaemia, familial hyperlipidaemia…"
monitor_inn: "EZETIMIBE"
predicted_indications: ["hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "cholesterol-ester transfer protein deficiency"]
---

# Ezetimibe
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **4** 
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

# Ezetimibe: From Hyperlipidaemia to Hyperlipoproteinaemia

## One-Sentence Summary

Ezetimibe is a cholesterol absorption inhibitor, originally used to treat hyperlipidaemia (including familial hypercholesterolaemia and sitosterolaemia).
The TxGNN model predicts it may be effective for **hyperlipoproteinaemia**, with **40 clinical trials** and **19 publications** compiled for this direction.
This prediction largely restates the existing use rather than a true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperlipidaemia, familial hyperlipidaemia, homozygous familial hypercholesterolaemia, sitosterolaemia (the SAHPRA licence records contain no indication text) |
| Predicted New Indication | Hyperlipoproteinaemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 6 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ezetimibe inhibits NPC1L1-mediated cholesterol absorption in the intestine. This lowers LDL-C and other atherogenic lipoproteins. Detailed mechanism of action data was not available in the compiled data, but this mechanism is well established in the literature.

Hyperlipoproteinaemia is closely related to the original indications, and the mechanism that supports the existing hyperlipidaemia use applies directly. The high TxGNN score (99.63%) is consistent with this overlap. It is better read as an extension or restatement of labelled use than as a new therapeutic area.

Other predictions in the data are much weaker:
- **Familial hypercholesterolaemia (score 99.38%):** Homozygous FH is already an original indication. Heterozygous FH is the extension. Ezetimibe's complementary pathway is useful when LDL receptor function is impaired. Evidence level L1.
- **Hypercholesterolaemia due to cholesterol 7-alpha-hydroxylase deficiency (99.25%):** Only one preclinical mechanistic paper; it did not test ezetimibe in this disease. Evidence level L4, Hold.
- **Cholesteryl ester transfer protein deficiency (99.09%):** Only a general review and an animal study, with no ezetimibe-specific data. The score reflects network proximity, not clinical support. Evidence level L5, Hold.

---

## Clinical Trial Evidence

The compiled data lists 40 trials for hyperlipoproteinaemia. The most relevant are shown below. No SANCTR or PACTR identifiers were available.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE: ezetimibe + high-dose simvastatin vs simvastatin alone on carotid atherosclerosis progression in heterozygous FH |
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Phase 3 | Completed | 1220 | Ezetimibe/simvastatin plus extended-release niacin in type IIa/IIb hyperlipidaemia |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | Completed | 576 | Fenofibrate + ezetimibe in mixed hyperlipidaemia |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Phase 3 | Completed | 587 | Fenofibrate + ezetimibe in mixed hyperlipidaemia |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | Completed | 611 | Ezetimibe/simvastatin + fenofibrate in mixed hyperlipidaemia |
| [NCT01984424](https://clinicaltrials.gov/study/NCT01984424) | Phase 3 | Completed | 511 | Evolocumab vs ezetimibe in patients unable to tolerate statins due to muscle side effects (ezetimibe as comparator) |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10 mg added to atorvastatin or simvastatin in homozygous FH |
| [NCT00092833](https://clinicaltrials.gov/study/NCT00092833) | Phase 3 | Terminated | 49 | Open-label treatment-use study of ezetimibe 10 mg/day in homozygous FH or sitosterolaemia |
| [NCT00705211](https://clinicaltrials.gov/study/NCT00705211) | N/A (observational) | Completed | 1794 | 52-week post-marketing safety investigation of Zetia 10 mg in Japan |
| [NCT00753883](https://clinicaltrials.gov/study/NCT00753883) | Phase 4 | Completed | 40 | Ezetimibe added to statin vs statin alone for lipid lowering |

For familial hypercholesterolaemia, additional directly relevant trials include [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) (Phase 3, n=44, long-term safety in homozygous FH), [NCT00867165](https://clinicaltrials.gov/study/NCT00867165) (Phase 3, placebo-controlled, n=138, children aged 6–10 years) and [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) (Phase 3, n=248, adolescents with heterozygous FH).

No clinical trials were registered for the predictions in ranks 3 and 4.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT (Phase 3) | Lancet | TANDEM: obicetrapib/ezetimibe fixed-dose combination for LDL-C reduction |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Oral PCSK9 inhibitor enlicitide in heterozygous FH (ezetimibe is not the test drug) |
| [25282519](https://pubmed.ncbi.nlm.nih.gov/25282519/) | 2015 | RCT | Lancet | RUTHERFORD-2: evolocumab in heterozygous FH despite statin ± ezetimibe |
| [37850379](https://pubmed.ncbi.nlm.nih.gov/37850379/) | 2024 | RCT | Circulation | ORION-5: inclisiran in homozygous FH |
| [35101175](https://pubmed.ncbi.nlm.nih.gov/35101175/) | 2022 | Cohort | Lancet | Worldwide retrospective cohort of homozygous FH patients and current practice |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Review | Mol Med Rep | Advances in drugs targeting hyperlipidaemia |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | New and emerging LDL-C and apoB lowering therapies, on a foundation of statins, ezetimibe and PCSK9 inhibitors |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiol Clin | Familial hypercholesterolaemia; ezetimibe listed among LDL-lowering treatments |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Review | Am J Cardiovasc Drugs | Ezetimibe drug profile: selective inhibition of intestinal cholesterol and plant sterol absorption |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | Review | Drug Ther Bull | Ezetimibe update: lowers LDL-C alone or with a statin |

Much of this literature concerns other drugs (PCSK9 inhibitors, CETP inhibitors) with ezetimibe as background or comparator therapy, so the evidence for ezetimibe itself is partly indirect.

---

## South Africa Market Information

All 6 registrations are valid single-ingredient licences. The SAHPRA records compiled for this report contain no approved indication text or manufacturer names. The data does not state whether ezetimibe is on the Essential Medicines List.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 54/7.5/0364 | Ezorb | Tablet | Not available in compiled data |
| Reg. No. 55/7.5/0779 | Lypstaplus 10 Mg/10 Mg | Tablet | Not available in compiled data |
| Reg. No. 50/7.5/1171 | Liptruzet 10/10 | Film-coated tablet | Not available in compiled data |
| Reg. No. 54/7.5/0693 | Reguchole 10/5Mg | Tablet | Not available in compiled data |
| Reg. No. A51/7.5/1008 | Tryzetor Plus 10/20 Mg | Tablet | Not available in compiled data |

A sixth registration, Reg. No. 50/7.5/1173 (Liptruzet 10/40, film-coated tablet), is also valid.

---

## Safety Considerations

**Contraindication-related diseases (from the knowledge graph, not label text):** pancreatitis, liver disease, gallbladder disease, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, substance abuse/dependence, rhabdomyolysis, nodular fasciitis. These come from drug–disease network associations and should be checked against the approved Professional Information (PI). Some may relate to statin partners in combination products.

**Drug Interactions:** 100 interactions were identified. The main ones graded Moderate are:
- Chenodeoxycholic acid
- Eluxadoline
- Rosuvastatin
- Simvastatin

Other interactions are of unknown severity (for example calcitriol, pantoprazole, glimepiride, mesalazine, doxycycline, metformin, omeprazole, morphine, cimetidine, vancomycin and lactulose).

The label warnings and contraindications from the SAHPRA-approved PI were not available. Please refer to the PI for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials (including large combination studies, FH-specific studies and paediatric studies) support ezetimibe in lipid disorders. Hyperlipoproteinaemia largely overlaps the existing labelled use, so the efficacy risk is low. The decision is limited by the missing PI safety text and the indirect nature of some evidence. The other two predictions (CYP7A1 deficiency and CETP deficiency) should be placed on **Hold** because they have no human data for ezetimibe.

**To proceed, the following is needed:**
- Obtain the SAHPRA-approved PI to confirm approved indications, warnings and contraindications
- Obtain detailed mechanism of action data from DrugBank
- Confirm Essential Medicines List status in South Africa
- Review the moderate interactions with statins and bile acid-related drugs, and the liver and muscle safety signals, for the target population
- Define a monitoring plan for patients on combination products containing ezetimibe plus a statin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

