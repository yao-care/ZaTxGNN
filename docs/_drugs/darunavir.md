---
layout: default
title: Darunavir
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 4
---

# Darunavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Darunavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Darunavir is a second-generation HIV-1 protease inhibitor widely used in combination antiretroviral therapy (cART) for the treatment of HIV/AIDS. The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**, with **0 clinical trials** and **4 publications** (all non-human primate studies) currently supporting this direction. Notably, SIV is the standard translational animal model for HIV research, making this prediction a reflection of known pharmacological cross-reactivity rather than a novel repurposing opportunity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (antiretroviral combination therapy) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 (Preclinical / animal studies only) |
| South Africa Market Status | Not marketed (no SAHPRA registrations on record) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. However, darunavir is a well-characterised second-generation HIV-1 protease inhibitor (PI). It works by binding to the active site of HIV-1 protease with high affinity, blocking the cleavage of viral Gag and Gag-Pol polyproteins. This prevents the maturation of infectious viral particles. Darunavir is notable for its high genetic barrier to resistance and is a cornerstone of modern antiretroviral regimens.

SIV (Simian Immunodeficiency Virus) and HIV-1 both belong to the *Lentivirus* genus, and their protease enzymes share high structural homology. Darunavir, as an HIV-1 protease inhibitor, can cross-inhibit SIV protease activity, blocking polyprotein cleavage and viral particle maturation. The published non-human primate (NHP) literature confirms that darunavir-containing cART regimens effectively suppress SIV replication in rhesus macaques to clinically relevant levels.

It is important to note that SIV infection in primates is the **standard translational model** for HIV research — it is not an independent clinical indication for human drug repurposing. The TxGNN model's prediction reflects the well-known pharmacological relationship between HIV and SIV rather than identifying a genuinely novel therapeutic application. This prediction is scientifically valid but of limited actionable value for human drug repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered for darunavir specifically in simian immunodeficiency virus infection.

> **Note on related trials:** One Phase 4 trial ([NCT02770508](https://clinicaltrials.gov/study/NCT02770508)) was identified under the second predicted indication (feline AIDS) but was determined to be a **mapping error** — this is actually a human HIV-1 trial comparing boosted darunavir + lamivudine vs. boosted darunavir + tenofovir/emtricitabine (n=145, completed 2017). It does not provide evidence for any of the predicted non-HIV indications.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Animal Study (NHP) | AIDS Res Hum Retroviruses | Evaluated two novel cART regimens (including darunavir) in SIVmac239-infected rhesus macaques; demonstrated effective suppression of SIV replication to clinically relevant levels |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Animal Study (NHP) | PLoS One | Studied SIV-infected Chinese rhesus macaques on intensive cART (including darunavir) combined with HDAC inhibitor SAHA; explored viral reservoir reduction strategies |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal Study (NHP) | PLoS Pathog | Tested highly intensified ART (including darunavir) in SIVmac251-infected rhesus macaques across a wide viremia range (10³–10⁷ copies/mL); achieved long-term viral suppression and viral reservoir restriction |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Animal Study (NHP) | AIDS | Evaluated gold compound auranofin alongside cART (including darunavir) in SIV model; demonstrated restriction of viral reservoir and viral load containment following ART suspension |

> **Evidence quality note:** All four publications are non-human primate (NHP) animal studies. No human clinical data exists for this specific indication. These studies use darunavir as a component of multi-drug cART regimens in SIV-infected macaques, serving as translational models for HIV cure research.

## South Africa Market Information

No SAHPRA registrations found for darunavir in the current dataset.

> **Note:** Darunavir (brand name Prezista®) is widely registered internationally and is included on the WHO Model List of Essential Medicines. Healthcare professionals in South Africa should verify current SAHPRA registration status and Essential Medicines List (EML) inclusion directly with SAHPRA, as this dataset may not reflect the most current regulatory status.

## Additional Predicted Indications Overview

The TxGNN model generated four predicted indications for darunavir. Given the limited actionable value of the primary prediction, all four are summarised below for completeness:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Mechanistic Assessment | Recommendation |
|------|---------------------|-------------|----------------|----------------------|----------------|
| 1 | Simian immunodeficiency virus infection | 99.97% | L4 | Strong — SIV/HIV protease homology; standard translational model, not novel repurposing | Hold |
| 2 | Feline acquired immunodeficiency syndrome | 99.97% | L4 | Weak to moderate — FIV protease shares only ~25–30% homology with HIV-1 protease; veterinary indication, not applicable to human use | Hold |
| 3 | Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.97% | L5 | No known link — rare genetic neurodevelopmental disorder; HIV PI has no known myelin-protective or neurodevelopmental mechanism; likely a knowledge graph topology artefact | Hold |
| 4 | Obsolete familial combined hyperlipidaemia | 99.19% | L5 | **Adverse relationship** — HIV protease inhibitors are known to *cause* dyslipidaemia (elevated triglycerides, cholesterol) via SREBP pathway interference; darunavir would likely worsen, not treat, this condition | Hold |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> **General safety note for darunavir (from established literature):**
> - Darunavir must be co-administered with a pharmacokinetic booster (ritonavir or cobicistat)
> - Known metabolic effects include dyslipidaemia and hyperglycaemia
> - Hepatotoxicity risk — liver function monitoring recommended
> - Severe skin reactions (including Stevens-Johnson syndrome) have been reported
> - Significant CYP3A4 interactions — extensive drug-drug interaction potential
> - Sulphonamide allergy cross-reactivity (darunavir contains a sulphonamide moiety)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The primary TxGNN prediction (SIV infection) reflects the well-established pharmacological relationship between HIV-1 and SIV protease inhibition — this is the basis of the standard NHP translational model for HIV research, not a novel drug repurposing opportunity. The remaining predicted indications are either veterinary (feline AIDS), unsupported by any mechanistic rationale (neurodevelopmental disorder), or represent an **adverse effect** of the drug class (hyperlipidaemia). None of the four predictions offer actionable repurposing value for human clinical application in South Africa.

**To proceed, the following would be needed:**
- Identification of genuinely novel human disease indications beyond the known HIV/lentivirus relationship
- Detailed mechanism of action data (MOA) from DrugBank to explore any off-target pharmacological activities
- SAHPRA Professional Information (PI) for complete safety, warnings, and contraindications data
- Verification of current SAHPRA registration status for darunavir (Prezista®)
- If SIV model research is of interest for HIV cure strategies, collaboration with NHP research centres would be the appropriate pathway rather than drug repurposing

---

*This report was generated on 2026-04-05 based on Evidence Pack v4 (data cutoff: 2026-04-05). Results are for research reference only and do not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

