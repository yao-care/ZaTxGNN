---
layout: default
title: Cocaine
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
---

# Cocaine
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

# Cocaine: From Local Anaesthetic to Cauda Equina Syndrome

---

## One-Sentence Summary

Cocaine (DB00907) is a tropane alkaloid historically employed as a topical local anaesthetic and vasoconstrictor in ENT and ophthalmic surgical procedures — though it carries **no current SAHPRA-approved therapeutic indication** and is not marketed in South Africa.
The TxGNN model predicts it may have relevance for **Cauda Equina Syndrome**, yet this is supported by **no clinical trials** and only **1 case report** — one that describes the condition itself, not cocaine as a treatment.
Given the complete absence of mechanistic evidence, zero registered trials, and the drug's Schedule 7 controlled substance status, a **Hold** decision is strongly recommended across all predicted indications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No SAHPRA-approved indication (cocaine is not registered in South Africa) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved from DrugBank for this Evidence Pack. Based on established pharmacology, cocaine is a tropane alkaloid acting via two primary mechanisms: (1) **blockade of voltage-gated sodium channels**, producing topical local anaesthesia and vasoconstriction; and (2) **inhibition of presynaptic monoamine reuptake transporters** (norepinephrine, dopamine, serotonin), producing sympathomimetic and psychostimulant effects. It was historically the first clinically used local anaesthetic, introduced in the late 19th century for ENT and ophthalmic procedures.

Cauda equina syndrome (CES) is a neurological emergency arising from acute mechanical compression of the cauda equina nerve roots — most commonly by a large central lumbar disc herniation, epidural haematoma, or tumour. Its hallmark presentation includes urinary retention or incontinence, faecal incontinence, saddle-area sensory loss, and bilateral lower limb weakness. Definitive treatment is emergency surgical decompression, and delays beyond 48 hours are associated with permanent neurological deficit.

**There is no established mechanistic connection between cocaine's sodium channel blockade or monoamine reuptake inhibition and the pathophysiology of CES.** CES is a structural-mechanical emergency requiring surgical intervention, not anaesthetic or sympathomimetic pharmacotherapy. The TxGNN model's high score of 99.98% reflects knowledge graph topology — likely indirect network proximity — rather than a validated biological relationship. This prediction is assessed as a graph artefact rather than a clinically meaningful repurposing signal. Notably, all 10 top-ranked TxGNN predictions for cocaine received a **Hold** recommendation, reflecting a broader pattern of weak mechanistic grounding across the entire candidate list.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31528422](https://pubmed.ncbi.nlm.nih.gov/31528422/) | 2019 | Case Report | Surgical Neurology International | Case report of distal CES from lumbosacral disc pathology in a single patient; reviews the protean symptomatology of CES including urinary incontinence, saddle hypoaesthesia, and lower extremity weakness. Cocaine is not involved as a treatment agent. |

> **Note:** The sole literature item identified describes CES as a clinical condition and has no connection to cocaine as a therapy. This confirms the **L5** evidence rating — model prediction only, with no supporting clinical or preclinical studies.

---

## South Africa Market Information

Cocaine is **not registered with SAHPRA** and is not available as a pharmaceutical product in South Africa. Under the Drugs and Drug Trafficking Act 140 of 1992, cocaine is classified as a **Schedule 7 undesirable dependence-producing substance** — the most restrictive controlled category. It does not appear on the Essential Medicines List (EML).

No SAHPRA product licences exist, and no Section 21 (unregistered medicine) authorisation records appear in this dataset. Any clinical or research use of cocaine — including investigational repurposing studies — would require explicit authorisation from SAHPRA under both the Medicines and Related Substances Act 101 of 1965 (as amended) and applicable controlled substance legislation, and would be subject to rigorous ethics committee review.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for complete safety information. Report adverse drug reactions to SAHPRA via the MedSafety online portal.

> **Important context for prescribers and investigators:** Cocaine carries a well-characterised and serious toxicity profile. Key concerns include coronary artery spasm and myocardial infarction (even in patients without pre-existing cardiovascular disease), life-threatening arrhythmias, cerebrovascular events, seizures, and profound psychological dependence. Its vasoconstrictor effects cause ischaemic mucosal and tissue necrosis with chronic use. There is no established therapeutic window for systemic administration. These risks represent fundamental barriers to repurposing development and must be addressed before any clinical investigation is contemplated.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no mechanistic basis linking cocaine's pharmacological actions to cauda equina syndrome — a surgical emergency requiring spinal decompression rather than pharmacological management. The combination of zero supporting clinical trials, one non-relevant case report, no SAHPRA registration, Schedule 7 controlled substance status, and a well-documented serious toxicity profile makes this prediction unsuitable for further repurposing development at this time.

**To proceed, the following would be required:**

- A biologically plausible mechanistic hypothesis specifically connecting cocaine's sodium channel blockade or monoamine reuptake inhibition to CES pathophysiology
- Preclinical data (animal spinal compression models) demonstrating a measurable therapeutic benefit
- Full MOA and safety data retrieval from DrugBank (currently a data gap — see DG001 and DG002)
- Formal regulatory pathway assessment with SAHPRA for Schedule 7 controlled substance research use
- Ethics committee approval prior to any investigational human use
- Comparative analysis against established and safer alternatives for any overlapping indication

---

> ⚠️ **Research Disclaimer:** This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require rigorous clinical validation before therapeutic application. Cocaine is a Schedule 7 controlled substance in South Africa; its possession, manufacture, or supply outside of authorised regulatory channels is a criminal offence. This content complies with YMYL standards for medical information.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

