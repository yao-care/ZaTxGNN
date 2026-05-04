---
layout: default
title: Aspartic Acid
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 1
---

# Aspartic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Aspartic Acid: From Nutritional Amino Acid to Renal Tubular Acidosis

## One-Sentence Summary

Aspartic acid is a naturally occurring non-essential amino acid used primarily as a nutritional/dietary supplement, with no formally registered therapeutic indications in South Africa.
The TxGNN model predicts it may have therapeutic potential for **Renal Tubular Acidosis (RTA)**, with **no directly relevant clinical trials** and **10 publications** (primarily basic science, animal studies, and case reports) currently available to support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered therapeutic indications (nutritional/dietary amino acid) |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for aspartic acid as a therapeutic agent is not available through this evidence system. Aspartic acid is a non-essential amino acid that plays a central role in cellular metabolism, serving as an intermediate in the tricarboxylic acid (TCA) cycle and the urea cycle. Its importance to acid-base homeostasis in the kidney forms the biological basis for this TxGNN prediction.

The mechanistic link to renal tubular acidosis (RTA) is grounded in basic renal physiology. Aspartic acid participates in ammoniagenesis and acid-base buffering within renal tubular cells — processes directly impaired in RTA. Importantly, the SLC22A13 transporter mediates active efflux of aspartate and glutamate specifically at the basolateral membrane of type A intercalated cells in the renal collecting duct (PMID: 24147638) — the exact cell type responsible for proton secretion that fails in distal RTA. Animal studies further demonstrate that chronic metabolic acidosis alters concentrations of aspartate and other metabolic intermediates in rat kidney tissue (PMID: 2884989; PMID: 5641145), suggesting aspartic acid is metabolically responsive to the acidotic state.

There is one isolated historical case report (PMID: 6422151, 1983) describing a neonate with pyruvate carboxylase deficiency complicated by proximal RTA, who showed clinical improvement when dietary aspartic acid supplementation was introduced. While this is a single anecdotal observation in the context of a complex metabolic disorder, it represents the closest direct clinical signal in the available literature. The TxGNN high prediction score of 99.47% reflects structural associations in the knowledge graph rather than established clinical evidence, and must be interpreted with appropriate caution at this stage.

---

## Clinical Trial Evidence

