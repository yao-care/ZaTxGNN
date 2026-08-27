---
layout: default
title: Isoniazid
parent: 僅模型預測 (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
---

# Isoniazid
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

# Isoniazid: From Tuberculosis to Conjunctivitis

## One-Sentence Summary

Isoniazid is a first-line antimycobacterial agent long used to treat and prevent tuberculosis. The TxGNN model predicts a strong association with **Conjunctivitis** (score 99.36%), but the supporting evidence — **1 clinical trial** and **20 publications** — largely describes isoniazid-related ocular adverse effects and tuberculous eye disease rather than a genuine therapeutic benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (established antimycobacterial use; no SAHPRA-approved indication text is available in this evidence pack, as the product is not currently registered in South Africa) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacological knowledge, isoniazid inhibits mycolic acid synthesis in the mycobacterial cell wall (via the InhA/KasA pathway) and is used almost exclusively for tuberculosis treatment and latent TB infection prevention.

There is no known anti-inflammatory or antimicrobial mechanism by which isoniazid would treat ordinary (bacterial, viral, or allergic) conjunctivitis. Reviewing the supporting literature shows the association arises from two unrelated phenomena: (1) case reports describing isoniazid itself *causing* ocular adverse reactions, and (2) case reports of conjunctival tuberculosis — i.e., the eye being infected by the same organism isoniazid is used to treat, not evidence that isoniazid treats conjunctivitis as a general condition.

In short, the TxGNN similarity score is high, but the directionality of the clinical signal is reversed — it reflects a drug-adverse-effect / disease-overlap relationship rather than a therapeutic one. This should be treated as a caution flag rather than supporting evidence for repurposing.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04094012](https://clinicaltrials.gov/study/NCT04094012) | Phase 3 | Completed | 490 | Compared systemic adverse drug reaction rates between 3HP (rifapentine + isoniazid) and 1HP regimens for latent TB infection treatment; not designed to evaluate conjunctivitis outcomes — included only as a general isoniazid safety background trial (relevance grade C). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5005929](https://pubmed.ncbi.nlm.nih.gov/5005929/) | 1971 | Unclassified | Annals of Ophthalmology | Brief report titled "Rifampicin," concerning ocular effects of an anti-TB co-medication; no abstract available. |
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Review | Optometry Clinics | Reviews ocular side effects of systemic drugs; notes conjunctivitis/blepharoconjunctivitis has been associated with several drug classes — an adverse-effect review, not efficacy evidence. |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case Report | Archives of Ophthalmology | Describes primary tuberculosis of the conjunctiva — a disease case, not a treatment-response report. |
| [32674602](https://pubmed.ncbi.nlm.nih.gov/32674602/) | 2020 | Case Report | Clinical Pediatrics | Adolescent case of conjunctivitis with an unexpected (infectious/TB-related) cause. |
| [12226788](https://pubmed.ncbi.nlm.nih.gov/12226788/) | 2002 | Unclassified | Deutsche Medizinische Wochenschrift | Reactive arthritis and conjunctivitis following intravesical BCG instillation for bladder cancer — an immune reaction, unrelated to isoniazid efficacy. |
| [10084173](https://pubmed.ncbi.nlm.nih.gov/10084173/) | 1999 | Unclassified | Revue du Rhumatisme | Review of 26 cases of polyarthritis (with associated conjunctivitis) following intravesical BCG immunotherapy. |
| [26692731](https://pubmed.ncbi.nlm.nih.gov/26692731/) | 2015 | Case Report | Middle East African Journal of Ophthalmology | Case of tuberculous conjunctivitis in an anophthalmic socket — active TB infection of ocular tissue. |
| [14195962](https://pubmed.ncbi.nlm.nih.gov/14195962/) | 1964 | Case Report | Southern Medical Journal | Report of toxic epidermal necrolysis, a severe drug reaction; relevance to conjunctivitis unclear from title alone. |
| [10084171](https://pubmed.ncbi.nlm.nih.gov/10084171/) | 1999 | Unclassified | Revue du Rhumatisme | Isoniazid used to manage refractory arthropathy after intravesical BCG therapy — a treatment-of-complication use, not a conjunctivitis indication. |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case Report | Medicine | Pediatric case of primary sinonasal tuberculosis presenting with phlyctenular keratoconjunctivitis. |

## South Africa Market Information

Isoniazid currently has no active SAHPRA product registrations on record (Market Status: **Not Marketed**; 0 licenses in this evidence pack).

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for conjunctivitis is high, but the underlying evidence shows an inverted signal — the literature documents isoniazid-induced ocular adverse effects and TB-related conjunctival disease, not therapeutic efficacy against conjunctivitis. The one supporting clinical trial does not evaluate conjunctivitis outcomes. Isoniazid is also not currently marketed in South Africa, so any repurposing pathway would require new SAHPRA registration regardless of indication.

**To proceed, the following is needed:**
- SAHPRA-equivalent Professional Information (PI) warnings/contraindications data (currently a blocking data gap, DG001)
- Confirmed mechanism of action and original indication documentation from DrugBank (DG002)
- A mechanistic rationale or controlled study specifically evaluating isoniazid for conjunctivitis before further consideration
- Note: among the 10 candidates screened in this evidence pack, **leprosy** (rank 5, evidence level L3, decision stage S1, "Research Question") is mechanistically far more plausible — isoniazid is antimycobacterial and *Mycobacterium leprae* is closely related to *M. tuberculosis*, with direct historical trials supporting use (e.g. PMID 12991685, 13281923) — and may warrant separate, dedicated evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

