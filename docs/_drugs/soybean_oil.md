---
layout: default
title: Soybean Oil
parent: 僅模型預測 (L5)
nav_order: 414
evidence_level: L5
indication_count: 10
---

# Soybean Oil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Soybean Oil: From Parenteral Nutrition Lipid Source to Esophageal Disease

## One-Sentence Summary

Soybean oil (DrugBank DB09422) is not currently registered with SAHPRA, and no formal original indication is recorded in this evidence pack — literature consistently describes it as a component of intravenous lipid emulsions used in parenteral/enteral nutrition. Of the 10 indications the TxGNN model predicted for this drug, only **Esophageal Disease** (rank 4, score 98.25%) has any supporting clinical trial or literature evidence — the other 9 (including the top-ranked amenorrhea) are pure model output with zero corroborating studies. This report focuses on Esophageal Disease as the only prediction that clears an initial evidence bar, supported by **3 clinical trials** and **10 publications**, though the mechanistic direction of effect is inconsistent.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in regulatory data; literature context indicates use as a lipid emulsion component in parenteral/enteral nutrition (e.g. Intralipid®) |
| Predicted New Indication | Esophageal Disease |
| TxGNN Prediction Score | 98.25% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a High-severity data gap, DG002). Based on the available literature, soybean oil is best understood as a source of long-chain polyunsaturated fatty acids (n-3/n-6 PUFA) delivered via intravenous lipid emulsion, most often studied in the context of post-surgical nutritional support rather than as a standalone therapeutic agent.

The link to esophageal disease is indirect. Several studies included in the evidence pack examine soybean oil-based lipid emulsions given to patients undergoing esophagectomy or esophageal cancer surgery — but these look at postoperative immune and inflammatory outcomes (PMID 10024108, 22457418, 24379010), not treatment of esophageal disease itself. Separately, a distinct thread of mechanistic and animal research suggests dietary fat, including soybean oil, may *increase* esophageal sensitivity to acid and influence the severity of reflux esophagitis (PMID 11911356, 22300015, 27716366) — a signal pointing toward risk rather than benefit. One completed trial testing fermented soybean supplementation for GERD (NCT06524271) is the closest to a direct therapeutic test, but it used a food supplement rather than pharmaceutical-grade soybean oil, was non-randomized/non-phased, and its relevance is graded only "B" (moderate).

Taken together, the evidence is directionally mixed rather than convergent: it does not clearly support a therapeutic mechanism for soybean oil in esophageal disease, and part of the literature raises a plausible risk signal instead.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06524271](https://clinicaltrials.gov/study/NCT06524271) | NA | Completed | 110 | Fermented soybean (FSB) supplementation tested for GERD symptom management; direct disease-relevant test but not a phased pharmaceutical RCT, and intervention is a food supplement, not soybean oil itself (relevance: B). |
| [NCT05680064](https://clinicaltrials.gov/study/NCT05680064) | NA | Completed | 86 | Chewing gum and tongue/lip/jaw exercises for xerostomia and dysphagia in Sjögren's syndrome; addresses swallowing symptoms but has no direct relationship to soybean oil (relevance: C). |
| [NCT03127345](https://clinicaltrials.gov/study/NCT03127345) | Phase 2 | Withdrawn (enrollment 0) | 0 | Compared omega-3 (Omegaven®) vs. standard soybean-based lipid emulsion (Intralipid®) on bone outcomes in infants with esophageal atresia; withdrawn before enrollment, no data generated (relevance: C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10024108](https://pubmed.ncbi.nlm.nih.gov/10024108/) | 1999 | RCT | Annals of Surgery | Soybean oil emulsion and EPA effects on stress response and immune function after esophageal cancer surgery — postoperative supportive care context, not disease treatment. |
| [22457418](https://pubmed.ncbi.nlm.nih.gov/22457418/) | 2013 | RCT | JPEN J Parenter Enteral Nutr | Slow infusion of soybean oil emulsion and its effect on plasma cytokines/T-cell proliferation after esophagectomy. |
| [22300015](https://pubmed.ncbi.nlm.nih.gov/22300015/) | 2012 | Cohort/Mechanistic | Neurogastroenterol Motil | Duodenal lipid intensifies esophageal acid perception via apolipoprotein A-IV/CCK signaling — suggests a symptom-provoking rather than protective role for fat. |
| [24379010](https://pubmed.ncbi.nlm.nih.gov/24379010/) | 2013 | Cohort | Nutrients | Compared lipid emulsions (olive oil-based vs. MCT/LCT) in parenteral nutrition of esophageal cancer surgical patients; soybean oil not the primary comparator. |
| [11911356](https://pubmed.ncbi.nlm.nih.gov/11911356/) | 2002 | Mechanistic | Dig Dis Sci | Intragastric fat infusion increased esophageal sensitivity to acid versus saline — a risk-direction mechanistic signal. |
| [17868414](https://pubmed.ncbi.nlm.nih.gov/17868414/) | 2007 | Animal study | Cancer Science | High soybean-oil diet altered bile acid composition and promoted Barrett's esophagus/adenocarcinoma development in a rat reflux model — potential harm signal. |
| [27716366](https://pubmed.ncbi.nlm.nih.gov/27716366/) | 2016 | Animal study | Lipids Health Dis | n-3/n-6 PUFA ratio affected severity of acute reflux esophagitis in rats; direction depended on fatty acid ratio, not soybean oil alone. |
| [9646301](https://pubmed.ncbi.nlm.nih.gov/9646301/) | 1998 | Review | Nutrition | n-3 vs n-6 PUFA effects on immune/metabolic outcomes in critical illness, including esophageal cancer patients; general nutritional review, not disease-specific. |
| [31795982](https://pubmed.ncbi.nlm.nih.gov/31795982/) | 2019 | Case report | BMC Pulm Med | Case of exogenous lipoid pneumonia associated with avocado/soybean unsaponifiables, noting association with esophageal abnormalities/GERD; safety signal, not efficacy. |
| [105637](https://pubmed.ncbi.nlm.nih.gov/105637/) | 1979 | Cohort (historical) | Am J Hosp Pharm | Case of essential fatty acid deficiency during fat-free TPN in a patient with esophageal-colonic anastomosis obstruction; illustrates soybean oil's role as an EFA source, not a treatment for esophageal disease. |

---

## South Africa Market Information

Soybean oil currently has no SAHPRA product registration under this evidence pack (0 licenses, market status: Not marketed).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note: safety data collection for this drug is currently blocked — no TFDA/SAHPRA package insert warnings or contraindications could be retrieved (data gap DG001, Blocking severity), so a safety pre-screen (S1 stage) cannot be completed until this is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Mechanism of action data is entirely absent, and the available literature on soybean oil and esophageal disease points in inconsistent directions — some studies suggest dietary fat may worsen esophageal acid sensitivity and reflux, while supportive-care studies only examine postoperative immune outcomes rather than disease treatment. No completed Phase 2/3 trial directly tests soybean oil for an esophageal indication, and the drug has no SAHPRA registration or market presence in South Africa.

**To proceed, the following is needed:**
- TFDA/SAHPRA package insert warnings and contraindications (blocking gap, DG001) — required before any safety pre-screen
- Mechanism of action data via DrugBank (DG002)
- A dedicated mechanistic study clarifying whether soybean oil-derived lipids are protective or provocative for esophageal disease, given the conflicting literature signals
- Confirmation of pharmaceutical-grade formulation and regulatory pathway, since the drug is currently unregistered in South Africa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

