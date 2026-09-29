---
layout: default
title: Cysteine
parent: Model Prediction Only (L5)
nav_order: 158
evidence_level: L5
indication_count: 10
---

# Cysteine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Cysteine: From an Unspecified Registered Indication to Dry Eye Syndrome

## One-Sentence Summary

Cysteine is an amino acid found in three SAHPRA-registered products in South Africa, but the records provided do not state an approved indication.
The TxGNN model predicts it may be effective for **dry eye syndrome**, with **7 retrieved clinical trials** and **20 retrieved publications**.
The direct evidence is thin. Only 1 trial (NCT04793646) is rated moderately relevant, and it is Phase NA. Almost all human data involve N-acetylcysteine (NAC) or cysteine-modified polymers, not free cysteine.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA records provided (all three registrations have blank indication text) |
| Predicted New Indication | Dry eye syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 (the Evidence Pack labelled L2, but no completed Phase 2/3 RCT of cysteine or NAC in dry eye was retrieved, so I downgraded it) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for cysteine is not available in the Evidence Pack. Cysteine is the precursor of glutathione, the body's main antioxidant. It is also the parent molecule of N-acetylcysteine (NAC), which has antioxidant, mucolytic and anti-inflammatory effects.

Dry eye disease involves oxidative stress on the ocular surface and an unstable, mucin-rich tear film. NAC is thought to help by scavenging reactive oxygen species and by loosening mucus through disulfide-bond cleavage. Thiolated polymers such as chitosan-NAC and L-cysteine conjugates also stick better to mucus, which prolongs contact time on the eye.

**Caveats:**
- **Indirect evidence.** All clinical and preclinical evidence concerns NAC or cysteine conjugates, so extrapolating to free cysteine is indirect.
- **Conflicting signal.** Topical NAC has been used to create a *mucin-deficient dry eye* animal model (PMID 30025127), so its effect on the ocular surface is not simply beneficial.
- **Formulation and route.** The registered cysteine products are a wound powder and parenteral infusions. None is an ophthalmic formulation, so route compatibility has not been established.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04793646](https://clinicaltrials.gov/study/NCT04793646) | Phase NA | Completed | 60 | Randomised, double-blind study of NAC for dryness symptoms in primary Sjögren's syndrome. Results are not in the pack. Most relevant trial, but the target condition is Sjögren's dryness, not dry eye specifically. |
| [NCT04440280](https://clinicaltrials.gov/study/NCT04440280) | Phase 2 | Recruiting | 45 | Topical NAC eye drops to reduce oxidative stress in Fuchs endothelial corneal dystrophy. Similar antioxidant rationale, but a different eye disease. |
| [NCT01064830](https://clinicaltrials.gov/study/NCT01064830) | Phase 2 | Completed | 21 | Topical cyclosporine under occlusion for brittle nail syndrome. Cysteine deficiency is mentioned only as a possible cause. Not a cysteine intervention. |
| [NCT01424033](https://clinicaltrials.gov/study/NCT01424033) | Phase 2/3 | Terminated | 5 | Oral NAC tolerability in connective-tissue-disease interstitial lung disease. Wrong disease, and terminated after 5 patients. |

Three further trials (NCT03525678, NCT04162210, NCT03544281) are belantamab mafodotin oncology studies. They were matched only because corneal toxicity is an adverse event of that drug, and they have no cysteine link, so they are not listed. No SANCTR or PACTR registrations were found.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28441068](https://pubmed.ncbi.nlm.nih.gov/28441068/) | 2017 | RCT | J Ocul Pharmacol Ther | Controlled, double-blind study of chitosan-NAC eye drops on tear film thickness in dry eye syndrome. Only the aim is available in the pack. |
| [39360368](https://pubmed.ncbi.nlm.nih.gov/39360368/) | 2024 | RCT | Clin Exp Rheumatol | Placebo-controlled, double-blind study of NAC for dryness symptoms in Sjögren's disease. Only the aim is available in the pack. |
| [16334742](https://pubmed.ncbi.nlm.nih.gov/16334742/) | 2005 | Clinical comparison | Acta Med Croat | Local acetylcysteine compared with artificial tears in dry eye syndrome. |
| [34339721](https://pubmed.ncbi.nlm.nih.gov/34339721/) | 2022 | Review | Surv Ophthalmol | Review of 106 references on topical NAC in eye disease: mechanisms, applications and adverse effects. |
| [24993428](https://pubmed.ncbi.nlm.nih.gov/24993428/) | 2014 | Review | J Control Release | Thiolated polymers (thiomers) bind mucus through disulfide bonds with cysteine-rich glycoproteins. |
| [40123221](https://pubmed.ncbi.nlm.nih.gov/40123221/) | 2025 | Preclinical | Adv Mater | Eye-drop nanoformulation of catalase with cysteine-modified chitosan, targeting ROS in dry eye. |
| [39842600](https://pubmed.ncbi.nlm.nih.gov/39842600/) | 2025 | Preclinical | Int J Biol Macromol | NAC-chitosan conjugate on dexamethasone lipid carriers: better corneal retention and permeability. |
| [36581034](https://pubmed.ncbi.nlm.nih.gov/36581034/) | 2023 | Preclinical | Int J Biol Macromol | Chondroitin sulfate-L-cysteine conjugate on lipid carriers: better corneal permeation and retention. |
| [30025127](https://pubmed.ncbi.nlm.nih.gov/30025127/) | 2018 | Animal study | Invest Ophthalmol Vis Sci | Topical NAC used to create a mucin-deficient dry eye model, which is a caution signal. |
| [26606856](https://pubmed.ncbi.nlm.nih.gov/26606856/) | 2015 | Preclinical | Ther Deliv | Hyaluronic acid modified with cysteine ethyl ester, evaluated as a mucoadhesive lubricant. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G2370 (ACT 101/1965) | Cicatrin Powder 15G | Powder | Not stated in the records provided |
| 52/25/0739 | Numeta G13E | Infusion | Not stated in the records provided |
| 52/25/0740 | Numeta G16E | Infusion | Not stated in the records provided |

The pack contains no ophthalmic dosage form, and it gives no Essential Medicines List (EML) status.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but the supporting evidence is indirect: NAC and cysteine-conjugate studies, several with only abstract stubs and no reported results. No completed Phase 2/3 RCT of cysteine in dry eye was found. SAHPRA safety data are missing (a blocking gap), and there is no ophthalmic product registered in South Africa. This is a research question, not a candidate ready for clinical use.

**To proceed, the following is needed:**
- SAHPRA Professional Information for all three registered products (safety, contraindications, approved indications)
- Mechanism of action data from DrugBank
- Full results of NCT04793646 and RCTs 28441068 and 39360368, to judge whether the benefit applies to dry eye and to free cysteine rather than NAC or conjugates
- Reconciliation of the mucin-deficient dry eye model finding (PMID 30025127) with the proposed benefit
- An ophthalmic formulation and route-compatibility assessment
- Curation of the duplicate glaucoma entries (closed-angle and angle-closure), which the Evidence Pack recommends merging

This report covers the top-ranked prediction only. The other nine predictions, including tracheal disease (L4, mucolytic rationale), are unassessed here.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

