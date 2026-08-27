---
layout: default
title: Nitrofurantoin
parent: 僅模型預測 (L5)
nav_order: 334
evidence_level: L5
indication_count: 10
---

# Nitrofurantoin
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

# Nitrofurantoin: From Urinary Tract Infection to Rheumatoid Arthritis

## One-Sentence Summary

> Nitrofurantoin is a long-established antibacterial primarily used to treat urinary tract infections (the drug is not currently marketed in South Africa, with 0 SAHPRA registrations on record).
> The TxGNN model predicts a possible link to **Rheumatoid Arthritis**, with a prediction score of **99.89%**, but **0 clinical trials** and **12 publications** are currently associated with this pairing — and critically, the literature retrieved is predominantly about nitrofurantoin-*induced* harm (pulmonary fibrosis, autoimmune-type reactions), not therapeutic benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (established antibacterial use; not captured in the supplied registration data) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for nitrofurantoin is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on known pharmacology, nitrofurantoin is a nitrofuran-class antibacterial that is reduced by bacterial flavoproteins into reactive intermediates that damage bacterial DNA, ribosomal proteins, and metabolic enzymes — a mechanism specific to bacterial cell biology, with no established immunomodulatory or anti-rheumatic pathway.

Unlike a typical repurposing case where the original and new indications share a plausible pharmacological link, the literature surfaced here does **not** support a therapeutic connection between nitrofurantoin and rheumatoid arthritis (RA). Instead, the retrieved publications point in the opposite direction: one cohort study found antibiotic exposure (including nitrofurans) associated with *flares* of RA rather than benefit; several case reports and reviews describe nitrofurantoin-induced pulmonary fibrosis, including a documented case where the drug caused irreversible lung injury specifically in an RA patient already on methotrexate; and RA itself is independently recognized as a risk factor for interstitial lung disease, compounding this risk.

Given this, the high TxGNN score is best interpreted as a graph-embedding artifact — nitrofurantoin and RA are likely connected in the knowledge graph through shared "lung/pulmonary complication" or "autoimmune" nodes rather than through any genuine therapeutic mechanism. This is a pattern seen across nearly all of this drug's top 10 predicted indications (see Conclusion), several of which are instead documented **adverse-reaction associations** (e.g., methemoglobinemia) rather than repurposing candidates.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Self-controlled case series (Cohort) | Scientific Reports | Antibiotic use (including nitrofurans) was associated with **flares** of RA in a UK cohort of 31,992 patients — an inverse signal, not supportive of benefit |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | Lists nitrofurantoin among drugs causing pulmonary fibrosis; notes RA itself predisposes to the same condition |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case Report | Cureus | Irreversible pulmonary fibrosis from methotrexate + nitrofurantoin interaction in a 94-year-old RA patient treated for UTI |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du praticien | Nitrofurantoin listed among antibiotics causing drug-induced interstitial lung disease |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort/Retrospective | Chest | RA patients hospitalized for interstitial lung fibrosis had poor prognosis; drug not a treatment in this context |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case Report | Annales de Dermatologie et de Vénéréologie | Drug-induced sialadenitis case series naming nitrofurantoin among culprit drugs (not RA-related) |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | Cohort/Screening study | Acta Medica Scandinavica | Short-term nitrofurantoin therapy outcomes for bacteriuria; no RA relevance |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case Report | Cureus | Autoimmune hepatitis workup listing nitrofurantoin among drugs to rule out as cause, alongside RA as a differential diagnosis |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Case Report | Revue de Pneumologie Clinique | Gold-salt–induced pneumonitis case (RA context); nitrofurantoin not the causative agent |
| [4608019](https://pubmed.ncbi.nlm.nih.gov/4608019/) | 1974 | Review | Der Internist | General review of alveolitis/pulmonary fibrosis mentioning nitrofurantoin as one causative drug class |

---

## South Africa Market Information

No SAHPRA registrations are on record for nitrofurantoin in this dataset (total_licenses = 0; market status: Not marketed).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Signals identified during this evidence review** (not from formal PI data, but recurring across the retrieved literature and worth flagging for any repurposing assessment):
- Multiple reports of nitrofurantoin-induced **pulmonary fibrosis/interstitial lung disease**, with one case of irreversible injury when combined with methotrexate in an RA patient (PMID 35145797).
- Documented **methemoglobinemia** induction (photoactivation-related, and in neonatal case reports) associated with nitrofurantoin elsewhere in this evidence pack's predicted-indication list — a mechanistic contraindication signal, not a treatment rationale.
- Nitrofurantoin appears among drugs implicated in **drug-induced autoimmune hepatitis** differentials.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.89% TxGNN score is not supported by the retrieved evidence — there are no clinical trials, and the 12 literature hits are predominantly reports of nitrofurantoin causing harm (pulmonary fibrosis, flares, hepatic/hematologic adverse reactions) rather than evidence of benefit in RA. The drug is also not currently marketed in South Africa (0 SAHPRA registrations), which is an independent barrier to any near-term clinical use regardless of the efficacy question.

**To proceed, the following is needed:**
- SAHPRA/TFDA-approved Professional Information (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action data to assess biological plausibility (High-severity data gap, DG002)
- A genuine positive pharmacological hypothesis linking nitrofurantoin to RA pathogenesis (none currently identified)
- If pursued further, prospective safety monitoring given the documented pulmonary and hematologic signal, particularly in patients on concomitant methotrexate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

