---
layout: default
title: Morphine
parent: Model Prediction Only (L5)
nav_order: 332
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
monitor_inn: "Morphine"
predicted_indications: ["myofascial pain syndrome", "manic bipolar affective disorder", "Tourette syndrome", "restless legs syndrome", "attention deficit hyperactivity disorder, inattentive type", "migraine disorder", "trichotillomania", "methemoglobinemia", "migraine with brainstem aura", "specific developmental disorder"]
description: "Morphine: predicted new indication Myofascial pain syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Morphine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Morphine: Myofascial pain syndrome
{: .text-alpha }

## One-Sentence Summary

Morphine is an opioid analgesic that acts as a mu-opioid receptor agonist. The TxGNN model predicts it may be useful for **myofascial pain syndrome (myofascial pain syndrome)**, but no clinical trials are registered and no publication directly tests morphine in this condition, so the evidence level is **L5** (model prediction only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Myofascial pain syndrome |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 25 of 32) |
| Number of SAHPRA Registrations | 32 (valid: 25) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on general pharmacology, morphine is a mu-opioid receptor agonist that provides analgesia through central and peripheral pain modulation. This makes a role in muscle-related pain plausible in principle.

However, the retrieved literature concerns opioid use in related pain conditions (temporomandibular dysfunction, failed back surgery pain, myofascial pelvic pain) or peri-procedural analgesia. None tests morphine as a treatment for myofascial pain syndrome. Long-term opioid use for chronic musculoskeletal pain also carries risks of tolerance, opioid-induced hyperalgesia and dependence. The mechanistic link is therefore plausible but unproven.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the publications below tests morphine as a treatment for myofascial pain syndrome itself.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41664327](https://pubmed.ncbi.nlm.nih.gov/41664327/) | 2026 | RCT | Asian Spine Journal | Double-blind randomized trial of dexmedetomidine plus morphine versus plain ropivacaine for myofascial infiltration in spinal fusion surgery (postoperative pain setting, not myofascial pain syndrome) |
| [39793344](https://pubmed.ncbi.nlm.nih.gov/39793344/) | 2025 | RCT | Eur J Obstet Gynecol Reprod Biol | Pudendal nerve block for perioperative pain after OnabotulinumtoxinA injection for myofascial pelvic pain (does not test morphine) |
| [17870625](https://pubmed.ncbi.nlm.nih.gov/17870625/) | 2008 | RCT | Eur J Pain | Epidural analgesia (bupivacaine and morphine) versus intercostal cryoanalgesia for post-thoracotomy pain |
| [35066974](https://pubmed.ncbi.nlm.nih.gov/35066974/) | 2022 | Cohort | Pain Pract | Structured stretching programme for myofascial pain and opioid usage in "legacy pain" patients |
| [21691691](https://pubmed.ncbi.nlm.nih.gov/21691691/) | 2011 | Cohort | Rev Assoc Med Bras | Descriptive study of therapeutic approaches in 56 patients with failed back surgery pain syndrome |
| [21419546](https://pubmed.ncbi.nlm.nih.gov/21419546/) | 2011 | Review | J Oral Maxillofac Surg | Long-term opioid use in temporomandibular joint dysfunction can be neither supported nor refuted by current evidence |
| [16713811](https://pubmed.ncbi.nlm.nih.gov/16713811/) | 2006 | Review | J Oral Maxillofac Surg | TMJ arthrocentesis followed by intra-articular morphine infusion for refractory joint pain |
| [16967674](https://pubmed.ncbi.nlm.nih.gov/16967674/) | 2006 | Review | J Calif Dent Assoc | Medications, infusions and injections in the differential diagnosis of orofacial pain |

## South Africa Market Information

Morphine-containing products are marketed in South Africa. No approved-indication text is recorded for them.

<!-- review:begin za-lic-20261105-morphine-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Morphine-containing products are marketed in South Africa, and all three registrations in the data compiled for this report are valid single-ingredient records. No approved-indication text is recorded for them." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 32 registrations for this drug, 25 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-morphine-1 -->

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| B0769 | Cyclimorph 1ml | injection | Valid |
| B0770 | Cyclimorph 1ml | injection | Valid |
| R/2.9/294 | Mst continus | Srt | Valid |
| R/2.9/295 | Mst continus | Srt | Valid |
| S/2.9/278 | Mst continus | Srt | Valid |

Showing 5 of 32 registrations (valid registrations first).

<!-- licenses:end -->

## Safety Considerations

**Drug Interactions** (100 interactions recorded; examples of the main ones):
- **Major:** fentanyl, dihydrocodeine, codeine, tramadol, butalbital, dichloralphenazone, ethanol, alprazolam (additive central nervous system and respiratory depression)
- **Moderate:** chlorpheniramine, acebutolol, nifedipine, hydrochlorothiazide, cetirizine, metformin, among others

Please also refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but no registered trial and no publication directly tests morphine in myofascial pain syndrome, so the evidence level is L5. The risks of long-term opioid use (tolerance, hyperalgesia, dependence) further argue against moving forward without direct evidence.

**To proceed, the following is needed:**
- Controlled studies of morphine in patients with myofascial pain syndrome
- Detailed mechanism of action data
- SAHPRA Professional Information warnings and contraindications for a formal safety review
- A risk-benefit assessment against established non-opioid options for chronic musculoskeletal pain

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "and all three registrations in the data compiled for this report are valid single-ingredient records" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

