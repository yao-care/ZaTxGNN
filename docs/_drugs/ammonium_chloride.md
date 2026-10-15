---
layout: default
title: Ammonium Chloride
parent: Model Prediction Only (L5)
nav_order: 34
evidence_level: L5
indication_count: 10
---

# Ammonium Chloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Ammonium Chloride: From Pharyngitis and Common Cold to Acute Laryngopharyngitis

## One-Sentence Summary

Ammonium chloride is a traditional expectorant, originally used for pharyngitis, common cold and nasopharyngitis.
The TxGNN model predicts it may be effective for **acute laryngopharyngitis**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction.
It is a model prediction only, and the score likely reflects similarity to the existing indications rather than a new mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pharyngitis, common cold, nasopharyngitis (from the TxGNN knowledge graph; no approved indication text is available from the SAHPRA records) |
| Predicted New Indication | Acute laryngopharyngitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ammonium chloride is a traditional expectorant that may increase respiratory tract secretions. It is used in South Africa only in combination cough preparations, and mechanistically it may be applicable to acute laryngopharyngitis.

Acute laryngopharyngitis is very close to the existing indications (pharyngitis, common cold, nasopharyngitis), all of which are upper respiratory tract conditions. The high score most likely reflects this similarity to the existing indications rather than a genuinely new mechanism. No trials or literature were found to confirm it.

**Other predictions in the top 10** (all prediction only unless stated):
- **Nasal cavity disease** (99.94%): plausible given the labelled upper respiratory indications, but the category is broad and non-specific.
- **Faucial diphtheria** (98.93%): no plausible mechanism. Diphtheria is a toxin-mediated infection that needs antitoxin and antibiotics.
- **Cervical disc degenerative disorder** (98.87%): no plausible mechanism; likely a graph-based artifact.
- **Allergic urticaria** (98.50%): the one retrieved paper is about occupational skin disease from epoxy compounds and is likely a spurious match.
- **Trigeminal autonomic cephalalgia** (98.17%): no direct evidence.
- **Headache disorder** (97.99%): the only indication with historical clinical signals (see below).
- **Tracheal disease** (97.96%): biologically plausible given the expectorant action, but the one retrieved paper is a preclinical plant-extract study.
- **Papillary conjunctivitis** (91.73%) and **gonococcal urethritis** (91.64%): no rationale or evidence; gonococcal urethritis has established antibiotic therapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for acute laryngopharyngitis.

---

## Literature Evidence

Currently no related literature available for acute laryngopharyngitis.

For reference, four historical papers were found for the lower-ranked prediction **headache disorder**. They are from the 1950s, and no abstracts were available. Their titles suggest case series or clinical reports, and their methods cannot be verified.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [13254186](https://pubmed.ncbi.nlm.nih.gov/13254186/) | 1955 | Historical clinical report | Orvosi Hetilap | Ammonium chloride therapy of chronic migraine |
| [13345397](https://pubmed.ncbi.nlm.nih.gov/13345397/) | 1956 | Historical clinical report | Ideggyogyaszati Szemle | Neuro-endocrine effects of ammonium chloride in chronic headaches |
| [13317850](https://pubmed.ncbi.nlm.nih.gov/13317850/) | 1956 | Historical clinical report | Endokrinologie | Neuroendocrine effects of ammonium chloride, with focus on chronic headaches |
| [13466764](https://pubmed.ncbi.nlm.nih.gov/13466764/) | 1957 | Historical report / hypothesis | Revue Neurologique | Ammonium chloride treatment of anachlorhydric migraine; pathogenic considerations |

---

## South Africa Market Information

All 16 registrations are valid single-ingredient registrations (no cancelled ones). Most are syrups, and one is a tablet. No approved indication text is available in the data compiled for this report. The first 5 registrations are listed below. Essential Medicines List (EML) inclusion status was not available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. G830 (ACT101/1965) | Benylin & codeine | Syrup | Not available |
| Reg. No. 31/2.6/0241 | Coprax | Tablet | Not available |
| Reg. No. 28/10.1/0249 | Expectalin with cod | Syrup | Not available |
| Reg. No. 27/10.1/0529 | Dynalex | Syrup | Not available |
| Reg. No. G/10.1/1112 | Broncleer & cod unboxed | Syrup | Not available |

---

## Safety Considerations

Product-specific warnings and contraindications are not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Contraindication signals from the knowledge graph** (these come from graph edges, not label text, and should be confirmed against the PI). They include:
- Hepatic and renal: liver failure, impaired renal function, anuria
- Metabolic and endocrine: adrenocortical insufficiency/Addison disease, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, hyperthyroidism/Graves disease/thyrotoxicosis
- Cardiovascular: hypertension, sudden cardiac arrest, heart conduction disease, myocardial ischaemia, coronary artery disease, pulmonary oedema
- Neurological and psychiatric: epilepsy, insomnia, anxiety disorder, agoraphobia, obsessive-compulsive disorder
- Other: peptic ulcer disease, benign prostatic hyperplasia, bladder neck obstruction, ocular hypertension, angle-closure glaucoma, necrotizing enterocolitis

**Drug Interactions** (21 recorded from DDInter; 20 shown in the data compiled):
- **Moderate**: amphetamine, dextroamphetamine, lisdexamfetamine, metamfetamine, benzphetamine
- **Minor**: ephedrine (including nasal), pseudoephedrine, methadone, mexiletine, flecainide, and the tricyclic antidepressants (amitriptyline, clomipramine, desipramine, doxepin including topical, imipramine, nortriptyline, protriptyline, trimipramine)

Several registered products also contain codeine, so the safety profile of the whole combination must be considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for acute laryngopharyngitis is supported only by the model score (L5) and is very close to existing indications, so it adds little new. No trials or literature support it, and the safety data from the product labels is incomplete.

**To proceed, the following is needed:**
- Download and review the SAHPRA Professional Information (PI) for the registered products to obtain warnings, contraindications and approved indications
- Detailed mechanism of action data (MOA), for example from DrugBank
- Any clinical evidence for acute laryngopharyngitis, particularly modern controlled trials
- For headache disorder (graded L4, "Research Question"): the 1950s reports are not enough, and modern controlled studies would be needed before progressing
- A safety review of the knowledge-graph contraindication signals, given the many cardiovascular, renal and hepatic flags
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

