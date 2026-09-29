---
layout: default
title: Lansoprazole
parent: Model Prediction Only (L5)
nav_order: 285
evidence_level: L5
indication_count: 10
---

# Lansoprazole
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

# Lansoprazole: From Acid-Related Gastric Disorders to Duodenogastric Reflux

## One-Sentence Summary

Lansoprazole is a proton pump inhibitor (PPI) used for acid-related conditions such as peptic ulcer and gastro-oesophageal reflux disease.
The TxGNN model predicts it may be effective for **duodenogastric reflux**, but there are **no registered clinical trials** and only **2 publications** (one rat study and one general PPI review). Evidence is very limited, and the rat study raises a safety concern.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acid-related disorders (peptic ulcer, GORD), per the published literature. No SAHPRA indication text was supplied. |
| Predicted New Indication | Duodenogastric reflux |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 (animal and mechanism-level evidence only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Lansoprazole reduces gastric acid by inhibiting the H+/K+ ATPase (proton pump) in gastric parietal cells. It is well established for peptic ulcer, *Helicobacter pylori* eradication regimens, gastro-oesophageal reflux disease, NSAID-induced gastrointestinal lesions and Zollinger-Ellison syndrome.

Duodenogastric reflux is the backflow of duodenal contents, including bile, into the stomach. It is a gastric condition, so the model links it to lansoprazole's gastric use. Mechanistically, however, the link is weak. Bile reflux injury is not primarily acid-driven, so acid suppression may bring little benefit. Any benefit would probably come from treating coexisting acid-related mucosal damage, not from correcting the reflux itself.

The available evidence also points to a possible harm. In a rat model of duodenogastric reflux, lansoprazole-induced acid suppression, with the resulting rise in gastrin, was associated with promotion of gastric carcinogenesis. This prediction is therefore not well supported by mechanism and carries a potential safety signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Animal study | Gastric Cancer | In rats with duodenogastric reflux, lansoprazole promoted gastric carcinogenesis. This is a safety concern, not evidence of benefit. |
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | Eur J Clin Pharmacol | General update on PPI use. PPIs are first choice for peptic ulcer, *H. pylori* infection, GORD, NSAID-related lesions and Zollinger-Ellison syndrome. It does not address duodenogastric reflux. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. A39/11.4.3/0116 | Burnloc | Capsule |
| Reg. No. 56/11.4.3/0763.762 | Laanero | Capsule |

Approved indication text and Essential Medicines List status were not available for these registrations.

---

## Safety Considerations

- **Literature signal**: In a rat model, lansoprazole combined with duodenogastric reflux was associated with gastric carcinogenesis (PMID 15052437). Human relevance is unknown, but this needs to be addressed before any use for this indication.

No drug-interaction records were found. Please refer to the SAHPRA-approved Professional Information (PI) for full warnings, contraindications and interactions. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct evidence is a rat study suggesting harm, there are no clinical trials, and the mechanism does not support benefit in a non-acid-driven condition. Lansoprazole has stronger candidate indications in the same prediction list, such as duodenitis (L3) and gastrojejunal ulcer, which are more plausibly acid-related.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for the S1 safety screen)
- Detailed mechanism of action data (MOA), for example from DrugBank
- Human clinical data for duodenogastric reflux specifically, including bile reflux endpoints
- A safety assessment of the gastrin and carcinogenesis signal from the rat study, particularly for long-term use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

