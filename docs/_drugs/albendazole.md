---
layout: default
title: Albendazole
parent: High Evidence (L1-L2)
nav_order: 20
evidence_level: L2
indication_count: 10
---

# Albendazole
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Albendazole: From Anthelmintic Use to Alveolar Echinococcosis

## One-Sentence Summary

Albendazole is a benzimidazole anthelmintic (deworming) drug, and one product is currently registered with SAHPRA in South Africa.
The TxGNN model predicts it may be effective for **alveolar echinococcosis**, a severe liver-centred parasitic disease.
The prediction is supported by **5 retrieved clinical trials (1 directly relevant Phase 2 trial)** and **20 publications**, but the disease is already treated with albendazole in practice, so this is closer to standard of care than to novel repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA registration data (albendazole is a broad-spectrum anthelmintic) |
| Predicted New Indication | Alveolar echinococcosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the source record. Based on known pharmacology, albendazole binds parasite beta-tubulin, blocks microtubule polymerisation and impairs glucose uptake. This is *parasitostatic* against *Echinococcus multilocularis* metacestodes: it slows parasite growth but does not kill it.

Alveolar echinococcosis is caused by the larval stage of a tapeworm. Albendazole is already used against related tapeworm larval diseases such as cystic echinococcosis and neurocysticercosis, so the mechanism transfers biologically. The literature describes albendazole as the guideline-recommended long-term therapy for alveolar echinococcosis. It is used especially when surgery is not feasible, and it is given alongside surgery when surgery is possible.

The model's prediction therefore matches established clinical practice. The main uncertainty is whether this use is on the South African label, which the supplied data do not show.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Phase 2 | Completed | 194 | Albendazole treatment in early-stage alveolar echinococcosis, found through ultrasound screening in Kyrgyzstan. This is the direct disease and drug match. |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | Not applicable | Completed | 50 | EchinoVISTA: parasite viability and follow-up markers in albendazole-treated hepatic alveolar echinococcosis, to guide when treatment can be stopped. It is monitoring-focused and does not test efficacy. |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | Not applicable | Unknown | 24 | Randomised trial of adjuvant albendazole vs placebo after pulmonary hydatid cyst resection. It concerns cystic disease, so it is only supportive. |
| [NCT05824442](https://clinicaltrials.gov/study/NCT05824442) | Not applicable | Recruiting | 43 | Multiplex qPCR diagnostic evaluation for echinococcosis. It provides no treatment evidence. |
| [NCT07176598](https://clinicaltrials.gov/study/NCT07176598) | Not applicable | Completed | 1 | Case report of an intramuscular hydatid cyst (cystic disease). It is anecdotal. |

No Phase 3 randomised trial was found for this indication.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19931502](https://pubmed.ncbi.nlm.nih.gov/19931502/) | 2010 | Expert consensus | Acta Trop | Updated expert consensus on diagnosis, treatment and follow-up of cystic and alveolar echinococcosis. |
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | Review | Clin Microbiol Rev | 21st-century advances in echinococcosis genetics, diagnostics and treatment techniques. |
| [39311470](https://pubmed.ncbi.nlm.nih.gov/39311470/) | 2024 | Review | Parasite | Benzimidazoles are the only recommended drugs for alveolar echinococcosis. They are parasitostatic, so the parasite can resume growth if treatment stops. They can also cause liver dysfunction. |
| [39254012](https://pubmed.ncbi.nlm.nih.gov/39254012/) | 2024 | Review | Tidsskr Nor Legeforen | Clinical overview. Treatment is often extensive surgery combined with prolonged albendazole. |
| [36974024](https://pubmed.ncbi.nlm.nih.gov/36974024/) | 2022 | Review | Chin J Schisto Control | Albendazole may delay progression in patients who cannot or will not have surgery. |
| [34161992](https://pubmed.ncbi.nlm.nih.gov/34161992/) | 2021 | Review | Semin Liver Dis | Hepatic alveolar echinococcosis is rare but severe, and cases are re-emerging in historically endemic areas. |
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | Review | Parasite | Albendazole and mebendazole are the current options. Novel compounds are being explored. |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Review | Acta Trop | No non-surgical option currently replaces albendazole or mebendazole. |
| [38501660](https://pubmed.ncbi.nlm.nih.gov/38501660/) | 2024 | Preclinical (rat model) | Antimicrob Agents Chemother | Albendazole's poor solubility limits oral bioavailability. Solubilising formulations were tested in infected rats. |
| [34688631](https://pubmed.ncbi.nlm.nih.gov/34688631/) | 2022 | Preclinical (animal) | Acta Trop | Carvacrol combined with albendazole enhanced efficacy over monotherapy in experimental disease. |

No randomised controlled trials were retrieved for this indication.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A38/12/0426 | Wormadole | "Chu" (as recorded in the source data) | Not recorded in the supplied data |

Essential Medicines List (EML) status was not included in the supplied data and should be checked separately.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The supplied data contain no interaction records. The literature notes that benzimidazole therapy can cause liver dysfunction, which is why the guardrails below include liver and blood count monitoring.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 2 trial (194 patients) and extensive review and guideline literature support albendazole in alveolar echinococcosis. It is already a mainstay of long-term therapy. The evidence stays at L2 because there is no Phase 3 randomised trial, and the safety data for South Africa are still missing.

**To proceed, the following is needed:**
- The SAHPRA Professional Information, to confirm labelled indications, warnings and contraindications. This is currently a blocking gap.
- Confirmation of whether alveolar echinococcosis falls within the registered indication of Wormadole, and of its EML status.
- Verified mechanism-of-action data from DrugBank.
- A specialist-led management plan covering prolonged dosing, liver function and full blood count monitoring, and surgical assessment where feasible.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

