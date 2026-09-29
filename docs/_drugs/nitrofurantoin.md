---
layout: default
title: Nitrofurantoin
parent: Moderate Evidence (L3-L4)
nav_order: 341
evidence_level: L4
indication_count: 10
---

# Nitrofurantoin
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

# Nitrofurantoin: From Urinary Tract Infection to Rheumatoid Arthritis

## One-Sentence Summary

Nitrofurantoin is an antibacterial drug used for urinary tract infections (UTIs). The TxGNN model predicts it may be relevant to **rheumatoid arthritis**, but there are **0 clinical trials** and only a handful of loosely related publications. Most of these describe harms such as lung toxicity, not benefit, so the prediction should be treated as unsupported for now.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (general drug knowledge; the SAHPRA record has no indication text) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Nitrofurantoin is a urinary antibacterial, and no anti-rheumatic mechanism has been established for it.

The published literature links nitrofurantoin and rheumatoid arthritis (RA) mainly through harm:

- Drug-induced pulmonary fibrosis is a known toxicity, and RA itself can involve the lungs.
- One case report describes a patient on methotrexate who developed irreversible pulmonary fibrosis after adding nitrofurantoin.
- A UK cohort study examined whether antibiotic use is associated with RA flares.

The high TxGNN score most likely reflects co-occurrence in the knowledge graph (RA patients, chronic UTIs, pulmonary toxicity), not therapeutic benefit. Overall, the prediction has no credible mechanistic support at present.

The other nine predictions for this drug are also on Hold, and none has clinical trial support. Several look like adverse-effect signals rather than opportunities:

- **Methemoglobinemia**: nitrofurantoin is reported to cause it.
- **Sclerosing cholangitis**: nitrofurantoin is a known cause of drug-induced liver injury.
- **Diabetic nephropathy**: nitrofurantoin becomes less effective as renal function declines.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Cohort (self-controlled case series) | Scientific Reports | Studied antibiotic use and RA flares in 31,992 newly diagnosed RA patients (UK CPRD GOLD). This concerns antibiotics in general, not nitrofurantoin as a treatment. |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case report | Cureus | A 94-year-old woman with RA on long-term methotrexate developed irreversible pulmonary fibrosis after nitrofurantoin for chronic UTIs. |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | Lists nitrofurantoin among drugs that cause pulmonary fibrosis. RA is noted as a disease that predisposes to it. |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du Praticien | Drug-induced interstitial lung disease, with nitrofurantoin named among the implicated antibiotics. |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | 57 RA patients hospitalised for interstitial lung fibrosis; hospitalisation was rare (about 1 per 3,500 patient-years). Does not involve nitrofurantoin as a treatment. |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case report | Cureus | Autoimmune hepatitis versus drug-induced liver injury. Nitrofurantoin is listed as a possible cause to rule out. |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Case report | Revue de Pneumologie Clinique | Gold-salt-induced pneumonitis with CD4 alveolitis. Nitrofurantoin is not the focus. |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case report | Annales de Dermatologie et de Vénéréologie | Phenylbutazone-induced sialadenitis. Nitrofurantoin is only mentioned as another possible cause. |

None of these publications shows that nitrofurantoin treats RA. Of the 12 items retrieved, four (PMIDs 899886, 4608019, 5401858 and 4933314) were judged not relevant and are not listed.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 53/18.5/0109.107 | Cipladantin 50 | Capsule (oral) | Not provided in the retrieved record |

## Safety Considerations

Safety information from the SAHPRA-approved Professional Information (PI) has not been retrieved. Please refer to the PI for warnings and contraindications. Report adverse drug reactions to SAHPRA.

From the retrieved literature only, and not a substitute for the PI:

- **Pulmonary toxicity**: Nitrofurantoin is a recognised cause of pulmonary fibrosis and interstitial lung disease. This matters in RA, which itself can involve the lungs.
- **Drug interaction**: One case report describes irreversible pulmonary fibrosis when nitrofurantoin was added to long-term methotrexate. Methotrexate is a common RA drug.
- **Liver**: Drug-induced liver injury and autoimmune-like hepatitis have been reported.
- **Blood**: Methemoglobinemia and hemolytic anaemia have been reported, including in newborns.
- **Renal function**: Efficacy falls as renal function declines.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The RA prediction has no clinical trials and no plausible mechanism, and the literature mainly documents harm. Using nitrofurantoin in RA patients, who are often on methotrexate and prone to lung disease, carries more risk than potential benefit.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indication), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank, to assess any biological link to RA
- Evidence of therapeutic benefit, such as preclinical or clinical studies, which does not exist in the current data
- A structured safety review of the methotrexate–nitrofurantoin interaction and pulmonary risk before any further consideration

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

