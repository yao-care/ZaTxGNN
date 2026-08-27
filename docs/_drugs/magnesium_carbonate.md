---
layout: default
title: Magnesium Carbonate
parent: 僅模型預測 (L5)
nav_order: 298
evidence_level: L5
indication_count: 10
---

# Magnesium Carbonate
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

# Magnesium Carbonate: From Antacid Use to Active Peptic Ulcer Disease

## One-Sentence Summary

> Magnesium carbonate is a classic antacid, long used to neutralize gastric acid and relieve hyperacidity symptoms.
> The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**,
> with **no registered clinical trials** but **4 supporting publications** (3 of them randomized controlled trials) currently backing this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the evidence pack (no SAHPRA licence text available); magnesium carbonate is classically classified as an antacid used for symptomatic relief of gastric hyperacidity |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L2 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for magnesium carbonate is not available from DrugBank in this evidence pack (data gap DG002). Based on known pharmacological classification — and consistent with the repurposing rationale attached to this candidate — magnesium carbonate is a classic antacid: it reacts with gastric hydrochloric acid to form magnesium chloride, water, and carbon dioxide, thereby neutralizing gastric acid and raising intragastric pH.

Active peptic ulcer disease is fundamentally an acid/pepsin-mediated condition — mucosal injury occurs when acid and pepsin exposure overwhelms the stomach or duodenum's protective mechanisms. Since magnesium carbonate's core action is direct acid neutralization, the mechanistic link to peptic ulcer disease is strong and well precedented: antacids were a mainstay of ulcer therapy before H2-receptor antagonists and proton pump inhibitors (PPIs) became standard of care. Historical randomized trials (summarized below) directly tested antacid regimens against cimetidine and placebo in patients with active duodenal and prepyloric ulcers, providing direct — if dated — clinical support for this mechanistic reasoning.

Two caveats temper this otherwise strong mechanistic fit. First, magnesium salts can accumulate in patients with renal impairment, raising a hypermagnesemia risk that must be screened for before repurposing in this population. Second, magnesium carbonate can chelate with co-administered drugs such as tetracyclines and fluoroquinolones, reducing their absorption — a clinically important drug-interaction consideration even though no formal DDI data on this specific pairing were retrieved (see Safety Considerations).

---

## Clinical Trial Evidence

Currently no related clinical trials registered for active peptic ulcer disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT | Scandinavian Journal of Gastroenterology | In 72 patients with active duodenal/prepyloric ulcers, a 12-week double-blind trial found 3-week healing rates of 67% with cimetidine and 50% with an antacid/anticholinergic regimen, both significantly better than placebo |
| [6755656](https://pubmed.ncbi.nlm.nih.gov/6755656/) | 1982 | RCT | Scandinavian Journal of Gastroenterology. Supplement | Companion report evaluating antacid/anticholinergic vs. cimetidine vs. placebo in active prepyloric and duodenal ulcer treatment |
| [3003883](https://pubmed.ncbi.nlm.nih.gov/3003883/) | 1985 | RCT | Scandinavian Journal of Gastroenterology | In 80 patients with active duodenal ulcer given antacid tablets (120 mmol HCl/day neutralizing capacity) plus high- or low-fiber diet, ulcer healing was 67.5% vs. 60% at 4 weeks, with no significant difference in symptom relief between fiber groups |
| [35720246](https://pubmed.ncbi.nlm.nih.gov/35720246/) | 2022 | Review/In-vitro | Medicine and Pharmacy Reports | Evaluated the acid-neutralizing capacity (ANC) and other pharmaceutical properties of antacid products (including magnesium-based formulations) marketed in Morocco |

---

## South Africa Market Information

Magnesium carbonate currently has **no SAHPRA-registered products** in South Africa (Market Status: Not Marketed; Total Registrations: 0). No product-level registration data (registration number, brand name, dosage form) is available in the evidence pack.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note: retrieval of TFDA/SAHPRA-equivalent label warnings and contraindications is flagged as a **Blocking** data gap (DG001) in this evidence pack — this must be resolved before a formal safety (S1) assessment can proceed. Independently, the mechanistic rationale for this candidate flags two specific risks worth monitoring even before PI data is obtained: magnesium accumulation in patients with renal impairment, and reduced absorption of co-administered tetracyclines or fluoroquinolones due to chelation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between magnesium carbonate's acid-neutralizing action and active peptic ulcer disease's acid-mediated pathophysiology is strong, and three historical RCTs support antacid efficacy in ulcer healing comparable to early H2-antagonist therapy. However, all supporting evidence predates the PPI era (1981–1985), no modern or South Africa–specific trials exist, and a blocking safety data gap remains unresolved.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI): warnings, precautions, and contraindications (resolves blocking gap DG001)
- Confirmed mechanism-of-action data from DrugBank (resolves gap DG002)
- Renal-function-based dosing/monitoring guidance given magnesium accumulation risk in renal impairment
- Drug-interaction protocol addressing chelation with tetracyclines and fluoroquinolones
- Positioning assessment against current standard-of-care (PPIs/H2RAs), since supporting evidence predates modern ulcer therapy
- A regulatory pathway assessment, since the product is not currently marketed or registered in South Africa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

