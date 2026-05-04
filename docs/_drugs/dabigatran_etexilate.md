---
layout: default
title: Dabigatran Etexilate
parent: 僅模型預測 (L5)
nav_order: 157
evidence_level: L5
indication_count: 10
---

# Dabigatran Etexilate
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

# Dabigatran Etexilate: From Anticoagulation to Sclerosing Cholangitis

## One-Sentence Summary

Dabigatran etexilate is a direct oral anticoagulant (DOAC), widely used internationally for stroke prevention in non-valvular atrial fibrillation and treatment/prevention of venous thromboembolism. The TxGNN model predicts it may be effective for **Sclerosing Cholangitis**, but with **0 clinical trials** and only **1 tangentially related publication**, this prediction currently lacks meaningful supporting evidence. Among all 10 predicted indications, **rheumatoid arthritis** (rank 9) is the only candidate with direct preclinical support.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anticoagulation (stroke prevention in non-valvular AF; treatment/prevention of DVT and PE; VTE prophylaxis post-orthopaedic surgery) — *no SAHPRA registration data available* |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 (Model prediction only, no actual studies) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Dabigatran etexilate is a prodrug that is converted to dabigatran, a potent, competitive, reversible direct thrombin (Factor IIa) inhibitor. By binding to the active site of thrombin, it prevents the conversion of fibrinogen to fibrin and inhibits thrombin-mediated platelet activation. Internationally, it is marketed as Pradaxa® (Boehringer Ingelheim) and is registered in numerous countries for anticoagulation indications.

Sclerosing cholangitis is a chronic cholestatic liver disease characterised by inflammation and fibrosis of the bile ducts. There is emerging basic science interest in the role of the coagulation cascade in hepatic fibrosis — thrombin can activate protease-activated receptor-1 (PAR-1), which may promote fibrogenic pathways in stellate cells. Theoretically, inhibiting thrombin could attenuate fibrosis progression. However, this mechanistic link remains speculative, and no direct evidence supports the use of dabigatran in sclerosing cholangitis. The single retrieved publication (PMID 36906733) concerns cilofexor (an FXR agonist), not dabigatran, and was retrieved only because sclerosing cholangitis appeared as a background disease context.

