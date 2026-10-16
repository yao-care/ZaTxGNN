---
layout: default
title: Cinchocaine
parent: Model Prediction Only (L5)
nav_order: 122
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Cinchocaine: predicted new indication Bronchitis (evidence level L5). Approved use: Dermatitis"
monitor_inn: "CINCHOCAINE"
predicted_indications: ["bronchitis", "acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "acne keloid", "hydroa vacciniforme, familial", "amyopathic dermatomyositis"]
---

# Cinchocaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Cinchocaine: From Dermatitis to Bronchitis

## One-Sentence Summary

Cinchocaine (dibucaine) is a local anaesthetic, originally used for dermatitis and topical symptom relief.
The TxGNN model predicts it may be effective for **Bronchitis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction is based on the computational model only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis (from the knowledge graph; the SAHPRA registrations contain no indication text) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Cinchocaine is an amide-type local anaesthetic, a class that blocks voltage-gated sodium channels. Its efficacy in its current dermatological and anorectal uses relates to symptomatic relief of pain and itch.

A theoretical link to bronchitis would be suppression of airway sensory nerve activity (the cough reflex). Other local anaesthetics, such as lidocaine, have been studied for cough. This is speculative, however. Systemic or inhaled use of cinchocaine is not an established route, and its toxicity profile argues for caution. The high TxGNN score is a computational prediction only and is not backed by any trial or publication.

**Other predicted indications (all L5, Hold):**

| Predicted Indication | TxGNN Score | Assessment |
|------|------|------|
| Acrodermatitis chronica atrophicans | 99.76% | Late Lyme disease skin manifestation. No anti-infective mechanism; likely driven by proximity to skin-disease nodes. |
| Neonatal dermatomyositis | 99.72% | Autoimmune process not addressed by sodium channel blockade. Neonatal use raises systemic toxicity concerns. |
| Secondary childhood interstitial lung disease (connective tissue disease) | 99.72% | No credible mechanistic link; likely an association artefact. |
| Acne keloid | 99.67% | Possible symptomatic relief of pain or itch with topical use only. No evidence of effect on inflammation or fibrosis. |
| Hydroa vacciniforme, familial | 99.66% | Management centres on photoprotection. No disease-modifying mechanism. |
| Amyopathic dermatomyositis | 99.65% | Autoimmune (type I interferon) pathogenesis not addressed. Symptomatic use is unsupported. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| E/11.8/0667 | Scheriproct (new formulary) | Ointment | Not available in the data compiled |
| E529 (ACT 101 1965) | Proctosedyl Suppositories | Suppository | Not available in the data compiled |

Both registrations are valid single-ingredient registrations. The data compiled for this report contains no Essential Medicines List (EML) information for this drug.

---

## Safety Considerations

**Contraindication signals from the knowledge graph (not label text):** the knowledge graph links cinchocaine to the following conditions as contraindications: epilepsy, kidney disease, liver disease, gallbladder disease, pyoureter, sudden cardiac arrest, heart conduction disease, cardiovascular disease, heart disease, respiratory failure, myasthenia gravis (including adult-onset), neuromuscular junction disease and butyrylcholinesterase deficiency.

These signals are particularly relevant to any systemic or airway use, such as for bronchitis, given the cardiac, neuromuscular and respiratory entries.

No drug-interaction records were found in the data compiled.

SAHPRA package insert warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is model prediction only (L5), with no clinical trials or publications for bronchitis or any other predicted indication. The mechanistic link is speculative, and the knowledge-graph contraindication signals (cardiac, respiratory, neuromuscular) argue against any systemic or inhaled use.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Preclinical or clinical evidence of antitussive or airway effects of cinchocaine
- Route compatibility assessment, since current products are topical or rectal only
- A safety assessment for any non-topical route
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

