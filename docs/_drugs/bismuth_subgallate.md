---
layout: default
title: Bismuth Subgallate
parent: Model Prediction Only (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Bismuth Subgallate: predicted new indication Heparin cofactor 2 deficiency (evidence level L5). Approved use: Not stated"
monitor_inn: "Bismuth subgallate"
predicted_indications: ["heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "rheumatoid arthritis", "factor 5 excess with spontaneous thrombosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "thrombophilia", "brachydactyly-syndactyly syndrome", "gout", "gastroduodenitis", "peptic ulcer disease"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Bismuth Subgallate: From an Unspecified Local Indication to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Bismuth subgallate is a locally acting bismuth salt with astringent and deodorizing properties. It is registered in South Africa as a suppository, but the data compiled for this report do not state an approved indication.
The TxGNN model's top-ranked prediction is **heparin cofactor 2 deficiency**, but **no clinical trials and no publications** support it, and no plausible mechanism has been identified.
The most credible prediction in the list is **peptic ulcer disease** (rank 10), and even that rests only on **2 indirect publications** about bismuth compounds in general.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated (the SAHPRA registration record contains no approved indication text) |
| Predicted New Indication | Heparin cofactor 2 deficiency (top-ranked prediction) |
| TxGNN Prediction Score | 98.16% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Bismuth subgallate is a bismuth salt used as an astringent and deodorizing agent, and it is registered locally as a suppository. Its original indication could not be confirmed from the registration record.

**For the top-ranked prediction (heparin cofactor 2 deficiency), the prediction is not supported.** There is no known interaction between bismuth subgallate and the heparin cofactor II / thrombin inhibition pathway. The high score appears to be an artefact of the knowledge graph, probably from proximity to coagulation-related genes and pathways. The same applies to the other coagulation-related predictions (antithrombin deficiency type 2, factor 5 excess with spontaneous thrombosis, thrombophilia). A rare congenital deficiency is not expected to respond to a locally acting astringent.

**Other predictions without support:** rheumatoid arthritis, gout, and the ultra-rare developmental syndromes (colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome) have no documented mechanistic link, trials or literature. Bismuth subgallate has limited systemic absorption, and gold-salt use in rheumatoid arthritis should not be extrapolated to it.

**The only biologically plausible predictions are gastrointestinal:**
- **Gastroduodenitis** (rank 9, score 93.46%): bismuth compounds have mucosal protective and astringent actions and antimicrobial activity against *H. pylori*. This is class-level reasoning and no direct data exist for bismuth subgallate.
- **Peptic ulcer disease** (rank 10, score 92.53%): bismuth compounds have an established role through mucosal coating, cytoprotection and anti-*H. pylori* activity. Bismuth subcitrate and subsalicylate, not subgallate, are the established agents in *H. pylori* regimens.

## Clinical Trial Evidence

Currently no related clinical trials registered, for the top-ranked prediction or for any of the ten predictions.

## Literature Evidence

No literature was found for the top-ranked prediction (heparin cofactor 2 deficiency). The only publications in the data relate to the rank 10 prediction, **peptic ulcer disease**:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2199292](https://pubmed.ncbi.nlm.nih.gov/2199292/) | 1990 | Review | Gastroenterology | Bismuth therapy showed efficacy in peptic ulcer disease and diarrhoea. In peptic ulcer it was as effective as H2-receptor antagonists, cheaper, and had a lower relapse rate. It suppresses *H. pylori* without eliminating it, and is combined with antibiotics for elimination. |
| [8280948](https://pubmed.ncbi.nlm.nih.gov/8280948/) | 1993 | In vitro study | Zentralblatt fur Bakteriologie | Anti-ulcer therapeutics inhibited *H. pylori* receptor binding in vitro. Bismuth salts have potent antimicrobial activity. Whether bismuth subgallate itself was tested is unverified. |

Both publications are old and address bismuth compounds in general, so they do not establish efficacy of bismuth subgallate in patients.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| E512 | Anugesic | Suppository | Not stated in the data compiled |

Essential Medicines List (EML) status could not be determined from the data compiled.

## Safety Considerations

- **Drug Interactions:** 9 interactions of Moderate severity were identified:
  - **Tetracycline-class antibiotics:** doxycycline, tetracycline, minocycline, demeclocycline, oxytetracycline
  - **Opioids:** morphine, opium, codeine, hydrocodone
- **Coagulation:** any pro- or anticoagulant effect of bismuth subgallate is undocumented. This is a safety concern, not a benefit, if coagulation disorders were pursued.

Warnings and contraindications from the label are not available. Please refer to the SAHPRA-approved Professional Information (PI) for them. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (heparin cofactor 2 deficiency) has no trials, no literature and no plausible mechanism, and appears to be a knowledge-graph artefact. Evidence level is L5. The gastrointestinal predictions (gastroduodenitis and peptic ulcer disease, L4) are plausible but rest on class-level and in vitro evidence only, and are best treated as research questions.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (PI) for Anugesic, to confirm the approved indication, warnings and contraindications
- Mechanism of action data from DrugBank
- A bismuth subgallate-specific literature review, including whether it was tested in PMID 8280948
- Clinical data, if any exist, for gastroduodenitis and peptic ulcer disease, before any clinical positioning
- Route compatibility assessment, since the only local product is a suppository, which is not an obvious fit for gastric conditions
- No further work on the coagulation, rheumatological, gout or congenital malformation predictions unless new mechanistic evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

