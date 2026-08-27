---
layout: default
title: Phenylalanine
parent: 僅模型預測 (L5)
nav_order: 359
evidence_level: L5
indication_count: 2
---

# Phenylalanine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Phenylalanine: From Essential Amino Acid Supplementation to Sclerosing Cholangitis

## One-Sentence Summary

Phenylalanine is an essential amino acid with no registered therapeutic indication and no SAHPRA market presence in South Africa. The TxGNN model predicts a possible association with **Sclerosing Cholangitis**, but on review the supporting literature (4 publications, 0 clinical trials) does not describe phenylalanine as a treatment for this condition — the signal appears to be a knowledge-graph artefact rather than a genuine pharmacological hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — phenylalanine is an essential amino acid with no registered therapeutic indication in South Africa |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for phenylalanine in this context is not available, and no combination/drug class association is documented in the evidence pack.

More importantly, a review of the supporting literature does not establish a credible mechanistic link. None of the four retrieved publications studies phenylalanine as a treatment for sclerosing cholangitis: one examines plasma **tyrosine** (not phenylalanine) levels and fatigue in primary biliary cirrhosis/primary sclerosing cholangitis patients as an observational biomarker; one is a serum metabolomic profiling study in cholangiocarcinoma; and two describe **fMLP** (N-formyl-methionyl-leucyl-phenylalanine), a synthetic neutrophil-chemotactic tripeptide used to induce bile-duct inflammation in rat models — phenylalanine here is merely one amino-acid residue within an unrelated synthetic peptide, not free phenylalanine acting pharmacologically.

Given this, the high TxGNN score (99.43%) most likely reflects graph-embedding co-occurrence (e.g., shared terms such as "phenylalanine," "tyrosine," and "biliary/cholangitis" across unrelated studies) rather than a genuine biological hypothesis. This prediction should be treated as a data-driven signal requiring independent pharmacological justification, not as a validated mechanistic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohort/Observational | BMC Gastroenterology | Examined plasma **tyrosine** (not phenylalanine) concentration and its relation to fatigue in primary biliary cirrhosis and primary sclerosing cholangitis; not an interventional or phenylalanine-treatment study |
| [32025163](https://pubmed.ncbi.nlm.nih.gov/32025163/) | 2020 | Cohort/Metabolomics | Journal of Clinical and Experimental Hepatology | Serum metabolomic profiling in cholangiocarcinoma vs. benign hepatobiliary disease for biomarker discovery; not a treatment study |
| [8000512](https://pubmed.ncbi.nlm.nih.gov/8000512/) | 1994 | Animal model | Journal of Gastroenterology | Rat model of small-duct cholangitis induced by the synthetic chemotactic peptide fMLT (contains a phenylalanine residue); mechanistically unrelated to free phenylalanine pharmacology |
| [2103382](https://pubmed.ncbi.nlm.nih.gov/2103382/) | 1990 | Basic/Radioimmunoassay method | Journal of Gastroenterology and Hepatology | Describes enterohepatic circulation of bacterial chemotactic peptides (F-met-oligopeptides) in humans; an assay-methodology paper, not a phenylalanine treatment study |

---

## South Africa Market Information

No SAHPRA-registered products were found for phenylalanine. The drug is currently **not marketed** in South Africa (0 registrations).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*Note: A Professional Information warnings/contraindications review is flagged as a Blocking data gap — this must be resolved before any safety pre-assessment can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but none of the retrieved literature supports a real pharmacological link between phenylalanine and sclerosing cholangitis, no clinical trials exist for this candidate, and a Blocking data gap (PI warnings/contraindications) prevents even an initial safety assessment.

**To proceed, the following is needed:**
- PI warnings and contraindications data (Blocking gap — DG001)
- Mechanism of action (MOA) data for phenylalanine (High-priority gap — DG002)
- Independent pharmacological or preclinical evidence directly linking phenylalanine (not tyrosine or unrelated synthetic peptides) to biliary/cholangitis pathways
- Confirmation of any future SAHPRA registration status, since the drug is currently unmarketed in South Africa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

