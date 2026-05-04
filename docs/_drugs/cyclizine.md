---
layout: default
title: Cyclizine
parent: 僅模型預測 (L5)
nav_order: 151
evidence_level: L5
indication_count: 10
---

# Cyclizine
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

# Cyclizine: From Antiemetic/Antihistamine to Allergic Urticaria

## One-Sentence Summary

Cyclizine is a first-generation H1 antihistamine and piperazine derivative, traditionally used as an antiemetic for motion sickness, postoperative nausea, and vomiting. The TxGNN model predicts it may be effective for **Allergic Urticaria**, with **0 clinical trials** and **1 publication** currently supporting this specific direction. However, the mechanistic rationale is strong given that H1 antihistamines are the established first-line treatment for urticaria.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antiemetic (motion sickness, postoperative nausea and vomiting) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 — Preclinical / mechanism-based studies |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Cyclizine is a first-generation piperazine-class H1 receptor antagonist with additional anticholinergic (muscarinic) properties. It is best known internationally as an antiemetic — used to prevent and treat motion sickness, postoperative nausea and vomiting, and drug-induced nausea. In the UK, it is available over the counter (e.g., Valoid®) and is a component of the combination product Migraleve® (with paracetamol and codeine) for migraine. Its antiemetic action is mediated through H1 blockade in the vomiting centre and vestibular nuclei, as well as muscarinic receptor antagonism.

The core pathophysiology of allergic urticaria involves mast cell degranulation, leading to histamine release that activates H1 receptors on endothelial cells and sensory nerve endings. This produces the characteristic triad of vasodilatation (erythema), increased vascular permeability (wheals), and pruritus. H1 antihistamines are the universally recognised first-line treatment for urticaria, as endorsed by international guidelines including the EAACI/GA²LEN/EDF/WAO guidelines. Since cyclizine directly blocks the H1 receptor — the same pharmacological target addressed by cetirizine, loratadine, and other established urticaria treatments — the mechanistic link is very strong.

The principal limitation is that cyclizine is a first-generation (sedating) antihistamine with significant anticholinergic side effects (drowsiness, dry mouth, blurred vision, urinary retention). Current clinical guidelines universally recommend second-generation non-sedating antihistamines (cetirizine, loratadine, fexofenadine) as first-line therapy due to their superior safety and tolerability profiles. This means cyclizine, while mechanistically sound, would face a competitive disadvantage against well-established alternatives unless a specific clinical niche (e.g., urticaria with concurrent nausea/vomiting, or settings where second-generation agents are unavailable) can be identified.

## Clinical Trial Evidence

