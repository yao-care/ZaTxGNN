---
layout: default
title: Aspartic Acid
parent: Moderate Evidence (L3-L4)
nav_order: 48
evidence_level: L4
indication_count: 1
---

# Aspartic Acid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Aspartic Acid: From Parenteral Nutrition Component to Renal Tubular Acidosis

## One-Sentence Summary

Aspartic acid is an amino acid. In South Africa it is registered as a component of parenteral nutrition infusions, and the registration records do not state a separate approved indication.
The TxGNN model predicts it may be useful for **renal tubular acidosis**.
This rests on a knowledge-graph prediction only: **1 registered clinical trial (not relevant)** and **10 publications, none testing aspartic acid as a treatment for this condition**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records; registered products are parenteral nutrition infusions |
| Predicted New Indication | Renal tubular acidosis |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Aspartic acid is a component of amino acid infusion products, and mechanistically it may be linked to renal acid-base handling.

Aspartate takes part in renal tubular amino acid handling. It also sits in the glutamate/glutamine pathways that feed renal ammoniagenesis and acid excretion. This gives a plausible biochemical connection to acid-base regulation, which is why a knowledge-graph model could link it to renal tubular acidosis (RTA).

There are important limits. Distal RTA is mainly caused by defects in transporters and pumps (for example SLC4A1/AE1, ATP6V1B1, ATP6V0A4), not by aspartate deficiency. No retrieved evidence shows that aspartic acid supplementation corrects tubular acidification. The high score is a model prediction and could not be cross-checked against known pharmacology, because the original indication and mechanism of action are unavailable.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04725812](https://clinicaltrials.gov/study/NCT04725812) | Phase 2 | Terminated | 2 | Eculizumab in preeclampsia (CRUSH study). It does not study aspartic acid or RTA and provides no usable evidence. |

No SANCTR or PACTR registrations were identified.

---

## Literature Evidence

None of the publications below is an RCT. They are genetic case reports and case series of RTA, or preclinical and physiological studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24147638](https://pubmed.ncbi.nlm.nih.gov/24147638/) | 2014 | Preclinical | Biochem J | SLC22A13 mediates efflux of aspartate and glutamate at the basolateral membrane of type A intercalated cells in the renal collecting duct, co-localising with AE1 |
| [2884989](https://pubmed.ncbi.nlm.nih.gov/2884989/) | 1987 | Preclinical | Biochem J | Metabolic fate of glutamate carbon in rat renal tubules, including the effect of chronic metabolic acidosis |
| [6422151](https://pubmed.ncbi.nlm.nih.gov/6422151/) | 1983 | Case report | J Inherit Metab Dis | Neonate with pyruvate carboxylase deficiency, proximal RTA and cystinuria. The infant thrived after a diet supplemented with several amino acids including aspartic acid, so the effect cannot be attributed to aspartic acid or to RTA correction |
| [990372](https://pubmed.ncbi.nlm.nih.gov/990372/) | 1976 | Physiological study | Biomedicine | Intravenous arginine and ornithine-aspartate loading in siblings with a neurological syndrome, cystinuria and incomplete RTA |
| [26208211](https://pubmed.ncbi.nlm.nih.gov/26208211/) | 2015 | Genetic diagnostic study | J Pediatr (Rio J) | Whole-exome sequencing gave a genetic diagnosis in four children with distal RTA |
| [20068363](https://pubmed.ncbi.nlm.nih.gov/20068363/) | 2010 | Case series | Nephron Physiol | Distal RTA in Filipino children caused by SLC4A1 (AE1) mutations |
| [12087557](https://pubmed.ncbi.nlm.nih.gov/12087557/) | 2002 | Case report | Am J Kidney Dis | Autosomal recessive distal RTA caused by the G701D mutation of AE1 |
| [23053187](https://pubmed.ncbi.nlm.nih.gov/23053187/) | 2013 | Case report | Ann Hematol | Hypokalaemic distal RTA with haemolysis and acanthocytosis in an AE1 A858D homozygote |
| [14301365](https://pubmed.ncbi.nlm.nih.gov/14301365/) | 1965 | Physiological study | Am J Physiol | Relationship between tubular cell pNH3 and renal ammonia production |
| [5641145](https://pubmed.ncbi.nlm.nih.gov/5641145/) | 1968 | Preclinical | Nature | Concentrations of metabolic intermediates in kidneys of rats with metabolic acidosis |

---

## South Africa Market Information

Six registrations are recorded. Five entries are listed below; two of them share registration number 41/25/0757. The registration records do not state an approved indication text.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 41/25/0757 | Nutriflex Lipid Peri | Infusion | Not stated in registration record |
| Reg. No. 52/25/0739 | Numeta G13E | Infusion | Not stated in registration record |
| Reg. No. 52/25/0740 | Numeta G16E | Infusion | Not stated in registration record |
| Reg. No. 49/25/0065 | Nutriflex Omega Specialized | Infusion | Not stated in registration record |
| Reg. No. 41/25/0757 | Nutriflex lipid peri 1875ml | TPN | Not stated in registration record |

All registered products are injectable or infusion parenteral nutrition products. No oral formulation is registered.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by any relevant clinical or mechanistic evidence. The only trial is unrelated, and the literature describes RTA genetics and renal metabolism without showing that aspartic acid corrects tubular acidification. RTA is mainly driven by transporter and pump defects rather than amino acid deficiency. In addition, the safety information needed for screening is not yet available.

**To proceed, the following is needed:**
- SAHPRA Professional Information (PI) for the registered products, covering warnings and contraindications
- Mechanism of action data, for example from DrugBank
- Evidence that aspartic acid supplementation changes urinary acidification or acid-base status in RTA, from preclinical models or human physiological studies
- Assessment of route compatibility, since all registered products are intravenous parenteral nutrition and no oral product exists
- Definition of the original indication, to allow a proper comparison with the predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

