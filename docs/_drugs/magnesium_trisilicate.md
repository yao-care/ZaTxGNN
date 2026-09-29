---
layout: default
title: Magnesium Trisilicate
parent: Model Prediction Only (L5)
nav_order: 306
evidence_level: L5
indication_count: 5
---

# Magnesium Trisilicate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Magnesium Trisilicate: From Antacid Use (Registered Indication Not Recorded) to Active Peptic Ulcer Disease

## One-Sentence Summary

Magnesium trisilicate is a classic antacid marketed in South Africa as a powder. Its registered indication is not recorded in the supplied data.
The TxGNN model predicts it may be useful for **active peptic ulcer disease**, but this top prediction has **0 clinical trials** and **0 publications** behind it.
Lower-ranked predictions (gastrojejunal ulcer, gastric ulcer) have **1 trial** and **about 20 mostly historical publications**, but the evidence is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (the registration record has no indication text) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general antacid pharmacology, magnesium trisilicate neutralises gastric acid and forms colloidal silica. This can protect the ulcer surface, so it is mechanistically plausible for acid-related mucosal disease.

The record lists no original indication, so it is unclear whether this is true repurposing or simply the drug's existing antacid use. The high score (99.86%) may reflect that known use rather than a new signal.

For related predicted indications:
- **Gastrojejunal ulcer:** an antacid's acid-neutralising effect is a plausible route to ulcer healing.
- **Peptic ulcer perforation:** this is an acute surgical complication, and an antacid has no clear role in the acute event. The score likely reflects proximity to peptic ulcer in the knowledge graph.
- **Gastroduodenitis:** symptomatic relief is plausible, but no supporting data were supplied.

---

## Clinical Trial Evidence

For the top prediction (active peptic ulcer disease), currently no related clinical trials are registered.

The only trial in the pack relates to a lower-ranked prediction (gastric ulcer):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07310927](https://clinicaltrials.gov/study/NCT07310927) | Phase 2/3 | Recruiting | 140 | Alginate vs sucralfate added to PPIs for GERD symptom relief. Magnesium trisilicate is not an arm and the condition is GERD, so it is only contextually related. |

---

## Literature Evidence

For the top prediction, currently no related literature is available. The table below covers the lower-ranked predictions (gastrojejunal ulcer and gastric ulcer). It shows 10 of about 20 records, and none of the shown titles addresses gastrojejunal (marginal) ulcer specifically.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14248445](https://pubmed.ncbi.nlm.nih.gov/14248445/) | 1965 | RCT | Br Med J | Double-blind trial of bismuth aluminate and magnesium trisilicate in peptic ulceration with gastric analysis. No abstract; magnesium trisilicate may be the comparator. |
| [6328685](https://pubmed.ncbi.nlm.nih.gov/6328685/) | 1984 | Clinical trial | S Afr Med J | 88 patients with gastric or duodenal ulcer. Ranitidine vs an aluminium hydroxide/magnesium trisilicate antacid (Gelusil) over 4 weeks. Duodenal ulcer healing was 74% on ranitidine and 63% on the antacid. The abstract is truncated. |
| [6368445](https://pubmed.ncbi.nlm.nih.gov/6368445/) | 1983 | Controlled trial (different agent) | Int J Tissue React | De-Nol (bismuth) vs an antacid mixture containing magnesium trisilicate in gastric ulcer, over 4 weeks. |
| [15425465](https://pubmed.ncbi.nlm.nih.gov/15425465/) | 1950 | Case series | Am J Dig Dis | 125 peptic ulcer patients treated with aluminium hydroxide and magnesium trisilicate plus mucin. |
| [20271751](https://pubmed.ncbi.nlm.nih.gov/20271751/) | 1947 | Case series | Arch Surg | Gastroscopic and clinical study of the same combination in peptic ulcer. |
| [20321118](https://pubmed.ncbi.nlm.nih.gov/20321118/) | 1938 | Case series | CMAJ | Magnesium trisilicate in the treatment of peptic ulcer. |
| [6547921](https://pubmed.ncbi.nlm.nih.gov/6547921/) | 1984 | Mechanistic study | Fortschr Med | 3 groups of 6 gastric ulcer patients. Sucralfate, aluminium hydroxide or magnesium trisilicate was applied to the ulcer under endoscopy and the local electrical potential difference was measured. |
| [4301560](https://pubmed.ncbi.nlm.nih.gov/4301560/) | 1968 | Clinical study (combination) | Wien Med Wochenschr | Antacid effect of a magnesium trisilicate–hyoscyamine combination (Neoplex B). |
| [6293043](https://pubmed.ncbi.nlm.nih.gov/6293043/) | 1982 | Review | Scand J Gastroenterol Suppl | Antacid therapy and changes in mineral metabolism (long-term safety consideration). |
| [15688172](https://pubmed.ncbi.nlm.nih.gov/15688172/) | 2005 | Case report/safety | Urologe A | Silica-containing urinary stones, a safety signal for long-term silicate use. |

**Limitations:** the evidence is dated (1938–1984), and several studies test combination products, which confounds attribution. The only controlled comparison with abstract data is the 1984 South African study, and it does not isolate magnesium trisilicate.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| E/11.4.1/1195 | Bisma-Rex Powder | Powder | Not stated in the registration record |

---

## Safety Considerations

Literature signals from the supplied records (not a substitute for the PI):
- **Long-term mineral metabolism:** a 1982 review of antacid therapy flags mineral metabolism changes with prolonged use.
- **Silica-containing urinary stones:** reported in the literature (PMID 15688172), relevant to long-term silicate use.
- **Absorption interactions:** a 1981 crossover study (PMID 7336470) tested an aluminium hydroxide–magnesium trisilicate antacid on phenytoin bioavailability. The abstract is truncated, so the result should be checked.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings, contraindications and drug interactions. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is supported only by the TxGNN score, with no trials or literature. The evidence for related ulcer indications is historical, indirect and confounded by combination products, so it does not establish a new indication. It is also unclear whether this is repurposing or the drug's existing antacid use.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indication), which is currently a blocking gap for safety screening
- Mechanism of action data (for example from DrugBank)
- Clarification of the drug's original registered indication, to tell repurposing from existing antacid use
- A focused review of the full literature set (about 20 records, only 10 reviewed here) for direct evidence in gastrojejunal ulcer and gastric ulcer
- Modern controlled data, if the drug is to be considered against current acid-suppression standards
- A long-term safety plan covering mineral metabolism, silica stones and absorption interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

