---
layout: default
title: Fenoterol
parent: Model Prediction Only (L5)
nav_order: 224
evidence_level: L5
indication_count: 10
---

# Fenoterol
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

# Fenoterol: From Bronchodilator Use (Airway Obstruction) to Multiple System Atrophy

## One-Sentence Summary

Fenoterol is a beta2-adrenergic agonist bronchodilator, marketed in South Africa as nebulisation vials and inhalers. The registration data supplied do not state an approved indication.
The TxGNN model's top-ranked prediction is **multiple system atrophy** (score 99.70%), but there are **0 clinical trials and 0 publications** for it, and the mechanism is not plausible. Across all 10 predicted indications, the only one with any literature is **anaphylaxis** (11 records, all preclinical or indirect).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data (drug class: beta2-agonist bronchodilator) |
| Predicted New Indication | Multiple system atrophy (rank 1) |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

The 10 predicted indications, in rank order:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision |
|---|---|---|---|---|
| 1 | Multiple system atrophy | 99.70% | L5 | Hold |
| 2 | Postural orthostatic tachycardia syndrome | 99.61% | L5 | Hold |
| 3 | Variably protease-sensitive prionopathy | 99.54% | L5 | Hold |
| 4 | Open-angle glaucoma | 99.43% | L5 | Hold |
| 5 | Raynaud disease | 99.41% | L5 | Hold |
| 6 | Primary hereditary glaucoma | 99.37% | L5 | Hold |
| 7 | Sinoatrial block | 99.35% | L5 | Hold |
| 8 | Sinoatrial node disease | 99.25% | L5 | Hold |
| 9 | Anaphylaxis | 98.28% | L4 | Research question |
| 10 | Glaucoma 1, open angle | 98.16% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Fenoterol is a beta2-adrenergic agonist. Its established pharmacology is bronchodilation, and it is also used as a tocolytic.

**Multiple system atrophy (rank 1):** No disease-modifying mechanism is evident. Fenoterol's peripheral vasodilation could lower blood pressure further in MSA-related autonomic failure and orthostatic hypotension. The high score is most likely a knowledge-graph artifact.

**Other top-ranked predictions:**
- **POTS:** Beta2 agonism would be expected to worsen tachycardia and orthostatic intolerance. Beta-blockade, not agonism, is the direction used in practice, so this is a potential safety concern.
- **Prion disease (variably protease-sensitive prionopathy):** No link between beta2 signalling and prion misfolding is established. This is probably a proximity artifact in an ultra-rare disease with sparse network data.
- **Glaucoma (three entries):** Adrenergic agonists can modulate aqueous humour dynamics, so the mechanism is loosely plausible. Fenoterol is not an ocular agent, and ocular delivery, efficacy and safety are unstudied. "Open-angle glaucoma" and "glaucoma 1, open angle" are the same disease group and should be merged.
- **Raynaud disease:** Beta2-mediated vasodilation gives a superficial rationale. Systemic beta2 agonism has no established benefit here, and its tachycardia and hypotension liabilities argue against use.
- **Sinoatrial block and sinoatrial node disease:** Beta-agonist chronotropy relates mechanistically to sinus node function. Fenoterol is not selective enough for this use, and its arrhythmogenic and hypokalaemic effects are a safety risk.

**Anaphylaxis (rank 9)** is the only prediction with a coherent biological rationale. Beta2 agonists, including fenoterol, inhibit antigen-induced mediator release from mast cells and basophils. They also attenuate anaphylactic bronchospasm in rat and guinea pig models. Epinephrine remains the standard of care, and beta2 agonists are at most an adjunct for bronchospasm.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the 10 predicted indications (ClinicalTrials.gov and ICTRP; no SANCTR or PACTR identifiers were provided).

---

## Literature Evidence

