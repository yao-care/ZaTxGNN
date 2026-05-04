---
layout: default
title: Caffeine
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
---

# Caffeine
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

# Caffeine: From CNS Stimulant to Hypnic Headache

## One-Sentence Summary

Caffeine (DB00201) is a methylxanthine alkaloid widely recognised as a CNS stimulant and analgesic adjuvant in combination analgesic products, but currently holds **no SAHPRA registration** in South Africa and has no formally listed approved indications in this dataset.
The TxGNN model generated 10 top predicted indications; among these, **hypnic headache** emerges as the most clinically actionable candidate, backed by **multiple disease-specific case series and systematic reviews** — with several expert review articles explicitly recommending caffeine as the **preferred first-line therapy** for this rare sleep-related headache disorder.
Hypnic headache is the only indication in this analysis to reach a **Proceed with Guardrails** decision (Evidence Level L3), despite ranking 9th by raw TxGNN score, making it the primary focus of this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Known Role (No formal SAHPRA indication) | CNS stimulant; analgesic adjuvant in combination products; neonatal apnoea of prematurity treatment |
| Primary Predicted New Indication | Hypnic Headache |
| TxGNN Prediction Score | 99.17% (Rank #9 in top-10 predictions) |
| Evidence Level | L3 (case series, observational data, systematic reviews) |
| South Africa (SAHPRA) Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Proceed with Guardrails** |

---

## All TxGNN Top Predictions at a Glance

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|---------------------|-------------|---------------|---------|
| 1 | Nasal cavity disease | 99.91% | L5 | Hold |
| 2 | Thrombotic disease | 99.90% | L4 | Research Question |
| 3 | Acute laryngopharyngitis | 99.89% | L5 | Hold |
| 4 | Papillary conjunctivitis | 99.79% | L5 | Hold |
| 5 | Neuralgia | 99.34% | L3 | Research Question |
| 6 | Glossodynia | 99.26% | L5 | Hold |
| 7 | Coccygodynia | 99.22% | L5 | Hold |
| 8 | Trigeminal autonomic cephalalgia | 99.21% | L4 | Research Question |
| **9** | **Hypnic headache ⭐** | **99.17%** | **L3** | **Proceed with Guardrails** |
| 10 | Vein disease | 99.06% | L4 | Research Question |

> ⭐ **Focus indication:** Although ranked 9th by TxGNN score, hypnic headache is the only candidate meeting threshold for a "Proceed with Guardrails" recommendation. A higher TxGNN score alone does not indicate clinical readiness — evidence depth and mechanistic coherence are decisive. The remainder of this report details the hypnic headache case.

---

## Why is This Prediction Reasonable?

Formal mechanism of action (MOA) data for caffeine is not captured in the drug database fields of this evidence pack. However, caffeine's pharmacology is among the best-characterised of any bioactive compound: it acts primarily as a **non-selective adenosine A1/A2A receptor antagonist** and **phosphodiesterase (PDE) inhibitor**, producing CNS stimulation, mild cerebral vasoconstriction, increased cAMP levels in multiple cell types, and modulation of nociceptive signalling. These actions underpin its established role as an adjuvant in aspirin/paracetamol combination analgesics (enhancing analgesic efficacy by approximately 40%) and as a primary agent in neonatal apnoea of prematurity.

Hypnic headache (HH) is a rare benign primary headache disorder, characterised by recurrent nocturnal headache attacks that strictly awaken patients from sleep — both REM and NREM phases — typically lasting 15–180 minutes, and occurring almost exclusively in patients aged over 60 years. The most coherent pathophysiological hypothesis centres on **adenosine accumulation during sleep**: as sleep pressure escalates across the night, rising extracellular adenosine activates A1/A2A receptors within the trigeminovascular system, reducing the threshold for headache onset. Caffeine's primary pharmacological mechanism — direct, competitive blockade of A1/A2A adenosine receptors — would interrupt this precise trigger at its source, representing an unusually direct mechanistic alignment between drug and disease.

This is not speculative: three independent disease-focused reviews (Liang & Wang 2014; Lanteri-Minet 2014; Holle et al. 2013) and a systematic analysis of 348 published HH cases (Silva-Néto et al. 2019) consistently designate caffeine — taken at bedtime as 1–2 cups of strong coffee or a 40–60 mg caffeine tablet — as the **preferred first-line treatment** for both acute relief and nightly prophylaxis. Diener et al. (2012) state explicitly: *"Caffeine is the preferable first-line therapy for both acute treatment (i.e., a cup of strong coffee when awaking with headache) and prophylaxis."* No RCTs exist, reflecting the rarity of the condition (~1 per 100,000 persons per year), but the consistency of case-series evidence and the directness of the mechanistic rationale make this the most robust repurposing signal identified in this TxGNN analysis.

---

## Clinical Trial Evidence

Currently no clinical trials specifically investigating caffeine for hypnic headache are registered in ClinicalTrials.gov or the ICTRP.

> **Contextual note on related indications:** Nine clinical trials were retrieved under the neuralgia query (Rank #5, L3, Research Question). Review of these trials reveals that **none involve caffeine as a primary intervention** — they cover nerve block techniques (NCT03478735, NCT06374524, NCT04844229), cognitive-behavioural therapy for insomnia in pain populations (NCT06428006, NCT06434571), and exploratory neurostimulation studies. Their retrieval reflects broad keyword overlap rather than caffeine-specific evidence. Caffeine's role in neuralgia remains confined to animal models and historical case reports.

---

## Literature Evidence

The following publications are most relevant to caffeine for hypnic headache:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [22072057](https://pubmed.ncbi.nlm.nih.gov/22072057/) | 2012 | Clinical Review | *Current Treatment Options in Neurology* | Diener et al. explicitly designate caffeine as "the preferable first-line therapy for both acute treatment and prophylaxis" of hypnic headache; reviews all available case evidence and tolerability in the elderly |
| [24942086](https://pubmed.ncbi.nlm.nih.gov/24942086/) | 2014 | Systematic Review | *Cephalalgia* | Systematic review of HH clinical features and therapeutic options per ICHD-3β criteria; positions caffeine alongside indomethacin and lithium as primary treatment options |
| [25231430](https://pubmed.ncbi.nlm.nih.gov/25231430/) | 2014 | Review / Case Series | *Headache* | Comprehensive HH review; documents bedtime caffeine (coffee or tablet) as consistently effective with favourable tolerability in elderly patients |
| [23832130](https://pubmed.ncbi.nlm.nih.gov/23832130/) | 2013 | Review / Case Series | *Cephalalgia* | Holle et al. review clinical features and management; confirms caffeine as first-line approach, noting its practical advantages over indomethacin in the elderly |
| [31075680](https://pubmed.ncbi.nlm.nih.gov/31075680/) | 2019 | Systematic Review | *Journal of Neurological Sciences* | Most comprehensive synthesis available: 348 HH cases published 1988–2018; analyses treatment outcomes systematically, with caffeine among the most frequently reported effective interventions |
| [23728805](https://pubmed.ncbi.nlm.nih.gov/23728805/) | 2013 | Annual Review | *Current Pain and Headache Reports* | Reviews 2012 HH publications; highlights specific pharmacological and non-pharmacological successes with caffeine dosing regimens |
| [12654950](https://pubmed.ncbi.nlm.nih.gov/12654950/) | 2003 | Review (71 cases) | *Neurology* | Early seminal analysis of 71 HH cases including polysomnographic findings; establishes caffeine within the treatment algorithm and discusses pathophysiological hypotheses |
| [15111685](https://pubmed.ncbi.nlm.nih.gov/15111685/) | 2004 | PSG Study | *Neurology* | Polysomnographic monitoring of 10 HH patients documents attacks arising from both REM and NREM sleep — critical mechanistic evidence supporting adenosine accumulation as the common trigger |
| [35574653](https://pubmed.ncbi.nlm.nih.gov/35574653/) | 2023 | Comprehensive Review | *Critical Reviews in Food Science and Nutrition* | Reviews caffeine's full health effects including sleep, headache, and cardiovascular outcomes; contextualises dose-response relationships relevant to therapeutic application |
| [33974014](https://pubmed.ncbi.nlm.nih.gov/33974014/) | 2021 | Review | *JAMA* | Evidence-based headache management review; addresses rare primary headaches including HH within the broader neurological diagnostic framework, aiding clinical context for South African practitioners |

---

## South Africa Market Information

Caffeine holds **no SAHPRA product registrations** in South Africa. No products appear in the SAHPRA database under this active pharmaceutical ingredient as a standalone registered therapeutic agent.

> **Practical context for South African clinicians:** Caffeine is ubiquitously available as a dietary substance (coffee, tea, energy drinks). It appears as an unlisted adjuvant component in certain OTC combination analgesic products (e.g., aspirin/paracetamol combinations) that may hold SAHPRA registration — but caffeine itself carries no approved indication. For use as a directed therapeutic agent for hypnic headache, the prescriber should consider:
> - **Off-label prescribing** under informed consent (currently the most practical route)
> - **Section 21 authorisation** if a specific formulated product is required
> - Inclusion on institutional formularies with appropriate clinical justification
>
> This medicine is **not currently listed on the South African Essential Medicines List (EML)** for any indication.

---

## Safety Considerations

Formal SAHPRA-approved Professional Information (PI) for caffeine as a standalone registered medicine is not available. Please refer to the SAHPRA-approved PI of any combination product containing caffeine, and to published international prescribing information. Report any adverse drug reactions to SAHPRA via the **MedSafety** reporting system.

**Key safety considerations specifically relevant to hypnic headache use (derived from published literature):**

- **Elderly population risk**: Hypnic headache predominantly affects patients aged >60 years. Caffeine's cardiovascular effects — including elevated heart rate, raised blood pressure, and potential arrhythmia induction (see NCT05464940, the COFFEE-AF trial studying IV caffeine's atrial electrophysiological effects) — require individual cardiovascular risk assessment before initiating regular bedtime caffeine.
- **Withdrawal rebound headache**: Regular bedtime caffeine use may establish caffeine dependency. Abrupt discontinuation can trigger **caffeine withdrawal headache** (onset 12–24 hours after last dose), potentially confounding the headache diary and complicating management. Gradual dose tapering protocols should be planned from the outset.
- **Sleep architecture effects**: Caffeine taken at bedtime may paradoxically impair sleep quality in caffeine-naive or caffeine-sensitive patients. Initial response monitoring with a sleep diary is strongly advised.
- **Drug interactions via CYP1A2**: Caffeine is metabolised primarily by CYP1A2. Plasma levels increase with CYP1A2 inhibitors (ciprofloxacin, fluvoxamine, oral contraceptives) and decrease with CYP1A2 inducers (carbamazepine, rifampicin, cigarette smoking). Dose adjustment may be required accordingly.
- **Intraocular pressure**: Caffeine may transiently raise intraocular pressure; caution is warranted in patients with glaucoma.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple independent systematic reviews and case series consistently identify caffeine as the preferred first-line treatment for hypnic headache, underpinned by a mechanistic rationale — adenosine receptor blockade interrupting sleep-phase adenosine-mediated trigeminovascular activation — that is unusually direct and biologically coherent. While the absence of RCTs reflects the rarity of the condition rather than lack of clinical interest, the convergence of mechanistic plausibility with consistent real-world case evidence justifies cautious clinical application.

**To proceed, the following is needed:**

- **Geriatric cardiovascular safety assessment** before initiation: baseline ECG, blood pressure measurement, and review of co-medications with CYP1A2 interactions are mandatory given the elderly target population
- **Formulation and dose specification**: caffeine tablets (40–60 mg taken at bedtime) are preferable to coffee for reproducible dosing; neither is currently SAHPRA-registered for this indication — document the off-label use explicitly in the patient record
- **Structured response monitoring**: implement a standardised headache frequency/severity diary (minimum 4 weeks baseline + 4 weeks post-initiation); monitor sleep quality (Pittsburgh Sleep Quality Index or equivalent), blood pressure, and heart rate at each review
- **Withdrawal risk counselling**: counsel patients from day one on the risk of rebound withdrawal headache if doses are missed; provide a written cessation protocol
- **SAHPRA regulatory pathway clarification**: confirm with the institution's clinical governance team whether off-label prescribing guidance, a dedicated treatment protocol, or a broader Section 21 application is the appropriate route for individual or programme-level use
- **Formal MOA data retrieval**: query the DrugBank API for caffeine (DB00201) to populate the MOA field and strengthen future mechanistic documentation

---

> **Disclaimer**: This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All prescribing decisions must be made by qualified healthcare professionals in accordance with SAHPRA regulations and current South African clinical guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

