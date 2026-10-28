---
layout: default
title: Abacavir
parent: Model Prediction Only (L5)
nav_order: 11
evidence_level: L5
indication_count: 3
monitor_inn: "ABACAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-29
description: "Abacavir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease and AIDS"
---

# Abacavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Abacavir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Abacavir is a nucleoside reverse transcriptase inhibitor, originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**,
but there are **0 clinical trials** and only **1 preclinical publication** (a combination-regimen study in a cell-culture system) supporting this direction. This is a veterinary indication with limited relevance for human use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease and AIDS (relations recorded in the knowledge graph; the local licence records compiled for this report contain no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9979 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 11 of 11) |
| Number of SAHPRA Registrations | 11 (valid: 11) |
| Recommended Decision | Hold |

**Note on evidence level:** The one cited study examined feline immunodeficiency virus (FIV) replication in vitro. FIV is the virus that causes feline AIDS, but the study tested a three-drug combination (zidovudine, lamivudine and abacavir) and does not isolate abacavir's own effect. It does not directly address the predicted disease as a treated condition, so the evidence level is capped at L5 (model prediction, no directly supporting study).

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, abacavir is a carbocyclic guanosine nucleoside analogue. It is phosphorylated inside cells to carbovir triphosphate, which blocks viral reverse transcriptase and terminates proviral DNA chain elongation.

Feline immunodeficiency virus (FIV) is a lentivirus whose reverse transcriptase is related to that of HIV-1. This is why the cat is used as an animal model for HIV, and several HIV reverse transcriptase inhibitors also act against FIV. A mechanistic rationale therefore exists.

However, the very high TxGNN score most likely reflects the close similarity to the original HIV/AIDS indication and does not independently validate efficacy. The only supporting paper looks at a combination regimen, so abacavir's own contribution cannot be separated. Feline AIDS is a veterinary condition, so it is not a human repurposing target.

Two other predictions were also generated:
- **Simian immunodeficiency virus infection** (score 0.9979): supported only by an in vitro susceptibility study. SIV is mainly a research model for HIV and not a human clinical indication. Evidence level L5.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 0.9978): no trials, no literature and no clear mechanistic link. Evidence level L5.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Preclinical / in vitro study (classified from title only) | Antiviral Research | Tested zidovudine + lamivudine + abacavir combined against FIV replication in vitro. Frames the cat as an animal model for HIV. The effect of abacavir alone cannot be isolated. |

For the related SIV prediction, one in vitro study ([15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/), Antiviral Therapy, 2004) compared the susceptibility of HIV-2, SIV and SHIV to approved anti-HIV-1 drugs. It is indirect, non-clinical evidence only.

## South Africa Market Information

All 11 registrations are valid single-ingredient records. No approved-indication text is available in the licence records compiled for this report. Essential Medicines List (EML) status was not available in the data compiled.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 54/20.2.8/0219 | Vexabax | Film-coated tablet | Not stated in the records |
| Reg. No. 49/20.2.8/0462 | Dumiva Dispersible Tablets | Effervescent tablet | Not stated in the records |
| Reg. No. 44/20.2.8/0293 | Auro Abacavir Lamivudine 600/300Mg Tablets | Film-coated tablet | Not stated in the records |
| Reg. No. 54/20.2.8/0206 | Cagol | Tablet | Not stated in the records |
| Reg. No. 55/20.2.8/0338 | Vuterar | Tablet | Not stated in the records |

Showing 5 of 11 registrations. Several product names (for example Auro Abacavir Lamivudine, Kivexa, Heteruam) suggest fixed-dose combinations, even though the records label them as single-ingredient. Verify against the SAHPRA register before relying on them.

## Safety Considerations

**Contraindication relations recorded in the knowledge graph (not label text):** liver failure, liver disease, fatty liver disease, non-alcoholic steatohepatitis, kidney disease, pancreatitis, gallbladder disease, lactic acidosis, neutropenia, agranulocytosis, anaemia (including macrocytic anaemia), hypertriglyceridaemia, obesity disorders, myopathy and other muscle diseases (including myositis and dermatomyositis), familial periodic paralysis, and pyoureter.

**Drug interactions:** 93 interactions are recorded in total. Those with a stated severity level are rated **Moderate**:
- Naltrexone
- Orlistat

Other listed interactions have no severity rating, including vitamin A, pantoprazole, omeprazole, lansoprazole, glimepiride, metformin, rosiglitazone, morphine, vancomycin, prednisone, hydrocortisone, amphotericin B and sulfasalazine.

Abacavir is also known to carry a risk of HLA-B*57:01-associated hypersensitivity, which would need careful consideration in any new population.

Label warnings and contraindications were not available in the data compiled. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence is one in vitro combination study in a feline virus model, there are no clinical trials, and feline AIDS is a veterinary condition rather than a human indication. The high TxGNN score reflects similarity to the existing HIV indication and is not evidence of new efficacy.

**To proceed, the following is needed:**
- Confirmation of whether a veterinary indication falls within the scope of this human-use repurposing programme
- Abacavir-alone data (not combination regimens) in FIV or SIV models
- Mechanism of action data from DrugBank
- SAHPRA Professional Information (PI) warnings and contraindications, which are currently a blocking gap for safety screening
- Approved-indication text and EML status for the local registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

