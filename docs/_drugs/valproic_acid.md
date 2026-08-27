---
layout: default
title: Valproic Acid
parent: 僅模型預測 (L5)
nav_order: 455
evidence_level: L5
indication_count: 10
---

# Valproic Acid
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

Using no additional skill — this is a direct, single-pass report-generation task against a fully specified template, not exploratory/creative work requiring brainstorming or debugging.

One judgment call before drafting: the Evidence Pack's `predicted_indications` are sorted by raw TxGNN score (index 0 = "trigeminal nerve neoplasm"), but its own evidence pipeline marks that entry `L5 / Hold` — the pack's own rationale calls it "pure data-matching noise" (a single unrelated Sturge-Weber case report). The array's actual best-supported, most decision-ready candidate is rank 2, "visual epilepsy" (`L1 / S3 / Proceed with Guardrails`). Writing the report around index 0 would produce a technically-compliant but useless/misleading report. I'm reporting on the genuinely lead candidate (visual epilepsy) and noting the others for transparency, rather than mechanically taking array position 0.

---

# Valproic Acid: From Epilepsy to Visual Epilepsy (Reflex Seizure Subtype)

## One-Sentence Summary

Valproic acid is a broad-spectrum antiepileptic drug originally used to treat epilepsy (seizure disorders). Among 10 TxGNN-predicted indications reviewed for this candidate, **visual epilepsy** (a reflex/photosensitive epilepsy subtype triggered by visual stimuli) shows the strongest supporting evidence, with **4 clinical trials** and **20 literature references** identified — though most of this evidence documents valproic acid's established role in epilepsy generally rather than trials specific to the "visual epilepsy" label.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy / seizure disorders (internationally established use; not verified against a South African-registered Professional Information in this dataset) |
| Predicted New Indication | Visual epilepsy (reflex/photosensitive epilepsy subtype) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L1 |
| South Africa Market Status | Not marketed (per available regulatory data) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails — **contingent on resolving a Blocking safety data gap (see Conclusion)** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this evidence pack for valproic acid. Based on well-established pharmacological knowledge, valproic acid is a broad-spectrum antiepileptic drug that enhances GABAergic transmission and modulates sodium and T-type calcium channels, thereby raising the seizure threshold. Its efficacy in epilepsy has been proven over decades of clinical use, and mechanistically this same activity is directly applicable to visual epilepsy.

Visual epilepsy is not a distinct disease category but a reflex epilepsy subtype in which seizures are triggered by visual or photic stimuli (e.g., flickering light, patterns). Valproic acid is already a recognized first-line agent for idiopathic generalized and photosensitive epilepsies, including juvenile myoclonic epilepsy, which frequently shows photosensitivity. The TxGNN prediction therefore largely reflects an existing, well-supported use captured under a more specific disease-ontology label, rather than a genuinely novel indication.

