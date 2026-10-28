---
layout: default
title: Dabigatran Etexilate
parent: Model Prediction Only (L5)
nav_order: 162
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Dabigatran Etexilate: predicted new indication Sclerosing cholangitis (evidence level L5). Approved use: Not available in the registration data (the anticoagulant use is infe…"
monitor_inn: "Dabigatran etexilate"
predicted_indications: ["sclerosing cholangitis", "obsolete familial combined hyperlipidemia", "hypoalphalipoproteinemia", "homozygous familial hypercholesterolemia", "primary release disorder of platelets"]
---

# Dabigatran Etexilate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Dabigatran etexilate: From Thromboembolic Anticoagulation to Sclerosing Cholangitis
{: .text-alpha }

## One-Sentence Summary

Dabigatran etexilate is an oral direct thrombin inhibitor, marketed in South Africa as an anticoagulant. The original indication text is not recorded in the data compiled for this report.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but there are **0 clinical trials** and only **1 publication** (a drug-interaction study of a different compound), so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the registration data (the anticoagulant use is inferred from the drug class) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 2 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Dabigatran is known to be a direct thrombin (factor IIa) inhibitor.

The link to sclerosing cholangitis is speculative. Thrombin and PAR signalling may contribute to liver fibrosis and inflammation, but this has not been established for diseases of the bile ducts. The single linked publication (PMID 36906733) is a drug-interaction study of cilofexor, a different compound. It does not test dabigatran in this disease. The very high TxGNN score is a computational prediction only.

Other top-ranked predictions are weaker still. One is a bleeding disorder (primary platelet release disorder), where an anticoagulant would be expected to raise bleeding risk. Others are lipid disorders, with no plausible mechanistic link and no evidence. These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for sclerosing cholangitis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36906733](https://pubmed.ncbi.nlm.nih.gov/36906733/) | 2023 | In vitro / drug-interaction pharmacology | Clinical Pharmacokinetics | Evaluates CYP450 and transporter-mediated drug interaction potential of cilofexor, an FXR agonist in development for primary sclerosing cholangitis and NASH. It does not evaluate dabigatran efficacy. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 56/8.2/0690.687 | Dabitrin 110Mg | Capsule | Not available |
| Reg. No. 56/8.2/0695 | Dabigatran 75 Drl | Capsule | Not available |

Both registrations are valid single-ingredient oral products. Essential Medicines List (EML) status is not available in the data compiled for this report.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease edges in the TxGNN knowledge graph, not label text): blood coagulation disease, anaemia, macrocytic anaemia and intracerebral haemorrhage.
- **Bleeding risk in platelet and coagulation disorders:** several predicted indications are bleeding disorders, where an anticoagulant is mechanistically inappropriate.
- **Drug interactions:** Dabigatran is a P-gp substrate, so interactions with some antiretrovirals (for example boosted protease inhibitors) are a practical concern. No interaction records were retrieved.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no clinical trials, and the only publication does not study dabigatran. The mechanistic link is speculative, and the bleeding risk and knowledge-graph contraindication signals argue for caution.

**To proceed, the following is needed:**
- The SAHPRA package insert, to confirm approved indications, warnings and contraindications (a blocking gap)
- Mechanism of action data from DrugBank
- Preclinical or clinical evidence of dabigatran in cholestatic or fibrotic liver disease
- A hepatobiliary safety and bleeding risk assessment in patients with sclerosing cholangitis, including portal hypertension and varices
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

