---
layout: default
title: Acyclovir
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 10
---

# Acyclovir
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

# Acyclovir: From Herpes Virus Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Acyclovir is a well-established antiviral nucleoside analogue with proven global efficacy against herpes simplex virus (HSV) and varicella-zoster virus (VZV) infections, though it holds no current SAHPRA registration in South Africa.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis (PEK)**, with **0 clinical trials** and **2 case series publications** currently supporting this specific direction — the high prediction score almost certainly reflects the close knowledge-graph relationship between HSV keratitis and PEK rather than direct evidence for this indication.
Given the absence of direct clinical evidence and the drug's lack of SAHPRA registration, this indication carries a **Hold** recommendation pending further investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No SAHPRA-registered indications available; Acyclovir is internationally established for HSV-1, HSV-2, and VZV infections |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the formal evidence record for this evaluation. Based on well-established pharmacological knowledge, Acyclovir is an acyclic guanosine nucleoside analogue whose antiviral activity depends on selective phosphorylation by herpes virus-specific thymidine kinase (TK). This confers high selectivity for HSV-1, HSV-2, and VZV. Acyclovir ophthalmic ointment is a globally recognised treatment for herpetic keratitis, which provides indirect mechanistic support for any prediction involving herpetic ocular disease.

Punctate epithelial keratoconjunctivitis (PEK) is a non-specific pattern of diffuse corneal surface inflammation, characterised by multiple fine epithelial erosions visible on slit-lamp examination with fluorescein staining. HSV-1 is one recognised cause: it can present as PEK during the early or recurrent phase of herpetic keratitis. The TxGNN model's high score (99.67%) most likely arises from the close proximity of HSV keratitis and PEK nodes in the medical knowledge graph — since Acyclovir treats HSV keratitis (which can clinically manifest as PEK), the model infers a treatment relationship for PEK as a disease entity.

It is critical to recognise, however, that PEK is aetiologically heterogeneous. Common causes include adenoviral infection, dry eye disease, contact lens toxicity, exposure keratopathy, and other drug-induced corneal surface damage. The two supporting publications in this evidence pack address drug-induced corneal lipidosis and microsporidial keratoconjunctivitis respectively — neither directly evaluates Acyclovir as a treatment for PEK. The prediction is biologically plausible only for the HSV-associated subset of PEK, and must not be extrapolated to other aetiologies for which Acyclovir would provide no benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Acyclovir in punctate epithelial keratoconjunctivitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Case Series | American Journal of Ophthalmology | Two AIDS patients receiving antiviral therapy for opportunistic infections developed bilateral drug-induced corneal lipidosis with ocular surface changes; relevant as a differential diagnosis consideration when evaluating PEK-like presentations in patients on multiple medications |
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Case Series | Indian Journal of Pathology & Microbiology | Case series of microsporidial keratoconjunctivitis in an eastern Indian cohort; highlights that infectious keratoconjunctivitis can have non-herpetic causes, underscoring the importance of aetiological diagnosis before initiating antiviral therapy |

> Neither publication directly evaluates Acyclovir for the treatment of punctate epithelial keratoconjunctivitis.

---

## South Africa Market Information

Acyclovir (DrugBank ID: DB00787) is **not currently registered with SAHPRA** and holds no active product licences in South Africa. There are no local product registrations to list.

Healthcare professionals wishing to use Acyclovir in South Africa should consult SAHPRA regarding the Section 21 authorisation process for unregistered medicines (Medicines and Related Substances Act), or identify currently registered antiviral alternatives. Internationally, Acyclovir is widely registered in the USA, EU, and UK for oral, intravenous, topical, and ophthalmic formulations across multiple herpes virus indications.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> Since Acyclovir is not currently registered in South Africa, no SAHPRA-approved PI is available. Prescribers considering use under a Section 21 framework should consult internationally recognised prescribing information (e.g., FDA labelling or EMA SmPC). Key safety considerations documented internationally include: **renal toxicity** (notably with intravenous formulations — adequate hydration is essential; dose adjustment required in renal impairment), **neurotoxicity** (confusion, tremor, encephalopathy — risk increased with renal impairment), and **phlebitis** at IV infusion sites. Acyclovir is generally well tolerated in oral and topical formulations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for Acyclovir in punctate epithelial keratoconjunctivitis is mechanistically plausible only for the HSV-associated subset of PEK, but no direct clinical trial evidence or prospective observational data supports this specific repurposing. Furthermore, Acyclovir is not currently registered with SAHPRA, creating a significant regulatory barrier to clinical application in South Africa.

**To proceed, the following is needed:**
- Initiate SAHPRA registration process or Section 21 authorisation for Acyclovir before considering any clinical use
- Resolve the MOA data gap through formal DrugBank API query or published pharmacology reference to support mechanistic analysis
- Conduct prospective studies specifically evaluating Acyclovir in patients with **HSV-confirmed** punctate epithelial keratoconjunctivitis (aetiological specificity is essential)
- Retrieve and review internationally approved PI (e.g., FDA package insert) for formal safety, contraindication, and DDI profiling in the South African clinical context

---

**Note on higher-priority indications from the same TxGNN run:**
While PEK (rank 1) carries a Hold recommendation, three other TxGNN-predicted indications have substantially stronger evidence and merit closer evaluation:

| Rank | Indication | Evidence Level | Clinical Trials | Decision |
|------|-----------|---------------|----------------|---------|
| 2 | Common Wart (intralesional Acyclovir) | L2 | 6 trials, incl. Phase 2/3 RCTs (n=92) | Research Question |
| 3 | Post-Infectious Neuralgia (Postherpetic Neuralgia) | L2 | 12 trials (Valacyclovir/Acyclovir class) | Proceed with Guardrails |
| 9 | Disease of Orbital Region (Herpetic ocular disease) | L2 | Multiple completed trials | Proceed with Guardrails |

These indications are recommended for priority review in subsequent evaluation cycles, particularly **post-herpetic neuralgia** — where Acyclovir/Valacyclovir class evidence for prevention of PHN during acute herpes zoster is mechanistically sound and supported by completed Phase 3 trials.

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. This evaluation was generated using the TxGNN model (data cut-off: 4 April 2026).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

