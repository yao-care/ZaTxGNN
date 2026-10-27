---
layout: default
title: Etoricoxib
parent: Model Prediction Only (L5)
nav_order: 221
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Etoricoxib: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the SAHPRA registration data (general pharmacology sour…"
monitor_inn: "Etoricoxib"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "ulerythema ophryogenesis", "pulmonary hypertension", "benign prostatic hyperplasia (disease)", "kyphoscoliotic heart disease", "headache disorder", "trigeminal autonomic cephalalgia"]
---

# Etoricoxib
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

## Etoricoxib: From an Unspecified Registered Indication to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Etoricoxib is a selective COX-2 inhibitor. The SAHPRA registration data compiled for this report do not state its approved indication, although general pharmacology sources describe use in arthritis, back pain, acute pain and gout. The TxGNN model predicts it may be effective for **migraine disorder**, but **no clinical trials** and only **1 indirectly related publication** (a scoping review) support this specific prediction. The best-supported related direction is **indomethacin-responsive primary headache disorders**, which rest on case reports only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data (general pharmacology sources list rheumatoid arthritis, osteoarthritis, chronic lower back pain, ankylosing spondylitis, acute pain and gout) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 (mechanistic plausibility only; no clinical studies in migraine) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Etoricoxib is, however, a well-known selective COX-2 inhibitor (target gene PTGS2), and it is used for inflammatory and pain conditions.

Prostaglandins produced via COX-2, such as PGE2, are thought to contribute to neurogenic inflammation and sensitisation of the trigeminovascular system in migraine. This makes a role for COX-2 inhibition biologically plausible. A preclinical study in rat trigeminal ganglia examined NSAIDs, including etoricoxib, and their effect on CGRP and PGE2 release, which gives indirect mechanistic support.

It is important to be clear about the limits of the evidence. The only publication linked directly to the migraine prediction is a scoping review of fasting-induced headache during Ramadan, which does not show that etoricoxib works in migraine. The prediction is therefore a research question, not an established use.

**Other predictions in the model output:**
- **Headache disorder and trigeminal autonomic cephalalgia** have the most clinical support. Case reports and small series describe etoricoxib responses in indomethacin-responsive headaches (primary stabbing headache, secondary cough headache, and some trigeminal autonomic cephalalgias). These are low-level observations without controlled trials.
- **Pulmonary hypertension, kyphoscoliotic heart disease, atrophoderma vermiculata and ulerythema ophryogenesis** have no credible mechanistic link and are likely network artefacts. The pulmonary hypertension prediction carries a potential harm signal.
- **Benign prostatic hyperplasia** has only a weak theoretical rationale and no supporting studies.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Publications linked to the top prediction (migraine disorder) and to the closest related headache predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42841395](https://pubmed.ncbi.nlm.nih.gov/42841395/) | 2026 | Review | Pain management | Scoping review of fasting-induced headache during Ramadan; does not provide direct evidence of etoricoxib efficacy in migraine |
| [29209105](https://pubmed.ncbi.nlm.nih.gov/29209105/) | 2017 | Preclinical (rat) | Mediators of inflammation | Oral nimesulide, etoricoxib and ketoprofen altered CGRP and PGE2 release from rat trigeminal ganglia (indirect mechanistic support only) |
| [35277974](https://pubmed.ncbi.nlm.nih.gov/35277974/) | 2022 | Case series/observational | Headache | Etoricoxib and celecoxib effective in indomethacin-responsive headache disorders, including some trigeminal autonomic cephalalgias |
| [36893522](https://pubmed.ncbi.nlm.nih.gov/36893522/) | 2023 | Case report | Clinical neurology and neurosurgery | Two patients with secondary cough headache responded to etoricoxib |
| [18171381](https://pubmed.ncbi.nlm.nih.gov/18171381/) | 2008 | Case report | European journal of neurology | Primary stabbing headache responsive to etoricoxib |
| [17883876](https://pubmed.ncbi.nlm.nih.gov/17883876/) | 2007 | Case report | Journal of medical case reports | Etoricoxib used to treat idiopathic stabbing headache |
| [25229174](https://pubmed.ncbi.nlm.nih.gov/25229174/) | 2014 | Case report (adverse event) | Clinical neuropharmacology | Reversible cerebral vasoconstriction syndrome possibly induced by etoricoxib (safety signal) |
| [21373319](https://pubmed.ncbi.nlm.nih.gov/21373319/) | 2010 | Case report (adverse event) | International journal of emergency medicine | Life-threatening hyperkalaemia and acute kidney dysfunction after etoricoxib in a patient taking telmisartan (safety signal) |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 49/20.2.8/0399 | Erestz | Film-coated tablet (Fct) | Not stated in the compiled registration data |

Etoricoxib has 1 valid single-ingredient registration. Essential Medicines List (EML) status is not available in the data compiled for this report.

## Safety Considerations

- **Drug Interactions**: The interaction query completed, but it returned only pharmacological target information (COX-2 / PTGS2) and no specific drug-drug interaction entries. A published case report describes severe hyperkalaemia and acute kidney injury when etoricoxib was taken with telmisartan on a potassium-rich, low-sodium diet.
- **Published safety signals**: Case reports describe possible reversible cerebral vasoconstriction syndrome with etoricoxib. As a class, COX-2 inhibitors are associated with cardiovascular risk (including myocardial infarction), fluid retention and raised blood pressure. This is relevant to any use in headache and argues against use in pulmonary hypertension or cardiac disease.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction rests on a high model score and biological plausibility, but no clinical trial or direct clinical study of etoricoxib in migraine was found. Only case-level evidence exists for related indomethacin-responsive headaches, and there are cardiovascular, renal and cerebrovascular safety signals. The SAHPRA safety information has not yet been reviewed.

**To proceed, the following is needed:**
- The SAHPRA Professional Information for Erestz (approved indication, warnings, contraindications), which is a blocking gap for safety screening
- Detailed mechanism of action data (for example from DrugBank)
- A structured literature search for controlled studies of etoricoxib or other COX-2 inhibitors in migraine and in indomethacin-responsive headaches
- A defined target population and a cardiovascular and renal risk assessment before any study design
- Confirmation of EML status and of the approved indication in the South African context
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

