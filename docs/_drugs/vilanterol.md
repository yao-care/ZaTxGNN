---
layout: default
title: Vilanterol
parent: 僅模型預測 (L5)
nav_order: 459
evidence_level: L5
indication_count: 10
---

# Vilanterol
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

# Vilanterol: From an Undocumented Original Indication to Obstructive Lung Disease

## One-Sentence Summary

Vilanterol (DrugBank DB09082) is a long-acting beta2-agonist (LABA) that, per the available evidence, is not independently marketed for any single condition — it is developed only as a component of fixed-dose inhaler combinations. The TxGNN model predicts it may be effective for **Obstructive Lung Disease**, with **50 clinical trials** and **20 publications** currently supporting this direction. The evidence pack also flags a **Blocking** data gap on SAHPRA-approved safety labelling, which must be resolved before any regulatory decision.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no approved monotherapy indication on record) |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for vilanterol is not available in the evidence pack (data gap DG002). However, the supporting literature itself describes vilanterol's pharmacology: PMID 23232038 characterizes it as "a novel inhaled long-acting β2-agonist with inherent 24-h activity ... in development as a combination with the inhaled corticosteroid fluticasone furoate for both COPD and asthma." Vilanterol is never marketed alone — it appears only in fixed-dose combination inhalers: fluticasone furoate/vilanterol (Relvar Ellipta), umeclidinium/vilanterol (Anoro Ellipta), and fluticasone furoate/umeclidinium/vilanterol (Trelegy Ellipta), all of which appear by name in the trial evidence collected here.

Because vilanterol's therapeutic role has always been bronchodilation in obstructive airway disease, the TxGNN prediction of "Obstructive Lung Disease" is mechanistically unsurprising — it largely reconfirms vilanterol's existing global role in COPD and asthma management rather than identifying a genuinely novel indication. The practical significance for South Africa is therefore less about discovering new pharmacology and more about a **market-access gap**: vilanterol-containing combination inhalers are extensively validated internationally but are not currently registered with SAHPRA.

