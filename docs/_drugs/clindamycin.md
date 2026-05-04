---
layout: default
title: Clindamycin
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 10
---

# Clindamycin
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

# Clindamycin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Clindamycin is a lincosamide antibiotic with well-established use in treating bacterial infections including skin and soft tissue infections, anaerobic infections, pelvic inflammatory disease, and ocular toxoplasmosis.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis** (rank 1, score 99.97%); however, the mechanistic rationale is biologically weak, and **no supporting clinical trials or published literature** were identified for this specific indication.
Across all 10 predicted indications, the evidence remains at Level L4–L5, and a **Hold** decision is recommended pending further mechanistic and clinical validation.

---

## Quick Overview

| Item | Content |
|---|---|
| Original Indication | Not documented in South African regulatory data (no SAHPRA registrations on record) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Clindamycin is a lincosamide antibiotic that inhibits bacterial protein synthesis by binding to the 50S ribosomal subunit, thereby blocking peptide chain elongation. It has demonstrated efficacy against gram-positive cocci (including *Staphylococcus aureus* and *Streptococcus* spp.), anaerobes, and certain protozoa (notably *Toxoplasma gondii*, making it a recognised treatment for ocular toxoplasmosis).

Punctate epithelial keratoconjunctivitis (PEK) is primarily caused by adenoviral infection, dry eye disease, or drug toxicity — none of which is a bacterial process amenable to Clindamycin's antibiotic mechanism. While ocular toxoplasmosis (a known Clindamycin indication) can produce secondary corneal involvement, the pathobiology of PEK is substantially distinct from toxoplasmal chorioretinitis.

The Evidence Pack's mechanistic analysis notes that the high TxGNN score (0.9997) is most likely attributable to **high node-density connections** in the knowledge graph between Clindamycin and ocular network nodes, rather than a genuine therapeutic signal. No clinical trials and no published literature were retrieved to support this repurposing hypothesis. The biological plausibility of Clindamycin as a primary treatment for PEK is not currently supported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the 10 TxGNN-predicted indications.

---

## Literature Evidence (Top Predicted Indication: Punctate Epithelial Keratoconjunctivitis)

Currently no related literature available for this specific indication.

> **Note:** Limited indirect literature was retrieved for lower-ranked predicted indications. See the supplementary overview below for context.

### Supplementary: Literature Retrieved for Secondary Predicted Indications

| PMID | Year | Type | Journal | Indication Searched | Key Findings |
|---|---|---|---|---|---|
| [22880135](https://pubmed.ncbi.nlm.nih.gov/22880135/) | 2012 | Retrospective Case Series | *PLoS One* | Exposure Keratitis | Prevalence and antibiotic susceptibility of MRSA vs MSSA ocular infections; clindamycin susceptibility patterns reported |
| [24244625](https://pubmed.ncbi.nlm.nih.gov/24244625/) | 2013 | Retrospective Hospital Review | *PLoS One* | Exposure Keratitis | Clinical features and antibiotic susceptibility of *S. aureus* keratitis; MRSA vs MSSA comparison |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case Report | *Ophthalmology* | Exposure Keratitis | First reported case of contact lens-related *Bacillus cereus* keratitis; indirect relevance only |
| [33847093](https://pubmed.ncbi.nlm.nih.gov/33847093/) | 2021 | Retrospective Veterinary Study | *Polish J Vet Sci* | Exposure Keratitis | Feline ocular toxoplasmosis treatment outcomes; veterinary data, not directly applicable to humans |
| [36684930](https://pubmed.ncbi.nlm.nih.gov/36684930/) | 2022 | Molecular Epidemiology (Veterinary) | *Front Public Health* | Non-Human Animal Disease | *C. difficile* genetic overlap between companion animals and humans; Clindamycin implicated as a CDI-inducing agent (negative signal) |
| [40172204](https://pubmed.ncbi.nlm.nih.gov/40172204/) | 2025 | Epidemiological Study (Veterinary) | *Appl Environ Microbiol* | Non-Human Animal Disease | *C. difficile* in feral horse populations in Australia; veterinary epidemiology only |
| [21908289](https://pubmed.ncbi.nlm.nih.gov/21908289/) | 2011 | In Vitro MIC Study (Veterinary) | *J Vet Diagn Invest* | Epidemic Keratoconjunctivitis | MIC data for *Moraxella bovoculi* in infectious bovine keratoconjunctivitis; bovine pathogen, not applicable to human adenoviral EKC |
| [25261461](https://pubmed.ncbi.nlm.nih.gov/25261461/) | 2014 | Retrospective Field Epidemiology (Veterinary) | *J Vet Diagn Invest* | Epidemic Keratoconjunctivitis | Retrospective characterisation of *Moraxella* spp. in cattle IBK; veterinary data only |

**Important caveat:** All retrieved literature is indirect, involves veterinary subjects or non-target pathogens, and does not constitute clinical evidence for the predicted human indications. Two papers (PMIDs 36684930, 40172204) contain a **negative safety signal**: Clindamycin is identified as a high-risk inducer of *Clostridioides difficile* infection (CDI), not a therapeutic agent in that context.

---

## South Africa Market Information

Clindamycin is **not currently registered** with SAHPRA per this dataset. No product licences, dosage forms, or approved indications are on record.

> Clinicians requiring Clindamycin for established indications (e.g., bacterial vaginosis, anaerobic infections, toxoplasmosis) should verify current SAHPRA registration status and Section 21 authorisation requirements via the SAHPRA online register.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for complete safety information. In the absence of South African PI data in this Evidence Pack, healthcare professionals should note the following from established pharmacological knowledge:

- **CDI Risk:** Clindamycin carries a well-documented risk of *Clostridioides difficile*-associated diarrhoea and pseudomembranous colitis. This is reflected in the retrieved literature (PMIDs 36684930, 40172204) and is a critical prescribing consideration.
- **Drug Interactions:** No DDI data was returned by the query. Consult current interaction databases before co-prescribing.

Report adverse drug reactions to SAHPRA via the MedSafety reporting system.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Clindamycin in this pack are rated L4–L5 evidence, with no supporting clinical trials registered and only indirect veterinary or non-specific literature retrieved. The top-ranked indication (punctate epithelial keratoconjunctivitis, score 99.97%) has no biological plausibility as a primary treatment target given Clindamycin's antibiotic mechanism of action; the high score is attributable to knowledge graph topology, not therapeutic signal. Additionally, a negative CDI-induction signal was identified in the retrieved literature, warranting caution.

**To proceed, the following is needed:**

- **MOA data:** Confirm full mechanism of action via DrugBank API (data gap DG002) to enable proper mechanistic-link analysis
- **SAHPRA status clarification:** Verify current SAHPRA registration status; if the drug is commercially available in South Africa under a different dataset snapshot, obtain PI document for safety and contraindication data (data gap DG001)
- **Biological plausibility review:** Commission a structured mechanistic review for any ocular indication under consideration, specifically examining whether Clindamycin's known anti-*Toxoplasma* activity provides a credible secondary-infection rationale
- **Hypothesis refinement:** Consider re-running TxGNN with edge-weight normalisation to reduce false-positive signals from high-density KG nodes in the Clindamycin–ophthalmic network
- **Clinical feasibility assessment:** If the ocular toxoplasmosis link is to be explored further, redirect query to chorioretinitis or uveitis (known indications) rather than keratoconjunctivitis subtypes

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All predictions should be interpreted in the context of established clinical guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

