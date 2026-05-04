---
layout: default
title: Betamethasone
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 10
---

# Betamethasone
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

# Betamethasone: From Inflammatory Conditions to Alopecia Areata

---

## One-Sentence Summary

Betamethasone is a potent synthetic glucocorticoid corticosteroid widely used for its anti-inflammatory and immunosuppressive properties across dermatological, rheumatic, and allergic conditions.
The TxGNN model predicts it may be effective for **Alopecia Areata** — an autoimmune condition causing non-scarring hair loss — with **7 clinical trials** and **20 publications** currently supporting this direction.
Evidence ranges from a Cochrane Network Meta-Analysis to multiple RCTs directly testing betamethasone in this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum anti-inflammatory and immunosuppressive therapy (no specific SAHPRA-registered indication found in current data) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| South Africa Market Status | Not found in SAHPRA database — verify directly with SAHPRA, as this is likely a data gap |
| Number of SAHPRA Registrations | 0 (data gap — betamethasone is on the WHO Essential Medicines List and widely available globally) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Alopecia areata (AA) is an autoimmune disease driven by CD8⁺ NKG2D⁺ T cells that disrupt the normal "immune privilege" of hair follicles — the biological shield that usually protects them from immune attack. Once this protection collapses, T cells infiltrate the follicle and trigger sustained inflammation, leading to non-scarring hair loss. The key cytokines driving this process include IL-2, IFN-γ, and TNF-α.

Betamethasone acts directly on this pathological cascade. As a high-potency synthetic glucocorticoid, it binds to the glucocorticoid receptor (GR), suppressing the production of the same pro-inflammatory cytokines that underpin AA. It also down-regulates T-cell infiltration into the follicle and reduces MHC class I expression on follicle cells, effectively restoring some degree of immune tolerance. This mechanistic alignment between betamethasone's pharmacology and AA's core pathology is direct and biologically well-supported.

