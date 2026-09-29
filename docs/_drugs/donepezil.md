---
layout: default
title: Donepezil
parent: Model Prediction Only (L5)
nav_order: 194
evidence_level: L5
indication_count: 8
---

# Donepezil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Donepezil: From Alzheimer's Disease to Psychogenic Movement Disorders

## One-Sentence Summary

Donepezil is an acetylcholinesterase inhibitor, widely used for Alzheimer's dementia (the SAHPRA record supplied here does not state an indication).
The TxGNN model predicts it may be effective for **psychogenic movement disorders**, but this is a **model prediction only, with 0 clinical trials and 0 publications** supporting it.
Other predicted movement-related indications, notably chronic tic disorder and lingual-facial-buccal dyskinesia, have more supporting literature (see below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA record supplied. Alzheimer's dementia, inferred from the literature retrieved for this drug |
| Predicted New Indication | Psychogenic movement disorders |
| TxGNN Prediction Score | 99.23% (model rank 4030) |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied record. Donepezil is generally known as an acetylcholinesterase inhibitor: it raises cholinergic signalling in the brain.

For psychogenic (functional) movement disorders, no rationale in the supplied data links cholinergic enhancement to the condition. The high score therefore reflects the knowledge-graph pattern rather than a demonstrated biological link. It should not be read as evidence of benefit.

Two other predicted indications have a more plausible, though still unproven, rationale:

- **Chronic tic disorder** (score 99.19%, L3): Striatal cholinergic dysfunction has been proposed in tics and ADHD. Mouse studies show donepezil affects the serotonergic system and DOI-induced head twitch, a Tourette-relevant model. Small human reports in children and adolescents exist.
- **Lingual-facial-buccal dyskinesia / tardive dyskinesia** (score 99.02%, L3): Tardive dyskinesia is hypothesised to involve a dopaminergic-cholinergic imbalance. Cochrane reviews of cholinergic drugs exist, but they are class-level, not donepezil-specific.

The remaining predicted indications are L5 or indirect: primary orthostatic tremor, benign shuddering attacks, benign paroxysmal tonic upgaze of childhood with ataxia, and tremor-nystagmus-duodenal ulcer syndrome. "Extrapyramidal and movement disease" (L4) has conflicting evidence, including a safety signal (see Safety Considerations).

---

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR or PACTR) for psychogenic movement disorders or for any other predicted indication in this evidence pack.

---

## Literature Evidence

For the lead indication (psychogenic movement disorders), currently no related literature available.

The table below lists the most relevant publications for the other predicted indications. Study types are inferred from titles or truncated abstracts and need full-text verification.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29553158](https://pubmed.ncbi.nlm.nih.gov/29553158/) | 2018 | Cochrane review | Cochrane Database Syst Rev | Cholinergic medication for antipsychotic-induced tardive dyskinesia (class-level; effect size not in supplied text) |
| [15610922](https://pubmed.ncbi.nlm.nih.gov/15610922/) | 2004 | Meta-analysis of RCTs | Prog Neuropsychopharmacol Biol Psychiatry | Systematic review of cholinergic drugs, including donepezil, for neuroleptic-induced tardive dyskinesia |
| [40224553](https://pubmed.ncbi.nlm.nih.gov/40224553/) | 2025 | Systematic review | Brain Circ | Movement disorders **associated with** acetylcholinesterase inhibitors in Alzheimer's dementia (harm signal) |
| [18343255](https://pubmed.ncbi.nlm.nih.gov/18343255/) | 2008 | Open-label trial (inferred) | Clin Ther | Donepezil in children and adolescents with tics and ADHD, 18-week dose-escalating study; outcomes not in supplied text |
| [15669896](https://pubmed.ncbi.nlm.nih.gov/15669896/) | 2005 | Small clinical study (inferred) | J Clin Psychiatry | Title reports a beneficial effect of donepezil in elderly patients with tardive movement disorders |
| [19142126](https://pubmed.ncbi.nlm.nih.gov/19142126/) | 2009 | Not classified | J Clin Psychopharmacol | Effect of donepezil on tardive dyskinesia; no abstract supplied |
| [15689723](https://pubmed.ncbi.nlm.nih.gov/15689723/) | 2005 | Case report / letter (inferred) | J Am Acad Child Adolesc Psychiatry | Donepezil and tardive dyskinesia |
| [10440471](https://pubmed.ncbi.nlm.nih.gov/10440471/) | 1999 | Case report (inferred) | J Clin Psychopharmacol | Donepezil for Tourette's disorder and ADHD |
| [16986157](https://pubmed.ncbi.nlm.nih.gov/16986157/) | 2006 | Commentary / letter (inferred) | Mov Disord | Asks whether donepezil is also effective in Tourette's syndrome |
| [18321753](https://pubmed.ncbi.nlm.nih.gov/18321753/) | 2008 | Not classified | Parkinsonism Relat Disord | Donepezil-induced jaw tremor (harm signal); no abstract supplied |

Preclinical mouse work on tics (PMIDs 14643839 and 16045972) is not tabulated. Many other retrieved papers concern dementia or Parkinson's disease and are only indirectly relevant.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 46/7.1.3/0744 | Valheft 80 | Fct | Not stated in the record supplied |

Essential Medicines List (EML) status is not available in the supplied data.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA. No drug interactions were found in the queried data.

Signals from the retrieved literature, not from the PI, that matter for any movement-disorder use:

- A 2025 systematic review reports movement disorders associated with acetylcholinesterase inhibitors, including donepezil, in Alzheimer's dementia.
- A case report describes donepezil-induced jaw tremor.
- Benign shuddering attacks are a benign, self-limiting paediatric condition, so any drug intervention there would need particularly careful safety justification.
- Tic-related evidence involves children and adolescents, so paediatric safety needs specific review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The lead prediction, psychogenic movement disorders, is model-only (L5) with no trials, no literature and no supported mechanism. Safety data are missing from the pack, which blocks safety screening. Chronic tic disorder and tardive dyskinesia (both L3) are better framed as research questions than as candidates for clinical use.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indication), obtained by downloading and parsing the PDF
- Mechanism of action data, e.g. from the DrugBank API
- Full-text review of the tic and tardive dyskinesia papers to confirm design, effect size and certainty
- Reconciliation of the harm signals (AChEI-associated movement disorders, jaw tremor) with any hyperkinetic-disorder use
- Confirmation of the Valheft 80 strength and formulation against the PI
- A trial-registry search (SANCTR, PACTR) for the shortlisted indications

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

