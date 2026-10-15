---
layout: default
title: Isoniazid
parent: Moderate Evidence (L3-L4)
nav_order: 278
evidence_level: L4
indication_count: 10
---

# Isoniazid
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

# Isoniazid: From Pulmonary Tuberculosis to Conjunctivitis

## One-Sentence Summary

Isoniazid is an antimycobacterial drug, originally used to treat pulmonary tuberculosis.
The TxGNN model predicts it may be effective for **conjunctivitis**, but there are **no registered clinical trials** and only **indirect literature** (11 publications, mostly case reports, reviews and a 1965 cohort study on tuberculosis-related eye disease) supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis (the registration record has no approved indication text, so this comes from the knowledge graph used by the model) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Isoniazid is a well-established antimycobacterial agent, and its efficacy in tuberculosis is proven. Its activity is generally understood to be restricted to mycobacteria.

The link to conjunctivitis is indirect. Phlyctenular keratoconjunctivitis is a hypersensitivity reaction to tuberculoprotein, and isoniazid has appeared in this context as prophylaxis (an Alaskan cohort, 1965) and as part of anti-TB therapy in case reports of conjunctival and sinonasal TB. There is no evidence that isoniazid acts directly on non-tuberculous conjunctivitis, which is mostly viral, bacterial (non-mycobacterial) or allergic. The high TxGNN score most likely reflects the TB-related ocular context in the literature, not a demonstrated therapeutic effect.

Other predictions in the model output (ranks 2 to 10) are weaker still. Only leprosy has a plausible mechanistic rationale, and its clinical support is historical and weak (see the conclusion).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Cohort | Am Rev Respir Dis | Isoniazid prophylaxis and phlyctenular keratoconjunctivitis among Eskimos in Alaska |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case report | Medicine | Phlyctenular keratoconjunctivitis with primary sinonasal TB in a child |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Case series | Oftalmologia | 28 cases of tuberculous keratoconjunctivitis, 13 in children with primary TB |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case report | Arch Ophthalmol | Primary tuberculosis of the conjunctiva |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Not classified | Ann Ocul | Local isoniazid use in ocular tuberculosis |
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Review | Optom Clin | Ocular side effects of systemic drugs, including conjunctivitis |
| [12226788](https://pubmed.ncbi.nlm.nih.gov/12226788/) | 2002 | Case report | Dtsch Med Wochenschr | Chronic reactive arthritis with conjunctivitis after intravesical BCG |
| [10084171](https://pubmed.ncbi.nlm.nih.gov/10084171/) | 1999 | Case report | Rev Rhum | Isoniazid used for refractory arthropathy after BCG therapy |

These publications concern tuberculosis-related eye disease and drug or BCG adverse reactions. None shows efficacy of isoniazid in non-tuberculous conjunctivitis.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 52/20.2/0208 | Cotrizid | Tablet | Not stated in the registration record |

Only one registration is held (a valid single-ingredient product), oral route only. Essential Medicines List status could not be determined from the data compiled for this report.

---

## Safety Considerations

**Contraindications or conditions of concern (from knowledge-graph drug-disease links, not label text):** liver failure, acute liver failure, hepatitis, liver disease, gallbladder disease, inherited porphyria, porphyria and porphyrin metabolism disease, diabetes mellitus, diabetic ketoacidosis, gout, peripheral neuropathy and peripheral nervous system disease, substance abuse/dependence, and slow acetylator status.

**Drug Interactions:** 100 interactions were identified. Those listed in this report include:
- **Moderate:** acarbose, albiglutide, alogliptin, metformin, pioglitazone, canagliflozin, dapagliflozin, chlorpropamide (a pattern of interactions with glucose-lowering drugs), metronidazole, alosetron, budesonide, cholecalciferol, calcifediol, calcitriol, picosulfuric acid
- **Minor:** hydrocortisone, triamcinolone, dexamethasone, betamethasone

**Other notes from the literature:** peripheral neuropathy, especially in slow acetylators, is a documented adverse effect, as are hepatotoxicity, rhabdomyolysis and neuropsychiatric effects. The SAHPRA package insert warnings and contraindications have not yet been retrieved. Please refer to the SAHPRA-approved Professional Information (PI) and report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by indirect literature on tuberculosis-related eye disease, with no clinical trials and no direct evidence in non-tuberculous conjunctivitis. Isoniazid also carries a notable safety burden (hepatotoxicity, neuropathy). The package insert safety data, a blocking gap, are still missing.

**To proceed, the following is needed:**
- Download and review the SAHPRA package insert for warnings, contraindications and approved indications (blocking gap)
- Detailed mechanism of action data (for example from DrugBank)
- Clarification of whether the intended use is tuberculous (phlyctenular) conjunctivitis or general conjunctivitis, and a route-compatibility assessment (current registration is oral tablet only)
- Direct clinical evidence in the target population, if the question is pursued

**Note on other predictions:** Leprosy (score 97.85%) has a mechanistic rationale, but *M. leprae* has a non-functional katG gene, isoniazid is not part of standard multidrug therapy, and the clinical support is from 1950s reports. It is best treated as a research question, not a candidate for adoption. Rheumatoid arthritis and the neuritis-type predictions appear to reflect isoniazid's role as TB prophylaxis or a neurotoxic adverse effect, not a therapeutic signal. The remaining predictions have no supporting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