It is worth noting that among the 10 TxGNN-predicted indications, **rheumatoid arthritis** (rank 9, score 98.71%) is the only candidate with direct preclinical evidence: a 2022 animal study (PMID 36142208) demonstrated that dabigatran ameliorated CFA-induced arthritis in rats via modulation of the kallikrein-kinin system. This represents the only mechanistically supported prediction in this evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for dabigatran in sclerosing cholangitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36906733](https://pubmed.ncbi.nlm.nih.gov/36906733/) | 2023 | DDI/Pharmacokinetics | Clinical Pharmacokinetics | Evaluated CYP450 and transporter-mediated DDI potential for **cilofexor** (FXR agonist) in development for NASH and primary sclerosing cholangitis. Not a study of dabigatran; retrieved due to disease keyword overlap only. |

> **Note:** The sole retrieved publication does not evaluate dabigatran for sclerosing cholangitis. It concerns a different drug (cilofexor) and was captured only because sclerosing cholangitis appeared in the search context.

---

## South Africa Market Information

No SAHPRA registrations were identified for dabigatran etexilate in the provided dataset.

> **Note:** Dabigatran (Pradaxa®) is registered and marketed in many countries worldwide. The absence of SAHPRA registration data in this evidence pack may reflect a data gap rather than true non-availability. Healthcare professionals should verify current registration status directly with SAHPRA or the Boehringer Ingelheim South Africa office.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> **General safety context (from international labelling):** Dabigatran carries a significant bleeding risk, has no routine coagulation monitoring, and has a specific reversal agent (idarucizumab / Praxbind®). It is primarily renally eliminated (~80%), and dose adjustment or avoidance is required in renal impairment. Co-administration with P-glycoprotein inhibitors (e.g. ketoconazole, dronedarone, cyclosporine) may significantly increase dabigatran exposure. These safety considerations would be critical for any repurposing investigation.

---

## Summary of All Predicted Indications

Given that none of the top-ranked predictions have strong clinical evidence, the following summary provides context across all 10 TxGNN predictions:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Key Note |
|------|---------------------|-------------|----------------|----------------|----------|
| 1 | Sclerosing cholangitis | 99.82% | L5 | Hold | No relevant evidence |
| 2 | Obsolete familial combined hyperlipidemia | 99.63% | L5 | Hold | Obsolete disease term; no mechanistic link |
| 3 | Hypoalphalipoproteinemia | 99.57% | L5 | Hold | No mechanistic link to thrombin inhibition |
| 4 | Homozygous familial hypercholesterolemia | 99.49% | L5 | Hold | No mechanistic link; LDL receptor pathway |
| 5 | Primary release disorder of platelets | 99.06% | L4 | Hold | Mechanistic direction contradictory (would worsen bleeding) |
| 6 | Glanzmann thrombasthenia | 98.90% | L4 | Hold | Anticoagulant use would increase bleeding risk |
| 7 | Gout | 98.79% | L5 | Hold | Literature only reflects co-morbidity management |
| 8 | Pseudo-von Willebrand disease | 98.78% | L5 | Hold | Contradictory mechanism; would worsen bleeding |
| 9 | **Rheumatoid arthritis** | **98.71%** | **L4** | **Research Question** | **Only indication with direct preclinical support (animal model)** |
| 10 | HIV infectious disease | 98.70% | L5 | Hold | All evidence relates to DDI studies, not treatment |

---

## Highlight: Rheumatoid Arthritis (Rank 9) — Most Promising Candidate

Given that rheumatoid arthritis is the only predicted indication with mechanistic and preclinical support, the following additional detail is provided:

### Preclinical Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36142208](https://pubmed.ncbi.nlm.nih.gov/36142208/) | 2022 | Preclinical (Animal Model) | Int J Mol Sci | Dabigatran ameliorated CFA-induced rheumatoid arthritis in rats via modulation of the kallikrein-kinin system. Demonstrated anti-inflammatory effects including reduced joint swelling, inflammation, and dysfunction. |
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Review of lower extremity VTE diagnosis and treatment; provides context for anticoagulation in inflammatory conditions. |
| [27457374](https://pubmed.ncbi.nlm.nih.gov/27457374/) | 2016 | Case Report/DDI | Eur J Clin Pharmacol | Tocilizumab and mesenteric arterial thrombosis: drug-drug interaction with anticoagulants including dabigatran via CYP450/P-gp pathways. |

### Mechanistic Rationale

Thrombin activates protease-activated receptors (PAR-1 and PAR-4), which trigger pro-inflammatory signalling pathways (NF-κB, MAPK) involved in synovial inflammation and angiogenesis in RA. The kallikrein-kinin system (KKS) plays a significant role in RA inflammation, with bradykinin promoting vascular permeability and pain. The 2022 preclinical study directly demonstrated that dabigatran, by inhibiting thrombin, modulates the KKS and exerts anti-inflammatory effects in an established animal model of RA. This represents a plausible and testable mechanistic hypothesis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (sclerosing cholangitis) has no supporting clinical or preclinical evidence, and the mechanistic link between thrombin inhibition and biliary fibrosis remains entirely theoretical. The majority of the remaining predicted indications involve lipid disorders or bleeding disorders where dabigatran has no mechanistic relevance or could worsen the clinical picture. The drug is also not currently registered with SAHPRA per the available data.

**Exception — Rheumatoid Arthritis (recommend: Research Question):**
This is the only prediction warranting further scientific investigation, supported by a published preclinical animal study demonstrating efficacy via kallikrein-kinin system modulation.

**To proceed, the following is needed:**
- Confirmation of SAHPRA registration status for dabigatran etexilate (Pradaxa®)
- Detailed mechanism of action data from DrugBank (currently a data gap)
- SAHPRA-approved Professional Information (PI) for safety, warnings, and contraindications
- For the RA repurposing hypothesis specifically:
  - Replication of the preclinical findings in additional animal models
  - Pharmacokinetic modelling to determine whether anti-inflammatory doses are achievable at safe anticoagulant exposure levels
  - Systematic review of thrombin–PAR-1–inflammation axis in RA
  - Consultation with rheumatology and haematology specialists regarding bleeding risk–benefit in RA populations

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All findings should be interpreted in the context of the available evidence and local regulatory requirements.*

*Report generated: 2026-04-05 | Evidence Pack version: v4 | Data cutoff: 2026-04-05*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

