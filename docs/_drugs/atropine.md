---
layout: default
title: Atropine
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
---

# Atropine
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

# Atropine: From Bradycardia and Organophosphate Poisoning to Migraine Disorder

---

## One-Sentence Summary

Atropine is a classical anticholinergic drug used in clinical practice for symptomatic bradycardia, as an antidote for organophosphate poisoning, and as a preanesthetic agent to reduce secretions. The TxGNN model predicts it may be effective for **migraine disorder** by blocking the parasympathetic signalling that drives neurogenic inflammation during migraine attacks, with **no registered clinical trials** and **13 publications** — all indirect mechanistic or animal studies — currently supporting this direction. Importantly, a related headache prediction (post-dural puncture headache, PDPH) carries Phase 3 trial support for the Neostigmine+Atropine combination, representing the most immediately actionable finding in this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Symptomatic bradycardia; organophosphate poisoning antidote; preanesthetic antisecretory use |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Atropine is not available in the current dataset. Based on well-established pharmacology, Atropine is a competitive, non-selective antagonist of muscarinic acetylcholine receptors (mAChR, M1–M5 subtypes). By blocking the effects of acetylcholine at parasympathetic neuroeffector junctions and in the central nervous system, Atropine produces tachycardia, reduced glandular secretions, bronchodilation, mydriasis, and — at higher doses — central anticholinergic effects including cognitive changes.

The predicted link to migraine centres on the role of the parasympathetic nervous system in migraine pathophysiology. The sphenopalatine ganglion (SPG) — the largest cranial parasympathetic relay centre — when activated, drives neurogenic inflammation of the dura mater, the membrane lining the brain. This process involves dural vasodilation, plasma protein extravasation, and release of neuropeptides such as calcitonin gene-related peptide (CGRP), all of which contribute to the migraine pain cascade. A 2024 experimental study (PMID 36485173) confirmed that cholinergic modulation via meningeal mast cells — including with muscarinic antagonists — influences this neuroinflammatory process in a rat nitroglycerin-induced migraine model. A 1997 animal study (PMID 9344563) further demonstrated that direct electrical stimulation of the SPG induces dural plasma protein extravasation, establishing the SPG as a druggable parasympathetic target in migraine.

Despite this plausible mechanistic basis, all available evidence remains indirect. Atropine appears in the migraine literature as a pharmacological tool — used to confirm cholinergic pathway involvement in vasomotor responses and antinociception — rather than as the investigational treatment itself. A 1986 clinical observation (PMID 2943405) noted that systemic atropine markedly reduced autonomic attack features (sweating, tearing, nasal secretion) in four patients with chronic paroxysmal hemicrania, providing the single direct clinical signal that mAChR blockade can modify a headache syndrome. No prospective clinical trial has evaluated Atropine as a migraine therapy, and the appropriate dose, route of administration, and target patient population remain entirely undefined.

---

## Clinical Trial Evidence

Currently no clinical trials directly evaluating Atropine for migraine disorder have been registered on ClinicalTrials.gov or ICTRP.

