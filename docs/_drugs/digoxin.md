---
layout: default
title: Digoxin
parent: Moderate Evidence (L3-L4)
nav_order: 176
evidence_level: L4
indication_count: 6
---

# Digoxin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

# Digoxin: From Cardiac Glycoside Therapy to Prinzmetal Angina

## One-Sentence Summary

Digoxin is a cardiac glycoside, generally used for heart failure and certain arrhythmias. The registration data supplied does not state its approved indication.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but this rests on a graph-based score alone, with **0 clinical trials** and only **2 general publications**, neither showing digoxin benefit.
The mechanistic rationale is weak, and the evidence supports a **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. On general pharmacology, digoxin inhibits Na+/K+-ATPase, which raises intracellular calcium and increases cardiac contractility.

This does not obviously support use in Prinzmetal angina, which is caused by coronary vasospasm. Increased intracellular calcium and vascular tone could plausibly be unfavourable in that setting. The high TxGNN score reflects a pattern in the knowledge graph, not a demonstrated pharmacological link. No clear mechanistic rationale has been identified.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9206110](https://pubmed.ncbi.nlm.nih.gov/9206110/) | 1996 | Review | Chin Med Sci J | 30 patients with angina decubitus had severe coronary obstruction and raised myocardial oxygen consumption. This describes the mechanism of a different angina type, with no digoxin efficacy data |
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiol Pharmacol Bulg | General review of chronopharmacology in antihypertensive treatment. No direct link to digoxin in Prinzmetal angina |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| G.2846 | Lanoxin | Tablet (oral) |

The registration record appears twice under the same number. No approved indication text was supplied.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a knowledge-graph score alone. There are no trials, the two publications do not show digoxin benefit, and the general pharmacology may be unfavourable in coronary vasospasm. Safety data for South Africa is also missing, which blocks progression to safety screening.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indication)
- Mechanism of action data from DrugBank, to test the mechanistic link
- Any direct clinical or mechanistic evidence for digoxin in vasospastic angina

**Other predicted indications (all Hold):**

| Rank | Indication | Score | Evidence Level | Note |
|------|------|------|------|------|
| 2 | Duodenal obstruction | 99.70% | L5 | No plausible mechanism. The only paper is a prune-belly syndrome case report |
| 3 | Duodenal ulcer | 99.59% | L4 | Literature covers drug interactions (cimetidine, PPIs) and glycoside toxicity presenting as nausea and vomiting, not efficacy |
| 4 | Duodenogastric reflux | 99.53% | L5 | No literature or trials |
| 5 | Susceptibility to ischemic stroke (obsolete term) | 99.29% | L5 | Obsolete ontology term; needs remapping before review |
| 6 | Hypoalphalipoproteinemia | 99.20% | L5 | No established link to HDL metabolism |

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

