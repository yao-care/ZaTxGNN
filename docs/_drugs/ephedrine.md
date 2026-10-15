---
layout: default
title: Ephedrine
parent: Model Prediction Only (L5)
nav_order: 214
evidence_level: L5
indication_count: 3
---

# Ephedrine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Ephedrine: From Allergic Rhinitis and Related Upper Airway Conditions to Nasal Cavity Disease

## One-Sentence Summary

Ephedrine is a sympathomimetic agent originally used for allergic and vasomotor rhinitis, the common cold, pharyngitis, bronchitis and conjunctivitis, among other conditions.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but the evidence is thin: **0 registered clinical trials** and only **2 publications** (a 1964 combination-product study and a 2000 uncontrolled observation of a compound spray). Because the new indication largely overlaps with its existing uses, this is a broader restatement rather than a true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, rhinitis, nasopharyngitis, common cold, pharyngitis, bronchitis, headache disorder, conjunctivitis (atopic, papillary, vernal). The indication text on the local registrations is empty, so this list comes from the knowledge graph. |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 (no trials; only two low-tier publications on combination products) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 12 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. From general pharmacology, ephedrine is an indirect-acting sympathomimetic that promotes norepinephrine release and also has some direct adrenergic activity. Alpha-1 mediated vasoconstriction of nasal mucosal vessels reduces swelling and congestion.

This is consistent with its established use in allergic rhinitis, vasomotor rhinitis, rhinitis and nasopharyngitis. "Nasal cavity disease" is a broad category that already contains these conditions. The high TxGNN score therefore mostly reflects existing uses, and the mechanistic link is inferred rather than demonstrated.

Two other predictions were generated, both at evidence level L5 (model prediction only) and both on Hold:
- **Acute laryngopharyngitis** (score 99.90%): no trials or literature. The link is indirect decongestion, and vasoconstriction does not address the infectious or inflammatory cause. Pharyngitis is already an original indication.
- **Trigeminal autonomic cephalalgia** (score 99.34%): no trials or literature. The link to headache is speculative, and sympathomimetics carry cardiovascular risks and may worsen headache.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14211229](https://pubmed.ncbi.nlm.nih.gov/14211229/) | 1964 | Clinical testing (combination product) | Svenska lakartidningen | Experimental testing of an antihistamine (N-hydroxyethylpromethazine chloride) combined with ephedrine hydrochloride in the nasal cavity. No abstract is available, so results cannot be summarised. |
| [11789239](https://pubmed.ncbi.nlm.nih.gov/11789239/) | 2000 | Preliminary clinical observation (uncontrolled) | Zhongguo Zhong Xi Yi Jie He Za Zhi | Preliminary observation of a compound rhinitis spray for chronic rhinitis. The abstract states only the aim, and ephedrine's individual contribution cannot be isolated. |

Both publications involve combination products, are uncontrolled or old, and have not been assessed for relevance.

## South Africa Market Information

All 12 registrations are valid single-ingredient registrations. The approved indication text is not available for any of them. The data compiled for this report does not state Essential Medicines List (EML) status.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| C795 (OM) | Grippon Cold And Flu Syrup | Syrup | Not available |
| G1236 | Codef Cough | Syrup | Not available |
| 29/5.8/0782 | Sinuend | Tablet | Not available |
| G979 | Sinucon | Tablet | Not available |
| C 810 (OM) | Colcleer (cold + flu) | Tablet | Not available |

The remaining 7 registrations are Brunacod, Docsed, Flusin (capsule), Dequa-coff, Corbar linctus, Coughcod senior and Coughcod junior. The product names suggest that most are cough, cold and flu preparations.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (drug-disease edges, not label text): hypertension, congestive heart failure, hypothyroidism, open-angle glaucoma, epilepsy, anxiety and other mental disorders (including psychotic disorders), COPD, liver and kidney disease, gastric and peptic ulcer, pancreatitis, gallbladder disease, inflammatory bowel disease, thrombocytopenia and porphyria. These need confirmation against the SAHPRA-approved Professional Information (PI).
- **Drug interactions:** 100 interactions were recorded; 20 are shown in the data compiled for this report. Major-level interactions among those shown include:
  - Tramadol
  - Amitriptyline
  - Bupropion
  - Methylene blue

  Moderate-level interactions include:
  - Beta-blockers (atenolol, acebutolol)
  - Other adrenergic agents (salbutamol, formoterol, arformoterol, methylphenidate, amphetamine, atomoxetine)
  - Antidiabetic agents (metformin, acarbose, alogliptin, albiglutide)

  Morphine and ascorbic acid are minor.

The label warnings and contraindications from the SAHPRA package insert have not been retrieved. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for nasal cavity disease largely restates ephedrine's existing uses. There are no registered trials, and the two publications are old or uncontrolled combination-product studies. Package insert safety data has not been obtained, which blocks progression to safety screening.

**To proceed, the following is needed:**
- Download and review the SAHPRA package inserts to obtain warnings, contraindications and approved indications for the 12 registrations.
- Obtain mechanism-of-action data from DrugBank.
- Define which specific nasal cavity conditions go beyond the current labelled uses. If none do, the prediction adds little novelty.
- Search for controlled studies of ephedrine as a single agent in nasal conditions.
- Assess cardiovascular and interaction risks, given the number of KG-flagged contraindications and recorded interactions.
- Consider the two other predictions (acute laryngopharyngitis, trigeminal autonomic cephalalgia) only if supporting evidence emerges. Both currently have no clinical support.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

