---
layout: default
title: Ceftriaxone
parent: Model Prediction Only (L5)
nav_order: 106
evidence_level: L5
indication_count: 10
---

# Ceftriaxone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Ceftriaxone: From Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Ceftriaxone is a third-generation cephalosporin antibiotic, originally used for bacterial infections such as pneumonia, meningitis, gonorrhoea and salmonellosis.
The TxGNN model's top-ranked prediction is **hyperamylasemia** (99.39%), but this has no supporting evidence and no plausible mechanism.
The best-supported prediction is **infectious otitis media**, with **1 registered trial (which does not test ceftriaxone)** and **18 publications**. This is largely an on-spectrum use of the antibiotic rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (e.g. pneumonia, bacterial meningitis, gonorrhoea, salmonellosis). SAHPRA indication text is not available in the data compiled for this report. |
| Predicted New Indication | Hyperamylasemia (top-ranked by TxGNN; see note below) |
| TxGNN Prediction Score | 99.39% |
| Evidence Level | L5 for the top-ranked prediction (L3 for infectious otitis media, the best-supported candidate) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 6 |
| Recommended Decision | Hold (top-ranked prediction); Proceed with Guardrails is not yet justified for any candidate |

**Note:** Several predictions score above 99%, but the score does not reflect evidence quality. The ten predictions below are summarised by evidence strength.

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 1 | Hyperamylasemia | 99.39% | L5 | Hold. The literature suggests an adverse-effect direction, not benefit |
| 2 | Polyclonal hyperviscosity syndrome | 99.39% | L5 | Hold. No rationale or evidence |
| 3 | Congenital analbuminemia | 99.37% | L5 | Hold. No rationale or evidence |
| 4 | Infectious otitis media | 99.26% | L3 | Research question. Biologically plausible |
| 5 | Blood group incompatibility | 99.12% | L5 | Hold. No mechanistic link |
| 6 | Suppurative otitis media | 99.02% | L3 | Research question |
| 7 | Chronic otitis media | 99.01% | L4 | Hold. Limited activity against the dominant pathogens |
| 8 | Premalignant haematological system disease | 98.99% | L5 | Hold. Likely a graph-based artefact |
| 9 | Middle ear disease | 98.99% | L4 | Research question. Overlaps with otitis media |
| 10 | Otosalpingitis | 98.95% | L5 | Hold. Model prediction only |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Ceftriaxone is a beta-lactam antibiotic with proven efficacy in a wide range of bacterial infections, and its antibacterial activity is the basis for assessing any new indication.

**Top-ranked prediction (hyperamylasemia):** There is no plausible mechanism by which ceftriaxone would lower amylase. Ceftriaxone is known to cause biliary sludge and pseudolithiasis, which can occasionally be associated with pancreatitis and raised amylase. The direction of association is therefore more likely an adverse effect than a therapeutic benefit. The high TxGNN score is not supported by biological rationale.

**Otitis-media group (ranks 4, 6, 7, 9, 10):** Acute otitis media is caused mainly by *Streptococcus pneumoniae*, *Haemophilus influenzae* and *Moraxella catarrhalis*, all within ceftriaxone's spectrum. Single-dose intramuscular ceftriaxone is already used clinically for acute otitis media. The picture is weaker in chronic disease, which is dominated by *Pseudomonas aeruginosa*, *Staphylococcus aureus* and biofilm-forming organisms, against which ceftriaxone has limited activity (topical therapy is generally preferred).

**Ranks 2, 3, 5 and 8** (hyperviscosity, analbuminemia, blood group incompatibility, premalignant haematological disease) have no mechanistic rationale. They are most likely knowledge-graph artefacts.

---

## Clinical Trial Evidence

