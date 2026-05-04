---
layout: default
title: Acetaminophen
parent: 僅模型預測 (L5)
nav_order: 14
evidence_level: L5
indication_count: 10
---

# Acetaminophen
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

# Acetaminophen: From Pain and Fever Management to Migraine with Brainstem Aura

## One-Sentence Summary

Acetaminophen (paracetamol) is one of the world's most widely used over-the-counter analgesics and antipyretics, indicated for the relief of mild to moderate pain and the reduction of fever.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** — a subtype of migraine characterised by reversible brainstem symptoms (e.g., vertigo, dysarthria, diplopia) preceding the headache phase —
with **0 registered clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Mild to moderate pain relief and fever reduction (analgesic/antipyretic) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L3 |
| South Africa Market Status | Not currently registered per current dataset (see note below) |
| Number of SAHPRA Registrations | 0 (likely a data retrieval gap — see note) |
| Recommended Decision | Proceed with Guardrails |

> **Important note on SAHPRA registration:** The Evidence Pack returns 0 SAHPRA registrations for "Acetaminophen." This is almost certainly a data retrieval gap rather than a true absence from the South African market, as acetaminophen-containing products (e.g., Panado®, Calpol®, Tylenol®) are widely available in South Africa. Verification against the SAHPRA online medicines register using the INN **"paracetamol"** is strongly recommended before drawing any conclusions about market status.

---

## Why is This Prediction Reasonable?

Acetaminophen exerts its analgesic effect primarily through **central COX-3 inhibition**, reducing prostaglandin synthesis within the central nervous system. This attenuates neuroinflammation and central sensitisation in the trigeminovascular system — the key pathway driving migraine pain. Unlike NSAIDs, acetaminophen's action is predominantly central rather than peripheral, which is mechanistically appropriate for a condition driven by central pain processing abnormalities.

Migraine with brainstem aura is a distinct subtype in which aura symptoms — such as vertigo, tinnitus, diplopia, ataxia, or decreased consciousness — arise from brainstem generators before the headache phase. A critical clinical consideration is that **vasoconstrictive agents (triptans, ergotamines) are relatively contraindicated** in this subtype due to theoretical concerns about basilar artery vasospasm. This effectively removes first-line acute migraine treatments from the available toolkit, elevating acetaminophen to a pragmatic primary analgesic option for mild-to-moderate attacks in this population.

The 2015 American Headache Society (AHS) Evidence Assessment (PMID 25600718) assigns acetaminophen **Level A evidence** for acute treatment of mild-to-moderate migraine overall. While no randomised controlled trials have been conducted specifically in patients with brainstem aura, the mechanistic plausibility, the known efficacy in general migraine, and the safety advantage over vasoconstrictors in this subgroup together make the TxGNN prediction biologically coherent and clinically defensible. The primary evidence gap is the absence of brainstem-aura-specific trial data.

---

## Clinical Trial Evidence

Currently no clinical trials specifically registered for acetaminophen in migraine with brainstem aura.

