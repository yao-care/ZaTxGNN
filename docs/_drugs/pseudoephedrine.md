---
layout: default
title: Pseudoephedrine
parent: Model Prediction Only (L5)
nav_order: 395
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-31
monitor_inn: "PSEUDOEPHEDRINE"
predicted_indications: ["nasal cavity disease", "allergic urticaria"]
description: "Pseudoephedrine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Pseudoephedrine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Pseudoephedrine: Nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Pseudoephedrine is a nasal decongestant originally used for allergic rhinitis, vasomotor rhinitis, pharyngitis and the common cold.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but this is largely a broader category of its existing uses.
Currently there are **0 registered clinical trials** and **7 publications** (one review, one human comparative study and five animal-model studies) linked to this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences on record: at least 16) |
| Number of SAHPRA Registrations | at least 19 |
| Recommended Decision | Hold (research question) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the compiled analysis, pseudoephedrine is an indirect sympathomimetic with alpha-adrenergic activity. It constricts blood vessels in the nasal lining and so reduces congestion.

This closely matches its existing uses in rhinitis, nasopharyngitis and the common cold. "Nasal cavity disease" is therefore mostly a wider label for what the drug already treats, not a true repurposing to a new disease area.

Two other predictions were also generated, and both are weak:
- **Allergic urticaria** (score 0.9914): the retrieved literature concerns H1-antihistamines (ebastine, desloratadine, fexofenadine, loratadine), not pseudoephedrine. Pseudoephedrine does not block H1 receptors or stabilise mast cells. The high score probably reflects co-formulation with antihistamines rather than a true therapeutic link. Evidence level L5, Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Literature for the top prediction (nasal cavity disease):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11345158](https://pubmed.ncbi.nlm.nih.gov/11345158/) | 2001 | Clinical comparative study | Am J Rhinol | Compared the oral and topical decongestant effects of phenylpropanolamine and d-pseudoephedrine on nasal cavity dimensions using acoustic rhinometry |
| [22794679](https://pubmed.ncbi.nlm.nih.gov/22794679/) | 2012 | Review | Allergy Asthma Proc | Overview of nonallergic rhinitis (inflammatory and noninflammatory causes) |
| [19769798](https://pubmed.ncbi.nlm.nih.gov/19769798/) | 2009 | Animal model (cat) | Am J Rhinol Allergy | Loratadine plus montelukast produced decongestion; d-pseudoephedrine was also studied with and without desloratadine |
| [12962193](https://pubmed.ncbi.nlm.nih.gov/12962193/) | 2003 | Animal model (dog) | Am J Rhinol | Model of allergic nasal congestion in ragweed-sensitised dogs |
| [12387934](https://pubmed.ncbi.nlm.nih.gov/12387934/) | 2002 | Animal model (dog) | J Pharmacol Toxicol Methods | Pharmacological characterisation of a chronic dog model of nasal congestion |
| [11895194](https://pubmed.ncbi.nlm.nih.gov/11895194/) | 2002 | Animal model (dog) | Am J Rhinol | Acoustic rhinometry dog model of nasal congestion |
| [24492651](https://pubmed.ncbi.nlm.nih.gov/24492651/) | 2014 | Animal model | J Pharmacol Exp Ther | Selective α2c-adrenergic agonists in animal models of nasal congestion |

No human randomised controlled trial data are included. For the allergic urticaria prediction, the retrieved papers do not study pseudoephedrine itself and are not listed as supporting evidence.

## South Africa Market Information

All 19 registrations are valid single-ingredient entries, but no approved indication text is available in the data compiled for this report. The first 5 are shown. EML inclusion status is not available.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 36/5.8/0207 | Sinutab 3-way | Tablet | Not available |
| 37/5.8/0138 | Sinutab sinus pain non-drowsy | Tablet | Not available |
| T/5.8/196 | Sudafed sinus pain 500 mg | Tablet | Not available |
| 36/5.8/0206 | Benylin daytime flu | Tablet | Not available |
| 40/5.8/0218 | Ibumax cold & flu | Tablet | Not available |

Other registered forms include syrups, capsules, sachets, a cream and a transdermal patch.

## Safety Considerations

**Contraindication-related conditions from the knowledge graph** (not label text), including:
- Cardiovascular and cerebrovascular: hypertension, coronary artery disease, congestive heart failure, stroke
- Endocrine and metabolic: diabetes mellitus, diabetic ketoacidosis, hypothyroidism
- Hepatic and renal: liver failure, kidney disease
- Other: epilepsy, COPD, peptic ulcer disease, benign prostatic hyperplasia

**Drug Interactions:** A total of 100 interactions were found. The 20 displayed are mostly Moderate and involve:
- Antidiabetic agents (acarbose, glimepiride, glipizide, glyburide, chlorpropamide, insulins)
- GLP-1 agonists (exenatide, dulaglutide)
- SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin)
- Diethylpropion

Ascorbic acid is the only Minor interaction listed.

Please refer to the SAHPRA-approved Professional Information (PI) for official warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is largely a broader label for existing approved uses, so it is not a true repurposing opportunity. Evidence is limited to L4 (one small human comparative study plus animal models), with no registered trials. The other two predictions (L5) lack supporting evidence.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Approved indication text for the 19 SAHPRA registrations
- Human controlled trial data for any indication genuinely beyond current approved uses
- A cardiovascular and metabolic safety review given the knowledge-graph contraindications and the antidiabetic drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

