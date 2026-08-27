---
layout: default
title: Selenium
parent: 僅模型預測 (L5)
nav_order: 403
evidence_level: L5
indication_count: 10
---

# Selenium
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

# Selenium: From Trace Element Supplementation to Sclerosing Cholangitis

## One-Sentence Summary

> Selenium (DrugBank DB11135) is an essential trace element with no specific approved disease indication on file in this evidence pack.
> The TxGNN model predicts it may be relevant to **Sclerosing Cholangitis**, but the supporting literature shows selenium deficiency as a *consequence* of the disease's cholestasis-driven malabsorption, not a validated treatment target —
> with **0 clinical trials** and **5 publications** currently available, none testing selenium supplementation as therapy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No specific approved indication on file — Selenium is registered here as an essential trace element/nutritional supplement rather than a drug approved for a defined disease |
| Predicted New Indication | Sclerosing Cholangitis (primary sclerosing cholangitis, PSC) |
| TxGNN Prediction Score | 99.04% (global rank 4,662) |
| Evidence Level | L4 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on known information, Selenium is a cofactor for glutathione peroxidase and other selenoproteins, giving it a general antioxidant role in human physiology.

Sclerosing cholangitis is a chronic cholestatic liver disease. The literature linking selenium to PSC describes **hepatic retention of copper and selenium** and **poor fat-soluble micronutrient intake** in PSC patients — findings that point to disease-driven trace-element derangement (malabsorption secondary to cholestasis), not a demonstrated benefit of selenium *supplementation* in treating PSC.

Critically, the evidence pack's own mechanistic assessment flags this directly: selenium deficiency in PSC appears to be a **result of the disease**, not a treatment target, and there is **no mechanistic hypothesis supporting selenium supplementation as PSC therapy**. The TxGNN score should therefore be read as a knowledge-graph association (both entities co-occur in liver/trace-element literature) rather than evidence of therapeutic applicability.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9053974](https://pubmed.ncbi.nlm.nih.gov/9053974/) | 1995 | Cohort | Scandinavian Journal of Gastroenterology | Hepatic copper and selenium retention studied in 32 PSC patients; indicates abnormal trace-element metabolism in PSC, not a treatment effect |
| [39601354](https://pubmed.ncbi.nlm.nih.gov/39601354/) | 2025 | Cohort/Dietary survey | Liver International | PSC patients show poor dietary intake of fat-soluble vitamins and lower overall diet quality versus Nordic nutrition recommendations |
| [29148959](https://pubmed.ncbi.nlm.nih.gov/29148959/) | 2017 | Case report | JPEN (J Parenter Enteral Nutr) | Case report on parenteral lipid emulsion in a patient with severe malabsorption and overlapping PSC/ulcerative colitis; discusses oxidative stress and antioxidant status in cholestatic disease |
| [17109383](https://pubmed.ncbi.nlm.nih.gov/17109383/) | 2006 | Animal/Proteomic | Proteomics | Hepatic proteome changes in murine models of toxin-induced fibrosis and sclerosing cholangitis; mechanistic, not selenium-specific |
| [18941372](https://pubmed.ncbi.nlm.nih.gov/18941372/) | 2008 | Review | European Journal of Cancer Prevention | Review of colorectal cancer chemoprevention agents (aspirin, NSAIDs); topic overlap with PSC/selenium is minimal — low relevance |

---

## South Africa Market Information

Selenium is currently **not marketed** in South Africa under this evidence pack, with **0 SAHPRA registrations** on file. No product/registration records are available to summarize.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The available literature shows selenium/trace-element abnormalities as a *downstream consequence* of PSC-related cholestasis and malabsorption, not evidence that selenium supplementation treats the disease. No clinical trials have tested selenium in PSC, and no mechanistic rationale supports repurposing at this stage.

**To proceed, the following is needed:**
- Mechanism of action data for Selenium (Data Gap DG002)
- TFDA/SAHPRA-approved Professional Information — warnings, contraindications, DDI (Data Gap DG001)
- An interventional study specifically testing selenium supplementation as a therapeutic intervention in PSC patients (current data is observational/correlational only)
- Reassessment of causality: whether correcting selenium deficiency alters PSC disease course, versus deficiency being merely a biomarker of cholestasis severity

**Note:** Other TxGNN-predicted indications in this evidence pack carry stronger evidence than the top-ranked hit — notably **congestive heart failure** (Evidence Level L2, decision stage S2, 4 clinical trials including two large Phase 3 RCTs: NCT06694727 n=4,044 and NCT07234422 n=1,100) and **rheumatoid arthritis** (Evidence Level L3, decision stage S1, one Phase 1-tier RCT/meta-analysis plus multiple mechanistic studies). These may warrant separate evaluation reports given their comparatively stronger evidentiary base.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

