---
layout: default
title: Benzocaine
parent: Model Prediction Only (L5)
nav_order: 61
evidence_level: L5
indication_count: 10
---

# Benzocaine
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

# Benzocaine: From Topical Local Anaesthetic to Papillary Conjunctivitis

## One-Sentence Summary

Benzocaine is a sodium channel-blocking topical anaesthetic. The SAHPRA data supplied for this report do not record an approved indication.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but there are **0 clinical trials** and **0 publications** for this prediction, so it rests on the model score alone.
Among the other predictions, only **dyspepsia** has any benzocaine-specific human evidence, a single randomised comparison with lidocaine (PMID 15219296).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the supplied SAHPRA data (approved indication text is empty for both registrations) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.38% (model rank 3,341) |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, benzocaine is a sodium channel-blocking topical anaesthetic. It could at most give symptomatic relief of ocular surface pain or itch. It has no known disease-modifying effect on conjunctival inflammation.

The prediction is therefore weak on biological grounds. Papillary conjunctivitis is an inflammatory or allergic surface condition, and blocking sodium channels does not address its cause. Repeated ocular anaesthetic exposure also risks corneal toxicity, and benzocaine is not a standard ophthalmic agent. The high score most likely reflects knowledge-graph proximity to other ocular surface agents rather than a biological rationale.

The other ocular and periocular predictions (blepharoconjunctivitis, rosacea conjunctivitis, ulcerative blepharitis, parasitic eyelid infestation, noninfectious eyelid dermatoses) follow the same pattern. Each is prediction-only at L5 and Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered for papillary conjunctivitis. No SANCTR or PACTR entries were supplied.

## Literature Evidence

Currently no related literature available for papillary conjunctivitis.

**For context, the strongest benzocaine-specific evidence in the package belongs to another prediction, dyspepsia (score 98.29%, L3, "Research Question"):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15219296](https://pubmed.ncbi.nlm.nih.gov/15219296/) | 2004 | RCT (single-blinded) | J Emerg Med | Compared viscous lidocaine with benzocaine in a "GI cocktail" for dyspepsia in emergency patients. It is an active-comparator study without placebo, and the cocktail's other components confound attribution. |
| [23565580](https://pubmed.ncbi.nlm.nih.gov/23565580/) | 2013 | Mechanistic study | Neurogastroenterol Motil | Role of duodenal mucosal nerve endings in the acid-induced duodenogastric reflex, in healthy humans. The title suggests a benzocaine effect, but the study drug is unconfirmed from the supplied data. |

None of the 10 dyspepsia trials listed (of 28 reported) tests benzocaine. The closest is [NCT00521703](https://clinicaltrials.gov/study/NCT00521703), a Phase 3 topical lidocaine spray study for paediatric upper GI endoscopy, which is procedural anaesthesia with a different drug.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 43/8/0830 | Soluspirin cv | Effervescent tablet (oral) | Not stated in supplied data |
| Reg. No. B0917 (ACT 101) | Vidol teething powders | Powder | Not stated in supplied data |

Neither registered product is an ophthalmic formulation, so no existing SAHPRA-registered route matches conjunctival use.

## Safety Considerations

- **Concerns noted in the evidence review:**
  - Repeated ocular anaesthetic exposure risks corneal toxicity.
  - Topical benzocaine can cause contact allergic dermatitis, a liability on thin periocular skin.
  - Systemic exposure and methemoglobinemia risk with oral or mucosal use need a safety review before any further step.
- **Drug Interactions:** No interaction records were found in the queried source.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials or literature behind it (L5). Any plausible benefit is symptomatic only, and the ocular surface safety concerns are significant. The dyspepsia prediction is the only one with human evidence (L3), and it is better framed as a research question than a repurposing candidate.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications for both registered products
- Mechanism of action data (e.g. from DrugBank)
- Confirmation of the original approved indications, since the supplied SAHPRA indication text is empty
- Confirmation of the study drug in PMID 23565580, and a placebo-controlled study of benzocaine alone if dyspepsia is pursued
- A clear ophthalmic route and formulation rationale, plus an ocular safety review, before any conjunctival use is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

