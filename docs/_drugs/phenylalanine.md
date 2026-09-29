---
layout: default
title: Phenylalanine
parent: Model Prediction Only (L5)
nav_order: 367
evidence_level: L5
indication_count: 2
---

# Phenylalanine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Phenylalanine: From Amino Acid Component of Nutrition Products to Sclerosing Cholangitis

## One-Sentence Summary

Phenylalanine is an essential amino acid. In South Africa it is registered as an ingredient in amino acid-containing infusion and nutrition products, and no formal approved indication text is recorded for it.
The TxGNN model predicts it may be relevant to **sclerosing cholangitis**.
There are **no clinical trials** and **4 publications** on this indication, none of which tests phenylalanine as a treatment, so this is a **model prediction only**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records (products are amino acid infusion/nutrition preparations) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L4 (mechanism and observational metabolic data only; no interventional evidence) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Phenylalanine is an essential amino acid and the metabolic precursor of tyrosine. It is supplied as part of amino acid solutions for parenteral nutrition and peritoneal dialysis. Its established role is nutritional, not disease-modifying.

The only link to sclerosing cholangitis is metabolic. One cohort study (2005) measured plasma tyrosine in patients with primary biliary cirrhosis and primary sclerosing cholangitis and related it to fatigue. This shows that amino acid patterns are altered in cholestatic liver disease. It does not show that giving phenylalanine treats the condition.

The other retrieved papers do not support a therapeutic link. Two concern formylated bacterial chemotactic peptides (fMLP/fMLT-type), which are different molecules from free phenylalanine. One is a cancer metabolomics study. The TxGNN score is high, but it is a computational output and not backed by clinical data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohort | BMC Gastroenterology | Examined plasma tyrosine and amino acid patterns in relation to fatigue in PBC and PSC. Observational only. |
| [32025163](https://pubmed.ncbi.nlm.nih.gov/32025163/) | 2020 | Cohort | Journal of Clinical and Experimental Hepatology | Serum metabolic profiling of cholangiocarcinoma vs benign hepatobiliary disease in a UK cohort. Biomarker-oriented; not a treatment study. |
| [8000512](https://pubmed.ncbi.nlm.nih.gov/8000512/) | 1994 | Animal study | Journal of Gastroenterology | Rectal fMLT (a chemotactic tripeptide) induced small duct cholangitis in colitic rats. Involves a peptide, not free phenylalanine. |
| [2103382](https://pubmed.ncbi.nlm.nih.gov/2103382/) | 1990 | Laboratory/assay | Journal of Gastroenterology and Hepatology | Radioimmunoassay showing enterohepatic circulation of bacterial chemotactic peptides in humans. Methods paper. |

---

## South Africa Market Information

Registration records do not include approved indication text or manufacturer. Some product names (for example Adco-ipratropium) do not obviously contain phenylalanine, so the drug-to-product mapping should be verified against the SAHPRA Professional Information.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 37/34/0243 | Nutrineal PD4 with 1.1% amino acids 2.5L | Infusion | Not stated in registry record |
| Reg. No. 33/10.2.1/0271 | Adco-ipratropium (ni201) | Vial | Not stated in registry record |
| Reg. No. 38/34/0172 | Extraneal 2L single bag | Infusion | Not stated in registry record |
| Reg. No. 37/25.2/0503 | Oliclinomel N6 900E 2000ml | Infusion | Not stated in registry record |
| Reg. No. 41/25/0757 | Nutriflex Lipid Peri | Infusion | Not stated in registry record |

Showing 5 of 12 registrations.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score and one observational tyrosine/fatigue study. No trials exist, and no retrieved paper tests phenylalanine as a therapy for sclerosing cholangitis. A second predicted indication, congenital prothrombin deficiency, has even weaker support (L5, no plausible mechanism, only a withdrawn trial of a different drug) and is also on Hold.

**To proceed, the following is needed:**
- A plausible mechanism linking phenylalanine or tyrosine metabolism to cholangitis pathology
- Preclinical or early clinical data showing a treatment effect, not just altered amino acid levels
- Safety data from the SAHPRA package insert (warnings, contraindications), which is currently missing and blocks safety screening
- Mechanism of action data (for example from DrugBank)
- Confirmation of which SAHPRA products actually contain phenylalanine

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

