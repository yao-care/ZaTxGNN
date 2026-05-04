---
layout: default
title: Chromium
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
---

# Chromium
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

# Chromium: From Essential Trace Mineral to Rheumatoid Arthritis

## One-Sentence Summary

Chromium (trivalent, Cr³⁺; DrugBank DB11136) is an essential trace element recognised for its role in insulin signalling and glucose metabolism, with no current registered therapeutic indication in South Africa.
The TxGNN model's highest-ranked musculoskeletal predictions (osteoarthritis, ranks 1–2) are assessed as knowledge-graph artefacts driven by cobalt-chromium implant safety literature — not genuine repurposing signals — while **Rheumatoid Arthritis** (rank 3, score 98.54%) is the only prediction supported by actual therapeutic evidence.
This indication is backed by **1 completed Phase 2/3 RCT** and **2 directly relevant publications**, placing it at Evidence Level L2.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None (essential trace element; no registered therapeutic use) |
| Predicted New Indication | Rheumatoid Arthritis *(rank 3 — see critical note below)* |
| TxGNN Prediction Score | 98.54% |
| Evidence Level | L2 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **⚠️ Critical note on TxGNN ranking:** The top two predictions — osteoarthritis (rank 1, 98.68%) and osteoarthritis susceptibility (rank 2, 98.54%) — are **knowledge-graph confounds**. Virtually all chromium + osteoarthritis literature in the training data originates from cobalt-chromium orthopaedic implant safety monitoring studies, representing a *harm signal* (metal ions leaching from failed implants) rather than a therapeutic signal. No trial has ever tested chromium supplementation as a treatment for osteoarthritis. Both are rated **L5 / Hold**. Rheumatoid arthritis is therefore featured as the clinically actionable focus of this report.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not currently available for Chromium (DB11136) in this evidence pack. Based on established nutritional biochemistry and RA-specific preclinical and clinical evidence, three mechanistically coherent pathways link trivalent Cr³⁺ to rheumatoid arthritis:

**Insulin receptor sensitisation via chromodulin.** Cr³⁺ binds the low-molecular-weight oligopeptide chromodulin, which amplifies insulin receptor tyrosine kinase activity following insulin binding. Rheumatoid arthritis is associated with systemic insulin resistance and impaired T-cell energy metabolism. Restoring insulin sensitivity may reduce pro-inflammatory immune cell activation, as T-cell function is tightly coupled to metabolic status.

**NF-κB suppression and cytokine reduction.** Animal model studies demonstrate that Cr³⁺ supplementation downregulates NF-κB signalling, reducing production of TNF-α, IL-1β, and IL-6 — the central drivers of synovial inflammation, cartilage degradation, and bone erosion in RA. The 2022 rat adjuvant-induced arthritis study (PMID 35829940) further documented upregulation of FOXP3 (a marker of immunosuppressive regulatory T-cells) and a decrease in synovial cathepsin G, suggesting modulation of adaptive immunity beyond simple cytokine suppression.

