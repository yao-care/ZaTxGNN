---
layout: default
title: Ampicillin
parent: Model Prediction Only (L5)
nav_order: 37
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
monitor_inn: "Ampicillin"
predicted_indications: ["laryngitis", "Ureaplasma urethritis", "chronic rhinosinusitis", "chronic ethmoidal sinusitis", "gingivitis", "paranasal sinus neoplasm (disease)", "bacterial arthritis", "conjunctivitis", "pericoronitis"]
description: "Ampicillin: predicted new indication Laryngitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Ampicillin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Ampicillin: Laryngitis
{: .text-alpha }

## One-Sentence Summary

Ampicillin is a beta-lactam antibiotic that blocks bacterial cell wall synthesis and is marketed in South Africa. The TxGNN model predicts it may be useful for **laryngitis**, but **no clinical trials** are registered and the **20 publications** retrieved do not test ampicillin in laryngitis itself, so the evidence level is **L5**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Laryngitis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 24 of 64; 4 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 64 (valid: 24, of which 4 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, ampicillin is a beta-lactam that inhibits bacterial cell wall synthesis, so it can act against susceptible bacteria.

The reasoning for laryngitis is indirect. Bacterial infections of the larynx and surrounding structures, such as epiglottitis caused by *Haemophilus influenzae* or deep neck abscess, are plausibly susceptible to ampicillin. However, laryngitis itself is mostly viral and self-limiting, so antibiotics would rarely be indicated. Beta-lactamase production in *H. influenzae* also limits ampicillin as monotherapy. The high model score therefore should not be read as proof of benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these publications studies ampicillin in laryngitis. They concern related conditions (acute epiglottitis, laryngeal abscess, neck infections) or other diseases. The most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3977063](https://pubmed.ncbi.nlm.nih.gov/3977063/) | 1985 | Review | Anaesth Intensive Care | Retrospective review of 161 children with acute epiglottitis, with airway management and complications |
| [3026014](https://pubmed.ncbi.nlm.nih.gov/3026014/) | 1986 | Clinical report | Rev Infect Dis | Sulbactam/ampicillin for acute epiglottitis in children, given ampicillin-resistant *H. influenzae* type b |
| [3290661](https://pubmed.ncbi.nlm.nih.gov/3290661/) | 1988 | Case series | Monatsschr Kinderheilkd | Epiglottitis in 27 children; rising ampicillin resistance of *H. influenzae* type b changed treatment |
| [6881564](https://pubmed.ncbi.nlm.nih.gov/6881564/) | 1983 | Case series | Anesth Analg | Duration of intubation and fever in 23 children with epiglottitis treated with ampicillin or chloramphenicol |
| [3322611](https://pubmed.ncbi.nlm.nih.gov/3322611/) | 1987 | Case series | Clin Otolaryngol Allied Sci | Bacteriology and treatment of 19 adult epiglottitis cases |
| [35923122](https://pubmed.ncbi.nlm.nih.gov/35923122/) | 2023 | Case report/Review | Ann Otol Rhinol Laryngol | Spontaneous laryngeal abscess: new case and review of reported cases |
| [25944348](https://pubmed.ncbi.nlm.nih.gov/25944348/) | 2015 | Cohort | Otolaryngol Head Neck Surg | Perioperative antibiotic choice and complications after laryngectomy |
| [7487676](https://pubmed.ncbi.nlm.nih.gov/7487676/) | 1995 | Animal study | Auris Nasus Larynx | Ibuprofen added to ampicillin in experimental otitis media in chinchillas |

---

## South Africa Market Information

No approved indication text is recorded in the local data. Essential Medicines List status is not available in the data compiled for this report.

<!-- review:begin za-lic-20261105-ampicillin-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Seven of the eight SAHPRA registrations are valid and one is cancelled. All are single-ingredient products. No approved indication text is recorded in the local data." Removed: it said the registrations were cancelled, not registered, or not valid, which did not match the SAHPRA registration data as of 2026-11-05. The SAHPRA data list 64 registrations for this drug, 24 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-ampicillin-1 -->

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 30/20.1.2/0247 | Ampicillin 250 injection unimed vial | injection | Valid |
| 30/20.1.2/0248 | Ampicillin 500 injection unimed vial | injection | Valid |
| 41/20.1.2/0122 | Auro ampicillin powder for injection via | injection | Valid |
| H/20.1.2/26 | Ampicillin-fresenius vial | injection | Valid |
| V/20.1.2/115 | Ampipen | capsule | Valid (status not confirmed by SAHPRA) |

Showing 5 of 64 registrations (valid registrations first).

<!-- licenses:end -->

---

## Safety Considerations

Label warnings and contraindications from the SAHPRA Professional Information (PI) are not available in the data compiled for this report. Please refer to the SAHPRA-approved PI for safety information. Report adverse drug reactions to SAHPRA.

**Drug Interactions:** 61 interactions were identified. The main ones with a Moderate level are:
- Doxycycline, minocycline and tetracycline
- Kanamycin
- Balsalazide
- Lansoprazole and dexlansoprazole
- Picosulfuric acid

Clarithromycin is rated Minor.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The evidence level is L5. No study tests ampicillin in laryngitis, and the retrieved papers address epiglottitis, laryngeal abscess and other conditions. Laryngitis is mostly viral, and beta-lactamase-producing organisms limit ampicillin's usefulness, so the high model score is not supported by clinical data.

**To proceed, the following is needed:**
- Clinical studies that directly test ampicillin in bacterial laryngitis, defining the target population
- Mechanism of action data and the SAHPRA Professional Information warnings and contraindications
- A review of local *H. influenzae* resistance patterns and antibiotic stewardship considerations

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "Seven of the eight SAHPRA registrations are valid and one is cancelled. All are single-ingredient products" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