Only one registered trial was identified, for infectious otitis media (rank 4). It does not test ceftriaxone and provides disease-context information only.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02567825](https://clinicaltrials.gov/study/NCT02567825) | N/A | Completed | 250 | Tympanostomy tubes vs non-surgical management in children with recurrent acute otitis media; no ceftriaxone arm |

No trials were registered for the other predicted indications.

---

## Literature Evidence

Selected publications for **infectious otitis media** (rank 4) and **suppurative otitis media** (rank 6). The top-ranked prediction, hyperamylasemia, has no publications that support a therapeutic effect.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8989332](https://pubmed.ncbi.nlm.nih.gov/8989332/) | 1997 | RCT | Pediatrics | Single IM dose of ceftriaxone compared with 10 days of oral trimethoprim-sulfamethoxazole in acute otitis media |
| [11099083](https://pubmed.ncbi.nlm.nih.gov/11099083/) | 2000 | Clinical study | Pediatr Infect Dis J | One-day vs three-day IM ceftriaxone in nonresponsive acute otitis media |
| [9877360](https://pubmed.ncbi.nlm.nih.gov/9877360/) | 1998 | Clinical study | Pediatr Infect Dis J | Bacteriological efficacy of a three-day IM ceftriaxone regimen in nonresponsive acute otitis media |
| [2523493](https://pubmed.ncbi.nlm.nih.gov/2523493/) | 1989 | Clinical study | Jpn J Antibiot | Ceftriaxone 1 g once daily vs cefotiam in acute suppurative otitis media and acute exacerbation of chronic disease; efficacy 71% vs 86% |
| [12166789](https://pubmed.ncbi.nlm.nih.gov/12166789/) | 2002 | Consensus | Clin Pediatr | Consensus recommendations for treating acute otitis media |
| [10688388](https://pubmed.ncbi.nlm.nih.gov/10688388/) | 2000 | Review | Clin Ther | Review of treatment recommendations for acute otitis media |
| [35841649](https://pubmed.ncbi.nlm.nih.gov/35841649/) | 2022 | Cohort | Int J Pediatr Otorhinolaryngol | Patterns of ceftriaxone use for acute otitis media in US primary care; possible marker of antimicrobial resistance |
| [20660544](https://pubmed.ncbi.nlm.nih.gov/20660544/) | 2010 | Review | Pediatrics | Prevention and treatment of otitis media and meningitis in children with cochlear implants |
| [7522351](https://pubmed.ncbi.nlm.nih.gov/7522351/) | 1994 | Cohort | South Med J | Hyperamylasemia of pancreatic origin in intracranial bleeding (not ceftriaxone-specific) |
| [10458061](https://pubmed.ncbi.nlm.nih.gov/10458061/) | 1999 | Clinical study | Bratisl Lek Listy | Prophylactic ceftriaxone after endoscopic papillosphincterotomy; likely infection prevention, not hyperamylasemia treatment |

Much of the retrieved literature is microbiology surveys and general reviews, and some items are unrelated to the predicted indication. The only clinical studies of ceftriaxone in otitis media are dated (1989 to 2000).

---

## South Africa Market Information

Ceftriaxone is marketed in South Africa, with 6 valid single-ingredient injectable registrations and no cancelled registrations. Approved indication text and manufacturer details are not available in the data compiled for this report. Essential Medicines List (EML) status could not be confirmed from the data.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 47/20.1.1/1245 | Obkef 1G Injection | Injection | Not available |
| Reg. No. 48/20.1.1/0228 | Ceftriaxone 1G Fksa | Injection | Not available |
| Reg. No. 37/20.1.1/0042 | Adco Ceftriaxone powder for injection | Injection | Not available |
| Reg. No. 37/20.1.1/0368 | Rociject powder for injection | Injection | Not available |
| Reg. No. R/20.1.1/47 | Rocephin | Injection | Not available |

A sixth registration (Reg. No. 34/20.1.1/0044, Aspen Ceftriaxone 1G Injection) is also valid.

All registered forms are injectable only.

---

## Safety Considerations

**Contraindications and disease-level cautions (from the knowledge graph, not label text):** Ceftriaxone is linked to the following conditions, which should be considered in patient selection:
- Liver disease
- Gallbladder disease
- Neonatal jaundice
- *Clostridium difficile* colitis
- Perinatal necrotizing enterocolitis
- Haemolytic anaemia

**Drug Interactions (100 interactions recorded; main ones listed):**
- **Major:** Calcium chloride, calcium glucoheptonate, calcium gluconate. Intravenous calcium-containing products are a recognised concern with ceftriaxone, so check the SAHPRA Professional Information (PI) for administration restrictions.
- **Moderate:** Kanamycin, neomycin, streptomycin (aminoglycosides) and picosulfuric acid.
- Other recorded interactions have unclassified severity (e.g. amphotericin B, epinephrine, amoxicillin, doxycycline, pantoprazole).

**Other considerations:** Ceftriaxone is associated with biliary sludge and pseudolithiasis. Because it is highly protein-bound, altered albumin levels could change its pharmacokinetics.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications, as label-derived safety data were not available for this report. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (hyperamylasemia) rests on model score alone (L5), with no trials and no plausible mechanism. The literature points toward an adverse effect rather than a benefit.
- The otitis-media predictions (ranks 4, 6, 9) are plausible and partly supported by older clinical studies (L3 to L4). However, they are largely on-spectrum uses of an antibiotic already in clinical use, not true repurposing, and no recent Phase 3 RCT was identified. Chronic otitis media is weakly supported because of ceftriaxone's limited activity against the dominant pathogens.

**To proceed, the following is needed:**
- Review of the SAHPRA-approved PI to confirm approved indications, warnings and contraindications (label-derived safety data are currently missing, which blocks safety screening)
- Mechanism of action data (currently unavailable)
- For infectious otitis media: confirmation of whether it is already covered by the current SAHPRA-approved indications, and comparison with local guidelines and resistance data
- For any new indication: a recent controlled trial with ceftriaxone as the tested intervention
- For the top-ranked hyperamylasemia prediction: no further development is recommended unless new mechanistic evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

