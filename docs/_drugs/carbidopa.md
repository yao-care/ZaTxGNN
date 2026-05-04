---
layout: default
title: Carbidopa
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
---

# Carbidopa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Carbidopa: From Parkinson's Disease to Rasmussen Subacute Encephalitis

---

## One-Sentence Summary

Carbidopa is a peripheral dopa decarboxylase inhibitor classically combined with levodopa to treat Parkinson's disease — it prevents the peripheral breakdown of levodopa, allowing more of it to reach the brain while reducing side effects such as nausea and cardiovascular dysregulation. The TxGNN model's top-ranked prediction suggests potential use in **Rasmussen Subacute Encephalitis**, with **no clinical trials and no publications** currently supporting this direction. Across all 10 predicted indications reviewed, the strongest evidence was found for **X-linked intellectual disability-ataxia-apraxia syndrome** (Evidence Level L3; Proceed with Guardrails), where two recent publications in *Movement Disorders* directly report Levodopa/Carbidopa treatment responses in a mechanistically overlapping disorder.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease (adjunct to levodopa) |
| Predicted New Indication (TxGNN Rank 1) | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 98.43% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Carbidopa is a selective peripheral aromatic L-amino acid decarboxylase (DOPA decarboxylase) inhibitor. Because it does not cross the blood-brain barrier, it acts exclusively outside the CNS to block the conversion of levodopa to dopamine in the periphery. In the standard levodopa/carbidopa combination, this raises levodopa bioavailability in the brain, reduces peripheral dopaminergic side effects (nausea, vomiting, hypotension), and allows lower total levodopa doses. Its mechanism of action is fundamentally linked to the dopaminergic system.

Rasmussen encephalitis, by contrast, is a progressive T-cell-mediated autoimmune encephalitis driven by cytotoxic lymphocytes and GluR3 (glutamate receptor 3) antibodies. The pathological hallmarks are unilateral cortical inflammation, pharmacoresistant focal epilepsy, and progressive hemiplegia. Primary dopaminergic neuron degeneration is not a feature of this disease, and no established pharmacological pathway connects DOPA decarboxylase inhibition to the immune-mediated mechanisms that drive Rasmussen encephalitis.

The 98.43% TxGNN score for this pairing most likely reflects topological proximity within the knowledge graph — neurological disease nodes share upstream classification nodes (e.g., "Encephalitis," "CNS disease") — rather than a genuine pharmacological link. This is a well-recognised limitation of graph-based machine learning methods applied to rare neuroimmune diseases, and the **Hold** recommendation is appropriate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Carbidopa in Rasmussen Subacute Encephalitis.

---

## Literature Evidence

Currently no related literature available for Carbidopa in Rasmussen Subacute Encephalitis.

---

## South Africa Market Information

Carbidopa is not currently registered with SAHPRA and is not marketed in South Africa as a standalone product. No SAHPRA licences are on record.

> **Note for prescribers**: Fixed-dose levodopa/carbidopa combination products (co-careldopa) may carry independent SAHPRA registration. Current SAHPRA status for combination formulations should be verified separately before any clinical application. Essential Medicines List (EML) inclusion for combination products should also be confirmed with the National Department of Health.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA via the MedSafety reporting system.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN top-ranked prediction linking Carbidopa to Rasmussen Subacute Encephalitis has no mechanistic plausibility and is entirely unsupported by clinical trials or published literature. This association almost certainly reflects a knowledge graph topology artefact and does not represent an actionable repurposing opportunity.

**To proceed, the following is needed:**
- A credible biological hypothesis linking peripheral DOPA decarboxylase inhibition to autoimmune encephalitis pathophysiology
- Preclinical evidence establishing any pharmacological interaction with GluR3-mediated or T-cell-mediated CNS inflammation
- Full SAHPRA PI review to document safety profile before any further evaluation

---

---

## Additional Predicted Indications — Summary and Prioritised Review

The TxGNN model generated 10 predicted indications for Carbidopa. While the top-ranked prediction (Rasmussen encephalitis) warrants a Hold decision, several lower-ranked predictions carry stronger dopaminergic mechanistic rationale and emerging clinical evidence. These are summarised below and expanded for the three most clinically relevant.

