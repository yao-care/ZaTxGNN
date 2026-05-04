---
layout: default
title: Azathioprine
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azathioprine: From Organ Transplant Rejection to Inflammatory Bowel Disease

## One-Sentence Summary

Azathioprine (AZA) is a thiopurine immunosuppressant prodrug, established globally as a first-line immunomodulator for organ transplant rejection prevention and autoimmune conditions, but currently unregistered with SAHPRA in South Africa.
The TxGNN model predicts it may be effective for **Inflammatory Bowel Disease (IBD)** — encompassing Crohn's disease and ulcerative colitis — with **50+ clinical trials** and **20 publications** supporting this direction, representing the highest-evidence clinically actionable prediction in this analysis (Rank 5 by TxGNN score; the four highest-scoring predictions are rare congenital or genetic structural disorders without immunological plausibility, each recommended Hold with no supporting evidence).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Organ transplant rejection prevention; autoimmune diseases (not currently SAHPRA-registered in South Africa) |
| Predicted New Indication | Inflammatory Bowel Disease (Crohn's disease and Ulcerative Colitis) |
| TxGNN Prediction Score | 99.52% (Rank 5 by TxGNN score; highest-evidence clinically actionable prediction in this pack) |
| Evidence Level | L1 (multiple completed Phase 3 RCTs + Cochrane systematic reviews, 2025 update) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Azathioprine is a prodrug that undergoes non-enzymatic conversion to 6-mercaptopurine (6-MP), which is further metabolised intracellularly to 6-thioguanine nucleotides (6-TGN) — the primary active metabolites. These exert immunosuppression through three complementary mechanisms: (1) competitive inhibition of de novo purine synthesis, blocking DNA and RNA production in rapidly dividing cells; (2) induction of activated T-cell apoptosis via inhibition of Rac1 GTPase, a pathway selectively active in proliferating lymphocytes; and (3) direct interference with DNA synthesis, suppressing clonal lymphocyte expansion. The balance between efficacious 6-TGN and hepatotoxic 6-methylmercaptopurine (6-MMP) metabolites is substantially governed by pharmacogenetic variation in TPMT (thiopurine methyltransferase) and NUDT15, making pre-treatment pharmacogenomic screening essential to safe clinical use.

The core pathology of IBD — comprising Crohn's disease (CD) and ulcerative colitis (UC) — involves dysregulated intestinal mucosal immunity. In CD, Th1/Th17 lymphocyte activity drives transmural granulomatous inflammation; in UC, Th2/Th17 dysregulation results in superficial mucosal ulceration and barrier breakdown. AZA's mechanism directly targets this shared inflammatory cycle: by suppressing pathogenic lymphocyte proliferation and inducing activated T-cell apoptosis, AZA reduces the inflammatory burden that perpetuates mucosal relapse in both conditions. This mechanistic alignment is what makes AZA therapeutically rational across the IBD spectrum.

This biological plausibility is confirmed by over four decades of accumulated clinical evidence. Multiple completed Phase 3 randomised controlled trials, three Cochrane systematic reviews (updated most recently in 2025), and a landmark 2025 RCT in acute severe UC collectively establish AZA as the global standard first-line immunomodulator for IBD maintenance therapy — formally endorsed at Grade A by ECCO (European Crohn's and Colitis Organisation) guidelines. The primary challenge for South Africa is not a lack of efficacy evidence, but the complete absence of SAHPRA registration, which creates a significant access and regulatory gap for patients with IBD who could benefit from this affordable, well-characterised therapy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00094458](https://clinicaltrials.gov/study/NCT00094458) | Phase 3 | Completed | 508 | Landmark multicentre double-blind RCT comparing infliximab monotherapy, AZA monotherapy, and infliximab + AZA combination in biologic- and immunomodulator-naïve Crohn's disease. AZA served as the active control arm, confirming its established standard-of-care role and providing direct comparative efficacy data at scale. |
| [NCT00098111](https://clinicaltrials.gov/study/NCT00098111) | Phase 3 | Terminated | 31 | ACORDIS study: double-blind, dose-ranging RCT directly investigating optimal weight-based azathioprine dosing in active Crohn's disease requiring corticosteroids. Early termination due to slow enrolment; however, provides Phase 3 safety and dose–response data for AZA monotherapy, directly informing dose selection in clinical practice. |
| [NCT00946946](https://clinicaltrials.gov/study/NCT00946946) | Phase 3 | Completed | 78 | Double-blind, double-dummy multicentre RCT comparing AZA versus mesalazine for prevention of clinical relapse in post-operative Crohn's disease patients with moderate-to-severe endoscopic recurrence. Directly evaluates AZA's role in the postoperative maintenance setting. |
| [NCT00976690](https://clinicaltrials.gov/study/NCT00976690) | Phase 3 | Completed | 83 | Multicentre randomised open-label study comparing AZA vs. mesalazine for prevention of postoperative Crohn's disease recurrence; superiority design provides direct comparative evidence for AZA as a postoperative maintenance immunomodulator. |
| [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) | Phase 3 | Unknown | 84 | Investigator-initiated multicentre parallel-arm RCT directly comparing low-dose AZA + allopurinol (metabolite-optimisation strategy) vs. standard-dose AZA monotherapy in ulcerative colitis. Addresses the major clinical challenge that up to 50% of UC patients fail or experience adverse events on standard AZA therapy. |
| [NCT02425852](https://clinicaltrials.gov/study/NCT02425852) | Phase 4 | Completed | 65 | Multicentre randomised open-label trial evaluating early combination infliximab + AZA vs. corticosteroids + AZA in acute severe ulcerative colitis responding to IV corticosteroids. Directly positions AZA within evidence-based management of the highest-acuity IBD scenario. |
| [NCT00537316](https://clinicaltrials.gov/study/NCT00537316) | Phase 3 | Terminated | 242 | Three-arm multicentre RCT comparing infliximab monotherapy, infliximab + AZA, and AZA monotherapy in moderate-to-severe active ulcerative colitis; the AZA-only arm provides direct Phase 3 monotherapy data in UC despite early termination. |
| [NCT05040464](https://clinicaltrials.gov/study/NCT05040464) | Phase 3 | Recruiting | 166 | Open-label RCT directly comparing AZA versus methotrexate as the immunosuppressant component of combination therapy with adalimumab in Crohn's disease. Contemporary design positions AZA within modern biologic-combination strategies and will inform the best immunomodulator partner for anti-TNF therapy. |
| [NCT02852694](https://clinicaltrials.gov/study/NCT02852694) | Phase 4 | Completed | 192 | Risk-stratified paediatric CD RCT comparing weekly subcutaneous methotrexate vs. daily oral AZA/6-MP (low-risk group) vs. subcutaneous adalimumab (high-risk group) for maintaining remission. Provides AZA vs. MTX head-to-head evidence in paediatric IBD, informing treatment sequencing decisions. |
| [NCT01802593](https://clinicaltrials.gov/study/NCT01802593) | Phase 4 | Terminated | 20 | Paediatric multicentre RCT evaluating two AZA withdrawal strategies after achieving remission on infliximab + AZA combination therapy in active paediatric Crohn's disease. Directly addresses the clinically important question of how long to maintain AZA after biological induction. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | Cochrane Systematic Review | Cochrane Database Syst Rev | The most current Cochrane review updating evidence for AZA and 6-MP in maintenance of remission in ulcerative colitis; synthesises all available RCT-level evidence confirming the sustained clinical role of thiopurines in UC maintenance. |
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | RCT | Gut | ACTIVE trial: parallel, open-label RCT comparing infliximab + AZA vs. AZA monotherapy as maintenance therapy following corticosteroid-responsive acute severe UC. The most recent high-quality head-to-head evidence for AZA-based regimens in the most challenging IBD scenario. |
| [40538240](https://pubmed.ncbi.nlm.nih.gov/40538240/) | 2025 | Clinical Study | Aliment Pharmacol Ther | Contemporaneous comparative study evaluating AZA vs. tofacitinib as maintenance therapy in corticosteroid-responsive acute severe ulcerative colitis; directly positions AZA against newer JAK inhibitors. |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | Meta-analysis | Aliment Pharmacol Ther | Meta-analysis directly quantifying the efficacy of AZA and 6-MP in ulcerative colitis; establishes thiopurine superiority over placebo for maintenance of remission in UC with pooled statistical estimates. |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Comprehensive Review | J Crohn's Colitis | Expert multidisciplinary review of thiopurine treatment in IBD; covers indications, pharmacogenomics (TPMT, NUDT15), TDM (6-TGN/6-MMP monitoring), safety, and practical management guidance. Essential clinical reference for practitioners initiating AZA in IBD. |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | Mechanism & Clinical Review | Expert Rev Gastroenterol Hepatol | Detailed review of AZA's molecular mechanism of action in IBD — including the Rac1 GTPase T-cell apoptosis pathway — integrated with 45 years of clinical trial evidence; directly supports the mechanistic rationale for AZA use in IBD. |
| [22072847](https://pubmed.ncbi.nlm.nih.gov/22072847/) | 2011 | Clinical Practice Review | World J Gastroenterol | Practical guidance on optimising 6-MP and AZA therapy in IBD; covers therapeutic drug monitoring (6-TGN levels predict efficacy; elevated 6-MMP predicts hepatotoxicity), dose adjustment, and allopurinol co-administration strategies. |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | Cochrane Systematic Review | Cochrane Database Syst Rev | 2016 Cochrane review on AZA/6-MP for maintenance of remission in UC; intermediate update in the ongoing review cycle demonstrating consistent evidence across multiple systematic synthesis iterations. |
| [9412914](https://pubmed.ncbi.nlm.nih.gov/9412914/) | 1997 | Prospective Clinical Study | J Clin Gastroenterol | Foundational prospective study evaluating AZA in steroid-resistant (n=10) and steroid-dependent (n=46) UC over a mean follow-up of 29 months; establishes the critical clinical niche of AZA as a corticosteroid-sparing agent in UC, which remains its primary current use. |
| [10499471](https://pubmed.ncbi.nlm.nih.gov/10499471/) | 1999 | Clinical Efficacy & Safety Review | Scand J Gastroenterol Suppl | Update on clinical efficacy and safety of AZA for long-term IBD therapy, including documentation of the Netherlands regulatory approval for long-term AZA maintenance in Crohn's disease; provides the historical regulatory and clinical foundation for the IBD indication. |

---

## South Africa Market Information

Azathioprine currently has **no SAHPRA-registered products** on the South African market.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | No registered products | — | No SAHPRA-approved products at time of report |

> **Regulatory access note:** Despite azathioprine's well-established global evidence base for IBD, no SAHPRA-registered formulation is available in South Africa. Clinicians wishing to prescribe azathioprine for IBD patients would currently need to apply for SAHPRA Section 21 (unregistered medicines) authorisation on a per-patient basis. Azathioprine appears on the WHO Essential Medicines List and is listed in multiple international IBD guidelines (ECCO, ACG, BSG) as a first-line immunomodulator — making a formal SAHPRA registration application a priority if this medicine is to be used routinely.

---

## Safety Considerations

Please refer to the manufacturer's international Professional Information (PI) for complete safety data, as no SAHPRA-approved South African PI exists. Report any observed adverse drug reactions to SAHPRA's pharmacovigilance programme.

The following safety considerations are directly relevant to IBD use and the South African clinical context:

- **Haematological toxicity (Key Warning):** Myelosuppression — including leucopenia, thrombocytopenia, and anaemia — is dose-dependent and can be life-threatening. Risk is substantially increased in patients with reduced TPMT or NUDT15 enzyme activity. Pre-treatment pharmacogenomic screening (TPMT enzyme activity assay or genotype; NUDT15 genotype, particularly relevant for patients of African or Asian ancestry) is strongly recommended before initiating therapy. Full blood count (FBC) with differential must be monitored regularly throughout treatment.

- **Infection risk (Key Warning):** Immunosuppression increases susceptibility to bacterial, viral, and opportunistic infections. This is particularly important in the South African context given the high burden of tuberculosis and HIV. Active TB or HIV must be excluded and managed appropriately before commencing AZA. All appropriate vaccinations (including pneumococcal, influenza, and hepatitis B vaccines) should be administered **prior** to initiation, as live vaccines are contraindicated during treatment.

- **Hepatotoxicity:** Elevated liver enzymes are associated with accumulation of the toxic metabolite 6-MMP. Liver function tests should be monitored regularly. The strategy of combining low-dose AZA with allopurinol preferentially shunts metabolism toward 6-TGN and away from 6-MMP, and may reduce hepatotoxicity while improving efficacy in selected patients (requires AZA dose reduction to 25–33% of standard dose).

- **Long-term malignancy risk:** Prolonged thiopurine therapy is associated with a small but statistically increased risk of EBV-associated lymphoproliferative disease (especially in younger patients) and non-melanoma skin cancer. Regular dermatological review, strict sun protection, and periodic reassessment of the risk–benefit balance are advised, particularly beyond 3–5 years of use.

- **Drug Interactions:** No formal drug interaction data was available in this evidence pack. Clinically critical interactions include: allopurinol (markedly increases 6-TGN levels — mandatory AZA dose reduction to 25% of usual dose required when co-prescribed); aminosalicylates such as mesalazine and sulfasalazine (inhibit TPMT, increasing myelosuppression risk); and warfarin (AZA may reduce anticoagulant effect, requiring INR monitoring).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Azathioprine has one of the most robust and mature evidence bases of any immunomodulator in IBD management — supported by multiple completed Phase 3 RCTs, three sequential Cochrane systematic reviews (most recently updated in 2025), a 2025 RCT specifically evaluating AZA-based strategies in acute severe UC, and formal endorsement in international IBD guidelines. The TxGNN model prediction at Rank 5 is fully consistent with this established global evidence and presents no novel mechanistic leap. The primary barrier to use in South Africa is the complete absence of SAHPRA registration, not any lack of efficacy or mechanistic evidence.

**To proceed, the following is needed:**

- **SAHPRA registration or Section 21 authorisation:** A formal regulatory pathway must be established. Given the comprehensive Phase 3 RCT dossier and multiple Cochrane-level systematic reviews available, a SAHPRA registration submission is strongly justified and should be prioritised. Section 21 individual patient authorisation remains the interim access route.
- **Pre-treatment pharmacogenomic screening protocol:** A South African clinical guideline specifying TPMT enzyme activity measurement (and NUDT15 genotyping where applicable for non-European ancestry patients) must be established before routine prescribing to prevent severe haematological toxicity.
- **Therapeutic drug monitoring (TDM) capacity:** The ability to measure 6-TGN and 6-MMP metabolite levels should be available at IBD-treating institutions to guide dose optimisation, differentiate treatment failures from non-adherence, and manage hepatotoxicity.
- **South African infection screening protocol:** A context-specific protocol addressing TB exclusion (TST/IGRA), hepatitis B serology, HIV testing, and pre-treatment vaccination must be developed and implemented, reflecting the local epidemiological burden of opportunistic infections.
- **Local pharmacovigilance:** Healthcare professionals should systematically report adverse drug reactions observed with azathioprine to SAHPRA, contributing to local safety surveillance in a population where pharmacogenomic risk profiles may differ from those studied in existing predominantly European and North American trials.

---

> **Disclaimer:** This report is intended for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All clinical decisions should be made in accordance with approved prescribing information and applicable South African regulatory requirements.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

