---
layout: default
title: Stavudine
parent: 僅模型預測 (L5)
nav_order: 416
evidence_level: L5
indication_count: 3
---

# Stavudine
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

# Stavudine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Stavudine (d4T) is a nucleoside reverse transcriptase inhibitor (NRTI) historically used to treat HIV-1 infection in humans. The TxGNN model predicts a possible link to **feline acquired immunodeficiency syndrome (FIV)** — a veterinary, not human, condition — supported currently by **0 clinical trials** and only **2 publications**, neither of which studies stavudine itself. The evidence base for this specific prediction is weak and largely non-applicable to human repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (NRTI antiretroviral) — detailed SAHPRA-approved indication text not available, as the product is not currently registered/marketed in South Africa |
| Predicted New Indication | Feline acquired immunodeficiency syndrome (a veterinary condition, not a human disease) |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation for stavudine is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology, stavudine is an NRTI: after intracellular phosphorylation it competitively inhibits HIV reverse transcriptase and causes DNA chain termination, the same general mechanism class used against other lentiviruses.

The two supporting publications, however, do not actually test stavudine. Both describe **stampidine**, a structurally modified aryl phosphoramidate **prodrug derived from stavudine**, evaluated in dogs and in cats infected with feline immunodeficiency virus (FIV) — a veterinary lentivirus distinct from HIV. While stampidine and stavudine share a d4T-derived nucleoside backbone and a broadly similar reverse-transcriptase-inhibition mechanism, stampidine was specifically engineered to improve cellular penetration and antiviral potency, so its pharmacokinetic and efficacy data cannot be directly extrapolated to stavudine itself.

In addition, FIV is a veterinary indication affecting cats, not a human disease. Even if the mechanistic rationale (NRTI activity against a lentivirus) is plausible in principle, this specific predicted indication has no direct relevance to human therapeutic use, which limits its practical value as a human drug-repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16570826](https://pubmed.ncbi.nlm.nih.gov/16570826/) | 2006 | Animal pharmacokinetics/toxicity study | Arzneimittel-Forschung | Studied **stampidine** (a stavudine-derived prodrug, not stavudine itself) in beagle dogs and FIV-infected domestic cats; found therapeutic plasma levels achievable at non-toxic oral doses. Not a human study. |
| [12654652](https://pubmed.ncbi.nlm.nih.gov/12654652/) | 2003 | Animal antiviral activity study | Antimicrobial Agents and Chemotherapy | Single oral doses of **stampidine** (not stavudine) transiently reduced FIV viral load in chronically infected cats with no observed side effects. Not a human study. |

*Note: Both publications concern stampidine, a chemically modified prodrug of stavudine, evaluated in a veterinary (feline) context — not clinical evidence for stavudine in humans.*

---

## South Africa Market Information

No SAHPRA registration records are available — stavudine is currently **not marketed** in South Africa (0 licenses on file).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(No key warnings, contraindications, or drug interaction data were available in this evidence pack — retrieval of the formal product label is flagged as a blocking data gap.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L4 (preclinical/mechanism-only), with no clinical trials and only two animal studies — both of which test a different compound (stampidine) rather than stavudine, in a veterinary rather than human indication. The high TxGNN score is not corroborated by directly relevant evidence, so this candidate does not currently support progression.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information / label data (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism-of-action documentation from DrugBank
- Direct evidence (in vitro, animal, or clinical) using stavudine itself, not its prodrug derivatives
- Reassessment of whether a human-relevant indication exists — the related candidate "simian immunodeficiency virus infection" (rank 2, evidence level L4, decision stage S1, "Research Question") may warrant separate preclinical follow-up, though it too currently lacks stavudine-specific efficacy data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

