---
layout: default
title: Warfarin
parent: Moderate Evidence (L3-L4)
nav_order: 475
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Warfarin: predicted new indication Heparin cofactor 2 deficiency (evidence level L4). Approved use: Pulmonary embolism, thrombotic disease, intracranial embolism"
monitor_inn: "Warfarin"
predicted_indications: ["heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "rheumatoid arthritis", "breast fibrocystic disease", "benign mammary dysplasia", "blunt duct adenosis of breast", "apocrine adenosis of breast", "migraine disorder"]
---

# Warfarin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Warfarin: From Thrombotic Disease to Heparin Cofactor II Deficiency

## One-Sentence Summary

Warfarin is an oral vitamin K antagonist anticoagulant, originally used to treat and prevent pulmonary embolism, thrombotic disease and intracranial embolism.
The TxGNN model predicts it may be effective for **Heparin Cofactor II Deficiency** (a rare inherited thrombophilia), but the supporting evidence is limited to **3 case reports** and **no registered clinical trials**.
Of the top 10 predictions, the one with the strongest evidence is **Thrombophilia** (1 Phase 3 trial and 19 publications), although this largely overlaps with warfarin's existing use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, thrombotic disease, intracranial embolism (the SAHPRA record has no indication text) |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Warfarin is a vitamin K antagonist and is well known to reduce the synthesis of clotting factors II, VII, IX and X. Its efficacy in venous thromboembolism has been established.

Heparin cofactor II deficiency is an inherited thrombophilia, meaning a tendency to form clots. Long-term anticoagulation is a plausible approach for patients with recurrent thrombosis. This is effectively an extension of warfarin's existing thrombotic indication rather than true repurposing. The TxGNN score most likely reflects the shared thrombosis phenotype.

The other predictions fall into three groups:

- **Thrombotic and thrombophilic conditions** (factor V excess with spontaneous thrombosis, antithrombin deficiency type 2, thrombophilia): mechanistically coherent, but they overlap with existing use.
- **Rheumatoid arthritis and benign breast conditions** (fibrocystic disease, benign mammary dysplasia, blunt duct adenosis, apocrine adenosis): no plausible therapeutic mechanism. These predictions likely reflect co-prescription or drug-interaction artefacts in the knowledge graph.
- **Migraine**: several case reports describe remission on warfarin, and a hypothesis involving microembolism or hypercoagulability exists. It remains speculative, and warfarin's bleeding risk and narrow therapeutic index are major barriers.

---

## Clinical Trial Evidence

No clinical trials are registered for the top predicted indication, heparin cofactor 2 deficiency. The trials below relate to other predictions and are included for context.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00895505](https://clinicaltrials.gov/study/NCT00895505) | Phase 3 | Unknown | 300 | D-dimer-guided duration of oral anticoagulant therapy after unprovoked DVT (thrombophilia). Relevant to thrombosis management, but no results are available and it is not specific to thrombophilia. |
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completed | 3520 | Paediatric pharmacokinetic study of understudied drugs (migraine). It does not test warfarin efficacy. |
| [NCT01311622](https://clinicaltrials.gov/study/NCT01311622) | Phase 1 | Completed | 15 | Warfarin used as a probe drug in an interaction study with fostamatinib (rheumatoid arthritis). No efficacy testing. |
| [NCT04246762](https://clinicaltrials.gov/study/NCT04246762) | Phase 1 | Completed | 17 | Effect of olokizumab on CYP substrates, including S-warfarin, in rheumatoid arthritis. No therapeutic intent. |
| [NCT01636557](https://clinicaltrials.gov/study/NCT01636557) | Phase 1 | Completed | 12 | Sirukumab CYP interaction study with warfarin as a probe (rheumatoid arthritis). No therapeutic intent. |
| [NCT05392127](https://clinicaltrials.gov/study/NCT05392127) | Phase 1 | Completed | 24 | SHR0302 interaction study in healthy volunteers using S-warfarin as a probe. Not a treatment study. |

No SANCTR or PACTR identifiers were found in the data compiled for this report.

---

## Literature Evidence

**Heparin cofactor II deficiency (top prediction):** all three publications are case reports.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2214444](https://pubmed.ncbi.nlm.nih.gov/2214444/) | 1990 | Case report | Kyobu Geka | Right ventricular thrombus in a 14-year-old with familial heparin cofactor II deficiency. |
| [2033902](https://pubmed.ncbi.nlm.nih.gov/2033902/) | 1991 | Case report | Nihon Kyobu Shikkan Gakkai Zasshi | Congenital antithrombin deficiency with pulmonary infarction. The patient was on warfarin for 7 years and was then switched to low-dose heparin. |
| [11570053](https://pubmed.ncbi.nlm.nih.gov/11570053/) | 2001 | Case report (family) | Journal of UOEH | Family with multiple thromboses from infancy. A child started on warfarin had recurrent DVT. |

**Selected publications for other predictions:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39233011](https://pubmed.ncbi.nlm.nih.gov/39233011/) | 2024 | Review/Cohort | J Thromb Haemost | ISTH communication on DOACs for secondary VTE prevention in severe thrombophilia. Evidence comes only from cohort or single-centre studies. |
| [39244017](https://pubmed.ncbi.nlm.nih.gov/39244017/) | 2024 | Review | Presse Med | Impact of thrombophilia on VTE management. |
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Diagnosis and treatment of lower extremity VTE. |
| [29582922](https://pubmed.ncbi.nlm.nih.gov/29582922/) | 2017 | Case report | Hamostaseologie | Unprovoked VTE in a young patient with antithrombin type IIB deficiency (antithrombin deficiency type 2). |
| [22222938](https://pubmed.ncbi.nlm.nih.gov/22222938/) | 2012 | Review | Neurol Sci | Migraine remission on warfarin in a patient treated for pulmonary embolism, with discussion of anticoagulants for migraine prophylaxis. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case report | Headache | Migraine with aura resolved on warfarin but recurred on apixaban. |
| [8140017](https://pubmed.ncbi.nlm.nih.gov/8140017/) | 1994 | Case report | Postgrad Med J | Migraine abolished by warfarin, with a double-blind placebo rechallenge in one patient. |
| [16716139](https://pubmed.ncbi.nlm.nih.gov/16716139/) | 2006 | Case report/Review | Pharmacotherapy | Leflunomide-warfarin interaction (rheumatoid arthritis). The warfarin dose needed a 22% reduction. |
| [1591422](https://pubmed.ncbi.nlm.nih.gov/1591422/) | 1992 | Case report | Ann Pharmacother | Danazol potentiates warfarin's anticoagulant effect. This is an interaction report, not evidence of benefit in fibrocystic breast disease. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 54/8.2/0676 | Segavin 5 Mg | Tablet (oral) | Not available in the data compiled for this report |

Warfarin has 1 valid single-ingredient registration in South Africa. Essential Medicines List (EML) status was not available in the data compiled for this report.

---

## Safety Considerations

**Contraindication-related conditions (from a knowledge graph, not label text).** The TxGNN knowledge graph links warfarin to contraindication edges for the following conditions, and these should be checked against the SAHPRA Professional Information (PI):

- **Cardiovascular and metabolic:** hypertension, congestive heart failure, hyperlipidaemia, hypothyroidism
- **Hepatic and biliary:** liver failure and liver disease, gallbladder disease, cholestasis
- **Renal:** impaired renal function, nephrotic syndrome
- **Haematological:** blood coagulation disease, anaemia
- **Psychiatric:** psychotic disorders, mental disorders, substance abuse/dependence
- **Other:** connective tissue disease, bone and cartilage disease, chronic diarrhoeal disease

**Drug interactions.** The interaction query returned 100 records. The main ones from the first 20 reviewed are:

- **Major:** acetylsalicylic acid (aspirin), metronidazole
- **Moderate:** ranitidine, rabeprazole, doxycycline, amoxicillin, metformin, bupropion, aprepitant, mesalazine, balsalazide, chenodeoxycholic acid, and corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone)
- **Minor:** acarbose, albiglutide, ascorbic acid

**Other considerations from the literature:** bleeding complications with interacting drugs (for example danazol), a rare risk of warfarin-induced skin necrosis, and the need for INR monitoring.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, heparin cofactor II deficiency, is supported only by case reports (L4), and it largely overlaps with warfarin's existing thrombotic indication. Several lower-ranked predictions (rheumatoid arthritis, benign breast conditions) look like knowledge-graph artefacts from co-prescription. Migraine has interesting case reports, but its evidence is anecdotal and the bleeding risk is a major barrier. Thrombophilia (L3) may merit a research question, but it adds little beyond established VTE practice, and DOACs are increasingly used instead.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications and approved indications), which is currently missing and blocks safety screening
- Mechanism of action data
- For thrombophilia: a systematic review or comparative data on warfarin versus DOACs in inherited thrombophilia
- For migraine: a controlled study with a defined bleeding-risk assessment before any consideration
- Confirmation of EML status and of the approved indication text for Reg. No. 54/8.2/0676
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

