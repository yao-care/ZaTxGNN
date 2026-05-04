---
layout: default
title: Candesartan Cilexetil
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 5
---

# Candesartan Cilexetil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Candesartan Cilexetil: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Candesartan cilexetil is an angiotensin II receptor blocker (ARB) used globally for the treatment of hypertension and heart failure, though no formal SAHPRA registration data was retrievable in this Evidence Pack.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease** — a severe hypertension-driven acute renal injury with limited targeted treatment options — with a prediction confidence of **99.68%**.
Currently, **no registered clinical trials** and **no directly relevant publications** specific to this indication were identified, placing the evidence at Level L4 (mechanistic rationale only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / Heart failure (ARB class; no SAHPRA registration data retrieved in this Evidence Pack) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L4 |
| South Africa Market Status | Not registered (no SAHPRA licences retrieved) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Candesartan cilexetil is a prodrug that is hydrolysed to its active metabolite candesartan during gastrointestinal absorption. Candesartan selectively and competitively antagonises the angiotensin II type 1 receptor (AT1R), thereby interrupting the renin-angiotensin-aldosterone system (RAAS). The net effect is sustained reduction of vasoconstriction, suppression of aldosterone secretion, attenuation of sympathetic nervous system activation, and — critically — reduction of intraglomerular hypertension and proteinuria. Detailed pharmacological MOA data was not retrievable from DrugBank for this Evidence Pack; however, the above is well-established in the clinical literature for the ARB class.

Malignant hypertensive renal disease (malignant nephrosclerosis) is characterised by acute, severe microvascular injury to the kidney driven by extreme systemic blood pressure elevation. The pathological core is hyperactivation of the RAAS: circulating angiotensin II acts via AT1R to cause intense afferent arteriolar vasoconstriction, promote glomerular hypertension, stimulate inflammatory and pro-fibrotic cascades, and accelerate nephron loss. This makes AT1R blockade the most mechanistically direct pharmacological intervention available, and the TxGNN prediction — linking candesartan to this disease — is therefore rated as having very strong mechanistic plausibility (★★★★★).

The relationship between candesartan's established indications and malignant hypertensive renal disease is essentially a severity extension of the same pathophysiology. Existing hypertension guidelines and emergency management frameworks already advocate for RAAS blockade in hypertensive urgencies with renal involvement (where bilateral renal artery stenosis has been excluded). The TxGNN model's high prediction score reflects this tight mechanistic alignment, and the prediction should be viewed as a hypothesis to be formally tested rather than a novel or unexpected finding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

No SAHPRA registration records were retrieved for candesartan cilexetil in this Evidence Pack (0 licences, market status: not registered). This is likely a **data gap** rather than a true absence from the South African market — candesartan cilexetil (e.g., Atacand®, AstraZeneca, and multiple generic products) is registered and marketed in numerous countries, including several African markets. Healthcare professionals should verify current registration status directly via the [SAHPRA online drug register](https://www.sahpra.org.za/find-a-medicine/).

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| — | Not retrieved | — | — |

> **Essential Medicines List (EML) status** cannot be confirmed from this data. ARB-class agents are included on the National EML for hypertension in many low- and middle-income countries; EML status for South Africa should be verified through the [National Department of Health](https://www.health.gov.za/).

---

## Safety Considerations

Formal SAHPRA warnings, contraindications, and drug interaction data were not retrievable for this Evidence Pack (classified as blocking and high-severity data gaps respectively).

Please refer to the SAHPRA-approved Professional Information (PI) for complete safety information. Adverse drug reactions should be reported to SAHPRA via the [MedSafety online reporting portal](https://www.sahpra.org.za/pharmacovigilance/).

> **Clinically important caution specific to the predicted indication:** ARBs carry a well-recognised risk of precipitating acute kidney injury in patients with bilateral renal artery stenosis or a solitary functioning kidney, as these patients depend on angiotensin II–mediated efferent arteriolar tone to maintain glomerular filtration pressure. This risk is directly relevant given the predicted indication of malignant hypertensive renal disease, which frequently involves underlying renovascular pathology. Renal function, serum potassium, and blood pressure must be monitored closely when initiating any ARB in this setting.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case for candesartan in malignant hypertensive renal disease is scientifically compelling — AT1R blockade directly addresses the RAAS-driven pathophysiology at the centre of this disease — but the complete absence of registered clinical trials and directly relevant clinical literature (Evidence Level L4) means there is insufficient clinical evidence to recommend immediate advancement. The unresolved SAHPRA registration status adds further regulatory uncertainty for South African practice.

**To proceed, the following is needed:**

- **Verify SAHPRA registration status** for candesartan cilexetil products (suspected data gap; check the SAHPRA drug register directly)
- **Retrieve SAHPRA Professional Information (PI)** to complete the mandatory safety, warnings, and contraindications assessment (currently a Blocking data gap — required before any S1 safety evaluation can be conducted)
- **Obtain full MOA data** from DrugBank API (DB00796) to formalise the mechanistic rationale (currently a High-severity data gap)
- **Conduct a targeted systematic literature search** for ARBs (not limited to candesartan) in malignant hypertensive nephropathy and malignant nephrosclerosis, as evidence may exist under broader class-level or disease-specific search terms not captured in the current query
- **Screen for bilateral renal artery stenosis** in any future patient-level evaluation — the related TxGNN prediction of malignant renovascular hypertension (Rank 2) is rated Hold due to the safety concern of precipitating acute renal failure, and this risk applies to this indication as well
- **Explore observational registry or case-series design** if no prospective trial evidence is identified, given the rarity and severity of malignant hypertensive renal disease makes large RCTs logistically challenging

---

> **Disclaimer:** This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require formal clinical validation before therapeutic application. All clinical decisions must be made by a qualified healthcare professional with reference to approved prescribing information.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

