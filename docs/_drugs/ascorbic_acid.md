---
layout: default
title: Ascorbic Acid
parent: 僅模型預測 (L5)
nav_order: 47
evidence_level: L5
indication_count: 10
---

# Ascorbic Acid
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

# Ascorbic Acid: From Vitamin C Deficiency to Esophageal Disease

## One-Sentence Summary

Ascorbic acid (Vitamin C) is a water-soluble essential vitamin with a well-established role in preventing and treating vitamin C deficiency (scurvy), and widely used as a nutritional supplement supporting collagen synthesis and immune function.
The TxGNN model predicts it may have protective or therapeutic effects in **Esophageal Disease** (TxGNN rank 2, score 99.90%),
with **5 clinical trials** and **20 publications** providing contextual support — though the evidence remains at Level 3 (observational and mechanistic), and a biologically important counter-signal means this finding represents a research question rather than an immediate treatment recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vitamin C deficiency / Scurvy prevention |
| Predicted New Indication | Esophageal Disease |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L3 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ascorbic acid is the physiologically active form of Vitamin C and functions principally as a potent hydrophilic antioxidant and essential enzyme cofactor. It is required for the activity of prolyl-4-hydroxylase and lysyl hydroxylase — enzymes that stabilise the collagen triple helix — as well as dopamine β-hydroxylase and several other monooxygenases. It directly neutralises reactive oxygen species (ROS) in aqueous compartments and regenerates oxidised vitamin E, making it a critical component of the body's antioxidant network. It also enhances non-haem iron absorption by reducing ferric iron (Fe³⁺) to the bioavailable ferrous form (Fe²⁺) in the intestinal lumen.

Three mechanistic pathways support the TxGNN prediction for oesophageal disease: **(1) Inhibition of N-nitroso compound (NOC) formation** — in the acidic oesophageal and gastric environment, ascorbic acid competitively scavenges nitrous acid, reducing the synthesis of carcinogenic NOCs linked to oesophageal squamous cell carcinoma (ESCC), an effect of particular epidemiological relevance to southern Africa; **(2) Oxidative mucosal protection** — gastro-oesophageal acid reflux generates sustained ROS that injure the oesophageal epithelium and may drive progression from reflux oesophagitis to Barrett's oesophagus; ascorbic acid's antioxidant activity may attenuate this cascade; **(3) Direct anti-tumour activity** — in vitro studies demonstrate that ascorbic acid potentiates tea polyphenol-induced apoptosis in the Eca-109 oesophageal carcinoma cell line via MAPK pathway activation, and a co-culture model shows it biases cell competition in favour of normal over neoplastic oesophageal cells.

