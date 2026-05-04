---
layout: default
title: Dexchlorpheniramine Maleate
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 10
---

# Dexchlorpheniramine Maleate
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

# Dexchlorpheniramine Maleate: From Allergic Conditions to Acute Intermittent Porphyria

## One-Sentence Summary

Dexchlorpheniramine maleate is a first-generation H1 antihistamine, widely used internationally for the symptomatic relief of allergic conditions such as allergic rhinitis and urticaria. The TxGNN model predicts it may be effective for **Acute Intermittent Porphyria**, however there are **no clinical trials** and **no publications** supporting this specific direction, and mechanistic analysis suggests the prediction lacks biological plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, urticaria, and other histamine-mediated allergic conditions |
| Predicted New Indication | Acute Intermittent Porphyria |
| TxGNN Prediction Score | 99.12% |
| Evidence Level | L5 (Model prediction only, no actual studies) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known pharmacology, dexchlorpheniramine is the dextrorotatory isomer of chlorpheniramine, a first-generation alkylamine-class H1 receptor antagonist. It competitively blocks histamine at H1 receptors, inhibiting the vasodilation, increased vascular permeability, and pruritus that characterise histamine-mediated allergic responses. It also possesses mild anticholinergic and sedative properties due to its ability to cross the blood-brain barrier.

Acute intermittent porphyria (AIP) is an inherited metabolic disorder caused by deficiency of porphobilinogen deaminase (PBGD/HMBS), leading to accumulation of porphyrin precursors (ALA and PBG). The disease manifests with acute neurovisceral attacks including severe abdominal pain, neuropsychiatric symptoms, and autonomic dysfunction. There is no identifiable mechanistic link between H1 receptor antagonism and the haem biosynthesis pathway defect underlying AIP.

Critically, some antihistamines have been flagged in porphyria literature as potential triggers of acute attacks via CYP450 enzyme induction, which can upregulate ALA synthase activity. This raises a safety concern rather than a therapeutic rationale. The TxGNN prediction score is high (99.12%), but the model rank (4,402) and the complete absence of supporting evidence suggest this is a spurious prediction. Without any mechanistic, preclinical, or clinical basis, this prediction should not be pursued.

## Clinical Trial Evidence

Currently no related clinical trials registered on ClinicalTrials.gov, SANCTR (South African National Clinical Trials Register), PACTR (Pan African Clinical Trials Registry), or ICTRP for dexchlorpheniramine in acute intermittent porphyria.

## Literature Evidence

Currently no related literature available for dexchlorpheniramine in acute intermittent porphyria.

## South Africa Market Information

Dexchlorpheniramine maleate currently has no SAHPRA registrations. The drug is not marketed in South Africa. It is not listed on the South African Essential Medicines List (EML). Any use would require importation under Section 21 of the Medicines and Related Substances Act (Act 101 of 1965).

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information, noting that no PI is currently available for this product in South Africa as it is not registered. International product information (e.g., from the TGA, FDA, or EMA) should be consulted. Report adverse drug reactions to SAHPRA.

**Additional safety note for the predicted indication:** Some antihistamines are listed as potentially porphyrinogenic agents. Healthcare professionals should exercise extreme caution and consult specialist porphyria references (e.g., the European Porphyria Network drug safety database) before considering any use of dexchlorpheniramine in patients with porphyria.

## Other Predicted Indications Summary

The TxGNN model generated 10 predicted indications for dexchlorpheniramine. The table below provides a summary assessment:

| Rank | Predicted Indication | Score | Evidence Level | Recommendation | Mechanistic Plausibility |
|------|---------------------|-------|---------------|----------------|------------------------|
| 1 | Acute intermittent porphyria | 99.12% | L5 | Hold | None; potential harm |
| 2 | Nephrogenic syndrome of inappropriate antidiuresis | 98.36% | L5 | Hold | None |
| 3 | Porphyria | 97.69% | L5 | Hold | None; potential harm |
| 4 | Schizophrenia | 97.17% | L5 | Hold | Negative (impairs cognition) |
| 5 | Polymicrogyria with cerebellar hypoplasia | 97.13% | L5 | Hold | None (structural/genetic) |
| 6 | Allergic urticaria | 96.96% | L3 | Proceed with Guardrails | Direct (known indication) |
| 7 | Syndromic myopia | 96.83% | L5 | Hold | None |
| 8 | Atypical glycine encephalopathy | 96.75% | L5 | Hold | None |
| 9 | Myopia 26, X-linked, female-limited | 96.71% | L5 | Hold | None |
| 10 | Myopia X-linked | 96.61% | L5 | Hold | None |

**Notable finding:** The rank 6 prediction (allergic urticaria) is a known and well-established indication for dexchlorpheniramine, with **6 publications** supporting its use. This is not a true repurposing candidate but rather validates the drug's existing therapeutic profile. Relevant literature for this known indication includes:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39265704](https://pubmed.ncbi.nlm.nih.gov/39265704/) | 2024 | Comparative PD study | Eur J Pharm Sci | Phase I trial comparing parenteral dexchlorpheniramine with bilastine in histamine-induced wheal and flare suppression |
| [29723372](https://pubmed.ncbi.nlm.nih.gov/29723372/) | 2018 | Pharmacodynamic study | An Bras Dermatol | Demonstrated wheal and flare suppression by major H1 antihistamines including dexchlorpheniramine |
| [19220286](https://pubmed.ncbi.nlm.nih.gov/19220286/) | 2009 | Experimental pharmacology | Br J Pharmacol | H1 receptor blockade predominantly impairs sensory processes in sensorimotor performance (relevant to schizophrenia prediction, rank 4) |
| [2523357](https://pubmed.ncbi.nlm.nih.gov/2523357/) | 1989 | In vitro study | Int Arch Allergy Immunol | Cetirizine inhibition of eosinophil chemotaxis; comparative context for first-generation antihistamines |

**Model bias observation:** The TxGNN model shows a systematic pattern of predicting myopia-related conditions (ranks 7, 9, 10) for this drug, likely representing model noise rather than genuine therapeutic signals, as H1 antihistamines have no known effect on ocular axial length or refractive development.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (acute intermittent porphyria) lacks any mechanistic plausibility, and H1 antihistamines may in fact be harmful in porphyria patients by potentially triggering acute attacks. Nine of the ten predictions have L5 evidence (model prediction only), and the one prediction with literature support (allergic urticaria) is already a known indication. The drug is also not registered in South Africa, adding a regulatory barrier.

**To proceed, the following would be needed:**
- Identification of a genuinely novel and mechanistically plausible indication (none identified in current predictions)
- Detailed mechanism of action data and CYP450 interaction profiling to assess porphyrinogenicity risk
- SAHPRA registration or Section 21 authorisation pathway assessment
- Safety data including Professional Information (PI) review from an established regulatory authority
- Consultation with a clinical pharmacologist specialising in porphyria before any consideration of predictions 1 and 3

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All predictions are generated by the TxGNN computational model and must be interpreted by qualified healthcare professionals.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

