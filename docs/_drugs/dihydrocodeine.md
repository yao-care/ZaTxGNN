---
layout: default
title: Dihydrocodeine
parent: Model Prediction Only (L5)
nav_order: 177
evidence_level: L5
indication_count: 10
---

# Dihydrocodeine
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

# Dihydrocodeine: From Opioid Analgesic and Antitussive to Nasal Cavity Disease

## One-Sentence Summary

Dihydrocodeine is an opioid (mu-receptor agonist) used for pain relief and cough suppression. The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. It rests on a graph-based model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA register data; generally used as an analgesic and antitussive |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Dihydrocodeine is a semi-synthetic opioid that acts on mu-opioid receptors. It provides analgesia and suppresses the cough reflex centrally.

**The link to nasal cavity disease is weak.** No clear mechanistic connection was identified, and the very high model score is not backed by any clinical or literature support. At most, the drug might give symptomatic relief (for example, of cough or pain) in upper airway conditions. That would not treat the disease itself.

**The other top predictions are mostly implausible too:**
- *Acute laryngopharyngitis:* plausible only as cough relief, not disease modification.
- *Cervical disc degenerative disorder:* plausible only as symptomatic analgesia, which the drug already provides, so it is not a new use.
- *Allergic urticaria, cold urticaria, atopic conjunctivitis, papillary conjunctivitis:* opioids can trigger histamine release, so benefit is biologically unlikely and harm is possible.
- *Faucial diphtheria:* the drug has no antimicrobial or antitoxin activity.
- *Headache disorder and trigeminal autonomic cephalalgia:* opioids are generally discouraged because of medication-overuse headache and dependence risk.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for nasal cavity disease.

Only the lower-ranked prediction "headache disorder" returned two papers. Neither shows efficacy: one is a 2002 case series on cough-syrup abuse ([PMID 11915306](https://pubmed.ncbi.nlm.nih.gov/11915306/)), and the other is a 2017 Cochrane review digest ([PMID 28521551](https://pubmed.ncbi.nlm.nih.gov/28521551/)).

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| B1041 ACT 101 OF 1965 | Paracodin | Syrup | Not stated in register data |
| B730 (ACT 101) | Df 118 1ml | Injection | Not stated in register data |

Essential Medicines List (EML) inclusion status was not provided.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug interaction records were found in the queried source. This should not be read as an absence of interactions. As an opioid, dihydrocodeine carries known risks of dependence, misuse and respiratory depression, so these need review in the PI before any repurposing work.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials, no publications and no plausible mechanism for nasal cavity disease. The opioid class also carries dependence and misuse risks that would need strong efficacy evidence to justify.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for both SAHPRA registrations
- Clinical review of whether any predicted indication (for example, symptomatic cough relief in acute laryngopharyngitis) is worth pursuing
- Evidence from trials or literature for the chosen indication
- Route compatibility assessment against the syrup and injection forms available

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

