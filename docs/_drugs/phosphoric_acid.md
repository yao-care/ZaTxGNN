---
layout: default
title: Phosphoric Acid
parent: 僅模型預測 (L5)
nav_order: 364
evidence_level: L5
indication_count: 10
---

# Phosphoric Acid
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

# Phosphoric Acid: From No Established Therapeutic Indication to Osteoarthritis (Evidence Contradicts Therapeutic Direction)

## One-Sentence Summary

Phosphoric acid (DrugBank DB09394) has no established original therapeutic indication in the available data — it is not currently registered with SAHPRA and functions mainly as an excipient/acidifying agent. The TxGNN model predicts a possible association with **Osteoarthritis** (score 98.21%), but the supporting literature actually describes phosphate/pyrophosphate crystal deposition as a **pathogenic** contributor to osteoarthritis, not a therapeutic mechanism, and neither of the two identified clinical trials is actually relevant to this drug-disease pair.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — no SAHPRA-approved indication text available; phosphoric acid is primarily known as an excipient/acidifying agent |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.21% |
| Evidence Level | L4 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data for phosphoric acid is not available (flagged as a High-severity data gap). Based on the literature retrieved for this candidate, phosphoric acid itself is not described as a treatment for osteoarthritis at all. Instead, the evidence base centers on **basic calcium phosphate (BCP) and calcium pyrophosphate dihydrate (CPPD) crystals**, which are well-documented **pathological drivers** of cartilage calcification, inflammation, and joint damage in osteoarthritis.

This means the mechanistic direction implied by the literature runs **opposite** to what a repurposing hypothesis would require: rather than phosphate/phosphoric acid alleviating osteoarthritis, elevated phosphate-containing crystal formation is associated with worsening cartilage degradation. The TxGNN score is therefore best interpreted as reflecting a strong topical/co-occurrence association between "phosphate" and "osteoarthritis" in the knowledge graph, not a validated therapeutic mechanism. The internal repurposing rationale for this candidate explicitly flags this as a weak and potentially harmful mechanistic link.

The remaining nine predicted indications for this drug were also scored Hold, and five of them (hepatopulmonary syndrome, primitive portal vein thrombosis, idiopathic copper-associated cirrhosis, early-onset familial noncirrhotic portal hypertension, hepatoportal sclerosis) share an identical prediction score with zero supporting trials or literature — consistent with an embedding-similarity artifact rather than an independent signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07049731](https://clinicaltrials.gov/study/NCT07049731) | N/A | Not yet recruiting | 224 | Protein/resistance-exercise intervention for sarcopenia; matched on keywords only, no relevance to phosphoric acid or OA treatment |
| [NCT06921720](https://clinicaltrials.gov/study/NCT06921720) | N/A | Not yet recruiting | 65 | Diagnostic phosphorus-31 spectroscopy study in phosphate diabetes; not a therapeutic trial and not related to phosphoric acid repurposing |

Neither trial provides evidence for phosphoric acid as a treatment for osteoarthritis; both were flagged internally as low-relevance ("Grade C", keyword coincidence).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39089298](https://pubmed.ncbi.nlm.nih.gov/39089298/) | 2024 | Review | Lancet Rheumatology | CPPD crystal deposition drives inflammatory arthritis and is strongly linked to cartilage degradation/osteoarthritis — a pathogenic, not therapeutic, role |
| [36509917](https://pubmed.ncbi.nlm.nih.gov/36509917/) | 2023 | Review | Nature Reviews Rheumatology | Pathological calcification (BCP/CPP crystal formation) is a hallmark of osteoarthritis progression |
| [16716886](https://pubmed.ncbi.nlm.nih.gov/16716886/) | 2006 | Review | Rheumatic Diseases Clinics of North America | Calcium crystals are common, under-recognized contributors that may cause or worsen osteoarthritis |
| [29516278](https://pubmed.ncbi.nlm.nih.gov/29516278/) | 2018 | Review | Current Rheumatology Reports | BCP and CPPD crystals induce inflammation and may drive OA pathogenesis |
| [26720903](https://pubmed.ncbi.nlm.nih.gov/26720903/) | 2016 | Review | Current Opinion in Rheumatology | Discusses BCP crystals as a pathogenic target in osteoarthritis, not a treatment mechanism |
| [20425024](https://pubmed.ncbi.nlm.nih.gov/20425024/) | 2010 | Review | Current Rheumatology Reports | Examines association between uric acid/calcium pyrophosphate crystals and osteoarthritis onset/progression |
| [21169842](https://pubmed.ncbi.nlm.nih.gov/21169842/) | 2011 | Review | Current Opinion in Rheumatology | CPPD/BCP crystals are common in osteoarthritic joint fluid; role in joint damage remains under study |
| [34732285](https://pubmed.ncbi.nlm.nih.gov/34732285/) | 2021 | Review | Best Practice & Research Clinical Rheumatology | Calcium crystal-related endotypes present in ~60% of OA patients; crystals implicated in disease phenotype, not treatment |
| [20500910](https://pubmed.ncbi.nlm.nih.gov/20500910/) | 2010 | Editorial/Review | Arthritis Research & Therapy | Meniscal calcification correlates with OA severity; phosphocitrate (a crystal-formation inhibitor) reduces calcification — the opposite intervention direction from phosphoric acid |
| [38877353](https://pubmed.ncbi.nlm.nih.gov/38877353/) | 2024 | Preclinical/Materials study | Advanced Materials | Hydrogel scaffold for OA regeneration; contains hydroxyapatite (a calcium phosphate) as a structural material, not a discussion of phosphoric acid pharmacology |

All ten publications describe phosphate-containing crystals in the context of osteoarthritis **pathogenesis or diagnosis**, not as a therapeutic intervention.

---

## South Africa Market Information

Phosphoric acid currently holds **no SAHPRA product registration** (0 licenses recorded; market status: Not Marketed). No dosage form, brand name, or approved indication text is available for South Africa.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

(No SAHPRA-specific warnings, contraindications, or drug-interaction data were retrievable for this candidate; TFDA-equivalent labeling data is flagged as a Blocking data gap pending source retrieval.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic evidence for this candidate points in the opposite direction from a therapeutic hypothesis — phosphate-containing crystal deposition is documented as a driver of osteoarthritis pathology rather than a treatment. Combined with the absence of any relevant clinical trial evidence, no SAHPRA registration, and missing MOA/safety data, this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- Mechanism of action data for phosphoric acid (currently a High-severity data gap)
- TFDA/SAHPRA-equivalent Professional Information, warnings, and contraindications (currently a Blocking data gap)
- A therapeutic (not diagnostic/pathogenic) rationale specifically supporting phosphoric acid administration in osteoarthritis, ideally from a dedicated pharmacology or preclinical intervention study
- Re-evaluation of the other 9 ranked predictions for this drug before considering any indication other than osteoarthritis, given 5 share an identical, likely artifactual score with zero supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

