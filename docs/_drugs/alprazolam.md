---
layout: default
title: Alprazolam
parent: Model Prediction Only (L5)
nav_order: 24
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Alprazolam: predicted new indication Insomnia (evidence level L5). Approved use: Anxiety disorder"
---

# Alprazolam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Alprazolam: From Anxiety Disorder to Insomnia

## One-Sentence Summary

Alprazolam is a benzodiazepine originally used to treat anxiety disorders and mixed anxiety and depressive disorder.
The TxGNN model predicts it may be effective for **insomnia**, but there are currently **0 registered clinical trials** and only **indirect literature** (no alprazolam-specific insomnia efficacy trials), so this remains a model-driven hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorder; anxiety; mixed anxiety and depressive disorder (from the knowledge graph, as the registrations list no indication text) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L4 (see note below) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 |
| Recommended Decision | Hold |

*Note: The literature for insomnia contains no alprazolam-specific efficacy trials. The evidence is indirect (mechanism, utilisation and epidemiology), consistent with the L4 mechanism-level rating.*

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general benzodiazepine pharmacology, alprazolam enhances GABA-A receptor signalling, which produces sedative and anxiolytic effects. This gives a plausible basis for sleep-promoting activity.

Insomnia commonly occurs alongside anxiety and panic, so the symptom overlap with alprazolam's original indications is likely. This is a reasonable explanation for the model's prediction.

However, the supplied papers address panic disorder, benzodiazepine pharmacokinetics, prescribing trends, economic burden, zolpidem deprescribing and COVID-19 insomnia epidemiology. They offer only indirect support. Long-term hypnotic use also carries risks of dependence, tolerance, falls and cognitive impairment, particularly in elderly patients.

Two other predictions were also reviewed:
- **Agoraphobia (score 99.56%, evidence level L3):** Agoraphobia often coexists with panic disorder, for which alprazolam is established. Several controlled studies in panic disorder with agoraphobia exist, but the evidence is mostly on panic disorder with agoraphobia rather than agoraphobia alone. It may largely reflect existing use. This is better framed as a research question than a new indication.
- **Benign paroxysmal torticollis of infancy (score 99.61%, evidence level L5):** A model prediction only, with no trials, no literature and no supported mechanism. Benzodiazepine use in infants also raises safety concerns. The high score should not be read as clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for insomnia.

---

## Literature Evidence

None of the publications below is an alprazolam-specific insomnia efficacy trial. The most relevant items are listed.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | Retrospective clinical study | Medicine | 116 patients with coronary heart disease and insomnia; alprazolam was the control treatment compared with Du Meridian moxibustion plus ear acupuncture |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharmaceutica | Tranquilisers in elderly patients with chronic non-communicable diseases, assessing dose, outcomes and adverse effects |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | Pharmacokinetics of anxiolytic drugs |
| [7484706](https://pubmed.ncbi.nlm.nih.gov/7484706/) | 1995 | Review | Am Fam Physician | Overview of panic disorder (indirect relevance) |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | Predictive model | Value Health Reg Issues | Benzodiazepine use trends and economic burden; long-term use linked to memory loss, dependence, falls and traffic accidents |
| [35493764](https://pubmed.ncbi.nlm.nih.gov/35493764/) | 2022 | Cohort study | JHEP Reports | Deprescribing zolpidem in cirrhosis reduced falls and fractures |
| [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/) | 2023 | Preclinical (mouse) | Aging | Repeated alprazolam administration linked to mitochondrial dysfunction and impaired hippocampus-dependent memory |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Prescription pattern study | Sleep Medicine | Characteristics of hypnotic prescriptions in a managed-care population |
| [38363887](https://pubmed.ncbi.nlm.nih.gov/38363887/) | 2024 | Cross-sectional | Medicine | Insomnia among COVID-19 survivors (epidemiology only) |

---

## South Africa Market Information

Alprazolam is marketed in South Africa as oral tablets. No approved indication text was available for these registrations, and Essential Medicines List status was not available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 28/2.6/0001 | Biozane | Tablet | Not available |
| Reg. No. 29/2.6/0182 | Azor | Tablet | Not available |
| Reg. No. 30/2.6/0264 | Zopax | Tablet | Not available |
| Reg. No. 31/2.6/0241 | Coprax | Tablet | Not available |
| Reg. No. 32/2.6/0372 | Mylan alprazolam | Tablet | Not available |

---

## Safety Considerations

**Knowledge-graph contraindication signals** (from drug-disease relationships in the TxGNN knowledge graph, not from label text, so they must be verified against the Professional Information):
- Respiratory and sleep: obstructive sleep apnoea syndrome, sleep apnoea syndrome, congenital central hypoventilation syndrome
- Eye: open-angle and angle-closure glaucoma
- Organ impairment: kidney disease, liver disease, gallbladder disease
- Substance-related: substance-related disorder, substance abuse/dependence
- Other: obesity disorder, monogenic obesity, neurotic disorder, dysthymic disorder, pyoureter, Haddad syndrome

**Drug interactions:** The interaction screen returned 100 interactions in total, of which 20 are displayed. The most clinically important are:
- **Major:** morphine (including liposomal morphine), with the risk of additive central nervous system and respiratory depression
- **Moderate:** aprepitant, bupropion, cimetidine, clarithromycin, clotrimazole, dronabinol, eliglustat, glycerol phenylbutyrate, metoclopramide, miconazole
- **Minor:** antacids (aluminium hydroxide, calcium carbonate, magaldrate, magnesium salts) and corticosteroids (betamethasone, dexamethasone)

**Literature-based safety signals:** dependence, withdrawal and rebound symptoms on discontinuation (tapering required), memory impairment, falls in the elderly, and behavioural toxicity.

Please refer to the SAHPRA-approved Professional Information (PI) for label warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction rests on a plausible general benzodiazepine mechanism and indirect literature, with no registered trials and no alprazolam-specific insomnia efficacy data. Dependence, tolerance, falls and cognitive risks, along with a major interaction with opioids, further argue against advancing now.

**To proceed, the following is needed:**
- Retrieval and review of the SAHPRA package insert (warnings, contraindications and approved indications), which is currently a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- Alprazolam-specific randomised trials or systematic reviews in insomnia, compared against established hypnotics
- A risk-benefit assessment for elderly and comorbid populations, including a dependence and withdrawal mitigation plan
- Separately, for agoraphobia: determine whether it adds anything beyond the existing panic disorder use, and verify trial design and phase from registry records
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

