---
layout: default
title: Docetaxel
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 10
---

# Docetaxel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Docetaxel: From Taxane Antineoplastic to Female Breast Carcinoma

## One-Sentence Summary

Docetaxel is a taxane-class cytotoxic chemotherapy agent used globally for the treatment of multiple solid tumours including breast, prostate, and lung cancers, but is currently not registered in South Africa.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**,
with **50 clinical trials** and **20 publications** currently supporting this direction — including multiple large completed Phase 3 RCTs recognised by the FDA and EMA.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No SAHPRA-registered indication (drug not currently registered in South Africa) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| South Africa Market Status | Not registered |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Docetaxel is a taxane-class microtubule-stabilising agent. It works by promoting tubulin polymerisation and inhibiting depolymerisation, thereby blocking tumour cells at the G2/M phase of cell division and inducing programmed cell death (apoptosis). This mechanism directly targets the machinery that all rapidly dividing cells depend on — a hallmark of breast carcinoma regardless of subtype.

Breast cancer cells — whether hormone receptor-positive, HER2-positive, or triple-negative — depend on continuous active proliferation for growth and survival. Docetaxel's cytotoxic effect is therefore broadly applicable across breast cancer subtypes. Beyond its standalone activity, it demonstrates well-documented synergy with HER2-targeted agents (trastuzumab, pertuzumab), anthracyclines and alkylating agents (doxorubicin, cyclophosphamide), platinum salts (carboplatin), and immune checkpoint inhibitors (pembrolizumab) — making it a backbone agent across neoadjuvant, adjuvant, and metastatic treatment settings.