There is no literature for multiple system atrophy (rank 1) or for any other predicted indication except anaphylaxis. The table below therefore shows the anaphylaxis records (10 of 11 shown). All are preclinical, ex vivo or case-level.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [98295](https://pubmed.ncbi.nlm.nih.gov/98295/) | 1978 | Preclinical (rat) | Chest | Effects of fenoterol on passive cutaneous anaphylaxis and histamine skin test in rats |
| [2889607](https://pubmed.ncbi.nlm.nih.gov/2889607/) | 1987 | Preclinical (rat) | Eur J Pharmacol | Sodium cromoglycate and the beta2 agonists fenoterol and salbutamol were synergistic in inhibiting passive anaphylactic bronchoconstriction |
| [68010](https://pubmed.ncbi.nlm.nih.gov/68010/) | 1977 | Preclinical (rat) | Int Arch Allergy Appl Immunol | Fenoterol was the most potent inhibitor of IgE-mediated histamine release in vivo (ED50 6 µg/kg i.v., vs salbutamol 40 and isoproterenol 94) |
| [6203772](https://pubmed.ncbi.nlm.nih.gov/6203772/) | 1984 | Preclinical / ex vivo | Eur J Respir Dis Suppl | Beta-adrenoceptor subtypes mediating relaxation and inhibition of antigen-induced histamine release in human and guinea pig airways |
| [6199956](https://pubmed.ncbi.nlm.nih.gov/6199956/) | 1984 | Preclinical (guinea pig) | Agents Actions | Fenoterol attenuated antigen-induced bronchospasm and changes in tissue histamine |
| [2864902](https://pubmed.ncbi.nlm.nih.gov/2864902/) | 1985 | Preclinical (guinea pig lung) | Arch Int Pharmacodyn Ther | Possible mechanism for the anti-anaphylactic effect of beta agonists, via thromboxane A2 release (class mechanism) |
| [2565667](https://pubmed.ncbi.nlm.nih.gov/2565667/) | 1989 | Preclinical (guinea pig) | Agents Actions | Beta-adrenoceptor-mediated inhibition of IgG1- and IgE-dependent anaphylactic tracheal contraction (class mechanism) |
| [6416724](https://pubmed.ncbi.nlm.nih.gov/6416724/) | 1983 | Preclinical (indirect) | Clin Exp Pharmacol Physiol | Fenoterol was about 1000 times more potent than cromoglycate in relaxing guinea pig trachea; the study is mainly about cromoglycate |
| [2409769](https://pubmed.ncbi.nlm.nih.gov/2409769/) | 1985 | Preclinical (other drug) | Agents Actions | Clenbuterol inhibited histamine release from human lung tissue; the fenoterol effect was propranolol-sensitive |
| [11993080](https://pubmed.ncbi.nlm.nih.gov/11993080/) | 2002 | Case report | Anaesthesist | Anaphylaxis after IV hydrocortisone; not about fenoterol, so low relevance |

The remaining record (PMID 42288, 1979, guinea pig ileum Schultz-Dale reaction) is not classified and is not shown.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 35/10.2.1/0004 | Adco-nebrafen 4ml | Vial | Not provided in the data |
| Reg. No. 35/10.2.1/0302 | Duovent Hfa | Inhaler | Not provided in the data |
| Reg. No. 37/20.1.1/0042 | Adco ceftriaxone powder f/injection | Injection | Not provided in the data |
| Reg. No. Z/10.2.1/78 | Atrovent beta udv 4ml | Vial | Not provided in the data |

The ceftriaxone product (37/20.1.1/0042) is an antibiotic and is probably a mapping error in the source data. Verify it before counting it among fenoterol registrations. Essential Medicines List (EML) status was not provided.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Mechanism-based concerns noted in the prediction rationale (not taken from the PI):
- Vasodilation and hypotension, which is relevant to MSA and orthostatic disorders.
- Tachycardia, which is relevant to POTS.
- Arrhythmia and hypokalaemia, which is relevant to sinoatrial disease.

No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predictions (including multiple system atrophy) have no trials or literature, and several are mechanistically implausible or potentially harmful, so a high TxGNN score alone is not enough. Anaphylaxis is the only indication with any supporting literature, but that literature is preclinical, and epinephrine remains the standard of care. It stays at the research-question stage.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indications). This is a blocking gap that prevents safety screening.
- Mechanism of action data from DrugBank.
- Verification of the four registrations, especially the ceftriaxone product.
- Merging of the duplicate glaucoma entries.
- For anaphylaxis, human clinical data on beta2 agonists as adjunctive therapy for bronchospasm, plus a safety review against the cardiovascular liabilities above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

