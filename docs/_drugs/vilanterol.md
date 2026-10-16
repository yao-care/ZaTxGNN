---
layout: default
title: Vilanterol
parent: High Evidence (L1-L2)
nav_order: 471
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Vilanterol: predicted new indication Obstructive lung disease (evidence level L1). Approved use: COPD, asthma and related airway diseases"
---

# Vilanterol
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Vilanterol: From Chronic Obstructive Pulmonary Disease and Asthma to Obstructive Lung Disease

## One-Sentence Summary

Vilanterol is a long-acting beta2-agonist (LABA) bronchodilator, originally used to treat chronic obstructive pulmonary disease (COPD) and asthma.
The TxGNN model predicts it may be effective for **obstructive lung disease**,
with **26 clinical trials** and **20 publications** currently supporting this direction.
Obstructive lung disease overlaps almost completely with vilanterol's existing indications, so this is better read as confirmation of current use than as true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | COPD, asthma and related airway diseases (the SAHPRA indication text was not available in the data compiled for this report; the original indications come from the TxGNN knowledge graph) |
| Predicted New Indication | Obstructive lung disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From established pharmacology, vilanterol is a long-acting beta2-adrenoceptor agonist. It relaxes airway smooth muscle and produces bronchodilation with once-daily dosing. It is used in fixed-dose inhalers combined with an inhaled corticosteroid (fluticasone furoate) and/or a long-acting muscarinic antagonist (umeclidinium).

Obstructive lung disease is essentially the same disease space as vilanterol's existing indications (COPD, asthma). The high TxGNN score therefore mainly confirms current use. Large Phase 3 randomised trials (IMPACT, FULFIL, HZA106829) show improvements in lung function and reductions in exacerbations. A post hoc analysis of IMPACT also reported a reduction in all-cause mortality with triple therapy (fluticasone furoate/umeclidinium/vilanterol) compared with dual therapy.

The other predictions in the ranking are weakly supported:
- **Structural or anatomical conditions** (compensatory, interstitial and congenital lobar emphysema, tracheal stenosis, tracheal calcification, hyperlucent lung): bronchodilation is not expected to modify these, and no trials or literature were found. They most likely reflect shared terms or network proximity to emphysema and COPD.
- **Bronchial neoplasm**: no antitumour mechanism is established. The only signal is a perioperative bronchodilator trial in lung cancer patients with COPD, which addresses the comorbid COPD rather than the tumour.
- **Respiratory malformation and laryngotracheitis**: no relevant evidence was found.

## Clinical Trial Evidence

