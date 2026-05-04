---
layout: default
title: Brinzolamide
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 10
---

# Brinzolamide
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

# Brinzolamide: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Brinzolamide (Azopt®) is a topical carbonic anhydrase-II inhibitor globally indicated for reducing elevated intraocular pressure (IOP) in ocular hypertension and primary open-angle glaucoma, but currently not registered with SAHPRA in South Africa.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**, with **no clinical trials** and **no publications** currently supporting this specific indication.
The high prediction score of **99.48%** reflects mechanistic overlap with broader glaucoma subtypes rather than direct clinical evidence for this hereditary form.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ocular hypertension and primary open-angle glaucoma (globally approved; not SAHPRA-registered) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L4 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this dataset (DrugBank retrieval pending). Based on established pharmacological knowledge, Brinzolamide is a sulfonamide-derived carbonic anhydrase inhibitor. It selectively inhibits the CA-II isoenzyme in the ciliary body epithelium, reducing Na⁺/HCO₃⁻ co-transport and thereby decreasing aqueous humour production by approximately 17–20%. This IOP-lowering mechanism has been validated across numerous Phase 3 randomised controlled trials in patients with open-angle glaucoma and ocular hypertension worldwide.

Primary hereditary glaucoma encompasses conditions such as juvenile open-angle glaucoma (predominantly associated with *MYOC* gene mutations) and primary congenital glaucoma (associated with *CYP1B1* mutations). The unifying pathology is structural dysfunction of the trabecular meshwork or anterior chamber angle, leading to impaired aqueous drainage and chronically elevated IOP. The TxGNN model identifies the mechanistic rationale: when aqueous outflow is structurally compromised, reducing aqueous inflow through CA-II inhibition could still provide clinically meaningful IOP reduction as an adjunctive strategy.

However, it is important to recognise the limitations of this rationale. Brinzolamide's mechanism does not address the underlying genetic pathology driving trabecular meshwork dysfunction. In congenital and juvenile hereditary glaucoma, surgical correction of anterior chamber angle anatomy (goniotomy, trabeculotomy) remains the definitive treatment. Furthermore, systemic absorption of topical carbonic anhydrase inhibitors carries a risk of metabolic acidosis — a particularly important consideration in infant and paediatric populations where primary congenital glaucoma is diagnosed. Efficacy and safety data for Brinzolamide in this specific hereditary population are entirely absent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for primary hereditary glaucoma.

---

## Literature Evidence

Currently no related literature available for primary hereditary glaucoma.

---

## South Africa Market Information

Brinzolamide has no current SAHPRA registration. As of the data cut-off (April 2026), Brinzolamide — including brand-name products such as Azopt® (brinzolamide 1% ophthalmic suspension) and fixed-combination products such as Azarga® (brinzolamide/timolol) and Simbrinza® (brinzolamide/brimonidine) — is **not marketed** in South Africa. Any clinical use would require a Section 21 unregistered medicine application to SAHPRA.

---

## Safety Considerations

Please refer to the manufacturer's global Professional Information (PI) for complete safety information, as no SAHPRA-approved PI exists for this unregistered product. Report any adverse drug reactions to SAHPRA.

**Clinically relevant safety note:** A published case report ([PMID 39870471](https://pubmed.ncbi.nlm.nih.gov/39870471/), *BMJ Case Reports*, 2025) documented topical brinzolamide-induced unilateral ciliary body effusion presenting acutely with secondary angle closure and myopic shift. The effusion resolved promptly upon cessation of brinzolamide and instillation of atropine. This rare but serious adverse event is particularly relevant when considering use in patients with anatomically shallow anterior chambers or genetic predispositions to angle closure — a population that may overlap with certain hereditary glaucoma presentations. Prescribers should be aware of this risk prior to any compassionate-use or trial application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials or peer-reviewed publications directly evaluating Brinzolamide in primary hereditary glaucoma, and the drug has no SAHPRA registration pathway currently established in South Africa. The complete absence of clinical evidence in this hereditary subtype, combined with unresolved safety questions for paediatric populations, means the evidentiary threshold for advancing this indication has not been met.

**To proceed, the following is needed:**
- Formal mechanism of action documentation via DrugBank API retrieval (DrugBank ID: DB01194)
- Targeted literature review for Brinzolamide use specifically in hereditary glaucoma subtypes (*MYOC*, *CYP1B1* mutation carriers) and juvenile open-angle glaucoma
- Pharmacokinetic data in paediatric populations, including systemic carbonic anhydrase inhibition risk and metabolic acidosis potential in infants
- Comparative effectiveness assessment against dorzolamide (a related CAI that may have existing South African market presence) for the hereditary glaucoma setting
- SAHPRA registration pathway assessment or Section 21 application strategy for Brinzolamide 1% ophthalmic suspension
- Ophthalmology specialist input on whether Brinzolamide offers a clinically meaningful advantage over existing IOP-lowering agents currently accessible in South Africa for hereditary glaucoma management

---

> ⚠️ **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All content is based on predictive modelling and available evidence as of April 2026.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

