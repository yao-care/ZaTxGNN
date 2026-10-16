---
layout: default
title: Tacrolimus
parent: Model Prediction Only (L5)
nav_order: 432
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Tacrolimus: predicted new indication Seborrheic dermatitis (evidence level L5). Approved use: Atopic eczema / atopic dermatitis"
monitor_inn: "TACROLIMUS"
predicted_indications: ["seborrheic dermatitis", "parapsoriasis", "dermatitis"]
---

# Tacrolimus
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Tacrolimus: From Atopic Eczema to Seborrheic Dermatitis

## One-Sentence Summary

Tacrolimus is a calcineurin inhibitor, originally used for atopic eczema (atopic dermatitis).
The TxGNN model predicts it may be effective for **Seborrheic Dermatitis**,
with **2 directly relevant clinical trials** (both completed) and **several publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic eczema / atopic dermatitis (per the TxGNN knowledge graph; SAHPRA indication text was not available) |
| Predicted New Indication | Seborrheic dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 (see note below) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* The strict rule (at least two completed Phase 3 RCTs) is not fully met for seborrheic dermatitis, where there is one completed Phase 3 trial and one completed Phase 4 trial. The L1 grade follows the compiled assessment; a conservative reading would be L2.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the literature, tacrolimus is a calcineurin inhibitor. It blocks T-cell activation and the release of inflammatory cytokines (such as IL-2, IL-4 and interferon-gamma). Its efficacy in atopic dermatitis is well established.

Seborrheic dermatitis is a chronic, relapsing inflammatory skin disease affecting mainly the face and scalp. It involves an inflammatory response to *Malassezia* yeast and a disrupted skin barrier. The same anti-inflammatory pathway that works in atopic dermatitis is therefore plausible here. Topical tacrolimus also avoids the skin thinning (atrophy) associated with repeated topical corticosteroid use on the face, which makes it attractive for maintenance therapy.

The published literature supports facial use and maintenance therapy (for example PMID 26512166, 19213227 and 27804089).

**Other predictions (brief):**
- **Parapsoriasis** (score 99.24%): Evidence is limited to two case reports of topical tacrolimus in pityriasis lichenoides, with no registered trials (evidence level L4, research question only). Large plaque parapsoriasis carries a lymphoma-progression risk, which these reports do not address.
- **Dermatitis** (score 99.17%): This largely confirms the existing atopic dermatitis use rather than offering new repurposing. It is supported by many trials, including large Phase 3 studies, but extension to other dermatitis subtypes should be assessed individually.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Protopic (tacrolimus) ointment as maintenance treatment of severe seborrheic dermatitis on the adult face, aiming to reduce relapses and steroid use |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Proactive once- or twice-weekly 0.1% tacrolimus ointment to keep adult facial seborrheic dermatitis in remission and reduce flares |

Results of these trials are not described in the data compiled for this report. No SANCTR or PACTR identifiers were found.

For reference, the broader dermatitis category includes many completed Phase 3/4 atopic dermatitis trials, for example [NCT00560378](https://clinicaltrials.gov/study/NCT00560378) (n=789, long-term safety of 0.1% ointment) and [NCT02601703](https://clinicaltrials.gov/study/NCT02601703) (n=1110, generic vs Protopic equivalence).

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Clinical study | Annals of Dermatology | Maintenance therapy of facial seborrheic dermatitis with 0.1% tacrolimus ointment, adapting the low-dose intermittent regimen used in atopic dermatitis |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic review | Am J Clin Dermatol | Topical treatment of facial seborrheic dermatitis; reviews antifungals, keratolytics and corticosteroids |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | Topical calcineurin inhibitors as a safe alternative to corticosteroids in seborrheic dermatitis |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | Current status and therapeutic horizons of facial seborrheic dermatitis |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | Clinical trial | Annals of Parasitology | Sertaconazole 2% cream vs tacrolimus 0.03% cream in 60 patients with seborrheic dermatitis |
| [31476936](https://pubmed.ncbi.nlm.nih.gov/31476936/) | 2019 | Review | J Cutan Med Surg | Evidence for off-label use of topical calcineurin inhibitors in dermatologic disorders |
| [15461548](https://pubmed.ncbi.nlm.nih.gov/15461548/) | 2004 | Review | Expert Opin Pharmacother | Tacrolimus ointment in atopic dermatitis and other inflammatory skin disease |
| [36370744](https://pubmed.ncbi.nlm.nih.gov/36370744/) | 2023 | Systematic review / meta-analysis | Lancet Child Adolesc Health | Cancer risk with topical calcineurin inhibitors in atopic dermatitis (safety) |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. A40/13.12/0219 | Protopic | Ointment | Not available in the compiled data |
| Reg. No. A39/34/0647 | Prograf | Capsule | Not available in the compiled data |
| Reg. No. 32/34/0561 | Prograf ampoule 1ml | Infusion | Not available in the compiled data |
| Reg. No. 43/34/1051 | Graftac 0,5 | Capsule | Not available in the compiled data |
| Reg. No. 51/32.16/0172 | Tacrum 0,5 Mg | Capsule | Not available in the compiled data |

All five registrations are valid single-ingredient products. Only the ointment (Protopic) is relevant to a topical dermatological use; the capsule and infusion products are systemic formulations. Essential Medicines List status could not be confirmed from the compiled data.

## Safety Considerations

SAHPRA package insert warnings and contraindications were not available in the compiled data. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Additional information that was compiled:

- **Knowledge-graph contraindication signals** (not label text): the knowledge graph links tacrolimus with conditions including hypertension, long QT syndrome/torsades de pointes, liver failure, kidney disease, epilepsy, hyperglycaemia/diabetes, active or chronic infections (including herpes simplex, herpes zoster and Epstein-Barr virus), cancer and lymphoma, progressive multifocal leukoencephalopathy and posterior leukoencephalopathy syndrome. Many of these relate mainly to systemic use and should be checked against the PI for the topical product.
- **Drug interactions** (100 recorded in total; examples): *Major* interactions include amphotericin B, loperamide, mesalazine, omeprazole and balsalazide. *Moderate* interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), metformin, pioglitazone, famotidine, rabeprazole and metronidazole. These are most relevant to systemic tacrolimus; systemic absorption from topical use is minimal.
- **Malignancy concern**: a 2023 systematic review (PMID 36370744) examined cancer risk with topical calcineurin inhibitors, and the topic remains part of the long-term safety discussion for tacrolimus ointment.
- Topical corticosteroid or calcineurin inhibitor use can mask or alter fungal skin infections such as tinea incognito (PMID 20347654, 38892976), so diagnosis should be confirmed before treatment.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Tacrolimus ointment is already registered in South Africa (Protopic) and has a plausible anti-inflammatory mechanism in seborrheic dermatitis. One completed Phase 3 trial, one completed Phase 4 trial and supportive clinical literature point in the same direction. Published efficacy results are not yet summarised here, and the safety label data are missing, so use should remain controlled.

**To proceed, the following is needed:**
- Retrieve the SAHPRA Professional Information for Protopic (indications, warnings, contraindications, malignancy statements)
- Review the published results of NCT02004860 and NCT01591070 to confirm efficacy and relapse-prevention outcomes
- Detailed mechanism of action data (for example from DrugBank)
- Confirm whether the existing SAHPRA indication covers seborrheic dermatitis, since this would be off-label use
- A long-term safety monitoring plan, including skin infection and malignancy surveillance, for facial maintenance use
- Check local availability and Essential Medicines List status of the ointment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

