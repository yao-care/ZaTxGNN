---
layout: default
title: Albendazole
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 10
---

# Albendazole
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

# Albendazole: From Intestinal Helminthiasis to Alveolar Echinococcosis

## One-Sentence Summary

Albendazole is a broad-spectrum benzimidazole anthelmintic, established as the standard medical treatment for intestinal helminthiasis and a range of other parasitic infections worldwide, though it is not currently registered with SAHPRA in South Africa.
The TxGNN model predicts it may be highly effective for **Alveolar Echinococcosis (AE)** — a rare but potentially fatal parasitic liver disease caused by *Echinococcus multilocularis* — with **5 registered clinical trials** (including 1 completed Phase 2 study enrolling 194 patients) and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum anthelmintic for intestinal helminthiasis and parasitic infections (not registered with SAHPRA) |
| Predicted New Indication | Alveolar Echinococcosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Albendazole belongs to the benzimidazole class of anthelmintics. Its primary active metabolite — **albendazole sulfoxide (ABZSO)** — is generated through hepatic first-pass metabolism and acts by selectively binding to helminth β-tubulin, inhibiting microtubule polymerisation. This disrupts intracellular transport, cell division, and glucose uptake in the parasite, ultimately causing energy depletion and growth arrest or parasite death. For alveolar echinococcosis specifically, ABZSO is able to penetrate the cyst wall of *E. multilocularis* to achieve pharmacologically active concentrations within the germinal layer, causing degeneration of the parasite's protoscoleces. A 2024 pharmacological study (PMID 38501660) further characterised the hepatic metabolic pathways underlying therapeutic efficacy and assessed novel solubilising formulations to address albendazole's poor oral bioavailability.

Alveolar echinococcosis is caused by the metacestode (larval) stage of *E. multilocularis*, which forms pseudo-tumoral, infiltrative, multicystic lesions primarily in the liver, closely mimicking hepatic malignancy on imaging. Without treatment, AE carries an approximately 100% fatality rate within 10–15 years of infection. Curative surgical resection is feasible in only 30–40% of patients due to the invasive nature of the disease. For the remaining patients, long-term — often lifelong — medical therapy with albendazole is the only available option. The drug's effect is parasitostatic rather than parasiticidal: it arrests cyst growth but does not eradicate the parasite, necessitating prolonged treatment and structured monitoring.

