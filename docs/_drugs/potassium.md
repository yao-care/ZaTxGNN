---
layout: default
title: Potassium
parent: Model Prediction Only (L5)
nav_order: 375
evidence_level: L5
indication_count: 10
---

# Potassium
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

# Potassium: From Electrolyte Replacement to Hypertensive Disorder

## One-Sentence Summary

Potassium is an essential electrolyte. In South Africa it is registered only in parenteral nutrition and infusion products, and none of the SAHPRA records list an approved indication.
The TxGNN model predicts it may be useful for **hypertensive disorder**. The support is a few small dietary or supplement trials and about 20 publications, including a dose-response meta-analysis and a large salt-substitute RCT, but no confirmatory drug trial.
The evidence concerns dietary potassium and potassium-enriched salt substitutes, not a new drug-labelled indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA licence data |
| Predicted New Indication | Hypertensive disorder |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L3 (the source pack labelled it L1; see the note below) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 8 |
| Recommended Decision | Proceed with Guardrails |

**Evidence level note:** L1 requires at least 2 completed Phase 3 RCTs. The only Phase 3 trial that tests potassium (NCT00160368) has an unknown status. The other completed Phase 3 hypertension trials test other drugs. The support comes from meta-analyses, a large RCT of potassium-enriched salt substitute, and reviews. That fits L3, so I assigned L3 rather than L1.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for the registered products is not available. From the literature, higher potassium intake promotes renal sodium excretion. A 2023 preclinical study (PMID 37676724) shows that dietary potassium reduces activity of the NaCl cotransporter (NCC) in the distal kidney tubule. Potassium also supports vasodilation. Together these lower blood pressure, most clearly in people with high sodium intake.

Potassium has no recorded original indication in this dataset, so the prediction is best read as a nutritional or electrolyte-balance effect rather than a classic drug repurposing. Two sources support this direction. A dose-response meta-analysis of RCTs (PMID 32500831) examined potassium supplementation and blood pressure. A large randomised salt-substitute trial (PMID 34459569) examined cardiovascular events and death.

