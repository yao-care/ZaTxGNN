---
layout: default
title: Ciprofloxacin
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
---

# Ciprofloxacin
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

# Ciprofloxacin: From Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

Ciprofloxacin is a broad-spectrum fluoroquinolone antibiotic used to treat a wide range of bacterial infections, including urinary tract infections, respiratory tract infections, and gastrointestinal infections.
The TxGNN model predicts it may be effective for **Diffuse Scleroderma** (systemic sclerosis), based on its antifibrotic activity in dermal fibroblasts and its established role in managing small intestinal bacterial overgrowth (SIBO) — a common complication of this disease.
Currently, **no registered clinical trials** and **2 publications** directly support this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum bacterial infections (fluoroquinolone antibiotic; SAHPRA registration data unavailable in current dataset) |
| Predicted New Indication | Diffuse Scleroderma (Systemic Sclerosis) |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed (not found in SAHPRA database; data collection may be incomplete) |
| Number of SAHPRA Registrations | 0 (may reflect data collection gap) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ciprofloxacin belongs to the fluoroquinolone class of antibiotics. Its primary mechanism of action is inhibition of bacterial DNA gyrase (GyrA/GyrB) and Topoisomerase IV, which blocks bacterial DNA replication and repair. Importantly, ciprofloxacin also exerts effects on mammalian fibroblasts: it suppresses TGF-β–driven collagen synthesis (Collagen Types I and III) and downregulates inhibitors of matrix metalloproteinases (MMPs). This antifibrotic activity maps directly onto the core pathological mechanism in scleroderma — unchecked fibroblast activation and excessive extracellular matrix deposition.

Diffuse scleroderma (diffuse cutaneous systemic sclerosis) is an autoimmune connective tissue disease characterised by microvascular injury, immune dysregulation, and progressive fibrosis of the skin and internal organs, principally driven by aberrant TGF-β signalling. The alignment between ciprofloxacin's documented cellular effects and the dominant fibrotic pathway in scleroderma provides a biologically credible rationale for the TxGNN prediction.

A second, independent mechanistic pathway further strengthens the case: patients with systemic sclerosis frequently develop small intestinal bacterial overgrowth (SIBO) as a consequence of gastrointestinal dysmotility. Ciprofloxacin can reduce intestinal bacterial load, lower systemic endotoxin exposure, and thereby indirectly attenuate ongoing immune activation that contributes to disease progression. A 1995 observational study in British Journal of Rheumatology confirmed the clinical relevance of this pathway, documenting antibiotic treatment outcomes in 24 systemic sclerosis patients presenting with malabsorption symptoms.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Pilot RCT | The Journal of Dermatology | Controlled, double-blind randomised trial evaluating oral ciprofloxacin as an antifibrotic agent in patients with scleroderma; assessed whether ciprofloxacin reduces skin fibrosis severity. Pilot-scale; results provide early-stage interventional signal. |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Observational/Diagnostic Study | British Journal of Rheumatology | Twenty-four systemic sclerosis patients with malabsorption symptoms (chronic diarrhoea and weight loss) were assessed for SIBO via jejunal aspiration; six had diffuse disease. Antibiotic treatment outcomes reported, supporting the role of antibiotics including ciprofloxacin in managing SIBO-related gastrointestinal complications in systemic sclerosis. |

---

## South Africa Market Information

No SAHPRA registrations were identified in the current dataset (market status: not marketed; 0 licences retrieved). This likely reflects a data collection gap rather than true non-availability — ciprofloxacin is a WHO Essential Medicine and is expected to be registered and widely accessible in South Africa, including on the National Essential Medicines List (NEML).

Healthcare professionals should verify the current registration status directly on the SAHPRA website ([www.sahpra.org.za](https://www.sahpra.org.za)) and consult the current NEML for approved indications and formulations.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for complete safety information. Report adverse drug reactions to SAHPRA.

> **Important clinical note for this repurposing context:** Ciprofloxacin carries black box warnings (US FDA) for tendinitis and tendon rupture, peripheral neuropathy, and central nervous system effects. These risks are particularly relevant when considering off-label use in systemic sclerosis patients, as peripheral neuropathy can also be a manifestation of the underlying disease — creating potential diagnostic confusion and compounding risk. A careful benefit-risk assessment is essential before use in this population.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base for ciprofloxacin in diffuse scleroderma currently consists of one small pilot randomised trial (2010) and one observational study (1995), with no active registered clinical trials — placing this at an L4 evidence level, insufficient to support clinical use beyond investigational settings. The mechanistic rationale is credible but requires prospective validation.

**To proceed, the following is needed:**
- A well-powered Phase 2 randomised controlled trial evaluating oral ciprofloxacin vs placebo in diffuse scleroderma, with validated skin fibrosis endpoints (e.g., modified Rodnan Skin Score) and functional outcomes
- Retrieval of complete mechanism of action (MOA) data from DrugBank to fully characterise the antifibrotic signalling pathway and support mechanistic dossier development
- Safety profiling specific to scleroderma patients, with particular attention to tendinopathy and peripheral neuropathy risks given both the drug's black box warnings and disease-related neuropathy
- Confirmation of current SAHPRA registration status, approved indications, and inclusion on the South African National Essential Medicines List (NEML)
- Review of the SAHPRA-approved Professional Information (PI) for complete contraindications, warnings, and drug interaction data before any clinical protocol is designed

> **Note on other predicted indications:** Among all 10 TxGNN-predicted indications in this Evidence Pack, **Septicemic Plague** (Rank 10, TxGNN score 99.64%) carries substantially stronger evidence — an L2 rating supported by a completed Phase 2 randomised non-inferiority trial (NCT01243437) and FDA approval under the Animal Efficacy Rule — with a recommendation of **Proceed with Guardrails**. A dedicated report for this indication is recommended as a priority.

---

*This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. This document should be read in conjunction with the SAHPRA-approved Professional Information for ciprofloxacin.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

