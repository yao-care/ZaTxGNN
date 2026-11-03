---
layout: default
title: Ceftriaxone
parent: Model Prediction Only (L5)
nav_order: 106
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-03
monitor_inn: "Ceftriaxone"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "chronic otitis media"]
description: "Ceftriaxone: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Not recorded in the local data"
---

# Ceftriaxone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Ceftriaxone: Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Ceftriaxone is a injectable cephalosporin-type (beta-lactam) antibacterial that is currently marketed in South Africa.
The TxGNN model predicts it may be relevant to **hyperamylasemia** (score 0.9939), but **no clinical trials** and no publications that test ceftriaxone for this condition were found.
Because of this, the prediction is not supported by biological rationale, and the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 0.9939 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 5 of 6) |
| Number of SAHPRA Registrations | 6 (valid: 5) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ceftriaxone is an antibacterial beta-lactam, and it is not known to lower serum amylase.

The direction of association appears more likely to be an adverse effect than a therapeutic benefit. Ceftriaxone is known to cause biliary sludge and pseudolithiasis, which can occasionally be associated with pancreatitis and raised amylase. A high model score alone is therefore not backed by a plausible biological explanation, and the prediction should be treated as a model signal rather than a treatment hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the retrieved publications tests ceftriaxone as a treatment for hyperamylasemia. They are indirect at best.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10458061](https://pubmed.ncbi.nlm.nih.gov/10458061/) | 1999 | Clinical study | Bratisl Lek Listy | Ceftriaxone 1 g given as prophylaxis to 30 patients after endoscopic papillosphincterotomy, compared with 30 untreated patients. The focus was prevention of post-procedural infection, not treatment of raised amylase. |
| [7522351](https://pubmed.ncbi.nlm.nih.gov/7522351/) | 1994 | Cohort | South Med J | In 38 patients with intracranial bleeding, elevated pancreatic enzymes (lipase, amylase) occurred without pancreatitis. Describes the condition only; ceftriaxone was not studied. |
| [36263834](https://pubmed.ncbi.nlm.nih.gov/36263834/) | 2023 | Case report | Rev Esp Enferm Dig | Case of Weil syndrome with upper gastrointestinal bleeding. No evidence of a therapeutic effect on hyperamylasemia. |

---

## South Africa Market Information

Ceftriaxone is marketed in South Africa as single-ingredient injectable products. Five registrations are currently valid and one is cancelled. The approved indication text is not recorded in the local data. Essential Medicines List status is not available from the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 47/20.1.1/1245 | Obkef 1G Injection | Injection | Not available |
| Reg. No. 48/20.1.1/0228 | Ceftriaxone 1G Fksa | Injection | Not available |
| Reg. No. 37/20.1.1/0042 | Adco Ceftriaxone powder for injection | Injection | Not available |
| Reg. No. 37/20.1.1/0368 | Rociject powder for injection | Injection | Not available |
| Reg. No. R/20.1.1/47 | Rocephin | Injection | Not available |

---

## Safety Considerations

- **Drug Interactions** (a total of 100 interactions were recorded; the main ones are listed here):
  - **Major:** calcium chloride, calcium glucoheptonate, calcium gluconate (calcium-containing products)
  - **Moderate:** kanamycin, neomycin, streptomycin, picosulfuric acid
- **Biliary and pancreatic effects:** Ceftriaxone is associated with biliary pseudolithiasis and sludge, which may occasionally be linked to pancreatitis and raised amylase. This is relevant because the predicted condition may represent an adverse-effect signal.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction has no supporting clinical trials and no publications testing ceftriaxone for hyperamylasemia (Evidence Level L5). There is also no plausible mechanism, and the known biliary effects suggest the association may reflect an adverse effect rather than a benefit.

**To proceed, the following is needed:**
- Mechanism of action data for ceftriaxone and a pharmacological rationale for any effect on amylase.
- Review of the SAHPRA Professional Information for warnings and contraindications.
- Evidence from studies that directly examine ceftriaxone in hyperamylasemia, including whether the signal reflects drug-induced biliary or pancreatic effects.

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

