---
layout: default
title: Chromium
parent: Model Prediction Only (L5)
nav_order: 117
evidence_level: L5
indication_count: 10
---

# Chromium
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

# Chromium: From Parenteral Nutrition Component to Osteoarthritis

## One-Sentence Summary

Chromium is registered in South Africa mainly as a component of parenteral nutrition and infusion products. The registration data give no stated therapeutic indication. The TxGNN model predicts it may be relevant to **osteoarthritis**, and **48 registered trials** and **20 publications** were retrieved for this prediction. However, none tests chromium as a treatment for osteoarthritis. They almost all concern chromium ions released from metal joint implants, where chromium is a marker of exposure and harm, not a therapy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data (all approved-indication fields are empty); products are infusion and TPN formulations |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.68% |
| Evidence Level | L5 (model prediction only, no therapeutic studies) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Chromium is a trace element that is supplied in parenteral nutrition, but no established mechanism links it to osteoarthritis.

The high score (0.987) most likely reflects knowledge-graph associations. Chromium appears in literature on cobalt-chromium joint implants used to treat osteoarthritis, so it sits close to the disease in the graph. In those studies chromium is released as ions from the implant and is monitored as a sign of wear and toxicity. It is not given as a treatment. The prediction should therefore be read as an association artefact, not a therapeutic hypothesis.

A different signal appears for **rheumatoid arthritis**, a separate predicted indication for this drug. A completed Phase 2/3 randomized trial of trivalent chromium (NCT05545020, n=60, compared with baricitinib; published as PMID 39030450) and a supporting rat-model study exist. This is the only direct therapeutic evidence in the dataset, and it does not transfer to osteoarthritis. Osteoarthritis is mainly a degenerative disease, and the trial results were not available for review.

## Clinical Trial Evidence