The TxGNN prediction score of 99.97% reflects this well-established biological plausibility and the weight of supporting evidence, rather than a speculative repurposing. The WHO Informal Working Group on Echinococcosis (WHO-IWGE) expert consensus (PMID 19931502), multiple international guidelines, and a completed Phase 2 RCT (NCT07182305, n=194) all confirm albendazole as the current standard of medical care for AE. The primary unmet need in South Africa is regulatory: albendazole has no SAHPRA registration and is not marketed locally, requiring Section 21 unregistered medicine authorisation for individual patient access.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Phase 2 | Completed | 194 | Direct treatment trial of early-stage AE in a surveillance cohort in Kyrgyzstan (prevalence ~6%); albendazole used as parasitostatic treatment; provides the most direct and highest-quality clinical efficacy evidence for AE |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | N/A | Completed | 50 | Prospective EchinoVISTA study defining parasite viability biomarkers and imaging markers during albendazole treatment for hepatic AE; informs evidence-based criteria for treatment withdrawal decisions |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | N/A | Unknown | 24 | RCT of adjuvant albendazole vs placebo after pulmonary hydatid cyst (cystic echinococcosis — CE, not AE) resection to reduce recurrence; mechanistically related but a distinct clinical entity; small sample and status uncertain |
| [NCT05824442](https://clinicaltrials.gov/study/NCT05824442) | N/A | Recruiting | 43 | Validation of a new multiplex quantitative PCR technique for diagnosing both AE and CE; albendazole is the standard background treatment but this is a diagnostic — not therapeutic — trial |
| [NCT07176598](https://clinicaltrials.gov/study/NCT07176598) | N/A | Completed | 1 | Single case report of a misdiagnosed intramuscular hydatid cyst (deltoid muscle); treated with albendazole after surgical excision; evidence level extremely low (n=1) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [19931502](https://pubmed.ncbi.nlm.nih.gov/19931502/) | 2010 | Expert Consensus / Guideline | *Acta Tropica* | WHO-IWGE international expert consensus on diagnosis, treatment and follow-up for CE and AE; formally establishes albendazole (continuous or cycle-based) as standard of care for inoperable AE |
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | Comprehensive Review | *Clinical Microbiology Reviews* | 21st-century advances in *Echinococcus* genetics, genomics, diagnostics and treatment; comprehensive review of albendazole's central role and known limitations in AE management |
| [39311470](https://pubmed.ncbi.nlm.nih.gov/39311470/) | 2024 | Review | *Parasite* (Paris) | Current state of benzimidazole chemotherapy for AE; addresses the parasitostatic limitation, hepatotoxicity risks with long-term use, and urgent need for novel alternative agents |
| [36974024](https://pubmed.ncbi.nlm.nih.gov/36974024/) | 2022 | Review | *Chinese Journal of Schistosomiasis Control* | Progress review of albendazole research specifically in AE; covers mechanism of action, clinical outcomes for surgical and non-surgical patients, formulation advances, and emerging drug combinations |
| [38501660](https://pubmed.ncbi.nlm.nih.gov/38501660/) | 2024 | Pharmacological Study | *Antimicrobial Agents and Chemotherapy* | Metabolic mechanism and pharmacokinetics of ABZ in a secondary hepatic AE rat model; evaluates novel solubilising formulations (ABZ-CSD, TABZ-HCl-H, TABZ-HES-H) to overcome poor oral bioavailability |
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | Comparative Review | *Parasite* (Paris) | Compares albendazole and mebendazole for AE and CE; explores whole-organism drug screening strategies for identifying next-generation chemotherapeutic compounds |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Review | *Acta Tropica* | Novel treatment prospects for CE and AE; confirms that no non-surgical option currently replaces albendazole (or mebendazole) as first-line medical therapy, despite extensive investigation |
| [34161992](https://pubmed.ncbi.nlm.nih.gov/34161992/) | 2021 | Clinical Review | *Seminars in Liver Disease* | Hepatic AE: clinical presentation, resurgence in Europe, and emergence in previously non-endemic countries; treatment paradigm of surgery plus long-term albendazole with close follow-up |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Review | *World Journal of Gastroenterology* | Current management of liver echinococcosis; surgical resection as cornerstone, albendazole as essential medical adjunct pre- and post-operatively; AE mimics carcinoma and is uniformly fatal without treatment |
| [39254012](https://pubmed.ncbi.nlm.nih.gov/39254012/) | 2024 | Review | *Tidsskrift for den Norske Laegeforening* | AE as an imported disease in non-endemic regions (Norway); treatment with extensive hepatic surgery and prolonged albendazole; directly relevant for South African clinicians managing imported or travel-associated cases |

---

## South Africa Market Information

Albendazole is **not registered with SAHPRA** and is not currently marketed in South Africa. There are no SAHPRA product licences on record.

For clinical access, prescribers must apply for **Section 21 (unregistered medicine) authorisation** from SAHPRA on a per-patient basis. Albendazole is included on the **WHO Essential Medicines List (EML)** and is available from multiple WHO prequalified generic manufacturers internationally. The National Department of Health Essential Medicines List (EML) should be consulted for any recent updates to listing status.

---

## Safety Considerations

Please refer to the manufacturer's Summary of Product Characteristics (SmPC) or WHO product monograph for complete safety information, as albendazole is not SAHPRA-registered and no SAHPRA-approved Professional Information (PI) is available. Report any adverse drug reactions to SAHPRA via the MedSafety online reporting platform.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Albendazole is the WHO-endorsed first-line medical treatment for alveolar echinococcosis, supported by a completed Phase 2 RCT (n=194), extensive WHO-IWGE expert consensus, and a well-characterised mechanism of action (β-tubulin inhibition with cyst penetration by active metabolite ABZSO). The TxGNN score of 99.97% reflects validated biological plausibility rather than speculative repurposing. The critical barriers to use in South Africa are regulatory and logistical, not clinical.

**To proceed, the following is needed:**
- **Regulatory pathway**: Apply for SAHPRA Section 21 unregistered medicine authorisation for individual AE patients; explore feasibility of formal SAHPRA registration given WHO EML inclusion and established global use
- **Safety profile documentation**: Obtain and formally document key warnings, contraindications, and drug-drug interaction profile from the international SmPC (absent from this Evidence Pack); particular attention to hepatotoxicity and bone marrow suppression with long-term use
- **Supply chain**: Identify a WHO prequalified generic albendazole supplier and establish importation and storage logistics
- **Clinical monitoring plan**: Baseline and periodic liver function tests (ALT/AST), full blood count (FBC with differential), and abdominal imaging (ultrasound, CT or MRI) for assessment of treatment response and disease progression
- **Specialist referral**: AE management requires multidisciplinary input (infectious disease, hepatology, hepatobiliary surgery) given its clinical mimicry of liver malignancy, long treatment duration, and complex surgical considerations

---

> **Disclaimer**: This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All prescribing decisions should adhere to current SAHPRA regulations and clinical guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

