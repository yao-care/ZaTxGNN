---
layout: default
title: Bismuth Subgallate
parent: Model Prediction Only (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
---

# Bismuth Subgallate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Bismuth Subgallate: From an Unrecorded Original Indication to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Bismuth subgallate is a bismuth salt marketed in South Africa as a suppository (Anugesic), but the available registration data does not state its approved indication.
The TxGNN model predicts it may be effective for **Heparin Cofactor 2 Deficiency**, with **0 clinical trials** and **0 publications** supporting this prediction. It rests on a computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available registration data |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 98.16% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Bismuth subgallate is a bismuth compound, and bismuth compounds as a class are mainly used in gastrointestinal conditions. Its original indication could not be confirmed from the registration data.

The link to heparin cofactor 2 deficiency is weak. Bismuth subgallate has no known role in serpin or coagulation-inhibitor pathways. The high score most likely reflects proximity in the knowledge graph, not a pharmacological rationale.

The same pattern appears in other top-ranked predictions, such as antithrombin deficiency type 2, factor 5 excess and thrombophilia. These form a correlated thrombosis cluster, and none has trial or literature support. Treat this prediction as a computational hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered. No entries were found in ClinicalTrials.gov or ICTRP, and no SANCTR or PACTR identifiers were available.

## Literature Evidence

Currently no related literature available for heparin cofactor 2 deficiency.

For context, the only predicted indication with any literature is **peptic ulcer disease** (rank 10, score 92.53%, L4). The publications below cover bismuth compounds as a class, not bismuth subgallate specifically.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2199292](https://pubmed.ncbi.nlm.nih.gov/2199292/) | 1990 | Review | Gastroenterology | Bismuth therapy in peptic ulcer disease and diarrhoea. In peptic ulcer it was reported as effective as H2-receptor antagonists, cheaper, with a lower relapse rate. In H. pylori disease it suppresses the organism and is used with antibiotics. |
| [1589712](https://pubmed.ncbi.nlm.nih.gov/1589712/) | 1992 | Pharmacokinetic study | Scand J Gastroenterol | Less than 0.1% of an oral dose of five bismuth compounds was absorbed. Basic bismuth gallate absorption was 0.038%, higher than salicylate, nitrate and aluminate salts. |
| [8280948](https://pubmed.ncbi.nlm.nih.gov/8280948/) | 1993 | In vitro study | Zentralbl Bakteriol | Therapeutics used for peptic ulcers, including bismuth remedies, inhibited H. pylori receptor binding in vitro. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| E512 (as recorded) | Anugesic | Suppository | Not stated in the available data |

Essential Medicines List (EML) status could not be determined from the available data.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

A drug-interaction query returned no records, which is not the same as no interactions. Systemic absorption of oral bismuth compounds appears very low (PMID 1589712), but this study covers oral use, not the suppository route.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for heparin cofactor 2 deficiency is prediction-only (L5), with no trials, no literature and no plausible mechanism. It should not be pursued clinically. Peptic ulcer disease is the only candidate with a coherent rationale (L4, "Research Question"), and gastroduodenitis is plausible by analogy, but both rely on indirect class-level evidence.

**To proceed, the following is needed:**
- The SAHPRA Professional Information for Anugesic, covering the approved indication, warnings and contraindications. This is a blocking gap for any safety screening.
- Mechanism of action data for bismuth subgallate, for example from DrugBank.
- Confirmation of the original indication, since the registration record has none.
- If the peptic ulcer or gastroduodenitis direction is pursued, evidence specific to bismuth subgallate and a check that a suppository route is compatible with an upper-GI indication.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