This is further reinforced by the scale of the supporting clinical programme — including the large outcomes trial IMPACT (NCT01313676, n=16,568) demonstrating a mortality benefit, and multiple additional Phase 3 trials across both COPD and asthma populations — which collectively represent one of the most extensively studied LABA-based combination platforms in respiratory medicine.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01313676](https://clinicaltrials.gov/study/NCT01313676) | Phase 3 | Completed | 16,568 | Outcomes study of fluticasone furoate/vilanterol vs. placebo on survival in moderate COPD with cardiovascular risk |
| [NCT02345161](https://clinicaltrials.gov/study/NCT02345161) | Phase 3 | Completed | 1,811 | FF/UMEC/VI once-daily vs. budesonide/formoterol twice-daily in COPD; improved lung function and health status |
| [NCT02924688](https://clinicaltrials.gov/study/NCT02924688) | Phase 3 | Completed | 2,436 | FF/UMEC/VI vs. FF/VI dual therapy in inadequately controlled asthma |
| [NCT02105974](https://clinicaltrials.gov/study/NCT02105974) | Phase 3 | Completed | 1,621 | FF/VI 100/25mcg vs. vilanterol monotherapy in COPD, isolating FF's contribution to lung function |
| [NCT02729051](https://clinicaltrials.gov/study/NCT02729051) | Phase 3 | Completed | 1,055 | "Closed" triple therapy (FF/UMEC/VI) vs. "open" triple (FF/VI + UMEC) in COPD |
| [NCT01316913](https://clinicaltrials.gov/study/NCT01316913) | Phase 3 | Completed | 872 | UMEC/VI vs. UMEC monotherapy vs. tiotropium over 24 weeks in COPD |
| [NCT03248128](https://clinicaltrials.gov/study/NCT03248128) | Phase 3 | Completed | 906 | FF/VI vs. FF alone in uncontrolled paediatric/adolescent asthma (ages 5-17) |
| [NCT01822899](https://clinicaltrials.gov/study/NCT01822899) | Phase 3 | Completed | 717 | UMEC/VI vs. fluticasone propionate/salmeterol over 12 weeks in COPD |
| [NCT01323634](https://clinicaltrials.gov/study/NCT01323634) | Phase 3 | Completed | 519 | 24-hour pulmonary function profile: FF/VI vs. fluticasone propionate/salmeterol in COPD |
| [NCT04937387](https://clinicaltrials.gov/study/NCT04937387) | Phase 3 | Completed | 359 | Bridging study of FF/UMEC/VI vs. FF/VI in Chinese participants with inadequately controlled asthma |

No SANCTR or Pan African Clinical Trials Registry (PACTR) entries were identified for this indication in the evidence pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29668352](https://pubmed.ncbi.nlm.nih.gov/29668352/) | 2018 | RCT | New England Journal of Medicine | IMPACT trial: once-daily single-inhaler triple therapy reduces COPD exacerbations vs. dual therapy |
| [32162970](https://pubmed.ncbi.nlm.nih.gov/32162970/) | 2020 | RCT (post-hoc) | Am J Respir Crit Care Med | FF/UMEC/VI reduces all-cause mortality vs. UMEC/VI in COPD (IMPACT trial) |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | RCT | Am J Respir Crit Care Med | FULFIL trial: once-daily triple therapy improves lung function and health status vs. ICS/LABA |
| [32918892](https://pubmed.ncbi.nlm.nih.gov/32918892/) | 2021 | RCT | The Lancet Respiratory Medicine | CAPTAIN trial: FF/UMEC/VI vs. FF/VI in inadequately controlled asthma |
| [29094315](https://pubmed.ncbi.nlm.nih.gov/29094315/) | 2017 | RCT | Advances in Therapy | Head-to-head comparison of UMEC/VI and tiotropium/olodaterol in symptomatic COPD |
| [31281061](https://pubmed.ncbi.nlm.nih.gov/31281061/) | 2019 | RCT subgroup analysis | The Lancet Respiratory Medicine | Blood eosinophil counts predict differential response to ICS-containing therapy (IMPACT) |
| [32299860](https://pubmed.ncbi.nlm.nih.gov/32299860/) | 2020 | RCT subgroup analysis | European Respiratory Journal | Effect of exacerbation history on treatment outcomes (IMPACT trial) |
| [35849317](https://pubmed.ncbi.nlm.nih.gov/35849317/) | 2022 | Network meta-analysis | Advances in Therapy | FF/UMEC/VI compared with other triple and dual COPD therapies |
| [39696097](https://pubmed.ncbi.nlm.nih.gov/39696097/) | 2024 | Systematic review/meta-analysis | BMC Pulmonary Medicine | Comparative efficacy of UMEC/VI vs. other bronchodilators in COPD |
| [39797646](https://pubmed.ncbi.nlm.nih.gov/39797646/) | 2024 | Cohort study | BMJ | Real-world comparative effectiveness and safety of single-inhaler triple therapies in COPD |

---

## South Africa Market Information

No SAHPRA registrations were found for vilanterol or vilanterol-containing products. Internationally, vilanterol is marketed only within fixed-dose combination inhalers referenced in the trial evidence — fluticasone furoate/vilanterol (Relvar Ellipta), umeclidinium/vilanterol (Anoro Ellipta), and fluticasone furoate/umeclidinium/vilanterol (Trelegy Ellipta) — none of which currently appear on the South African register based on available data.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The efficacy evidence is strong (L1: multiple completed large Phase 3 RCTs, including the pivotal IMPACT trial demonstrating a mortality benefit), but a **Blocking** data gap on TFDA/SAHPRA-approved warnings and contraindications means the mandatory S1 safety initial evaluation cannot currently be completed, and the product has zero SAHPRA registrations in South Africa.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) for vilanterol-containing combination products (warnings, contraindications, drug interactions)
- Confirmed mechanism-of-action data from DrugBank (DG002)
- Assessment of a South African registration/import pathway for the relevant combination products (Relvar Ellipta, Anoro Ellipta, Trelegy Ellipta)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

