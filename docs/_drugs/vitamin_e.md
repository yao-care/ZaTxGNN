---
layout: default
title: Vitamin E
parent: 僅模型預測 (L5)
nav_order: 462
evidence_level: L5
indication_count: 10
---

# Vitamin E
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

# Vitamin E: From Nutritional Supplementation to Inborn Disorder of Bilirubin Metabolism

## One-Sentence Summary

Vitamin E (DrugBank DB00163) is a fat-soluble antioxidant vitamin conventionally used for nutritional supplementation; this evidence pack records no formal original indication and no current market registration. The TxGNN model predicts potential effectiveness for **Inborn Disorder of Bilirubin Metabolism**, but this direction is currently supported only by **3 clinical trials** (none testing Vitamin E as the study drug) and **2 publications** (case report/review level, not evaluating Vitamin E).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded — no approved indication or product license on file for this drug |
| Predicted New Indication | Inborn Disorder of Bilirubin Metabolism |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Vitamin E is not available in this evidence pack. Based on general pharmacological knowledge, Vitamin E (α-tocopherol) is a lipid-soluble antioxidant that scavenges free radicals and protects cell membranes from oxidative damage — this is the basis of its conventional use in correcting vitamin E deficiency and as adjunctive antioxidant support.

Inborn disorders of bilirubin metabolism (e.g., Crigler-Najjar syndrome, Gilbert syndrome) are caused primarily by UGT1A1 enzyme deficiency, a defect in hepatic conjugation — a pathway with no established direct biochemical link to antioxidant activity. The model's own rationale for this candidate states explicitly that there is no direct mechanistic connection between Vitamin E's antioxidant activity and the enzymatic defects underlying these disorders.

Consistent with this, the supporting evidence is weak by design, not by omission: all three retrieved clinical trials were graded "C" relevance because the tested drug was *not* Vitamin E (lomitapide, eplontersen, cholic acid) — they were only pulled in via disease-term overlap. The two literature hits are a 1975 review/case report and a 1994 case report on a bile-acid synthesis defect, neither of which studied Vitamin E. This is a **model-generated signal without drug-specific supporting evidence**, and should be interpreted accordingly.

*(Note: a related but distinct candidate in this evidence pack, "bilirubin metabolism disease" — a broader liver/cholestasis-related term — has materially stronger evidence, including a completed Phase 4 RCT directly testing Vitamin E, NCT04977661/PMID 34919247. This may be a more actionable signal than the top-ranked candidate and is worth separate evaluation.)*

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01556906](https://clinicaltrials.gov/study/NCT01556906) | Phase 2 | Completed | 6 | Dose-escalation safety/tolerability study of lomitapide (MTP inhibitor) in homozygous familial hypercholesterolemia; **Vitamin E was not the study drug** — relevance flagged as disease-term match only. |
| [NCT06465810](https://clinicaltrials.gov/study/NCT06465810) | N/A | Recruiting | 1850 | Non-interventional, multi-country registry on ATTR amyloidosis treatment patterns (eplontersen); **no Vitamin E arm**. |
| [NCT03115086](https://clinicaltrials.gov/study/NCT03115086) | N/A | Active, not recruiting | 55 | Post-marketing patient registry for Cholbam (cholic acid) in bile acid synthesis disorders; **no Vitamin E arm**. |

**None of the retrieved trials tested Vitamin E for this indication** — all were captured via disease-term overlap rather than drug-specific evaluation.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [803225](https://pubmed.ncbi.nlm.nih.gov/803225/) | 1975 | Review/Case | The New England Journal of Medicine | Discussion of neonatal nonhemolytic jaundice; abstract not available, does not evaluate Vitamin E. |
| [7915305](https://pubmed.ncbi.nlm.nih.gov/7915305/) | 1994 | Case Report | The Journal of Pediatrics | Describes 3β-hydroxy-C27-steroid dehydrogenase/isomerase deficiency as a cause of progressive intrahepatic cholestasis (Byler disease); does not evaluate Vitamin E. |

---

## South Africa Market Information

Vitamin E is currently **not marketed** under this evidence pack, with **0 registrations on file**. No product license, dosage form, or approved indication text is available to summarize.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted mechanism has no established biochemical link to the disease's known pathophysiology (UGT1A1 deficiency vs. antioxidant activity), and none of the retrieved clinical trials or literature actually studied Vitamin E for this indication — the high TxGNN score is not yet corroborated by drug-specific evidence. Two blocking/high-severity data gaps (missing PI warnings/contraindications, missing MOA) also prevent a preliminary safety assessment.

**To proceed, the following is needed:**
- TFDA/SAHPRA-equivalent product labeling (warnings, contraindications) — currently blocking (DG001)
- Verified mechanism-of-action data from DrugBank — currently high-impact gap (DG002)
- Drug-specific (Vitamin E) clinical trials or case series in inborn bilirubin metabolism disorders
- Consider evaluating the related, better-evidenced candidate "bilirubin metabolism disease" (L2, completed RCT NCT04977661) as a potentially more actionable repurposing direction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

