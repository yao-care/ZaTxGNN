---
layout: default
title: Methylcellulose
parent: Model Prediction Only (L5)
nav_order: 318
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Methylcellulose: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not stated in the SAHPRA registration data compiled for this report"
---

# Methylcellulose
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

# Methylcellulose: From an Unspecified Original Indication to Osteoarthritis

## One-Sentence Summary

Methylcellulose is a cellulose ether (a bulk-forming agent and pharmaceutical excipient). The SAHPRA registration data compiled for this report does not state an approved indication.
The TxGNN model predicts it may be useful for **osteoarthritis**, but there are **0 registered clinical trials** and only **preclinical formulation studies** in which methylcellulose serves as a gel or hydrogel carrier for other drugs.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data compiled for this report |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 95.21% |
| Evidence Level | L4 (preclinical/formulation studies only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, methylcellulose is a non-absorbed cellulose ether that acts as a bulk-forming agent in the gut and is widely used as an excipient. It has no established systemic pharmacological activity.

The osteoarthritis literature retrieved uses methylcellulose as a thermosensitive hydrogel or gel base to deliver active agents (meloxicam, celecoxib, curcumin, proanthocyanidin, stem-cell spheroids). Any therapeutic effect in those studies comes from the delivered drug, not from methylcellulose itself. The high TxGNN score most likely reflects network proximity to these co-formulated osteoarthritis drugs rather than a true pharmacological mechanism.

A possible indirect role as a lubricating, viscosupplement-like or sustained-release vehicle is plausible, but it is unproven.

## Clinical Trial Evidence

Currently no related clinical trials registered. No SANCTR or PACTR entries were identified in the data compiled for this report.

## Literature Evidence

The literature below is all preclinical or formulation work. No human efficacy studies of methylcellulose for osteoarthritis were found.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41054792](https://pubmed.ncbi.nlm.nih.gov/41054792/) | 2025 | Preclinical formulation | Artif Cells Nanomed Biotechnol | Injectable methylcellulose–carboxymethyl chitosan hydrogel carrying amniotic fluid stromal cell spheroids for cartilage regeneration |
| [40354857](https://pubmed.ncbi.nlm.nih.gov/40354857/) | 2025 | Preclinical formulation | Int J Biol Macromol | Transdermal F127/methylcellulose hydrogel with nanozymes for osteoarthritis relief via immunomodulatory pathways |
| [36079990](https://pubmed.ncbi.nlm.nih.gov/36079990/) | 2022 | Formulation optimisation | Nanomaterials (Basel) | Proanthocyanidin transferosomes loaded into a 4% methylcellulose gel for osteoarthritis |
| [32027902](https://pubmed.ncbi.nlm.nih.gov/32027902/) | 2020 | Preclinical formulation | Int J Biol Macromol | Injectable carboxymethyl chitosan–methylcellulose–pluronic hydrogel encapsulating meloxicam nanoparticles |
| [30767746](https://pubmed.ncbi.nlm.nih.gov/30767746/) | 2020 | Formulation | Curr Rheumatol Rev | Herbal topical patch with curcumin and Arnica montana for osteoarthritis |
| [26752990](https://pubmed.ncbi.nlm.nih.gov/26752990/) | 2015 | Formulation | Res Pharm Sci | Iontophoretic delivery of celecoxib from gel formulations that include cellulose derivatives |
| [21959817](https://pubmed.ncbi.nlm.nih.gov/21959817/) | 2011 | Formulation | Pak J Pharm Sci | Meloxicam solubility enhancement by ternary complexation |

Two further retrieved papers (grapiprant in dogs, agmatine in dogs) concern different drugs and have no therapeutic link to methylcellulose, so they are not counted as supporting evidence.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| E1246 (OM) | Medigel | Suspension | Not stated in the data compiled for this report |

One valid single-ingredient registration exists. Essential Medicines List (EML) inclusion status was not available in the data compiled for this report.

## Safety Considerations

**Drug Interactions**

A total of 25 interacting drugs were identified. The data shown covers 20 of them, mostly rated Minor:

- **Moderate:** lactulose.
- **Minor:** antidiabetic agents (acarbose, miglitol, chlorpropamide, glimepiride, glipizide, glyburide, tolazamide, nateglinide, repaglinide, and several insulins), and laxatives or gut-active agents (picosulfuric acid, linaclotide).

Bulk-forming agents can alter the absorption of co-administered oral drugs, so separating dosing times is a reasonable precaution.

For warnings and contraindications, please refer to the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for osteoarthritis is preclinical formulation work in which methylcellulose is a delivery vehicle, not an active agent. The model score likely reflects excipient use in co-formulated drugs rather than a true drug effect. No clinical trials exist.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (indication, warnings and contraindications) for Medigel, which is currently missing and blocks safety screening
- Mechanism of action data (for example from DrugBank)
- Evidence that methylcellulose itself, rather than a co-delivered drug, has an effect in osteoarthritis
- Clarification of the route and formulation needed (the registered product is a suspension, whereas the studies used injectable or topical hydrogels)

## Other Predicted Indications (Reference Only)

The other top-ranked predictions have no clinical trials, and their literature is either indirect or absent. All are rated Hold.

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Enterocolitis | 93.73% | L5 | Theoretical stool-consistency effect only. May be inappropriate in acute inflammatory bowel conditions |
| Alopecia | 93.54% | L4 | Literature concerns minoxidil nanocrystal delivery with methylcellulose as an excipient, not a hair-growth effect |
| Pseudoachondroplasia | 93.45% | L5 | Genetic (COMP) disorder with no plausible mechanism |
| Hypotrichosis simplex of the scalp | 93.28% | L5 | No link to hair follicle biology |
| Congenital hypotrichosis milia | 93.15% | L5 | Model score only |
| Diffuse alopecia areata | 92.92% | L5 | Autoimmune condition. Methylcellulose has no known immunomodulatory activity |
| Insomnia | 92.90% | L5 | Not absorbed, no CNS activity |
| Exercise-induced malignant hyperthermia | 92.78% | L5 | Muscle calcium-handling disorder with no plausible mechanism |
| Osteoarthritis susceptibility | 92.76% | L5 | Genetic susceptibility phenotype, not a treatable disease state |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

