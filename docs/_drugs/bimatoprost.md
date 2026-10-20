---
layout: default
title: Bimatoprost
parent: Model Prediction Only (L5)
nav_order: 70
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Bimatoprost: predicted new indication Alopecia (androgenetic alopecia / female pattern hair loss… (evidence level L5). Approved use: Open-angle glaucoma and ocular hypertension (also hypertrichosis o…"
monitor_inn: "Bimatoprost"
predicted_indications: ["malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "Ambras type hypertrichosis universalis congenita", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "genetic alopecia", "pulmonary arteriovenous malformation (disease)"]
---

# Bimatoprost
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Bimatoprost: From Open-Angle Glaucoma to Alopecia

## One-Sentence Summary

Bimatoprost is a prostamide (prostaglandin F2-alpha analogue) eye drop, originally used to lower eye pressure in open-angle glaucoma and ocular hypertension. It is also used for eyelash hypotrichosis.
The TxGNN model predicts it may be effective for **alopecia** (hair loss), with **11 clinical trials** (including 5 completed Phase 2 studies) and **20 publications** supporting this direction.
The ten highest-scoring predictions for this drug are not all equally credible, and alopecia is the best-supported one (see "Why is This Prediction Reasonable?").

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma and ocular hypertension (also hypertrichosis of the eyelid, i.e. eyelash growth). The SAHPRA registration entries in the data compiled for this report do not include indication text. |
| Predicted New Indication | Alopecia (androgenetic alopecia / female pattern hair loss, plus related entries such as genetic alopecia and alopecia areata) |
| TxGNN Prediction Score | 99.99% (model rank 91) |
| Evidence Level | L2 (completed Phase 2 RCTs; no Phase 3 evidence) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

**Note on prediction selection:** The three highest-scoring predictions were ranked ahead of alopecia by TxGNN, but they have no supporting trials or literature. They are a malformation syndrome with a dental component, a Dandy-Walker malformation syndrome and an isolated genetic hair shaft abnormality. This report focuses on alopecia because it is the prediction with substantive evidence.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for bimatoprost is not available as a formal entry. Based on the rationale compiled for this report, bimatoprost is a prostamide / prostaglandin F2-alpha analogue acting on FP and prostamide receptors. In the eye it lowers intraocular pressure. In the hair follicle, this pathway prolongs the anagen (growth) phase and increases follicle activity.

The link between the original and the new indication is a well-known side effect. Patients using the eye drops for glaucoma grew longer, thicker and darker eyelashes, which led to the approved eyelash hypotrichosis use. Researchers then asked whether the same effect could help scalp hair loss. Several controlled Phase 2 studies in men with androgenetic alopecia and women with female pattern hair loss were run, including comparisons against minoxidil. Phase 1 studies also looked at scalp absorption and tolerability.

There are limits to this evidence:
- No Phase 3 trial for scalp alopecia is present.
- Efficacy compared with established treatments such as minoxidil is not established in the data compiled for this report.
- Results from the Phase 2 trials were not included, only their designs.
- For **alopecia areata** (an autoimmune condition), bimatoprost does not address the immune attack. The supporting evidence is small and indirect: a laser-plus-bimatoprost study and case reports.
- The related entry "genetic alopecia" is largely the same condition as androgenetic alopecia. Its evidence level is inherited from the trials listed here.

The other high-scoring predictions are not credible on current data:
- **Ambras-type hypertrichosis:** probably a label artefact. Bimatoprost promotes hair growth, so it would be expected to worsen an excess-hair disorder.
- **Dandy-Walker syndrome, pulmonary arteriovenous malformation and the dental malformation syndrome:** no plausible mechanistic link.
- **Hypotrichosis simplex of the scalp and congenital hypotrichosis milia:** biologically plausible, but with no disease-specific evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01325337](https://clinicaltrials.gov/study/NCT01325337) | Phase 2 | Completed | 307 | Three doses of bimatoprost solution vs vehicle and OTC minoxidil 5% in men with androgenetic alopecia |
| [NCT01325350](https://clinicaltrials.gov/study/NCT01325350) | Phase 2 | Completed | 306 | Three doses of bimatoprost vs vehicle and minoxidil 2% in women with female pattern hair loss |
| [NCT01904721](https://clinicaltrials.gov/study/NCT01904721) | Phase 2 | Completed | 244 | Safety and efficacy of bimatoprost in men with androgenetic alopecia (second dataset) |
| [NCT02170662](https://clinicaltrials.gov/study/NCT02170662) | Phase 2 | Completed | 33 | Effect of 0.03% bimatoprost on scalp hair growth and androgen-dependent follicles |
| [NCT05600673](https://clinicaltrials.gov/study/NCT05600673) | Phase 1/2 | Completed | 30 | CO2 fractional laser combined with bimatoprost 0.03% in alopecia areata (combination design confounds the bimatoprost effect) |
| [NCT01023841](https://clinicaltrials.gov/study/NCT01023841) | Phase 4 | Completed | 71 | Bimatoprost 0.03% vs vehicle for eyelash hypotrichosis in children |
| [NCT01189279](https://clinicaltrials.gov/study/NCT01189279) | Phase 1 | Completed | 42 | Safety, tolerability and PK of new topical bimatoprost formulations in alopecia |
| [NCT02848300](https://clinicaltrials.gov/study/NCT02848300) | Phase 1 | Completed | 11 | Skin PK and tolerability of two scalp formulations over 14 days in men with androgenetic alopecia |
| [NCT02676310](https://clinicaltrials.gov/study/NCT02676310) | Phase 1 | Terminated | 53 | Dose escalation of safety, tolerability and PK in men with androgenetic alopecia |
| [NCT00187577](https://clinicaltrials.gov/study/NCT00187577) | Not applicable | Completed | 14 | Latanoprost vs bimatoprost for eyelash regrowth in alopecia areata (small, investigator-masked) |

One further registered trial (NCT00999557, eyebrow and eyelash growth after chemotherapy) was withdrawn with zero enrolment and provides no data. No SANCTR or PACTR identifiers were available in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37089845](https://pubmed.ncbi.nlm.nih.gov/37089845/) | 2023 | Non-randomised open-label trial | Indian Dermatol Online J | Bimatoprost vs clobetasol propionate in scalp alopecia areata |
| [35278027](https://pubmed.ncbi.nlm.nih.gov/35278027/) | 2022 | Prospective open-label study | Dermatol Ther | Topical bimatoprost for eyelash loss in alopecia totalis and universalis; evaluated safety and efficacy over at least 12 weeks |
| [40252129](https://pubmed.ncbi.nlm.nih.gov/40252129/) | 2025 | Clinical study | Arch Dermatol Res | CO2 fractional laser plus bimatoprost for hair regrowth in alopecia areata |
| [38794131](https://pubmed.ncbi.nlm.nih.gov/38794131/) | 2024 | Review | Pharmaceuticals (Basel) | Overview of bimatoprost from glaucoma care to hair growth |
| [28264599](https://pubmed.ncbi.nlm.nih.gov/28264599/) | 2017 | Review | Expert Opin Investig Drugs | Bimatoprost for eyelash, eyebrow and scalp alopecia |
| [29854658](https://pubmed.ncbi.nlm.nih.gov/29854658/) | 2018 | Review | Indian Dermatol Online J | Dermatological uses of bimatoprost, including alopecia and vitiligo |
| [25601618](https://pubmed.ncbi.nlm.nih.gov/25601618/) | 2015 | Review | J Am Acad Dermatol | Prostaglandin F2-alpha analogues in androgenetic alopecia, alopecia areata and chemotherapy-induced alopecia |
| [23104985](https://pubmed.ncbi.nlm.nih.gov/23104985/) | 2013 | Translational review | FASEB J | Rationale for prostamide-related therapy in scalp alopecias |
| [27377163](https://pubmed.ncbi.nlm.nih.gov/27377163/) | 2016 | Case report | Pediatr Dermatol | Steroid-resistant paediatric alopecia areata treated successfully with topical bimatoprost |
| [35040730](https://pubmed.ncbi.nlm.nih.gov/35040730/) | 2022 | Preclinical | Drug Deliv | Topical bimatoprost formulation with enhanced skin penetration and hair regrowth in an androgenic alopecia model |

Ten of the 20 publications retrieved are shown above. The other ten are mostly general alopecia reviews and further formulation research.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 56/15.4/0781 | Glauptico | Drops | Not stated in the data compiled; refer to the PI |
| Reg. No. 54/15.4/0389.388 | Timpromat | Drops | Not stated in the data compiled; refer to the PI |

Both registrations are valid single-ingredient products. The data compiled for this report does not state Essential Medicines List (EML) status. Only eye-drop forms are registered, and no scalp or dermal product exists, so any scalp use would be off-label.

---

## Safety Considerations

- **Conditions flagged in drug-disease data (not label text):** liver disease, gallbladder disease, uveitis, iritis and other iris or ciliary body disease, panuveitis, and macular or cystoid macular oedema. Confirm against the SAHPRA PI.
- **Drug interactions:** 66 potential interactions were recorded, none with a severity grade (all unclassified). Examples include prednisone, prednisolone, triamcinolone, simvastatin, metformin, omeprazole, pantoprazole, morphine and ondansetron. Their clinical relevance for topical use is unclear.
- **Scalp-specific points:** the evidence base is limited for irritation and hyperpigmentation with scalp use. Eyelid pigmentation and hypertrichosis are known effects of this drug class.

Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for alopecia). The other top-scoring predictions remain on **Hold**.

**Rationale:**
- Multiple completed Phase 2 controlled trials (about 850 participants across the three largest) in androgenetic alopecia and female pattern hair loss, together with a well-understood follicle mechanism, support feasibility.
- The evidence is limited by the lack of Phase 3 data, unreviewed Phase 2 results, no established advantage over minoxidil, and no registered scalp formulation in South Africa.

**To proceed, the following is needed:**
- Review of the published results of NCT01325337, NCT01325350 and NCT01904721, including efficacy endpoints and comparison with minoxidil.
- Scalp-specific safety assessment (irritation, hyperpigmentation, systemic absorption).
- A defined formulation and dose, since the registered products are eye drops.
- The SAHPRA PI warnings and contraindications for the registered products.
- Formal mechanism-of-action data.
- A regulatory pathway for an unregistered scalp indication or formulation in South Africa.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

