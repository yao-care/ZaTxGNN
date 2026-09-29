---
layout: default
title: Metoclopramide
parent: Moderate Evidence (L3-L4)
nav_order: 319
evidence_level: L4
indication_count: 5
---

# Metoclopramide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Metoclopramide: From Nausea/Vomiting and Gastric Motility Disorders to Gastric Ulcer

## One-Sentence Summary

Metoclopramide is a prokinetic and antiemetic drug that is marketed in South Africa. The SAHPRA registry extract does not state its approved indications, so the original use here is taken from the literature.
The TxGNN model predicts it may be effective for **gastric ulcer**, but the supporting evidence is weak: **2 registered clinical trials** (neither tests ulcer healing) and **20 publications**, mostly reviews and animal studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registry records. Literature describes antiemetic and gastric prokinetic use (PMID 6336644) |
| Predicted New Indication | Gastric ulcer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. From general pharmacology, metoclopramide is a dopamine D2 antagonist and 5-HT4 agonist that speeds gastric emptying. It is used for nausea, vomiting and delayed gastric emptying.

Gastric ulcer and the drug's original uses are both upper gastrointestinal conditions, and faster gastric emptying could reduce bile or acid reflux exposure. However, metoclopramide has no acid-suppressive or mucosal-healing action. Animal studies (PMID 2730234, 6436177, 28652516) address ulcer induction or gastric emptying after ulceration and do not show healing benefit.

The very high TxGNN score most likely reflects knowledge-graph proximity to gastrointestinal motility and symptom terms, not ulcer-healing biology. Any plausible role is adjunctive, for example improving endoscopic visualisation in bleeding or treating gastroparesis-type symptoms in ulcer patients.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Phase 4 | Unknown | 60 | Double-blind trial of metoclopramide premedication in upper GI bleeding. It asks whether repeat endoscopy, radiological intervention or surgery are reduced and whether visualisation improves. It does not test ulcer healing. Status is unverified |
| [NCT03747107](https://clinicaltrials.gov/study/NCT03747107) | N/A | Completed | 19 | Pharmacist and data-driven prescribing-safety quality-improvement programme in Scottish primary care. Not a drug efficacy trial, and metoclopramide has no evident specific role |

No SANCTR or PACTR registrations were identified in the evidence pack.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16807979](https://pubmed.ncbi.nlm.nih.gov/16807979/) | 2006 | Randomised double-blind trial (indirect endpoint) | Yonsei Med J | IV metoclopramide plus ranitidine versus saline on preoperative gastric contents in day-case gynaecologic surgery (n=40). Not an ulcer outcome |
| [6336644](https://pubmed.ncbi.nlm.nih.gov/6336644/) | 1983 | Review | Ann Intern Med | Pharmacology and clinical use: dopamine antagonism, antiemetic effect, gastrointestinal smooth muscle stimulation |
| [19225](https://pubmed.ncbi.nlm.nih.gov/19225/) | 1977 | Review | Drugs | Review of drugs for gastric and duodenal ulcer (no abstract available) |
| [797497](https://pubmed.ncbi.nlm.nih.gov/797497/) | 1976 | Review | Clin Pharmacokinet | Drugs and diseases (including gastric ulcer) that alter gastric emptying and hence oral drug absorption |
| [2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/) | 1989 | Animal study (rat) | Arch Int Pharmacodyn Ther | Ulcer-protective and antisecretory effects in aspirin-induced and pylorus-ligated models, compared with ranitidine |
| [6436177](https://pubmed.ncbi.nlm.nih.gov/6436177/) | 1984 | Animal study (guinea pig) | Indian J Physiol Pharmacol | Protection against experimental ulcers without changing gastric acidity, probably through better gastric drainage and less pyloric reflux |
| [28652516](https://pubmed.ncbi.nlm.nih.gov/28652516/) | 2017 | Animal study (rat) | J Smooth Muscle Res | Gastric emptying after acetic acid ulcers depends on ulcer site, with effects of prokinetic drugs. Not a healing study |
| [4779253](https://pubmed.ncbi.nlm.nih.gov/4779253/) | 1973 | Study type unclassified | Curr Med Res Opin | Bile reflux in gastric ulcer: effect of smoking, metoclopramide and carbenoxolone (no abstract; based on title only) |
| [775822](https://pubmed.ncbi.nlm.nih.gov/775822/) | 1976 | Study type unclassified | ZFA | Therapy of gastric and duodenal ulcer with metoclopramide (German; no abstract; based on title only) |
| [6106882](https://pubmed.ncbi.nlm.nih.gov/6106882/) | 1980 | Study type unclassified | Med Klin | Conservative treatment of gastric ulcer (German; no abstract; based on title only) |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 29/5.7.2/0781 | Pramalon | Injection | Not recorded in the registry extract |
| Reg. No. V/5.7.2/352 | Bio metoclopramide | Tablet | Not recorded in the registry extract |
| Reg. No. Q/5.7.2/228 | Metoclopramide 10 oethmaan | Tablet | Not recorded in the registry extract |
| Reg. No. L/5.7.2/0319 | Clopamon | Syrup | Not recorded in the registry extract |

Injectable, oral tablet and syrup forms are all available locally.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The evidence pack also carries these signals from the literature and the prediction analysis. The PI was not available to confirm them:
- A neurotoxicity report (PMID 3059051), mainly extrapyramidal effects, argues against pursuing a new indication without clear benefit.
- Prokinetics are contraindicated in mechanical obstruction or perforation.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trial tests ulcer healing, and the literature is mainly narrative reviews and animal studies. Metoclopramide does not address ulcer pathogenesis, for which acid suppression and *H. pylori* eradication remain the mainstay. The 99.93% score should be treated as a hypothesis-generating signal, not evidence of efficacy.

The lower-ranked predictions (gastroduodenitis, peptic ulcer disease, gastrojejunal ulcer, peptic ulcer perforation) are also on Hold. Peptic ulcer perforation looks like a knowledge-graph artefact and should not be pursued.

**To proceed, the following is needed:**
- SAHPRA package inserts for the four registered products (warnings, contraindications, approved indications). This is a blocking gap for safety screening.
- Mechanism of action data from DrugBank.
- Results and verified status of NCT05746377. If positive, it could support a narrow adjunctive role in endoscopic visualisation for upper GI bleeding, not ulcer healing.
- A clear defined clinical question, such as an adjunct for dysmotility symptoms in ulcer patients, and a comparison against standard acid-suppressive therapy.
- A risk-benefit review of extrapyramidal adverse effects for any new use.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