Currently no related clinical trials registered on ClinicalTrials.gov, ICTRP, SANCTR, or PACTR for cyclizine in allergic urticaria.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8573923](https://pubmed.ncbi.nlm.nih.gov/8573923/) | 1995 | Case series | Dermatology (Basel) | Investigated action, inhibition, and augmentation spectra in solar urticaria. Demonstrated that light spectra outside activating wavelengths can influence wheal formation. Indirectly relevant to understanding urticaria pathophysiology. |

## South Africa Market Information

Cyclizine is **not currently registered with SAHPRA** and has no approved products on the South African market. There are no SAHPRA registration numbers to report.

> **Note:** Cyclizine is widely available in the UK (Valoid® 50 mg tablets, Valoid® 50 mg/mL injection), Ireland, Australia, and New Zealand. Its absence from the South African market means that any repurposing initiative would first require SAHPRA registration or Section 21 importation authorisation.

## Safety Considerations

Detailed SAHPRA-approved Professional Information (PI) is not available as cyclizine is not registered in South Africa. Based on international product information:

- **Key Warnings**: Cyclizine may cause drowsiness and impair the ability to drive or operate machinery. It has anticholinergic properties and should be used with caution in patients with angle-closure glaucoma, prostatic hypertrophy, pyloric stenosis, or urinary retention. Avoid in severe heart failure (intravenous cyclizine may cause a fall in cardiac output).
- **Contraindications**: Hypersensitivity to cyclizine or any excipients. Caution in porphyria.
- **Drug Interactions**: Enhanced sedation with CNS depressants (opioids, benzodiazepines, alcohol). Anticholinergic effects may be additive with other anticholinergic medicines (tricyclic antidepressants, phenothiazines). May counteract the prokinetic effects of metoclopramide and domperidone.

> Report adverse drug reactions to SAHPRA via the national ADR reporting system.

## Additional Predicted Indications of Note

The TxGNN model identified 10 candidate indications for cyclizine. Beyond allergic urticaria, two additional predictions warrant brief mention:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|----------------|----------------|
| 1 | Allergic Urticaria | 99.98% | L4 | Proceed with Guardrails |
| 4 | Cold Urticaria | 99.84% | L5 | Research Question |
| 6 | Headache Disorder | 99.49% | L3 | Proceed with Guardrails |
| 8 | Rhinitis | 99.35% | L5 | Research Question |

**Headache Disorder (Rank 6)** is notable because cyclizine is already used in the UK as a component of Migraleve® (cyclizine 50 mg + paracetamol 500 mg + codeine 8 mg) for migraine. This indication has the strongest real-world evidence among all predictions, with **5 publications** including comparative clinical trials:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3926322](https://pubmed.ncbi.nlm.nih.gov/3926322/) | 1985 | Comparative clinical trial | Cephalalgia | Compared naproxen sodium vs. an ergotamine combination containing cyclizine 50 mg for acute migraine attack in 114 patients. |
| [4148490](https://pubmed.ncbi.nlm.nih.gov/4148490/) | 1973 | Clinical trial | The Practitioner | Migraine treated with an antihistamine-analgesic combination containing cyclizine. |
| [20420788](https://pubmed.ncbi.nlm.nih.gov/20420788/) | 2010 | Pharmacoepidemiology | Int J Clin Pharmacol Ther | Prescribing patterns for migraine, including analysis of triptan usage in primary care. |
| [11472386](https://pubmed.ncbi.nlm.nih.gov/11472386/) | 2001 | Pharmacoepidemiology | Cephalalgia | Patterns of ergotamine and sumatriptan use in the Netherlands (1991–1997). |
| [10842162](https://pubmed.ncbi.nlm.nih.gov/10842162/) | 2000 | Case report | J Vasc Surg | Chronic ergot toxicity from long-term use of ergotamine-containing migraine combinations. |

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between cyclizine (H1 receptor antagonist) and allergic urticaria is scientifically robust — H1 antihistamines are the established standard of care for urticaria. However, cyclizine's first-generation profile (sedation, anticholinergic effects) places it at a competitive disadvantage relative to second-generation antihistamines already available in South Africa. The drug is not currently SAHPRA-registered, adding a significant regulatory barrier. This candidate is best pursued only if a specific unmet need or niche clinical scenario is identified.

**To proceed, the following is needed:**
- **Regulatory pathway assessment**: Determine feasibility and timeline for SAHPRA registration or Section 21 access
- **Mechanism of action data**: Obtain detailed MOA from DrugBank to support mechanistic dossier
- **Competitive landscape analysis**: Compare cyclizine to second-generation H1 antihistamines (cetirizine, loratadine, fexofenadine) already registered in South Africa for urticaria
- **Safety dossier**: Obtain full Professional Information from international regulators (UK MHRA, Australian TGA) for safety assessment
- **Clinical justification**: Identify specific clinical scenarios where cyclizine may offer advantages over existing alternatives (e.g., concurrent nausea/vomiting with urticaria, resource-limited settings)
- **Cost-effectiveness study**: Assess whether cyclizine offers any pharmacoeconomic advantage in the South African healthcare context

---

*Disclaimer: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. Data cutoff: 2026-04-05.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

