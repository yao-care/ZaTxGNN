---
layout: default
title: Procaine
parent: Moderate Evidence (L3-L4)
nav_order: 390
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-29
description: "Procaine: predicted new indication Methemoglobinemia (evidence level L4). Approved use: Not available"
monitor_inn: "Procaine"
predicted_indications: ["methemoglobinemia", "methemoglobinemia, alpha type", "Tourette syndrome", "anaphylaxis", "methemoglobin reductase deficiency", "hyperthyroidism", "fibromyalgia", "tendinitis", "idiopathic granulomatous myositis", "myositis fibrosa"]
---

# Procaine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

## Procaine: From Unspecified Original Indication to Methemoglobinemia (Prediction Not Supported)
{: .text-alpha }

## One-Sentence Summary

Procaine is an ester-type local anaesthetic. The data compiled for this report do not record an approved indication for it in South Africa.
The TxGNN model's top prediction is **methemoglobinemia**, but the available literature describes procaine as a **cause** of this condition rather than a treatment.
No clinical trials are registered for this prediction, and only **5 publications** were found, all of which are case reports, a review, a pharmacokinetic study or a small clinical study.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the single SAHPRA registration lists no approved indication text) |
| Predicted New Indication | Methemoglobinemia |
| TxGNN Prediction Score | 0.9950 |
| Evidence Level | L4 |
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Procaine is known as a local anaesthetic that blocks sodium channels. Pharmacology data compiled for this report also list the ryanodine receptors RyR1 and RyR2 as proposed molecular targets. However, no public bioactivity data were found to confirm these targets.

For methemoglobinemia, the published literature points in the opposite direction from the prediction. Reports describe procaine and related local anaesthetics such as lignocaine as **causing** methemoglobin formation (for example, "Methemoglobinemia due to intravenous procaine", 1970). The high TxGNN score (0.9950) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. On current evidence, using procaine for this indication would be a safety concern.

Other predictions in the list include methemoglobinemia (alpha type), methemoglobin reductase deficiency, anaphylaxis, Tourette syndrome, hyperthyroidism, fibromyalgia, tendinitis, idiopathic granulomatous myositis and myositis fibrosa. Of these, the musculoskeletal pain indications are the most plausible. They are noted under Conclusion and Next Steps.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5529388](https://pubmed.ncbi.nlm.nih.gov/5529388/) | 1970 | Case report | Acta Physiol Latino Am | Methemoglobinemia following intravenous procaine |
| [3691245](https://pubmed.ncbi.nlm.nih.gov/3691245/) | 1987 | Clinical study | Zhonghua Wai Ke Za Zhi | Effect of intravenous procaine anaesthesia on methemoglobin levels |
| [6705717](https://pubmed.ncbi.nlm.nih.gov/6705717/) | 1984 | Review | Drugs | Rational use of local anaesthetics |
| [14246695](https://pubmed.ncbi.nlm.nih.gov/14246695/) | 1965 | Case report | Lancet | Methaemoglobinaemia following lignocaine |
| [5644303](https://pubmed.ncbi.nlm.nih.gov/5644303/) | 1968 | Pharmacokinetic study | Am J Obstet Gynecol | Passage of procaine and para-aminobenzoic acid across the human placenta |

None of these publications shows a therapeutic benefit of procaine in methemoglobinemia.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 34/20.1.1/0044 | Aspen Ceftriaxone 1G Injection | Injection | Not stated in the data |

Only one registration (single-ingredient, valid) was identified, and it is for an injectable product. The product name refers to ceftriaxone, so it should be verified against the SAHPRA register whether this registration actually contains procaine. The data compiled for this report do not show Essential Medicines List (EML) status.

---

## Safety Considerations

**Drug interactions** (17 records found; the main ones are listed):
- **Major:** Nitrous acid
- **Moderate:** Sulfasalazine, and other local anaesthetics (topical or ophthalmic lidocaine, benzocaine, cocaine, tetracaine, oxybuprocaine, cinchocaine)
- **Minor:** Laronidase, hyaluronidase, doxorubicin (including liposomal)

**Conditions flagged as contraindication-related in the knowledge graph** (not taken from label text):
- Cardiac: long QT syndrome, torsades de pointes, atrioventricular block, cardiovascular and heart disease
- Haematological: thrombocytopenia, agranulocytosis, neutropenia (including congenital forms)
- Neuromuscular: myasthenia gravis, neuromuscular junction disease, butyrylcholinesterase deficiency
- Organ disease: kidney, liver and gallbladder disease
- Other: systemic lupus erythematosus, potassium deficiency, hypotensive disorders, *Clostridium difficile* colitis, necrotizing enterocolitis

The literature also describes procaine as a trigger of allergic and pseudo-allergic reactions (anaphylaxis, Hoigné's syndrome, contact dermatitis) and of methemoglobin formation.

Warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available. Please refer to the PI for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for methemoglobinemia is not supported. The evidence shows procaine causing the condition, so repurposing it for this indication would be a safety concern. There are no clinical trials, and the TxGNN score (0.9950) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**Other predictions of note:**
- **Tendinitis** (evidence level L3, research question): a 2022 study of 1% procaine neural therapy in supraspinatus tendinopathy ([35480510](https://pubmed.ncbi.nlm.nih.gov/35480510/)) and a 2013 RCT of local anaesthetic versus corticosteroid injection in lateral epicondylitis ([23494116](https://pubmed.ncbi.nlm.nih.gov/23494116/)) offer more modern, though not procaine-specific, data.
- **Fibromyalgia** (L4, research question): the evidence is limited to uncontrolled reports from 1951-1963. A modern controlled trial of trigger point injection could be a reasonable research question.
- **Anaphylaxis, hyperthyroidism, Tourette syndrome and the remaining predictions:** evidence is adverse-effect reports, historical or indirect reports, or prediction only. These are not recommended for further pursuit at this stage.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings and contraindications), which is currently a blocking gap
- Verification that the registered product (listed as ceftriaxone) actually contains procaine, and identification of the approved indication
- Mechanism of action data
- For tendinopathy or myofascial pain: a prospective, procaine-specific controlled trial with a clear safety plan covering allergy, methemoglobin and cardiac risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

