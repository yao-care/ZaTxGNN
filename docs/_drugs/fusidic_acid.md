---
layout: default
title: Fusidic Acid
parent: Moderate Evidence (L3-L4)
nav_order: 243
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Fusidic Acid: predicted new indication Exposure keratitis (evidence level L4). Approved use: Bacterial infections, including urinary tract infection, bronchitis…"
monitor_inn: "Fusidic acid"
predicted_indications: ["exposure keratitis", "non-human animal disease", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "parasitic eyelid infestation"]
---

# Fusidic Acid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Fusidic Acid: From Bacterial Infections to Exposure Keratitis

## One-Sentence Summary

Fusidic acid is an antibiotic originally used for bacterial infections, particularly skin infections caused by Gram-positive organisms such as *Staphylococcus aureus*.
The TxGNN model predicts it may be effective for **exposure keratitis**, but there are **no registered clinical trials** and only **1 indirect publication** (a case series on ocular *Tsukamurella* infections) supporting this direction.
The prediction is therefore a computational signal only, not yet a clinically supported indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections, including urinary tract infection, bronchitis, folliculitis, acne, seborrhoeic dermatitis and bacterial pneumonia (from the knowledge graph; no SAHPRA indication text available) |
| Predicted New Indication | Exposure keratitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, fusidic acid inhibits bacterial elongation factor G (EF-G) and is active mainly against Gram-positive bacteria such as *Staphylococcus aureus*. Its efficacy in skin and soft-tissue infections is established.

Exposure keratitis, however, is primarily a mechanical or desiccation disorder of the cornea (for example, incomplete eyelid closure). An antibacterial would be relevant only for secondary bacterial infection. The single publication retrieved is a case series on ocular *Tsukamurella* infections. It is indirect and does not evaluate fusidic acid for this condition. The high TxGNN score is therefore not supported by clinical evidence.

**Other predictions reviewed:**

- **Otitis externa** (score 99.84%, evidence L4, flagged as a research question). It is commonly caused by *S. aureus* and other Gram-positive organisms, which fusidic acid targets. The supporting literature consists of bacteriology and resistance surveys, mostly in dogs, plus two older human studies of discharging ears. None evaluates fusidic acid efficacy. This is the most biologically plausible of the predictions, but it still needs formal evaluation.
- **Other predictions** (non-human animal disease, postinfectious vasculitis, post-bacterial disorder, post-infectious syndrome, infective urethral stricture, Chagas cardiomyopathy, infection-related haemolytic uraemic syndrome, parasitic eyelid infestation). All are L5 with no trials or literature, and several lack a plausible mechanistic link. For infection-related haemolytic uraemic syndrome, antibiotics are generally avoided because they may increase toxin release.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31246677](https://pubmed.ncbi.nlm.nih.gov/31246677/) | 2019 | Case series | Cornea | Largest case series of *Tsukamurella*-associated ophthalmic infections, including the first report of ocular implant infection after enucleation. Indirect; fusidic acid was not evaluated. |

**Supporting literature for the secondary prediction (otitis externa):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12542200](https://pubmed.ncbi.nlm.nih.gov/12542200/) | 2002 | Cohort/microbiology (human) | Acta Oto-Laryngologica | Prevalence of community-acquired MRSA in discharging ears compared with other pathogens |
| [12437801](https://pubmed.ncbi.nlm.nih.gov/12437801/) | 2002 | Cohort/microbiology (human) | J Laryngol Otol | In 161 outpatients with otorrhoea, *S. aureus* was found in 43.5% of isolates and *Pseudomonas* was the most common non-*S. aureus* pathogen |
| [20434850](https://pubmed.ncbi.nlm.nih.gov/20434850/) | 2010 | Case series/case-control (canine) | Vet Microbiol | Coryneform bacteria in canine otitis externa |
| [41148721](https://pubmed.ncbi.nlm.nih.gov/41148721/) | 2025 | Resistance survey (canine) | Antibiotics (Basel) | Antimicrobial resistance of *S. pseudintermedius* in dogs with otitis externa and healthy dogs |
| [41594059](https://pubmed.ncbi.nlm.nih.gov/41594059/) | 2025 | Resistance survey (canine) | Antibiotics (Basel) | Resistance patterns in bacteria from canine skin and ear infections in Serbia |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 45/13.4.1/0678 | Fucibet | Cream | Not available in the data compiled |
| Reg. No. 45/13.4.1/0568 | Fucidin H | Cream | Not available in the data compiled |
| Reg. No. G2090 (OM) | Fucidin H | Ointment | Not available in the data compiled |

All three registrations are valid single-ingredient products, and all are topical (cream or ointment). Essential Medicines List (EML) status is not available in the data compiled for this report.

---

## Safety Considerations

**Contraindications flagged in the knowledge graph.** These come from drug-disease edges in the TxGNN knowledge graph, not from label text, and should be verified against the SAHPRA-approved Professional Information (PI). The flagged conditions include:

- **Hepatic and renal:** liver failure, liver disease, gallbladder disease, kidney disease, nephrocalcinosis
- **Ocular:** glaucoma, open-angle glaucoma, ocular hypertension, herpes simplex virus keratitis, eye infectious disease, conjunctivitis
- **Metabolic:** diabetes mellitus, diabetic ketoacidosis, hypercalcaemia, potassium deficiency, phosphorus metabolism disease
- **Cardiac:** atrial fibrillation, atrioventricular block, Adams-Stokes syndrome, Wolff-Parkinson-White syndrome
- **Gastrointestinal:** *Clostridium difficile* colitis, colitis, perinatal necrotising enterocolitis, oesophageal dyskinesia
- **Neuromuscular and respiratory:** myasthenia gravis, neuromuscular junction disease, respiratory failure, central nervous system origin vertigo
- **Other:** pyoureter

Several of these, particularly the eye infection, conjunctivitis and herpes simplex keratitis entries, are relevant to the ocular prediction. Many of these edges appear to reflect other drugs or formulations (for example, systemic or combination products), so they should be interpreted cautiously.

Package-insert warnings, contraindications and drug interaction data were not available. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication of exposure keratitis has no clinical trials and only one indirect case series, so the high TxGNN score is not backed by clinical evidence. The SAHPRA label warnings and contraindications are also unavailable, so a safety review cannot be completed.

**To proceed, the following is needed:**
- SAHPRA package insert (warnings, contraindications, approved indications), which is a blocking data gap
- Detailed mechanism of action data (for example, from DrugBank)
- For exposure keratitis: evidence that fusidic acid has a role beyond treating secondary bacterial infection, and ophthalmic formulation and safety data, as only topical skin products are registered in South Africa
- For otitis externa: a formal evaluation of topical fusidic acid in human patients, together with local *S. aureus* resistance data, as the more plausible research question
- Review of the knowledge-graph contraindications against the PI
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

