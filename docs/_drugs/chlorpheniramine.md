---
layout: default
title: Chlorpheniramine
parent: Moderate Evidence (L3-L4)
nav_order: 114
evidence_level: L4
indication_count: 10
---

# Chlorpheniramine
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

# Chlorpheniramine: From Licensed Antihistamine Use (Indication Not Recorded) to Allergic Urticaria

## One-Sentence Summary

Chlorpheniramine is a first-generation H1 antihistamine, registered in South Africa in several cold, flu and sinus/allergy products. The TxGNN model predicts it may be effective for **allergic urticaria**. No clinical trials are registered for this pair, and the supporting literature is **18 publications**, mostly reviews of other antihistamines. This is probably an established antihistamine use rather than a novel repurposing, but the supplied data cannot confirm that.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied SAHPRA data (registered products are cold, flu and sinus/allergy preparations) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 12 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. Chlorpheniramine is a potent alkylamine first-generation H1 antihistamine that has been used since the 1950s. It is widely used for allergic conditions and in over-the-counter cough and cold products.

In allergic urticaria, mast-cell histamine release drives the wheal-and-flare response, and H1 antagonists are the standard first-line drug class. Blocking the H1 receptor is therefore mechanistically consistent with symptom relief. A 2024 review lists chronic urticaria among chlorpheniramine's reported clinical uses.

The data do not show whether this is a genuinely new use. The original indication fields are empty, and the literature retrieved is mostly about other antihistamines (cetirizine, loratadine, ebastine, acrivastine). No controlled chlorpheniramine trial in allergic urticaria appears in the evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for chlorpheniramine in allergic urticaria (ClinicalTrials.gov or ICTRP). No SANCTR or PACTR identifiers were supplied.

## Literature Evidence

No RCTs were found for this indication. The table lists reviews first, then a phase I trial, then case reports.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35652393](https://pubmed.ncbi.nlm.nih.gov/35652393/) | 2024 | Review | Curr Rev Clin Exp Pharmacol | Comprehensive review of chlorpheniramine, including reported uses such as chronic urticaria, asthma and depression |
| [7528133](https://pubmed.ncbi.nlm.nih.gov/7528133/) | 1994 | Review | Drugs | Loratadine review; controlled studies compare it with several antihistamines, including chlorpheniramine, in allergic disorders including urticaria |
| [1683523](https://pubmed.ncbi.nlm.nih.gov/1683523/) | 1991 | Review | Ann Allergy | Compares second-generation H1 antihistamines with older, more sedating first-generation agents |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Review | Drugs | Cetirizine in allergic rhinitis, pollen-induced asthma and chronic urticaria (a different drug; class context only) |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Review | Drugs | Acrivastine effective in chronic urticaria and allergic rhinitis (class context only) |
| [8808167](https://pubmed.ncbi.nlm.nih.gov/8808167/) | 1996 | Review | Drugs | Ebastine efficacy in allergic disorders including chronic idiopathic urticaria (class context only) |
| [14977391](https://pubmed.ncbi.nlm.nih.gov/14977391/) | 2004 | Review | Drugs | Cetirizine in allergic disorders (class context only) |
| [39265704](https://pubmed.ncbi.nlm.nih.gov/39265704/) | 2024 | Randomised phase I trial | Eur J Pharm Sci | Bilastine (oral and parenteral) vs parenteral dexchlorpheniramine on histamine-induced wheal and flare |
| [31852144](https://pubmed.ncbi.nlm.nih.gov/31852144/) | 2019 | Case reports + pharmacovigilance review | Medicine | Two cases of chlorpheniramine-induced anaphylaxis, with a review of a pharmacovigilance database (safety signal) |
| [26240795](https://pubmed.ncbi.nlm.nih.gov/26240795/) | 2015 | Case report | Asia Pac Allergy | Chlorpheniramine-induced anaphylaxis diagnosed by basophil activation test (safety signal) |

## South Africa Market Information

Twelve registrations are recorded. The five main ones are listed below. Approved indication text was not supplied for any of them.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 37/5.8/0260 | Sinutab sinus allergy congestion and pai (name truncated in source) | Tablet | Not stated in supplied data |
| Reg. No. 37/5.8/0552 | Corenza Cold And Flu Syrup | Syrup | Not stated in supplied data |
| Reg. No. 27/5.8/0123 | Degoran Cold And Flu Hot Medicated Drink | Sachet | Not stated in supplied data |
| Reg. No. G1235 (ACT 101) | Famucaps | Capsule | Not stated in supplied data |
| Reg. No. 37/5.8/0139 | Sinutab sinus pain extra strength | Tablet | Not stated in supplied data |

## Safety Considerations

The following points come from the retrieved literature, not from SAHPRA labelling:

- **Hypersensitivity**: Case reports describe chlorpheniramine-induced anaphylaxis (PMID 31852144, 26240795).
- **Sedation**: This is a recognised class effect of first-generation antihistamines (PMID 1683523).

Please refer to the SAHPRA-approved Professional Information (PI) for warnings, contraindications and drug interactions. No drug interaction data were retrieved, and that may be a data gap. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and the TxGNN score is very high. There are no registered trials, no direct controlled chlorpheniramine evidence for allergic urticaria in the retrieved literature, and no SAHPRA safety data. The evidence is limited to reviews of other antihistamines.

**To proceed, the following is needed:**
- SAHPRA Professional Information (PI) for the registered products, covering warnings, contraindications and approved indications, to confirm whether urticaria is already a labelled use
- Mechanism of action data from DrugBank
- Direct controlled evidence for chlorpheniramine in urticaria (targeted literature search)
- A verified drug interaction check
- For comparison, rhinitis (predicted rank 10) has stronger published evidence (L2) and may be a more useful direction to review.

*This report is for research reference only and does not constitute medical advice. Predictions require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

