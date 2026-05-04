---
layout: default
title: Colchicine
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 10
---

# Colchicine
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

# Colchicine: From Gout and Familial Mediterranean Fever to Plasmodium falciparum Malaria

---

## One-Sentence Summary

Colchicine is a well-established alkaloid used globally for the treatment and prevention of gout and familial Mediterranean fever (FMF).
The TxGNN model's top-ranked predicted new indication is **Plasmodium falciparum malaria** (score: 99.60%), supported by **0 clinical trials** and **6 publications** — all of which are in vitro or indirect mechanistic studies, placing the evidence at preclinical level only.
Notably, Colchicine's second-ranked prediction is FMF (score: 99.38%, evidence level L1), reflecting its well-established global use — a high-priority finding given that Colchicine carries **zero SAHPRA registrations** in South Africa.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gout and Familial Mediterranean Fever (FMF) |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L4 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured dataset. Based on well-established pharmacological knowledge, Colchicine is an alkaloid derived from *Colchicum autumnale* that binds to tubulin dimers and inhibits their polymerisation into microtubules. This disrupts neutrophil chemotaxis, NLRP3 inflammasome assembly, and cell division — the basis of its anti-inflammatory efficacy in gout and FMF, both of which have been proven in decades of clinical use. Mechanistically, this same action may be applicable to *Plasmodium falciparum* malaria through disruption of the parasite's cytoskeletal dynamics.

The TxGNN prediction is built on *P. falciparum*'s reliance on microtubule-mediated cytoskeletal function during intraerythrocytic schizogony (asexual replication inside red blood cells). Several in vitro studies have shown that structurally related tubulin-binding compounds — including colcemid and tubulozoles — inhibit parasite protein biosynthesis and growth, suggesting that plasmodial tubulin represents a viable antimalarial target. Separately, 82% of acute malaria patients in one clinical series were found to carry IgM autoantibodies against intermediate filaments, implying that host cytoskeletal disruption is a feature of infection pathology.

There are, however, important caveats. Plasmodial tubulins appear structurally distinct from human tubulins at the molecular level, raising questions about both selectivity and therapeutic window. Critically, **no available publication directly studies Colchicine itself** in malaria — all mechanistic links are inferred from structural analogues or indirect in vitro findings. No animal model data or human pharmacokinetic-pharmacodynamic modelling supports clinical translation at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Colchicine in *Plasmodium falciparum* malaria.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2221861](https://pubmed.ncbi.nlm.nih.gov/2221861/) | 1990 | In vitro | Antimicrobial Agents and Chemotherapy | Tubulozoles (tubulin-targeting antimalarial candidates) inhibit *P. falciparum* protein biosynthesis; colcemid (microtubule inhibitor structurally related to colchicine) produced similar effects, supporting plasmodial tubulin as a drug target |
| [2670249](https://pubmed.ncbi.nlm.nih.gov/2670249/) | 1989 | In vitro | Cell Biology International Reports | Nine tubulin-binding compounds tested against intraerythrocytic *P. falciparum*; plasmodial tubulins appear molecularly distinct from mammalian proteins; tubulozole-T (inactive in mammalian systems) identified as a promising novel antimalarial |
| [6362934](https://pubmed.ncbi.nlm.nih.gov/6362934/) | 1984 | Clinical Observation | Clinical and Experimental Immunology | 82% of acute malaria patients (n=78) carried IgM autoantibodies to intermediate filaments in human cells, versus only 8% of blood donors; implicates host cytoskeletal disruption as a feature of malaria pathology |
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro | PLoS ONE | Curcumin binds tubulin and disrupts *P. falciparum* microtubules, providing mechanistic precedent for tubulin-directed antimalarial strategies; indirect evidence only — curcumin, not colchicine, was studied |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | Molecular Biology | Molecular and Cellular Biology | Expression of the plasmodial pfmdr1 transporter in mammalian cells increased chloroquine susceptibility; contextualises intracellular drug accumulation pharmacology in *P. falciparum*, indirectly relevant to understanding drug-target access |

---

## South Africa Market Information

Colchicine is **not currently registered with SAHPRA** and holds no active product licences in South Africa. No SAHPRA-approved Professional Information (PI) document exists for this medicine locally.

> **Regulatory context:** Colchicine is included on the **WHO Essential Medicines List** (for gout and FMF). It is approved by the US FDA (Colcrys®, Mitigare®) and the EMA for gout and FMF, and is widely available in Europe, North America, and the Middle East. Clinical access for patients in South Africa would currently require a **Section 21 authorisation** (unregistered medicine application to SAHPRA) on a per-patient basis. Pursuing formal SAHPRA registration — particularly for the FMF indication — represents a significant unmet regulatory opportunity (see Conclusion).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. As no product is currently registered in South Africa, clinicians should consult internationally approved prescribing information (e.g., FDA-approved labelling for Colcrys®) and report adverse drug reactions to SAHPRA via the MedSafety reporting system.

> **Important general safety note:** Published literature (PMID 20586571) documents that Colchicine carries a **narrow therapeutic index** with no clearly defined demarcation between non-toxic, toxic, and lethal doses — unintentional overdose is a recognised clinical hazard. Particular caution is warranted when co-prescribing with strong CYP3A4 inhibitors (e.g., clarithromycin, ritonavir) or P-glycoprotein inhibitors, which can markedly elevate colchicine plasma concentrations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All current evidence linking Colchicine to *Plasmodium falciparum* malaria is indirect and preclinical (evidence level L4): no Colchicine-specific in vitro studies exist, no animal models have been explored, and no clinical trials have been registered. While the mechanistic hypothesis via microtubule disruption of intraerythrocytic schizonts is biologically coherent, the translational gap from structural analogues to Colchicine itself in a clinical context is substantial.

**To proceed with malaria investigation, the following is needed:**
- Direct in vitro susceptibility testing of Colchicine against *P. falciparum* (3D7 and resistant strains), with IC₅₀ determination
- Selectivity index assessment: comparison of cytotoxicity in parasitised vs. uninfected red blood cells and hepatocytes
- Animal model proof-of-concept study (e.g., *Plasmodium berghei* murine malaria model)
- Pharmacokinetic-pharmacodynamic modelling to determine whether clinically safe plasma concentrations achieve sufficient antimalarial exposure
- Full safety profile review using SAHPRA-equivalent approved PI from a reference jurisdiction before any human study

---

### ⚠️ High-Priority Secondary Finding: Familial Mediterranean Fever (Rank 2 — L1 Evidence)

The TxGNN model's **second-ranked prediction** — **Familial Mediterranean Fever (FMF)** (score: 99.38%, evidence level **L1**) — represents Colchicine's most robustly evidenced global indication. Multiple Phase 3 RCTs and international guidelines from EULAR and ACR confirm Colchicine as the **first-line, gold-standard treatment for FMF**: it prevents recurrent febrile attacks, reduces systemic inflammation, and critically prevents renal amyloidosis — the leading cause of FMF mortality.

FMF predominantly affects populations of Mediterranean, Middle Eastern, North African, and Ashkenazi Jewish descent, communities that are present in South Africa. Given that Colchicine has **zero SAHPRA registrations**, South African patients with FMF currently have no straightforward regulatory pathway to this essential medicine.

**Recommended action:** Initiate a SAHPRA Section 21 pathway for urgent individual access, and engage with a pharmaceutical sponsor to explore full product registration for the FMF indication. This represents a near-term, high-impact regulatory opportunity grounded in L1 evidence.

---

*This report is generated for research reference purposes only. It does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Adverse drug reactions should be reported to SAHPRA.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

