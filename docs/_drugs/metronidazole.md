---
layout: default
title: Metronidazole
parent: Model Prediction Only (L5)
nav_order: 321
evidence_level: L5
indication_count: 10
---

# Metronidazole
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

# Metronidazole: From Anaerobic and Protozoal Infections to Pneumocystosis

## One-Sentence Summary

Metronidazole is a nitroimidazole antimicrobial, marketed in South Africa as oral, intravenous and vaginal gel products. The TxGNN model ranks **pneumocystosis** as its top predicted new indication, with a score of 99.99%. **No relevant clinical trials or supporting publications** were found. The review concludes that the prediction is most likely a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA records supplied. Metronidazole is an established antimicrobial for anaerobic bacterial and protozoal infections (the source reviews cite amoebiasis and trichomoniasis). |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug in the Evidence Pack. Metronidazole is known to act against anaerobic bacteria and protozoa through reduction of its nitro group.

The link to pneumocystosis is weak. *Pneumocystis* is a fungus, and metronidazole has no established antifungal or anti-*Pneumocystis* activity. A 1980 review in the evidence set lists trimethoprim-sulfamethoxazole as the drug of choice for pneumocystis pneumonia and metronidazole for amoebic colitis and trichomoniasis. The very high score most likely reflects the drug's neighbours in the knowledge graph (antiparasitic and antiprotozoal agents) rather than a real therapeutic relationship.

The same pattern applies to other low-ranked predictions in this set. Cryptococcal meningitis (also a fungus), postmenopausal atrophic vaginitis (estrogen-deficiency driven), and the conjunctivitis predictions have no plausible metronidazole mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

The search returned 23 trial records. Ten were reviewed and graded unrelated, and the other 13 were not yet graded. Their titles cover health-services, behavioural, education and device topics, and none involves metronidazole or *Pneumocystis*. No SANCTR or PACTR entries were found.

## Literature Evidence

None of the ten publications shows metronidazole treating pneumocystosis. No RCTs were retrieved.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | Am Fam Physician | Lists metronidazole for amoebic colitis and trichomoniasis, and trimethoprim-sulfamethoxazole for pneumocystis pneumonia |
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clin Proc | General review of antiparasitic agents; no metronidazole–*Pneumocystis* finding |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clin Pharmacokinet | Pharmacokinetic rationale for antiprotozoal therapy |
| [2280469](https://pubmed.ncbi.nlm.nih.gov/2280469/) | 1990 | Review | Nihon Rinsho | Review of drugs against protozoan infections (no abstract available) |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clin Pharm | Reviews treatment of AIDS infections; *Pneumocystis carinii* pneumonia is the most common life-threatening one |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Top Antivir Med | HIV opportunistic infections remain relevant; no metronidazole treatment data |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Rev Infect Dis | Critique of antimicrobial prophylaxis trials; not specific to pneumocystosis |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case report | Am Rev Respir Dis | Man given metronidazole and tetracycline for diarrhoea later developed *Pneumocystis* and CMV pneumonia (an association, not a treatment) |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case series | Kansenshogaku Zasshi | Metronidazole treated amoebic dysentery in a patient who later developed PCP |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case report | J Formos Med Assoc | AIDS patient with amoebic colitis and CMV disease and colon perforation; not a pneumocystosis treatment report |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. S/20.2.6/153 | Sandoz Metronidazole | Tablet (oral) |
| Reg. No. 42/20.2/0567 | Bio Metronidazole IV | Infusion (injectable) |
| Reg. No. 33/20.2.6/0243 | Metrogel V | Vaginal gel |

Approved indication text and manufacturer were not supplied for these registrations.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Pneumocystosis has no credible mechanistic link, no relevant trials, and no supportive publications, so the score is best treated as a model artifact. Pneumocystosis should not be pursued further for metronidazole.

**Other candidates in this prediction set (for separate review):**
- **Cap polyposis** (L4): case reports describe remission after antibiotic regimens that included metronidazole, and one report proposes an anti-inflammatory mechanism. The evidence is case-level only, and one refractory case shows an inconsistent response.
- **Vulval ulceration** (L3, tentative): metronidazole is used in vulval Crohn's disease and amoebic ulcers. The grade rests on titles only and needs full-text confirmation.
- **Ulcerative proctosigmoiditis** and **myiasis** (L4): the links are indirect and weak.

**To proceed, the following is needed:**
- The SAHPRA package insert warnings and contraindications (a blocking gap for safety screening).
- Mechanism of action data from DrugBank.
- Full-text review of the cap polyposis and vulval ulceration literature to see whether metronidazole outcomes are actually reported.

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