No clinical trials directly investigating aspartic acid for renal tubular acidosis were identified. One trial was returned during the database query but is not applicable to this drug-disease pair:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT04725812](https://clinicaltrials.gov/study/NCT04725812) | Phase 2 | Terminated | 2 | **Not applicable to this analysis** — Investigates eculizumab (a complement inhibitor) for preeclampsia at 23–30 weeks gestation; no relationship to aspartic acid or renal tubular acidosis. Trial was terminated early with only 2 participants enrolled. |

**Currently no relevant clinical trials investigating aspartic acid for renal tubular acidosis are registered on ClinicalTrials.gov or ICTRP.**

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [6422151](https://pubmed.ncbi.nlm.nih.gov/6422151/) | 1983 | Case Report | J Inherit Metab Dis | Neonate with pyruvate carboxylase deficiency, proximal RTA, and cystinuria; clinical improvement observed when diet was supplemented with aspartic acid — the only direct clinical signal identified |
| [24147638](https://pubmed.ncbi.nlm.nih.gov/24147638/) | 2014 | In Vitro / Transporter Study | Biochemical Journal | SLC22A13 mediates unidirectional efflux of aspartate and glutamate at the basolateral membrane of type A intercalated cells in the renal collecting duct; co-localises with anion exchanger 1 (AE1) |
| [2884989](https://pubmed.ncbi.nlm.nih.gov/2884989/) | 1987 | Animal Study | Biochemical Journal | ¹³C NMR study in rat renal tubules: chronic metabolic acidosis significantly alters aspartate/glutamate utilisation and metabolic intermediate flux |
| [5641145](https://pubmed.ncbi.nlm.nih.gov/5641145/) | 1968 | Animal Study | Nature | Altered concentrations of metabolic intermediates, including aspartate, in kidneys of rats with experimental metabolic acidosis |
| [14301365](https://pubmed.ncbi.nlm.nih.gov/14301365/) | 1965 | Basic Science | Am J Physiol | Foundational study on the relationship between tubular cell pNH₃ and renal ammonia production; relevant to understanding aspartic acid's role in tubular acid-base handling |
| [990372](https://pubmed.ncbi.nlm.nih.gov/990372/) | 1976 | Case Series | Biomedicine | IV loading with ornithine-aspartate in children with familial neurological syndrome associated with incomplete RTA and cystinuria; amino acid metabolic responses characterised |
| [26208211](https://pubmed.ncbi.nlm.nih.gov/26208211/) | 2015 | Diagnostic Cohort | Jornal de Pediatria | Whole-exome sequencing for genetic diagnosis of distal RTA in four children; no therapeutic data on aspartic acid |
| [20068363](https://pubmed.ncbi.nlm.nih.gov/20068363/) | 2010 | Genetic Case Series | Nephron Physiology | SLC4A1 (AE1, Band 3) mutations causing distal RTA in Filipino children; mechanistic genetic study |
| [12087557](https://pubmed.ncbi.nlm.nih.gov/12087557/) | 2002 | Genetic Case Series | Am J Kidney Dis | G701D mutation of AE1 gene causing autosomal recessive distal RTA; defines how AE1 defects at the basolateral membrane impair proton secretion |
| [23053187](https://pubmed.ncbi.nlm.nih.gov/23053187/) | 2013 | Case Report | Ann Hematol | SLC4A1/AE1 A858D homozygous mutation with distal RTA, thrombocytopaenia, and haemolysis; no therapeutic data on aspartic acid |

---

## South Africa Market Information

Aspartic acid (DrugBank ID: DB00128) is **not registered with SAHPRA** and is currently **not marketed in South Africa** as a standalone therapeutic agent. No product licences or registration data are available.

> Note: Aspartic acid may be present as an excipient or as a component of nutritional formulations in some registered products, but no therapeutic registrations were identified in the SAHPRA database.

---

## Safety Considerations

No formal safety data — including warnings, contraindications, or drug-drug interactions — are available through this evidence system for aspartic acid as a therapeutic agent.

> As aspartic acid is not currently registered with SAHPRA as a standalone therapeutic product, no South African-approved Professional Information (PI) document is available for reference. Clinicians should consult primary literature and specialist resources before any clinical use. Any adverse drug reactions should be reported to SAHPRA via the **MedSafety** online reporting system (https://www.sahpra.org.za/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model identifies a biologically plausible mechanistic connection between aspartic acid and renal tubular acidosis through its role in renal ammoniagenesis and SLC22A13-mediated aspartate transport in intercalated cells. However, the overall evidence base is **L5** — limited to foundational basic science, animal studies, and isolated historical case reports — with no controlled human studies or registered clinical trials directly evaluating aspartic acid supplementation for RTA. The drug is also not registered in South Africa, presenting an additional regulatory barrier to any clinical pathway.

**To proceed, the following is needed:**

- Retrieval and review of complete mechanism of action data from DrugBank and primary pharmacology sources
- A scoping or systematic review specifically examining aspartic acid (and structurally related compounds such as ornithine-aspartate or potassium aspartate) in renal acid-base disorders
- A preclinical proof-of-concept study (in vitro tubular cell model or animal RTA model) to formally test the hypothesis that aspartic acid supplementation can improve renal proton secretion
- Investigation of whether related commercially available formulations (e.g., L-Ornithine L-Aspartate, used in hepatic encephalopathy) provide any indirect translational evidence
- Pharmacokinetic assessment of renal tubular aspartate concentrations achievable with oral or intravenous supplementation
- SAHPRA regulatory pathway assessment for potential investigational use, including Section 21 authorisation if clinical investigation is planned

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All content should be reviewed by a qualified clinician before any action is taken.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

