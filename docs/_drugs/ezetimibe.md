---
layout: default
title: Ezetimibe
parent: Model Prediction Only (L5)
nav_order: 220
evidence_level: L5
indication_count: 4
---

# Ezetimibe
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Ezetimibe: From Lipid-Lowering Therapy to Hyperlipoproteinemia

## One-Sentence Summary

Ezetimibe is a marketed cholesterol-absorption inhibitor. The registration data supplied for this report do not state its approved indication, so its original use is inferred from its drug class.
The TxGNN model predicts it may be effective for **hyperlipoproteinemia**, with **48 clinical trials** and **20 publications** retrieved. Of these, only about 10 trials and 1 publication directly test ezetimibe in lipid disorders.
Because ezetimibe is already a lipid-lowering drug, this prediction is probably an existing labelled use rather than true repurposing. The SAHPRA label must be checked before it is reported as a repurposing finding.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 (at least 2 completed Phase 3 RCTs) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 6 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Ezetimibe blocks NPC1L1, the intestinal transporter that takes up dietary and biliary cholesterol. This lowers LDL-cholesterol, which is directly relevant to hyperlipoproteinemia. Preclinical work also links NPC1L1 to cholesterol handling and bile acid regulation.

Detailed mechanism-of-action data are not available in the source record. Based on known information, ezetimibe is an established lipid-lowering agent, and mechanistically it is well suited to conditions with raised LDL-C. Completed Phase 3 trials, including combinations with simvastatin, fenofibrate, niacin and atorvastatin, cover mixed hyperlipidaemia and related lipid disorders.

The original indication is blank in the source record. This is most likely a data gap rather than evidence that the use is new. If the SAHPRA label already lists hyperlipidaemia or hypercholesterolaemia, the prediction confirms an existing use and is not a repurposing candidate.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | Completed | 611 | Ezetimibe/simvastatin plus fenofibrate in mixed hyperlipidaemia (high cholesterol and triglycerides) |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Phase 3 | Completed | 587 | Fenofibrate and ezetimibe coadministration in mixed hyperlipidaemia |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | Completed | 576 | Second fenofibrate and ezetimibe coadministration study in mixed hyperlipidaemia |
| [NCT00349284](https://clinicaltrials.gov/study/NCT00349284) | Phase 3 | Completed | 181 | Double-blind comparison of fenofibrate 145 mg, ezetimibe 10 mg and their combination in type IIb dyslipidaemia with metabolic syndrome features |
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Phase 3 | Completed | 1220 | Ezetimibe/simvastatin plus extended-release niacin in type IIa or IIb hyperlipidaemia |
| [NCT00195793](https://clinicaltrials.gov/study/NCT00195793) | Phase 3 | Completed | 174 | Fenofibrate or ezetimibe added to atorvastatin in combined hyperlipidaemia |
| [NCT00268697](https://clinicaltrials.gov/study/NCT00268697) | Phase 3 | Completed | 1267 | Lapaquistat acetate alone or with ezetimibe 10 mg versus ezetimibe 10 mg in primary dyslipidaemia |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE: ezetimibe plus high-dose simvastatin versus simvastatin alone, measuring carotid atherosclerosis progression in heterozygous familial hypercholesterolaemia |
| [NCT00704444](https://clinicaltrials.gov/study/NCT00704444) | N/A (observational) | Completed | 11332 | 12-week Japanese post-marketing investigation of Zetia alone or combined; real-world safety and efficacy, no control arm |
| [NCT00704535](https://clinicaltrials.gov/study/NCT00704535) | N/A (observational) | Completed | 4105 | Filipino post-marketing surveillance of ezetimibe; real-world safety and tolerability, uncontrolled |

Ten of 48 retrieved trials are shown. The remaining trials mostly test PCSK9 agents, bempedoic acid or behavioural interventions, or are pharmacokinetic studies. Ezetimibe is a comparator or background therapy in these, not the intervention under study. None of the supplied trial records carries a SANCTR or PACTR identifier.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT | Lancet | TANDEM: phase 3 placebo-controlled trial of an obicetrapib and ezetimibe fixed-dose combination for LDL-C reduction |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Oral PCSK9 inhibitor enlicitide in heterozygous familial hypercholesterolaemia; ezetimibe is not the test agent |
| [25282519](https://pubmed.ncbi.nlm.nih.gov/25282519/) | 2015 | RCT | Lancet | RUTHERFORD-2: evolocumab in heterozygous familial hypercholesterolaemia despite statin, with or without ezetimibe |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Consensus statement | Eur Heart J | European Atherosclerosis Society guidance: familial hypercholesterolaemia is underdiagnosed and undertreated |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiol Clin | Familial hypercholesterolaemia; lists ezetimibe among LDL-lowering treatments |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Review | Mol Med Rep | Research advances in current drugs targeting hyperlipidaemia |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | New and emerging LDL-C and apoB therapies built on statins, ezetimibe and PCSK9 inhibitors |
| [34480646](https://pubmed.ncbi.nlm.nih.gov/34480646/) | 2021 | Review | Curr Cardiol Rep | Familial hypercholesterolaemia: global burden, diagnosis and management |
| [30702994](https://pubmed.ncbi.nlm.nih.gov/30702994/) | 2019 | Review | Circ Res | Overview of cholesterol-lowering agents |
| [18376001](https://pubmed.ncbi.nlm.nih.gov/18376001/) | 2008 | Not classified | N Engl J Med | "Cholesterol lowering and ezetimibe" (no abstract in the record) |

Only TANDEM tests an ezetimibe-containing regimen directly. The other publications provide disease and treatment-landscape context.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 54/7.5/0364 | Ezorb | Tablet |
| Reg. No. 55/7.5/0779 | Lypstaplus 10 Mg/10 Mg | Tablet |
| Reg. No. 50/7.5/1171 | Liptruzet 10/10 | Film-coated tablet (listed as "Fct") |
| Reg. No. 54/7.5/0693 | Reguchole 10/5Mg | Tablet |
| Reg. No. A51/7.5/1008 | Tryzetor Plus 10/20 Mg | Tablet |

Six registrations are recorded, but only five are itemised in the data. The approved-indication text is blank for all of them. Several product names carry two strengths, which suggests fixed-dose combinations, but the components are not stated in the data. Essential Medicines List (EML) status is not provided.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several completed Phase 3 RCTs test ezetimibe, alone or combined, in mixed hyperlipidaemia and related lipid disorders, and large post-marketing studies add real-world data. The mechanism is directly relevant, and ezetimibe is already marketed in South Africa. However, the safety data are missing (a blocking gap), and this looks like an existing labelled use rather than a new one.

**To proceed, the following is needed:**
- Download and parse the SAHPRA package insert for warnings, contraindications and the approved indication (blocking gap)
- Compare the label indication with "hyperlipoproteinemia" to decide whether this is repurposing or an already-labelled use
- Retrieve mechanism-of-action data from DrugBank
- Identify the components of the fixed-dose combination products and check EML status
- Review the other TxGNN predictions separately. Familial hypercholesterolaemia (rank 2) also reaches L1 and looks similarly close to the labelled use. Hypercholesterolaemia due to CYP7A1 deficiency (rank 3) has only preclinical support (L4). CETP deficiency (rank 4) has no plausible ezetimibe mechanism and should stay on Hold.

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