However, a critical counter-signal must be highlighted: in acid reflux animal models, combined exposure to ascorbic acid and dietary sodium nitrite paradoxically enhanced oesophageal carcinogenesis, likely through nitric oxide generation under acidic conditions. This dual mechanistic role — protective in some contexts, potentially pro-carcinogenic in others — creates an important safety uncertainty that must be resolved before any therapeutic recommendations can be made for patients with gastro-oesophageal reflux disease (GORD).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00342654](https://clinicaltrials.gov/study/NCT00342654) | N/A | Completed | 32,902 | Linxian Nutritional Intervention Trial (China) – landmark 40-year follow-up study (1985–2025) of the world's largest oesophageal cancer chemoprevention cohort; evaluated multivitamin/mineral combinations including vitamin C in a population with the highest documented oesophageal cancer rate globally; earlier results showed multivitamin supplementation reduced premalignant lesion burden |
| [NCT02695186](https://clinicaltrials.gov/study/NCT02695186) | N/A | Unknown | 180 | Oxidative stress and inflammation markers in intestinal metaplasia (a Barrett's oesophagus precursor) and metabolic syndrome; directly relevant to ascorbic acid's antioxidant mechanism in the oesophago-gastric junction |
| [NCT07212998](https://clinicaltrials.gov/study/NCT07212998) | Phase 3 | Not Yet Recruiting | 750 | PREEVEnT Trial (2026–2030) – plasma resuscitation in severe thermal burns (≥20% BSA); ascorbic acid included as adjunctive component; indirect relevance via mucosal injury mechanism |
| [NCT03610256](https://clinicaltrials.gov/study/NCT03610256) | N/A | Completed | 382 | SADI-S vs Roux-en-Y gastric bypass comparison for morbid obesity; low direct relevance to ascorbic acid in oesophageal disease |
| [NCT02881372](https://clinicaltrials.gov/study/NCT02881372) | N/A | Withdrawn | 0 | Eosinophilic oesophagitis oral desensitisation pilot in children – withdrawn prior to enrolment; not relevant to ascorbic acid mechanism |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [35703897](https://pubmed.ncbi.nlm.nih.gov/35703897/) | 2022 | Meta-analysis | Nutrition and Cancer | Updated dose-response meta-analysis (18 studies; 4,126 cases; 36,902 controls): dietary vitamin C intake significantly inversely associated with oesophageal cancer risk |
| [26355388](https://pubmed.ncbi.nlm.nih.gov/26355388/) | 2016 | Meta-analysis | Int J Cancer | Dose-response meta-analysis: higher dietary vitamin C associated with reduced risk of oesophageal cancer across multiple study designs |
| [36014780](https://pubmed.ncbi.nlm.nih.gov/36014780/) | 2022 | Mendelian Randomisation | Nutrients | Two-sample MR analysis of circulating antioxidants (including vitamin C) and digestive system tumour risk; addresses confounding limitations of observational studies |
| [24025629](https://pubmed.ncbi.nlm.nih.gov/24025629/) | 2013 | Prospective Cohort | Am J Clin Nutr | Prediagnostic plasma vitamin C levels inversely associated with gastric adenocarcinoma and ESCC risk in a large Chinese high-risk cohort; supports biological plausibility |
| [23892041](https://pubmed.ncbi.nlm.nih.gov/23892041/) | 2013 | In vitro | Biochem Biophys Res Commun | Ascorbic acid enhances EGCG- and TF3-induced apoptosis in oesophageal carcinoma (Eca-109) cells and lung adenocarcinoma cells via MAPK pathway activation; caspase-3/9 activity confirmed |
| [22026449](https://pubmed.ncbi.nlm.nih.gov/22026449/) | 2011 | In vitro | BMC Cancer | Oesophageal cell co-culture model: ascorbic acid identified as a modulator of competitive dynamics between normal and neoplastic oesophageal cells, favouring normal cell survival |
| [8598417](https://pubmed.ncbi.nlm.nih.gov/8598417/) | 1995 | Review | J Am Coll Nutr | Critical appraisal: evidence for ascorbic acid inhibiting carcinogenesis is stronger for gastric cancer than oesophageal cancer; insufficient data for precancerous oesophageal conditions at time of publication |
| [8304939](https://pubmed.ncbi.nlm.nih.gov/8304939/) | 1993 | Review | Basic Life Sci | Mechanistic review of nitrosation inhibition: ascorbic acid competitively reduces NOC formation in acidic conditions relevant to oesophageal and gastric carcinogenesis |
| [17953708](https://pubmed.ncbi.nlm.nih.gov/17953708/) | 2008 | Animal Study | Cancer Sci | ⚠️ Safety signal: combined ascorbic acid + sodium nitrite treatment enhanced oesophageal carcinogenesis in acid reflux model rats over 32 weeks via nitric oxide generation; clinically relevant caution for GORD patients |
| [12667416](https://pubmed.ncbi.nlm.nih.gov/12667416/) | 2003 | Review | Curr Oncol Rep | Dietary approaches to GI cancer prevention: ascorbic acid-rich foods consistently identified as protective in oesophageal cancer epidemiology; clinical trial evidence growing |

---

## South Africa Market Information

Ascorbic acid (DB00126) currently holds **no SAHPRA pharmaceutical registrations** and is classified as **not marketed** as a regulated medicine in South Africa.

While ascorbic acid preparations may be available as unregulated food supplements or nutritional products, they do not hold pharmaceutical registration status and are not subject to SAHPRA quality, safety, and efficacy oversight in that capacity. Any formal therapeutic application in South Africa would require registration through the standard SAHPRA new medicine application pathway.

**Note on Essential Medicines List status:** Ascorbic acid is included on the **WHO Essential Medicines List** for the treatment of scurvy. Review of potential inclusion on the South African National Essential Medicines List (NEML) for this indication — as the first regulatory step — is recommended as part of any market access strategy.

---

## Safety Considerations

**Key Warnings (indication-specific):**
- **Dual mechanistic risk in GORD patients:** Combined exposure to ascorbic acid and dietary sodium nitrite under acidic reflux conditions may paradoxically enhance oesophageal carcinogenesis through nitric oxide generation, as demonstrated in rat models (PMID 17953708). The clinical significance in patients with pre-existing gastro-oesophageal reflux disease is unresolved and requires evaluation before any therapeutic trial.
- **Direct oesophageal mucosal injury from oral formulations:** Ascorbic acid tablets lodged in the oesophagus have caused localised proximal oesophagitis (PMID 131047) and drug-induced oesophageal strictures requiring surgical intervention (PMID 3606243). Patients must take solid oral formulations with at least 200 mL of water and remain upright for at least 30 minutes post-dose.
- **Adverse effects on oesophageal function:** Ascorbic acid is listed among pharmacological agents with documented adverse effects on oesophageal structure and function (PMID 20227023).

For comprehensive safety information, please refer to the SAHPRA-approved Professional Information (PI) of any registered ascorbic acid product. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Population-level meta-analyses and prospective cohort data demonstrate a consistent inverse association between dietary vitamin C intake and oesophageal cancer risk, and the inhibition of N-nitroso compound formation provides a credible biological mechanism. However, current evidence is Level 3 (observational studies and mechanistic/in vitro data), no controlled clinical trial has confirmed a therapeutic benefit of ascorbic acid supplementation specifically for oesophageal disease, and an unresolved pro-carcinogenic safety signal under gastro-oesophageal reflux conditions precludes a "proceed" recommendation without further safety characterisation.

**To proceed, the following is needed:**
- A prospective controlled trial evaluating ascorbic acid supplementation in ESCC chemoprevention — particularly relevant to South Africa given the high incidence of ESCC in the southern African oesophageal cancer belt
- Mechanistic studies resolving the dual role of ascorbic acid in the presence of dietary nitrite under acid reflux conditions, to define safe patient populations
- Pharmacokinetic data establishing plasma and oesophageal mucosal concentrations achievable with feasible oral or intravenous dosing regimens
- Formal SAHPRA pharmaceutical registration of ascorbic acid (initial pathway: scurvy/vitamin C deficiency indication via NEML inclusion)
- MOA data retrieval from DrugBank API (currently a data gap) to complete mechanistic profiling
- Development of a safety monitoring plan for patients with GORD, Barrett's oesophagus, or high dietary nitrite intake

---

*Report generated: 2026-04-04 | Candidate ID: TW-DB00126-multi | Data cut-off: 2026-04-04 | For research purposes only — this report does not constitute medical advice. Drug repurposing candidates require clinical validation before application. YMYL disclaimer: all findings are preliminary research outputs and must not be used to guide clinical treatment decisions without further validation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

