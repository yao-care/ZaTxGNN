---
layout: default
title: Dexamethasone
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 10
---

# Dexamethasone
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

# Dexamethasone: From Corticosteroid Anti-inflammatory Use to Alopecia Areata

## One-Sentence Summary

Dexamethasone is a potent synthetic glucocorticoid widely used for its anti-inflammatory and immunosuppressive properties across numerous indications. The TxGNN model predicts it may be effective for **Alopecia Areata**, with **20 publications** — including a randomised controlled trial and a systematic review/network meta-analysis — currently supporting this direction. Notably, dexamethasone oral mini-pulse (OMP) therapy for alopecia areata already has over 20 years of clinical use documented in the literature.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glucocorticoid anti-inflammatory/immunosuppressive (multiple indications; specific SAHPRA-approved indications not available) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (1 RCT + systematic review/network meta-analysis) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note:** Although dexamethasone has no SAHPRA registrations under DrugBank ID DB01234 in this dataset, dexamethasone formulations are widely available in South Africa under various registrations and are included on the South African Essential Medicines List (EML). The "not marketed" status here reflects a data-matching limitation rather than true unavailability.

## Why is This Prediction Reasonable?

Alopecia areata (AA) is a T-cell-mediated autoimmune disease in which CD8⁺ NKG2D⁺ T lymphocytes attack the hair follicle immune privilege zone, leading to non-scarring hair loss. The collapse of hair follicle immune privilege is driven by pro-inflammatory cytokines including IFN-γ, IL-2, and IL-15, which upregulate MHC class I and NKG2D ligands on follicular epithelium.

Dexamethasone is a potent synthetic glucocorticoid that exerts its immunosuppressive effects through multiple complementary pathways: (1) suppression of NF-κB and AP-1 transcription factors, reducing production of pro-inflammatory cytokines central to the AA pathomechanism; (2) induction of T-cell apoptosis, directly reducing the autoreactive T-cell population attacking hair follicles; and (3) inhibition of antigen-presenting cell function, disrupting the immune cascade that sustains follicular damage.

The oral mini-pulse (OMP) regimen — typically 5 mg dexamethasone on two consecutive days per week — has been used clinically for extensive AA since the late 1990s. This intermittent dosing strategy aims to achieve meaningful immunosuppression while minimising the cumulative adverse effects of continuous corticosteroid use. A 2024 systematic review and network meta-analysis confirmed systemic steroids among effective treatments for severe AA, and a randomised controlled trial directly evaluated dexamethasone OMP in paediatric AA, providing Level 2 evidence for this repurposing prediction.

## Clinical Trial Evidence

No directly relevant clinical trials evaluating dexamethasone specifically for alopecia areata were identified on ClinicalTrials.gov, SANCTR, or PACTR registries. The 14 trials retrieved all used dexamethasone as a supportive agent in unrelated oncology protocols (multiple myeloma, glioblastoma, lymphoma, mesothelioma) and were graded as irrelevant (Grade C) to the alopecia areata indication.

