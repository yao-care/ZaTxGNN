---
layout: default
title: Carbocisteine
parent: Model Prediction Only (L5)
nav_order: 101
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Carbocisteine: predicted new indication Gout (evidence level L5). Approved use: Not available"
monitor_inn: "Carbocisteine"
predicted_indications: ["gout", "appendicitis", "congestive heart failure", "acute pulmonary heart disease", "epiglottitis", "peritonitis", "laryngitis", "Lesch-Nyhan syndrome", "gastrointestinal allergy"]
---

# Carbocisteine
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

# Carbocisteine: From Mucolytic Use to Gout (Top TxGNN Prediction) and Bronchitis (Best-Supported Prediction)

## One-Sentence Summary

Carbocisteine is a mucoregulatory (mucolytic) drug marketed in South Africa as a syrup. The top-ranked TxGNN prediction is **gout** (score 99.67%), but it has **no clinical trials and no publications** and no plausible mechanism, so it is most likely a knowledge-graph artefact. The best-supported prediction is **bronchitis** (score 98.77%), backed by **8 publications** (one double-blind RCT, one systematic review/meta-analysis, plus laboratory and animal studies) and **no registered trials**. This is closer to an established use than a new repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the SAHPRA registration data compiled for this report contain no approved indication text) |
| Predicted New Indication | Gout (rank 1 by TxGNN score); Bronchitis (best evidence, rank 2) |
| TxGNN Prediction Score | Gout 99.67%; Bronchitis 98.77% |
| Evidence Level | Gout: L5; Bronchitis: L3 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Gout: Hold; Bronchitis: Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on the published literature, carbocisteine is a mucolytic and mucoregulator. It is reported to restore the balance of sialomucins and fucomucins, improve mucociliary transport, and scavenge reactive oxygen species.

**Bronchitis (rank 2).** The mechanistic link is reasonable.
- In a rat model of SO2-induced bronchitis, carbocisteine improved the mucociliary transport rate (PMID 8500784).
- In vitro, carbocisteine scavenged reactive oxygen species (PMID 19144049).
- Clinical support comes from a 1985 long-term double-blind placebo-controlled trial in chronic bronchitis (PMID 3907681) and a 2024 systematic review and meta-analysis of mucolytics in stable COPD (PMID 39413571).
- Carbocisteine is already used for this purpose in many markets, so this is not a novel repurposing.

**Gout (rank 1) and other low-evidence predictions.** No identifiable mechanistic link exists. Carbocisteine has no known effect on urate metabolism or gout inflammation. Likewise, Lesch-Nyhan syndrome (HPRT deficiency, purine metabolism) is probably scored highly because of its graph association with gout and uric acid. Appendicitis, congestive heart failure, acute pulmonary heart disease, epiglottitis, and gastrointestinal allergy have no supporting evidence or plausible mechanism.

**Indirect or exploratory signals.**
- *Peritonitis:* a mouse study showed reduced virus-induced pulmonary inflammation under cigarette smoke exposure (PMID 24303786). It concerns the lung, not the peritoneum.
- *Laryngitis:* a study of carbocisteine plus clarithromycin in chronic upper-airway disease (PMID 21636230) is indirect and confounded by the combination design. This is classed as a research question only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the ten predicted indications.

---

## Literature Evidence

