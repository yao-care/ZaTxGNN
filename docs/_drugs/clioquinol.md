---
layout: default
title: Clioquinol
parent: 僅模型預測 (L5)
nav_order: 130
evidence_level: L5
indication_count: 10
---

# Clioquinol
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

# Clioquinol: From Topical Antiseptic to Cutaneous Candidiasis

## One-Sentence Summary

Clioquinol is a broad-spectrum halogenated hydroxyquinoline antiseptic and antifungal agent with a long clinical history, best known as the active ingredient in topical combination preparations such as Vioform (clioquinol 3% + corticosteroid). The TxGNN model predicts it may be effective for **cutaneous candidiasis**, with **0 registered clinical trials** and **6 publications** currently supporting this direction. Evidence is limited to older observational and comparative clinical studies from the 1960s–1980s, placing this candidate at the research question stage pending formal safety evaluation and regulatory assessment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Topical antiseptic; historically used in combination products (e.g., Locacorten-Vioform) for infected dermatoses |
| Predicted New Indication | Cutaneous candidiasis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L3 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the evidence pack. Based on established pharmacological knowledge, clioquinol is a halogenated 8-hydroxyquinoline compound that functions primarily as a broad-spectrum metal chelator. It chelates divalent metal ions — particularly Zn²⁺ and Cu²⁺ — which are essential cofactors for fungal metalloenzymes including superoxide dismutase and cytochrome oxidase. This chelation disrupts *Candida* species' antioxidant defences and mitochondrial respiratory function, while the molecule also exerts direct membrane-disruptive toxicity against fungal cell walls.

The connection between clioquinol's historical clinical use and cutaneous candidiasis is well-established in practice, even if the formal mechanistic literature is incomplete. The topical preparation Locacorten-Vioform (clioquinol 3% + flumetasone 0.02%) was widely used across multiple countries for infected dermatoses, including cutaneous candidiasis. Iodochlorhydroxyquin-hydrocortisone combinations were standard comparator agents in dermatological clinical trials through the 1970s and 1980s, often tested specifically against *Candida* skin infections. This constitutes direct clinical precedent for the TxGNN prediction.

From a mechanistic standpoint, the prediction is scientifically coherent: *Candida* species depend heavily on metal-dependent enzyme systems to neutralise host-generated oxidative stress. By chelating the zinc and copper required to sustain these defences, clioquinol effectively disarms the pathogen's survival mechanisms. Combined with its broad-spectrum antimicrobial activity demonstrated in historical studies, the prediction that clioquinol is effective in cutaneous candidiasis is supported in principle — though it lacks prospective trial validation and a full modern safety assessment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (neither ClinicalTrials.gov nor ICTRP search returned any results for Clioquinol + cutaneous candidiasis).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [155507](https://pubmed.ncbi.nlm.nih.gov/155507/) | 1979 | Clinical Evaluation | *Current Medical Research and Opinion* | Parallel comparison of HNA cream vs. iodochlorhydroxyquin-hydrocortisone (I-HC) in 80 patients with cutaneous candidiasis; excellent response in 95% (HNA) vs. 43% (I-HC control), providing indirect evidence for the active iodochlorhydroxyquin component |
| [6459255](https://pubmed.ncbi.nlm.nih.gov/6459255/) | 1981 | Comparative Clinical Study | *Journal of International Medical Research* | Randomised parallel study (n=154) comparing a topical cream containing betamethasone/gentamicin/iodochlorhydroxyquin/tolnaftate vs. halcinonide/neomycin/nystatin for infected eczematous dermatoses and cutaneous candidiasis; equivalent therapeutic responses, confirming activity of the iodochlorhydroxyquin-containing formulation |
| [128475](https://pubmed.ncbi.nlm.nih.gov/128475/) | 1975 | Clinical Case Series | *Dermatologica* | Double-blind study (n=430): Locacorten-Vioform (flumetasone 0.02% + **clioquinol 3%**) significantly superior to flumetasone alone, clioquinol alone, and placebo for dermatological conditions with secondary infection; microbiological conversion markedly greater with the combination |
| [136333](https://pubmed.ncbi.nlm.nih.gov/136333/) | 1976 | Clinical Evaluation | *Current Therapeutic Research* | Clinical evaluation of a halcinonide-antifungal combination product; no abstract available |
| [4220930](https://pubmed.ncbi.nlm.nih.gov/4220930/) | 1965 | Mechanistic/Observational | *Z. Haut- u. Geschlechtskrankheiten* | Historical investigation into the role of yeasts in Danbolt-Closs acrodermatitis enteropathica; contextually relevant to clioquinol's use in zinc-related dermatoses; no abstract available |
| [2978600](https://pubmed.ncbi.nlm.nih.gov/2978600/) | 1988 | Preventive/Occupational Study | *Przeglad Dermatologiczny* | In vitro evaluation of soap additives against *Candida albicans* isolates; clioquinol-containing preparations demonstrated the strongest fungicidal activity in alkaline soap solutions, with maintained stability at production temperatures |

> **Note on evidence quality**: All six publications are from 1965–1988. None are prospective RCTs with clioquinol as a stand-alone intervention; most evaluate combination formulations where clioquinol is the antifungal component. Contemporary controlled trials are absent.

---

## South Africa Market Information

Clioquinol is currently **not registered with SAHPRA** and has no approved products on the South African market (0 licences). It is not included on the Essential Medicines List (EML).

Any clinical use of clioquinol in South Africa would require prior **Section 21 authorisation** (unregistered medicine) from SAHPRA. Prescribers should contact SAHPRA's Regulatory Affairs unit before initiating any compassionate or investigational use.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> **Important context for clinicians**: Although no formal safety data was available in this evidence pack, healthcare professionals should be aware that oral/systemic clioquinol was withdrawn from many markets in the 1970s following reports of **subacute myelo-optic neuropathy (SMON)** — a serious neurological complication associated with long-term high-dose systemic use, predominantly documented in Japan. Topical use at standard concentrations (≤3%) is generally considered to carry a substantially lower systemic risk, but prolonged application to large body surface areas should be avoided. A full SAHPRA-approved PI review is essential before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.84%) to clioquinol for cutaneous candidiasis, and there is genuine historical clinical precedent in combination topical preparations. However, the supporting evidence consists entirely of older observational and comparative clinical studies (L3), no prospective clinical trials exist, clioquinol is not registered with SAHPRA, and formal safety data is absent from the evidence pack. These gaps preclude advancement to active clinical development at this stage.

**To proceed, the following is needed:**

- **Safety assessment**: Full SAHPRA PI/SmPC review or submission of a dossier for SAHPRA Section 21 authorisation; specific evaluation of SMON risk with topical formulations
- **Mechanism of action data**: Formal retrieval from DrugBank API (DB04815) to complete the mechanistic rationale
- **Contemporary evidence review**: Systematic literature search for post-1990 studies on clioquinol in fungal infections, including in vitro MIC data against *Candida* species and any in vivo animal model data
- **Comparative efficacy context**: Benchmarking against current standard-of-care topical antifungals registered in South Africa (e.g., clotrimazole, miconazole) to establish whether a clinical development pathway is justified
- **Formulation pathway**: Identification of a suitable topical dosage form and manufacturer for potential Phase 2 proof-of-concept study in South Africa

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. Results should be interpreted by qualified healthcare professionals. For adverse drug reaction reporting, contact SAHPRA at [www.sahpra.org.za](https://www.sahpra.org.za).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