> **Important context:** The clinical evidence for dexamethasone in alopecia areata resides primarily in published peer-reviewed literature (see below) rather than in prospective registered trials. This is consistent with the long-standing off-label use of dexamethasone OMP for AA, which predates modern trial registration requirements.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | Systematic Review / Network Meta-Analysis | Arch Dermatol Res | Compared systemic steroids, oral JAK inhibitors, and contact immunotherapy for severe AA (SALT ≥ 50%). Network meta-analysis identified relative efficacy across treatment modalities for severe AA. |
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | RCT | Dermatol Ther | Randomised controlled trial in 30 children with severe non-progressive AA, comparing low-dose dexamethasone OMP vs diphenylcyclopropenone (DPCP) contact sensitisation. Directly evaluated dexamethasone OMP efficacy and safety in paediatric AA. |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | Prospective Cohort | J Clin Med | Real-world prospective cohort assessing effectiveness and safety of dexamethasone mini-pulse OMP in AA patients. Explored factors associated with successful treatment response. |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | Retrospective Multicentric Study | Dermatol Ther | Multicentre evaluation of oral dexamethasone mini-pulse for moderate-to-severe AA (totalis, universalis, multifocal). Assessed outcomes in the context of limited JAK inhibitor accessibility. |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | Clinical Study (Paediatric) | Dermatol Ther | Prospective study of 73 paediatric patients with severe AA (>30% scalp involvement). Compared 1-day vs 3-day IV dexamethasone pulse regimens combined with topical clobetasol. Assessed response rates and short-term outcomes. |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | Clinical Study (Long-term Follow-up) | Dermatol Ther | Long-term follow-up (median 96 months) of 65 children/adolescents with severe AA treated with oral dexamethasone pulse + topical clobetasol. Evaluated durability of response across AA subtypes. |
| [16707886](https://pubmed.ncbi.nlm.nih.gov/16707886/) | 2006 | Comparative Study | Dermatology (Basel) | Compared efficacy, relapse rate, and side effects of three systemic corticosteroid modalities for extensive AA. Provides evidence on relative performance of different steroid regimens. |
| [41872082](https://pubmed.ncbi.nlm.nih.gov/41872082/) | 2026 | Retrospective Chart Review | Eur J Dermatol | Real-world experience combining stepwise topical corticosteroids with baricitinib, using pulse dexamethasone as rescue therapy in non-responders with severe AA. |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | Case Series / Focused Review | J Dermatolog Treat | Documents durable remission of severe AA using dexamethasone OMP when JAK inhibitors are unavailable or contraindicated. Particularly relevant for resource-limited settings. |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | Clinical Study | J Dermatol | Foundational study of twice-weekly 5 mg dexamethasone OMP in 30 patients with extensive AA. Evaluated terminal hair regrowth after minimum 12 weeks of treatment. |

**Additional relevant publications** (not tabled): paediatric dosing review (PMID [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/)), dexamethasone-loaded nanoparticle formulations for follicular targeting (PMIDs [33920403](https://pubmed.ncbi.nlm.nih.gov/33920403/), [34452283](https://pubmed.ncbi.nlm.nih.gov/34452283/)), murine hair cycle model (PMID [8040602](https://pubmed.ncbi.nlm.nih.gov/8040602/)), and an observational cohort from Sri Lanka (PMID [25556409](https://pubmed.ncbi.nlm.nih.gov/25556409/)).

## South Africa Market Information

No SAHPRA registrations were identified in this dataset for dexamethasone under the queried DrugBank identifier.

> **Practical note:** Dexamethasone is widely available in South Africa and is listed on the **South African Essential Medicines List (EML)** as a corticosteroid for multiple indications. Various dexamethasone products (tablets, injectable solutions, ophthalmic preparations) are registered with SAHPRA under different marketing authorisation holders. The absence of registrations in this report reflects a data-matching limitation and should not be interpreted as unavailability. Clinicians should consult the SAHPRA database directly for current product registrations.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for dexamethasone safety information. Report adverse drug reactions to SAHPRA.

**General safety considerations relevant to dexamethasone OMP for alopecia areata include:**

- **Hypothalamic-pituitary-adrenal (HPA) axis suppression:** Even intermittent pulse dosing carries risk of adrenal suppression, particularly with prolonged use. Monitoring and appropriate tapering are required.
- **Metabolic effects:** Weight gain, glucose intolerance, dyslipidaemia, and Cushingoid features may occur with repeated courses.
- **Bone health:** Osteoporosis risk with cumulative exposure; consider bone density monitoring for longer treatment courses.
- **Immunosuppression:** Increased susceptibility to infections; screen for latent tuberculosis (particularly relevant in the South African context given high TB prevalence).
- **Paediatric considerations:** Growth suppression with prolonged use; the literature includes specific paediatric dosing studies (see PMIDs 36086930, 31579982, 26179196).
- **Ophthalmological effects:** Glaucoma and posterior subcapsular cataracts with prolonged use.

> **Note:** Specific SAHPRA PI warnings, contraindications, and drug-drug interaction data were not available in this evidence pack. These must be obtained from the approved Professional Information before initiating treatment.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dexamethasone oral mini-pulse therapy for alopecia areata is supported by over two decades of clinical experience, a randomised controlled trial, a systematic review/network meta-analysis, and multiple prospective and retrospective clinical studies. The mechanistic rationale is strong (Grade A): dexamethasone directly targets the T-cell-mediated autoimmune pathomechanism of AA through NF-κB suppression, T-cell apoptosis induction, and antigen-presenting cell inhibition. This is a well-established off-label use with robust literature support, particularly relevant for settings where JAK inhibitors are inaccessible or unaffordable.

**To proceed, the following is needed:**
- **SAHPRA registration confirmation:** Verify current dexamethasone product registrations in South Africa suitable for oral pulse therapy (0.5 mg and 4 mg tablets)
- **Detailed Professional Information (PI) review:** Obtain full safety data including contraindications, warnings, and drug interactions from SAHPRA-approved PI
- **Treatment protocol standardisation:** Develop a South African clinical protocol for dexamethasone OMP in AA, specifying dose (e.g. 5 mg on two consecutive days/week), duration, monitoring schedule, and stopping rules
- **TB screening protocol:** Given South Africa's high TB burden, establish mandatory latent TB screening before initiating immunosuppressive corticosteroid therapy
- **Paediatric dosing guidance:** Adapt published paediatric dosing data for local use, with growth monitoring requirements
- **Pharmacovigilance plan:** Establish systematic monitoring for HPA axis suppression, metabolic effects, and infection risk in the local treatment population

---

*This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. Report generated: 2026-04-05.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

