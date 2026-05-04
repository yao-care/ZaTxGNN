---
layout: default
title: Iopamidol
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
---

# Iopamidol
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

# Iopamidol: From Radiographic Contrast Imaging to Prinzmetal Angina

## One-Sentence Summary

Iopamidol is a non-ionic, low-osmolality iodinated radiographic contrast medium used in diagnostic imaging procedures including computed tomography (CT), angiography, and myelography — it has no currently registered therapeutic indication. The TxGNN model predicts it may be relevant to **Prinzmetal Angina** (variant angina) with a score of **98.57%**, however **no clinical trials** and **no supporting publications** exist for this as a therapeutic application. The high prediction score is most likely a knowledge graph artefact arising from Iopamidol's extensive co-occurrence with cardiovascular disease nodes in imaging literature, rather than a genuine therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Radiographic contrast medium (CT, angiography, myelography) — no SAHPRA-registered therapeutic indication |
| Predicted New Indication | Prinzmetal Angina (variant angina) |
| TxGNN Prediction Score | 98.57% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known pharmacological information, Iopamidol is a non-ionic, low-osmolality iodinated contrast agent (DrugBank: DB08947). Its molecular structure features an iodinated benzene ring with amide side chains (-CONH-) that confer both water solubility and reduced systemic toxicity compared to earlier ionic contrast media. Its entire clinical utility is derived from its radiodensity properties for anatomical imaging — it does not interact with cell surface receptors, enzymes, or intracellular signalling pathways in a therapeutic sense.

Prinzmetal angina (variant angina) is characterised by episodic coronary artery vasospasm occurring at rest. The pathological core involves dysregulation of vascular smooth muscle calcium channels and impaired nitric oxide (NO) bioavailability. Standard pharmacological management targets calcium channel blockers (e.g., amlodipine, diltiazem) and nitrates. Iopamidol's iodinated benzene ring structure has no known pharmacological intersection with coronary smooth muscle tone, calcium channel gating, or NO synthase activity.

The high TxGNN score (0.986, ranked 6,418 globally) is most plausibly explained by indirect knowledge graph (KG) associations: Iopamidol is routinely used in coronary angiography and cardiac CT, generating dense co-occurrence linkages in biomedical literature with cardiovascular disease nodes — including Prinzmetal angina. This constitutes a **systematic false positive arising from diagnostic context co-occurrence**, not a therapeutic biological signal. The absence of any supporting clinical trial or literature evidence (L5) is consistent with this interpretation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Iopamidol is **not currently registered with SAHPRA** and is not marketed in South Africa. No product licences are on record for this active pharmaceutical ingredient. Healthcare professionals requiring this contrast agent should consult SAHPRA Section 21 authorisation pathways for unregistered medicines if clinical need arises.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. As Iopamidol is not registered in South Africa, consult the originator product's prescribing information for warnings, contraindications, and precautions — including contrast-induced nephropathy risk, hypersensitivity reactions, and restrictions in patients with renal impairment, thyroid disease, or myasthenia gravis. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Iopamidol is a diagnostic radiographic contrast agent with no established therapeutic mechanism of action. The TxGNN prediction for Prinzmetal angina is an L5 signal (model prediction only) with zero supporting clinical trials or publications, consistent with a knowledge graph artefact driven by cardiovascular imaging co-occurrence data rather than any genuine therapeutic biology. The drug is additionally not registered or marketed in South Africa, creating a significant regulatory barrier to any repurposing pathway.

**To proceed, the following is needed:**
- **KG audit:** Determine whether the TxGNN training graph distinguishes diagnostic/imaging exposure from therapeutic intervention — contrast agents may systematically generate false positives across a broad range of disease nodes due to their widespread diagnostic use
- **MOA verification:** Retrieve full pharmacology data from DrugBank API (DG002 remediation) to formally document the absence of therapeutic target engagement
- **Regulatory pathway clarification:** If any repurposing hypothesis for Iopamidol is to be pursued, SAHPRA registration status and Section 21 authorisation requirements must be addressed as a prerequisite
- **Model flag:** Consider tagging Iopamidol and other pure contrast/diagnostic agents in the candidate pipeline as a distinct class requiring separate evaluation criteria before standard repurposing analysis is applied

---

> ⚠️ **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All content should be reviewed by qualified healthcare professionals before informing clinical decisions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

