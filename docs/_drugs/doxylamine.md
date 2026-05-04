---
layout: default
title: Doxylamine
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 4
---

# Doxylamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using the `txgnn-pipeline` skill to confirm context. Now generating the South African drug repurposing evaluation report from the provided Evidence Pack.

---

# Doxylamine: From OTC Sleep Aid to Allergic Urticaria

## One-Sentence Summary

Doxylamine is a first-generation H1 antihistamine used internationally as an over-the-counter sleep aid and, in combination with pyridoxine, for nausea and vomiting of pregnancy — it currently holds **no SAHPRA registration** in South Africa.
The TxGNN model predicts it may be effective for **Allergic Urticaria**, with a mechanistic rationale firmly grounded in its H1-blocking action — the very pharmacological class used as first-line therapy for urticaria.
This prediction is supported by **no clinical trials** and **no peer-reviewed literature** specific to doxylamine in this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No SAHPRA-approved indication (not registered in South Africa) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Doxylamine is a first-generation H1 receptor antagonist belonging to the ethanolamine class of antihistamines. By competitively and reversibly blocking H1 receptors on endothelial cells and sensory nerve endings, it directly prevents histamine from triggering vasodilation, increased vascular permeability, and itch — the three core pathological events driving allergic urticaria (hives). This places doxylamine squarely within the pharmacological class that international guidelines (EAACI/GA²LEN, World Allergy Organization) already recommend as first-line therapy for urticaria.

The TxGNN prediction therefore reflects a strong **class-effect rationale** rather than a novel mechanistic discovery. H1 antihistamines are established, guideline-endorsed treatments for allergic urticaria, and doxylamine belongs to this class. The high prediction score (99.85%) is consistent with TxGNN's knowledge graph capturing the well-established "H1 antagonism → histamine-driven urticaria" pharmacological relationship.

However, a critical clinical limitation must be clearly stated: doxylamine is a **first-generation** antihistamine with pronounced central nervous system penetration, causing marked sedation. Current clinical practice strongly favours **second-generation**, non-sedating H1 antihistamines (cetirizine, loratadine, fexofenadine, bilastine) for allergic urticaria — these agents provide equivalent histamine blockade with substantially better tolerability and no impairment of daily functioning. Any further development of doxylamine for this indication must demonstrate a specific clinical advantage over second-generation alternatives.

---

## Clinical Trial Evidence

Currently no clinical trials of doxylamine specifically for allergic urticaria are registered on ClinicalTrials.gov, WHO ICTRP, SANCTR (South African National Clinical Trials Register), or PACTR (Pan African Clinical Trials Registry).

---

## Literature Evidence

Currently no peer-reviewed literature specifically evaluating doxylamine for allergic urticaria is available in PubMed.

---

## South Africa Market Information

Doxylamine holds **no current SAHPRA registrations** in South Africa and is not marketed domestically. There are no approved product licences to list.

Prescribers wishing to access doxylamine in South Africa would need to consider the **Section 21 (unregistered medicines) pathway** under the Medicines and Related Substances Act (Act 101 of 1965, as amended), or determine whether any internationally registered combination products (e.g. doxylamine succinate + pyridoxine hydrochloride for pregnancy nausea) could serve as a regulatory bridging reference.

---

## Safety Considerations

Doxylamine is not registered in South Africa and no SAHPRA-approved Professional Information (PI) is available. Based on its pharmacological classification as a first-generation H1 antihistamine (ethanolamine class), the following class-level safety considerations apply:

- **Key Warnings**: Significant CNS sedation — impairs driving ability, psychomotor performance, and reaction time. Patients must be warned not to drive or operate machinery. Risk of additive CNS depression is substantial when combined with alcohol, opioids, benzodiazepines, or other sedating agents.
- **Anticholinergic Effects**: Dry mouth, urinary retention (exercise caution in patients with benign prostatic hyperplasia), constipation, blurred vision, and risk of precipitating acute closed-angle glaucoma.
- **Drug Interactions**: Additive CNS depression with alcohol, opioids, benzodiazepines, and other CNS depressants; potentiation of anticholinergic effects with tricyclic antidepressants, bladder antimuscarinics, and other anticholinergic agents; concurrent use with MAO inhibitors is contraindicated.
- **Contraindications (class-level)**: Concurrent MAO inhibitor use; closed-angle glaucoma; symptomatic benign prostatic hyperplasia; neonates and premature infants.
- **Special Populations**: Use during breastfeeding is not recommended due to sedation risk in the infant. Risk–benefit assessment is required for use in pregnancy outside of the approved pyridoxine combination context.

Please report any adverse drug reactions to **SAHPRA** via the [MedSafety reporting system](https://www.sahpra.org.za/).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Doxylamine's mechanism of action as an H1 receptor antagonist is directly aligned with the pathophysiology of allergic urticaria, and the H1 antihistamine class represents established first-line therapy for this condition — the TxGNN prediction is mechanistically coherent and pharmacologically defensible. However, doxylamine carries no SAHPRA registration, no direct clinical trial data for urticaria, and faces a significant competitive disadvantage against second-generation antihistamines in standard clinical practice; a clearly defined and justified clinical use-case is required before investment in further development.

**To proceed, the following is needed:**

- Conduct a systematic literature review to confirm the absence of doxylamine-specific urticaria studies, including non-English language and grey literature sources
- Define a specific clinical niche where doxylamine's sedating properties may confer an advantage — for example, **nocturnal urticaria** requiring concurrent sleep aid, or resource-limited settings where second-generation agents are unavailable or cost-prohibitive
- Obtain the complete international SmPC or equivalent safety document (e.g. US FDA label, EMA PI) to establish a full contraindication and interaction profile prior to any clinical use
- Retrieve full mechanism of action (MOA) data from DrugBank (DB00366) to support the mechanistic section of any regulatory dossier
- If pursuing South African market access: initiate a SAHPRA Section 21 application for specific patient access, or evaluate requirements for a full product registration dossier
- Commission or identify a comparative tolerability study vs. cetirizine or loratadine if seeking a formal urticaria indication, as regulators will require evidence of clinical benefit over the established standard of care
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

