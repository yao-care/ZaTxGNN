---
layout: default
title: Acetylsalicylic Acid
parent: 僅模型預測 (L5)
nav_order: 16
evidence_level: L5
indication_count: 10
---

# Acetylsalicylic Acid
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

# Acetylsalicylic Acid (Aspirin): From Cardiovascular and Pain Management to Migraine with Brainstem Aura

## One-Sentence Summary

Acetylsalicylic acid (aspirin) is one of the most widely used medicines in the world, established for pain relief, fever reduction, anti-inflammatory therapy, and cardiovascular event prevention through its cyclooxygenase inhibition and antiplatelet mechanisms.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** (formerly basilar-type migraine),
with **no registered clinical trials** specifically for this subtype and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain, fever, inflammation, and cardiovascular event prevention (antiplatelet) — no SAHPRA-registered indication text available in current dataset |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 (observational studies and systematic reviews) |
| South Africa Market Status | No SAHPRA registrations found in current dataset |
| Number of SAHPRA Registrations | 0 (likely a data retrieval gap — aspirin is included on the South African Essential Medicines List) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved in this evidence pack. Based on well-established pharmacological knowledge, aspirin irreversibly acetylates the serine residue (Ser530) of cyclooxygenase-1 (COX-1) and, to a lesser extent, COX-2. This permanently blocks the synthesis of prostaglandin E2 (PGE2) — a key mediator of neurogenic inflammation and pain sensitisation — and thromboxane A2 (TXA2), which drives platelet aggregation and vasoconstriction. Because platelets are anucleate and cannot regenerate COX-1, a single dose of aspirin suppresses platelet TXA2 for the entire platelet lifespan (7–10 days).

Migraine with brainstem aura (ICHD-3 classification) is characterised by focal neurological symptoms — including diplopia, dysarthria, tinnitus, vertigo, and ataxia — that arise from cortical spreading depression (CSD) originating in or propagating through the brainstem and occipital cortex. The vasoactive cascade triggered by CSD involves local prostaglandin release and inflammatory sensitisation of the trigeminovascular system, making aspirin's dual anti-inflammatory and antiplatelet profile a plausible mechanistic fit. The platelet hypothesis of migraine — first proposed by Hanington and supported by a decade of observational research (PMID 2701286) — lends further biological rationale: CSD may be facilitated by platelet-derived vasoactive substances, which aspirin suppresses.

Crucially, this migraine subtype presents a clinically important prescribing gap: triptans and ergotamine derivatives are **contraindicated** due to their vasoconstrictive effects on the posterior circulation. Aspirin therefore occupies a unique therapeutic space as one of the few agents usable acutely in this patient group. A retrospective cohort study (PMID 25729594, n = 203) demonstrated efficacy of low-dose aspirin as prophylaxis in migraine with aura patients, and a randomised trial (PMID 10448545) showed that intravenous aspirin was comparable to subcutaneous sumatriptan in resolving acute migraine attacks. A 2025 systematic review (PMID 39989443) further consolidates evidence for antithrombotic drugs — including aspirin — as migraine preventive agents. The additional protection aspirin may confer against ischaemic stroke (PMID 35006660), a known elevated risk in patients with migraine with aura, provides dual clinical benefit.

---

## Clinical Trial Evidence

Currently no clinical trials specifically registered for Acetylsalicylic Acid in Migraine with Brainstem Aura.

