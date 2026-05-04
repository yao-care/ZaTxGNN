---
layout: default
title: Clobetasol Propionate
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 7
---

# Clobetasol Propionate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Clobetasol Propionate: From Inflammatory Skin Conditions to Exanthem

## One-Sentence Summary

Clobetasol Propionate is an ultra-potent topical glucocorticoid established internationally as the standard of care for severe inflammatory dermatoses such as lichen sclerosus, oral lichen planus, and psoriasis — though it currently holds **no SAHPRA registration** in South Africa.

The TxGNN model predicts **7 candidate new indications**; **exanthem** (rank 3, score 99.26%) carries the strongest available clinical evidence, backed by **multiple completed Phase 2–3 randomised trials** and **6 supporting publications**, while the top-ranked prediction (vulvar inverted follicular keratosis) remains at evidence level L5 with no supporting studies whatsoever.

The recommended overall decision is **Hold**, primarily due to the absence of SAHPRA registration and missing formal safety data, with **Research Question** status warranted for exanthem and acne keloid once regulatory groundwork is completed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe inflammatory skin conditions — lichen sclerosus, oral lichen planus, psoriasis, eczema (internationally established; **not registered in South Africa**) |
| Top-Ranked Predicted Indication | Vulvar Inverted Follicular Keratosis (Rank 1) |
| Most Evidenced Predicted Indication | Exanthem (Rank 3) |
| TxGNN Prediction Score (Rank 1 / Rank 3) | 99.46% / 99.26% |
| Evidence Level (Rank 1 / Rank 3) | L5 / L2 |
| South Africa Market Status | **Not marketed** |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## All Predicted Indications — Summary

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|-------------|----------------|----------|
| 1 | Vulvar Inverted Follicular Keratosis | 99.46% | L5 | Hold |
| 2 | Acrodermatitis Chronica Atrophicans | 99.30% | L5 | Hold |
| 3 | **Exanthem** | **99.26%** | **L2** | **Research Question** |
| 4 | **Acne Keloid** | **99.21%** | **L3** | **Research Question** |
| 5 | Neonatal Dermatomyositis | 99.16% | L5 | Hold |
| 6 | Childhood CTD-Associated Interstitial Lung Disease | 99.07% | L5 | Hold |
| 7 | Amyopathic Dermatomyositis | 99.05% | L5 | Hold |

> The clinical evidence and analysis below focus on **exanthem** (rank 3) and **acne keloid** (rank 4) — the two indications with meaningful supporting evidence. Ranks 1, 2, 5, 6, and 7 are addressed briefly in the rationale section and excluded from further evidence tables.

---

## Why is This Prediction Reasonable?

Formal mechanism of action data is not available in the current Evidence Pack. Based on well-established pharmacology, however, clobetasol propionate is a **Class I (super-potent) synthetic glucocorticoid** that binds with high affinity to intracellular glucocorticoid receptors (GR). This triggers nuclear translocation and suppression of pro-inflammatory transcription factors — most critically NF-κB — resulting in dramatically reduced production of IL-1β, TNF-α, and IFN-γ, curtailed infiltration by T lymphocytes and mast cells, decreased keratinocyte proliferation, and reduced vascular permeability. These actions collectively underlie its efficacy in erythematous, oedematous, and pruritic inflammatory skin lesions.

**For exanthem (rank 3):** The "exanthem" category encompasses a broad spectrum of cutaneous eruptions, from immune-mediated drug reactions and DRESS (Drug Reaction with Eosinophilia and Systemic Symptoms) to lichen planus and viral exanthems. The mechanistic overlap is strongest for immune-mediated subtypes: T-cell–driven cutaneous inflammation — the dominant pathophysiology of lichen planus and DRESS — is precisely the pathway clobetasol suppresses. Crucially, multiple completed Phase 2/3 RCTs already confirm this mechanism in lichen planus and lichen sclerosus, providing indirect but scientifically coherent support. The principal limitation is that "exanthem" is diagnostically broad; viral exanthems and self-limiting drug rashes generally do not require ultra-potent corticosteroids, so clinical refinement of the target subtype is essential before any therapeutic application.

