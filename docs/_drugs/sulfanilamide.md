---
layout: default
title: Sulfanilamide
parent: Model Prediction Only (L5)
nav_order: 431
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Sulfanilamide: predicted new indication Postmenopausal atrophic vaginitis (evidence level L5). Approved use: Vulvovaginal candidiasis, vulvovaginitis, vaginitis…"
monitor_inn: "Sulfanilamide"
predicted_indications: ["postmenopausal atrophic vaginitis", "ulceration of vulva", "vulvar neoplasm", "trichomonal vulvovaginitis", "vaginal discharge", "leukoplakia of vagina", "apocrine adenosis of breast", "blunt duct adenosis of breast", "infective vaginitis", "herpetic vulvovaginitis"]
---

# Sulfanilamide
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

# Sulfanilamide: From Vulvovaginitis to Postmenopausal Atrophic Vaginitis

## One-Sentence Summary

Sulfanilamide is a sulfonamide antibacterial, originally used for vulvovaginal infections such as vulvovaginal candidiasis, bacterial vaginosis and vaginitis.
The TxGNN model predicts it may be effective for **postmenopausal atrophic vaginitis**, but **no clinical trials and no publications** currently support this prediction.
Of the ten predictions reviewed, only **infective vaginitis** and **vaginal discharge** have any supporting literature, and that literature is old, indirect and of low quality.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vulvovaginal candidiasis, vulvovaginitis, vaginitis, bacterial vaginosis, vulvitis (from the knowledge graph; the SAHPRA records compiled for this report contain no approved indication text) |
| Predicted New Indication | Postmenopausal atrophic vaginitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, sulfanilamide is a bacteriostatic sulfonamide. It blocks bacterial folate synthesis by competing with para-aminobenzoic acid (PABA) and inhibiting dihydropteroate synthase. Its established use is in infective vaginitis.

Postmenopausal atrophic vaginitis is a different problem. It is driven by oestrogen deficiency and thinning of the vaginal epithelium, not by infection. Sulfanilamide has no known oestrogenic or tissue-restorative action. The very high TxGNN score most likely reflects the drug's closeness to other vaginitis indications in the knowledge graph, not a mechanistic basis. Treat this prediction with caution.

### Other predicted indications

The other nine predictions fall into three groups:

- **Closest to the existing use:** Infective vaginitis is essentially an extension of the labelled use rather than true repurposing. Trichomonal vulvovaginitis and vaginal discharge are infection-related, but the evidence is weak (see below).
- **Plausible only for secondary bacterial infection:** Ulceration of vulva and herpetic vulvovaginitis. The underlying causes (herpes, syphilis, autoimmune disease) are not bacterial, and herpes needs antivirals such as acyclovir.
- **No plausible mechanism:** Vulvar neoplasm, leukoplakia of vagina, apocrine adenosis of breast and blunt duct adenosis of breast. The last two share an identical score, which suggests a knowledge-graph artefact.

## Clinical Trial Evidence

Currently no related clinical trials registered for postmenopausal atrophic vaginitis. None were found for any of the other nine predicted indications either.

## Literature Evidence

There is no literature for the top-ranked prediction, postmenopausal atrophic vaginitis. The most relevant publications found for other predictions are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9132982](https://pubmed.ncbi.nlm.nih.gov/9132982/) | 1997 | RCT (comparator study) | Sex Transm Dis | Multicentre comparison of clotrimazole vaginal tablets, oral metronidazole and sulfanilamide/aminacrine/allantoin vaginal suppositories in symptomatic trichomoniasis. Sulfanilamide was not the focus. (Linked to infective vaginitis) |
| [7330756](https://pubmed.ncbi.nlm.nih.gov/7330756/) | 1981 | Review | Sex Transm Dis | General review of vulvovaginitis therapy. Metronidazole is the reliable treatment for trichomoniasis, and imidazole antifungals are superior to polyenes for candidiasis. (Linked to trichomonal vulvovaginitis and infective vaginitis) |
| [13333451](https://pubmed.ncbi.nlm.nih.gov/13333451/) | 1956 | Review / clinical experience | Med Times | Office management of leukorrhoea. (Linked to vaginal discharge) |
| [14360612](https://pubmed.ncbi.nlm.nih.gov/14360612/) | 1954 | Case series | Zentralbl Gynakol | Clinical experience with a vaginal preparation for fluor vaginalis. (Linked to vaginal discharge) |
| [14896783](https://pubmed.ncbi.nlm.nih.gov/14896783/) | 1951 | Case series | Dtsch Med Wochenschr | Leukorrhoea treated with Viozol. (Linked to vaginal discharge) |
| [14796369](https://pubmed.ncbi.nlm.nih.gov/14796369/) | 1950 | Case series | Med Klin | New treatment of leukorrhoea with Gynaedron. (Linked to vaginal discharge) |

**Limitations:** Apart from the 1997 comparator trial, the publications are decades old, are mostly uncontrolled clinical experience reports, and largely do not assess sulfanilamide directly. Several further retrieved papers (a nitrofuran animal study and two gonorrhoea papers, PMIDs 15830472, 14107752 and 14148729) were off-topic and are not listed.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H990 (OM) | Achromide | Ointment | Not available in the data compiled for this report |
| 33/10.2.1/0271 | Adco-ipratropium (ni201) | Vial | Not available in the data compiled for this report |

Both registrations are valid single-ingredient entries. The Adco-ipratropium entry is named for a different drug (ipratropium), so the registration match should be checked against the SAHPRA register before it is relied upon. Essential Medicines List (EML) status could not be determined from the data compiled for this report.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these are graph associations, not label text): inherited porphyria, porphyrin metabolism disease, porphyria, kidney disease, pyoureter, haematologic disease, liver disease, gallbladder disease, G6PD deficiency, glycogen storage disease, cystinuria and galactosemia.
- **Drug interactions:** No interaction records were found.

For label-based warnings, contraindications and dosing, please refer to the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction, postmenopausal atrophic vaginitis, is an oestrogen-deficiency condition with no plausible sulfanilamide mechanism, and no trials or publications support it. All ten predictions remain at the model-prediction stage (L4–L5), and the evidence behind the best-supported ones is old, indirect and of low quality. Modern guidelines favour other agents for the infective conditions.

**To proceed, the following is needed:**
- SAHPRA Professional Information (package insert) warnings, contraindications and approved indications. This is currently a blocking gap for safety screening.
- Mechanism of action data from DrugBank.
- Confirmation of the two SAHPRA registrations, including the product-to-drug match and EML status.
- For infective vaginitis, a head-to-head comparison against current standard-of-care agents using modern diagnostic criteria.
- A reassessment of whether the non-infective predictions (atrophic vaginitis, vulvar neoplasm, leukoplakia, breast adenosis) merit any further work. On current evidence they do not.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

