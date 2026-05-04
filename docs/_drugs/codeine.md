---
layout: default
title: Codeine
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 4
---

# Codeine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Codeine: From Cough Suppression and Pain Relief to Nasal Cavity Disease

---

## One-Sentence Summary

Codeine is a well-established opioid analgesic and centrally acting antitussive, classically used for mild-to-moderate pain relief and cough suppression. The TxGNN model predicts it may be effective for **Nasal Cavity Disease** with a score of 99.93%, but this prediction is supported by **0 clinical trials** and only **2 publications** — both of which document opioid-related *adverse* nasal events rather than any therapeutic benefit. This signal is assessed as a model false-positive, and the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Mild-to-moderate pain; cough suppression (antitussive) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this Evidence Pack. Based on established pharmacological knowledge, codeine is a naturally occurring phenanthrene alkaloid and opioid prodrug metabolised to morphine primarily via CYP2D6. Its central effects are mediated through μ-opioid receptor agonism in the medullary cough centre and ascending pain pathways, producing antitussive and analgesic actions respectively. Peripherally, codeine is also a direct mast cell degranulator, which underlies several of its known adverse effects.

A superficial mechanistic argument could be constructed: μ-opioid receptor activation theoretically suppresses neurogenic secretion from nasal mucosal glands, which might reduce rhinorrhoea in certain nasal conditions. However, this theoretical pathway has no clinical translation in the repurposing literature. The two publications retrieved document opioid *harm* in the nasal cavity — specifically, intranasal abuse of a hydrocodone-acetaminophen product causing mucosal necrosis, and impacted codeine-opium material forming a nasal rhinolith. Neither study examines codeine as a therapeutic agent for nasal cavity disease.

The high TxGNN prediction score almost certainly reflects statistical co-occurrence of opioid drug terminology with nasal cavity disease literature in the training knowledge graph, rather than a genuine drug–disease therapeutic relationship. This is a recognised model artefact (false-positive signal) and does not constitute evidence of repurposing potential.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [22965281](https://pubmed.ncbi.nlm.nih.gov/22965281/) | 2012 | Case Report | *The Laryngoscope* | Intranasal abuse of hydrocodone-acetaminophen tablets caused progressive necrosis of the nasal cavity and pharynx — documents a serious adverse/abuse event, not a therapeutic use of codeine |
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case Report | *Ear, Nose & Throat Journal* | A 21-year-old presented with chronic nasal obstruction caused by a hardened codeine-opium pellet ("opioma") acting as a rhinolith nidus — documents an unusual iatrogenic foreign body complication, not therapeutic benefit |

> ⚠️ **Interpretation note:** Both retrieved publications record opioid-associated nasal pathology arising from misuse or exposure, not controlled therapeutic trials. There is no positive efficacy signal in the literature for codeine in nasal cavity disease.

---

## South Africa Market Information

Codeine (DrugBank ID: DB00318) is **not currently registered with SAHPRA** and is not available as a marketed pharmaceutical product in South Africa. No registration records are on file.

> For information on codeine's regulatory and scheduling status in South Africa, consult SAHPRA directly or refer to the South African Medicines Formulary (SAMF).

---

## Safety Considerations

Detailed SAHPRA-approved warnings and contraindications for codeine are not available in this Evidence Pack (Data Gap DG001). Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Contextually relevant safety concerns** known from international regulatory sources include:

- **Opioid dependence and misuse potential:** Codeine is a Schedule 5 or Schedule 6 substance in many jurisdictions; abuse potential is high and directly relevant to the nasal cavity adverse events identified in this evidence pack.
- **CYP2D6 pharmacogenomic variability:** Ultra-rapid metabolisers convert codeine to morphine rapidly, risking life-threatening respiratory depression; poor metabolisers may obtain no therapeutic benefit.
- **Mast cell degranulation (pseudoallergy):** Codeine directly triggers non-IgE-mediated mast cell histamine release, causing urticaria, pruritus, and bronchospasm — relevant to any expanded use consideration.
- **Paediatric use restrictions:** Multiple international agencies (EMA, US FDA) have restricted or contraindicated codeine use in children under 12 following fatal respiratory events.
- **Drug–drug interactions:** Concurrent use with CNS depressants, benzodiazepines, or other opioids carries risk of additive respiratory depression.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction of codeine for nasal cavity disease represents a false-positive model signal with no supporting clinical evidence — the retrieved literature exclusively documents opioid-related nasal harm, and no mechanistic pathway supports therapeutic benefit. All four predicted indications in this evidence pack are assessed as Hold at the current evidence stage (L5 or L4 at best), and codeine is not registered with SAHPRA.

**To proceed beyond Hold, the following would be required:**

- A credible and specific mechanistic hypothesis linking codeine's pharmacology to a treatable nasal cavity condition (e.g., a defined subtype with neurogenic secretion as the dominant pathophysiology)
- At least one prospective, controlled clinical study demonstrating measurable therapeutic benefit in nasal cavity disease
- A comprehensive SAHPRA-approved Professional Information (PI) and safety review — currently unavailable (Data Gap DG001)
- Confirmed MOA data from DrugBank or equivalent source (Data Gap DG002)
- Regulatory feasibility assessment given codeine's controlled substance scheduling restrictions in South Africa
- A risk–benefit analysis addressing codeine's well-documented dependence, respiratory depression, and pseudoallergic risks in the context of a non-life-threatening nasal condition

---

## Other Evaluated Indications (Summary)

All four TxGNN predictions for codeine are currently assessed as **Hold** at evidence level L5 or L4. The table below summarises the full prediction set evaluated in this pack:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision | Key Concern |
|------|---------------------|-------------|----------------|----------|-------------|
| 1 | Nasal Cavity Disease | 99.93% | L5 | **Hold** | Literature documents opioid-related nasal harm (abuse/misuse), not therapeutic use; likely false-positive signal |
| 2 | Acute Laryngopharyngitis | 99.92% | L5 | **Hold** | No supporting literature; codeine's antitussive effect is non-specific and may impair secretion clearance in viral infection; addiction risk disproportionate to benefit |
| 3 | Trigeminal Autonomic Cephalalgia (TAC) | 99.43% | L5 | **Hold** | European Headache Federation guidelines explicitly advise against opioids in TAC due to high medication-overuse headache (MOH) risk; case report evidence is incidental, not supportive |
| 4 | Allergic Urticaria | 99.37% | L4 | **Hold** | Codeine directly *induces* urticaria via mast cell degranulation and is used as a positive control in skin reactivity testing — the mechanistic direction is diametrically opposite to treatment |

> **Overall assessment:** None of the four TxGNN predictions represent actionable repurposing opportunities for codeine. The model has identified statistical associations between codeine and these conditions, but in each case the underlying pharmacological relationship is either adverse (codeine *causes* the condition), non-specific (general opioid receptor effects with unfavourable benefit-risk), or explicitly contraindicated by clinical guidelines.

---

*This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All adverse drug reactions should be reported to SAHPRA.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