The table lists the most relevant trials (Phase 3 randomised trials first). All are vilanterol-containing regimens unless noted. No SANCTR or PACTR identifiers were available in the data compiled for this report.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03162055](https://clinicaltrials.gov/study/NCT03162055) | Phase 3 | Completed | 1119 | Glycopyrronium/formoterol vs umeclidinium/vilanterol over 24 weeks in moderate to very severe COPD (AERISTO) |
| [NCT05062304](https://clinicaltrials.gov/study/NCT05062304) | N/A (registry) | Completed | 17281 | Once-daily single-inhaler triple vs dual therapy in COPD (IMPACT); registry entry for a real-world replication of the trial |
| [NCT01134042](https://clinicaltrials.gov/study/NCT01134042) | Phase 3 | Completed | 587 | Fluticasone furoate/vilanterol vs fluticasone furoate alone vs fluticasone propionate in persistent asthma, 24 weeks |
| [NCT01686633](https://clinicaltrials.gov/study/NCT01686633) | Phase 3 | Completed | 1040 | Fluticasone furoate/vilanterol 200/25 and 100/25 mcg vs fluticasone furoate 100 mcg in moderate to severe persistent asthma, 12 weeks |
| [NCT02301975](https://clinicaltrials.gov/study/NCT02301975) | Phase 3 | Completed | 1526 | Once-daily fluticasone furoate/vilanterol vs twice-daily fluticasone propionate/salmeterol in adequately controlled persistent asthma (non-inferiority) |
| [NCT01706198](https://clinicaltrials.gov/study/NCT01706198) | Phase 3 | Completed | 4233 | Open-label 12-month effectiveness study of fluticasone furoate/vilanterol vs usual maintenance therapy in asthma |
| [NCT02094937](https://clinicaltrials.gov/study/NCT02094937) | Phase 3 | Completed | 430 | Fluticasone furoate step-down from fluticasone furoate/vilanterol in well-controlled asthma (Japanese subjects) |
| [NCT01342913](https://clinicaltrials.gov/study/NCT01342913) | Phase 3 | Completed | 528 | 24-hour lung function of fluticasone furoate/vilanterol once daily vs salmeterol/fluticasone propionate twice daily in COPD |
| [NCT01777334](https://clinicaltrials.gov/study/NCT01777334) | Phase 3 | Completed | 905 | Umeclidinium/vilanterol vs tiotropium over 24 weeks in COPD (trough FEV1) |
| [NCT02487446](https://clinicaltrials.gov/study/NCT02487446) | Phase 3 | Completed | 357 | Indacaterol/glycopyrronium vs umeclidinium/vilanterol in moderate to severe COPD (crossover) |

The data compiled for this report also include other completed Phase 3 vilanterol studies in COPD and asthma, early-phase pharmacokinetic and safety studies, and several withdrawn trials with no participants (for example NCT04671355, NCT01435902 and NCT02731846).

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29668352](https://pubmed.ncbi.nlm.nih.gov/29668352/) | 2018 | RCT | N Engl J Med | Once-daily single-inhaler triple vs dual therapy in COPD (IMPACT) |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | RCT | Am J Respir Crit Care Med | FULFIL trial: once-daily triple therapy vs ICS/LABA in COPD |
| [32162970](https://pubmed.ncbi.nlm.nih.gov/32162970/) | 2020 | RCT (post hoc) | Am J Respir Crit Care Med | Reduction in all-cause mortality with fluticasone furoate/umeclidinium/vilanterol vs umeclidinium/vilanterol, using complete vital status data |
| [32918892](https://pubmed.ncbi.nlm.nih.gov/32918892/) | 2021 | RCT | Lancet Respir Med | CAPTAIN: triple therapy vs fluticasone furoate/vilanterol in inadequately controlled asthma (Phase 3A) |
| [35849317](https://pubmed.ncbi.nlm.nih.gov/35849317/) | 2022 | Network meta-analysis | Adv Ther | Comparative efficacy of fluticasone furoate/umeclidinium/vilanterol vs other triple and dual therapies in COPD |
| [39696097](https://pubmed.ncbi.nlm.nih.gov/39696097/) | 2024 | Systematic review / meta-analysis | BMC Pulm Med | Umeclidinium/vilanterol vs other bronchodilators in COPD |
| [39797646](https://pubmed.ncbi.nlm.nih.gov/39797646/) | 2024 | Cohort study | BMJ | Comparative effectiveness and safety of two single-inhaler triple therapies in routine COPD care |
| [31389190](https://pubmed.ncbi.nlm.nih.gov/31389190/) | 2019 | Systematic review | Clin Respir J | Fixed-dose umeclidinium/vilanterol in COPD |
| [28956463](https://pubmed.ncbi.nlm.nih.gov/28956463/) | 2017 | Review | Expert Rev Respir Med | Fluticasone furoate/vilanterol for COPD |
| [23232038](https://pubmed.ncbi.nlm.nih.gov/23232038/) | 2013 | Clinical pharmacology | Pulm Pharmacol Ther | Vilanterol well tolerated in healthy subjects, with prolonged bronchodilation in asthma and COPD |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 48/21.5.1/0247 | Revinty Ellipta 92/22 µg | Inhaler | Not available in the data compiled for this report |
| Reg. No. 52/21.5.1/0177 | Trelegy Ellipta | Inhaler | Not available in the data compiled for this report |

Both registrations are currently valid. The data compiled for this report did not include Essential Medicines List (EML) status.

## Safety Considerations

**Drug Interactions**

The interaction search returned 100 interacting drugs. The first 20 returned (not a ranked selection) were mostly Moderate or Minor severity:
- **Antidiabetic agents (Moderate):** acarbose, albiglutide, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide and empagliflozin. Beta2-agonists can raise blood glucose, so glycaemic control may need closer monitoring.
- **Sympathomimetics (Moderate):** ephedrine, epinephrine and diethylpropion, which may add to beta-adrenergic effects.
- **QT-prolonging or related agents (Moderate):** cisapride, clarithromycin and dolasetron.
- **Corticosteroids (Minor):** beclomethasone, betamethasone, budesonide and dexamethasone.

Warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available in the data compiled for this report. Please refer to the PI for safety information, including cardiovascular effects and pneumonia risk with LABA/ICS combinations. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 randomised trials and large RCT publications support vilanterol-containing regimens in COPD and asthma. However, the predicted "obstructive lung disease" largely restates the existing indication, so this confirms current use rather than opening a new one. The other nine predicted indications have no or only indirect evidence and should stay on **Hold**, except bronchial neoplasm, which is a research question only.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (indications, warnings, contraindications) for both registered products, which was not available in the data compiled for this report
- Confirmation that use stays within the approved COPD and asthma populations, particularly for the mono-component and triple-therapy products
- Monitoring of cardiovascular risk and pneumonia risk associated with LABA/ICS combinations
- Glycaemic monitoring in patients on antidiabetic medicines
- Mechanism of action data from DrugBank to complete the mechanistic analysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

