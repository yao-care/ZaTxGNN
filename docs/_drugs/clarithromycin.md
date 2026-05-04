---
layout: default
title: Clarithromycin
parent: 僅模型預測 (L5)
nav_order: 126
evidence_level: L5
indication_count: 10
---

# Clarithromycin
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

# Clarithromycin: From Bacterial Infections to Monoclonal Gammopathy

## One-Sentence Summary

Clarithromycin is a macrolide antibiotic with well-established use in treating respiratory tract infections, skin and soft tissue infections, and *Helicobacter pylori* eradication.
The TxGNN model predicts it may be effective for **Monoclonal Gammopathy** (encompassing the Multiple Myeloma and MGUS spectrum),
with **1 registered clinical trial** and **19 publications** — including Phase 2 trials, a Phase 3 RCT, and a systematic review — currently supporting this direction.

> **Note:** The Evidence Pack contains 10 TxGNN-predicted indications. This report focuses on **Monoclonal Gammopathy** (ranked 7th by TxGNN score, evidence level L2) as the most clinically actionable prediction. The top-ranked prediction by TxGNN score (hyperamylasemia) carries only a single case report and a "Hold" recommendation; focusing the report on that indication would not serve clinical decision-making.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (respiratory tract, skin/soft tissue, *H. pylori* eradication, Mycobacterium avium complex) |
| Predicted New Indication | Monoclonal Gammopathy (Multiple Myeloma / MGUS spectrum) |
| TxGNN Prediction Score | 98.81% |
| Evidence Level | L2 |
| South Africa Market Status | Registration data not available in current pack — verify via SAHPRA online register |
| Number of SAHPRA Registrations | Not available in current pack |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data was not captured in this Evidence Pack. However, based on well-established pharmacological knowledge, clarithromycin is a 14-membered ring macrolide antibiotic that inhibits bacterial protein synthesis by binding to the 50S ribosomal subunit. Beyond antimicrobial activity, clarithromycin has demonstrated clinically relevant **immunomodulatory and anti-inflammatory effects**, including suppression of pro-inflammatory cytokines (IL-6, IL-8, TNF-α) and inhibition of the NF-κB signalling pathway — a critical plasma cell survival signal that is constitutively activated in multiple myeloma.

Monoclonal gammopathy spans a spectrum from asymptomatic MGUS through to symptomatic Multiple Myeloma (MM) and Waldenström's Macroglobulinaemia. Clarithromycin's mechanistic contribution in this context is multi-pronged: **(1)** NF-κB inhibition undermines a key plasma cell survival axis; **(2)** modulation of the autophagosome-lysosomal pathway appears to overcome resistance to immunomodulatory drugs (IMiDs) such as lenalidomide and pomalidomide; and **(3)** broad immunoregulatory effects potentiate host anti-tumour immunity. These effects are additive rather than overlapping with standard myeloma therapies, explaining why combination regimens incorporating clarithromycin have shown enhanced efficacy.

