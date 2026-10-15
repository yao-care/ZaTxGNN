---
layout: default
title: Benzocaine
parent: Model Prediction Only (L5)
nav_order: 62
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

# Benzocaine: From Tinea Pedis and Dermatitis to Dyspepsia

## One-Sentence Summary

Benzocaine is a topical ester local anaesthetic, originally associated with symptom relief in conditions such as tinea pedis, dermatitis, pharyngitis, tinea corporis and tinea infections.
The TxGNN model's top-ranked prediction is **papillary conjunctivitis**, but that prediction has no supporting studies. The best-supported candidate is **dyspepsia**, with **2 publications** (one small randomised comparison and one mechanistic physiology study) and **no registered clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, dermatitis, pharyngitis, tinea corporis, tinea infection (from the knowledge graph; the SAHPRA registrations list no approved indication text) |
| Predicted New Indication | Papillary conjunctivitis (top-ranked prediction); dyspepsia is the best-supported candidate |
| TxGNN Prediction Score | 99.38% (papillary conjunctivitis); 98.29% (dyspepsia) |
| Evidence Level | L5 for papillary conjunctivitis; L3 for dyspepsia |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold (papillary conjunctivitis); dyspepsia is a research question only |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, benzocaine is a topical ester local anaesthetic that blocks voltage-gated sodium channels, which dampens nerve signalling at the site of application. Its original uses are symptom-oriented (pain and itch relief), not curative.

**Papillary conjunctivitis (top-ranked).** This condition is usually allergic or contact-lens related. A transient numbing effect on the ocular surface is conceivable, but the high TxGNN score of 99.38% has no clinical or literature support. Topical benzocaine is not an accepted ocular treatment, and it carries risks of corneal toxicity and contact sensitisation. The same reasoning applies to the other eye and eyelid predictions (blepharoconjunctivitis, rosacea conjunctivitis, ulcerative blepharitis, parasitic eyelid infestation and noninfectious eyelid dermatoses). Benzocaine has no antimicrobial, antiparasitic or anti-inflammatory action relevant to these conditions, and it is a recognised contact allergen, which is a particular concern on the eyelid.

**Dyspepsia (best-supported).** Topical anaesthetics may reduce sensory signalling from the gut mucosa, which could attenuate visceral discomfort. A mechanistic study suggests duodenal mucosal nerve endings contribute to acid-related sensitivity, which supports biological plausibility. Evidence is rated L3 rather than L2 because the clinical study is small, has no placebo control, and no trials are registered.

**Other candidates.** Acute laryngopharyngitis is an extension of benzocaine's existing use for sore throat (pharyngitis), so it is the most clinically credible of the non-dyspepsia candidates, though evidence is indirect (L4). Cutaneous candidiasis and nasal cavity disease have no specific supporting evidence. Benzocaine has no antifungal activity, and any benefit in candidiasis would be limited to symptom relief.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the top 10 predicted indications.

---

## Literature Evidence

Literature was found only for dyspepsia.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15219296](https://pubmed.ncbi.nlm.nih.gov/15219296/) | 2004 | RCT | J Emerg Med | Prospective, randomised, single-blinded comparison of benzocaine versus viscous lidocaine as the topical anaesthetic in a GI cocktail for dyspepsia in emergency patients. It compared two anaesthetics, not benzocaine versus placebo, so it does not establish benzocaine's own efficacy. |
| [23565580](https://pubmed.ncbi.nlm.nih.gov/23565580/) | 2013 | Mechanistic physiology study | Neurogastroenterol Motil | Examined the role of duodenal mucosal nerve endings in the acid-induced duodenogastric reflex using benzocaine in healthy volunteers. Supports the plausibility of mucosal anaesthesia in functional dyspepsia. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 43/8/0830 | Soluspirin cv | Effervescent tablet | Not available |
| B0917 (ACT 101) | Vidol teething powders | Powder | Not available |

Essential Medicines List (EML) inclusion status was not available in the data compiled for this report.

---

## Cytotoxicity

Benzocaine is not an antineoplastic drug, so this section does not apply.

---

## Safety Considerations

- **Methemoglobinaemia:** Benzocaine carries a recognised risk of methemoglobinaemia with mucosal application. Systemic absorption must be considered for any oral or gastrointestinal use.
- **Contact sensitisation:** Benzocaine is a recognised contact allergen. This is a particular concern on the eyelid and periocular skin.
- **Ocular risks:** Topical use on the ocular surface raises concerns of epithelial or corneal toxicity.
- **Knowledge-graph contraindication signals:** The knowledge graph links benzocaine to a broad set of conditions, including liver disease and failure, kidney disease, porphyria, epilepsy, blood disorders (thrombocytopenia, neutropenia, agranulocytosis, blood coagulation disease), diabetes and diabetic ketoacidosis, and substance abuse or dependence. These come from graph edges rather than label text. They may reflect other ingredients in combination products (for example, Soluspirin cv appears to contain additional active ingredients). They should be verified against the approved Professional Information (PI) and not read as confirmed benzocaine contraindications.
- **Drug interactions:** No interaction data were found.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold** (papillary conjunctivitis and the other ocular or eyelid predictions). Dyspepsia and acute laryngopharyngitis are research questions only.

**Rationale:**
- The top-ranked predictions (papillary conjunctivitis and other eye or eyelid conditions) are supported only by model scores. They have no trials or publications and raise safety concerns. Dyspepsia has limited, indirect support (L3). Acute laryngopharyngitis is an extension of existing sore throat use (L4) rather than true repurposing.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications, which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- A placebo-controlled study of benzocaine in dyspepsia, with methemoglobinaemia monitoring
- Confirmation of approved indications for the two SAHPRA-registered products
- Route and formulation compatibility assessment for any new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

