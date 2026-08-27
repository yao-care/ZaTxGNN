---
layout: default
title: Ritonavir
parent: 僅模型預測 (L5)
nav_order: 393
evidence_level: L5
indication_count: 3
---

# Ritonavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Ritonavir: From HIV-1 Infection to Simian Immunodeficiency Virus (SIV) Infection

## One-Sentence Summary

Ritonavir is an HIV-1 protease inhibitor (also used as a CYP3A4-mediated pharmacokinetic booster for other antiretrovirals) — though this classification comes from the evidence-pack rationale text rather than a completed registry field, since structured original-indication data was not captured for this candidate. The TxGNN model predicts activity against **Simian Immunodeficiency Virus (SIV) Infection**, but SIV is exclusively an animal (macaque) disease model, not a human clinical entity, and the supporting evidence base consists entirely of preclinical/animal studies (**0 clinical trials, 12 publications**) — no human-relevant trial data exists for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in registry data (drug class per evidence rationale: HIV-1 protease inhibitor) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (preclinical / animal and in vitro studies only) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the structured registry record for this candidate. Based on the supporting rationale captured elsewhere in this evidence pack, ritonavir is an HIV-1 protease inhibitor, with well-established clinical use in human HIV-1 infection (commonly as a low-dose pharmacokinetic booster for other protease inhibitors via CYP3A4 inhibition).

SIV is a primate lentivirus closely related to HIV-1, and its protease shares high homology with HIV-1 protease. In vitro susceptibility data in this pack (e.g., PMID 12709355) show SIVmac239 is inhibited by ritonavir at concentrations comparable to those effective against HIV-1, and several animal studies use ritonavir-containing combination antiretroviral therapy in SIV-infected macaques as an HIV cure/reservoir research model. This gives the prediction a plausible biochemical basis.

However, this mechanistic plausibility does not translate into a human indication: SIV infection does not occur naturally in humans, and every piece of supporting evidence is an animal-model or in vitro study used for HIV/AIDS *research purposes*, not treatment of a human disease. It is also worth noting that the other two top-ranked predictions for ritonavir in this same evidence pack — feline acquired immunodeficiency syndrome (a cat-only disease, with the sole "supporting" clinical trial being a mismatched human HIV Phase 4 study per the pack's own relevance grading) and a rare monogenic neurodevelopmental disorder (no mechanistic link, no evidence at all) — are similarly non-actionable. This pattern suggests the near-threshold prediction rank for ritonavir (~rank 699–706) is picking up semantic/keyword associations ("immunodeficiency virus") rather than clinically translatable signals, and reinforces caution in treating the raw TxGNN score alone as an opportunity signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal model | J Virol | Rapid viral decay in SIV-infected macaques on quadruple antiretroviral therapy; models viral dynamics analogous to HIV-1. |
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro susceptibility | Antimicrob Agents Chemother | Ritonavir inhibited SIVmac239 in vitro (EC50 ~13 nM), comparable to its potency against HIV-1 (~25 nM), confirming cross-species protease inhibition. |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Animal/mechanistic | mBio | Lentivirus (HIV) persists in brain microglia/macrophages despite effective ART; reservoir biology relevant across HIV/SIV models. |
| [9875393](https://pubmed.ncbi.nlm.nih.gov/9875393/) | 1998 | Basic science (unrelated compound) | Antiviral Chem Chemother | Tests a different antiviral (fluoroquinolone K-12) against ritonavir-resistant HIV-1 and SIV strains; ritonavir used only as a resistance comparator. |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro susceptibility | Antiviral Therapy | Screened 16 approved anti-HIV-1 drugs (incl. ritonavir) against HIV-2, SIV and SHIV strains for treatment/post-exposure-prophylaxis relevance. |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Animal model | PLoS ONE | SIV-infected macaques on combination ART plus an HDAC inhibitor; studies viral reservoir persistence, not human treatment. |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Animal model | Microbes Infect | Engineered SHIV carrying HIV-1 protease gene, used to test protease inhibitor efficacy in vivo in macaques. |
| [12186895](https://pubmed.ncbi.nlm.nih.gov/12186895/) | 2002 | Mechanistic/basic science | J Virol | HIV-1 Vif protein processing by viral protease; basic virology, not direct ritonavir efficacy data. |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal model | J Virol Methods | Oral HAART including lopinavir/ritonavir in SHIV-infected macaques; assessed impact on CD8 subset. |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal model | PLoS Pathog | Intensified multidrug ART suppressed viremia and restricted the viral reservoir in an SIV-infected macaque AIDS model. |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (SIV infection) is an animal-only disease model with no human clinical relevance — evidence is limited to preclinical/animal and in vitro studies (Evidence Level L4, decision stage S0), with zero clinical trials. Ritonavir is also not currently marketed in South Africa (0 SAHPRA registrations), so there is no existing regulatory foothold to build a repurposing pathway on. The other two top-ranked predictions in this pack (feline AIDS, a rare neurodevelopmental disorder) are similarly non-actionable, indicating this candidate's current prediction set does not surface a clinically usable new indication.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information / warnings and contraindications (currently a blocking data gap)
- Confirmed mechanism-of-action documentation for ritonavir (currently a high-severity data gap)
- A human-relevant predicted indication — re-run or re-review TxGNN output beyond the current top-3, which are dominated by non-human or mechanistically unrelated entities
- If a human indication emerges, confirmation of South African market/registration pathway, since ritonavir is currently unregistered in this market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

