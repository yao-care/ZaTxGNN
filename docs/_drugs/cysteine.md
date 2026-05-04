---
layout: default
title: Cysteine
parent: 僅模型預測 (L5)
nav_order: 155
evidence_level: L5
indication_count: 10
---

# Cysteine
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

# Cysteine: From Amino Acid Supplement to Dry Eye Syndrome

## One-Sentence Summary

Cysteine is a naturally occurring amino acid and a rate-limiting precursor of glutathione (GSH), with no specific approved therapeutic indication currently listed in South Africa. The TxGNN model predicts it may be effective for **Dry Eye Syndrome**, with **7 clinical trials** and **20 publications** currently supporting this direction. Its derivative N-acetylcysteine (NAC) has been directly studied in randomised controlled trials for dry eye and Sjögren's disease-related dryness symptoms.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved therapeutic indication on record |
| Predicted New Indication | Dry Eye Syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Cysteine is the rate-limiting precursor for biosynthesis of glutathione (GSH), the body's principal intracellular antioxidant. Dry eye disease (DED) is characterised by tear film instability and ocular surface inflammation, both of which are driven by excessive reactive oxygen species (ROS). By replenishing cysteine, GSH synthesis is enhanced, enabling more effective scavenging of ROS and protection of the corneal and conjunctival epithelium. This antioxidant pathway — Cysteine → GSH synthesis → ROS clearance → ocular surface protection — provides a clear mechanistic rationale for the predicted indication.

N-acetylcysteine (NAC), the N-acetylated derivative of cysteine, adds a complementary mucolytic mechanism: it cleaves disulphide bonds in mucin glycoproteins, reducing mucus viscosity and improving tear film quality. This dual action (antioxidant + mucolytic) is particularly relevant for mucin-deficient dry eye and Sjögren's syndrome-associated dryness, where both oxidative stress and mucus accumulation contribute to ocular surface damage.

