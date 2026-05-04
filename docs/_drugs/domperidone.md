---
layout: default
title: Domperidone
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 1
---

# Domperidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Domperidone: From Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Domperidone is a peripheral dopamine D2/D3 receptor antagonist, widely used as an antiemetic and prokinetic agent for nausea, vomiting, and gastroparesis.
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
with **no clinical trials** and **no published literature** currently supporting this specific direction — making this a model-only prediction at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Nausea, vomiting, and gastroparesis (dopamine antagonist / prokinetic) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, domperidone is a peripheral dopamine D2 and D3 receptor antagonist that acts primarily at the gut wall and the area postrema (chemoreceptor trigger zone), which lies outside the blood-brain barrier. Its established efficacy in nausea, vomiting, and delayed gastric emptying is well documented.

Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) is a rare X-linked disorder caused by gain-of-function mutations in the AVPR2 gene (encoding the renal vasopressin V2 receptor), resulting in constitutive receptor activation, excessive water retention, and dilutional hyponatraemia — even in the absence of elevated arginine vasopressin (AVP/ADH) levels. The mechanistic rationale linking domperidone to NSIAD is indirect: dopaminergic pathways are known to modulate tubular water reabsorption and AVP secretion, and D2 receptor activity has been implicated in renal electrolyte handling. By blocking peripheral D2/D3 receptors, domperidone could theoretically influence this regulatory axis.

However, the connection between a prokinetic antiemetic and a rare renal channelopathy is not well established in clinical or preclinical literature. The TxGNN knowledge graph model captures network-level relationships between drug targets and disease nodes that may not yet have direct experimental validation. This prediction should therefore be treated as a hypothesis-generating signal requiring independent mechanistic and clinical verification before any repurposing strategy is considered.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR, PACTR).

---

## Literature Evidence

Currently no related literature available (PubMed search: domperidone AND nephrogenic syndrome of inappropriate antidiuresis returned 0 results as of 2026-04-20).

---

## South Africa Market Information

Domperidone currently holds **no SAHPRA registrations** and is **not marketed** in South Africa according to available regulatory data.

> **Note:** Domperidone is registered and widely used in numerous other jurisdictions (e.g., EU, Canada, Australia, UK) under brand names such as *Motilium*. Its absence from the SAHPRA register does not reflect a global safety withdrawal — it may reflect an unsubmitted or lapsed registration. Prescribers should verify current SAHPRA status directly before any use.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> **Important context for prescribers:** Although formal safety data was not available in this Evidence Pack, domperidone carries a well-known class-level concern regarding QT interval prolongation and an increased risk of serious cardiac arrhythmia (including sudden cardiac death), particularly at higher doses and in patients with pre-existing cardiac risk factors or those taking concomitant QT-prolonging medications. The European Medicines Agency (EMA) and Health Canada have issued risk minimisation measures on this basis. These warnings should be carefully considered in any repurposing evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is currently zero clinical or preclinical evidence linking domperidone to Nephrogenic Syndrome of Inappropriate Antidiuresis; the prediction is based entirely on the TxGNN knowledge graph model (L5 evidence), and domperidone is not registered with SAHPRA, meaning a full regulatory dossier would be required before any South African clinical use.

**To proceed, the following is needed:**

- **Mechanistic validation:** Commission a targeted literature and expert review to determine whether dopamine D2/D3 receptor antagonism has any plausible, experimentally supported effect on AVPR2 constitutive activity or renal water handling in NSIAD models
- **Preclinical evidence:** Identify or initiate in vitro / in vivo studies in NSIAD cell lines or animal models (e.g., AVPR2 gain-of-function knock-in mice) to test domperidone's effect on aquaporin-2 trafficking and urinary osmolality
- **Safety dossier:** Retrieve and review domperidone's SAHPRA (or EMA/Health Canada) full Professional Information for contraindications, QT-risk profile, and drug interaction data to assess suitability for a renally impaired or electrolyte-disturbed patient population
- **SAHPRA registration pathway:** Given zero current SAHPRA registrations, a Section 21 (unregistered medicine) application or full registration submission would be required before any investigational or compassionate use in South Africa
- **Patient population consideration:** NSIAD is an ultra-rare disease (primarily affecting neonatal/paediatric males); any development plan must account for paediatric pharmacokinetics and the specific cardiac safety concerns associated with domperidone in this age group

---

*This report is generated for research and clinical decision-support purposes only. It does not constitute medical advice or a recommendation for off-label prescribing. All repurposing candidates require clinical validation before therapeutic use. Adverse drug reactions should be reported to SAHPRA via the MedSafety reporting system.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

