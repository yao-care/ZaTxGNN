---
layout: default
title: Potassium Iodide
parent: 僅模型預測 (L5)
nav_order: 370
evidence_level: L5
indication_count: 10
---

# Potassium Iodide
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

Using the drug-repurposing evaluation report format to turn this Evidence Pack into the SA pharmacist-facing report.

# Potassium Iodide: From Undocumented Original Indication(s) to Nasal Cavity Disease

## One-Sentence Summary

Potassium iodide's original indication and mechanism of action are not documented in this evidence pack (both flagged as data gaps); it is not currently marketed in South Africa. The TxGNN model predicts potential activity against **Nasal Cavity Disease**, but this is currently supported only by **4 case-report publications** (no clinical trials), most of them veterinary rather than human data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap — no `original_indications` or SAHPRA/TFDA license text available) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 (case reports/mechanistic reasoning only, no controlled trials) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for potassium iodide in this evidence pack. Based on the literature that did surface, potassium iodide (as a saturated solution, SSKI) has a long-standing history as an antifungal agent for subcutaneous and mucosal mycoses (e.g. sporotrichosis, pythiosis, entomophthoromycosis), which is thought to relate to direct iodide antifungal activity and host immune modulation.

The predicted indication — nasal cavity disease — aligns with this established off-label antifungal use: three of the four supporting publications describe successful treatment of fungal infections of the nasal cavity (rhinofacial pythiosis in sheep, mycotic rhinitis in a horse, *Pseudallescheria boydii* nasal infection in a horse) and one describes nasofacial zygomycosis in a human patient responding to potassium iodide therapy. This gives the prediction biological plausibility.

However, the evidence base is thin and skewed: three of the four reports are veterinary (sheep, horse) rather than human, all are single case reports (no controlled comparison), and the most recent human case report dates to 1994. There is no clinical trial evidence for this specific indication, and the drug's original approved indication(s) are not on file, which limits any mechanistic comparison to a known original use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Nasal Cavity Disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7997795](https://pubmed.ncbi.nlm.nih.gov/7997795/) | 1994 | Case Report | Rev Inst Med Trop Sao Paulo | Human nasofacial zygomycosis case; rapid response to potassium iodide therapy |
| [39576399](https://pubmed.ncbi.nlm.nih.gov/39576399/) | 2024 | Case Report | Veterinary Research Communications | Mycotic rhinitis (Aspergillus fumigatus) in a horse; treated with topical clotrimazole plus oral potassium iodide |
| [34902797](https://pubmed.ncbi.nlm.nih.gov/34902797/) | 2022 | Case Report | Journal de Mycologie Médicale | Rhinofacial pythiosis in sheep successfully treated with potassium iodide |
| [10976304](https://pubmed.ncbi.nlm.nih.gov/10976304/) | 2000 | Case Report | J Am Vet Med Assoc | *Pseudallescheria boydii* nasal cavity infection in a horse; treated with intranasal miconazole plus sodium iodide |

---

## South Africa Market Information

Potassium iodide currently has no SAHPRA registrations on file and is not marketed in South Africa (0 licenses recorded). No product/dosage-form information is available to summarise here.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Additional flag from this evidence pack:** while reviewing other TxGNN-predicted indications for this drug, allergic urticaria was flagged — the rationale explicitly notes that potassium iodide is a *known cause* of iodide-induced urticaria/vasculitis (an adverse reaction), not a treatment for it. This is a reminder to review iodide hypersensitivity history before any off-label antifungal use is considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence for nasal cavity disease is limited to four case reports (mostly veterinary), with no clinical trials, and the drug is not currently marketed in South Africa.
- Most critically, TFDA/SAHPRA-equivalent product warnings and contraindications are a **Blocking** data gap — the pack itself notes this prevents even an initial (S1) safety evaluation, so no repurposing decision can responsibly proceed yet.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI): warnings, contraindications, and drug interactions (currently a Blocking data gap)
- Mechanism of action data from DrugBank or equivalent source (currently a High-severity data gap)
- The drug's documented original/approved indication(s), to enable a proper mechanistic comparison
- Human clinical evidence (ideally comparative) for antifungal use in nasal/sinus mycosis, given current data is almost entirely veterinary case reports
- Screening for iodide hypersensitivity history given the urticaria/vasculitis signal noted elsewhere in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

