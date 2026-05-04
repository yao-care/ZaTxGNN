---
layout: default
title: Ammonium Chloride
parent: 僅模型預測 (L5)
nav_order: 34
evidence_level: L5
indication_count: 10
---

# Ammonium Chloride
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

# Ammonium Chloride: From Expectorant to Acute Laryngopharyngitis

---

## One-Sentence Summary

Ammonium chloride is a traditional expectorant and urinary acidifier with a pharmacopoeial history spanning over a century in compound cough and throat preparations. The TxGNN model predicts it may be effective for **Acute Laryngopharyngitis** as the top-ranked indication (score: 99.94%), though **no direct clinical trials or publications** currently support this specific use. Notably, a secondary prediction for **Headache Disorder** (rank 7) carries the highest available evidence level in this evaluation — including **5 historical publications** (1955–1982) directly investigating ammonium chloride for achlorhydric migraine — and is flagged separately as a research-worthy finding.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Expectorant; urinary acidification (traditional pharmacopoeial use — no formal registered indication identified in this data set) |
| Predicted New Indication (Top) | Acute Laryngopharyngitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 — mechanistic plausibility only; no direct clinical studies |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ammonium chloride is a classic reflex expectorant: the ammonium ion (NH₄⁺) mildly irritates the gastric mucosa, stimulating a vagally-mediated reflex that increases respiratory tract mucus secretion, reduces mucus viscosity, and improves mucociliary clearance. This mechanism is well established in traditional pharmacopoeial literature and has underpinned ammonium chloride's inclusion in compound cough mixtures, expectorant syrups, and throat preparations for generations.

Acute laryngopharyngitis presents with inflammatory oedema and mucosal congestion of the larynx and pharynx, often accompanied by a dry, irritating cough and impaired mucus drainage — features that align directly with the therapeutic target of ammonium chloride's expectorant mechanism. The TxGNN knowledge graph prediction almost certainly captures this pharmacological overlap through shared upper respiratory tract disease nodes, making the prediction biologically coherent and not a model artefact.

Currently, detailed mechanism of action data are not available from DrugBank for this evidence pack. Based on established pharmacology, ammonium chloride undergoes hepatic conversion via the urea cycle (NH₄⁺ + HCO₃⁻ → urea + H₂O), with the chloride ion contributing to mild systemic acidification. While the mechanistic rationale for acute laryngopharyngitis is plausible, no modern randomised controlled trials have tested this hypothesis, and the prediction remains at the mechanistic-inference level (L4). Standard care for acute laryngopharyngitis — analgesics, antipyretics, and antivirals where indicated — should not be displaced without direct clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ammonium Chloride in Acute Laryngopharyngitis.

---

## Literature Evidence

Currently no related literature available for Ammonium Chloride in Acute Laryngopharyngitis.

---

## Notable Secondary Finding: Headache Disorder (Rank 7, L3)

Among all 10 TxGNN predictions evaluated, **Headache Disorder** carries the highest evidence level (**L3**) and merits separate attention. A historical body of European research (1955–1982) investigated ammonium chloride therapy for **achlorhydric migraine** — a proposed subtype in which gastric achlorhydria leads to incomplete protein digestion, excess intestinal ammonia generation, elevated blood ammonia levels, and neurotoxic headache. The proposed mechanism holds that ammonium chloride provides a controlled NH₄⁺ load which, through competitive urea cycle metabolism, reduces pathological free ammonia accumulation and thereby alleviates headache. Five publications directly examined this hypothesis.