Importantly, betamethasone is already applied to AA through three distinct routes in clinical practice — topical application, intralesional injection, and oral mini-pulse therapy — each with dedicated clinical trial evidence. This multi-route real-world utilisation further validates the TxGNN prediction and provides a practical implementation framework for South African prescribers.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT06786689](https://clinicaltrials.gov/study/NCT06786689) | Phase 2 | Completed | 60 | Direct RCT comparing weekly Azathioprine pulse vs Betamethasone Oral Mini-Pulse (BOMP) in moderate-to-severe AA; betamethasone was a primary intervention arm and not merely a comparator |
| [NCT05803070](https://clinicaltrials.gov/study/NCT05803070) | N/A | Unknown | 59 | Head-to-head comparison of topical cetirizine 1% vs topical betamethasone valerate 0.1% in localised AA; directly evaluates betamethasone as the target intervention |
| [NCT06087796](https://clinicaltrials.gov/study/NCT06087796) | Phase 1 | Unknown | 60 | Topical pentoxifylline 2% gel and metformin 10% gel vs topical betamethasone valerate 0.1% cream in patchy AA; betamethasone serves as the established standard comparator |
| [NCT02350023](https://clinicaltrials.gov/study/NCT02350023) | Phase 4 | Completed | 50 | Topical latanoprost vs topical corticosteroid (including betamethasone) in localised AA; corticosteroids are the standard-of-care reference arm |
| [NCT03535233](https://clinicaltrials.gov/study/NCT03535233) | Phase 4 | Completed | 40 | Combined topical minoxidil 5% plus potent topical corticosteroid vs intralesional triamcinolone in AA (n=40); evaluates optimal delivery route for corticosteroid therapy |
| [NCT01111981](https://clinicaltrials.gov/study/NCT01111981) | Phase 4 | Unknown | 30 | Clobetasol propionate 0.05% foam in Central Centrifugal Cicatricial Alopecia; related corticosteroid in a different alopecia subtype — indirect class-level evidence only |
| [NCT04207931](https://clinicaltrials.gov/study/NCT04207931) | Phase 4 | Recruiting | 250 | Multicenter prospective study examining treatment outcomes across therapies in Central Centrifugal Cicatricial Alopecia; indirect relevance to betamethasone in AA |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Network Meta-Analysis | Cochrane Database of Systematic Reviews | Comprehensive NMA evaluating all major treatments for AA including immunosuppressants and hair growth stimulants; represents the highest available evidence tier for treatment hierarchy in AA |
| [34400956](https://pubmed.ncbi.nlm.nih.gov/34400956/) | 2021 | RCT | Iranian Journal of Pharmaceutical Research | Double-blind placebo-controlled RCT (n=36) comparing oral betamethasone pulse (3 mg/week) vs methotrexate vs combination in severe AA; provides direct evidence for betamethasone efficacy as monotherapy |
| [39393548](https://pubmed.ncbi.nlm.nih.gov/39393548/) | 2025 | RCT | Journal of the American Academy of Dermatology | RCT evaluating microneedle transdermal delivery of compound betamethasone in AA; demonstrates improved drug delivery with significantly reduced procedural pain vs standard intralesional injection |
| [40510104](https://pubmed.ncbi.nlm.nih.gov/40510104/) | 2025 | RCT | Cureus | Non-blinded RCT (n=60) comparing oral cyclosporine (3 mg/kg) vs betamethasone mini-pulse in AA; provides head-to-head evidence for systemic therapy selection |
| [38623137](https://pubmed.ncbi.nlm.nih.gov/38623137/) | 2024 | Comparative RCT | Cureus | Comparative study of topical betamethasone dipropionate vs topical minoxidil in AA patients; directly assesses relative efficacy of betamethasone in the topical route |
| [40519428](https://pubmed.ncbi.nlm.nih.gov/40519428/) | 2025 | Prospective Clinical Study | Cureus | Prospective assessment of oral betamethasone mini-pulses in moderate-to-severe AA; supports intermittent dosing regimen as a viable alternative to continuous systemic corticosteroids |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Systematic Review | Dermatology Practical & Conceptual | Systematic review of corticosteroid pulse therapy across all subtypes of AA; summarises efficacy, relapse rates, side effects, and prognostic factors |
| [36257912](https://pubmed.ncbi.nlm.nih.gov/36257912/) | 2022 | Comparative Clinical Study | Dermatologic Therapy | Multi-arm blinded RCT (n=108 across 6 groups) comparing latanoprost, minoxidil, betamethasone, and their combinations; provides nuanced comparative data across treatment combinations |
| [36114868](https://pubmed.ncbi.nlm.nih.gov/36114868/) | 2023 | Clinical Trial | Archives of Dermatological Research | Evaluates fractional CO₂ laser alone vs combined with betamethasone valerate cream in AA; supports combination strategy and quantifies betamethasone's additive contribution |
| [32594786](https://pubmed.ncbi.nlm.nih.gov/32594786/) | 2022 | Within-patient RCT | Journal of Dermatological Treatment | Within-patient RCT directly comparing intralesional betamethasone vs triamcinolone acetonide in localised AA; provides the only head-to-head corticosteroid comparison at this route of administration |

---

## South Africa Market Information

According to the current Evidence Pack, no SAHPRA registrations for betamethasone were found in the database queried. This is very likely a **data gap** rather than a true absence, given that betamethasone is:

- Included on the **WHO Essential Medicines List**
- A commonly stocked generic corticosteroid available globally in topical, injectable, and oral formulations
- Widely referenced in clinical practice guidelines

**Recommended action:** Confirm current registration status directly on the [SAHPRA MCC website](https://www.sahpra.org.za) or via the South African Medicines Formulary (SAMF). Check whether betamethasone formulations are included in the **National Essential Medicines List (NEML)** — particularly topical betamethasone valerate or dipropionate, which are commonly available in public health facilities.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

> **Practical guidance for prescribers:** Betamethasone is a high-potency glucocorticoid. As a class, prescribers should be aware of standard corticosteroid risks including hypothalamic-pituitary-adrenal (HPA) axis suppression with prolonged or high-dose use, skin atrophy and telangiectasia with extended topical application, immunosuppression, and systemic effects in vulnerable populations (children, elderly, patients with diabetes or osteoporosis). For the oral mini-pulse regimen specifically evaluated in AA trials, the once-weekly intermittent schedule is intended to minimise systemic side effects while maintaining therapeutic efficacy. Consult the current SAMF or SAHPRA-approved PI for contraindications, dose adjustments, and drug interaction guidance.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Betamethasone has a mechanistically direct and biologically plausible rationale for use in alopecia areata, supported by a Cochrane Network Meta-Analysis, multiple completed RCTs (including one Phase 2 RCT directly comparing betamethasone to an active comparator), and an established multi-route clinical evidence base — collectively placing this at Evidence Level L2 with a clear pathway for structured implementation.

**To proceed, the following is needed:**

- **Confirm SAHPRA registration:** Verify current registration of specific betamethasone formulations (topical valerate/dipropionate, injectable, oral) with SAHPRA and confirm NEML inclusion status
- **Obtain approved PI:** Retrieve SAHPRA-approved Professional Information documents for formal safety, contraindication, and drug interaction review before clinical implementation
- **Define the treatment protocol:** Select the most appropriate route for the target patient population (topical for localised AA; oral mini-pulse for moderate-to-severe disease) and establish standardised dosing and monitoring intervals
- **Safety monitoring plan:** Develop monitoring protocols for HPA axis function, skin atrophy (topical route), and glycaemic control, particularly for extended therapy
- **Pharmacovigilance alignment:** Register anticipated use cases with the South African pharmacovigilance system and establish a mechanism for reporting adverse drug reactions to SAHPRA as real-world evidence accumulates in the local population

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. YMYL content — consult a qualified healthcare professional before making any prescribing decisions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

