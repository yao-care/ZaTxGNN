---
layout: default
title: Lidocaine
parent: Model Prediction Only (L5)
nav_order: 296
evidence_level: L5
indication_count: 10
monitor_inn: "Lidocaine"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "papillary conjunctivitis", "rosacea conjunctivitis", "exposure keratitis", "atopic conjunctivitis", "conjunctival disorder", "nephrotic syndrome", "non-human animal disease", "tinea corporis", "sporadic idiopathic steroid-resistant nephrotic syndrome"]
last_modified_at: 2026-10-29
description: "Lidocaine: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Lidocaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Lidocaine: Punctate epithelial keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Lidocaine is a local anaesthetic.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **no clinical trials and no publications** support this specific prediction in the data compiled for this report.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 2 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, lidocaine is a sodium channel blocker that gives local anaesthesia, and it could plausibly relieve pain or discomfort on the ocular surface.

Lidocaine's uses (neuralgia, dermatitis, haemorrhoids and others) are mostly about symptom relief, such as pain and itch. Any link to punctate epithelial keratoconjunctivitis would be symptomatic only. Nothing in the data suggests lidocaine changes the underlying disease. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is a computational prediction and has not been confirmed by any study.

## Clinical Trial Evidence

Currently no related clinical trials registered for punctate epithelial keratoconjunctivitis.

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

For context, the other TxGNN predictions were also reviewed. None provides direct efficacy evidence:

- **Conjunctival disorder** (score 0.9984): a completed Phase 4 trial ([NCT05978687](https://clinicaltrials.gov/study/NCT05978687), n=41) compared lidocaine gel with subconjunctival injection during pterygium excision. This tests anaesthesia delivery, not disease treatment. Several small pterygium-surgery studies (for example [PMID 18989343](https://pubmed.ncbi.nlm.nih.gov/18989343/), a randomised trial of lidocaine gel vs tetracaine drops) point the same way. Much of the remaining literature concerns SUNCT/SUNA headache, a different condition.
- **Atopic conjunctivitis** (0.9986): only indirect mechanistic and physiological studies ([PMID 37819721](https://pubmed.ncbi.nlm.nih.gov/37819721/)).
- **Nephrotic syndrome**, **tinea corporis**, **exposure keratitis**: only pharmacokinetic, safety or non-specific papers.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| F/21.5.4/228 | Depo-Medrol With Lidocaine | Injection | Not stated in the data compiled |
| W/2.7/142 | Nurofen period pain (was Nurofen extra s...) | Tablet | Not stated in the data compiled |

Both records are classed as single-ingredient and valid. Essential Medicines List status could not be confirmed from the data compiled. No ophthalmic lidocaine product appears among the registrations listed, so route compatibility for an eye indication is unconfirmed.

## Safety Considerations

- **Contraindications recorded in the knowledge graph (not label text):** hypertension, liver failure, liver disease, cirrhosis, epilepsy, kidney disease, adrenocortical insufficiency, hypothyroidism, open-angle glaucoma, osteoporosis, psychotic disorders, herpes simplex keratitis, varicella zoster infection, fungal infections, gastritis and others. These entries probably reflect combination products (such as the corticosteroid in Depo-Medrol With Lidocaine) and should not be read as lidocaine-specific contraindications.
- **Drug interactions:** 100 interactions were recorded. Notable examples:
  - Major: bupropion.
  - Moderate: aprepitant, cimetidine, liposomal morphine, obeticholic acid, polyethylene glycol with electrolytes, picosulfuric acid, sodium sulfate.
  - Minor: dexamethasone, omeprazole, and the aminoglycosides kanamycin, neomycin and streptomycin.
- **Literature safety signals:**
  - Neuropsychiatric and cardiac side-effects ([PMID 19250287](https://pubmed.ncbi.nlm.nih.gov/19250287/)).
  - Methemoglobinaemia in a child with nephrotic syndrome using topical lidocaine, benzocaine and co-trimoxazole ([PMID 41995267](https://pubmed.ncbi.nlm.nih.gov/41995267/)).
  - Seizures in macaques given a ceftriaxone–lidocaine preparation ([PMID 19858165](https://pubmed.ncbi.nlm.nih.gov/19858165/)).
  - Topical anaesthetics can impair corneal healing and protective reflexes, which matters for any corneal use.

Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. No trial or publication studies lidocaine in punctate epithelial keratoconjunctivitis, so the evidence level is L5. Any plausible benefit is symptomatic, and prolonged topical anaesthesia of the cornea carries safety concerns.

**To proceed, the following is needed:**
- Mechanism of action data and a clear disease-modifying rationale
- SAHPRA Professional Information warnings and contraindications (a blocking data gap)
- Evidence from clinical studies directly in punctate epithelial keratoconjunctivitis
- Confirmation of an ophthalmic route and formulation, and a corneal safety assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

