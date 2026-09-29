---
layout: default
title: Pheniramine
parent: Moderate Evidence (L3-L4)
nav_order: 363
evidence_level: L4
indication_count: 3
---

# Pheniramine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Pheniramine: From H1 Antihistamine Use to Allergic Urticaria

## One-Sentence Summary

Pheniramine is a first-generation H1-receptor antagonist, and its registered South African product is an oral effervescent tablet.
The TxGNN model predicts it may be effective for **allergic urticaria**.
Evidence is thin: **1 registered trial** (judged a spurious match) and **18 publications**, none showing pheniramine-specific efficacy in urticaria.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration record |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Pheniramine is a first-generation H1-receptor antagonist. Its use in allergic conditions is well established for this drug class, and mechanistically it may be applicable to allergic urticaria.

In allergic urticaria, histamine released from mast cells causes the wheal-and-flare response, and H1 blockade directly targets this pathway. This class-level logic is consistent with the very high TxGNN score.

The supporting evidence comes from related agents (chlorpheniramine, dexchlorpheniramine), not from pheniramine itself. No pheniramine-specific efficacy trial for urticaria is in the supplied data. The literature also contains pheniramine hypersensitivity and adverse-event reports, so safety needs review before any recommendation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02082054](https://clinicaltrials.gov/study/NCT02082054) | Phase 2 | Unknown | 125 | Dose-ranging study of atropine added to pseudoephedrine/chlorpheniramine in seasonal allergic rhinitis. Focused on atropine dosing, not pheniramine or urticaria, so it is a weak match and gives no direct evidence. |

No SANCTR or PACTR registrations were identified in the supplied data.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39265704](https://pubmed.ncbi.nlm.nih.gov/39265704/) | 2024 | Randomised phase I trial | Eur J Pharm Sci | Compared bilastine with parenteral dexchlorpheniramine on histamine-induced wheal and flare (related drug, not pheniramine) |
| [14709123](https://pubmed.ncbi.nlm.nih.gov/14709123/) | 2004 | Clinical study | Med J Aust | Hydrocortisone infusion with or without chlorpheniramine bolus to prevent early adverse reactions to snakebite antivenom |
| [35652393](https://pubmed.ncbi.nlm.nih.gov/35652393/) | 2024 | Review | Curr Rev Clin Exp Pharmacol | Review of chlorpheniramine, an alkylamine first-generation H1 antihistamine, including its use in chronic urticaria |
| [2859711](https://pubmed.ncbi.nlm.nih.gov/2859711/) | 1985 | Review | Z Hautkr | Worldwide astemizole results, including chronic urticaria; pheniramine is among the comparators |
| [12444322](https://pubmed.ncbi.nlm.nih.gov/12444322/) | 2002 | Clinical study | Int Arch Allergy Immunol | Single-dose oral tolerance testing with alternative compounds in drug adverse reactions |
| [18597008](https://pubmed.ncbi.nlm.nih.gov/18597008/) | 2008 | Surveillance study | Methods Find Exp Clin Pharmacol | Large-scale sedation surveillance of H1 antihistamines in 1,742 patients |
| [15698856](https://pubmed.ncbi.nlm.nih.gov/15698856/) | 2005 | Preclinical | Life Sci | Combined H1 and H3 blockade (with chlorpheniramine) reduced compound 48/80-induced skin vascular permeability in guinea pigs |
| [40125237](https://pubmed.ncbi.nlm.nih.gov/40125237/) | 2025 | Case report | Cureus | Immediate hypersensitivity reaction to pheniramine in multiple drug hypersensitivity syndrome (safety signal) |
| [40324831](https://pubmed.ncbi.nlm.nih.gov/40324831/) | 2025 | Case report | Indian J Pharmacol | Loss of consciousness after concurrent IV pheniramine and hydrocortisone for a drug allergic reaction |
| [31852144](https://pubmed.ncbi.nlm.nih.gov/31852144/) | 2019 | Case reports + pharmacovigilance review | Medicine | Chlorpheniramine-induced anaphylaxis (safety signal) |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 28/5.8/0696 | Degoran Fizzy Effervescent Tablets | Effervescent tablet | Not stated in the record |

Route: oral only. EML inclusion status is not available in the supplied data.

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records. This does not confirm the absence of interactions.
- **Signals from literature**:
  - Pheniramine-specific hypersensitivity and a case of loss of consciousness after IV pheniramine with hydrocortisone.
  - Anaphylaxis reported with chlorpheniramine, a related agent.
  - Sedation is the most frequent side effect of H1 antihistamines, as shown in the surveillance study.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case for H1 blockade in allergic urticaria is sound, but the evidence is class-level only (L4), with no pheniramine-specific efficacy data. Pheniramine safety signals are present, and the safety screening cannot proceed without the PI.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indication), which is a blocking gap
- Mechanism of action data from DrugBank
- Pheniramine-specific clinical evidence in urticaria, or a justified bridge from chlorpheniramine or dexchlorpheniramine data
- Confirmation that the registered oral effervescent product suits the intended use (route compatibility is still pending)

**Other predictions (both Hold):**
- *Nasal cavity disease* (score 99.28%) has only preclinical animal literature. The term should be narrowed, for example to allergic rhinitis.
- *Acute laryngopharyngitis* (score 99.25%) is model-derived only, with no trials or literature. It is mostly infectious, and antihistamines have no established role.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

