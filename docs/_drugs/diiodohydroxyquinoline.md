---
layout: default
title: Diiodohydroxyquinoline
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 10
---

# Diiodohydroxyquinoline
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

# Diiodohydroxyquinoline: From Intestinal Amebiasis to Osteoradionecrosis

## One-Sentence Summary

Diiodohydroxyquinoline (also known as iodoquinol) is a halogenated hydroxyquinoline antiprotozoal compound historically used as a luminal amebicide for intestinal amebiasis, though it holds no current SAHPRA registration in South Africa.
The TxGNN model predicts it may be effective for **Osteoradionecrosis** (radiation-induced bone necrosis), achieving a prediction score of **97.96%**.
However, **no clinical trials** and **no publications** directly supporting this specific indication have been identified; all evidence currently remains at model-prediction level only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered with SAHPRA (historically: intestinal amebiasis) |
| Predicted New Indication | Osteoradionecrosis |
| TxGNN Prediction Score | 97.96% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacological information, diiodohydroxyquinoline belongs to the halogenated 8-hydroxyquinoline class. Its established clinical use has been in the treatment of intestinal amebiasis, where it acts as a luminal amebicide — meaning it exerts its antiprotozoal effect directly within the gastrointestinal tract rather than systemically.

The 8-hydroxyquinoline scaffold is known to possess metal-chelating properties, particularly toward divalent metals such as Zn²⁺ and Fe²⁺. The TxGNN prediction for osteoradionecrosis may stem from this property: theoretically, disruption of redox homeostasis through metal chelation could conceivably influence the pathological microenvironment of radiation-induced bone necrosis, where oxidative stress plays a contributing role.

However, this mechanistic link is highly speculative. The core pathophysiology of osteoradionecrosis involves radiation-induced ischaemia, hypoxia, and an imbalance between osteoclast and osteoblast activity — none of which have an established or documented connection to the known mechanisms of quinoline-class drugs. The prediction most likely reflects topological proximity within the TxGNN knowledge graph rather than a direct mechanistic relationship, and should be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for osteoradionecrosis.

> **Note:** A PubMed search for diiodohydroxyquinoline and the third-ranked indication (pneumonitis) did return 4 publications; however, all 4 describe amebiasis cases where pneumonia/pleurisy appeared as a complication of hepatic amebiasis — not direct evidence of the drug treating pneumonitis. These publications do not support repurposing for any of the predicted indications.

---

## South Africa Market Information

Diiodohydroxyquinoline is **not registered with SAHPRA** and is not marketed in South Africa. No product licences are on record.

If prescribers wish to use an unregistered medicine, this would require a Section 21 application to SAHPRA (Medicines and Related Substances Act, 101 of 1965, as amended). The drug is also not listed on the Essential Medicines List (EML) for South Africa.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. As this drug is not currently registered in South Africa, prescribers should consult international reference sources (e.g., the FDA-approved label, British National Formulary, or WHO Model Formulary). Report adverse drug reactions to SAHPRA at [www.sahpra.org.za](https://www.sahpra.org.za).

> **Important known class-level concern:** Higher-dose or prolonged use of halogenated hydroxyquinolines (the drug class to which diiodohydroxyquinoline belongs) has been associated with subacute myelo-optic neuropathy (SMON). This is a serious neurological adverse effect documented with related compounds. This risk must be factored into any safety assessment before clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications are rated L5 — model prediction only — with zero supporting clinical trials or directly relevant publications identified across any indication. The top prediction (osteoradionecrosis) has no evidence base whatsoever, and the mechanistic link between diiodohydroxyquinoline's known properties and radiation-induced bone necrosis pathophysiology is highly speculative. Additionally, the drug has no SAHPRA registration and a known serious class-level safety concern (SMON risk with halogenated hydroxyquinolines), making any forward movement premature.

**To proceed, the following is needed:**

- **MOA clarification:** Obtain formal mechanism of action data from DrugBank (DB09115) or peer-reviewed pharmacology literature to confirm whether the 8-hydroxyquinoline metal-chelating properties have any biologically plausible relevance to the predicted indications
- **Preclinical evidence:** Any in vitro or animal model data demonstrating activity in osteoradionecrosis, radiodermatitis, or related conditions would be required before human studies are considered
- **Safety dossier:** Compile full safety data including SMON risk characterisation, contraindications, and drug-drug interactions before any clinical evaluation
- **Regulatory pathway:** If preclinical evidence supports progression, a Section 21 application to SAHPRA would be required for any South African clinical study or compassionate use
- **SAHPRA consultation:** Given the unregistered status and known class safety signals, early engagement with SAHPRA is strongly recommended before initiating any clinical research programme

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. This report has been prepared to support South African healthcare professionals in evaluating TxGNN model predictions and does not represent a SAHPRA regulatory assessment.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

