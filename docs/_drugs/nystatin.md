---
layout: default
title: Nystatin
parent: Moderate Evidence (L3-L4)
nav_order: 351
evidence_level: L4
indication_count: 10
---

# Nystatin
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

# Nystatin: From Cutaneous and Oral Candidiasis to Vulvovaginitis

## One-Sentence Summary

Nystatin is a polyene antifungal originally used to treat candidiasis (cutaneous, oral and vulvovaginal).
The TxGNN model predicts it may be effective for **vulvovaginitis**, but this is largely an extension of an existing indication (candidal vulvovaginitis). The data compiled for this report contain **no clinical trials** and **20 publications**, mostly reviews and guidelines.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cutaneous candidiasis, oral candidiasis, candidiasis, vulvovaginal candidiasis (from the TxGNN knowledge graph; SAHPRA indication text is not available) |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, nystatin binds ergosterol in the Candida cell membrane, forming pores and causing leakage of cell contents. Its efficacy against candidiasis is established.

Vulvovaginal candidiasis is a major cause of vulvovaginitis, so the prediction is largely an on-label extension rather than true repurposing. The effect is expected to be limited to the candidal subtype. Non-candidal vulvovaginitis (bacterial, trichomonal, atrophic) is not expected to respond.

Other high-scoring predictions for nystatin (for example orbital region disease, cystic teratoma, spinal cord dermoid cyst, biotin metabolic disease) have no plausible mechanistic link or supporting evidence and are likely model artefacts. They are not recommended for further evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered for vulvovaginitis. The only trial linked to any of the top-ranked predictions concerns an unrelated compound (ASP7317) in geographic atrophy and provides no evidence for nystatin.

## Literature Evidence

No randomised controlled trials were retrieved. The most relevant publications are listed below (reviews prioritised).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Review | BMJ Clin Evid | Vulvovaginal candidiasis is the second most common cause of vaginitis after bacterial vaginosis; *C. albicans* accounts for 85–90% of cases |
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Review | Pharmaceutics | Management of fluconazole-resistant vulvovaginal candidiasis, with nystatin among the alternative therapies |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | J Womens Health | Boric acid for recurrent vulvovaginal candidiasis; non-albicans species are more resistant to azoles |
| [18729533](https://pubmed.ncbi.nlm.nih.gov/18729533/) | 2008 | Review | Drugs | Local treatment of vulvovaginal candidosis; local and oral therapy considered equally effective in uncomplicated disease |
| [1436934](https://pubmed.ncbi.nlm.nih.gov/1436934/) | 1992 | Review | Obstet Gynecol Clin North Am | Nystatin, introduced in the 1950s, has been surpassed by imidazoles and triazoles as first-choice therapy |
| [10796183](https://pubmed.ncbi.nlm.nih.gov/10796183/) | 2000 | Systematic review | Cochrane Database Syst Rev | Topical treatment for vaginal candidiasis in pregnancy |
| [20406393](https://pubmed.ncbi.nlm.nih.gov/20406393/) | 2011 | Clinical study | Mycoses | Fluconazole and nystatin susceptibility compared with clinical outcome in 283 patients with complicated vulvovaginal candidosis |
| [36588489](https://pubmed.ncbi.nlm.nih.gov/36588489/) | 2022 | Clinical study | Rom J Morphol Embryol | Clinical and histopathological features of candida vaginitis before local nystatin treatment |
| [41745294](https://pubmed.ncbi.nlm.nih.gov/41745294/) | 2026 | Review | J Fungi (Basel) | Current and emerging antifungal agents for vulvovaginal candidiasis; azoles and polyenes remain the cornerstone |
| [4919155](https://pubmed.ncbi.nlm.nih.gov/4919155/) | 1970 | Review | Med Clin North Am | General review of nystatin |

## South Africa Market Information

SAHPRA indication text and manufacturer details are not available in the data compiled for this report. Essential Medicines List (EML) status is also not available.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| L/20.1.6/0394 | Nystacid | Ointment | Not available |
| 50/20.1.1/0250 | Polygynax® | Pvc | Not available |
| G1591 | Kenacomb | Cream | Not available |
| G1592 | Kenacomb | Ointment | Not available |

All four registrations are valid single-entry registrations. None has been cancelled.

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text):** adrenocortical insufficiency, Addison disease, skin atrophy, telangiectasis, capillary disease and hereditary haemorrhagic telangiectasia. These probably reflect the corticosteroid component of combination products (for example Kenacomb) rather than nystatin itself, and must be verified against the PI.
- **Drug interactions:** The interaction screen returned 100 entries, all of unknown severity. Examples include cyclosporine, fluconazole, erythromycin, azithromycin, octreotide, bortezomib, tramadol and sildenafil. These need clinical verification.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Vulvovaginitis due to Candida is already within nystatin's established antifungal activity, and the product is marketed in South Africa. However, the evidence is limited to reviews and guidelines with no trials, and nystatin has been largely superseded by azoles as first-line therapy. Non-candidal vulvovaginitis should not be expected to respond. The other top-ranked predictions should be held.

**To proceed, the following is needed:**
- SAHPRA package inserts (warnings, contraindications, approved indications), which are currently a blocking data gap
- Mechanism of action data from DrugBank
- Confirmation of whether the registered products carry a vulvovaginal indication, and in which dosage forms (the compiled data show topical and "other" routes only)
- Comparative efficacy data against azoles, particularly for fluconazole-resistant or non-albicans infections
- Clarification of the severity of the listed drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