### Headache Disorder — Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [13254186](https://pubmed.ncbi.nlm.nih.gov/13254186/) | 1955 | Historical Case Series | Orvosi Hetilap | Direct investigation of ammonium chloride therapy in chronic migraine; Fazekas series |
| [13466764](https://pubmed.ncbi.nlm.nih.gov/13466764/) | 1957 | Historical Case Series | Revue Neurologique | Anaclorhydric migraine treated with ammonium chloride; pathogenic considerations (Wolinetz & Godard) |
| [13345397](https://pubmed.ncbi.nlm.nih.gov/13345397/) | 1956 | Historical Clinical Study | Ideggyogyaszati Szemle | Effects of ammonium chloride on the neuro-endocrine system in chronic headaches |
| [13317850](https://pubmed.ncbi.nlm.nih.gov/13317850/) | 1956 | Historical Clinical Study | Endokrinologie | Ammonium chloride and the neuroendocrine system with reference to chronic headaches |
| [6294857](https://pubmed.ncbi.nlm.nih.gov/6294857/) | 1982 | Clinical Review | La Semaine des Hôpitaux | Achlorhydric migraine: pathogenesis and management — most recent review of the hypothesis |

> **Important caveats**: All publications are from 1955–1982, predate modern randomised trial standards, and have not been replicated in contemporary research. Abstracts are unavailable for four of the five papers. The concept of achlorhydric migraine does not appear in the current International Headache Classification (ICHD-3). Despite this, ammonium chloride is the **only drug evaluated across all 10 predictions here that has any historical direct clinical evidence**, making this finding unique in this data set.

### Headache Disorder — Clinical Trial Evidence

The 2 trials retrieved for headache disorder were assessed as **Grade C relevance** — both evaluated different study drugs (intravenous pantoprazole; intrathecal neostigmine) and did not investigate ammonium chloride. No directly relevant trials are registered.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA via [MedSafety](https://www.sahpra.org.za/pharmacovigilance/).

**Clinically important general safety considerations** relevant to South African practice (from established pharmacology, not the DrugBank data in this pack, which was not available):

- Ammonium chloride can precipitate **systemic metabolic acidosis** at supra-therapeutic doses, as the urea cycle becomes saturated.
- It is pharmacologically contraindicated in **hepatic impairment** (inability to convert NH₄⁺ to urea) and **renal impairment** (inability to excrete the acid load). Given South Africa's high burden of HIV-associated hepatic and renal disease, these contraindications are of direct clinical relevance.
- No drug-drug interaction data were retrieved in this evaluation. Clinicians should review interactions with diuretics and alkalinising agents in particular.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although ammonium chloride's expectorant mechanism provides pharmacological plausibility for the top TxGNN prediction (acute laryngopharyngitis), the complete absence of direct clinical trial or published literature evidence for this indication — combined with the drug's currently unregistered status in South Africa (0 SAHPRA licences) — does not support clinical progression at this time.

**To proceed, the following is needed:**

- **For Acute Laryngopharyngitis (rank 1):**
  - At minimum, a prospective observational study or pilot RCT evaluating ammonium chloride as adjunctive expectorant therapy in acute laryngopharyngitis
  - Full safety and contraindication data retrieved from the SAHPRA PI document and DrugBank MOA records (both currently absent from this pack)
  - Consideration of the appropriate SAHPRA regulatory pathway (Section 21 named patient authorisation, or new indication application) before any organised use

- **For Headache Disorder (rank 7 — secondary priority):**
  - A modern pharmacological reassessment of the achlorhydric migraine hypothesis using contemporary biomarkers (fasting serum ammonia, gastric pH measurement, validated migraine diary endpoints) before any clinical study is initiated
  - A scoping review to determine whether any post-1982 literature exists in non-English language journals that was not captured in this PubMed search
  - Ethical and scientific review to determine whether revisiting this 1950s hypothesis is warranted given current migraine treatment options (triptans, CGRP antagonists)

- **For both indications:**
  - Population-specific safety assessment for South African patients (hepatic disease, renal disease, HIV co-morbidities, potential interactions with antiretroviral therapy)
  - Inclusion of SANCTR (South African National Clinical Trials Register) and PACTR (Pan African Clinical Trials Registry) searches to identify any regionally registered trials not captured in ClinicalTrials.gov

---

*This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. YMYL disclaimer: predictions generated by the TxGNN computational model are hypothesis-generating and must not be used to guide clinical treatment decisions without independent clinical evidence review.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