> No entries were identified in ClinicalTrials.gov, SANCTR (South African National Clinical Trials Register), or PACTR (Pan African Clinical Trials Registry) for this drug–disease combination. This absence of registered trials is itself a key evidence gap and supports a "Proceed with Guardrails" rather than "Go" recommendation.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25729594](https://pubmed.ncbi.nlm.nih.gov/25729594/) | 2014 | Retrospective Study | Current Health Sciences Journal | 203 patients with migraine with aura (ICHD-II criteria); 46.8% received low-dose ASA prophylaxis vs other preventive therapies — the only study directly evaluating ASA as prophylaxis specifically in this migraine subtype |
| [10448545](https://pubmed.ncbi.nlm.nih.gov/10448545/) | 1999 | RCT (Double-blind) | Cephalalgia | Multicentre RCT (n=278) comparing IV lysine acetylsalicylate (equivalent to 1 g ASA) vs 6 mg sumatriptan SC vs placebo in acute migraine with or without aura; direct efficacy evidence for parenteral aspirin in migraine |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic Review | Headache | Systematic review of available evidence on antithrombotic drugs (including ASA) as migraine preventive medication; most recent and comprehensive synthesis of ASA's role in migraine prevention |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Evidence Assessment / AHS Guideline | Headache | American Headache Society updated evidence assessment of all pharmacological therapies for acute migraine, including aspirin and aspirin–caffeine combinations — Tier 1 guideline document |
| [35006660](https://pubmed.ncbi.nlm.nih.gov/35006660/) | 2022 | Review / Practice Guideline | FP Essentials | AHA/ASA primary stroke prevention guidelines; highlights elevated ischaemic stroke risk in patients with migraine with aura, providing the rationale for aspirin's dual protective role in this population |
| [34384631](https://pubmed.ncbi.nlm.nih.gov/34384631/) | 2021 | Review | Revue Neurologique | Comprehensive review of migraine with aura: CSD mechanisms, ICHD-3 diagnostic criteria, clinical subtypes including brainstem aura, and current treatment landscape |
| [30291554](https://pubmed.ncbi.nlm.nih.gov/30291554/) | 2018 | Review | Current Pain and Headache Reports | Comparison of pathophysiological and clinical differences between episodic migraine with and without aura; highlights distinct management implications including contraindication of vasoconstrictors in aura subtypes |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Observational | Heart (British Cardiac Society) | Clopidogrel reduced migraine with aura frequency after transcatheter closure of atrial shunts, supporting the antiplatelet mechanism as a valid therapeutic target for aura reduction |
| [2701286](https://pubmed.ncbi.nlm.nih.gov/2701286/) | 1989 | Review | Biomedecine & Pharmacotherapie | Migraine platelet hypothesis: 10-year review of evidence for primary platelet abnormality as a migraine substrate — foundational mechanistic rationale for antiplatelet therapy in migraine |
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT | European Heart Journal | PRIMA trial: multicentre RCT of percutaneous PFO closure in patients with migraine with aura refractory to medical treatment, contextualising the vascular and thromboembolic dimensions of this migraine phenotype |

---

## South Africa Market Information

No SAHPRA product registrations were identified in the current dataset for Acetylsalicylic Acid (DrugBank ID: DB00945).

> **Important note for clinicians:** This absence almost certainly reflects a **data retrieval limitation** rather than true unavailability. Aspirin is one of the most widely available generic medicines in South Africa, sold over the counter and by prescription in multiple formulations. It is included on the **South African Essential Medicines List (EML)** for primary healthcare. Clinicians should verify current registered products and approved indications directly via the [SAHPRA online product register](https://www.sahpra.org.za) and consult the approved Professional Information (PI) for each registered product.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA via the MedSafety reporting system.

> **Specific safety alerts relevant to this indication:**
>
> - **Contraindication of vasoconstrictors:** Triptans and ergotamine are contraindicated in migraine with brainstem aura. Aspirin does not carry this restriction, but prescribers should explicitly document the migraine subtype before initiating any abortive therapy.
> - **Gastrointestinal bleeding risk:** The most clinically significant concern with long-term or repeated aspirin use. Risk is elevated in elderly patients, those with *H. pylori* infection, concurrent NSAID use, or prior peptic ulcer disease. Co-prescription of a proton pump inhibitor should be considered.
> - **Reye's syndrome:** Aspirin is contraindicated in children and adolescents with current or recent viral illness (influenza, varicella).
> - **Pregnancy:** Use in the first and third trimesters requires careful risk–benefit assessment; low-dose aspirin in the second trimester context has an established safety profile in specific indications (e.g., pre-eclampsia prevention).
> - **Anticoagulant interactions:** Aspirin potentiates bleeding risk when combined with warfarin, direct oral anticoagulants (DOACs), or other antiplatelet agents. Drug interaction screening is essential before prescribing.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for aspirin in migraine with brainstem aura is biologically plausible and clinically rational — aspirin's anti-inflammatory and antiplatelet mechanisms address the neuroinflammatory and vascular pathophysiology of this migraine subtype, and it occupies a critical prescribing niche given the contraindication of vasoconstrictive agents in this patient group. Preliminary support comes from one retrospective cohort study (PMID 25729594), one randomised controlled trial of IV aspirin in acute migraine (PMID 10448545), and a 2025 systematic review of antithrombotics in migraine prevention (PMID 39989443); however, no prospective trial has been registered or completed specifically for the brainstem aura phenotype, limiting the evidence to L3.

**To proceed, the following is needed:**
- A prospective RCT evaluating oral low-dose aspirin (75–300 mg) for prophylaxis — and/or acute treatment — in patients with confirmed migraine with brainstem aura per ICHD-3 criteria
- Subgroup analyses within existing large migraine prevention trials to isolate the brainstem aura phenotype
- Mechanistic studies examining aspirin's effect on CSD initiation and propagation in the posterior fossa
- Post-marketing safety surveillance data relevant to South African patient demographics, including prevalence of *H. pylori* co-infection, tuberculosis co-treatment (drug interactions), and pregnancy-related risks
- Verification of current SAHPRA registration status and available aspirin formulations for the South African market

> **Broader context:** While migraine with brainstem aura is the highest-ranked TxGNN prediction for aspirin (score 99.94%), clinicians should note that other predicted indications — particularly **thrombotic disease (rank 8, Evidence Level L1)** and **thrombophilia (rank 9, Evidence Level L2)** — are supported by substantially stronger and more mature clinical evidence, including multiple completed Phase 3 RCTs. These applications may be more immediately actionable in clinical practice.

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Data cutoff: 4 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

