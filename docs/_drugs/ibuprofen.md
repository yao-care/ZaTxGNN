---
layout: default
title: Ibuprofen
parent: Model Prediction Only (L5)
nav_order: 257
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ibuprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis…"
monitor_inn: "Ibuprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "hypotrichosis simplex of the scalp", "WHIM syndrome", "congenital hypotrichosis milia"]
---

# Ibuprofen
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

# Ibuprofen: From Rheumatoid Arthritis and Osteoarthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ibuprofen is a widely used non-steroidal anti-inflammatory drug (NSAID), originally used for rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis, headache and patent ductus arteriosus.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but **no clinical trials and no publications** currently support this prediction, so it is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis, headache disorder, patent ductus arteriosus (from the knowledge-graph indication list; SAHPRA indication text was not available) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 19 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ibuprofen is generally known as a non-selective COX-1/COX-2 inhibitor that reduces prostaglandin synthesis, giving anti-inflammatory, analgesic and antipyretic effects. This general knowledge was not supplied in the compiled data.

Acromesomelic dysplasia, Hunter-Thompson type, is a skeletal dysplasia caused by loss-of-function mutations in the CDMP1/GDF5 gene, which disrupt cartilage and bone formation. Ibuprofen's original indications are inflammatory and degenerative joint conditions. No mechanistic link between prostaglandin inhibition and correction of this genetic defect is supported by the data.

The high TxGNN score (0.997) is a computational prediction. It most likely reflects knowledge-graph proximity to musculoskeletal terms rather than a biological mechanism. It should not be read as evidence of efficacy.

Other top-ranked predictions show the same pattern: brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, brachyolmia, brachydactyly-syndactyly syndrome, pseudoachondroplasia, colobomatous microphthalmia-rhizomelic dysplasia syndrome, hypotrichosis simplex of the scalp, WHIM syndrome and congenital hypotrichosis milia. All are rare genetic disorders with no trials or literature. Among them, only pseudoachondroplasia and myosclerosis have a plausible symptomatic rationale (joint pain or inflammation), and neither has a disease-modifying one.

---

## South Africa Market Information

Ibuprofen is marketed in South Africa with 19 valid single-ingredient registrations and no cancelled ones. Approved indication text and manufacturer details were not available in the compiled data. The Essential Medicines List (EML) status was also not available.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. R/3.1/186 | Adco-ibuprofen | Tablet |
| Reg. No. 49/2.7/0178 | Nurofen For Children Strawberry 4% M/V | Suspension |
| Reg. No. 33/2.8/0430 | Ibucod | Tablet |
| Reg. No. A39/2.8/0229 | Ibumol grape | Suspension |
| Reg. No. 37/2.8/0133 | Ibupain | Capsule |

Other registered products include Nurofen Express, Ibupain Forte, Mybulen, Mybulen Forte, Myprodol, Panado plus, Ibugesic plus, Advil cs, and cold and flu products (Sinutab 3-way, Benylin daytime flu, Ibumax cold & flu, Demazin Cold And Flu, Sinumax Cold And Flu), as well as Nurofen period pain. Available forms are tablets, capsules and suspensions, all for oral use.

---

## Safety Considerations

**Contraindications and conditions of concern (knowledge-graph data, not label text):** The knowledge graph links ibuprofen to the following conditions as contraindications. Verify them against the SAHPRA Professional Information (PI).
- Cardiovascular and cerebrovascular: hypertension, hypotensive disorder, myocardial infarction, stroke, cerebrovascular disorder, cerebral infarction
- Gastrointestinal: peptic ulcer disease, inflammatory bowel disease, gallbladder disease
- Hepatic and renal: liver failure, liver disease, kidney disease, pyoureter
- Blood and metabolic: thrombocytopenia, blood coagulation disease, potassium deficiency, diabetes mellitus, diabetic ketoacidosis, hypothyroidism
- Other: epilepsy, COPD, systemic lupus erythematosus, benign prostatic hyperplasia, substance abuse/dependence

**Drug Interactions:** The interaction screen returned 100 interactions, 20 of which are shown here. The one major interaction listed is **acetylsalicylic acid**. Moderate interactions include corticosteroids (betamethasone, budesonide, dexamethasone, hydrocortisone), sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), exenatide, kanamycin, levofloxacin, aprepitant, balsalazide and fenfluramine/dexfenfluramine. Minor interactions include the H2 blockers famotidine, ranitidine and cimetidine.

Warnings from the SAHPRA package insert were not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no publications and no supported mechanistic link to a genetic skeletal dysplasia. The patient population is also affected by the cardiovascular, gastrointestinal and renal cautions that apply to NSAIDs.

**To proceed, the following is needed:**
- Mechanism of action data and a biologically plausible link to GDF5/CDMP1-related pathology
- A literature and trial search (including SANCTR, PACTR and ICTRP) for any signal in skeletal dysplasias
- SAHPRA package insert warnings and contraindications
- If a role is pursued at all, consider symptomatic pain relief (for example in pseudoachondroplasia), which would need its own evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

