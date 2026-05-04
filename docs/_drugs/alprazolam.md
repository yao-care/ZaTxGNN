---
layout: default
title: Alprazolam
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 3
---

# Alprazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Alprazolam: From Anxiety / Panic Disorder to Insomnia

## One-Sentence Summary

Alprazolam is a benzodiazepine widely used internationally for anxiety disorders and panic disorder, acting by enhancing inhibitory GABA-A neurotransmission throughout the central nervous system.
The TxGNN model predicts it may be effective for **Insomnia**, with a prediction confidence of **99.81%**;
however, **no direct clinical trial or published literature** currently confirms alprazolam as a primary insomnia treatment, placing current evidence at Level 4 (mechanism-based only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anxiety disorder / Panic disorder |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L4 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Alprazolam is a triazolobenzodiazepine that potentiates GABA-A receptor-mediated chloride ion influx, increasing central inhibitory tone. This mechanism directly shortens sleep-onset latency and increases total sleep time — properties that are pharmacologically relevant to insomnia. The prediction is mechanistically sound: sleep and anxiety disorders both involve hyperarousal driven by GABA/glutamate imbalance and HPA axis dysregulation, and benzodiazepines have historically been used across both indications.

However, clinical suitability for insomnia is limited in practice. Shorter-acting Z-drugs (e.g., zolpidem) and low-dose sedating antidepressants are generally preferred for sleep induction; alprazolam's intermediate half-life (~11 hours), high abuse liability, and Schedule-controlled status place it well below first-line. Importantly, chronic use suppresses slow-wave sleep (SWS) and REM sleep, which can worsen overall sleep quality over time despite short-term benefit.

From a South African perspective, the primary barrier is regulatory: alprazolam has **no SAHPRA registration** and is not marketed in South Africa. Even if evidence were stronger, a formal new drug application would be required before any clinical deployment. Modern insomnia management guidelines — including those aligned with WHO recommendations relevant to South African primary care — prioritise Cognitive Behavioural Therapy for Insomnia (CBT-I) as first-line, with pharmacotherapy as adjunctive only.

---

## Clinical Trial Evidence

The 7 trials retrieved for the alprazolam + insomnia query are largely tangential. None directly evaluates alprazolam as a primary treatment for chronic insomnia; they address BZD cessation, perioperative sedation, or different drugs entirely.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Unknown | 1,400 | Prospective cohort (Taiwan) examining risk-benefit of hypnotics including benzodiazepines in elderly patients with sleep disorders; assesses efficacy, safety, pharmacokinetics and pharmacogenetics — the most relevant trial for the BZD-insomnia question, but status is unknown |
| [NCT00266409](https://clinicaltrials.gov/study/NCT00266409) | Phase 4 | Completed | 418 | Niravam™ (alprazolam ODT) combined with newly initiated SSRI/SNRI vs SSRI/SNRI alone in patients with GAD or panic disorder; anxiety-focused, not insomnia-focused |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | N/A | Completed | 170 | Electronic self-management programme to promote BZD cessation in US Veterans; cessation direction is opposite to evaluating insomnia efficacy — provides safety/dependence background only |
| [NCT03327506](https://clinicaltrials.gov/study/NCT03327506) | Phase 4 | Unknown | 128 | Hypnosis vs alprazolam premedication for perioperative anxiety in gynaecological surgery; acute sedation, not chronic insomnia treatment |
| [NCT01584440](https://clinicaltrials.gov/study/NCT01584440) | Phase 2 | Completed | 220 | AVP-923 (dextromethorphan/quinidine) for agitation in Alzheimer's disease; different drug and different indication |
| [NCT01146600](https://clinicaltrials.gov/study/NCT01146600) | Phase 2 | Completed | 26 | Clarithromycin for hypersomnia (excessive sleepiness); different drug and opposite sleep disorder |
| [NCT01893632](https://clinicaltrials.gov/study/NCT01893632) | Phase 2 | Terminated | 2 | Gabapentin for BZD dependence treatment; terminated early with only 2 participants enrolled — highlights BZD dependence risks rather than insomnia efficacy |

---

## Literature Evidence

Currently no related literature directly evaluating alprazolam for insomnia is available.

---

## South Africa Market Information

Alprazolam is **not currently registered with SAHPRA** and is not marketed in South Africa. No product licences are on record, and no dosage forms are available through registered channels. This constitutes a significant regulatory barrier: clinical use would require either a Section 21 unregistered medicine authorisation (for individual patients) or a full SAHPRA new drug application for any systematic repurposing programme.

> Healthcare professionals considering use under Section 21 should note that alprazolam is internationally classified as a controlled substance (Schedule IV in the USA; equivalent scheduling would apply in South Africa under the Medicines and Related Substances Act).

---

## Safety Considerations

Alprazolam has no SAHPRA-approved Professional Information (PI). Prescribers should consult the manufacturer's international prescribing information (FDA label, EMA SmPC). Based on internationally recognised data, the following are key considerations:

- **Dependence and withdrawal**: Physical dependence develops with regular use beyond 2–4 weeks; abrupt discontinuation can precipitate withdrawal seizures, requiring gradual taper
- **Sedation and psychomotor impairment**: Falls, road traffic accidents, and cognitive impairment are significant risks, particularly in patients over 65
- **Sleep architecture disruption**: Chronic use suppresses slow-wave sleep and REM sleep — potentially worsening the very condition being treated
- **Respiratory depression**: Risk is substantially increased when co-administered with opioids, alcohol, or other CNS depressants; potentially fatal combinations
- **Anterograde amnesia**: Documented in controlled studies with agoraphobia/panic patients receiving alprazolam

Report any adverse drug reactions to SAHPRA at [https://www.sahpra.org.za](https://www.sahpra.org.za).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction is mechanistically plausible — alprazolam's GABA-A enhancement does produce sedative-hypnotic effects relevant to insomnia. However, no dedicated clinical trial or published literature directly supports alprazolam for insomnia as a primary indication, evidence remains at L4 (mechanism-based only), and the drug has no SAHPRA registration in South Africa. Proceeding without stronger evidence and regulatory standing would not meet standard of care requirements.

> **Important secondary finding:** The TxGNN model also predicted alprazolam for **Agoraphobia** (rank 3, TxGNN score 99.56%), which carries **L1 evidence** — supported by multiple completed multicentre RCTs published in *Archives of General Psychiatry* (1988), the *British Journal of Psychiatry* (1993, 1994), and a 2011 meta-analysis in *Journal of Clinical Psychopharmacology* — with a recommendation of **Proceed with Guardrails**. This indication is a substantially more actionable repurposing opportunity and warrants a dedicated evaluation report.

**To proceed with the insomnia indication, the following is needed:**

- Initiate SAHPRA registration (via new drug application or Section 21 pathway) as the primary regulatory prerequisite
- Commission a dedicated Phase 2/3 RCT directly evaluating alprazolam for chronic insomnia against standard-of-care comparators (CBT-I, zolpidem, low-dose doxepin)
- Obtain complete mechanism of action and full prescribing information via DrugBank API and manufacturer data
- Conduct comparative effectiveness review vs. non-BZD insomnia options, including cost-effectiveness analysis relevant to the South African public health context
- Establish a robust dependence monitoring and pharmacovigilance plan prior to any patient exposure, with particular attention to high-risk groups (elderly, those with prior substance use disorders)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