Furthermore, thiolated chitosan (chitosan-cysteine conjugates) have been developed as bioadhesive ocular drug delivery platforms that exploit the thiol groups of cysteine to form disulphide bonds with cysteine-rich mucus glycoproteins, prolonging corneal retention time. Multiple preclinical and clinical studies have validated this approach, reinforcing the biological plausibility of cysteine-based therapies for dry eye.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04793646](https://clinicaltrials.gov/study/NCT04793646) | N/A (RCT) | Completed | 60 | Prospective randomised, double-blind, placebo-controlled trial of NAC for dryness symptoms in primary Sjögren's syndrome. Most directly relevant evidence. |
| [NCT04440280](https://clinicaltrials.gov/study/NCT04440280) | Phase 2 | Recruiting | 45 | Investigating topical NAC eye drops for Fuchs' endothelial corneal dystrophy, targeting ROS-mediated oxidative stress — mechanism overlaps with DED. |
| [NCT03525678](https://clinicaltrials.gov/study/NCT03525678) | Phase 2 | Completed | 221 | Belantamab mafodotin (DREAMM 2) study; corneal toxicity/dry eye reported as an adverse event — indirect relevance only. |
| [NCT04162210](https://clinicaltrials.gov/study/NCT04162210) | Phase 3 | Active, not recruiting | 325 | Belantamab mafodotin (DREAMM 3) — ocular toxicity including dry eye as a key safety concern; indirect relevance. |
| [NCT01064830](https://clinicaltrials.gov/study/NCT01064830) | Phase 2 | Completed | 21 | Cyclosporine 0.05% for brittle nail syndrome; cysteine deficiency mentioned as aetiological factor — indirect relevance. |

**Note:** The most pivotal trial is NCT04793646 — the only completed, directly relevant RCT examining NAC (a cysteine derivative) specifically for dry eye-related symptoms.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28441068](https://pubmed.ncbi.nlm.nih.gov/28441068/) | 2017 | RCT | J Ocul Pharmacol Ther | Controlled, randomised, double-blind study evaluating chitosan-NAC (C-NAC) eye drops on tear film thickness in DES patients. |
| [39360368](https://pubmed.ncbi.nlm.nih.gov/39360368/) | 2024 | RCT | Clin Exp Rheumatol | Randomised placebo-controlled double-blind trial assessing NAC efficacy for relieving dryness in Sjögren's disease. |
| [34339721](https://pubmed.ncbi.nlm.nih.gov/34339721/) | 2022 | Systematic Review | Surv Ophthalmol | Comprehensive review of topical NAC in ocular therapeutics — mucolytic, ROS-scavenging, and anti-inflammatory actions across 106 references. |
| [16334742](https://pubmed.ncbi.nlm.nih.gov/16334742/) | 2005 | Clinical Study | Acta Med Croatica | Comparison of local acetylcysteine vs artificial tears in DES management; NAC regulated mucus secretion and reduced accumulation. |
| [40123221](https://pubmed.ncbi.nlm.nih.gov/40123221/) | 2025 | Preclinical | Adv Mater | Nano-formulation of catalase self-assembled with cysteine-modified chitosan for DED treatment; demonstrated ROS elimination and ocular surface protection. |
| [39842600](https://pubmed.ncbi.nlm.nih.gov/39842600/) | 2025 | Preclinical | Int J Biol Macromol | NAC-chitosan conjugate modified dexamethasone NLC for DED; enhanced permeability, precorneal retention, and reduced inflammation. |
| [36581034](https://pubmed.ncbi.nlm.nih.gov/36581034/) | 2023 | Preclinical | Int J Biol Macromol | L-Cysteine conjugated chondroitin sulfate nanostructured lipid carriers for dry eye; improved corneal permeation and retention. |
| [25701684](https://pubmed.ncbi.nlm.nih.gov/25701684/) | 2015 | Basic Research | Exp Eye Res | ROS-activated NLRP3 inflammasomes in hyperosmolarity-stressed corneal epithelial cells and DED patients — supports antioxidant mechanism. |
| [3898475](https://pubmed.ncbi.nlm.nih.gov/3898475/) | 1985 | Clinical Observation | Trans Ophthalmol Soc UK | Review of topical drugs and preservatives effects on tears and corneal epithelium in dry eye. |
| [30025127](https://pubmed.ncbi.nlm.nih.gov/30025127/) | 2018 | Preclinical | Invest Ophthalmol Vis Sci | Topical NAC effects on tears and ocular surface; established mucin-deficient dry eye animal model. |

## South Africa Market Information

Cysteine (DB00151) currently has **no SAHPRA registrations** and is **not marketed** in South Africa as a registered medicine. N-acetylcysteine (NAC), the clinically relevant derivative, may be available under separate registrations but was not captured in this drug-specific query. Healthcare professionals should verify NAC availability through the SAHPRA database independently.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information, as no SAHPRA-registered product exists for cysteine in South Africa at this time. Report adverse drug reactions to SAHPRA.

**General pharmacological considerations for cysteine/NAC:**
- NAC is generally well tolerated when used topically (ophthalmic) or systemically
- Oral NAC may cause gastrointestinal disturbance (nausea, vomiting, diarrhoea)
- Topical ocular NAC may cause transient stinging or burning upon instillation
- Hypersensitivity reactions are rare but documented
- Detailed safety data, including drug-drug interactions, warnings, and contraindications specific to the South African context, require SAHPRA-approved product labelling

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
There is a completed randomised, double-blind, placebo-controlled trial (NCT04793646) directly studying NAC for Sjögren's disease-related dry eye, and an additional published RCT (PMID 28441068) evaluating chitosan-NAC eye drops for DES. The mechanistic rationale (antioxidant via GSH replenishment + mucolytic via disulphide bond cleavage) is well established. Multiple preclinical studies further support the ocular surface therapeutic potential. Evidence reaches L2 (1 completed Phase 2/3 equivalent RCT).

**To proceed, the following is needed:**
- **SAHPRA regulatory pathway clarification**: Cysteine is not currently registered; determine whether NAC ophthalmic formulations could be imported via Section 21 or whether a new registration is required
- **Detailed mechanism of action (MOA) data**: Obtain full DrugBank pharmacology profile for cysteine/NAC
- **Formulation assessment**: Confirm availability or feasibility of ophthalmic-grade NAC preparations suitable for the South African market
- **Safety data compilation**: Obtain comprehensive Professional Information for NAC from international regulatory sources (e.g., EMA, TGA) pending SAHPRA registration
- **Pharmacoeconomic analysis**: Compare cost-effectiveness against existing DED treatments available in South Africa (e.g., cyclosporine 0.05%, lifitegrast, artificial tears)
- **Local clinical validation**: Consider a confirmatory study in the South African population, particularly given the high prevalence of Sjögren's syndrome-associated dry eye

---

*Disclaimer: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All predictions are generated by the TxGNN model and should be interpreted by qualified healthcare professionals.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

