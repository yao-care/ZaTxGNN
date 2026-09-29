---
layout: default
title: Atropine
parent: Model Prediction Only (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
---

# Atropine
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

# Atropine: From Muscarinic Antagonist to Migraine Disorder

## One-Sentence Summary

Atropine is a muscarinic (anticholinergic) drug that is registered in South Africa as an oral capsule.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **0 clinical trials** and only **preclinical and unrelated publications** behind this prediction.
The high model score is not yet backed by any human data for migraine.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L4 (preclinical/mechanistic studies only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on the known drug class, atropine blocks muscarinic acetylcholine receptors. Mechanistically, it may be applicable to migraine.

Animal and in vitro studies link migraine to cholinergic and nicotinic signalling, meningeal mast cells, parasympathetic outflow and CGRP-related vascular changes. These processes drive neurogenic inflammation. If parasympathetic activity helps trigger a migraine attack, blocking muscarinic receptors is biologically plausible.

The evidence is weak and partly conflicting. A mouse study found that cholinergic activation *inhibits* cortical spreading depression, the process behind migraine aura, which could argue against a benefit from an anticholinergic. All migraine-specific evidence is animal or in vitro. No clinical trial has tested atropine for migraine, so the high graph score is a hypothesis, not a finding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine disorder.

For context, other predicted indications show some trials. The only clinically meaningful signal is for **post-dural puncture headache**, a secondary headache. In those trials atropine was given only as part of a neostigmine/atropine combination. This cannot be extended to migraine.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36485173](https://pubmed.ncbi.nlm.nih.gov/36485173/) | 2024 | Preclinical | Eur J Neurosci | In a rat nitroglycerin migraine model, cholinergic modulation acts through meningeal mast cells in neurogenic inflammation. |
| [9344563](https://pubmed.ncbi.nlm.nih.gov/9344563/) | 1997 | Preclinical | Exp Neurol | Stimulating the parasympathetic sphenopalatine ganglion causes plasma protein extravasation in rat dura mater. |
| [15882801](https://pubmed.ncbi.nlm.nih.gov/15882801/) | 2005 | Preclinical | Neurosci Lett | CGRP and nicotinic receptors are involved in centrally evoked facial blood flow changes. |
| [8930196](https://pubmed.ncbi.nlm.nih.gov/8930196/) | 1996 | Preclinical | J Pharmacol Exp Ther | The central cholinergic system contributes to the antinociceptive effect of sumatriptan in rodents. |
| [10193781](https://pubmed.ncbi.nlm.nih.gov/10193781/) | 1999 | Preclinical | Br J Pharmacol | Nicotine-evoked relaxation of guinea-pig basilar artery is inhibited by some migraine-related drugs (atropine was present in the assay). |
| [17186568](https://pubmed.ncbi.nlm.nih.gov/17186568/) | 2007 | Review | J Appl Toxicol | Pharmacology of anisodamine, an atropine-like cholinergic antagonist. Not migraine-specific. |
| [2943405](https://pubmed.ncbi.nlm.nih.gov/2943405/) | 1986 | Not classified | Cephalalgia | In 4 patients with chronic paroxysmal hemicrania, systemic atropine markedly reduced attack-related sweating, tearing and nasal secretion. Not migraine. |
| [1786517](https://pubmed.ncbi.nlm.nih.gov/1786517/) | 1991 | Preclinical | Br J Pharmacol | Ergotamine and dihydroergotamine are potent 5-HT1C agonists in piglet choroid plexus. Atropine is not studied. |
| [21252](https://pubmed.ncbi.nlm.nih.gov/21252/) | 1977 | Not classified | J Pharm Pharmacol | Possible mechanism of beta-phenethylamine in migraine. No abstract available. |

The remaining retrieved records (for example, botulinum toxin and topiramate case reports) do not concern atropine and are not listed.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. C955 (ACT101/1965) | Colstat | Capsule (oral) | Not listed in the register data |

Essential Medicines List (EML) status could not be determined from the available data.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Signals from the evidence review, not from the product label:
- **Glaucoma**: anticholinergics and cycloplegics can raise intraocular pressure and precipitate angle closure. Early clinical studies in open-angle glaucoma point this way.
- **Cerebral vasoconstriction**: one case report describes reversible cerebral vasoconstriction syndrome after neostigmine plus atropine given for post-dural puncture headache.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction rests only on animal and in vitro work, with no clinical trials. One mouse study even points the other way. The SAHPRA package insert safety data has not been obtained, which blocks any safety screening.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (download and parse the PI)
- Mechanism of action data from DrugBank
- Human evidence for atropine alone in migraine, such as a pilot or proof-of-concept trial
- A route and formulation assessment, since the only registered product is an oral capsule
- Safety review for people with glaucoma or cerebrovascular risk

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

