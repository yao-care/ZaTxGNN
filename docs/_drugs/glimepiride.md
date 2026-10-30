---
layout: default
title: Glimepiride
parent: Model Prediction Only (L5)
nav_order: 245
evidence_level: L5
indication_count: 9
monitor_inn: "GLIMEPIRIDE"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
last_modified_at: 2026-10-30
description: "Glimepiride: predicted new indication Focal stiff limb syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
---

# Glimepiride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Glimepiride: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome
{: .text-alpha }

## One-Sentence Summary

Glimepiride is a sulfonylurea medicine that, in the knowledge graph used by the TxGNN model, is recorded for type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
This is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (relation recorded in the knowledge graph; the local licence records contain no indication text) |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 2 of 3) |
| Number of SAHPRA Registrations | 3 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Glimepiride is a sulfonylurea. Sulfonylureas are generally known to close the ATP-sensitive potassium channels of pancreatic beta cells and so stimulate insulin release. Its recorded use in the knowledge graph is type 2 diabetes mellitus.

The link to focal stiff limb syndrome is unverified. Stiff limb syndrome is an autoimmune disorder usually associated with GAD65 antibodies and impaired GABAergic signalling. It often occurs together with diabetes. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Glimepiride has no known direct effect on GABAergic or neuromuscular pathways, so the score is most likely a disease-comorbidity artefact and not a therapeutic mechanism.

Other predictions in the same list (classic stiff person syndrome, opsismodysplasia, thiamine-responsive dysfunction syndrome, several localised lipodystrophies and pancreatic agenesis) also have no supporting trials or literature. Pancreatic agenesis is mechanistically implausible, because glimepiride needs residual beta cells to work.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for focal stiff limb syndrome. The only publication retrieved for the wider prediction list (PMID 12720536, a 2003 endosonography study of suspected insulinomas, linked to pancreatic agenesis) does not address glimepiride or the predicted disease and is not relevant evidence.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 41/21.2/0656 | Accord glimepiride | Tablet | Not available in the compiled records |
| Reg. No. A39/21.2/0023 | Glimepiride 1 oethmaan | Tablet | Not available in the compiled records |
| Reg. No. 43/21.2/0005 | Amaryl Combi 2/500 | Tablet | Not available in the compiled records |

All three registrations are valid. Essential Medicines List status is not available in the compiled data. The third product, Amaryl Combi, is named as a combination product; its licence is not used here to describe the single-ingredient drug.

## Safety Considerations

- **Disease relations recorded in the knowledge graph (not label text):** The knowledge graph records contraindication relations with kidney disease, liver disease, gallbladder disease, congestive heart failure, osteoporosis, infectious disease, and a large group of pituitary and hypogonadotropic disorders (including hypopituitarism and Kallmann syndrome). These need confirmation against the approved label.
- **Drug interactions:** The interaction database returned 100 entries. Most of the listed ones are of moderate severity, including:
  - Beta-agonists and sympathomimetics: salbutamol, formoterol, epinephrine, phenylephrine, pseudoephedrine
  - Beta-blocker: acebutolol
  - NSAIDs: ibuprofen, ketorolac
  - Corticosteroids: hydrocortisone
  - H2 blockers: famotidine, ranitidine
  - Others: acetazolamide, acitretin, ethinylestradiol, hydrochlorothiazide, albiglutide, nitazoxanide and ethanol
  - Topical hydrocortisone and topical alclometasone are listed as minor.
- **Hypoglycaemia:** As a sulfonylurea, glimepiride carries a hypoglycaemia risk. This is a particular concern in people with stiff person-spectrum disorders, who often have co-existing diabetes.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score (0.9975) is a computational prediction with no supporting trials or publications and no plausible mechanism. The evidence level is L5. Safety review also cannot proceed because the package insert warnings and contraindications are not yet available.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indications) for all three registrations
- Mechanism of action data for glimepiride
- A systematic literature search for glimepiride or sulfonylureas in stiff limb and stiff person syndromes
- Mechanistic evidence for any effect on GABAergic or neuromuscular pathways
- A hypoglycaemia risk assessment for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

