---
layout: default
title: Sulfadoxine
parent: 僅模型預測 (L5)
nav_order: 417
evidence_level: L5
indication_count: 10
---

# Sulfadoxine
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

# Sulfadoxine: From Antimalarial Use to Gout

## One-Sentence Summary

Sulfadoxine is a long-acting sulfonamide, historically used in combination with pyrimethamine as an antimalarial; detailed original-indication and mechanism-of-action data were not supplied in this evidence pack. The TxGNN model predicts possible efficacy in **Gout**, but this direction is currently supported by **0 clinical trials** and only **1 tangentially related publication** (a case series on toxic epidermal necrolysis, not gout). The evidence pack's own mechanistic review flags this prediction as a likely false positive arising from shared purine-metabolism graph nodes.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in evidence pack (sulfadoxine is historically a sulfonamide antimalarial, typically combined with pyrimethamine) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 99.10% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for sulfadoxine in this evidence pack. Based on known information, sulfadoxine is a sulfonamide antifolate antimicrobial/antimalarial agent (classically paired with pyrimethamine, e.g. Fansidar) that acts via inhibition of dihydropteroate synthase in the folate synthesis pathway of susceptible organisms.

Gout is a disorder of purine/uric acid metabolism, treated by inhibiting xanthine oxidase (e.g. allopurinol) or promoting renal uric acid excretion. There is no established pharmacological link between antifolate/antibacterial activity and uric acid metabolism.

The evidence pack's own repurposing rationale is explicit on this point: it states there is no known mechanistic connection, and that the single supporting publication (PMID 22285617, a burns-unit case series on toxic epidermal necrolysis — a severe drug reaction, not a gout treatment study) is unrelated to gout. The authors note this prediction likely reflects a spurious knowledge-graph association, possibly driven by shared "purine metabolism" nodes connecting sulfadoxine to a cluster of unrelated predictions (gout, hyperuricemia, Lesch-Nyhan syndrome) in this same evidence pack. This mechanistic implausibility should be weighed heavily against the high TxGNN score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22285617](https://pubmed.ncbi.nlm.nih.gov/22285617/) | 2012 | Case Series | Journal of the American Academy of Dermatology | Describes 5-year burns-unit experience treating toxic epidermal necrolysis (TEN); a severe adverse drug reaction report, not related to gout treatment |

Note: this is the only literature item associated with the gout prediction and does not provide mechanistic or clinical support for the indication.

---

## South Africa Market Information

Sulfadoxine currently has no SAHPRA product registrations recorded in this evidence pack (0 licenses, market status: Not marketed).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no plausible mechanistic link between sulfadoxine's antifolate/antimalarial activity and uric acid metabolism, no clinical trial evidence, and the single associated publication is unrelated to gout. The evidence pack's own analysis identifies this as a likely spurious graph-based association rather than a genuine repurposing signal. Sulfadoxine is also not currently marketed or registered in South Africa, which is a further barrier independent of the efficacy question.

**To proceed, the following is needed:**
- Confirmed original indication and mechanism-of-action data for sulfadoxine (currently data gaps)
- SAHPRA-approved Professional Information (warnings, contraindications, drug interactions) — currently unavailable
- Preclinical or mechanistic studies directly linking sulfadoxine to uric acid/purine metabolism, if this direction is to be pursued further
- Independent re-evaluation of the other TxGNN-predicted indications for this drug (bronchitis, several rare congenital/genetic syndromes, diabetic nephropathy, conjunctivitis, appendicitis, peritonitis), as the same evidence pack flags most of these as similarly low-confidence or mechanistically implausible
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

