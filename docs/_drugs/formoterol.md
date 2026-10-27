---
layout: default
title: Formoterol
parent: Model Prediction Only (L5)
nav_order: 240
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Formoterol: predicted new indication Respiratory malformation (evidence level L5). Approved use: Pulmonary emphysema, intrinsic asthma, allergic asthma"
monitor_inn: "FORMOTEROL"
predicted_indications: ["respiratory malformation", "bronchitis", "Rienhoff syndrome"]
---

# Formoterol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Formoterol: From Pulmonary Emphysema and Asthma to Respiratory Malformation
{: .text-alpha }

## One-Sentence Summary

Formoterol is a long-acting inhaled bronchodilator originally used for pulmonary emphysema and for intrinsic and allergic asthma.
The TxGNN model predicts it may be effective for **respiratory malformation**, but **no clinical trials** and **no publications that directly address this condition** support the prediction.
The high score most likely reflects the drug's closeness to obstructive airway diseases in the knowledge graph, not a genuine therapeutic relationship.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary emphysema, intrinsic asthma, allergic asthma (the registration entries in the data compiled for this report carry no indication text, so these come from the TxGNN knowledge graph) |
| Predicted New Indication | Respiratory malformation |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formoterol is a selective long-acting beta2-adrenergic agonist. It relaxes airway smooth muscle and gives sustained bronchodilation. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description reflects the established pharmacology of the drug class.

Respiratory malformations are structural, congenital abnormalities of the airway or lung. A bronchodilator cannot correct them. It may ease airflow obstruction or wheeze that accompanies such conditions, but that would be symptom relief, not treatment of the underlying disorder. The very high score probably reflects graph proximity to obstructive airway diseases such as asthma and emphysema. The publications retrieved concern asthma and COPD, not malformations.

The mechanistic link is therefore **not credible** for this prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for respiratory malformation.

---

## Literature Evidence

Nine publications were retrieved. None studies formoterol in respiratory malformation. They concern asthma, COPD and other conditions, and are listed here for transparency.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40840693](https://pubmed.ncbi.nlm.nih.gov/40840693/) | 2026 | Systematic review / meta-analysis | J Am Pharm Assoc | Budesonide/glycopyrrolate/formoterol compared with glycopyrrolate/formoterol for safety and efficacy in COPD |
| [35115339](https://pubmed.ncbi.nlm.nih.gov/35115339/) | 2022 | RCT (crossover) | Eur Respir J | Repeated-dose budesonide/formoterol vs salbutamol in stable adult asthma: bronchodilator, cardiovascular and adverse effects |
| [22541245](https://pubmed.ncbi.nlm.nih.gov/22541245/) | 2012 | RCT | J Allergy Clin Immunol | Long-term safety and asthma control with budesonide/formoterol in African American patients |
| [14738234](https://pubmed.ncbi.nlm.nih.gov/14738234/) | 2004 | RCT | Eur Respir J | Formoterol protection against platelet-activating-factor-induced effects in asthma |
| [20528601](https://pubmed.ncbi.nlm.nih.gov/20528601/) | 2010 | Review | J Asthma | Efficacy and safety of budesonide/formoterol pMDI in persistent asthma |
| [35034195](https://pubmed.ncbi.nlm.nih.gov/35034195/) | 2022 | Cohort | Eur J Appl Physiol | Compensatory responses to increased mechanical load in COPD during sleep |
| [24842803](https://pubmed.ncbi.nlm.nih.gov/24842803/) | 2014 | Review | Prog Neuropsychopharmacol Biol Psychiatry | Neurotransmitter-based strategies for cognitive dysfunction in Down syndrome (not relevant to formoterol in lung disease) |
| [37691104](https://pubmed.ncbi.nlm.nih.gov/37691104/) | 2023 | Case report | J Med Case Rep | Small airway disease in a patient with long COVID |
| [41686546](https://pubmed.ncbi.nlm.nih.gov/41686546/) | 2026 | Case report | Medicine | Allergic bronchopulmonary mycosis in a postoperative lung cancer patient |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A39/21.5.1/0506 | Vannair 80/4.5mcg per inhalation, 120 doses | Inhaler | Not provided |
| 36/2.6.5/0070 | Seroquel | Tablet | Not provided |

Both registrations are valid and recorded as single-ingredient products. Seroquel is normally a quetiapine brand, so this entry should be checked against the SAHPRA register before it is relied on. EML inclusion status was not available in the data compiled for this report.

---

## Safety Considerations

**Contraindications suggested by the knowledge graph.** These come from drug-disease relationships in the knowledge graph, not from approved label text, and must be verified against the SAHPRA-approved Professional Information (PI). They include:
- Cardiovascular: hypertension and long QT syndrome (including the familial form)
- Neurological: epilepsy
- Hepatic and biliary: liver disease and gallbladder disease
- Infectious: measles and herpes simplex keratitis
- Endocrine: pituitary hormone deficiencies and hypogonadotropic hypogonadism, including related syndromes (for example Kallmann syndrome and Sheehan syndrome)

**Drug interactions.** The interaction screen returned 100 interactions in total. The first 20 retrieved include:
- **Moderate:**
  - Antidiabetic agents: acarbose, alogliptin, albiglutide, dulaglutide, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide
  - QT-prolonging or related drugs: cisapride, clarithromycin, dolasetron
  - Sympathomimetics and stimulants: ephedrine (including nasal), isometheptene, diethylpropion
  - Acid suppression: famotidine
- **Minor:** corticosteroids (beclomethasone, betamethasone, budesonide, dexamethasone)

Please refer to the SAHPRA-approved Professional Information (PI) for key warnings and the full interaction list. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- There are no clinical trials and no directly relevant literature for respiratory malformation.
- The mechanism (bronchodilation) cannot correct structural congenital abnormalities.
- The 99.92% score looks like a graph-proximity artefact.

**Other predictions from the same analysis:**
- Obstructive lung disease and asthma are rated L1 (Proceed with Guardrails). Both are consistent with the existing label, so they are not true repurposing. The guardrails are:
  - Never use a long-acting beta2-agonist alone in asthma.
  - Always combine it with an inhaled corticosteroid.
  - Watch cardiovascular and pneumonia risk in COPD.
- Bronchitis is rated L2 (research question). The evidence is indirect and extends from COPD. Its trials are mostly safety and pharmacokinetic studies.

**To proceed, the following is needed:**
- Parse the SAHPRA-approved PI for warnings, contraindications and approved indications, and verify the Seroquel registration entry
- Obtain mechanism-of-action data from DrugBank
- Show any biological or clinical rationale linking beta2-agonism to a specific respiratory malformation, if one exists
- For a practical research direction, focus on the COPD/chronic bronchitis and asthma entries rather than this prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

