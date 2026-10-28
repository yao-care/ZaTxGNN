---
layout: default
title: Levofloxacin
parent: Model Prediction Only (L5)
nav_order: 294
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Levofloxacin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Bacterial infections (streptococcal and staphylococcal infections…"
monitor_inn: "Levofloxacin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
---

# Levofloxacin
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

## Levofloxacin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Levofloxacin is a broad-spectrum fluoroquinolone antibiotic, originally used for bacterial infections such as pneumonia, sinusitis, pyelonephritis and conjunctivitis.
The TxGNN model's top-ranked prediction is **punctate epithelial keratoconjunctivitis**, but this is supported by **0 clinical trials** and only **1 publication** (an outbreak report that does not test levofloxacin).
Among the other predictions, **septicemic plague** has the most credible support (L3, animal evidence), and **monoclonal gammopathy** has a large body of literature on infection prophylaxis in myeloma.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (streptococcal and staphylococcal infections, bacterial pneumonia, anthrax, sinusitis, conjunctivitis, pyelonephritis, among others). SAHPRA indication text is not available in the data compiled for this report. |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis (rank 1) |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 (rank 1 prediction). For reference: septicemic plague L3; monoclonal gammopathy L4 |
| South Africa Market Status | Marketed (valid licences: 4 of 4) |
| Number of SAHPRA Registrations | 4 (valid: 4) |
| Recommended Decision | Hold (rank 1 prediction) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Levofloxacin is a fluoroquinolone, a class that kills bacteria by inhibiting DNA gyrase and topoisomerase IV. Its efficacy in bacterial conjunctivitis and other infections is established, so ocular surface use is plausible for bacterial eye disease.

However, the rank 1 prediction is weakly supported. The only publication retrieved describes an outbreak of **microsporidial** keratoconjunctivitis linked to contaminated swimming pool water. Microsporidia are not susceptible to fluoroquinolones, and the report contains no evidence of levofloxacin efficacy. The high TxGNN score most likely reflects the drug's existing ocular indications rather than a true mechanistic link.

Of the ten predictions reviewed, two merit separate comment:

- **Septicemic plague (rank 9):** Levofloxacin acts directly on *Yersinia pestis*. Studies in African green monkeys showed cure of experimental pneumonic plague, and this model supported FDA approval under the Animal Rule. Evidence is non-human, there are no human RCTs, and some older mouse studies reported lack of efficacy against a nalidixic acid-resistant strain. Plague is already a labelled use in some jurisdictions, so this may not be a true repurposing.
- **Monoclonal gammopathy (rank 7):** The literature concerns levofloxacin as prophylaxis against infection in newly diagnosed symptomatic multiple myeloma, not treatment of the gammopathy itself. The TEAMM trial (a double-blind, placebo-controlled phase 3 RCT) is the key study. The evidence is indirect for the predicted indication.

The remaining predictions (hyperamylasemia, polyclonal hyperviscosity syndrome, congenital analbuminemia, premalignant haematological disease, haematological disease with acquired peripheral neuropathy, congenital haematological disorder) have no supporting trials or literature. Their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Blood group incompatibility is supported only by a case report of an infectious complication. Fluoroquinolones carry a known peripheral neuropathy risk, so the neuropathy-associated prediction is more likely a safety concern than a benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered for the rank 1 prediction. No trials were retrieved for any of the other top 10 predictions either.

## Literature Evidence

**Rank 1: Punctate epithelial keratoconjunctivitis**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Outbreak report | Am J Ophthalmol | Microsporidial keratoconjunctivitis outbreak from swimming pool water contamination in Taiwan; no levofloxacin efficacy data |

**Most relevant supporting literature for other predictions (for context)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31668592](https://pubmed.ncbi.nlm.nih.gov/31668592/) | 2019 | RCT (phase 3) | Lancet Oncol | TEAMM: levofloxacin prophylaxis in newly diagnosed myeloma (monoclonal gammopathy prediction) |
| [31690402](https://pubmed.ncbi.nlm.nih.gov/31690402/) | 2019 | RCT summary | Health Technol Assess | Summary of the TEAMM RCT of prophylactic levofloxacin in symptomatic myeloma |
| [26150022](https://pubmed.ncbi.nlm.nih.gov/26150022/) | 2015 | Cohort | Biol Blood Marrow Transplant | Levofloxacin prophylaxis and bloodstream infection or fever in myeloma patients undergoing autologous HSCT |
| [29080369](https://pubmed.ncbi.nlm.nih.gov/29080369/) | 2018 | Comparative study | Clin Transplant | Ciprofloxacin vs levofloxacin prophylaxis in autologous HSCT for myeloma |
| [21347450](https://pubmed.ncbi.nlm.nih.gov/21347450/) | 2011 | Animal study (primate) | PLoS Negl Trop Dis | Levofloxacin cured experimental pneumonic plague in African green monkeys |
| [32435805](https://pubmed.ncbi.nlm.nih.gov/32435805/) | 2020 | Animal study (primate) | Clin Infect Dis | Effect of delaying treatment on ciprofloxacin and levofloxacin efficacy in pneumonic plague |
| [32435803](https://pubmed.ncbi.nlm.nih.gov/32435803/) | 2020 | Review/Regulatory | Clin Infect Dis | African green monkey model and FDA approval of antimicrobials under the Animal Rule |
| [17517837](https://pubmed.ncbi.nlm.nih.gov/17517837/) | 2007 | Animal/in vitro model | Antimicrob Agents Chemother | Streptomycin vs levofloxacin for plague: resistance selection and mutant fitness |
| [21574421](https://pubmed.ncbi.nlm.nih.gov/21574421/) | 2010 | Animal study (mouse) | Antibiot Khimioter | Lack of levofloxacin efficacy against a nalidixic acid-resistant *Y. pestis* strain |
| [8913481](https://pubmed.ncbi.nlm.nih.gov/8913481/) | 1996 | In vitro | Antimicrob Agents Chemother | Levofloxacin highly active against 100 *Y. pestis* isolates from a southern African plague focus |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 44/20.1.1/0249 | Zybact 250 Mg | Tablet | Not available in data compiled |
| Reg. No. A39/20.1.1/0578 | Levofloxacin-winthrop IV sol for infusion | Infusion | Not available in data compiled |
| Reg. No. 42/20.1.1/0632 | Lintrip 250 | Tablet | Not available in data compiled |
| Reg. No. 46/20.1.1/0978 | Levojub 500 | Film-coated tablet (Fct) | Not available in data compiled |

All four registrations are valid single-ingredient products. Essential Medicines List inclusion status was not available in the data compiled for this report. No ophthalmic dosage form is registered, so ocular use would require a suitable topical formulation.

## Safety Considerations

**Contraindications / conditions of concern (from knowledge graph drug-disease edges, not label text):**
- Cardiac: long QT syndrome (including familial), torsades de pointes, myocardial ischaemia, coronary artery disease
- Neurological/neuromuscular: epilepsy, myasthenia gravis (including adult-onset), neuromuscular junction disease, peripheral neuropathy and peripheral nervous system disease
- Musculoskeletal: tendinitis, periarthritis, rhabdomyolysis, nodular fasciitis, exostosis
- Metabolic: diabetes mellitus, diabetic ketoacidosis, potassium deficiency
- Hepatic/biliary/renal: liver disease, drug-induced liver injury, gallbladder disease, impaired renal function
- Haematological: thrombocytopenia, leukopenia, pancytopenia, anaemia (including macrocytic)
- Gastrointestinal: *Clostridium difficile* colitis, perinatal necrotising enterocolitis

**Drug interactions:** 100 interactions were identified; examples from the first 20 returned include:
- **Major:** tramadol, hydrocortisone
- **Moderate:** abiraterone, acarbose, famotidine, formoterol, ketorolac, adenosine, ibuprofen, ethinylestradiol, albiglutide, salbutamol, alfuzosin, alogliptin, metformin, pioglitazone, amifampridine
- **Minor:** paclitaxel, aldesleukin, altretamine

A published case report also describes acute kidney injury from crystal nephropathy with pomalidomide and levofloxacin (PMID 25591868).

Please refer to the SAHPRA-approved Professional Information (PI) for label warnings and contraindications, which were not available in the data compiled. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold** (rank 1, punctate epithelial keratoconjunctivitis)

**Rationale:**
- The only evidence for the top prediction is an outbreak report of a microsporidial infection, which fluoroquinolones do not treat. The high TxGNN score is likely driven by the drug's existing conjunctivitis indications.
- Among the other predictions, septicemic plague (**Proceed with Guardrails**, L3) has a direct mechanism and strong animal data, and monoclonal gammopathy (**Research Question**, L4) has high-quality but indirect prophylaxis evidence. All other predictions should remain on Hold.

**To proceed, the following is needed:**
- SAHPRA package insert warnings, contraindications and approved indication text (currently a blocking data gap)
- Detailed mechanism of action data from DrugBank
- For punctate epithelial keratoconjunctivitis: identification of the causative pathogens and evidence of levofloxacin susceptibility, plus a topical ophthalmic formulation
- For septicemic plague: confirmation of whether plague is already within the labelled indication scope in South Africa, and local resistance data
- For monoclonal gammopathy: clarification that benefit is infection prophylaxis in symptomatic myeloma (not MGUS), weighed against resistance, *C. difficile* and QT risks
- Safety monitoring plan for QT prolongation, tendon, neuropsychiatric and dysglycaemia risks, and drug interaction screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