### All 10 TxGNN Predictions at a Glance

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation |
|------|-----------|:-----------:|:--------------:|:--------------:|
| 1 | Rasmussen Subacute Encephalitis | 98.43% | L5 | Hold |
| 2 | PLA2G6-Associated Neurodegeneration | 97.60% | L4 | Research Question |
| 3 | Transaldolase Deficiency | 97.40% | L5 | Hold |
| 4 | Myelitis | 97.40% | L5 | Hold |
| 5 | Fructose-1,6-Bisphosphatase Deficiency | 97.09% | L5 | Hold |
| 6 | Lewy Body Dementia | 95.99% | L3 | Research Question |
| 7 | Paralysis Agitans, Juvenile, of Hunt | 95.60% | L4 | Research Question |
| 8 | PSP-Corticobasal Syndrome | 95.36% | L4 | Research Question |
| **9** | **X-Linked ID-Ataxia-Apraxia Syndrome** | **94.87%** | **L3** | **Proceed with Guardrails** |
| 10 | X-Linked ID-Cerebellar Hypoplasia Syndrome | 93.72% | L4 | Research Question |

> **Hold indications explained**: Ranks 3 (transaldolase deficiency), 5 (fructose-1,6-bisphosphatase deficiency) involve carbohydrate metabolic disorders with no dopaminergic connection. Rank 4 (myelitis) involves inflammatory/demyelinating spinal cord injury — the retrieved literature is indirect (a dengue-induced parkinsonism case report and a post-polio selegiline case series, neither involving carbidopa directly or the target disease). These should not be pursued without new mechanistic hypotheses.

---

### Priority 1 — Rank 9: X-Linked Intellectual Disability-Ataxia-Apraxia Syndrome

**Decision: Proceed with Guardrails** | Evidence Level: L3 | TxGNN Score: 94.87%

#### Why Is This Prediction Reasonable?

This syndrome phenotypically overlaps with Allan-Herndon-Dudley Syndrome (AHDS), caused by loss-of-function variants in the monocarboxylate transporter 8 gene (*SLC16A2*, also known as MCT8). MCT8 is required for thyroid hormone (T3) transport across the blood-brain barrier. Its deficiency impairs brain T3 uptake during critical neurodevelopmental windows, leading to disrupted dopaminergic circuit maturation. The resulting dopamine metabolic abnormalities manifest as infantile and juvenile parkinsonism — rigidity, bradykinesia, dystonia, and ataxia — that are mechanistically analogous to idiopathic Parkinson's disease.

