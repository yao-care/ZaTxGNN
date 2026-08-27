---
layout: default
title: Fenofibrate
parent: 僅模型預測 (L5)
nav_order: 219
evidence_level: L5
indication_count: 7
---

# Fenofibrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Fenofibrate: From Dyslipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

> Fenofibrate is a fibrate-class, PPARα-agonist lipid-lowering agent whose core, well-established use is the treatment of hyperlipoproteinemia/dyslipidemia.
> The TxGNN model predicts it may also be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**,
> but this specific direction is currently supported by only **1 clinical trial** and **11 publications**, and the trial evidence itself is compromised — see below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no SAHPRA/TFDA license data available). The pack's own mechanistic notes describe fenofibrate as a PPARα agonist whose established core use is hyperlipoproteinemia/dyslipidemia. |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L3 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for fenofibrate is not available in this evidence pack (flagged as a High-severity data gap). Based on the mechanistic notes accompanying the model's other predictions, fenofibrate is a fibric-acid derivative and PPARα agonist: it activates lipoprotein lipase (LPL) and lowers ApoC-III, producing large reductions in triglycerides, modest LDL-C lowering, and increases in HDL-C. This is the pharmacological basis for its established use across the hyperlipoproteinemia spectrum (Types IIa/IIb/III/IV/V).

HoFH, however, is a distinct and more extreme phenotype: it results from near-complete loss of functional LDL receptors, so LDL-C clearance is largely independent of the PPARα pathway that fenofibrate acts through. The model's own rationale for this candidate explicitly flags this as a weak mechanistic link, and notes that historical literature on fenofibrate in HoFH is limited to older, small studies in general Type II hyperlipidemia populations rather than confirmed HoFH cohorts.

**Important caveat:** The single clinical trial associated with this prediction (NCT03510715) does not actually test fenofibrate — it tests alirocumab (a PCSK9 inhibitor) in pediatric HoFH patients, and was linked here only because of disease-label overlap, not because it provides direct fenofibrate evidence. This significantly weakens the practical evidentiary basis for this specific indication, despite the high raw TxGNN score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Evaluated **alirocumab** (PCSK9 inhibitor), not fenofibrate, in children/adolescents with HoFH. Linked to this candidate only via disease-label overlap — not direct fenofibrate evidence and should not be relied upon to support this repurposing direction. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Cohort | Pharmacological Research Communications | 22 patients with Type II hyperlipoproteinemia treated with fenofibrate 300 mg/day; one patient with HoFH showed the greatest fall in total and LDL cholesterol — the most directly relevant human data found. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocrine Practice | AACE/ACE dyslipidemia management guideline; general framework for lipid-lowering therapy, not HoFH-specific. |
| [24946816](https://pubmed.ncbi.nlm.nih.gov/24946816/) | 2014 | Review | Internal Medicine Journal | Liver transplantation for HoFH; discusses emerging lipid-lowering therapies as context, not fenofibrate efficacy data. |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart Journal | Notes fenofibrate's most definite indication is severe hypertriglyceridemia (TG >500 mg/dL) to reduce pancreatitis risk — not positioned as an HoFH therapy. |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Annals of the NY Academy of Sciences | Reviews pharmacologic/surgical treatment of dyslipidemic children, listing fenofibrate among agents used, largely in non-HoFH familial hypercholesterolemia. |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Review | Indian Heart Journal | General review of LDL-C lowering with statins and PCSK9 inhibitors; fenofibrate not a focus. |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | Pharmacokinetic study | Pharmacotherapy | Examines PK interactions of lomitapide (an approved HoFH adjunct) with commonly co-used lipid drugs including fenofibrate — relevant to co-administration safety, not fenofibrate monotherapy efficacy in HoFH. |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | Review | Current Atherosclerosis Reports | Dyslipidemia management in pregnancy; not specific to HoFH or fenofibrate. |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | Review | Pharmacotherapy | Reviews ezetimibe as a cholesterol absorption inhibitor; fenofibrate not discussed. |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Reviews atorvastatin pharmacology; included only via broad dyslipidemia topic overlap, not fenofibrate-specific. |

---

## South Africa Market Information

Fenofibrate is currently **not registered with SAHPRA** and has no licensed products recorded in this evidence pack (0 licenses, market status: Not Marketed).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: Key warnings, contraindications, and TFDA PI data are flagged in this evidence pack as a Blocking-severity data gap — this must be resolved before any safety-related decision can be made.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between fenofibrate's PPARα-mediated action and HoFH (a near-total LDL-receptor-deficiency disorder) is weak, and the only clinical trial associated with this specific candidate actually tests a different drug (alirocumab), not fenofibrate. The supporting literature is limited to small, decades-old cohort studies in general Type II hyperlipidemia rather than confirmed HoFH populations. Combined with the complete absence of SAHPRA registration and safety/PI data, this candidate does not currently meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA/SAHPRA-approved Professional Information (warnings, contraindications) — currently a Blocking data gap
- Formal, validated mechanism-of-action documentation for fenofibrate — currently a High-severity data gap
- Dedicated clinical evidence testing fenofibrate specifically (not PCSK9 inhibitors or other agents) in confirmed HoFH patients
- Re-evaluation against the model's higher-confidence candidate, **hyperlipoproteinemia** (rank 2, Evidence Level L1, decision stage S3, "Proceed with Guardrails"), which the evidence pack itself notes is closer to fenofibrate's existing core pharmacological use rather than true repurposing, and may represent a more actionable near-term direction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