The pack's summary says no registered trial tests potassium. In fact, four small trials do: NCT00160368 (potassium chloride and bicarbonate), NCT02759367, NCT02697708 and NCT00000521. They test dietary or supplemental potassium, not a licensed potassium drug product. None is a confirmatory Phase 3 programme.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00160368](https://clinicaltrials.gov/study/NCT00160368) | Phase 3 | Unknown | 45 | Potassium chloride vs bicarbonate: effect on blood pressure, target-organ damage markers and bone health in hypertensives. No results summarised. |
| [NCT02759367](https://clinicaltrials.gov/study/NCT02759367) | N/A | Completed | 20 | Safety of adequate dietary potassium in hypertensive patients on RAAS-antagonist drugs (hyperkalaemia risk) |
| [NCT00000521](https://clinicaltrials.gov/study/NCT00000521) | Phase 4 | Completed | 285 | Sodium-potassium nutritional intervention on blood pressure rise in children and adolescents |
| [NCT02697708](https://clinicaltrials.gov/study/NCT02697708) | Phase 1/2 | Unknown | 40 | Potassium from a supplement vs potatoes vs French fries: retention, acid-base balance, blood pressure |
| [NCT04894344](https://clinicaltrials.gov/study/NCT04894344) | N/A | Completed | 196 | Education to reduce sodium intake in university students, measured by 24-hour urinary sodium |
| [NCT05991050](https://clinicaltrials.gov/study/NCT05991050) | N/A | Unknown | 30 | Whole-body vibration plus a potassium-rich DASH diet on blood pressure in obese postmenopausal women |
| [NCT03569020](https://clinicaltrials.gov/study/NCT03569020) | N/A | Completed | 43 | DASH diet effect on serum uric acid in adults with gout |
| [NCT01650012](https://clinicaltrials.gov/study/NCT01650012) | N/A | Completed | 158 | Eplerenone in haemodialysis patients. Relevant only as hyperkalaemia context, not a potassium intervention. |

Most of the other ~40 registry hits for this prediction test unrelated drugs (for example losartan salts, beta-blockers and oncology agents). They are not listed.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34459569](https://pubmed.ncbi.nlm.nih.gov/34459569/) | 2021 | RCT | N Engl J Med | Tested whether lower-sodium, higher-potassium salt substitutes change cardiovascular events and death, beyond blood pressure |
| [32500831](https://pubmed.ncbi.nlm.nih.gov/32500831/) | 2020 | Meta-analysis of RCTs | J Am Heart Assoc | Dose-response relationship between potassium supplementation (≥4 weeks) and blood pressure |
| [23558164](https://pubmed.ncbi.nlm.nih.gov/23558164/) | 2013 | Systematic review and meta-analysis | BMJ | Effect of increased potassium intake on cardiovascular risk factors and disease |
| [37676724](https://pubmed.ncbi.nlm.nih.gov/37676724/) | 2023 | Preclinical mechanistic | J Clin Invest | Dietary potassium reduces NCC activity via Ppp1Ca-Ppp1r1a dephosphorylation and lowers blood pressure |
| [37772757](https://pubmed.ncbi.nlm.nih.gov/37772757/) | 2024 | Review | Am J Hypertens | State-of-the-art review of potassium and hypertension |
| [39472546](https://pubmed.ncbi.nlm.nih.gov/39472546/) | 2025 | Review | Hypertens Res | Role of dietary potassium and salt substitution in preventing and managing hypertension |
| [27455317](https://pubmed.ncbi.nlm.nih.gov/27455317/) | 2016 | Review | Nutrients | Potassium intake, bioavailability, hypertension and glucose control |
| [26634368](https://pubmed.ncbi.nlm.nih.gov/26634368/) | 2016 | Review | J Physiol Biochem | Dietary potassium in hypertension and diabetes; intervention trials show blood pressure benefit |
| [10979053](https://pubmed.ncbi.nlm.nih.gov/10979053/) | 2000 | Expert consensus review | Arch Intern Med | Guidelines for potassium replacement in clinical practice |
| [40232853](https://pubmed.ncbi.nlm.nih.gov/40232853/) | 2025 | Animal study | JCI Insight | Potassium supplementation attenuated blood pressure in salt-sensitive rats of both sexes |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| T/30.3/704 | Stabilised Human Serum-5% Protein Solution | Infusion | Not recorded |
| Exclusion under Section 36 & Section 14 | ITN 3014Xa 750ml | TPN | Not recorded |
| Article 21B | TPN non-specific | Infusion | Not recorded |
| Exclusion under Section 36 & Section 14 | ITN 8807a 2390ml | TPN | Not recorded |
| Exclusion under Section 36 & Section 14 | ITN 5501a 2240ml | TPN | Not recorded |

Five of the 8 registrations are shown. All are infusion or parenteral nutrition preparations, several under Section 21/36/14 exclusions rather than a standard registration. None is an oral potassium supplement or a hypertension product.

---

## Safety Considerations

- **Drug Interactions:** No interaction records were found in the queried database.

The SAHPRA package-insert warnings and contraindications were not retrieved. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Guardrails from the literature review:
- Avoid in chronic kidney disease with reduced eGFR and in anyone at risk of hyperkalaemia.
- Take extra care with concurrent ACE inhibitors, ARBs, mineralocorticoid antagonists or potassium-sparing diuretics.
- Monitor serum potassium.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The link between potassium intake and lower blood pressure has meta-analysis and large-RCT support, but it applies to dietary potassium and salt substitutes, not to the infusion products registered in South Africa. The safety review is incomplete because the SAHPRA PI data is missing (a blocking gap). Any further work should therefore stay within nutritional or supplement use, with potassium monitoring.

**To proceed, the following is needed:**
- Retrieve and review the SAHPRA package inserts for warnings and contraindications (blocking).
- Obtain mechanism-of-action data from DrugBank.
- Confirm whether an oral potassium product or salt substitute is available and registered in South Africa, since the current registrations are parenteral.
- Draw up a monitoring protocol for patients with CKD or on RAAS-acting drugs.

**Other predictions:** Congestive heart failure (98.41%) is a research question only, because the evidence is observational and concerns correcting deficiency. The other eight predictions (pulmonary hypertension subtypes, malignant hypertensive renal disease, malignant renovascular hypertension, Braddock syndrome, chronic pulmonary heart disease, alopecia and congenital hypotrichosis milia) are on Hold. They rest on model prediction or indirect potassium-channel biology, and no relevant potassium trials support them.

*For research reference only; not medical advice. Predictions require clinical validation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

