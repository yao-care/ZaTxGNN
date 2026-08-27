---
layout: default
title: Famciclovir
parent: 僅模型預測 (L5)
nav_order: 217
evidence_level: L5
indication_count: 10
---

# Famciclovir
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

# Famciclovir: From Herpes Zoster to Post-Infectious Neuralgia

## One-Sentence Summary

> Famciclovir is a well-established oral antiviral, originally used for herpes zoster (shingles) and related herpesvirus infections — though the evidence pack itself does not carry that original-indication field (see data gap below).
> The TxGNN model predicts it may be effective for **Post-Infectious Neuralgia** (i.e., postherpetic neuralgia, PHN),
> with **2 registered clinical trials** and **no dedicated publications** currently supporting this specific link, and neither trial actually tests famciclovir.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in this evidence pack (Data Gap DG002 — see below); herpes zoster/genital herpes is famciclovir's well-known approved use, based on general pharmacological knowledge, not this pack's data |
| Predicted New Indication | Post-Infectious Neuralgia |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (Data Gap **DG002**, High severity). Based on generally established pharmacological knowledge — not sourced from this pack — famciclovir is an oral prodrug of penciclovir, a nucleoside analogue that is phosphorylated by viral thymidine kinase and inhibits herpesvirus DNA polymerase; it is widely used against varicella-zoster virus (VZV) and herpes simplex virus (HSV) infections, including herpes zoster.

Post-infectious neuralgia (essentially postherpetic neuralgia, PHN) is a well-recognized complication of herpes zoster. Early antiviral treatment during the acute zoster phase is already understood to reduce the duration and severity of zoster-associated pain, which is mechanistically adjacent to — rather than truly novel relative to — famciclovir's existing antiviral role.

However, this mechanistic plausibility is **not confirmed by the trial evidence actually retrieved**: neither of the two clinical trials linked to this prediction tests famciclovir itself (see below). The prediction should therefore be read as a knowledge-graph association reflecting disease/drug-class proximity, not as direct experimental support.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06798662](https://clinicaltrials.gov/study/NCT06798662) | N/A | Not Yet Recruiting | 120 | Evaluates liposomal bupivacaine and ropivacaine nerve blocks for acute herpes zoster pain, and whether nerve blockade reduces required gabapentin dosage. **Does not test famciclovir.** |
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | N/A | Unknown | 140 | Investigates whether early oxycodone use during the acute herpes zoster phase prevents postherpetic neuralgia. **Does not test famciclovir.** |

**Caveat:** Both trials study the herpes zoster / PHN disease space but neither evaluates famciclovir as an intervention. No trial in this pack directly tests famciclovir for post-infectious neuralgia.

---

## Literature Evidence

Currently no related literature available for this specific indication (0 PubMed records returned for "Famciclovir" + "post-infectious neuralgia" per query log).

---

## South Africa Market Information

Famciclovir is currently **not marketed** in South Africa according to this evidence pack, with **0 SAHPRA registrations** recorded. No product/registration data is available to tabulate.

---

## Safety Considerations

Detailed SAHPRA-approved warnings, contraindications, and drug interaction data are not available in this evidence pack. This is flagged as **Data Gap DG001 (Blocking severity)** — its stated impact is that safety cannot proceed to the initial S1 safety evaluation stage. Please refer to the SAHPRA-approved Professional Information (PI), once identified, for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Safety data is a Blocking-severity gap (DG001) that by definition prevents initial safety evaluation, and no clinical trial in this pack directly tests famciclovir for the predicted indication — evidence level is L5 (model prediction only). The drug also has no current SAHPRA registration in South Africa.

**To proceed, the following is needed:**
- TFDA/SAHPRA-approved Professional Information (warnings, contraindications, DDI) to resolve DG001
- Confirmed mechanism-of-action documentation (DrugBank or equivalent) to resolve DG002
- Direct clinical evidence evaluating famciclovir specifically for post-infectious/postherpetic neuralgia as an endpoint (not proxy analgesic trials)
- Confirmation of famciclovir's registration pathway/status if market entry to South Africa is being considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

