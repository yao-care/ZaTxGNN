---
layout: default
title: Nicotine
parent: Model Prediction Only (L5)
nav_order: 342
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Nicotine: predicted new indication Exercise-induced malignant hyperthermia (evidence level L5). Approved use: Nicotine dependence"
monitor_inn: "Nicotine"
predicted_indications: ["exercise-induced malignant hyperthermia", "migraine with brainstem aura", "oppositional defiant disorder (disease)", "migraine disorder", "blepharospasm", "46,XY disorder of sex development due to testicular steroidogenesis defect", "longitudinal vaginal septum", "transverse vaginal septum", "communication disorder", "developmental disorder of mental health"]
---

# Nicotine
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

## Nicotine: From Nicotine Dependence to Exercise-Induced Malignant Hyperthermia
{: .text-alpha }

## One-Sentence Summary

Nicotine was originally indicated for nicotine dependence (the knowledge graph also lists pellagra and beriberi, which relate to its nicotinic acid–type naming and are not clinically relevant here).
The TxGNN model's top-ranked prediction is **exercise-induced malignant hyperthermia**, but this prediction has **no clinical trials and no publications** behind it.
The best-supported lower-ranked candidate is **blepharospasm**, with **2 small pilot studies** that gave conflicting results.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Nicotine dependence (the registration records compiled for this report contain no approved indication text) |
| Predicted New Indication | Exercise-induced malignant hyperthermia (rank 1) |
| TxGNN Prediction Score | 83.91% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Nicotine is generally known to act on nicotinic acetylcholine receptors, including those at the neuromuscular junction.

For the top-ranked prediction, the mechanistic link is weak. Malignant hyperthermia is driven mainly by dysregulation of the ryanodine receptor (RYR1) and calcium release in muscle. Nicotinic agonism could in theory worsen neuromuscular excitability, so a safety concern is more plausible than a benefit. No supporting link is established, and the prediction should be treated as a model output only.

Other candidates in the top ten were also reviewed:

- **Blepharospasm (rank 5, L3):** The most plausible candidate. Nicotinic modulation of basal ganglia dopaminergic and cholinergic circuits is a reasonable rationale. A 1996 pilot reported benefit from nicotine nasal spray, but a 1998 pilot concluded it was not a reliable treatment.
- **Migraine disorder and migraine with brainstem aura (ranks 2 and 4, L4):** The literature is epidemiological or mechanistic, with mixed signals (trigger, withdrawal headache, possible cholinergic modulation). No therapeutic benefit has been shown.
- **Oppositional defiant disorder and developmental disorder of mental health (ranks 3 and 10, L4):** The literature mainly shows nicotine and tobacco exposure as a risk factor, which argues against repurposing.
- **Communication disorder (rank 9, L4):** The match appears to be a semantic artefact.
- **46,XY disorder of sex development, longitudinal and transverse vaginal septum (ranks 6 to 8, L5):** No plausible pharmacological rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered for exercise-induced malignant hyperthermia.

Two trials were retrieved for lower-ranked predictions. Neither tests nicotine as a treatment for the predicted disease:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03289676](https://clinicaltrials.gov/study/NCT03289676) | Phase 1 | Completed | 53 | Feasibility of a storytelling communication and HIV-tailored smoking cessation intervention in women living with HIV (linked to "communication disorder"; low relevance) |
| [NCT04560868](https://clinicaltrials.gov/study/NCT04560868) | Phase 1 | Completed | 57 | Pilot of an mHealth app for smokers ambivalent about quitting (linked to "developmental disorder of mental health"; not relevant) |

No SANCTR or PACTR identifiers were available.

## Literature Evidence

No related literature was retrieved for exercise-induced malignant hyperthermia. The most relevant publications are for the best-supported alternative, blepharospasm, plus key nicotine–migraine papers:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8691949](https://pubmed.ncbi.nlm.nih.gov/8691949/) | 1996 | Pilot study/case series | Lancet | Reported benefit of nicotine nasal spray in blepharospasm |
| [9452355](https://pubmed.ncbi.nlm.nih.gov/9452355/) | 1998 | Pilot study | Movement Disorders | Concluded nicotine nasal spray is not a reliable treatment for blepharospasm |
| [11549226](https://pubmed.ncbi.nlm.nih.gov/11549226/) | 2001 | Review | Psychopharmacology | Prepulse inhibition of startle in patient groups and pharmacological studies (mechanistic context) |
| [40468190](https://pubmed.ncbi.nlm.nih.gov/40468190/) | 2025 | Systematic review/meta-analysis | J Headache Pain | Association between smoking and primary headaches |
| [26140522](https://pubmed.ncbi.nlm.nih.gov/26140522/) | 2015 | Review | Headache | Tobacco and nicotine as headache triggers and sources of disability |
| [28920040](https://pubmed.ncbi.nlm.nih.gov/28920040/) | 2017 | Review | Anesthesiol Pain Med | Parasympathetic cholinergic mechanisms in migraine |
| [16816594](https://pubmed.ncbi.nlm.nih.gov/16816594/) | 2006 | Case report | Eur J Emerg Med | Severe migraine after sudden discontinuation of nicotine gum |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A/21.8.1/743 | Menoflush | Tablet | Not available in the compiled data |
| H2466 | Complenatal Ff | Capsule | Not available in the compiled data |

Both are valid single-ingredient registrations, and both are oral forms. Essential Medicines List status could not be determined from the compiled data.

## Safety Considerations

**Contraindications flagged in the knowledge graph** (drug–disease contraindication links, not label text):

- **Cardiovascular:** acute coronary syndrome, coronary artery disease, myocardial infarction, coronary thrombosis, Prinzmetal angina, hypotensive disorder
- **Metabolic and endocrine:** diabetes mellitus (type 1 included), diabetic ketoacidosis, hyperglycaemia, hyperthyroidism (Graves disease, thyrotoxicosis), gout
- **Haematological:** thrombocytopenia, blood coagulation disease, haemoglobinopathy
- **Gastrointestinal and hepatic:** peptic ulcer disease, liver disease, gallbladder disease
- **Tumours:** phaeochromocytoma and sympathetic paraganglioma, adrenal gland cancer, duodenum cancer, small intestine cancer, heart cancer
- **Other:** substance abuse/dependence

**Drug interactions:** 100 interactions were recorded (20 listed in the compiled data). The only moderate-level interaction listed is **bupropion**. Minor interactions include famotidine, ranitidine, cimetidine and nizatidine. Many others (for example metformin, glimepiride, rosiglitazone, morphine, omeprazole, pantoprazole, lansoprazole, prednisone) have an unclassified severity level.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and label contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (exercise-induced malignant hyperthermia) is supported only by the model score, with no trials or literature, and nicotine's pharmacology suggests potential harm rather than benefit. Even the best-supported alternative, blepharospasm, has only two small, conflicting pilot studies. The other candidates are supported only by associative or risk-factor literature.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- If a candidate is pursued, blepharospasm is the most reasonable research question, and it would need a controlled study with a tolerability and cardiovascular safety assessment
- Review of the knowledge-graph contraindications against the intended population and route
- Confirmation of approved indications and EML status for the two registered products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

