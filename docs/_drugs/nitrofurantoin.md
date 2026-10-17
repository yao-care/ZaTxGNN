---
layout: default
title: Nitrofurantoin
parent: Model Prediction Only (L5)
nav_order: 343
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Nitrofurantoin: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not stated in the SAHPRA registration data compiled for this report (…"
monitor_inn: "Nitrofurantoin"
predicted_indications: ["rheumatoid arthritis", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "diabetic nephropathy", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "sclerosing cholangitis", "methemoglobinemia, alpha type", "gout", "methemoglobinemia"]
---

# Nitrofurantoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Nitrofurantoin: From Urinary Tract Infection (Antibacterial Use) to Rheumatoid Arthritis

## One-Sentence Summary

Nitrofurantoin is an oral antibacterial, registered in South Africa as a capsule, and used for urinary tract infections.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are **no registered clinical trials** and the **9 publications retrieved describe harm rather than benefit** (mainly drug-induced pulmonary fibrosis and interactions).
This prediction is not supported by the evidence compiled for this report.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data compiled for this report (nitrofurantoin is generally used as an antibacterial for urinary tract infections) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 (no trials; literature is limited to adverse-effect reports and observational data) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. In general, nitrofurantoin is an antibacterial whose nitroreductase-activated metabolites damage bacterial DNA and ribosomes. This activity is directed at bacteria, not at the immune-mediated joint inflammation of rheumatoid arthritis.

**The prediction is not mechanistically plausible.** The literature retrieved concerns harm, not therapeutic benefit:

- Drug-induced pulmonary fibrosis and interstitial lung disease, where nitrofurantoin is a recognised cause.
- A case of irreversible pulmonary fibrosis after methotrexate and nitrofurantoin were used together in a patient with rheumatoid arthritis.
- A large self-controlled case series examining antibiotic exposure and rheumatoid arthritis flares.

The high TxGNN score most likely reflects network proximity through shared adverse-effect or comorbidity pathways (for example interstitial lung disease) rather than a treatment effect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Cohort (self-controlled case series) | Scientific Reports | Examined the association between antibiotic use and rheumatoid arthritis flares in a UK cohort of 31,992 newly diagnosed patients; this is a flare-risk analysis, not evidence of benefit |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case report | Cureus | A 94-year-old woman on long-term methotrexate developed irreversible pulmonary fibrosis after nitrofurantoin was added |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | Drug-induced pulmonary fibrosis; nitrofurantoin listed among causative drugs, and rheumatoid arthritis as a predisposing disease |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du Praticien | Drug-induced interstitial lung diseases; nitrofurantoin listed among implicated antibiotics |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | Poor prognosis in rheumatoid arthritis patients hospitalised for interstitial lung fibrosis; does not involve nitrofurantoin therapy |

Four further retrieved papers (on bacteriuria screening, sialadenitis, autoimmune hepatitis and gold-salt pneumonitis) are only tangentially related and show no therapeutic benefit in rheumatoid arthritis.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 53/18.5/0109.107 | Cipladantin 50 | Capsule | Not stated in the data compiled for this report |

The Essential Medicines List (EML) status could not be determined from the data compiled for this report.

## Safety Considerations

Specific label warnings and contraindications from the SAHPRA Professional Information (PI) were not available. The PI should be reviewed before any use.

**Conditions flagged as contraindication-related in the knowledge graph** (derived from drug-disease relationships, not from label text):

- **Renal:** impaired renal function, anuria
- **Liver and biliary:** drug-induced liver injury, hepatitis, obstructive jaundice, biliary tract disease
- **Lung:** interstitial lung disease, pulmonary fibrosis (including postinflammatory)
- **Nerve and eye:** peripheral neuropathy, peripheral nervous system disease, optic neuritis
- **Haematological and metabolic:** G6PD deficiency, vitamin B12 deficiency, vitamin B deficiency, beriberi, ariboflavinosis, diabetes mellitus, diabetic ketoacidosis, glycogen storage disease, cystinuria, galactosemia
- **Gastrointestinal:** *Clostridium difficile* colitis, perinatal necrotizing enterocolitis

**Drug interactions:** 100 interactions were identified in the interaction databases. Those listed in this report include:

- **Moderate:** balsalazide, metronidazole, picosulfuric acid, naltrexone, rosuvastatin, simvastatin
- **Minor:** anticholinergics (hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, trospium, mepenzolate, methscopolamine, propantheline, scopolamine) and magnesium- or aluminium-containing antacids (magaldrate, magnesium carbonate, magnesium hydroxide, magnesium oxide)

**Particular concern for this prediction:** the retrieved literature documents pulmonary toxicity with methotrexate plus nitrofurantoin in rheumatoid arthritis, a combination relevant to many patients with this disease. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials, no plausible therapeutic mechanism, and the available literature points to harm (pulmonary fibrosis, methotrexate interaction) rather than benefit in rheumatoid arthritis. The high TxGNN score appears to reflect adverse-effect associations in the knowledge graph.

**To proceed, the following is needed:**
- A credible mechanistic rationale (the mechanism of action data is missing)
- The SAHPRA-approved PI warnings, contraindications and registered indication, which were not available for this report
- Preclinical or early-phase clinical evidence of anti-rheumatic activity, none of which currently exists
- A risk assessment addressing pulmonary toxicity and the methotrexate interaction

**Other predicted indications** (all Hold, none supported by evidence):

- **Diabetic nephropathy** (L4): reduced nitrofurantoin efficacy and avoidance at low eGFR argue against use.
- **Sclerosing cholangitis** (L4): nitrofurantoin is itself a cause of drug-induced liver injury.
- **Methemoglobinemia** (L4): nitrofurantoin is a cause, not a treatment, particularly in G6PD deficiency.
- **Brain small vessel disease, hereditary hematuria syndrome, brachydactyly-syndactyly, colobomatous microphthalmia, alpha-type methemoglobinemia and gout** (L5): prediction only, with no supporting data.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

