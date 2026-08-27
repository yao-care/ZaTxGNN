---
layout: default
title: Felodipine
parent: 僅模型預測 (L5)
nav_order: 218
evidence_level: L5
indication_count: 7
---

# Felodipine
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

# Felodipine: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

> Felodipine is a dihydropyridine calcium channel blocker generally used for hypertension. The TxGNN model's top-ranked prediction for this drug is **pulmonary hypertension owing to lung disease and/or hypoxia** (WHO Group 3), but **0 clinical trials** and **none of the 20 retrieved publications** actually studied felodipine for this indication — the literature is limited to general hypoxia biology, and current clinical guidance cautions against calcium channel blockers in this specific condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (based on drug class knowledge — dihydropyridine CCB; no SA-specific label text available in this evidence pack) |
| Predicted New Indication | Pulmonary Hypertension owing to Lung Disease and/or Hypoxia (WHO Group 3) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, felodipine is a dihydropyridine L-type calcium channel blocker that produces selective vascular smooth muscle relaxation, and its efficacy in hypertension is well established.

On the surface, a vasodilator could plausibly reduce pulmonary vascular resistance in Group 3 pulmonary hypertension (PH secondary to lung disease/hypoxia). However, the evidence in this pack does not support that link: all 20 retrieved PubMed articles are basic-science reviews on hypoxia biology (brain aging, cognitive impairment, tumor hypoxia, immunology) — none of them evaluate felodipine, and none address treatment of Group 3 PH.

More importantly, dihydropyridine CCBs are known to blunt hypoxic pulmonary vasoconstriction (HPV), the physiological compensatory mechanism that redirects blood flow away from poorly ventilated lung regions. In patients with hypoxic lung disease, this can worsen ventilation-perfusion mismatch and lower blood oxygenation — making felodipine a potential safety concern rather than a therapeutic candidate for this indication. The high TxGNN score appears disconnected from the actual literature and clinical guidance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

None of the publications below evaluate felodipine directly; all are general hypoxia-biology literature retrieved by disease-term matching. Listed for transparency only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | Hypoxia's role in brain aging/neurodegeneration; not drug-specific |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | Basic science | Advanced Science | Hypoxia tolerance mechanism (NAT10/SEPT9/HIF-1α) in gastric cancer cells |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | Hypoxia-induced cognitive impairment; mechanistic review, not treatment |
| [33278780](https://pubmed.ncbi.nlm.nih.gov/33278780/) | 2021 | Basic science | Redox Biology | Glucose metabolism in keloid fibroblasts under hypoxia |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | Journal of Cellular Biochemistry | General hypoxia-mediated biological control across diseases |
| [31706510](https://pubmed.ncbi.nlm.nih.gov/31706510/) | 2019 | Review | Trends in Cancer | Deubiquitinases and hypoxia signaling in cancer |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clinical Oncology | Therapeutic modification of tumor hypoxia (radiotherapy context) |
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respiratory Care Clinics of North America | Mechanisms of hypoxemia; general respiratory physiology |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Review | Redox Biology | Hypoxia's role in multiple sclerosis pathology |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Review | Rev Med Inst Mex Seguro Soc | High-altitude hypobaric hypoxia and human adaptation |

*10 additional articles in the evidence pack are similarly general hypoxia-biology literature and are omitted here for brevity; none reference felodipine.*

---

## South Africa Market Information

Felodipine has no current SAHPRA registrations recorded in this evidence pack (market status: Not Marketed, 0 licenses).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*Note: A Blocking-severity data gap exists for SAHPRA warnings/contraindications, which must be resolved before any safety assessment can proceed for this candidate.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not supported by clinical trials or felodipine-specific literature, and the proposed mechanism runs counter to known CCB pharmacology in hypoxic lung disease (inhibition of compensatory hypoxic pulmonary vasoconstriction may worsen oxygenation). This is a case where model output and clinical evidence diverge — proceeding would require dedicated safety review, not just efficacy evidence.

**To proceed, the following is needed:**
- SAHPRA-approved PI (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action data from DrugBank
- Any felodipine-specific studies in Group 3 PH populations, should they emerge
- Specialist (pulmonology/cardiology) input on the HPV-inhibition safety signal before any further evaluation

---

### Note: Other Candidates in This Evidence Pack

This evidence pack (`TW-DB01023-multi`) screened 7 predicted indications for felodipine. Two ranked lower by TxGNN score but have materially stronger evidence than the top-ranked candidate above, and may warrant separate evaluation:

| Rank | Indication | Evidence Level | Decision | Note |
|------|-----------|----------------|----------|------|
| 7 | Prinzmetal (variant) angina | L2 | Proceed with Guardrails | 3 RCTs directly testing felodipine; well-established CCB class effect (coronary vasospasm relief) |
| 6 | Chronic pulmonary heart disease (cor pulmonale) | L3 | Research Question | 2 clinical/hemodynamic studies directly on felodipine; mechanism is a "double-edged sword" (same HPV-inhibition concern as above) |

These were not the subject of this report per the pack's ranking, but are flagged for the reviewing pharmacist's awareness since they represent stronger repurposing signals than rank 1.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

