---
layout: default
title: Arginine
parent: Moderate Evidence (L3-L4)
nav_order: 43
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-15
description: "Arginine: predicted new indication Gastroparesis (evidence level L4). Approved use: Not stated in the registration data compiled for this report (all 10…"
monitor_inn: "ARGININE"
predicted_indications: ["gastroparesis (disease)"]
---

# Arginine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Arginine: From Parenteral Nutrition Component to Gastroparesis

## One-Sentence Summary

Arginine is an amino acid used as a component of parenteral nutrition and peritoneal dialysis products registered in South Africa. The TxGNN model predicts it may be effective for **gastroparesis**, but there are currently **no registered clinical trials** and only **animal and mechanistic studies** among the publications retrieved. This is a hypothesis-stage prediction, not a clinically supported one.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data compiled for this report (all 10 registered products are amino acid-containing nutrition or dialysis preparations) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for arginine is not available in the data compiled for this report. The following reasoning is based on the published literature retrieved.

L-arginine is the substrate for nitric oxide synthase (NOS). Neuronal NOS (nNOS) produces nitric oxide, which drives nitrergic neurotransmission. This pathway helps relax the gastric fundus (accommodation) and the pyloric sphincter, both of which are needed for normal gastric emptying.

Several animal studies point to a deficit in this pathway:
- In mice, glucocorticoids induced gastroparesis through depletion of L-arginine (PMID 25057793). This suggests restoring arginine might improve emptying.
- Rats with a Parkinson's disease model showed impaired nitrergic relaxation in the pyloric sphincter (PMID 35380456).
- Diabetic models showed myenteric neuropathy and reduced nNOS function, a proposed mechanism of diabetic gastroparesis (PMID 18312542).

The mechanistic link is plausible, but all supporting data are from animals, and no human data on arginine for gastroparesis were provided. The high TxGNN score is a computational prediction and does not replace clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No RCTs, reviews or human studies of arginine in gastroparesis were identified. The most relevant publications are below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25057793](https://pubmed.ncbi.nlm.nih.gov/25057793/) | 2014 | Animal study (mouse) | Endocrinology | Glucocorticoid-induced gastroparesis was linked to depletion of L-arginine |
| [35380456](https://pubmed.ncbi.nlm.nih.gov/35380456/) | 2022 | Animal study (rat) | Am J Physiol Gastrointest Liver Physiol | Impaired nitrergic relaxation of the pyloric sphincter in a Parkinson's disease model with delayed gastric emptying |
| [18312542](https://pubmed.ncbi.nlm.nih.gov/18312542/) | 2008 | Animal study (rat) | Neurogastroenterol Motil | Myenteric neuropathy and nNOS changes in diabetic BB-rats, relevant to diabetic gastroparesis |
| [21193530](https://pubmed.ncbi.nlm.nih.gov/21193530/) | 2011 | Animal study | Am J Physiol Gastrointest Liver Physiol | Hyperglycaemia inhibits gastric motility via nodose ganglia KATP channels |
| [18322959](https://pubmed.ncbi.nlm.nih.gov/18322959/) | 2008 | Animal study (mouse) | World J Gastroenterol | Ghrelin and GHRP-6 effects on gastric motility in diabetic mice with gastroparesis |
| [19023028](https://pubmed.ncbi.nlm.nih.gov/19023028/) | 2009 | Animal study (dog) | Am J Physiol Gastrointest Liver Physiol | Gastric electrical stimulation improved vagotomy-induced impaired accommodation via the nitrergic pathway |
| [31984783](https://pubmed.ncbi.nlm.nih.gov/31984783/) | 2020 | Animal study (rat) | Am J Physiol Gastrointest Liver Physiol | Sacral nerve stimulation increased gastric accommodation |
| [8194696](https://pubmed.ncbi.nlm.nih.gov/8194696/) | 1994 | Animal study (rat) | Gastroenterology | Delayed gastric emptying after food protein-induced anaphylaxis |

Two further retrieved publications (PMID 33867519, a case report on lactate normalisation in a mitochondrial disorder carrier) are not relevant to this prediction and are omitted.

## South Africa Market Information

All 10 registrations are valid, single-ingredient registrations. Approved indication text was not available in the data compiled for this report. Essential Medicines List (EML) status was not available.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 37/34/0243 | Nutrineal PD4 with 1.1% amino acids 2.5L | Infusion | Not available |
| 37/25.2/0503 | Oliclinomel N6 900E 2000ml | Infusion | Not available |
| 41/25/0757 | Nutriflex Lipid Peri | Infusion | Not available |
| 52/25/0739 | Numeta G13E | Infusion | Not available |
| 52/25/0740 | Numeta G16E | Infusion | Not available |

Other registrations include Smofkabiven (46/32.2/0518), Smofkabiven Peripheral (47/32.2/0036), Nutriflex Omega Specialized (49/25/0065), Nutriflex Lipid Special 625ml (41/25/0759) and Adco-ipratropium (33/10.2.1/0271, listed as a vial). The last entry looks like a data-matching anomaly, since ipratropium is not an arginine product, and should be verified.

All products are parenteral (infusion) formulations. No oral arginine product was identified, so route compatibility with a gastroparesis indication has not been assessed.

## Safety Considerations

Product-specific warnings, contraindications and interaction data were not available. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The knowledge graph used by the TxGNN model lists drug-disease contraindication associations. These are model-derived and not label text, but they flag conditions needing caution if arginine were studied in a new setting:
- **Renal:** kidney disease, chronic kidney disease, end-stage renal failure, nephrolithiasis, acute urate nephropathy
- **Acid-base and electrolyte:** metabolic acidosis, renal tubular acidosis, hypercalcaemia, hyperparathyroidism, phosphorus metabolism disorders
- **Cardiovascular:** heart disease, cardiovascular disease, digitalis poisoning, ventricular fibrillation
- **Metabolic and haematological:** phenylketonuria and other disorders of phenylalanine metabolism, sickle cell anaemia
- **Other:** sarcoidosis, constipation, lytic metastatic bone lesions

Constipation is also a notable association for a gastrointestinal motility indication.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible through the nitric oxide pathway, but evidence is limited to animal and mechanistic studies (L4), with no registered clinical trials and no human data. Safety data from the product labels were also unavailable, which blocks safety screening.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications, approved indications) for the registered arginine-containing products
- Mechanism of action data from DrugBank
- A systematic literature search for human studies of arginine or NO-donor strategies in gastroparesis
- Assessment of an appropriate route and formulation (current registrations are parenteral only)
- A safety review for gastroparesis patients, particularly those with diabetes, renal impairment or cardiovascular disease
- Preclinical or small early-phase studies before any clinical development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

