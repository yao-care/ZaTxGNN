---
layout: default
title: Clavulanic Acid
parent: Model Prediction Only (L5)
nav_order: 130
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Clavulanic Acid: predicted new indication Ureaplasma urethritis (evidence level L5). Approved use: Urinary tract infection, bacterial pneumonia…"
monitor_inn: "Clavulanic acid"
predicted_indications: ["Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "urogenital tuberculosis", "celiac trunk compression syndrome", "abdominal cystic lymphangioma", "abdominal ectopic pregnancy", "lymph node palisaded myofibroblastoma", "disease of uterine broad ligament"]
---

# Clavulanic Acid
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

## Clavulanic Acid: From Bacterial Infections to Ureaplasma urethritis
{: .text-alpha }

## One-Sentence Summary

Clavulanic acid is a beta-lactamase inhibitor, used with amoxicillin to treat bacterial infections such as urinary tract infection, pneumonia, and staphylococcal and *Escherichia coli* infections.
The TxGNN model's top-ranked prediction is **Ureaplasma urethritis**, but this prediction is not biologically credible. The best-supported direction is **gonococcal urethritis**, which has **9 publications** (mostly 1980s clinical studies) and **no registered clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, bacterial pneumonia, staphylococcal infection, *E. coli* infection, Klebsiella pneumonia (no approved indication text is available from the SAHPRA records) |
| Predicted New Indication | Ureaplasma urethritis (rank 1, model score only); gonococcal urethritis (rank 2) is the best-supported alternative |
| TxGNN Prediction Score | 0.9993 (Ureaplasma urethritis); 0.9993 (gonococcal urethritis) |
| Evidence Level | L5 or L4 for Ureaplasma urethritis (no direct evidence); L3 for gonococcal urethritis |
| South Africa Market Status | Marketed (valid licences: 14 of 14) |
| Number of SAHPRA Registrations | 14 (valid: 14) |
| Recommended Decision | Hold (Ureaplasma urethritis); gonococcal urethritis is a research question only |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, clavulanic acid is a beta-lactamase inhibitor given in combination with amoxicillin. Its efficacy against beta-lactamase-producing bacteria is established, and mechanistically it may be applicable to some urogenital infections.

**Ureaplasma urethritis (top prediction):** The prediction is unlikely to hold. *Ureaplasma* has no cell wall, so it is intrinsically resistant to beta-lactams, and clavulanic acid has no activity against it. The high score probably reflects the model's network proximity to other urethritis indications rather than a real mechanistic link. The retrieved literature covers general urethritis diagnosis and empirical treatment and contains no direct evidence for amoxicillin-clavulanate against *Ureaplasma*.

**Gonococcal urethritis (best-supported alternative):** Here the rationale is sound. Clavulanate inhibits the penicillinase of *Neisseria gonorrhoeae*, restoring amoxicillin activity. Several 1980s studies report good cure rates. However, these studies are old, small, and mostly non-randomized, and they predate current resistance patterns. Current guidelines favour ceftriaxone-based regimens, so the practical value is limited to historical or resistance-specific contexts.

The remaining predictions (ranks 3 to 10) are weak. Uterine inflammatory disease has only indirect evidence. Urogenital tuberculosis has a loose in vitro rationale (clavulanate inhibits the mycobacterial beta-lactamase BlaC) but no supporting clinical evidence. The others (for example, celiac trunk compression syndrome, abdominal ectopic pregnancy, and abdominal cystic lymphangioma) appear to be network artifacts with no plausible mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Gonococcal urethritis (rank 2), the best-supported indication:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6365235](https://pubmed.ncbi.nlm.nih.gov/6365235/) | 1984 | Comparative clinical study | Br J Vener Dis | 121 men: single-dose amoxicillin 3 g + clavulanate 250 mg vs IM procaine penicillin; 9.4% still culture-positive at 7 days vs 26.3% |
| [6428699](https://pubmed.ncbi.nlm.nih.gov/6428699/) | 1984 | Clinical study (two-dose) | Br J Vener Dis | 192 men: Augmentin two-dose cure rate 95.9% vs 87.4% for kanamycin; also effective against PPNG |
| [3533755](https://pubmed.ncbi.nlm.nih.gov/3533755/) | 1986 | Randomised comparative study | Genitourin Med | 500 patients: amoxicillin-clavulanate vs cefuroxime axetil, both with probenecid, for uncomplicated gonorrhoea |
| [4007860](https://pubmed.ncbi.nlm.nih.gov/4007860/) | 1985 | Clinical study (dose comparison) | Genitourin Med | Amoxicillin 3 g + clavulanate 125 mg + probenecid cured 97 of 100 patients; 11 of 13 PPNG infections cured |
| [3004176](https://pubmed.ncbi.nlm.nih.gov/3004176/) | 1985 | Clinical study | Afr J Med Med Sci | Single-dose Augmentin in Ibadan, Nigeria, where about 80% of strains are PPNG |
| [6757686](https://pubmed.ncbi.nlm.nih.gov/6757686/) | 1982 | Clinical study | Med J Malaysia | Single-dose oral amoxicillin-clavulanate in males with gonococcal urethritis |
| [3147528](https://pubmed.ncbi.nlm.nih.gov/3147528/) | 1988 | Clinical study / Review | Sex Transm Dis | Therapy options for antibiotic-resistant gonorrhoea, including clavulanate-potentiated penicillin or amoxicillin |

Ureaplasma urethritis (rank 1): the literature is general and indirect.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21947096](https://pubmed.ncbi.nlm.nih.gov/21947096/) | 2011 | Review | Rev Esp Quimioter | Best empirical treatment of urethritis in Madrid |
| [19544099](https://pubmed.ncbi.nlm.nih.gov/19544099/) | 2009 | Review | Rev Esp Quimioter | Prevalence of microorganisms causing urethritis in men |
| [34366085](https://pubmed.ncbi.nlm.nih.gov/34366085/) | 2021 | Case report | Infect Dis Now | *Pasteurella bettyae* urethritis and balanitis |

---

## South Africa Market Information

Clavulanic acid is registered in South Africa in 14 valid single-ingredient licences. No approved indication text and no Essential Medicines List (EML) status are available in the data compiled for this report. The five main registrations are:

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 50/20.1.2/0659 | Co-Amoxiclaz S Unimed | Suspension | Not available |
| 41/20.1.2/0977 | Gulf amoxy co powder for injection vial | Injection | Not available |
| 37/20.1.2/0674 | Augmaxcil vial 20ml | Injection | Not available |
| 43/20.1.2/0586 | Apoclav 1,2 G | Injection | Not available |
| 41/20.1.2/0535 | Auro-amoxiclav | Tablet | Not available |

Available dosage forms include suspension, injection and tablet.

Note: several other licences in the source records (for example Ventolin inhaler, Trandate, Kivexa, Trizivar, Stiemycin lotion, and Simayla Lisinopril) do not appear to be amoxicillin-clavulanate products. These entries should be verified against SAHPRA records.

---

## Safety Considerations

**Contraindications from the knowledge graph (not label text):** The knowledge graph links clavulanic acid to the following conditions: kidney disease, pyoureter, liver disease, gallbladder disease, cholestasis (including benign recurrent and familial intrahepatic cholestasis), *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, infectious mononucleosis, and chronic Epstein-Barr virus infection syndrome.

**Drug interactions:** 16 interactions were found.
- **Major:** leflunomide and teriflunomide.
- **Moderate:** methotrexate, naltrexone, balsalazide, asparaginase *E. coli*, pegaspargase, brentuximab vedotin, clofarabine, epirubicin, idelalisib, interferon beta-1a, interferon beta-1b, peginterferon beta-1a, tioguanine, and trabectedin.

Label-based warnings and contraindications could not be retrieved. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction, Ureaplasma urethritis, is mechanistically implausible because *Ureaplasma* lacks a cell wall and is intrinsically beta-lactam resistant. The remaining predictions have no clinical evidence or only indirect evidence.
- Gonococcal urethritis has plausible and directly clinical, but old, evidence. Current guidelines favour ceftriaxone-based regimens, so it is best treated as a research question (for example, resistance-specific contexts) rather than a repurposing candidate.

**To proceed, the following is needed:**
- The SAHPRA package insert warnings and contraindications (a blocking data gap for safety screening).
- Mechanism of action data from DrugBank.
- Current local gonococcal susceptibility data for South Africa, to determine whether amoxicillin-clavulanate has any role.
- Verification of the SAHPRA licence list, since several entries appear to be unrelated products.
- For any further pursuit, a critical appraisal of the 1980s gonococcal studies against current resistance patterns.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

