---
layout: default
title: Acyclovir
parent: Model Prediction Only (L5)
nav_order: 17
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Acyclovir: predicted new indication Common wart (evidence level L5). Approved use: Herpes simplex, herpes zoster, chickenpox, herpes labialis…"
---

# Acyclovir
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

# Acyclovir: From Herpes Simplex Infection to Common Wart

## One-Sentence Summary

Acyclovir is an antiviral medicine originally used to treat herpes simplex, herpes zoster (shingles), chickenpox, herpes labialis, herpes simplex encephalitis and genital herpes.
The TxGNN model's top-ranked prediction is **punctate epithelial keratoconjunctivitis** (score 99.67%), but the available evidence does not support it. The best-supported prediction is **common wart**, with **4 clinical trials** and **about 19 publications**, one of which is a randomised controlled trial. Because the evidence is clearly stronger for common wart, this report evaluates that indication in detail.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpes simplex, herpes zoster, chickenpox, herpes labialis, herpes simplex encephalitis, genital herpes (the registration records compiled for this report contain no approved indication text) |
| Predicted New Indication | Common wart (best-supported prediction; TxGNN rank 1 is punctate epithelial keratoconjunctivitis) |
| TxGNN Prediction Score | 99.46% for common wart (99.67% for punctate epithelial keratoconjunctivitis) |
| Evidence Level | L2 (common wart) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Proceed with Guardrails (research question only; not for routine clinical use) |

### Other Predicted Indications (Summary)

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Punctate epithelial keratoconjunctivitis | 99.67% | L5 | Hold. The literature retrieved concerns microsporidial keratoconjunctivitis and corneal lipidosis, which do not respond to acyclovir. |
| Common wart | 99.46% | L2 | Research question. Small randomised trials of intralesional use. |
| Post-infectious neuralgia | 99.25% | L5 | Hold. No trials or literature. |
| Hepatitis C induced liver cirrhosis | 99.23% | L5 | Hold. HCV is an RNA virus, so there is no plausible mechanism. |
| Eosinophilic pustular folliculitis | 99.22% | L5 | Hold. No rationale or evidence. |
| Sequela of COVID-19 | 99.16% | L4 | Hold. Evidence concerns treating herpesvirus reactivation, not COVID-19 sequelae. |
| Vulvovaginal candidiasis | 99.11% | L5 | Hold. Acyclovir has no antifungal activity. |
| Papular urticaria | 99.09% | L5 | Hold. No rationale or evidence. |
| Disease of orbital region | 99.08% | L3 | Research question. Mostly an extension of existing herpetic eye uses. |
| Epidemic keratoconjunctivitis | 99.07% | L4 | Hold. The usual cause is adenovirus, which acyclovir does not inhibit effectively. |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. In general, acyclovir is a nucleoside analogue. Herpesvirus thymidine kinase activates it selectively, and it then inhibits viral DNA polymerase. Its efficacy in herpes simplex and herpes zoster is well established.

Common warts are caused by human papillomavirus (HPV), a DNA virus that has no thymidine kinase of its own. Acyclovir's usual selective activation therefore does not apply, and the pharmacological plausibility is limited. Proposed mechanisms include weak inhibition of HPV DNA replication at the high local concentrations reached with intralesional injection, and an immunomodulatory effect. Several small randomised trials, mostly from Egypt, compare intralesional acyclovir with cryotherapy, vitamin D3, Candida antigen, 5-fluorouracil and HPV vaccine. The findings are described as promising, but they come from small, single-region, often open-label studies with different comparators. No Phase 3 confirmation exists.

For the other predictions, the mechanistic link is weak or absent. These include hepatitis C (an RNA virus), vulvovaginal candidiasis (a fungal infection) and epidemic keratoconjunctivitis (usually adenoviral). The orbital-region prediction is mainly herpetic eye disease, where acyclovir already has an established role.

## Clinical Trial Evidence