> **Note on Related Headache Evidence:** For the post-dural puncture headache (PDPH) indication (TxGNN Rank 8, Evidence Level L2), three Grade A clinical trials directly evaluating the Neostigmine+Atropine combination have been identified — see the Conclusion and Next Steps section below.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36485173](https://pubmed.ncbi.nlm.nih.gov/36485173/) | 2024 | Mechanistic lab study | European Journal of Neuroscience | Investigated cholinergic modulation via meningeal mast cells in a rat nitroglycerin-induced migraine model; muscarinic blockade reduces mast-cell-driven neurogenic inflammation — the most directly relevant study to the mAChR-migraine hypothesis |
| [9344563](https://pubmed.ncbi.nlm.nih.gov/9344563/) | 1997 | Animal study | Experimental Neurology | SPG parasympathetic stimulation induces dural plasma protein extravasation in rats; atropine-sensitive cholinergic signalling underlies this SPG-mediated neurogenic inflammatory response |
| [8930196](https://pubmed.ncbi.nlm.nih.gov/8930196/) | 1996 | Animal study | J Pharmacology & Experimental Therapeutics | Central atropine injection blocked sumatriptan antinociception in rodents and guinea pigs; demonstrates that central muscarinic pathways contribute to antimigraine drug efficacy |
| [2943405](https://pubmed.ncbi.nlm.nih.gov/2943405/) | 1986 | Clinical observation | Cephalalgia | Systemic atropine markedly reduced autonomic attack features (sweating, tearing, nasal secretion) in 4 patients with chronic paroxysmal hemicrania — the only direct clinical observation of mAChR blockade modifying a headache syndrome |
| [10193781](https://pubmed.ncbi.nlm.nih.gov/10193781/) | 1999 | Animal pharmacology | British Journal of Pharmacology | Atropine (3 µM) used as pharmacological probe in basilar artery relaxation studies; nicotine-evoked relaxation partially atropine-sensitive — relevant to migraine-associated vasomotor pharmacology |
| [15882801](https://pubmed.ncbi.nlm.nih.gov/15882801/) | 2005 | Animal study | Neuroscience Letters | Cholinergic-nicotinic pathways shown to contribute to CGRP release and facial blood flow changes in a centrally evoked trigeminovascular model relevant to migraine triggers |
| [17186568](https://pubmed.ncbi.nlm.nih.gov/17186568/) | 2007 | Review | Journal of Applied Toxicology | Pharmacological review of anisodamine (an atropine derivative); outlines mAChR antagonist class effects including CNS and vascular actions relevant to the migraine mechanistic hypothesis |
| [1786517](https://pubmed.ncbi.nlm.nih.gov/1786517/) | 1991 | Pharmacological experiment | British Journal of Pharmacology | Ergotamine and DHE pharmacology at 5-HT1C receptors in piglet choroid plexus; contextual background pharmacology of classical antimigraine agents |

---

## South Africa Market Information

Atropine (DrugBank ID: DB00572) is **not currently registered with SAHPRA** and holds no approved product licences in South Africa based on the data available for this report. There are no SAHPRA-registered products to list.

Healthcare professionals in South Africa requiring atropine for established indications (e.g., bradycardia, organophosphate antidote, perioperative use) should contact SAHPRA regarding the section 21 unregistered medicine authorisation process, and consult the current SAHPRA register for any updated product registration status.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Pharmacological safety signals identified from the literature:**

- **Intraocular pressure (IOP) elevation — contraindication signal:** Atropine's mydriatic and cycloplegic effects reduce aqueous outflow, raising IOP. Clinical studies from 1968 (PMID 5640848, long-term anticholinergic use in open-angle glaucoma patients) and 2025 (PMID 40932733, cohort study of children on topical atropine for myopia control) document this effect. Atropine is **contraindicated** in patients with open-angle or angle-closure glaucoma, and IOP screening must be included in any headache trial protocol.

- **Cardiovascular effects:** Tachycardia, palpitations, and arrhythmias are expected pharmacodynamic effects. Use with caution in patients with pre-existing ischaemic heart disease or arrhythmias.

- **RCVS safety signal with Neostigmine+Atropine:** A 2023 case report (PMID 37802666, *British Journal of Anaesthesia*) documented reversible cerebral vasoconstriction syndrome (RCVS) following Neostigmine+Atropine administration for PDPH — a rare but serious neurological adverse event. Neurological monitoring is warranted when this combination is used.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for migraine disorder is mechanistically plausible — Atropine's mAChR blockade could theoretically attenuate SPG-driven neurogenic inflammation — but is supported only by indirect preclinical and mechanistic evidence (Evidence Level L4). No clinical trial has directly tested Atropine for migraine, the drug is not currently registered with SAHPRA, and critical data including the MOA dataset, safety PI, and dose-route definition for neurological use are all absent.

**To proceed, the following is needed:**

- **MOA documentation:** Retrieve complete mechanism of action data from DrugBank to strengthen mechanistic analyses and support any regulatory submission
- **SAHPRA registration pathway:** Assess section 21 authorisation or formal registration requirements for established atropine indications in South Africa before initiating any new indication programme
- **Proof-of-concept trial design:** A small, controlled study evaluating selective mAChR antagonism on SPG-mediated outcomes in migraine patients would be needed to advance evidence from L4 to L2 or L3
- **IOP pre-screening requirement:** Any clinical protocol must include baseline and periodic intraocular pressure assessment, with exclusion of patients at risk of glaucoma
- **Glaucoma and PDPH contraindication review:** Given the IOP-elevation pharmacological signal, open-angle glaucoma (Rank 5) and primary hereditary glaucoma (Rank 6) should be flagged as **contraindicated** indications rather than repurposing candidates

---

**Priority Finding — Post-Dural Puncture Headache (Rank 8, Evidence Level L2): Proceed with Guardrails**

The strongest clinical evidence in this entire Evidence Pack relates not to the top TxGNN prediction, but to the **Neostigmine+Atropine combination for PDPH** (TxGNN Rank 8). The key evidence includes:

| Trial | Phase | Status | n | Relevance |
|-------|-------|--------|---|-----------|
| [NCT04910477](https://clinicaltrials.gov/study/NCT04910477) | Phase 3 | Completed | 90 | Direct comparison of nebulised Neostigmine+Atropine vs Dexmedetomidine for PDPH after caesarean section; highest-grade direct trial evidence |
| [NCT03997006](https://clinicaltrials.gov/study/NCT03997006) | Phase 4 | Completed | 60 | Head-to-head RCT: IV Neostigmine+Atropine vs IV Aminophylline for PDPH treatment |
| [NCT06729047](https://clinicaltrials.gov/study/NCT06729047) | Phase 1/2 | Not yet recruiting | 330 | Large prophylactic trial: IV Neostigmine+Atropine vs Ketorolac for PDPH prevention |
| [NCT03587441](https://clinicaltrials.gov/study/NCT03587441) | Phase 4 | Completed | 240 | Neostigmine intrathecal adjuvant to reduce PDPH incidence; Atropine as required co-agent |

| PMID | Year | Type | Key Finding |
|------|------|------|-------------|
| [30169405](https://pubmed.ncbi.nlm.nih.gov/30169405/) | 2018 | **RCT** | Landmark trial (*Anesthesia & Analgesia*): Neostigmine+Atropine added to conventional PDPH management significantly reduced headache severity |
| [36651373](https://pubmed.ncbi.nlm.nih.gov/36651373/) | 2023 | **RCT** | Confirms Neostigmine+Atropine efficacy vs nebulised dexmedetomidine for PDPH after caesarean section |
| [37802666](https://pubmed.ncbi.nlm.nih.gov/37802666/) | 2023 | Case report | RCVS reported after Neostigmine+Atropine for PDPH — critical safety signal requiring neurological monitoring |

**Clinical context:** In PDPH, Atropine functions as a **safety co-agent** — its role is to counteract neostigmine's peripheral mAChR side effects (bradycardia, hypersalivation, intestinal hypermotility), enabling safe neostigmine delivery. Atropine is not an independent PDPH treatment. A dedicated evidence pack focused on the Neostigmine+Atropine combination for PDPH is recommended for full regulatory and clinical evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