Docetaxel has been approved for breast cancer by both the FDA and EMA for over 30 years, with Level 1 evidence from multiple Phase 3 RCTs enrolling thousands of patients. Landmark trials such as BCIRG 005 (n=5,351), NSABP B-27 (n=2,411), HERA (n=2,168), and FNCLCC/PACS 01 (n=3,010) directly establish its clinical benefit in early and locally advanced disease, while Phase 2 and 3 data confirm its role in HER2-negative and triple-negative metastatic breast cancer. The TxGNN prediction reflects a globally established clinical reality; the primary opportunity for South Africa is establishing formal regulatory access pathways through SAHPRA.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00003782](https://clinicaltrials.gov/study/NCT00003782) | Phase 3 | Completed | 5,351 | Three-arm adjuvant trial comparing AC→T vs AT vs ATC in node-positive breast cancer; established Docetaxel-containing regimens as standard adjuvant care |
| [NCT00002707](https://clinicaltrials.gov/study/NCT00002707) | Phase 3 | Completed | 2,411 | Preoperative AC alone vs AC + Docetaxel (pre- or postoperative) in operable Stage II–III breast cancer; pivotal neoadjuvant trial establishing pCR as a surrogate endpoint |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3,270 | Adjuvant TC or AC→paclitaxel ± trastuzumab in HER2-low invasive breast cancer; large adjuvant platform assessing the role of HER2-targeted therapy addition |
| [NCT00593697](https://clinicaltrials.gov/study/NCT00593697) | Phase 3 | Completed | 2,168 | Trastuzumab + Docetaxel → FEC vs same regimen → single-agent trastuzumab in HER2+ early breast cancer; evaluated disease-free survival |
| [NCT00054587](https://clinicaltrials.gov/study/NCT00054587) | Phase 3 | Completed | 3,010 | Docetaxel 75 mg/m² + Epirubicin 75 mg/m² vs FEC100 in node-positive breast cancer with sequential trastuzumab in HER2+++ patients |
| [NCT03639948](https://clinicaltrials.gov/study/NCT03639948) | Phase 2 | Active, Not Recruiting | 120 | Pembrolizumab + Carboplatin + Docetaxel as neoadjuvant therapy in triple-negative breast cancer (TNBC); contemporary immunochemotherapy combination |
| [NCT00217672](https://clinicaltrials.gov/study/NCT00217672) | Phase 2 | Completed | 76 | Docetaxel ± Bevacizumab as first-line therapy for HER2-negative metastatic breast cancer; directly evaluated Docetaxel efficacy and the added value of anti-angiogenic therapy |
| [NCT01352494](https://clinicaltrials.gov/study/NCT01352494) | Phase 2 | Unknown | 99 | Docetaxel + Gemcitabine as neoadjuvant chemotherapy in locally advanced breast cancer; multi-centre assessment of response rate and safety profile |
| [NCT01547741](https://clinicaltrials.gov/study/NCT01547741) | Phase 3 | Unknown | 1,871 | Docetaxel + Cyclophosphamide (TC) vs anthracycline-based regimens in HER2-negative node-positive or high-risk node-negative breast cancer; direct comparison of non-anthracycline Docetaxel regimen |
| [NCT05301010](https://clinicaltrials.gov/study/NCT05301010) | Phase 3 | Completed | 128 | Trastuzumab biosimilar (NNG-TMAB) + Docetaxel in HER2+ recurrent or metastatic breast cancer; confirmed biosimilar equivalence with Docetaxel as the chemotherapy backbone |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | Phase 3 RCT | J Clin Oncol | ABC Trials (USOR 06-090, NSABP B-46-I/B-49): compared TC6 vs TaxAC — anthracycline-containing taxane regimens superior to TC6 in reducing early breast cancer recurrence |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Review | J Clin Oncol | Comprehensive review of Docetaxel's preclinical and clinical pharmacology; foundational reference establishing antineoplastic mechanism and early clinical activity in breast cancer |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Cohort | Breast Cancer (Tokyo) | Docetaxel + Cyclophosphamide + Trastuzumab (HER-TC) as neoadjuvant chemotherapy in HER2+ breast cancer; reported pCR rates with hormone receptor subtype stratification |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug Ther Bull | Comparative review of paclitaxel and docetaxel in breast and ovarian cancer; contextualised early evidence for the taxane class in breast carcinoma |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Phase 2 | Cancer | Capecitabine + Docetaxel + Epirubicin (TEX) as first-line treatment in locally advanced or metastatic breast carcinoma; demonstrated clinical activity in a triplet regimen |
| [11481357](https://pubmed.ncbi.nlm.nih.gov/11481357/) | 2001 | Phase 2 RCT | J Clin Oncol | Dose-dense Doxorubicin + Docetaxel ± Tamoxifen as preoperative therapy in operable breast cancer; randomised evaluation of pathological complete response rates |
| [15585076](https://pubmed.ncbi.nlm.nih.gov/15585076/) | 2004 | Phase 2 | Clin Breast Cancer | Docetaxel + Cisplatin as primary (neoadjuvant) chemotherapy in locally advanced breast cancer; evaluated pCR and down-staging rates prior to modified radical mastectomy |
| [9364543](https://pubmed.ncbi.nlm.nih.gov/9364543/) | 1997 | Phase 2 | Oncology | Docetaxel + Vinorelbine combination in metastatic breast cancer and NSCLC; reported response rates of 23–36% in previously untreated patients |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Phase 1 | Tumori | Docetaxel + Gemcitabine dose-finding study in anthracycline-pretreated metastatic breast cancer; established feasibility of weekly scheduling |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Cohort | Anti-Cancer Drugs | Association between adjuvant Docetaxel-based chemotherapy and breast cancer-related lymphedema; identified risk factors relevant to patient monitoring in clinical practice |

---

## South Africa Market Information

Docetaxel currently has **no SAHPRA registrations** and is not marketed in South Africa.

Healthcare professionals requiring access to Docetaxel must apply for **Section 21 unregistered medicine authorisation** from SAHPRA on a patient-by-patient or programme basis. This is a significant access barrier, given that the drug is a standard-of-care agent internationally.

There are no registered products to list at this time.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Taxane class (microtubule-stabilising agent) |
| Myelosuppression Risk | **High** — febrile neutropenia is the dose-limiting toxicity; Grade 3/4 neutropenia occurs in 75–85% of patients receiving standard 3-weekly Docetaxel 75 mg/m²; G-CSF prophylaxis is strongly recommended |
| Emetogenicity Classification | **Low to moderate** (MASCC/ESMO classification: minimal to low emetogenic potential for Docetaxel monotherapy; increases to moderate when combined with anthracyclines or platinum) |
| Monitoring Items | Full blood count (FBC) with differential before each cycle; liver function tests (ALT, AST, alkaline phosphatase, total bilirubin — Docetaxel is contraindicated with significant hepatic impairment); peripheral neuropathy assessment; fluid retention and oedema monitoring (cumulative dose-related; corticosteroid premedication required) |
| Handling Protection | Must be prepared and administered according to cytotoxic drug handling regulations — closed-system transfer devices (CSTD), appropriate PPE (gloves, gown, eye protection), dedicated pharmacy laminar-flow preparation area, and cytotoxic waste disposal per South African regulations |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for complete safety information once registration is obtained. In the interim, consult the FDA or EMA-approved prescribing information (Taxotere® US Prescribing Information / EU SmPC) for full details on warnings, contraindications, and drug interactions.

Report any adverse drug reactions experienced during Section 21 access to SAHPRA via the **MedSafety** pharmacovigilance reporting system.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Docetaxel has one of the strongest evidence bases in oncology for female breast carcinoma, with multiple completed Phase 3 RCTs (each enrolling 2,000–5,000 patients) and longstanding FDA and EMA approvals. The evidence quality meets L1 criteria. The primary barriers to use in South Africa are the complete absence of SAHPRA registration and the associated safety data gaps — these are administrative and regulatory challenges, not clinical or scientific ones.

**To proceed, the following is needed:**

- **Immediate access**: Apply for SAHPRA Section 21 unregistered medicine authorisation for individual patients requiring Docetaxel, supported by clinical justification and global prescribing information
- **Medium-term registration**: Initiate or support a full SAHPRA marketing authorisation application using the existing FDA/EMA-approved dossier as the basis (abridged registration pathway)
- **Safety documentation**: Obtain the FDA or EMA-approved Professional Information (PI/SmPC) to complete the contraindications, key warnings, and drug interaction profile review (resolving Data Gaps DG001 and DG002)
- **Pharmacy and infrastructure readiness**: Confirm cytotoxic drug preparation infrastructure (CSTD-equipped pharmacy units) and cold-chain logistics at treating institutions
- **Clinical protocols**: Develop G-CSF prophylaxis protocols for febrile neutropenia management appropriate to South African oncology practice settings, and establish corticosteroid premedication schedules for fluid retention prevention
- **Pharmacovigilance**: Register Docetaxel use under Section 21 with SAHPRA MedSafety to enable adverse event tracking prior to full registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

