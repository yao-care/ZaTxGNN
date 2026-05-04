---
layout: default
title: Benzocaine
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 10
---

# Benzocaine
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

# Benzocaine: From Topical Anaesthesia to Dyspepsia

## One-Sentence Summary

Benzocaine is an ester-type topical local anaesthetic with decades of established use in over-the-counter throat lozenges, dental gels, and procedural mucosal anaesthesia. The TxGNN model predicts it may be effective for **Dyspepsia**, supported by **1 direct randomised controlled trial** and **2 mechanistic studies** specifically evaluating benzocaine in upper gastrointestinal symptoms. However, benzocaine is currently not registered with SAHPRA, and evidence is limited to observational and indirect trial data, placing this candidate at the research-progression threshold.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Topical mucosal and skin anaesthesia |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 98.29% |
| Evidence Level | L3 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Benzocaine works by blocking voltage-gated sodium (Na⁺) channels in sensory nerve membranes, preventing the generation and propagation of pain and discomfort signals from mucosal surfaces. This mechanism is directly relevant to dyspepsia, a condition in which upper gastrointestinal discomfort is mediated in part by sensitised afferent nerve endings in the gastroduodenal mucosa — the same surface accessible to topically applied benzocaine.

A key mechanistic study (PMID 23565580, *Neurogastroenterology and Motility*, 2013) directly evaluated benzocaine in healthy human volunteers, demonstrating that application to the duodenal mucosa blocks the acid-induced duodenogastric sensorimotor reflex — the precise reflex pathway implicated in functional dyspepsia. This provides a clear biological chain of evidence: **Na⁺ channel blockade → suppression of duodenal mucosal afferent signalling → attenuation of dyspeptic symptoms**.

In clinical practice, this rationale has been translated into the **GI Cocktail** (benzocaine or viscous lidocaine + antacid + antispasmodic), a well-established emergency medicine preparation for symptomatic relief of upper gastrointestinal discomfort. A prospective RCT (PMID 15219296) confirmed that benzocaine performs equivalently to viscous lidocaine within this formulation, providing direct proof-of-concept for benzocaine's efficacy in this indication.

---

## Clinical Trial Evidence

No clinical trials directly evaluating benzocaine as a standalone therapeutic agent for dyspepsia were identified on ClinicalTrials.gov. The trials below provide the strongest contextual support for the mechanistic and therapeutic rationale:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00248651](https://clinicaltrials.gov/study/NCT00248651) | Phase 2/3 | Completed | 292 | Antidepressant therapy in functional dyspepsia; confirmed that the condition is driven by central sensory sensitisation and neurally-mediated pathways, indirectly validating sensory nerve modulation — benzocaine's mechanism — as a clinically effective treatment strategy |
| [NCT00521703](https://clinicaltrials.gov/study/NCT00521703) | Phase 3 | Completed | 78 | Evaluated topical lidocaine spray (structurally analogous to benzocaine, same pharmacological class) as an adjuvant during upper gastrointestinal endoscopy in children; confirmed the clinical feasibility and safety of applying topical local anaesthetics to the upper GI mucosa |

> The primary direct evidence for benzocaine in dyspepsia resides in the peer-reviewed literature (see below), not in registered clinical trials, which likely reflects the established OTC/emergency medicine status of this use rather than an absence of clinical evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [15219296](https://pubmed.ncbi.nlm.nih.gov/15219296/) | 2004 | Prospective RCT (active-controlled) | *Journal of Emergency Medicine* | Direct head-to-head RCT comparing benzocaine vs viscous lidocaine as the topical anaesthetic in a GI cocktail for dyspeptic patients in the emergency department (N not specified in abstract); benzocaine was equivalent to lidocaine in speed of onset and effectiveness of symptom relief — the strongest direct evidence for benzocaine in this indication |
| [23565580](https://pubmed.ncbi.nlm.nih.gov/23565580/) | 2013 | Mechanistic Experimental Study | *Neurogastroenterology and Motility* | Demonstrated in healthy humans that benzocaine applied to the duodenal mucosa blocks the acid-induced duodenogastric sensorimotor reflex (gastric relaxation + inhibition of antral motility + proximal gastric sensitisation); directly validates the proposed mechanism of action for functional dyspepsia and establishes duodenal mucosal nerve endings as the pharmacological target |
| [12077066](https://pubmed.ncbi.nlm.nih.gov/12077066/) | 2002 | Pathophysiology Study | *Gut* | Reviewed the role of dietary fat and cholecystokinin (CCK) in triggering dyspeptic symptoms via gastric distension and sensory sensitisation; provides pathophysiological context for the sensory nerve pathway that benzocaine targets, supporting the plausibility of mucosal afferent blockade as a therapeutic approach |

---

## South Africa Market Information

Benzocaine is currently **not registered with SAHPRA** and has no active product licences in South Africa. No entries were identified in the regulatory database.

For any formal clinical application in South Africa, SAHPRA registration would be required. Research use prior to registration may be pursued via a **Section 21 authorisation** under the Medicines and Related Substances Act (Act 101 of 1965), subject to SAHPRA approval.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for complete safety information once a registered product is identified. Report any adverse drug reactions to SAHPRA via the MedSafety online portal.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although benzocaine has a well-supported mechanistic basis and direct clinical RCT evidence for use in dyspepsia (particularly within the GI Cocktail framework), the drug is not currently registered with SAHPRA and has no approved products available in South Africa. Regulatory barriers must be resolved before clinical adoption can proceed. The overall evidence level (L3 — observational and indirect trial data, plus one active-controlled RCT) does not yet meet the threshold for a full repurposing recommendation in the absence of a dedicated Phase 2/3 RCT with dyspepsia as the primary endpoint.

**To proceed, the following is needed:**

- **Regulatory pathway**: Identify an existing SAHPRA-registered product containing benzocaine, or initiate a Section 21 application for research use
- **Dedicated RCT**: A well-designed randomised controlled trial specifically evaluating oral benzocaine formulations for functional dyspepsia as the primary endpoint (the existing RCT [PMID 15219296] used benzocaine within a combination GI cocktail, not as monotherapy)
- **Safety profile review**: Obtain the complete Professional Information (PI), with particular attention to methaemoglobinaemia risk (a class-specific concern for ester-type local anaesthetics) relevant to orally ingested mucosal doses
- **Pharmacokinetic data**: Confirm systemic absorption levels following oral mucosal administration at doses used for dyspepsia
- **Mechanism of action (MOA) data**: Retrieve full MOA detail from DrugBank (DB01086) to complete the mechanistic link analysis

> *This report is generated for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before therapeutic application. Results should be interpreted by qualified healthcare professionals.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

