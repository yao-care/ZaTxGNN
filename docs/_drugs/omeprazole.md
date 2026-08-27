---
layout: default
title: Omeprazole
parent: 僅模型預測 (L5)
nav_order: 345
evidence_level: L5
indication_count: 10
---

# Omeprazole
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

# Omeprazole: From Peptic Ulcer Disease to Duodenogastric Reflux

## One-Sentence Summary

> Omeprazole is a proton pump inhibitor (PPI) whose established, original use is the treatment of peptic ulcer disease and other acid-related gastrointestinal disorders.
> The TxGNN model's top-ranked prediction for this drug is **Duodenogastric Reflux**, supported by **1 clinical trial** and **20 publications** —
> but the trial is diagnostic (not therapeutic) and several of the publications are preclinical studies suggesting a potential **risk signal** rather than a clear efficacy signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease / acid-related GI disorders (PPI class) — noted in the evidence pack's own rationale for the "active peptic ulcer disease" candidate; SAHPRA-specific label text is not available |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L3 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold (evidence pack stage: S1 / "Research Question") |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this drug is not available in the evidence pack. Based on known pharmacology, omeprazole is a proton pump inhibitor that irreversibly blocks the H+/K+-ATPase ("proton pump") in gastric parietal cells, suppressing gastric acid secretion. Its efficacy in acid-related disorders such as peptic ulcer disease is well established.

Duodenogastric reflux (DGR), however, is driven primarily by **bile and duodenal content** entering the stomach — a mechanism distinct from acid overproduction. Omeprazole's acid-suppressing action does not directly target biliary reflux, which limits the mechanistic rationale for treating DGR itself. Several cohort studies in this evidence pack (e.g., in Barrett's oesophagus patients) do show that omeprazole reduces measurable acid and, in some cases, biliary reflux exposure — but the reduction in bile reflux appears to be a secondary consequence of acid suppression rather than a direct pharmacological effect.

More importantly, multiple preclinical studies included in the evidence base (PMID 10389684, 15052437, 8943968) report that gastric acid blockade with omeprazole **potentiates** mucosal growth stimulation and gastric carcinogenesis in animal models of induced duodenogastric reflux. This is flagged directly in the evidence pack's own rationale as a "direction unclear, with a potential risk signal." Taken together, the prediction is mechanistically plausible as a research question but is not yet supported by therapeutic-intent clinical evidence, and carries an identified safety caveat that must be resolved before further development.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02685150](https://clinicaltrials.gov/study/NCT02685150) | N/A | Completed | 157 | Diagnostic study evaluating endoscopic tri-modal imaging (NBI/AFI/WLI) to distinguish functional dyspepsia from reflux disease (acid or bile). Not a treatment trial and has no direct bearing on omeprazole's efficacy for DGR. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10994616](https://pubmed.ncbi.nlm.nih.gov/10994616/) | 2000 | Cohort | Scand J Gastroenterol | Long-term omeprazole therapy appears to reduce antral duodenogastric reflux in Barrett's oesophagus. |
| [9824338](https://pubmed.ncbi.nlm.nih.gov/9824338/) | 1998 | Cohort | Gut | Omeprazole 20 mg twice daily reduced duodenogastric and duodenogastro-oesophageal bile reflux in Barrett's oesophagus. |
| [9841990](https://pubmed.ncbi.nlm.nih.gov/9841990/) | 1998 | Cohort | J Gastrointest Surg | Medical acid suppression and Nissen fundoplication both studied for bile reflux control in benign/malignant Barrett's oesophagus. |
| [10389684](https://pubmed.ncbi.nlm.nih.gov/10389684/) | 1999 | Preclinical | Dig Dis Sci | **Safety signal:** gastric acid blockade with omeprazole promoted gastric carcinogenesis in a rat model of induced duodenogastric reflux. |
| [33027361](https://pubmed.ncbi.nlm.nih.gov/33027361/) | 2020 | Preclinical | Acta Cir Bras | Investigated whether omeprazole protects gastric mucosa in rats with induced duodenogastric reflux; carcinogenesis-related endpoint. |
| [8943968](https://pubmed.ncbi.nlm.nih.gov/8943968/) | 1996 | Preclinical | Dig Dis Sci | Duodenogastric reflux caused foregut mucosal growth stimulation that was **potentiated** by gastric acid blockade (omeprazole arm). |
| [16641575](https://pubmed.ncbi.nlm.nih.gov/16641575/) | 2006 | Prospective study | J Pediatr Gastroenterol Nutr | Prospective study of PPI (omeprazole) therapy for oesophageal bile reflux in children. |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Case series | Eur J Pediatr | Describes primary duodenogastric reflux in six children/adolescents, refractory to classical antacid therapy. |
| [19491829](https://pubmed.ncbi.nlm.nih.gov/19491829/) | 2009 | Cohort | Am J Gastroenterol | Compared degree of duodenogastroesophageal and acid reflux in GERD patients who did vs. did not respond to once-daily PPI. |
| [11232672](https://pubmed.ncbi.nlm.nih.gov/11232672/) | 2001 | Cohort | Am J Gastroenterol | Increased acid and bile reflux found in Barrett's oesophagus vs. reflux oesophagitis; examined effect of PPI therapy. |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for standard safety information. Report adverse drug reactions to SAHPRA.

**Research-specific caution (not part of standard PI):** Independent of routine safety labelling, multiple preclinical studies identified in the literature evidence above (PMID 10389684, 15052437, 8943968) indicate that gastric acid suppression with omeprazole may **potentiate** mucosal growth stimulation and carcinogenesis in animal models of duodenogastric reflux. This signal is specific to the DGR context and should be explicitly weighed before any further clinical development of this indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for this indication consists of one diagnostic (non-therapeutic) clinical trial and a literature base dominated by cohort/observational and preclinical studies (Evidence Level L3), consistent with the evidence pack's own "Research Question" / Stage S1 classification. Critically, preclinical data suggest a possible carcinogenesis-potentiation risk with acid suppression in the DGR setting, which argues against proceeding without further clarification.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings/contraindications) — currently a **Blocking** data gap (DG001) that prevents completion of the S1 safety initial assessment
- Confirmed mechanism-of-action data (DG002) to properly assess mechanistic relevance to duodenogastric reflux
- A therapeutic-intent clinical trial specifically targeting duodenogastric reflux as the primary endpoint (the only trial identified is diagnostic, not interventional)
- Dedicated evaluation of the carcinogenesis-potentiation signal seen in preclinical DGR models before any patient-facing use is considered
- SAHPRA registration status confirmation, since the drug is currently recorded as not marketed with 0 licenses on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