Of the 48 trials retrieved, none studies chromium as an osteoarthritis treatment. All are implant or device studies, most measuring chromium and cobalt ion release. The ten most relevant are listed below. No SANCTR or PACTR registrations were identified in the data. The ICTRP list is empty.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01493141](https://clinicaltrials.gov/study/NCT01493141) | N/A | Completed | 46 | Systemic effects of chronic metal ion exposure from metal-on-metal hip resurfacing (toxicity study) |
| [NCT00962351](https://clinicaltrials.gov/study/NCT00962351) | N/A | Completed | 120 | Randomized comparison of blood and urine cobalt, chromium and titanium levels for metal-on-metal vs metal-on-polyethylene hips |
| [NCT04585022](https://clinicaltrials.gov/study/NCT04585022) | N/A | Terminated | 75 | Randomized comparison of whole blood chromium and cobalt in two metal-on-metal hip types, 5-year follow-up |
| [NCT00757354](https://clinicaltrials.gov/study/NCT00757354) | N/A | Completed | 77 | Metal ion release from metal-on-metal cementless hip arthroplasty |
| [NCT03047564](https://clinicaltrials.gov/study/NCT03047564) | N/A | Completed | 120 | Metal ion levels in coated vs uncoated total knee arthroplasty |
| [NCT00862511](https://clinicaltrials.gov/study/NCT00862511) | N/A | Completed | 120 | Serum chromium, cobalt, molybdenum and nickel after coated vs uncoated knee prostheses |
| [NCT01437124](https://clinicaltrials.gov/study/NCT01437124) | N/A | Completed | 83 | Metal ion levels and chromosome abnormalities after ceramic-on-metal hip arthroplasty |
| [NCT00911599](https://clinicaltrials.gov/study/NCT00911599) | N/A | Completed | 60 | Randomized comparison of ion levels for all-cobalt-chrome vs modular hip |
| [NCT01010763](https://clinicaltrials.gov/study/NCT01010763) | N/A | Completed | 184 | Metal ion release and renal function in M2a Magnum hip arthroplasty |
| [NCT00156598](https://clinicaltrials.gov/study/NCT00156598) | N/A | Terminated | 5 | Serum cobalt, chromium and titanium in metal-on-metal vs metal-on-polyethylene hips |

NCT00586781 is labelled Phase 3, but it is a total ankle replacement device study and does not test chromium as a drug. It must not be counted toward the evidence level.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36545926](https://pubmed.ncbi.nlm.nih.gov/36545926/) | 2022 | RCT (implant study) | Acta Orthop | Cemented and cementless dual mobility cups showed similar fixation and low serum cobalt and chromium at 6 years |
| [34724103](https://pubmed.ncbi.nlm.nih.gov/34724103/) | 2023 | Cohort | Arch Orthop Trauma Surg | Whether cobalt and chromium blood levels normalize after revision of failed metal-on-metal hips |
| [37394959](https://pubmed.ncbi.nlm.nih.gov/37394959/) | 2023 | Cohort | Bone Joint J | Serum cobalt and chromium as predictors of patient-reported outcomes after ASR hip resurfacing |
| [22325959](https://pubmed.ncbi.nlm.nih.gov/22325959/) | 2012 | Cohort | J Arthroplasty | Cobalt and chromium levels rose significantly after large-diameter metal-on-metal hip arthroplasty |
| [19483243](https://pubmed.ncbi.nlm.nih.gov/19483243/) | 2009 | Cross-sectional | J Bone Joint Surg Br | Circulating cobalt and chromium from metal-on-metal hips associated with CD8+ T-cell lymphopenia |
| [21446789](https://pubmed.ncbi.nlm.nih.gov/21446789/) | 2011 | In vitro | J Immunotoxicol | Effects of clinically relevant Cr(6+) and Co(2+) concentrations on human lymphocytes |
| [27459602](https://pubmed.ncbi.nlm.nih.gov/27459602/) | 2016 | Cohort | Acta Orthop | Elevated chromium linked to worse quality of life and hip function in women with metal-on-metal hips |
| [35926884](https://pubmed.ncbi.nlm.nih.gov/35926884/) | 2022 | Cohort | Can J Surg | Whole blood metal ions at 1 and 10 years after Birmingham hip resurfacing |
| [27294138](https://pubmed.ncbi.nlm.nih.gov/27294138/) | 2016 | Observational | Biomed Res Int | Vanadium, chromium and calcium in cartilage and bone of patients with osteoarthritis |
| [34513441](https://pubmed.ncbi.nlm.nih.gov/34513441/) | 2021 | Case report | Cureus | End-stage tibiotalar osteoarthritis with chronic strontium toxicity, discussed alongside cobalt-chromium implants |

None of these studies evaluates chromium as a therapy for osteoarthritis.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 52/24/0031 | Nutryelt | Infusion | Not stated in registration data |
| L/24/329 | Dextrose 20% in water 500ml pcd201850 | Infusion | Not stated in registration data |
| Exclusion under Section 36 & Section 14 | ITN neonatal tpn 150ml 101 | TPN | Not stated in registration data |
| Exclusion under Section 36 & Section 14 | ITN 8811a 1520ml | TPN | Not stated in registration data |
| Exclusion under Section 36 & Section 14 | ITN neonatal tpn 150ml 102 | TPN | Not stated in registration data |

Eight registrations exist in total. Five are shown, all injectable or parenteral routes. Essential Medicines List status was not provided.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug-interaction records were found. Separately, the implant literature links chronic exposure to chromium and cobalt ions with lymphocyte changes and adverse local tissue reactions. This concerns implant-derived ions, not chromium given as a supplement, and it argues against assuming a benefit in joint disease.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The osteoarthritis prediction has no therapeutic evidence behind it. The 48 trials and 20 publications describe chromium as an implant-derived exposure marker, so the 98.68% score reflects knowledge-graph association and not clinical support.

**To proceed, the following is needed:**
- SAHPRA Professional Information warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for chromium
- Any preclinical or clinical study of chromium as an osteoarthritis therapy, none of which currently exists
- If pursuing the rheumatoid arthritis signal instead, the efficacy and safety results of NCT05545020 and independent replication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

