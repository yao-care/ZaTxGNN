---
layout: default
title: Calcium
parent: Moderate Evidence (L3-L4)
nav_order: 88
evidence_level: L4
indication_count: 10
---

# Calcium
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Calcium: From No Recorded Indication to Thrombotic Disease

## One-Sentence Summary

The supplied registration data record no approved indication for calcium in South Africa. The TxGNN model predicts it may be relevant to **thrombotic disease**, with a score of 98.25%. The search retrieved **40 clinical trials** and **20 publications**, but none tests calcium as a treatment for thrombosis, so this is a model signal and not clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied registration data (all approved-indication fields are empty) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 98.25% (model rank 7,514) |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for calcium is not available in the supplied data. Calcium ions are a physiological cofactor in blood coagulation and platelet activation, which explains why the knowledge graph links calcium to thrombosis.

That link points the wrong way for a treatment. Calcium's role in clotting suggests a pro-thrombotic or neutral effect, not a therapeutic one. The retrieved literature is mostly basic science on calcium signalling in platelets and endothelium, plus general reviews of calcium intake and cardiovascular risk. None of it shows that giving calcium treats or prevents thrombosis.

The high TxGNN score reflects graph proximity, not clinical proof. Because the drug's original indication is also unrecorded, there is no clear "original-to-new" therapeutic relationship to assess.

---

## Clinical Trial Evidence

