---
layout: default
title: Pantoprazole
parent: Model Prediction Only (L5)
nav_order: 359
evidence_level: L5
indication_count: 6
---

# Pantoprazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Pantoprazole: From Acid-Suppression Therapy to Active Peptic Ulcer Disease

## One-Sentence Summary

Pantoprazole is a proton pump inhibitor (PPI) that reduces stomach acid. The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**, and **3 clinical trials** and **19 publications** are linked to this prediction. This is an established acid-related use rather than a novel repurposing, so the report mainly confirms label use.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L1 (one completed Phase 3 registered trial plus several published RCTs, per the Evidence Pack scoring) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. From established pharmacology, pantoprazole irreversibly inhibits the H+/K+-ATPase (proton pump) of gastric parietal cells. This blocks the final step of acid secretion.

Peptic ulcers are acid-dependent. Profound acid suppression lets the ulcer heal and supports H. pylori eradication regimens, where a PPI is combined with antibiotics. Pantoprazole is already a standard agent for acid-related disease, so the prediction is mechanistically consistent. It also matches the direction of the published comparative trials (pantoprazole vs ranitidine or omeprazole in duodenal ulcer, and pantoprazole-based triple therapy).

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | Randomised, double-blind, active-controlled trial of ilaprazole vs pantoprazole triple therapy (7 days) for H. pylori eradication in gastric/duodenal ulcer. No results in the pack. |
| [NCT02197039](https://clinicaltrials.gov/study/NCT02197039) | N/A | Completed | 316 | Risk factors for choosing second-look endoscopy in bleeding peptic ulcer after high-dose PPI infusion. A management-strategy study, not a test of pantoprazole efficacy. |
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Effect of PPIs and statins on clopidogrel antiplatelet activity in PCI patients. A drug-interaction study, not ulcer treatment evidence. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18824852](https://pubmed.ncbi.nlm.nih.gov/18824852/) | 2008 | RCT | Digestion | Intermittent vs continuous pantoprazole infusion for rebleeding after endoscopic therapy in peptic ulcer bleeding |
| [10632647](https://pubmed.ncbi.nlm.nih.gov/10632647/) | 2000 | RCT | Aliment Pharmacol Ther | Pantoprazole and amoxycillin with azithromycin or clarithromycin for H. pylori eradication in duodenal ulcer |
| [12752349](https://pubmed.ncbi.nlm.nih.gov/12752349/) | 2003 | RCT | Aliment Pharmacol Ther | Three pantoprazole-based triple therapies for H. pylori eradication and gastric ulcer healing |
| [16677158](https://pubmed.ncbi.nlm.nih.gov/16677158/) | 2006 | RCT | J Gastroenterol Hepatol | Pantoprazole infusion as an adjunct to endoscopic treatment in peptic ulcer bleeding |
| [11802510](https://pubmed.ncbi.nlm.nih.gov/11802510/) | 2001 | RCT | Wien Klin Wochenschr | Amoxycillin and clarithromycin with either sucralfate or pantoprazole for H. pylori eradication in duodenal ulcer |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | Clinical study | Hepato-Gastroenterology | Lansoprazole vs pantoprazole in active duodenal ulcer and H. pylori eradication |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic review / network meta-analysis | Am J Gastroenterol | P-CABs vs PPIs for grade C/D esophagitis. Indirect relevance, since it concerns esophagitis rather than ulcer. |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Investig | Overview of pantoprazole pharmacology and its use in acid-related disease |
| [9017763](https://pubmed.ncbi.nlm.nih.gov/9017763/) | 1997 | Review | Pharmacotherapy | PPIs (omeprazole, lansoprazole, pantoprazole) compared with H2RAs for acid control |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | Preclinical (rat) | Inflammopharmacology | Pantoprazole plus mesenchymal stem cells in experimental gastric ulcer. Animal data only. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 45/11.4.3/0592 | Pentoz otc | Tablet |
| Reg. No. 44/11.4.3/0305 | Prazoloc powder for solution vial | Injection |
| Reg. No. 43/11.4.3/0844 | Mylan pantoprazole | Tablet |
| Reg. No. 43/11.4.3/0843 | Mylan pantoprazole | Tablet |

Both oral (tablet) and injectable forms are registered. The approved indication text and Essential Medicines List status are not in the Evidence Pack, so confirm them against the SAHPRA-approved Professional Information (PI).

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Peptic ulcer treatment is an established acid-related use of pantoprazole, supported by a completed Phase 3 trial and multiple published RCTs. The pack could not confirm the local approved indication text or safety data, and the clopidogrel interaction needs review. Hence guardrails are needed rather than an unconditional Go.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications and approved indications) to confirm that active peptic ulcer is on the local label for each registered product
- A check of dose and treatment duration against the label and guidelines
- An evaluation of the CYP2C19/clopidogrel interaction, especially for patients on dual antiplatelet therapy
- Monitoring of long-term PPI risks
- Mechanism of action data from DrugBank to close the MOA gap

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

