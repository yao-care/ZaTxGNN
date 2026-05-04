---
layout: default
title: Doravirine
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 3
---

# Doravirine
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

# Doravirine: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Doravirine (Pifeltro®) is a non-nucleoside reverse transcriptase inhibitor (NNRTI) approved internationally for HIV-1 infection in adults, though it currently holds no SAHPRA registration in South Africa.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**, with a high prediction score of **99.93%**.
However, **no clinical trials** and **no direct literature evidence** for doravirine in this indication are currently available, placing this prediction at **Evidence Level L5**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 Infection (FDA/EMA approved 2018; no SAHPRA registration on record) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Doravirine is a next-generation NNRTI that selectively binds to a non-catalytic allosteric pocket on the HIV-1 reverse transcriptase enzyme, blocking both RNA-dependent and DNA-dependent DNA polymerase activity. Its distinct binding profile compared to earlier NNRTIs (such as efavirenz) allows it to retain activity against many NNRTI-resistant viral variants, contributing to its approval as part of first-line HIV-1 antiretroviral therapy.

Simian Immunodeficiency Virus (SIV) is a lentivirus that naturally infects non-human primates and is the evolutionary precursor of HIV. SIV and HIV-1 share significant genomic and structural homology, including within the reverse transcriptase gene. This mechanistic overlap is the probable basis for TxGNN's high-confidence prediction: a drug that targets HIV-1 reverse transcriptase could, in principle, exhibit cross-reactive inhibitory activity against the closely related SIV reverse transcriptase. SIV/macaque models are in fact widely used in HIV antiretroviral research precisely because of this similarity.

It is important to note, however, that SIV infection in non-human primates serves primarily as a preclinical research model rather than a standalone human clinical target. The translational significance of this prediction for human healthcare is therefore indirect — it is more likely to inform animal model validation of antiretroviral combinations than to open a genuinely new clinical indication. The second-ranked prediction (feline acquired immunodeficiency syndrome, caused by the distantly related Feline Immunodeficiency Virus) has weaker mechanistic support given greater divergence in FIV reverse transcriptase structure.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Review | Current Opinion in HIV and AIDS | Discusses islatravir — a reverse transcriptase translocation inhibitor — for HIV-1 treatment and prevention; retrieved due to mechanistic overlap with reverse transcriptase inhibition, but does not evaluate doravirine or SIV directly |

> **Note:** The single publication retrieved in this search concerns islatravir (a different drug class), not doravirine, and addresses HIV-1 rather than SIV infection. No literature directly evaluating doravirine activity against SIV was identified. This evidence is therefore not counted toward the evidence level.

---

## South Africa Market Information

Doravirine is not currently registered with SAHPRA. No registration records are available.

For reference, doravirine is internationally approved as:
- **Pifeltro®** (doravirine 100 mg tablet, once daily) — FDA approved August 2018, EMA approved November 2018
- **Delstrigo®** (doravirine 100 mg / lamivudine 300 mg / tenofovir disoproxil fumarate 300 mg tablet) — FDA approved August 2018

Neither product has a documented entry on the South African Essential Medicines List (EML). Healthcare professionals requiring access should explore the SAHPRA Section 21 (unregistered medicine) authorisation pathway.

---

## Safety Considerations

As doravirine is not registered with SAHPRA, no locally approved Professional Information (PI) is available. Please consult the FDA-approved prescribing information for safety guidance. Report any adverse drug reactions to SAHPRA through the MedSafety reporting system.

Key safety considerations known from international labelling include:
- **CYP3A inducers**: Concomitant use with strong CYP3A inducers (e.g., rifampicin, carbamazepine, St John's Wort) significantly reduces doravirine plasma concentrations and may result in loss of virological response. This interaction is particularly relevant in South Africa where rifampicin is widely used for tuberculosis.
- **Immune Reconstitution Syndrome**: May occur in the setting of HIV treatment initiation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's high-confidence prediction for SIV infection is mechanistically plausible given the structural homology between HIV-1 and SIV reverse transcriptase, but SIV infection is a non-human primate research model rather than a human clinical indication. No clinical trials and no direct literature evidence for doravirine in this indication exist, and doravirine has no SAHPRA registration, making any clinical application in South Africa currently untenable.

**To proceed, the following is needed:**

- **Regulatory pathway**: Initiate SAHPRA Section 21 application if compassionate or research use is intended; track whether a full SAHPRA registration submission is planned
- **MOA data**: Retrieve complete mechanism of action and resistance profile data from DrugBank (DB12301) to strengthen or refine the mechanistic rationale
- **Safety data**: Download and parse the SAHPRA-equivalent PI or FDA label to complete safety screening (currently a blocking data gap)
- **Preclinical evidence search**: Conduct targeted searches for in vitro or primate studies evaluating doravirine or NNRTI class activity specifically against SIV strains
- **Indication re-evaluation**: Consider whether the clinically actionable repurposing target may be HIV-1 treatment optimisation (e.g., new combinations, drug-resistant strains) rather than SIV, given the animal model nature of the top-ranked prediction
- **Ranks 2 and 3 reassessment**: Feline AIDS and the neurodevelopmental disorder prediction (Rank 3) carry even lower mechanistic plausibility and should remain on Hold pending the above data gaps being resolved
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