> No entries were identified in ClinicalTrials.gov or the WHO ICTRP for this specific drug–disease combination. No SANCTR (South African National Clinical Trials Register) or PACTR (Pan African Clinical Trials Registry) entries were found.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Systematic Review / Guideline | *Headache* | AHS evidence assessment assigns **Level A** evidence for acetaminophen in acute mild-to-moderate migraine; the most comprehensive evidence grading available for migraine pharmacotherapy, conducted by the American Headache Society Guidelines Section |
| [11112243](https://pubmed.ncbi.nlm.nih.gov/11112243/) | 2000 | RCT | *Archives of Internal Medicine* | Randomised, double-blind, placebo-controlled, population-based trial demonstrating the efficacy and safety of acetaminophen monotherapy for migraine in a primary care setting |
| [9482363](https://pubmed.ncbi.nlm.nih.gov/9482363/) | 1998 | RCT | *Archives of Neurology* | Three double-blind, placebo-controlled RCTs assessing the acetaminophen + aspirin + caffeine (AAC) combination; established robust efficacy for alleviating migraine headache pain |
| [10321417](https://pubmed.ncbi.nlm.nih.gov/10321417/) | 1999 | RCT | *Clinical Therapeutics* | Retrospective analysis of 3 placebo-controlled RCTs of the AAC combination (Excedrin Migraine) in menstruation-associated migraine; acetaminophen component integral to efficacy |
| [11318886](https://pubmed.ncbi.nlm.nih.gov/11318886/) | 2001 | RCT | *Headache* | Comparative trial of isometheptene/dichloralphenazone/acetaminophen vs sumatriptan succinate for mild-to-moderate migraine with or without aura; both treatments effective when taken at first sign of attack |
| [39493026](https://pubmed.ncbi.nlm.nih.gov/39493026/) | 2024 | Review | *Cureus* | Reviews abortive and prophylactic migraine therapies in pregnancy; acetaminophen identified as the preferred first-line analgesic for migraine management, including in patients with aura where triptans are avoided |
| [30470274](https://pubmed.ncbi.nlm.nih.gov/30470274/) | 2019 | Review | *Neurologic Clinics* | Headache in pregnancy and puerperium; acetaminophen explicitly named as **first-line symptomatic treatment** for migraine, relevant to the brainstem aura subtype where vasoconstrictor avoidance is required |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | *Handbook of Clinical Neurology* | Status migrainosus review; examines management of prolonged migraine attacks (>72 h) and the role of analgesics including acetaminophen as bridging and background therapy |
| [33525313](https://pubmed.ncbi.nlm.nih.gov/33525313/) | 2021 | Review | *Neurology International* | Overviews acute migraine management; acetaminophen described as standard treatment for mild-to-moderate migraine, providing clinical context alongside newer CGRP antagonists |
| [37123778](https://pubmed.ncbi.nlm.nih.gov/37123778/) | 2023 | Review | *Cureus* | Migraine treatment in pregnancy and breastfeeding; discusses safety of acetaminophen across all migraine subtypes including those with aura, particularly where hormonal changes drive disease worsening |

---

## South Africa Market Information

SAHPRA registration data returned 0 records for acetaminophen under the INN "Acetaminophen" in the current dataset. This is inconsistent with the known widespread availability of paracetamol products in South Africa.

**Recommended action:** Query the SAHPRA medicines database at [https://www.sahpra.org.za](https://www.sahpra.org.za) using:
- Generic name: **paracetamol** (the INN used in South Africa and the UK/Commonwealth context)
- Common brand names: Panado®, Calpol®, Tylenol®, Grandpa®-containing products

Note that paracetamol is included on the South African **Essential Medicines List (EML)** for primary healthcare and hospital levels, which has significant implications for formulary access and procurement.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for complete safety information. Report adverse drug reactions to SAHPRA via the [MedSafety reporting portal](https://www.sahpra.org.za/pharmacovigilance/).

> The Evidence Pack does not contain extractable SAHPRA-specific safety data for this submission. Based on established pharmacology and international regulatory information, clinicians should note the following key safety considerations:
> - **Hepatotoxicity risk** with overdose or chronic high-dose use; maximum recommended adult dose is **4 g/day** (reduced to **2 g/day** in elderly patients and those with hepatic impairment or chronic alcohol use)
> - **Renal toxicity** is possible with chronic high-dose use
> - Multiple concurrent acetaminophen-containing products (combination cold/flu remedies, opioid combinations) are a common source of inadvertent overdose — patients should be counselled accordingly

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Acetaminophen holds Level A evidence for acute mild-to-moderate migraine (AHS 2015), and its analgesic mechanism via central COX-3 inhibition is directly applicable to migraine pain pathways. In the brainstem aura subtype specifically, the relative contraindication of vasoconstrictive triptans and ergotamines makes acetaminophen the most clinically appropriate first-line analgesic option. Evidence supporting general migraine efficacy is robust (multiple RCTs), though the brainstem aura subtype itself lacks dedicated trial data.

**To proceed, the following is needed:**

- Confirm current SAHPRA registration status by searching the SAHPRA online register under **"paracetamol"** rather than "acetaminophen"
- Retrieve and review the SAHPRA-approved Professional Information (PI) document to obtain formal local safety, warning, and contraindication data
- Confirm available dosage forms in the South African market appropriate for acute migraine management (oral tablet, soluble tablet, suspension, or IV formulation for emergency/inpatient settings)
- Verify alignment with the South African Essential Medicines List (EML) classification and any formulary restrictions at the intended level of care
- Seek input from a specialist neurologist or headache clinic to establish a protocol specific to migraine with brainstem aura management, given the subtype's distinct contraindication profile and the absence of subtype-specific RCT data
- Consider a local audit or case series to capture real-world outcomes when acetaminophen is used in this specific migraine subtype in South African patients

---

*This report is generated by the ZaTxGNN drug repurposing prediction system (Evidence Pack v4, data cut-off 2026-04-04). Results are for **research reference only** and do not constitute medical advice. Drug repurposing candidates require clinical validation before application in patient care. All suspected adverse drug reactions should be reported to SAHPRA.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

