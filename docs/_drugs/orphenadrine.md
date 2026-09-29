---
layout: default
title: Orphenadrine
parent: Model Prediction Only (L5)
nav_order: 354
evidence_level: L5
indication_count: 7
---

# Orphenadrine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Orphenadrine: From Anticholinergic Muscle Relaxant to Retinal Dystrophy

## One-Sentence Summary

Orphenadrine is an oral anticholinergic muscle relaxant, marketed in South Africa as tablets, and the registration data do not state its approved indication.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but there are **0 clinical trials** and **15 retrieved publications**, none of which concern orphenadrine.
The high score looks like a knowledge-graph artifact, not real supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available. Orphenadrine is generally described as an anticholinergic, H1-antihistamine and NMDA antagonist with muscle relaxant effects.

**No plausible link was found** between these actions and inherited retinal degeneration. The 15 retrieved papers are general reviews and case reports on congenital eye and orbital anomalies, such as extraocular muscle fibrosis, ptosis and orbital infections. They appear to have been matched on disease keywords only.

The model's score of 99.29% therefore should not be read as clinical support.

Other predictions for this drug (congenital glycosylation disorder, polymicrogyria, Charcot-Marie-Tooth 1G, and X-linked myopias) also have no mechanistic rationale and no trials. The X-linked myopias have only a weak analogy to atropine, and systemic anticholinergic effects on vision would be a concern.

The only prediction with real literature is **schizophrenia** (rank 5, evidence level L3). There, orphenadrine has been studied as an adjunct for antipsychotic-induced parkinsonism, not for core psychosis. It is worth assessing separately.

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR or PACTR).

## Literature Evidence

None of these publications studies orphenadrine. They are ordered by study type, with reviews first and then case reports and unclassified items.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | Orbital infections, mainly sinusitis-related cellulitis |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | Clinical approach to diplopia |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Congenital ptosis |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital anomalies of lens shape |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler syndrome complex (vitreoretinal degeneration) |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | Imaging of pediatric ocular pathologies |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Review | Arch Ophthalmol | Clinical features and outcomes of orbital arteriovenous malformations |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | Am J Ophthalmol | Two cases of unilateral cryptophthalmia |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case report | J Neuroophthalmol | Trochlear-oculomotor synkinesis in a child |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case report | Optom Vis Sci | Synergistic divergence in congenital fibrosis of extraocular muscles |

Five further papers (PMIDs 24932988, 33806565, 30196776, 27930425 and 37408430) are also unrelated to orphenadrine and are not listed.

## South Africa Market Information

Both entries share one registration number, and the second is a renamed version of the first. The registration data do not include manufacturer details or Essential Medicines List (EML) status.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 32/2.8/0605 | Besenol NC | Tablet | Not stated in registration data |
| Reg. No. 32/2.8/0605 | Uniflex (formerly Besenol NC) | Tablet | Not stated in registration data |

## Safety Considerations

No drug interactions were found in the DDI query. Warnings and contraindications were not available in the supplied data.

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Because orphenadrine is anticholinergic, systemic visual effects such as blurred vision, mydriasis and cycloplegia are a plausible concern in any eye-related use. This is general pharmacology and not taken from the PI.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (evidence level L5), with no trials and no relevant literature. No mechanistic link to inherited retinal degeneration was identified, and the papers retrieved are unrelated to orphenadrine.

**To proceed, the following is needed:**
- The SAHPRA package insert, covering approved indication, warnings and contraindications
- Mechanism of action data from DrugBank
- A biological rationale linking orphenadrine to retinal dystrophy, with preclinical evidence
- Separate review of the schizophrenia prediction (adjunct for antipsychotic-induced extrapyramidal symptoms). Cochrane reviews raise concerns about worsening tardive dyskinesia and cognitive impairment.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

