---
layout: default
title: Oxymetazoline
parent: Model Prediction Only (L5)
nav_order: 357
evidence_level: L5
indication_count: 3
---

# Oxymetazoline
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

# Oxymetazoline: From Topical Nasal Decongestant Use to Nasal Cavity Disease

## One-Sentence Summary

Oxymetazoline is a topical nasal decongestant that narrows the blood vessels in the nasal lining. The TxGNN model predicts it may be effective for **nasal cavity disease**, with a very high score of 99.96%. The Evidence Pack lists **16 clinical trials** and **5 publications** for this prediction, but only a few involve oxymetazoline directly. This signal probably reflects an existing approved use rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration record (the marketed product is a nasal spray) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L2 (as scored in the Evidence Pack; see the caveat under Clinical Trial Evidence) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, oxymetazoline is a direct alpha-adrenergic agonist. It constricts the blood vessels of the nasal mucosa, which reduces swelling and improves airflow through the nose.

This makes the link to nasal cavity disease biologically direct, because nasal congestion is the main problem in many nasal conditions. Oxymetazoline is already sold as a nasal spray, so the prediction most likely re-identifies its existing use. Before treating it as a new candidate, check the SAHPRA-approved label to see whether this indication is already covered.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03228914](https://clinicaltrials.gov/study/NCT03228914) | Phase 4 | Completed | 20 | Compares 0.05% oxymetazoline with 1:1000 epinephrine before sinus surgery, looking at blood loss and surgical view. This is the most directly relevant trial. |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | Randomised, double-blind, placebo-controlled crossover study of an H3 antagonist on congestion after nasal allergen challenge. Oxymetazoline is not the agent tested. |
| [NCT03620513](https://clinicaltrials.gov/study/NCT03620513) | Phase 4 | Completed | 160 | Double-blind randomised study of topical anaesthesia and/or decongestant before fibreoptic nasal laryngoscopy, looking at pain and discomfort. |
| [NCT03380715](https://clinicaltrials.gov/study/NCT03380715) | NA | Completed | 106 | Co-phenylcaine (lidocaine plus phenylephrine) spray versus nebulisation before nasoendoscopy. This is a decongestant plus anaesthetic procedure study. |
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | Completed | 16 | Cocaine, lidocaine/xylometazoline and saline for intranasal analgesia. Xylometazoline is a related imidazoline, so this supports a class effect only. |
| [NCT01411969](https://clinicaltrials.gov/study/NCT01411969) | NA | Completed | 16 | Acoustic rhinometry with an external nasal dilator, after decongestion with 0.05% oxymetazoline spray. Oxymetazoline is used as a tool, not tested for efficacy. |
| [NCT00147940](https://clinicaltrials.gov/study/NCT00147940) | Phase 4 | Terminated | 20 | Correlates nasal volume and cross-sectional area with nasalance scores. The role of oxymetazoline is unclear. |
| [NCT03506178](https://clinicaltrials.gov/study/NCT03506178) | NA | Unknown | 30 | Effect of nasal airflow on upper airway dilator muscles during sleep. This is a physiology study. |
| [NCT03890692](https://clinicaltrials.gov/study/NCT03890692) | NA | Unknown | 100 | Adenoid size assessed by nasoendoscopy and radiography. This is diagnostic only. |
| [NCT07021040](https://clinicaltrials.gov/study/NCT07021040) | NA | Recruiting | 125 | Collection of nasal olfactory tissue biopsies. This is a tissue-collection study. |

**Caveat on the evidence level:** the L2 rating comes from a completed Phase 2 randomised trial (NCT00562120) that did not test oxymetazoline. The only completed trial with oxymetazoline as a study drug (NCT03228914) is small (n=20) and tests it as a surgical aid, not as a treatment for nasal disease. Treat the L2 rating with caution.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8615587](https://pubmed.ncbi.nlm.nih.gov/8615587/) | 1996 | Preclinical (animal) | Ann Otol Rhinol Laryngol | Oxymetazoline nose drops versus placebo in rabbits with experimental bacterial sinusitis (14 animals). It examined effects on early local tissue defence. |
| [9929658](https://pubmed.ncbi.nlm.nih.gov/9929658/) | 1998 | Clinical physiology study | Ann N Y Acad Sci | Olfactory function during the common cold in 36 subjects, with nasal volume measured by acoustic rhinometry. |
| [25496205](https://pubmed.ncbi.nlm.nih.gov/25496205/) | 2015 | Observational study | J Plast Surg Hand Surg | Nasal patency by acoustic rhinometry in children after cleft lip and palate repair, compared with controls. |
| [28490409](https://pubmed.ncbi.nlm.nih.gov/28490409/) | 2017 | Case series / procedural report | Am J Rhinol Allergy | Endoscopic coblation of nasal telangiectasias in hereditary haemorrhagic telangiectasia. |
| [38024464](https://pubmed.ncbi.nlm.nih.gov/38024464/) | 2023 | Case report | Glob Pediatr Health | Rhinoscleroma in a 9-year-old boy presenting with nasal obstruction. |

None of these publications shows clinical efficacy of oxymetazoline in a nasal disease.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H1501 (OM) | Nazene Z 20ml | Spray | Not listed in the registration record |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The mechanism is direct and the drug is already marketed in South Africa as a nasal spray. The prediction most likely matches its existing use rather than a new one. The supporting trials are small and mostly use oxymetazoline as a procedural tool.

**To proceed, the following is needed:**
- Download the SAHPRA package insert for Nazene Z to confirm the approved indication, warnings and contraindications. This is a blocking data gap.
- Obtain DrugBank mechanism of action and original indication data.
- Confirm whether "nasal cavity disease" is already covered by the current label. If it is, treat this as an existing use, not a repurposing candidate.

**Other predictions in the Evidence Pack:**
- *Acute laryngopharyngitis* has no supporting trials or literature. It is an unsupported prediction and should be placed on Hold.
- *Headache disorder* is a research question only. The single direct signal is a study of intranasal tetracaine plus oxymetazoline in status migrainosus ([PMID 31919839](https://pubmed.ncbi.nlm.nih.gov/31919839/)). It used a combination product, so the effect cannot be attributed to oxymetazoline alone.

*This report is for research reference only and does not constitute medical advice. Any repurposing candidate requires clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

