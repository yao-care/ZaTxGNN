---
layout: default
title: Procaine
parent: Moderate Evidence (L3-L4)
nav_order: 386
evidence_level: L4
indication_count: 10
---

# Procaine
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

# Procaine: From Local Anaesthesia to Methemoglobinemia (Prediction Not Supported, Safety Signal)

## One-Sentence Summary

Procaine is an ester-type local anaesthetic. The SAHPRA record for the registration linked to it does not state an indication.
The TxGNN model predicts it may be effective for **methemoglobinemia**, but the literature shows procaine as a **cause** of methemoglobinemia, not a treatment.
There are **0 clinical trials** and **8 publications** (mostly case reports and reviews), so this prediction is most likely an adverse-event association in the knowledge graph.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA record (procaine is generally used as a local anaesthetic) |
| Predicted New Indication | Methemoglobinemia |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Procaine is a local anaesthetic that blocks nerve conduction, and its use in pain and anaesthesia is long established.

The prediction is **not** mechanistically reasonable as a therapy. The retrieved literature describes procaine, and related local anaesthetics such as lignocaine, as **inducing** methemoglobin formation. Reports include intravenous procaine in adults, a newborn after subcutaneous infiltration, and a 1987 clinical observation on methemoglobin levels during intravenous procaine anaesthesia. The high TxGNN score most likely reflects a drug-disease link in the knowledge graph that is adverse rather than therapeutic.

The same reasoning applies to the related predictions "methemoglobinemia, alpha type" and "methemoglobin reductase deficiency". These have no clinical evidence, and use in such patients would be a safety concern rather than a benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR or PACTR).

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5529388](https://pubmed.ncbi.nlm.nih.gov/5529388/) | 1970 | Case report (adverse event) | Acta Physiol Lat Am | Methemoglobinemia caused by intravenous procaine |
| [3691245](https://pubmed.ncbi.nlm.nih.gov/3691245/) | 1987 | Clinical observation | Zhonghua Wai Ke Za Zhi | Effect of intravenous procaine anaesthesia on methemoglobin levels |
| [705003](https://pubmed.ncbi.nlm.nih.gov/705003/) | 1978 | Case report (neonatal) | Rev Esp Anestesiol Reanim | Methemoglobinemia in a newborn after subcutaneous novocaine (procaine) infiltration |
| [14246695](https://pubmed.ncbi.nlm.nih.gov/14246695/) | 1965 | Case report (lignocaine) | Lancet | Methemoglobinaemia following lignocaine, a related local anaesthetic |
| [6705717](https://pubmed.ncbi.nlm.nih.gov/6705717/) | 1984 | Review | Drugs | Rational use of local anaesthetics (general background) |
| [5118947](https://pubmed.ncbi.nlm.nih.gov/5118947/) | 1971 | Review | Laval Med | General review of local anaesthetics |
| [5644303](https://pubmed.ncbi.nlm.nih.gov/5644303/) | 1968 | Pharmacokinetic study | Am J Obstet Gynecol | Placental transfer of procaine (off-topic) |
| [6745527](https://pubmed.ncbi.nlm.nih.gov/6745527/) | 1984 | Review | Fundam Appl Toxicol | Organophosphate toxicological interactions (off-topic) |

None of these publications shows a therapeutic benefit of procaine in methemoglobinemia.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 34/20.1.1/0044 | Aspen Ceftriaxone 1G Injection | Injection | Not stated in the record |

The linked product is a ceftriaxone injection, and no procaine-specific product with a stated indication was identified. The link between this registration and procaine (for example, use as a diluent or a mapping error) should be verified against the SAHPRA record. Essential Medicines List status could not be confirmed from the available data.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Beyond the PI, the retrieved literature flags **drug-induced methemoglobinemia** as a documented risk with procaine and related local anaesthetics, including in neonates. Caution is warranted in patients with haemoglobin abnormalities or methemoglobin reductase deficiency.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, methemoglobinemia, is contradicted by the literature, which describes procaine as a cause. There are no trials, and the evidence is limited to case reports from 1965-1987 and general reviews. Repurposing for this indication is not supported and carries a safety signal.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings and contraindications), and confirmation of which registered product actually contains procaine
- Mechanism of action data from DrugBank
- For the lower-ranked musculoskeletal predictions, fibromyalgia and tendinitis (both flagged "Research Question", L4): a scoped literature review of local anaesthetic injection in myofascial pain, plus full-text review of the 2022 neural therapy study in supraspinatus tendinopathy (PMID 35480510) to confirm design, agent and outcomes

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

