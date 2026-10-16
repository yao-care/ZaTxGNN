---
layout: default
title: Solifenacin
parent: Model Prediction Only (L5)
nav_order: 425
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Solifenacin: predicted new indication Polycystic kidney disease 3 with or without polycystic liver disease (evidence level L5). Approved use: Overactive bladder"
---

# Solifenacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Solifenacin: From Overactive Bladder to Polycystic Kidney Disease 3 (with or without Polycystic Liver Disease)

## One-Sentence Summary

Solifenacin is a selective muscarinic M3 receptor antagonist, originally used to treat overactive bladder.
The TxGNN model predicts it may be effective for **polycystic kidney disease 3 with or without polycystic liver disease**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. It is a graph-based prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Overactive bladder (the SAHPRA registration record contains no indication text; the indication is taken from the TxGNN knowledge graph) |
| Predicted New Indication | Polycystic kidney disease 3 with or without polycystic liver disease |
| TxGNN Prediction Score | 97.13% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, solifenacin is a muscarinic M3 antagonist that relaxes bladder smooth muscle, and its efficacy in overactive bladder is well established.

For the top-ranked prediction, **no mechanistic link has been established**. The high TxGNN score reflects graph-based proximity only. Nothing in the data compiled for this report documents a plausible role for muscarinic antagonism in cyst formation pathways (for example the PKD/GANAB/PRKCSH genes or cAMP signalling). Kidney-related network neighbours are the likely driver of the score. Any use in polycystic kidney disease would at most be symptomatic (lower urinary tract symptoms), not disease-modifying.

The other top-ranked predictions (thoracic malformation, renal-hepatic-pancreatic dysplasia, nephronophthisis-related syndromes, Joubert syndrome with renal defect, karyomegalic interstitial nephritis, polycystic kidney disease, subarachnoid haemorrhage, congenital analbuminemia) are likewise without credible mechanistic support or any trial or literature evidence. Many are genetic ciliopathies or developmental disorders unrelated to muscarinic receptor antagonism.

The only prediction with supporting literature is **low compliance bladder** (rank 7, score 95.37%, evidence level L3). It is biologically plausible, since antimuscarinics reduce detrusor overactivity and can improve bladder capacity and compliance. However, it overlaps closely with the original indication and is better viewed as an extension to neurogenic detrusor overactivity than as true repurposing. It is discussed below for context.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction. No trials were registered for the low compliance bladder prediction either, and no SANCTR or PACTR identifiers were available.

## Literature Evidence

No literature is available for the top-ranked prediction (polycystic kidney disease 3). The table below lists the most relevant literature for the best-supported alternative, **low compliance bladder**. Only titles and partial abstracts were available, so direct measurement of bladder compliance as an outcome cannot be confirmed for most of these papers.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25435915](https://pubmed.ncbi.nlm.nih.gov/25435915/) | 2014 | RCT | Ther Adv Urol | Cyclic vs continuous trospium plus solifenacin combination for severe OAB in elderly patients, with focus on compliance |
| [27928426](https://pubmed.ncbi.nlm.nih.gov/27928426/) | 2016 | RCT | Ther Adv Urol | Treatment compliance of working patients on high-dose antimuscarinic therapy |
| [25170796](https://pubmed.ncbi.nlm.nih.gov/25170796/) | 2014 | Comparative effectiveness study | Urol Int | Low- and standard-dose trospium plus solifenacin for moderate OAB in elderly patients |
| [32007426](https://pubmed.ncbi.nlm.nih.gov/32007426/) | 2020 | Long-term phase 3 open-label studies | J Pediatr Urol | Long-term efficacy and safety of solifenacin in children aged 6 months to 18 years with neurogenic detrusor overactivity |
| [25656013](https://pubmed.ncbi.nlm.nih.gov/25656013/) | 2015 | Retrospective clinical study | Hinyokika Kiyo | Mirabegron added to anticholinergics in 7 patients with anticholinergic-resistant neurogenic bladder (detrusor overactivity or low compliance) |
| [16465186](https://pubmed.ncbi.nlm.nih.gov/16465186/) | 2006 | Review | Br J Pharmacol | Role of muscarinic M2/M3 receptors in bladder function and antimuscarinic therapy |
| [17594185](https://pubmed.ncbi.nlm.nih.gov/17594185/) | 2007 | Review | Expert Opin Investig Drugs | Overview of OAB treatments in early-phase trials |
| [38256949](https://pubmed.ncbi.nlm.nih.gov/38256949/) | 2024 | Cohort | Pharmaceuticals (Basel) | Adherence to and reasons for discontinuing solifenacin in OAB patients |
| [25503446](https://pubmed.ncbi.nlm.nih.gov/25503446/) | 2015 | Prospective observational | Int Urol Nephrol | Association between dry mouth and solifenacin treatment in OAB |
| [15716204](https://pubmed.ncbi.nlm.nih.gov/15716204/) | 2005 | Open-label long-term study | Eur Urol | Safety, tolerability and persistence with solifenacin over up to 1 year in OAB |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 56/21.12/1063 | Firsoltam | Mrt | Not recorded in the data compiled for this report |

One valid single-ingredient registration exists. Essential Medicines List (EML) inclusion status was not available in the data compiled for this report.

## Safety Considerations

Formal label warnings and contraindications were not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Contraindication signals from the knowledge graph** (not label text; to be verified against the PI):
- Long QT syndrome (including familial), torsades de pointes
- Liver failure and liver disease
- Gallbladder disease
- Angle-closure (closed-angle) glaucoma
- Bladder neck obstruction

**Drug interactions** (100 interactions were found; the main ones are listed):
- **Major:** clarithromycin, dolasetron, potassium citrate
- **Moderate:** other anticholinergic or antimuscarinic agents (atropine, hyoscyamine, glycopyrronium, clidinium, dicyclomine, trospium); morphine, loperamide and eluxadoline; aprepitant, dexamethasone, cimetidine, famotidine; and laxatives or bowel preparations (bisacodyl, picosulfuric acid, polyethylene glycol)

Additional caution applies to the ranked predictions: solifenacin's anticholinergic activity could cause central nervous system adverse effects in acute neurological illness (relevant to the subarachnoid haemorrhage prediction).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (polycystic kidney disease 3) rests on graph-based scoring alone, with no clinical trials, no literature and no plausible mechanism. The evidence level is L5. The only prediction with literature support (low compliance bladder, L3) is an extension of the existing bladder indication rather than true repurposing. It could be treated as a research question.

**To proceed, the following is needed:**
- Mechanism of action data to assess any link to cystogenesis pathways
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Preclinical or mechanistic studies in polycystic kidney disease models, if this prediction is to be pursued
- For the low compliance bladder / neurogenic detrusor overactivity direction: full-text review of the supplied studies to confirm that bladder compliance was measured as an outcome, and a check of the SAHPRA registration for the neurogenic detrusor overactivity indication
- Route and formulation compatibility assessment, which is currently pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