**For acne keloid (rank 4 — acne keloidalis nuchae):** This represents a mechanistically distinct axis. Clobetasol's GR-mediated signalling inhibits TGF-β1 and connective tissue growth factor (CTGF), reducing fibroblast proliferation and collagen over-deposition in the follicular and perifollicular fibrotic papules of the posterior scalp. Ultra-potent topical corticosteroids are already an accepted clinical tool in keloid management, and foam formulations offer superior follicular penetration at the nape-of-neck distribution characteristic of this condition. This indication is particularly clinically relevant in South Africa given the higher prevalence of acne keloidalis nuchae in people of African descent.

**For ranks 1, 2, 5, 6, and 7:** These predictions are not clinically actionable at this stage. Vulvar inverted follicular keratosis (rank 1) is a benign follicular tumour driven by HPV rather than immune inflammation, making the mechanistic link to a corticosteroid tenuous at best. Acrodermatitis chronica atrophicans (rank 2) is a late-stage *Borrelia burgdorferi* bacterial infection requiring systemic antibiotics; topical corticosteroids risk masking infection symptoms and suppressing local immunity. Neonatal dermatomyositis (rank 5) and amyopathic dermatomyositis (rank 7) require systemic immunosuppression, and neonatal systemic absorption of clobetasol creates unacceptable safety risk. The childhood CTD-associated ILD (rank 6) requires systemic corticosteroids or immunosuppressants with pulmonary delivery — topical clobetasol has no viable route to lung tissue.

---

## Clinical Trial Evidence