The search returned 40 trials. None tests calcium as the intervention for thrombotic disease. The table lists the most relevant ones, and most involve other drugs. Nadroparin *calcium* is a low molecular weight heparin, so the calcium there is only the salt form and not the active moiety.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00951574](https://clinicaltrials.gov/study/NCT00951574) | Phase 3 | Completed | 1,166 | Nadroparin calcium (LMWH) versus placebo to prevent venous and arterial thromboembolism in cancer patients on chemotherapy |
| [NCT00421538](https://clinicaltrials.gov/study/NCT00421538) | Phase 3 | Completed | 260 | Nadroparin versus placebo for symptomatic calf vein thrombosis |
| [NCT04319627](https://clinicaltrials.gov/study/NCT04319627) | Phase 3 | Recruiting | 2,700 | Statins added to anticoagulation to reduce recurrent venous thromboembolism |
| [NCT02679664](https://clinicaltrials.gov/study/NCT02679664) | Phase 2 | Unknown | 312 | Rosuvastatin pilot for recurrent VTE (not a calcium intervention) |
| [NCT01528800](https://clinicaltrials.gov/study/NCT01528800) | Phase 2 | Completed | 85 | Vitamin K versus placebo on coronary artery calcification in haemodialysis patients (calcification is the outcome, not the drug) |
| [NCT07303816](https://clinicaltrials.gov/study/NCT07303816) | Phase 4 | Not yet recruiting | 4,000 | Rosuvastatin to prevent cancer-associated VTE |
| [NCT02526303](https://clinicaltrials.gov/study/NCT02526303) | N/A | Withdrawn | 0 | Anticoagulation for non-occlusive portal vein thrombosis in cirrhosis |
| [NCT05621915](https://clinicaltrials.gov/study/NCT05621915) | N/A | Completed | 43 | Nadroparin calcium pharmacokinetics in COVID-19 (observational) |
| [NCT00604825](https://clinicaltrials.gov/study/NCT00604825) | Phase 2 | Completed | 356 | GSK232802 for menopausal hot flushes (unrelated to calcium or thrombosis) |

The only trial in the pack that tests calcium itself is [NCT05027048](https://clinicaltrials.gov/study/NCT05027048), a Phase 3 RCT of calcium chloride for blood loss from uterine atony at caesarean delivery (n=120, completed). It was retrieved under a different predicted indication and gives no support for thrombotic disease.

No SANCTR or PACTR identifiers were supplied.

---

## Literature Evidence

No RCTs or clinical studies of calcium therapy for thrombosis were retrieved. The publications are reviews and basic or mechanistic studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22283597](https://pubmed.ncbi.nlm.nih.gov/22283597/) | 2012 | Review | Am J Cardiovasc Drugs | Reviews prospective studies and trials on calcium intake and cardiovascular disease. Discusses possible effects through cholesterol, vasodilation, inflammation and thrombosis, and notes both inadequate and excessive intake are of concern |
| [39796525](https://pubmed.ncbi.nlm.nih.gov/39796525/) | 2024 | Review | Nutrients | Vitamin D deficiency and thrombotic disease. Vitamin D is discussed as a regulator of calcium metabolism, not calcium as therapy |
| [36453103](https://pubmed.ncbi.nlm.nih.gov/36453103/) | 2023 | Preclinical/Mechanistic | Haematologica | Plasma from patients with immune TTP triggers calcium- and IgG-dependent endothelial activation, correlating with disease severity |
| [38880165](https://pubmed.ncbi.nlm.nih.gov/38880165/) | 2024 | Review | Life Sci | Altered calcium fluxes and mitochondrial metabolism in platelet activation, with relevance to atherothrombosis and ageing |
| [37563135](https://pubmed.ncbi.nlm.nih.gov/37563135/) | 2023 | Preclinical | Nat Commun | MTH1 protects platelet mitochondria and regulates platelet function and thrombosis. Its deficiency reduced thrombin-induced calcium mobilisation in mice |
| [26972052](https://pubmed.ncbi.nlm.nih.gov/26972052/) | 2016 | Preclinical/Mechanistic | Cell | Gut-microbe metabolite TMAO enhances platelet hyperreactivity and thrombosis risk. Not a calcium-therapy study |
| [35767715](https://pubmed.ncbi.nlm.nih.gov/35767715/) | 2022 | Preclinical | Blood | PTPN22 negatively modulates platelet function and thrombus formation in mice |
| [35165707](https://pubmed.ncbi.nlm.nih.gov/35165707/) | 2022 | Translational | Eur Heart J | Galectin-3 enhances platelet aggregation and thrombosis via Dectin-1 |
| [36334396](https://pubmed.ncbi.nlm.nih.gov/36334396/) | 2022 | Observational | Thromb Res | SCUBE1 is associated with thrombotic complications and in-hospital mortality in COVID-19 |
| [41055696](https://pubmed.ncbi.nlm.nih.gov/41055696/) | 2026 | Preclinical | Blood | STK10 regulates platelet function in arterial thrombosis and thromboinflammation in knockout mice |

---

## South Africa Market Information

The pack reports 20 SAHPRA registrations, and the five below are the first listed. None includes an approved-indication text. They are multi-component products (parenteral nutrition, human serum) and not single-ingredient calcium products.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTICLE 21B (N/A) | ITN 7009a 2520ml | TPN | Not stated |
| ARTICLE 21B (N/A) | ITN 2000a 2010ml | TPN | Not stated |
| Exclusion under Section 36 & Section 14 | ITN8011XA 1520ml adult | TPN | Not stated |
| Exclusion under Section 36 & Section 14 | ITN paediatric tpn 107 | TPN | Not stated |
| T/30.3/704 | Stabilised Human Serum-5% Protein Solution | Infusion | Not stated |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 98.25% TxGNN score is a model signal only. No retrieved trial or publication tests calcium as a therapy for thrombotic disease, and calcium's known role in coagulation suggests a pro-thrombotic or neutral effect. The pack's own review classes this as L4 with a Hold recommendation, and the other nine predicted indications are also Hold.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings and contraindications), which is currently missing and blocks safety screening
- Mechanism of action data from DrugBank
- Checking whether the prediction is a name-matching artefact, since the matched trials involve nadroparin calcium, vitamin K and statins, not calcium therapy
- Any human study testing a calcium intervention with a thrombosis outcome
- A defined original indication and the specific calcium salt and formulation under consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