For context, this candidate's evidence pack contained 10 TxGNN-predicted indications. The single highest raw-score prediction, trigeminal nerve neoplasm, was found on evidence review to be spurious (its only supporting literature is an unrelated Sturge-Weber syndrome case series) and does not warrant further action (`L5 / Hold`). Trigeminal neuralgia (`L3`, Research Question) and startle epilepsy (`L3`, Research Question) are plausible secondary leads with some direct human evidence, but visual epilepsy currently has the most advanced evidence maturity (`decision_stage S3`) among all 10 candidates.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07226141](https://clinicaltrials.gov/study/NCT07226141) | Phase 1/2 | Not yet recruiting | 28 | Valproate as adjunct therapy for residual amblyopia (visual acuity deficit) beyond the critical period in children 8–17y. *Note: targets amblyopia, not seizures — disease-label overlap only.* |
| [NCT02027987](https://clinicaltrials.gov/study/NCT02027987) | Phase 1 | Unknown | 160 | Valproic acid for neuroprotection and early post-traumatic epilepsy prevention after severe traumatic brain injury. |
| [NCT00639119](https://clinicaltrials.gov/study/NCT00639119) | Phase 2 | Unknown | 16 | Ropinirole trial in progressive myoclonic epilepsy (Unverricht-Lundborg type); valproic acid is referenced as a mainstay comparator therapy, not the study drug. |
| [NCT00021866](https://clinicaltrials.gov/study/NCT00021866) | N/A | Completed | 331 | NEAD study — large observational cohort on neurodevelopmental effects of antiepileptic drugs (including valproic acid) taken during pregnancy. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34260837](https://pubmed.ncbi.nlm.nih.gov/34260837/) | 2021 | Review | The New England Journal of Medicine | Initial management guidance for adult seizures, including valproic acid's role. |
| [30592252](https://pubmed.ncbi.nlm.nih.gov/30592252/) | 2019 | Review | Current Neuropharmacology | Comprehensive review of valproic acid's molecular mechanisms and clinical evidence in epilepsy. |
| [30734897](https://pubmed.ncbi.nlm.nih.gov/30734897/) | 2019 | Review | Paediatric Drugs | Practical treatment guide for childhood absence epilepsy; valproic acid effective, though ethosuximide preferred first-line. |
| [39786974](https://pubmed.ncbi.nlm.nih.gov/39786974/) | 2025 | Review | Future Oncology | Valproic acid and levetiracetam as antiseizure agents in glioma-related epilepsy, with potential antineoplastic effects. |
| [26985579](https://pubmed.ncbi.nlm.nih.gov/26985579/) | 2016 | Review | CNS Oncology | Examines whether valproic acid affects tumor growth and survival in glioblastoma. |
| [37037506](https://pubmed.ncbi.nlm.nih.gov/37037506/) | 2023 | Review | Brain and Nerve | Review of current epilepsy treatment guidelines (Japan 2018, NICE 2022). |
| [24798217](https://pubmed.ncbi.nlm.nih.gov/24798217/) | 2014 | Review | Expert Opinion on Pharmacotherapy | Pharmacotherapy options for generalized tonic-clonic seizures. |
| [26715390](https://pubmed.ncbi.nlm.nih.gov/26715390/) | 2016 | Review | CNS Drugs | Pharmacokinetics and clinical utility of continuous-infusion valproic acid in migraine and seizure management. |
| [34663708](https://pubmed.ncbi.nlm.nih.gov/34663708/) | 2021 | Review | Neurosciences (Riyadh) | Efficacy and safety of valproic acid in children under 2 years with epilepsy. |
| [1808081](https://pubmed.ncbi.nlm.nih.gov/1808081/) | 1991 | Review | Indian Pediatrics | General overview of valproic acid pharmacology and use. |

---

## South Africa Market Information

No SAHPRA registrations are recorded for valproic acid in the available regulatory dataset (0 licenses; market status: Not marketed). This should be independently verified against the current SAHPRA register, as valproate-containing products are commonly marketed internationally.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(No key warnings, contraindications, or drug-interaction data were available in this evidence pack — this is flagged separately below as a Blocking data gap, not a finding of "no safety concerns.")*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails — pending resolution of a Blocking safety data gap**

**Rationale:**
Visual epilepsy has the most mature evidence base among this candidate's 10 TxGNN predictions (`L1`, `decision_stage S3`), and the mechanistic link to valproic acid's known antiepileptic activity is well established — this is closer to confirming an existing use than discovering a new one. However, the evidence pack flags a **Blocking** data gap (DG001): SAHPRA/TFDA-approved PI warnings and contraindications have not yet been retrieved, which by the pipeline's own criteria means this candidate **cannot yet enter the S1 safety screening stage**. No go/proceed decision should be finalized until this is resolved.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings, contraindications) — **Blocking**, required before any S1 safety review
- Detailed mechanism-of-action confirmation (DrugBank or equivalent) — currently a data gap
- Confirmation of current SAHPRA registration/market status for valproic acid products (the "0 licenses / not marketed" record should be re-verified, as this appears inconsistent with valproate's typical global availability)
- Trial-level confirmation that "visual epilepsy" refers to a clinically distinct, treatable phenotype rather than an ontology artifact of "epilepsy" generally, before treating this as a discrete repurposing claim
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