**Epidemiological deficiency signal.** Two independent cross-sectional studies documented significantly lower serum and tissue chromium concentrations in RA patients compared to healthy controls (PMID 1153978, PMID 3776595), raising the hypothesis that a relative chromium deficiency impairs immune regulation in RA. This parallels the established therapeutic rationale for trace element correction in other chronic inflammatory conditions. The convergence of a biological deficiency signal with mechanistic plausibility provides a coherent rationale for the 2022–2024 clinical trial programme.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT05545020](https://clinicaltrials.gov/study/NCT05545020) | Phase 2/3 | Completed | 60 | **Core direct trial.** "Trivalent Chromium as a Treatment for Rheumatoid Arthritis Patients" (Egypt, 2022–2024). The only RCT ever to directly evaluate Cr³⁺ supplementation in RA patients. Used baricitinib (JAK1/2 inhibitor, a standard DMARD) as the active comparator. Assessed efficacy and safety of Cr³⁺. Results published in *Inflammopharmacology* 2024 (PMID 39030450). Investigators concluded Cr³⁺ has anti-rheumatic potential with a potentially more favourable side-effect profile than baricitinib. |

No SANCTR (South African National Clinical Trials Register) or PACTR (Pan African Clinical Trials Registry) trials were identified for chromium in rheumatoid arthritis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39030450](https://pubmed.ncbi.nlm.nih.gov/39030450/) | 2024 | RCT | *Inflammopharmacology* | Phase 2/3 RCT: trivalent Cr³⁺ vs baricitinib in RA patients (n=60). First human trial of Cr³⁺ as an immune-modulator. Authors describe Cr³⁺ as a natural element with anti-inflammatory properties and fewer side effects than baricitinib, positioning it as a potential upcoming DMARD. Key publication for this repurposing direction. |
| [35829940](https://pubmed.ncbi.nlm.nih.gov/35829940/) | 2022 | Animal Study | *Inflammopharmacology* | Cr³⁺ supplementation in adjuvant-induced RA rat model vs prednisolone control. Demonstrated amelioration of arthritis severity through FOXP3 upregulation and reduced synovial cathepsin G expression. First animal model validation of therapeutic Cr³⁺ in RA; underpins the mechanistic rationale for NCT05545020. |
| [1153978](https://pubmed.ncbi.nlm.nih.gov/1153978/) | 1975 | Cross-sectional | *Scand J Rheumatology* | Blood calcium, magnesium, copper, zinc, lead, and chromium in RA patients vs healthy controls. Chromium concentrations were significantly different, providing the earliest epidemiological signal for a chromium deficiency state in RA. |
| [3776595](https://pubmed.ncbi.nlm.nih.gov/3776595/) | 1986 | Cross-sectional | *Acta Pharmacol Toxicol* | Chromium, nickel, and cadmium measured in blood and other biological fluids of RA patients vs healthy controls. Corroborates lower chromium status in RA across multiple biological compartments, strengthening the deficiency hypothesis. |

---

## South Africa Market Information

Chromium (DB11136) currently has **no SAHPRA registrations** and is **not marketed** as a pharmaceutical product in South Africa. It does not appear on the Essential Medicines List (EML) as a therapeutic agent.

Chromium-containing dietary supplements (e.g., chromium picolinate, chromium polynicotinate, chromium chloride) may be commercially available in South Africa as health products under the Foodstuffs, Cosmetics and Disinfectants Act, but are not approved for the treatment of rheumatoid arthritis and fall outside the scope of pharmaceutical regulation.

Any investigational or therapeutic use in RA would require:
- **SAHPRA Section 21 authorisation** for access to an unregistered medicine for a specific patient or clinical trial, or
- A formal **marketing authorisation application** for the specific therapeutic indication once sufficient evidence is available.

---

## Safety Considerations

Full safety data for therapeutic chromium use in RA is not available in this evidence pack. The following critical distinctions must be communicated to all prescribers and investigators:

**Valence state distinction is clinically essential:**
- **Trivalent chromium (Cr³⁺)**: The biologically active, nutritionally essential form used in dietary supplements and in NCT05545020. Generally considered safe at supplemental doses (typically 200–1,000 µg/day). Toxicological data from diabetes management trials suggest low acute toxicity at these doses.
- **Hexavalent chromium (Cr⁶⁺)**: A confirmed human carcinogen (IARC Group 1), genotoxic, nephrotoxic, and hepatotoxic. This is an entirely different chemical entity with a fundamentally different risk profile. The two must not be conflated in clinical documentation or patient communication.

**Clinical trial safety signal:** The 2024 RCT (PMID 39030450) reported that Cr³⁺ was associated with fewer adverse effects than baricitinib, but full adverse event data requires review of the complete publication before clinical use.

Please refer to the SAHPRA-approved Professional Information (PI) for any registered chromium-containing products. Report adverse drug reactions to SAHPRA via the MedSafety online reporting portal.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(Rheumatoid Arthritis indication only)*

**Rationale:**
A completed Phase 2/3 RCT (NCT05545020, n=60, published 2024) provides the first direct clinical evidence for trivalent Cr³⁺ supplementation in RA, with baricitinib as an active comparator. Combined with a mechanistically coherent preclinical dataset and a consistent epidemiological deficiency signal, this constitutes Level 2 evidence and justifies cautious further evaluation. However, the trial is single-centre and small (n=60), and independent replication is required before any practice change.

**To proceed, the following is needed:**

- **Full critical appraisal of PMID 39030450**: Review specific Cr³⁺ dose and salt form, primary endpoints, effect sizes, blinding methodology, adverse event profile, and any limitations noted by peer reviewers
- **Dose and formulation specification**: Confirm the exact Cr³⁺ compound, daily dose (µg/day), administration route, and treatment duration used in the efficacy trial
- **Safety and monitoring protocol**: Establish chromium serum level monitoring thresholds, renal function surveillance plan, and genotoxicity assessment framework for any South African trial or Section 21 use
- **Independent replication**: A second Phase 3 RCT at an independent site with larger sample size (≥200 patients) and South African patient representation before clinical adoption
- **SAHPRA regulatory pathway planning**: Engage with SAHPRA early to determine requirements for Section 21 access or a formal indication-specific marketing authorisation
- **MOA data retrieval**: Obtain the full DrugBank mechanism of action entry for Chromium (DB11136) to complete the regulatory rationale dossier

> **Recommendation for all other TxGNN predictions (ranks 1, 2, 4–10): Hold.**
> Osteoarthritis (rank 1) and OA susceptibility (rank 2) are knowledge-graph confounds from implant safety literature. Gout (rank 4) has no mechanistic link to chromium biochemistry and no supporting trials. Ranks 5–10 (rare skeletal dysplasias) involve genetic pathways entirely unrelated to chromium's known biology. None of these warrant further investigation at this time.

---

*⚠️ Disclaimer: This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require independent clinical validation before therapeutic application. All clinical decisions should comply with current SAHPRA-approved prescribing information and applicable South African clinical guidelines.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

