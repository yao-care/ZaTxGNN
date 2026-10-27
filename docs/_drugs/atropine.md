---
layout: default
title: Atropine
parent: Model Prediction Only (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Atropine: predicted new indication Migraine disorder (evidence level L5). Approved use: Not available"
monitor_inn: "Atropine"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "open-angle glaucoma", "primary hereditary glaucoma", "ulerythema ophryogenesis", "headache disorder", "trigeminal autonomic cephalalgia", "nephrogenic syndrome of inappropriate antidiuresis"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Atropine: From an Unspecified Original Indication to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Atropine is a muscarinic (cholinergic) antagonist, and the data compiled for this report do not state its approved indication in South Africa.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **0 clinical trials** and only preclinical or indirect literature for this exact condition.
The best-supported nearby signal is for **headache disorder** (specifically post-dural puncture headache), with **2 completed trials** in which atropine is only a component of a neostigmine/atropine comparator.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the SAHPRA registration record has no indication text) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L4 (preclinical and mechanistic literature only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Atropine is, however, a well-known non-selective muscarinic antagonist. The literature retrieved describes it as a classic cholinergic antagonist (see the review of its derivative anisodamine).

Preclinical studies suggest the parasympathetic and cholinergic systems contribute to meningeal nociception and neurogenic inflammation in migraine. These include meningeal mast cell-cholinergic modulation in rats and parasympathetic stimulation causing plasma protein leakage in rat dura mater. Blocking muscarinic receptors is therefore biologically plausible.

This evidence has important limits:
- It comes from animal or in vitro work, from related compounds, or from adverse-event case reports.
- One mouse study suggests cholinergic *activation* inhibits cortical spreading depression, which does not clearly support an antagonist such as atropine.
- No clinical trials exist for migraine.

## Clinical Trial Evidence

No trials were found for migraine disorder itself. Currently no related clinical trials registered for this indication.

The closest signal is in the related prediction **headache disorder** (score 97.24%), where two completed trials studied post-dural puncture headache (PDPH). In both, atropine is given only in combination with neostigmine as a comparator, so its independent effect cannot be separated.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03997006](https://clinicaltrials.gov/study/NCT03997006) | Phase 4 | Completed | 60 | IV aminophylline vs IV neostigmine/atropine for PDPH |
| [NCT04910477](https://clinicaltrials.gov/study/NCT04910477) | Phase 3 | Completed | 90 | Nebulized dexmedetomidine vs neostigmine/atropine vs saline in PDPH after caesarean section |

No SANCTR or PACTR identifiers were available in the data compiled for this report.

## Literature Evidence

**Migraine disorder (most relevant publications):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17186568](https://pubmed.ncbi.nlm.nih.gov/17186568/) | 2007 | Review | J Appl Toxicol | Anisodamine, an atropine derivative, is a non-specific cholinergic antagonist, less potent and less toxic than atropine |
| [36485173](https://pubmed.ncbi.nlm.nih.gov/36485173/) | 2024 | Preclinical | Eur J Neurosci | Cholinergic modulation via meningeal mast cells in a rat migraine model |
| [9344563](https://pubmed.ncbi.nlm.nih.gov/9344563/) | 1997 | Preclinical | Exp Neurol | Parasympathetic stimulation causes plasma protein extravasation in rat dura mater |
| [2943405](https://pubmed.ncbi.nlm.nih.gov/2943405/) | 1986 | Clinical observation | Cephalalgia | In 4 patients with chronic paroxysmal hemicrania, systemic atropine markedly reduced attack-related sweating, tearing and nasal secretion |
| [40590589](https://pubmed.ncbi.nlm.nih.gov/40590589/) | 2024 | Case report | Pain Med Case Rep | Botulinum-induced dropped head syndrome in chronic migraine (not about atropine) |

**Headache disorder (randomised trials involving neostigmine/atropine):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30169405](https://pubmed.ncbi.nlm.nih.gov/30169405/) | 2018 | RCT | Anesth Analg | Neostigmine plus atropine added to conventional PDPH management |
| [36651373](https://pubmed.ncbi.nlm.nih.gov/36651373/) | 2023 | RCT | Minerva Anestesiol | Nebulized dexmedetomidine vs neostigmine/atropine for PDPH after caesarean section |
| [37802666](https://pubmed.ncbi.nlm.nih.gov/37802666/) | 2023 | Case report | Br J Anaesth | Reversible cerebral vasoconstriction syndrome after neostigmine/atropine for PDPH (safety signal) |

**Other predicted indications (brief):**
- **Trigeminal autonomic cephalalgia:** one 1984 uncontrolled report on atropine preparations in cluster headache ([6397917](https://pubmed.ncbi.nlm.nih.gov/6397917/)), plus preclinical work.
- **Migraine with brainstem aura:** a single mouse study ([31945385](https://pubmed.ncbi.nlm.nih.gov/31945385/)) with unclear direction of effect.
- **Open-angle glaucoma and primary hereditary glaucoma:** the literature describes atropine's ocular risks, mainly raised intraocular pressure (IOP). These predictions are likely spurious, and the safety signal runs against repurposing.
- **Atrophoderma vermiculata, ulerythema ophryogenesis, nephrogenic syndrome of inappropriate antidiuresis:** prediction only, with no literature, no trials and no identifiable mechanistic link.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| C955(ACT101/1965) | Colstat | Capsule (oral) | Not stated in the registration record |

The Essential Medicines List (EML) status could not be determined from the data compiled for this report.

## Safety Considerations

- **Drug Interactions:** A screen identified 100 potential interactions. Most of those shown are Moderate, with a few Minor. Examples include:
  - Other anticholinergic or antimuscarinic agents (aclidinium, hyoscyamine, amitriptyline, chlorpheniramine, acrivastine, phenyltoloxamine), which may add to anticholinergic effects.
  - Opioids (fentanyl, alfentanil, codeine, dihydrocodeine, tramadol), loperamide and ethanol.
  - Acetylcholine and galantamine, which oppose atropine's cholinergic action.
  - Amantadine, acebutolol, botulinum toxin type A, acetaminophen (Minor) and hydrochlorothiazide (Minor).
- **Ocular risk:** The literature links topical atropine to raised IOP and caution in glaucoma, because mydriasis can raise IOP.
- **Cerebrovascular signal:** One case report describes reversible cerebral vasoconstriction syndrome after neostigmine/atropine given for PDPH.

SAHPRA package insert warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The migraine prediction has a high model score but no clinical trials, and its support is preclinical or indirect, giving an L4 evidence level.
- The only trials (in post-dural puncture headache) use atropine in combination with neostigmine, so atropine's own effect is unknown.
- Safety review cannot proceed because the SAHPRA package insert data are missing.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (indications, warnings, contraindications) for Colstat, with the approved indication confirmed.
- Mechanism of action data (for example from DrugBank) to strengthen the mechanistic analysis.
- Controlled clinical evidence of atropine alone in migraine or cluster headache, or a well-designed pilot trial.
- A route and formulation assessment, since only an oral capsule is registered and route compatibility has not been assessed.
- A risk assessment for glaucoma, cerebrovascular events and anticholinergic interactions, especially in older patients.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