This is the strongest mechanistic-clinical link in the entire prediction set. Two 2025–2026 publications in *Movement Disorders* (the field's leading journal) directly document Levodopa/Carbidopa treatment responses in this overlapping population:

- **PMID 41144879 (2026)** directly reports altered dopamine metabolism *and* clinical treatment responses to Levodopa/Carbidopa in MCT8 deficiency patients, providing the most direct carbidopa-specific evidence in this dataset.
- **PMID 40088079 (2025)** reports a cohort of AHDS patients displaying childhood-onset parkinsonism that responds to Levodopa/Carbidopa treatment.

#### Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|:----:|------|---------|-------------|
| [41144879](https://pubmed.ncbi.nlm.nih.gov/41144879/) | 2026 | Case Report / Small Series | Movement Disorders | Documents altered dopamine metabolism and direct Levodopa/**Carbidopa** treatment response in MCT8 (SLC16A2) deficiency; dopaminergic circuit disruption confirmed as core pathophysiology |
| [40088079](https://pubmed.ncbi.nlm.nih.gov/40088079/) | 2025 | Observational Cohort / Case Series | Movement Disorders | AHDS patients present childhood-onset parkinsonism; trial of thyroid hormone derivatives failed; Levodopa/**Carbidopa** responses reported |
| [40767387](https://pubmed.ncbi.nlm.nih.gov/40767387/) | 2025 | Case Report | Am J Med Genet Part A | 30-year-old male with Basilicata-Akhtar syndrome (MSL3 variant): developmental delay, intellectual disability, motor disturbances — X-linked neurodevelopmental context |

#### Next Steps for Rank 9

- Prospective case series or international patient registry study of MCT8 deficiency / AHDS patients receiving Levodopa/Carbidopa, with standardised motor outcome measures
- Paediatric dosing and safety monitoring protocol, given the young patient population
- Engage rare disease networks (e.g., NBIA Research Alliance, EURO-RDI) for multi-centre data pooling
- Consider SAHPRA named-patient / compassionate use pathway if a South African patient presents with confirmed diagnosis

---

### Priority 2 — Rank 6: Lewy Body Dementia

**Decision: Research Question** | Evidence Level: L3 | TxGNN Score: 95.99%

#### Why Is This Prediction Reasonable?

Dementia with Lewy Bodies (DLB) shares core neuropathological features with Parkinson's disease: dopaminergic neuronal loss in the substantia nigra and nigrostriatal pathways, with widespread alpha-synuclein (Lewy body) inclusions. This substantial biological overlap provides direct mechanistic rationale for Levodopa/Carbidopa use to address motor symptoms. International DLB guidelines already acknowledge levodopa as a treatment option for parkinsonian motor features in DLB.

**Critical clinical caveat**: DLB patients exhibit extreme sensitivity to dopaminergic agents. Levodopa can precipitate or worsen hallucinations and neuropsychiatric symptoms, which are a defining feature of DLB. Clinical use requires a careful individual benefit-risk assessment, low starting doses, and close psychiatric monitoring. The available clinical trial (NCT04246437) is a Phase 1 [18F]F-DOPA PET imaging study — it validates the dopaminergic deficit as a molecular target but does not provide therapeutic efficacy data for Carbidopa.

#### Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|:-----:|:------:|:---------:|-------------|
| [NCT04246437](https://clinicaltrials.gov/study/NCT04246437) | Phase 1 | Recruiting | 40 | [18F]F-DOPA PET imaging in autonomic failure/alpha-synucleinopathies including DLB; confirms dopaminergic deficits as a molecular biomarker — this is an imaging study, not a therapeutic efficacy trial |

---

### Priority 3 — Rank 2: PLA2G6-Associated Neurodegeneration (PLAN)

**Decision: Research Question** | Evidence Level: L4 | TxGNN Score: 97.60%

#### Why Is This Prediction Reasonable?

PLAN belongs to the NBIA (Neurodegeneration with Brain Iron Accumulation) family, caused by *PLA2G6* mutations affecting phospholipid remodelling and mitochondrial membrane integrity. Adult-onset PLAN frequently presents with a Parkinson-like phenotype — rigidity, bradykinesia, focal dystonia, and cerebellar atrophy — due to dopaminergic neuronal loss, particularly in the substantia nigra. PMID 41769496 (2026) directly describes adult-onset PLA2G6-associated parkinsonism, supporting dopaminergic pathway involvement. The mechanistic basis for a therapeutic trial of Levodopa/Carbidopa is reasonable, though PLAN typically shows modest and declining levodopa responsiveness over time.

#### Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|:----:|------|---------|-------------|
| [41769496](https://pubmed.ncbi.nlm.nih.gov/41769496/) | 2026 | Case Report | Cureus | Adult male with rapidly progressive PLA2G6-associated parkinsonism, spastic rigidity, dystonia, and cognitive decline; clinical presentation directly supports dopaminergic hypothesis |
| [24368176](https://pubmed.ncbi.nlm.nih.gov/24368176/) | 2014 | Case Series | Parkinsonism & Related Disorders | NBIA subtype characterisation (including BPAN/SENDA); extrapyramidal features and intellectual deterioration across NBIA spectrum documented |
| [8439265](https://pubmed.ncbi.nlm.nih.gov/8439265/) | 1993 | Rehabilitation Study | Arch Phys Med Rehabil | Historic NBIA (Hallervorden-Spatz/PKAN) rehabilitation report; early characterisation of corticospinal and extrapyramidal features |

---

### Additional Notes — Ranks 7 and 8

**Rank 7 — Paralysis Agitans, Juvenile, of Hunt (Research Question; L4):** Hunt's juvenile paralysis agitans is an early-onset dopaminergic degeneration syndrome with high mechanistic similarity to adult Parkinson's disease. The mechanistic external validity for Levodopa/Carbidopa is strong, but the indication is so rare that no clinical trials or disease-specific publications were identified. This is a reasonable research question for rare disease specialists.

**Rank 8 — PSP-Corticobasal Syndrome (Research Question; L4):** PSP-CBS is a 4R-tauopathy. Unlike Parkinson's disease, postsynaptic striatal neurons are also degenerated, resulting in a levodopa response rate below 20%. Levodopa/Carbidopa appears in clinical guidelines as a time-limited therapeutic trial, but the likelihood of meaningful benefit is low. The available trial (NCT02994719) is an observational gait analysis study — it characterises the motor phenotype but provides no therapeutic efficacy data.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|:-----:|:------:|:---------:|-------------|
| [NCT02994719](https://clinicaltrials.gov/study/NCT02994719) | N/A | Recruiting | 120 | Observational gait analysis in parkinsonian disorders including PSP; motor phenotype characterisation only — not a Carbidopa therapeutic trial |

---

> **Disclaimer**: This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Safety information should be verified against the SAHPRA-approved Professional Information (PI). Adverse events should be reported to SAHPRA via the MedSafety reporting system.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