*Evidence presented for **exanthem** (rank 3), the highest-evidence predicted indication. No registered clinical trials exist for ranks 1, 2, 5, 6, or 7.*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01987076](https://clinicaltrials.gov/study/NCT01987076) | NA | Unknown | 112 | DRESS (Drug Reaction with Eosinophilia and Systemic Symptoms) — the most directly exanthem-relevant trial in this dataset. Examines corticosteroid treatment protocols for this severe multi-organ drug eruption, acknowledging the lack of prior controlled data. Status unknown is a limitation. |
| [NCT05010421](https://clinicaltrials.gov/study/NCT05010421) | Phase 3 | Completed | 246 | Largest completed Phase 3 RCT directly evaluating topical clobetasol for lichen sclerosus vs. non-ablative CO₂ laser. Provides the strongest efficacy dataset for clobetasol in an immune-mediated inflammatory dermatosis closely related to exanthem pathophysiology. |
| [NCT03592342](https://clinicaltrials.gov/study/NCT03592342) | Phase 2 | Completed | 140 | Dose-ranging Phase 2 RCT of Rivelin®-CLO buccal patches (0, 1, 5, and 20 µg clobetasol) for symptomatic oral lichen planus. Provides controlled safety and pharmacodynamic data for a novel mucosal delivery system. |
| [NCT04364555](https://clinicaltrials.gov/study/NCT04364555) | Phase 2/3 | Active, not recruiting | 90 | Multicentre, three-arm placebo-controlled RCT investigating once-daily vs. twice-daily clobetasol oral rinse for symptomatic OLP. Designed to establish the optimal dosing schedule with a robust placebo control. |
| [NCT00102557](https://clinicaltrials.gov/study/NCT00102557) | Phase 2 | Completed | 74 | RCT comparing hydroxychloroquine tablets vs. clobetasol 0.05% oral rinse for OLP; clobetasol was used as the active comparator, confirming its standard-of-care status for chronic mucosal inflammatory conditions. |
| [NCT02573883](https://clinicaltrials.gov/study/NCT02573883) | Phase 3 | Completed | 52 | Phase 3 RCT comparing clobetasol propionate 0.05% ointment vs. fractionated CO₂ laser for vulvar lichen sclerosus; establishes clobetasol as the reference treatment and gold standard for this indication. |
| [NCT02744378](https://clinicaltrials.gov/study/NCT02744378) | Phase 2 | Completed | 68 | Double-blind RCT of tacrolimus 0.1% vs. clobetasol 0.05% for symptomatic OLP conducted in Sri Lanka; provides comparative safety and efficacy data in an Asian population, extending generalisability. |
| [NCT01323673](https://clinicaltrials.gov/study/NCT01323673) | Phase 4 | Completed | 125 | Placebo-controlled Phase 4 RCT of clobetasol propionate ethanol-free foam 0.05% (Olux-E) for chronic hand dermatitis — a common inflammatory exanthem subtype — confirming real-world efficacy. |
| [NCT00393263](https://clinicaltrials.gov/study/NCT00393263) | Phase 2 | Completed | 38 | Double-blind RCT of pimecrolimus 1% cream vs. clobetasol 0.05% cream for vulvar lichen sclerosus; used clobetasol as the gold-standard comparator, with outcome data supporting its superior efficacy for genital inflammatory dermatoses. |
| [NCT06752343](https://clinicaltrials.gov/study/NCT06752343) | Phase 2 | Completed | 29 | Split-mouth RCT comparing photodynamic therapy vs. topical clobetasol for erosive oral lichen planus; confirms clobetasol as the current standard reference treatment for mucosal lichen planus. |

---

## Literature Evidence

*Combined evidence from exanthem (rank 3) and acne keloid (rank 4).*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [16047868](https://pubmed.ncbi.nlm.nih.gov/16047868/) | 2005 | Open-Label Study | *Cutis* | **Direct evidence for acne keloid (rank 4):** Clobetasol propionate 0.05% foam and betamethasone valerate 0.12% foam evaluated in 20 African American patients with acne keloidalis over 8–12 weeks using a pulsed-dose regimen. Both agents were found efficacious and well-tolerated. Clinically significant for South African practice given the high prevalence of this condition in African-descent populations. |
| [34289766](https://pubmed.ncbi.nlm.nih.gov/34289766/) | 2021 | Retrospective Database Study | *Current Medical Research and Opinion* | US database characterisation of generalized pustular psoriasis (GPP) hospitalisations and emergency department visits. GPP presents with disseminated erythematous rash with sterile pustules — a severe exanthem subtype — providing epidemiological context for the high clinical burden of inflammatory exanthems requiring corticosteroid management. |
| [18544295](https://pubmed.ncbi.nlm.nih.gov/18544295/) | 2008 | Case Series | *Journal of Cutaneous Medicine and Surgery* | Two adult cases of Gianotti-Crosti syndrome, a benign self-limited exanthem characterised by a papular eruption typically in children. Adult cases are rare and provide clinical description of an exanthem subtype where topical anti-inflammatory therapy may be considered for symptom relief. |
| [36342724](https://pubmed.ncbi.nlm.nih.gov/36342724/) | 2022 | Case Report | *Journal of Drugs in Dermatology* | Near-erythrodermic but asymptomatic cutaneous eruption ("Flolan Rash") in a patient on long-term IV epoprostenol for pulmonary arterial hypertension, lasting 10 years. Illustrates the spectrum of drug-induced exanthems and the clinical challenge of managing dermatological adverse events in complex patients. |
| [29974124](https://pubmed.ncbi.nlm.nih.gov/29974124/) | 2018 | Case Report | *Singapore Medical Journal* | Tamsulosin-induced photosensitivity rash — a drug-induced exanthem — managed in a dermatological setting. Provides clinical context for drug-induced cutaneous eruptions where topical corticosteroids may provide symptomatic relief. |
| [25878446](https://pubmed.ncbi.nlm.nih.gov/25878446/) | 2015 | Case Report | *International Journal of Trichology* | Acute diffuse and total alopecia associated with *Borrelia* infection (acrodermatitis chronica atrophicans). Relevant to rank 2 as a clinical description; underscores the infectious aetiology of ACA, supporting the conclusion that clobetasol is not appropriate for this indication. |

---

## Safety Considerations

As clobetasol propionate holds **no current SAHPRA registration**, no South African Professional Information (PI) is available. Prescribers should consult internationally approved PIs (EMA, US FDA, MHRA) and exercise clinical judgement regarding the following well-established safety considerations:

- **HPA axis suppression**: Super-potent (Class I) corticosteroid; prolonged use, occlusive dressings, or application to thin-skin or high-absorption sites (face, genitalia, flexures) carries risk of hypothalamic-pituitary-adrenal suppression, iatrogenic Cushing's syndrome, and adrenal insufficiency — particularly relevant for genital indications predicted here.
- **Skin atrophy and striae**: Irreversible thinning, telangiectasiae, and striae with long-term use; especially significant for chronic inflammatory dermatoses requiring maintenance therapy.
- **Paediatric and neonatal absorption**: Systemic absorption is substantially higher in neonates and infants due to increased skin surface area-to-body weight ratio and thinner stratum corneum. Use in neonatal dermatomyositis (rank 5) would carry unacceptable systemic risk.
- **Infection masking**: Application over infectious skin conditions (most relevant to acrodermatitis chronica atrophicans, rank 2) suppresses local immunity, may mask clinical signs of active infection, and risks bacterial dissemination.
- **Secondary infections**: Topical corticosteroids predispose to secondary bacterial and fungal infections, particularly at occluded sites; concurrent antifungal prophylaxis is often recommended for genital applications.

Report all suspected adverse drug reactions to SAHPRA at [www.sahpra.org.za](https://www.sahpra.org.za).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although exanthem (rank 3) is mechanistically plausible and supported by multiple completed Phase 2–3 RCTs for closely related immune-mediated dermatoses, and acne keloid (rank 4) has a directly applicable open-label study relevant to South African clinical demographics, clobetasol propionate is **not currently registered with SAHPRA**, comprehensive South African safety data are absent, and no formal contraindication or warning data is available. These regulatory and safety gaps must be resolved before any repurposing pathway can advance.

**To proceed, the following is needed:**

1. **SAHPRA registration or Section 21 authorisation**: Engage with SAHPRA to explore a registration pathway for clobetasol propionate, or apply for a Section 21 (unregistered medicine) authorisation for specific patient populations under dermatologist supervision.
2. **Complete safety and PI documentation**: Obtain a SAHPRA-equivalent PI from an internationally approved product (FDA, EMA, or MHRA registered) as the minimum safety dataset; address the formal blocking data gap (DG001: warnings/contraindications).
3. **Mechanism of action documentation**: Retrieve the complete MOA entry from DrugBank (DB01013) to formalise the mechanistic rationale for submission — addresses data gap DG002.
4. **Indication refinement for exanthem**: Specify a clinically distinct exanthem subtype — such as immune-mediated drug eruptions, oral lichen planus, or DRESS — rather than pursuing the broad "exanthem" category. Align the target indication with the existing Phase 2/3 trial evidence base.
5. **Feasibility study for acne keloid in South Africa**: Given direct open-label evidence (Callender et al., 2005) and the high clinical relevance to African-descent populations in South Africa, prioritise a prospective observational study or audit of clobetasol foam for acne keloidalis nuchae under specialist dermatological supervision.
6. **Exclude ranks 1, 2, 5, 6, and 7 from further development**: The mechanistic links are weak, the disease biology is incompatible with topical corticosteroid therapy, or safety concerns (infection masking in ACA; systemic absorption in neonatal patients; lack of pulmonary delivery route for CTD-ILD) outweigh any potential benefit at this stage.

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All adverse drug reactions should be reported to SAHPRA.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

