---
layout: default
title: Methionine
parent: 僅模型預測 (L5)
nav_order: 309
evidence_level: L5
indication_count: 10
---

# Methionine
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

# Methionine: From No Established Indication to Acne (Disease)

## One-Sentence Summary

Methionine is an essential sulfur-containing amino acid; no original approved indication is on record and the drug is **not currently registered or marketed in South Africa**. The TxGNN model predicts it may be effective for **Acne (Disease)**, with a very high prediction score (**99.9996%**), but only **4 publications** and **no clinical trials** currently exist to support this direction — and on closer reading, none of the literature actually demonstrates a therapeutic link between methionine and acne.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — no SAHPRA registration or original indication data on record |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.9996% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and there is no on-record original indication for methionine in South Africa. Based on general pharmacological knowledge, methionine is an essential sulfur-containing amino acid and metabolic precursor to cysteine, glutathione, and S-adenosylmethionine (SAMe) via the transsulfuration/methylation pathways — roles that are nutritional and metabolic rather than tied to a specific approved disease indication.

The predicted association with acne could not be substantiated by the retrieved literature. The four identified articles discuss methionine's metabolic byproducts (elevated homocysteine during isotretinoin therapy, MTHFR mutation presenting with neonatal acne as an incidental skin finding) and neutrophil/chemotactic function in unrelated inflammatory skin conditions (Sweet's syndrome, various dermatoses) — none evaluate methionine as a treatment for acne itself.

The TxGNN score of 99.9996% therefore most likely reflects indirect graph connectivity — shared metabolic or inflammatory pathway nodes in the knowledge graph — rather than a substantiated causal or therapeutic mechanism. This candidate should be regarded as a pure model-generated hypothesis at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Cohort (observational) | International Journal of Dermatology | Isotretinoin therapy for cystic acne was associated with elevated plasma homocysteine (a methionine metabolite), reported as a drug side-effect finding rather than evidence of methionine's own therapeutic effect on acne |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Case report | BMJ Case Reports | Neonate with MTHFR mutation (affecting methionine/homocysteine metabolism) presented with encephalopathy and neonatal acne among other dysmorphic features; acne was an incidental sign, not a treatment target |
| [3859500](https://pubmed.ncbi.nlm.nih.gov/3859500/) | 1985 | Case series | Journal of the American Academy of Dermatology | Neutrophil chemotactic activity studied in a patient with Sweet's syndrome and cystic acne; no methionine intervention evaluated |
| [3161955](https://pubmed.ncbi.nlm.nih.gov/3161955/) | 1985 | Clinical observational | Journal of Investigative Dermatology | Neutrophil C5a-response function assessed across several inflammatory skin conditions including acne conglobata; methionine not studied as a treatment |

---

## South Africa Market Information

Methionine currently has **no SAHPRA product registrations** (total registrations: 0). Market status is recorded as **Not marketed**. No dosage forms, brand names, or approved indication text are available for South Africa at this time.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: key warnings, contraindications, and drug-interaction data for methionine are currently unavailable — this is flagged as a Blocking data gap (DG001) in the evidence pack and must be resolved before any safety assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 — this is a model prediction only, with no clinical trials and no literature directly testing methionine's therapeutic effect on acne.
- The four retrieved publications describe methionine-related metabolites and unrelated inflammatory skin conditions, not a treatment relationship; the high TxGNN score appears to reflect indirect knowledge-graph connectivity rather than substantiated pharmacology.
- Methionine is not currently marketed or registered in South Africa (0 SAHPRA registrations), and mechanism-of-action and safety label data remain unavailable (data gaps DG001–Blocking, DG002–High).

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) — warnings, contraindications, and safety data (currently a Blocking data gap)
- Verified mechanism of action (MOA) data (currently a High-severity data gap)
- Dedicated acne-specific studies (in vitro, animal, or clinical) that directly test methionine as an intervention, rather than incidental metabolite observations
- Note: within this same evidence pack, other candidate indications for methionine — notably **diabetic cataract** (Evidence Level L3, "Research Question" stage) and **cortical cataract** (L4) — show comparatively stronger mechanistic and observational support (methionine/glutathione precursor role in lens oxidative stress) and may warrant separate, prioritized evaluation ahead of the acne hypothesis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