The BiRD regimen (Biaxin + Revlimid + Dexamethasone) has become a well-recognised combination in myeloma practice over two decades of investigational use, and clarithromycin has been studied across the full MM treatment continuum — from MGUS chemoprevention through to relapsed/refractory disease — providing a broad and internally consistent evidence base that corroborates this TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006219](https://clinicaltrials.gov/study/NCT00006219) | Phase 2 | Completed | N/A | Randomised Phase 2 comparing DHEA vs clarithromycin (Biaxin) in MGUS patients at high risk of progression to multiple myeloma; evaluated clarithromycin as a chemopreventive agent against myeloma development |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34021118](https://pubmed.ncbi.nlm.nih.gov/34021118/) | 2021 | Randomised Controlled Trial (Phase 3) | *Blood Cancer Journal* | Phase 3 RCT (n=286, transplant-ineligible MM); Rd ± clarithromycin until progression — no significant PFS difference, but provides definitive data on the addition of clarithromycin to continuous Rd |
| [36394758](https://pubmed.ncbi.nlm.nih.gov/36394758/) | 2022 | Systematic Review / Meta-analysis | *Eur Rev Med Pharmacol Sci* | Meta-analysis of pomalidomide + dex-based triplet regimens in relapsed/refractory MM; comparative safety and efficacy of clarithromycin-containing arms assessed |
| [30792190](https://pubmed.ncbi.nlm.nih.gov/30792190/) | 2019 | Phase 2 Trial | *Blood Advances* | Phase 2 ClaPd study (clarithromycin + pomalidomide + dex, n=120) in RRMM with prior lenalidomide exposure; demonstrated meaningful responses in heavily pre-treated patients (median 5 prior lines) |
| [34424561](https://pubmed.ncbi.nlm.nih.gov/34424561/) | 2021 | Phase 2 Trial | *Am J Hematology* | Car-BiRd regimen: carfilzomib/dex induction followed by lenalidomide + clarithromycin + dex consolidation and lenalidomide maintenance in newly diagnosed MM; achieved high response rates with reduced toxicity profile |
| [17989313](https://pubmed.ncbi.nlm.nih.gov/17989313/) | 2008 | Phase 2 Trial | *Blood* | BiRD (clarithromycin + lenalidomide + dex) as first-line therapy in treatment-naive symptomatic MM; established high complete and overall response rates that underpinned subsequent BiRD research |
| [24723438](https://pubmed.ncbi.nlm.nih.gov/24723438/) | 2014 | Cohort Study | *Am J Hematology* | Addition of clarithromycin to Rd at time of progression in 24 patients (median 3 prior therapies); 48% response rate, demonstrating ability to overcome established lenalidomide/dex resistance |
| [24576165](https://pubmed.ncbi.nlm.nih.gov/24576165/) | 2014 | Phase 2 Trial | *Leukemia & Lymphoma* | T-BiRD (thalidomide + clarithromycin + lenalidomide + dex) in 26 newly diagnosed symptomatic MM patients; high overall response rate reported |
| [27804150](https://pubmed.ncbi.nlm.nih.gov/27804150/) | 2017 | Clinical Study | *Am J Hematology* | Addition of clarithromycin to IMiD-based therapy in 31 MM and 17 AL amyloidosis patients refractory to IMiDs; 48% haematological response in MM group — suggests clarithromycin can re-sensitise resistant disease |
| [12685831](https://pubmed.ncbi.nlm.nih.gov/12685831/) | 2002 | Phase 2 Trial | *Leukemia & Lymphoma* | BLT-D (clarithromycin + low-dose thalidomide + dex) in previously untreated or treated MM and Waldenström's macroglobulinaemia; earliest formal Phase 2 evaluation establishing anti-myeloma activity of clarithromycin |
| [33138750](https://pubmed.ncbi.nlm.nih.gov/33138750/) | 2021 | Review | *Curr Med Chemistry* | Comprehensive review of drug repositioning in haematological malignancies; clarithromycin's mechanistic rationale and clinical evidence in MM detailed with signalling pathway context |

---

## South Africa Market Information

SAHPRA registration data was not available in this Evidence Pack (0 licences returned). This is likely a data capture gap, as clarithromycin is a widely used antibiotic available in many countries.

**Required action before proceeding:** Verify the current SAHPRA registration status, registered formulations (tablet, oral suspension, IV), and approved indications via the [SAHPRA medicines register](https://www.sahpra.org.za). Cross-reference with the National Essential Medicines List (EML) for relevant dosage forms.

---

## Safety Considerations

Detailed SAHPRA-registered warnings and contraindications were not available in this Evidence Pack. The following safety considerations are drawn from published clinical experience in the myeloma setting and are not exhaustive:

- **QT prolongation**: Clarithromycin prolongs the QTc interval. Many myeloma regimens (e.g., combinations with carfilzomib, bortezomib, or azole antifungals) carry additive QT risk. Baseline and on-treatment ECG monitoring is recommended.
- **CYP3A4 inhibition**: Clarithromycin is a potent CYP3A4 inhibitor. Dose adjustments may be required for co-administered agents metabolised by CYP3A4 that are commonly used in myeloma regimens (e.g., carfilzomib, ixazomib, certain corticosteroids, calcineurin inhibitors).
- **Neurological effects**: Auditory toxicity (hearing loss, tinnitus) and sensory disturbances have been reported, particularly at higher doses or with prolonged treatment. Clarithromycin itself may cause peripheral neuropathy symptoms, which is particularly relevant when combined with neurotoxic agents such as thalidomide or bortezomib.
- **Gastrointestinal**: Nausea, diarrhoea, abdominal discomfort, and taste disturbances are common and may compound IMiD-related GI side effects.

Please refer to the SAHPRA-approved Professional Information (PI) for complete safety information. Report adverse drug reactions to SAHPRA via the [MedSafety reporting system](https://www.sahpra.org.za/report-adverse-events/).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clarithromycin has a coherent mechanistic basis for activity in plasma cell dyscrasias (NF-κB inhibition, IMiD potentiation, immunomodulation), supported by multiple Phase 2 trials, one Phase 3 RCT, and a systematic review. However, the only Phase 3 RCT (PMID 34021118) did not demonstrate a statistically significant PFS benefit for adding clarithromycin to continuous Rd in transplant-ineligible patients, which tempers enthusiasm despite consistently positive Phase 2 signals. The drug has a well-characterised safety profile accumulated over decades of infectious disease use.

**To proceed, the following is needed:**

- Confirm SAHPRA registration status, available formulations, and approved indications via the SAHPRA online register
- Obtain the SAHPRA-approved Professional Information (PI) to complete a full safety and contraindication review
- Consult a South African haematologist or oncologist experienced in myeloma management before initiating off-label use in plasma cell dyscrasias
- Establish a formal drug interaction assessment for the intended combination regimen, particularly regarding CYP3A4-mediated interactions and QTc additive risk
- Implement a baseline and on-treatment ECG monitoring protocol for QTc interval surveillance
- Consider whether the use case is newly diagnosed MM (where Phase 2 data are stronger) or relapsed/refractory disease (where resistance-overcoming evidence is promising but Phase 3 data are lacking)
- Identify applicable South African clinical trial registrations via [SANCTR](https://www.sanctr.gov.za) or [PACTR](https://pactr.samrc.ac.za) should a formal investigational pathway be pursued

---

> *This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. This document should be reviewed by a qualified South African healthcare professional familiar with the relevant patient population and local treatment guidelines.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