Publications for the best-supported prediction, **bronchitis**:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3907681](https://pubmed.ncbi.nlm.nih.gov/3907681/) | 1985 | RCT (double-blind, placebo-controlled) | Br J Clin Pract | Long-term oral carbocisteine in chronic bronchitis (no abstract available) |
| [39413571](https://pubmed.ncbi.nlm.nih.gov/39413571/) | 2024 | Systematic review/meta-analysis | Respir Investig | Efficacy and safety of mucolytics in stable COPD, including chronic bronchitis |
| [18832259](https://pubmed.ncbi.nlm.nih.gov/18832259/) | 2008 | Review/commentary | Drug Ther Bull | Erdosteine for COPD exacerbations; compares its licensed use with carbocisteine and mecysteine (related drug) |
| [23291681](https://pubmed.ncbi.nlm.nih.gov/23291681/) | 2013 | Case report | Intern Med | Carbocisteine-induced pneumonia in a patient with CATCH22 syndrome (adverse event) |
| [19144049](https://pubmed.ncbi.nlm.nih.gov/19144049/) | 2009 | In vitro | Respirology | Carbocisteine scavenges reactive oxygen species |
| [3518737](https://pubmed.ncbi.nlm.nih.gov/3518737/) | 1986 | In vitro/biochemical | Biol Chem Hoppe-Seyler | Effects of reducing agents on proteolytic enzymes and alpha 1-proteinase inhibitor oxidation; carbocisteine lacks reducing properties |
| [8500784](https://pubmed.ncbi.nlm.nih.gov/8500784/) | 1993 | Animal study | Fundam Clin Pharmacol | Improved mucociliary transport in rats with SO2-induced bronchitis |
| [1487227](https://pubmed.ncbi.nlm.nih.gov/1487227/) | 1992 | Animal study | Fundam Clin Pharmacol | Oral carbocisteine and ventilatory parameters in SO2-induced rat bronchitis |

Other indications (limited, indirect, or not relevant):

| PMID | Year | Indication | Type | Journal | Key Findings |
|------|-----|------|------|---------|---------|
| [21636230](https://pubmed.ncbi.nlm.nih.gov/21636230/) | 2012 | Laryngitis | Clinical study (design unverified) | Auris Nasus Larynx | Carbocisteine plus clarithromycin vs clarithromycin alone in chronic rhinosinusitis; indirect |
| [24303786](https://pubmed.ncbi.nlm.nih.gov/24303786/) | 2014 | Peritonitis | Animal study | Am J Respir Cell Mol Biol | Reduced virus-induced pulmonary inflammation in smoke-exposed mice; indirect |
| [42557060](https://pubmed.ncbi.nlm.nih.gov/42557060/) | 2026 | Congestive heart failure | Post hoc analysis | Thorax | Drug response assessments for inhaled hypertonic saline in bronchiectasis (CLEAR trial); not relevant, likely a retrieval false positive |

No publications were found for gout, appendicitis, acute pulmonary heart disease, epiglottitis, Lesch-Nyhan syndrome, or gastrointestinal allergy.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M/10.1/248 | Flemex | Syrup | Not available in the data compiled for this report |

One valid single-ingredient registration; no combination products and no cancelled registrations. Essential Medicines List (EML) status could not be confirmed from the data compiled for this report.

---

## Safety Considerations

- **Knowledge-graph contraindication signal:** active peptic ulcer disease (from drug-disease contraindication edges in the TxGNN knowledge graph, not from label text).
- **Literature signal:** a case report of carbocisteine-induced pneumonia (PMID 23291681). Gastrointestinal adverse effects are a usual caution with this drug.
- **Drug interactions:** no interactions were found in the queried data.

SAHPRA package insert warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (bronchitis); Hold (gout and all other predictions)**

**Rationale:**
- Bronchitis is supported by a long-term double-blind RCT, a recent meta-analysis of mucolytics in COPD, and consistent mechanistic data. Evidence is capped at L3 because the trial is old, the meta-analysis covers mucolytics as a class, and no registered trials were provided.
- Gout, appendicitis, heart failure, acute pulmonary heart disease, epiglottitis, Lesch-Nyhan syndrome, and gastrointestinal allergy have no supporting evidence or plausible mechanism and should be treated as computational artefacts. Peritonitis has only indirect animal data (L4, Hold). Laryngitis is a research question only.

**To proceed, the following is needed:**
- Download and review the SAHPRA package insert to confirm the approved indication, warnings, and contraindications. This is a blocking gap for safety screening.
- Confirm the original and approved indication of Flemex, which is blank in the data compiled for this report, and the regional label status for bronchitis/COPD.
- Obtain the mechanism of action from DrugBank.
- Review the full text of the 1985 RCT (PMID 3907681) and the 2024 meta-analysis (PMID 39413571) to confirm carbocisteine-specific results.
- Apply caution in patients with active peptic ulcer disease, and keep the reported pneumonia case in mind.
- Verify the design of PMID 21636230 before any further assessment of upper-airway indications.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