### Common Wart

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06261684](https://clinicaltrials.gov/study/NCT06261684) | Phase 2/3 | Unknown | 92 | Intralesional acyclovir versus cryotherapy in plantar warts; randomised trial of safety and efficacy |
| [NCT05429151](https://clinicaltrials.gov/study/NCT05429151) | Phase 4 | Unknown | 40 | Intralesional acyclovir (70 mg/ml, every 2 weeks) versus Candida antigen in plantar warts |
| [NCT07448844](https://clinicaltrials.gov/study/NCT07448844) | Phase 4 | Recruiting | 40 | Intralesional vitamin D3 versus acyclovir in common, plantar, flat and periungual warts; primary outcome is complete clearance at week 8 |
| [NCT05324904](https://clinicaltrials.gov/study/NCT05324904) | Not designated | Unknown | 44 | Intralesional vitamin D3 versus acyclovir in plantar warts |

### Disease of Orbital Region (Herpetic Eye Disease, Mostly an Extension of Existing Uses)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06757907](https://clinicaltrials.gov/study/NCT06757907) | Not designated | Completed | 20 | Topical ganciclovir versus systemic acyclovir in herpetic keratitis (acyclovir is the comparator) |
| [NCT05313828](https://clinicaltrials.gov/study/NCT05313828) | Not designated | Unknown | 40 | Treatment modalities for dendritic viral ulcer (HSV keratitis) |
| [NCT03389191](https://clinicaltrials.gov/study/NCT03389191) | Not designated | Unknown | 30 | Oral acyclovir in refractory viral uveitis |

Other trials retrieved for this prediction were judged unrelated or of doubtful relevance: a CMV retinitis study, a neonatal HSV suppression study and a geographic atrophy study of a different drug (ASP7317). They are not listed. No clinical trials were found for the other predicted indications. No SANCTR or PACTR identifiers are available.

## Literature Evidence

### Common Wart

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40889709](https://pubmed.ncbi.nlm.nih.gov/40889709/) | 2026 | RCT | J Am Acad Dermatol | Intralesional acyclovir versus cryotherapy in plantar warts |
| [38822848](https://pubmed.ncbi.nlm.nih.gov/38822848/) | 2024 | RCT | Arch Dermatol Res | Intralesional acyclovir versus hepatitis B vaccine in resistant plantar warts (48 patients completed) |
| [40488756](https://pubmed.ncbi.nlm.nih.gov/40488756/) | 2025 | Comparative study | Arch Dermatol Res | Intralesional acyclovir versus 5-fluorouracil in recalcitrant warts |
| [40056255](https://pubmed.ncbi.nlm.nih.gov/40056255/) | 2025 | Comparative study | Arch Dermatol Res | Intralesional acyclovir versus quadrivalent HPV vaccine in recalcitrant cutaneous warts (60 patients) |
| [37303436](https://pubmed.ncbi.nlm.nih.gov/37303436/) | 2023 | Comparative study | Cureus | Intralesional acyclovir versus PPD immunotherapy in viral warts |
| [34412535](https://pubmed.ncbi.nlm.nih.gov/34412535/) | 2022 | Clinical study | J Cutan Med Surg | Intralesional acyclovir proposed as a potential option for cutaneous warts |
| [41686619](https://pubmed.ncbi.nlm.nih.gov/41686619/) | 2026 | Systematic review and network meta-analysis | Medicine | Compares treatments for cutaneous warts; intralesional acyclovir is described as a novel option |
| [38793636](https://pubmed.ncbi.nlm.nih.gov/38793636/) | 2024 | Case series and review | Viruses | Acyclovir or valaciclovir associated with remission in cases of HPV-related disease (penile condyloma) |
| [26885794](https://pubmed.ncbi.nlm.nih.gov/26885794/) | 2016 | Case report | J Drugs Dermatol | Persistent plantar warts resolved after a 10-day course of oral acyclovir given for herpes zoster |
| [6467981](https://pubmed.ncbi.nlm.nih.gov/6467981/) | 1984 | Report | Cutis | Acyclovir ointment in common warts (verrucae vulgares) |

Several of these are small studies from single regions. The abstracts retrieved for this report do not give full efficacy results, so effect sizes cannot be stated here.

For the other predictions, the literature retrieved is limited to general reviews, case reports and hypotheses. For COVID-19, it mainly describes herpesvirus reactivation. For punctate epithelial keratoconjunctivitis, it concerns microsporidial disease and drug-induced corneal lipidosis. None of it supports a benefit of acyclovir for those indications.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 28/20.2.8/0369 | Adco-acyclovir | Cream (topical) | Not available in the data compiled for this report |
| 38/20.2.8/0129 | Acitab-200 dt | Effervescent (dispersible) tablet (oral) | Not available in the data compiled for this report |

Both registrations are valid single-ingredient products. The data does not state whether acyclovir is on the Essential Medicines List (EML). No injectable formulation is registered in the data compiled for this report. The intralesional regimens studied for warts used the intravenous vial, so this is a practical gap. A topical cream and an oral dispersible tablet are available locally.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these come from model-derived drug-disease links, not from label text, and should be verified against the Professional Information): kidney disease and impaired renal function, hypertension, diabetes mellitus and diabetic ketoacidosis, hyperglycaemia, adrenocortical insufficiency (Addison disease), obesity, stroke and cerebrovascular disease, myocardial infarction, haemolytic-uraemic syndrome, thrombocytopenic purpura, peripheral vascular disease, skin atrophy and telangiectasia. Several of these are atypical for acyclovir and look like links that may belong to other drugs, so interpret them with caution.
- **Drug Interactions**: The interaction screen returned 100 interactions. The ones rated Moderate are:
  - Balsalazide
  - Mesalazine
  - Olsalazine
  - Sulfasalazine
  - Trospium

  Other listed interactions have an unrated (Unknown) severity. Examples are amphotericin B, mannitol, calcitriol, metformin, glimepiride, rosiglitazone, morphine, doxycycline, epinephrine, omeprazole, pantoprazole, lansoprazole, sucralfate, palonosetron and clotrimazole. The remaining interactions were not reviewed here.

Warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available for this report. Please refer to the PI for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (common wart, as a research question only). Hold for all other predicted indications.**

**Rationale:**
- Common wart has the strongest support, with one Phase 2/3 randomised trial and several small randomised comparisons (L2). The trials are small, mostly open-label and from one region, the pharmacological rationale is limited, and there is no Phase 3 confirmation. This supports further study, not routine use.
- The top-ranked TxGNN prediction (punctate epithelial keratoconjunctivitis) and the other high-scoring predictions have no supporting clinical data and mostly lack a plausible mechanism, so they should be held. The orbital-region prediction mainly overlaps with existing herpetic eye uses and is not new repurposing.

**To proceed, the following is needed:**
- Full results of the published trials (efficacy, recurrence, adverse events) and independent replication outside Egypt, ideally in a larger blinded Phase 3 trial against standard care.
- The SAHPRA Professional Information (warnings, contraindications, renal precautions) and confirmation of the approved indications for both local registrations.
- Detailed mechanism of action data, and a review of the knowledge-graph contraindication list against the label.
- A decision on the formulation: the trials used intravenous acyclovir vials injected intralesionally, which are not covered by the two local registrations (cream and oral tablet). Any local study would need regulatory and ethics review, including registration on SANCTR or PACTR.
- Review of the moderate-severity interactions (mesalazine-class drugs and trospium) and of renal function monitoring where systemic use is considered.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

