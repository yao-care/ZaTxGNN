---
layout: default
title: Arginine
parent: 僅模型預測 (L5)
nav_order: 43
evidence_level: L5
indication_count: 1
---

# Arginine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# L-Arginine: From Nutritional Amino Acid Supplement to Gastroparesis

## One-Sentence Summary

L-Arginine is a semi-essential amino acid used clinically as a nutritional supplement and in metabolic conditions such as urea cycle disorders, with no currently registered pharmaceutical indication in South Africa.
The TxGNN model predicts it may be effective for **Gastroparesis** via the nitric oxide (NO) signalling pathway,
with **no directly relevant clinical trials** and **10 preclinical publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Nutritional amino acid supplement; metabolic support (no SAHPRA-registered indication) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

L-Arginine is the obligate substrate for nitric oxide synthase (NOS), catalysing the conversion of L-arginine to L-citrulline and nitric oxide (NO) via the eNOS/nNOS pathway. NO is the principal inhibitory neurotransmitter in the enteric nervous system: it mediates pyloric sphincter relaxation and gastric accommodation — the reflex expansion of the stomach in response to incoming food. When NO bioavailability is reduced, the pylorus fails to relax appropriately and gastric emptying is delayed, which is the defining feature of gastroparesis.

The most direct mechanistic evidence comes from PMID 25057793 (Reichardt et al., 2014, *Endocrinology*), which demonstrated that oral dexamethasone causes gastroparesis in mice by specifically depleting L-arginine, and that the effect is abolished in GR(dim) mice, establishing a direct causal chain: glucocorticoid → L-arginine depletion → nitrergic failure → gastroparesis. This is corroborated by multiple independent animal studies showing that nNOS dysfunction (PMID 18312542), tetrahydrobiopterin deficiency impairing NOS activity (PMID 23639814), and impaired nitrergic pyloric relaxation in Parkinson's disease models (PMID 35380456) all produce a gastroparesis phenotype.

However, the entire mechanistic framework currently rests on animal models. No human clinical trial has evaluated L-arginine supplementation as a treatment for gastroparesis, and whether restoring arginine bioavailability translates to clinically meaningful improvements in gastric emptying in humans remains unproven. The jump from mouse and rat models to a human therapeutic strategy requires dedicated clinical validation.

---

## Clinical Trial Evidence

The database search identified one trial (NCT01702051), which investigates autologous pancreatic islet cell transplantation after pancreatectomy for chronic pancreatitis. Although post-pancreatectomy gastroparesis can occur as a surgical complication and L-arginine is involved in the arginine stimulation test for insulin secretion, the intervention in this trial is cell transplantation — not L-arginine administration. This trial was assigned a relevance grade of **C** and does not constitute supporting evidence for the predicted indication.

**Currently no directly relevant clinical trials evaluating L-arginine for gastroparesis are registered.**

---

## Literature Evidence

All 10 publications retrieved are animal or mechanistic studies (Tier 2–3). No human RCTs, clinical cohort studies, or systematic reviews were identified. The most mechanistically relevant papers are listed first.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25057793](https://pubmed.ncbi.nlm.nih.gov/25057793/) | 2014 | Animal Study (Mechanistic) | *Endocrinology* | Dexamethasone causes gastroparesis in mice by depleting L-arginine; strongest direct causal link between arginine deficiency and gastroparesis |
| [35380456](https://pubmed.ncbi.nlm.nih.gov/35380456/) | 2022 | Animal Study (Mechanistic) | *Am J Physiol Gastrointest Liver Physiol* | Impaired nitrergic (NO-mediated) relaxation of the pyloric sphincter in a 6-OHDA Parkinson's disease rat model; confirms nNOS/NO as the key effector pathway |
| [23639814](https://pubmed.ncbi.nlm.nih.gov/23639814/) | 2013 | Animal Study (Mechanistic) | *Am J Physiol Gastrointest Liver Physiol* | Tetrahydrobiopterin deficiency — a required NOS cofactor — causes gastroparesis in newborn mice, further supporting NO synthesis as the critical pathway |
| [18312542](https://pubmed.ncbi.nlm.nih.gov/18312542/) | 2008 | Animal Study (Mechanistic) | *Neurogastroenterol Motil* | Reduced nNOS expression in jejunal myenteric neurons of diabetic BB-rats, implicating nitrergic deficit as a driver of diabetic gastroparesis |
| [19023028](https://pubmed.ncbi.nlm.nih.gov/19023028/) | 2009 | Animal Study | *Am J Physiol Gastrointest Liver Physiol* | Synchronised gastric electrical stimulation rescues impaired gastric accommodation after vagotomy in dogs via the nitrergic pathway |
| [18322959](https://pubmed.ncbi.nlm.nih.gov/18322959/) | 2008 | Animal Study | *World J Gastroenterol* | Ghrelin and GHRP-6 improve gastric motility in diabetic mice with gastroparesis; contextual pharmacological model |
| [21193530](https://pubmed.ncbi.nlm.nih.gov/21193530/) | 2011 | Animal Study (Mechanistic) | *Am J Physiol Gastrointest Liver Physiol* | Hyperglycaemia inhibits gastric motility via nodose ganglia K(ATP) channels and vagal afferent pathways |
| [31984783](https://pubmed.ncbi.nlm.nih.gov/31984783/) | 2020 | Animal Study | *Am J Physiol Gastrointest Liver Physiol* | Sacral nerve stimulation improves impaired gastric accommodation via spinal afferent and vagal efferent mechanisms in rats |
| [33867519](https://pubmed.ncbi.nlm.nih.gov/33867519/) | 2021 | Case Report | *Am J Case Rep* | Lifestyle changes normalise serum lactate in a MELAS patient using L-arginine as mitochondrial support; indirect relevance to L-arginine's metabolic role in NO-related pathways |
| [8194696](https://pubmed.ncbi.nlm.nih.gov/8194696/) | 1994 | Animal Study | *Gastroenterology* | Food protein-induced anaphylaxis causes delayed gastric emptying in sensitised rats; identifies additional aetiological context for gastroparesis |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA via the MedWatch reporting system.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic hypothesis is biologically coherent and directly supported by animal evidence — L-arginine depletion has been causally demonstrated to induce gastroparesis via nitrergic pathway failure — but the entire evidence base remains at the preclinical level (L4), with no human trials identified and no SAHPRA-registered pharmaceutical products in South Africa. This is a scientifically interesting research question, not yet a clinically actionable repurposing candidate.

**To proceed, the following is needed:**
- A human proof-of-concept or Phase 1/2 clinical trial evaluating oral or intravenous L-arginine supplementation in gastroparesis patients, with gastric emptying scintigraphy as the primary endpoint
- Pharmacodynamic data in humans confirming that L-arginine supplementation restores NO bioavailability and pyloric relaxation at achievable plasma concentrations
- Dose-finding data: standard nutritional supplement doses (2–6 g/day) may differ substantially from the pharmacological doses required to restore nitrergic tone in gastroparesis
- Detailed mechanism of action and safety profile data from DrugBank (currently a noted data gap)
- Drug interaction assessment, particularly with phosphodiesterase inhibitors, antihypertensives, and anticoagulants, given L-arginine's NO-mediated vasodilatory effects
- A SAHPRA regulatory pathway assessment, as L-arginine is not currently registered as a pharmaceutical product in South Africa and a new marketing authorisation application would be required
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

