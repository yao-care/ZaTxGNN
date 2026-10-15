---
layout: default
title: Dicyclomine
parent: Model Prediction Only (L5)
nav_order: 176
evidence_level: L5
indication_count: 2
---

# Dicyclomine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Dicyclomine: From Irritable Bowel Syndrome to Cauda Equina Syndrome

## One-Sentence Summary

Dicyclomine is an antispasmodic (antimuscarinic) agent, originally used for irritable bowel syndrome, and the knowledge graph also lists *Clostridium difficile* colitis and neurocirculatory asthenia as related indications.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Irritable bowel syndrome (from the knowledge graph; the SAHPRA registrations carry no indication text) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on general pharmacology, dicyclomine is an antimuscarinic/antispasmodic agent that relaxes smooth muscle. Its efficacy in irritable bowel syndrome is established, and mechanistically it may be applicable to smooth-muscle dysfunction elsewhere in the body.

Cauda equina syndrome often presents with bladder dysfunction (urinary retention or overflow incontinence) because the sacral nerves are compressed. A possible, but speculative, link is symptomatic modulation of detrusor overactivity. This link is inferred, not demonstrated by the data compiled for this report.

There are important reasons for caution:
- Cauda equina syndrome is a surgical emergency that needs urgent decompression. Symptomatic drug therapy is not a treatment for the underlying condition.
- Anticholinergics can worsen urinary retention, which is the typical bladder problem in this syndrome.
- The high score (99.66%) is a computational prediction only, and no trial or publication supports it.

**Second-ranked prediction:** The model also predicts **neurogenic bladder** (listed under an obsolete disease term, score 99.50%). This is biologically more plausible because antimuscarinics are standard treatment for detrusor overactivity. However, the term may map imprecisely to current diagnoses, there is no supporting trial or publication, and bladder-selective agents such as oxybutynin and tolterodine are already established, so dicyclomine's added value is unclear.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 33/20.2.2/0267 | Pinaspor V | Vcr | Not stated in the data compiled |
| Reg. No. 32/11.4.2/0211 | Co-gel | Suspension | Not stated in the data compiled |
| Reg. No. 41/1.2/0373 | Voxra Xl 150 | Tablet | Not stated in the data compiled |
| Reg. No. 46/11.4.2/008 | Meddev | Syrup | Not stated in the data compiled |

All 4 registrations are valid single-ingredient products; none are cancelled. Essential Medicines List (EML) status could not be determined from the data compiled.

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** The knowledge graph links dicyclomine to the following conditions as contraindications or cautions. These need confirmation against the approved Professional Information (PI):
  - Eye: angle-closure (closed-angle) glaucoma
  - Urinary and prostate: benign prostatic hyperplasia, pyoureter, kidney disease
  - Gastrointestinal and hepatic: gastric ulcer, liver disease, liver failure, hepatic coma and encephalopathy, gallbladder disease
  - Cardiovascular: hypertension, coronary artery disease
  - Blood: thrombocytopenia, neutropenia, agranulocytosis, anaemia (including macrocytic)
  - Metabolic: porphyria (inherited porphyria and porphyrin metabolism disease)
  - Respiratory and sleep: obstructive sleep apnoea, sleep apnoea syndrome, congenital central hypoventilation syndrome (Haddad syndrome)
  - Psychiatric: anxiety disorder, neurotic disorder, dysthymic disorder, substance abuse/dependence
- **Drug Interactions:** 100 interactions are recorded; the 20 retrieved are all Moderate or Minor severity. The main ones are:
  - Opioids: fentanyl, alfentanil, codeine, dihydrocodeine, tramadol
  - Other anticholinergic or antihistamine agents: hyoscyamine, aclidinium, amitriptyline, chlorpheniramine, acrivastine, phenyltoloxamine
  - Other: ethanol, loperamide, amantadine, galantamine, botulinum toxin type A, acebutolol (moderate); acetaminophen and hydrochlorothiazide (minor)

  Additive anticholinergic and central nervous system effects are the main concern.

Package insert warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials or publications (Evidence Level L5). The proposed use is also clinically questionable: anticholinergic effects may worsen urinary retention, and cauda equina syndrome requires surgical decompression rather than symptomatic drug treatment.

**To proceed, the following is needed:**
- Detailed mechanism of action data
- The SAHPRA package insert (warnings, contraindications and approved indications), which is a blocking gap for safety screening
- A literature and trial search for dicyclomine in bladder dysfunction due to cauda equina syndrome or neurogenic bladder
- Clinical input on whether any symptomatic role exists, given the risk of urinary retention
- A comparison against established bladder-selective antimuscarinics if neurogenic bladder is pursued instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

