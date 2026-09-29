---
layout: default
title: Niacin
parent: Moderate Evidence (L3-L4)
nav_order: 338
evidence_level: L4
indication_count: 1
---

# Niacin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Niacin: From Established Lipid Modification to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Niacin is a lipid-modifying agent that lowers LDL-C, VLDL and triglycerides and raises HDL-C. The TxGNN model predicts it may be useful for **homozygous familial hypercholesterolemia (HoFH)**. Of the **2 clinical trials** and **20 publications** retrieved, none directly tests niacin in HoFH, so the evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.74% (rank 1756) |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Niacin is thought to lower lipids in two ways. It inhibits hepatic DGAT2, which reduces triglyceride synthesis and VLDL/apoB secretion. It also acts through GPR109A to suppress lipolysis in fat tissue. This is biologically plausible for hypercholesterolemia, and part of it does not depend on LDL receptor function.

HoFH is caused by severely impaired or absent LDL receptor activity, which produces very high LDL-C. Niacin's expected LDL-C reduction is modest (roughly 10-20%). That is small next to the severity of HoFH, where current management relies on high-intensity lipid lowering, PCSK9 inhibition, lomitapide and LDL apheresis.

The very high TxGNN score probably reflects niacin's existing lipid-modifying role in the knowledge graph rather than a new HoFH-specific signal. The registered indication and detailed mechanism-of-action data were not available in the input, so this link could not be checked against label data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label alirocumab (PCSK9 inhibitor) in children and adolescents with HoFH. Niacin was not studied. It shows only the standard-of-care landscape niacin would have to compete with or add to. |
| [NCT03110432](https://clinicaltrials.gov/study/NCT03110432) | N/A (registry) | Completed | 1695 | German registry of very-high-cardiovascular-risk dyslipidemia patients meeting criteria for PCSK9 inhibitor use. It is not HoFH-specific and has no niacin arm. |

Neither trial provides direct evidence for niacin.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26376908](https://pubmed.ncbi.nlm.nih.gov/26376908/) | 2015 | Scientific statement | Arterioscler Thromb Vasc Biol | Notes that placebo-controlled RCTs of niacin monotherapy reduced CVD endpoints. This is a general non-statin LDL-lowering statement, not HoFH-specific. |
| [24506448](https://pubmed.ncbi.nlm.nih.gov/24506448/) | 2014 | Review | Expert Rev Cardiovasc Ther | Critical review of non-statin options (fibrates, ezetimibe, bile acid sequestrants, n-3 fatty acids, niacin) for residual risk and statin intolerance. |
| [23959229](https://pubmed.ncbi.nlm.nih.gov/23959229/) | 2013 | Review | Nat Rev Cardiol | Reviews lipid-modifying agents beyond statins for severe hypercholesterolaemia or mixed dyslipidaemia. |
| [26370207](https://pubmed.ncbi.nlm.nih.gov/26370207/) | 2015 | Review | Drugs | Challenges in diagnosing and treating HoFH. |
| [27797643](https://pubmed.ncbi.nlm.nih.gov/27797643/) | 2016 | Review | Metab Syndr Relat Disord | Modern management of familial hypercholesterolemia, covering both HoFH and HeFH. |
| [25257073](https://pubmed.ncbi.nlm.nih.gov/25257073/) | 2014 | Review | Atheroscler Suppl | What can be achieved in HoFH today and the unmet needs, including apheresis and lipid-lowering drugs. |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | Pharmacokinetic study | Pharmacotherapy | Studied the pharmacokinetic effects of lomitapide (approved for HoFH) on several lipid-lowering drugs, including niacin. |
| [2912428](https://pubmed.ncbi.nlm.nih.gov/2912428/) | 1989 | Clinical observation | Arteriosclerosis | Lipid levels in children with familial hypercholesterolemia on various drug regimens (30 HeFH, 3 HoFH). |
| [3931803](https://pubmed.ncbi.nlm.nih.gov/3931803/) | 1985 | Case report | Br Med J | Family with four HoFH children, comparing treated and untreated outcomes. |
| [7040850](https://pubmed.ncbi.nlm.nih.gov/7040850/) | 1982 | Review | Med Clin North Am | Drug therapy for hypercholesterolemia, including combined regimens and HoFH. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| H2062 (ACT 101) | Filibon | Capsule (oral) |

The record for this registration does not include an approved indication or manufacturer, so I have not stated either. I could not confirm Essential Medicines List (EML) status from the data provided.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by any niacin-specific HoFH study. Both retrieved trials test other interventions (alirocumab) or are non-specific registries. The literature is mostly narrative reviews. Niacin's expected LDL-C lowering is modest, and HoFH patients have little or no LDL receptor function. Safety screening also cannot begin because the SAHPRA package insert data are missing.

**To proceed, the following is needed:**
- Download and review the SAHPRA package insert for Filibon (warnings, contraindications, registered indication)
- Confirm the mechanism of action and original indications from DrugBank
- Look for niacin-specific data in HoFH, for example add-on use with statins, ezetimibe, PCSK9 inhibitors or lomitapide
- Assess whether niacin's modest LDL-C effect could add value beyond current HoFH standard of care in South Africa
- Check SANCTR and PACTR for any relevant registered trials

---

*This report is for research reference only and does not constitute medical advice. The predicted indication requires clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

