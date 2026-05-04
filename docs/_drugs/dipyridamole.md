---
layout: default
title: Dipyridamole
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 10
---

# Dipyridamole
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

# Dipyridamole: From Antiplatelet Therapy to Prinzmetal Angina

## One-Sentence Summary

Dipyridamole is a phosphodiesterase inhibitor and adenosine reuptake inhibitor, used internationally as an antiplatelet agent and pharmacological cardiac stress testing adjunct, with no current SAHPRA registration in South Africa.
The TxGNN model predicts a relationship with **Prinzmetal angina** (TxGNN score: 99.99%); however, **⚠️ this is a reverse indication** — available evidence consistently shows that dipyridamole *triggers* coronary vasospasm in variant angina patients rather than treating it.
**15 publications** address this relationship, all within diagnostic or mechanistic contexts with no therapeutic use documented.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in South Africa; internationally used for antiplatelet therapy and pharmacological cardiac stress testing |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacological knowledge, dipyridamole works through two complementary pathways: inhibition of phosphodiesterase (PDE) enzymes raises intracellular cAMP and cGMP levels, while blockade of adenosine reuptake transporters elevates local adenosine concentrations in the coronary microenvironment. Together these actions produce vasodilation and platelet aggregation suppression — the basis of its established use in antiplatelet therapy and cardiac stress testing.

**⚠️ Reverse Indication Warning:** Although TxGNN has identified a high-scoring association with Prinzmetal (variant) angina, the pharmacological reality is the opposite of a therapeutic one. Elevated adenosine concentrations — dipyridamole's primary downstream effect — act on A1 receptors in the coronary vasculature and can *provoke* vasospasm in susceptible patients. PMID 3421166 (1988) explicitly documents that dipyridamole pharmacological stress testing triggered coronary vasospasm in hospitalised variant angina patients, and the episode required intravenous aminophylline (an adenosine antagonist) to terminate. Early data from PMID 633593 (1978) similarly recorded that dipyridamole 50 mg given to Prinzmetal patients did not suppress attacks and that adrenergic blockade tended to aggravate rest angina.

All 15 retrieved publications are framed within diagnostic or mechanistic research contexts — dipyridamole was the stress *inducer*, not the therapeutic agent. This prediction most likely reflects knowledge graph network similarity between vasospastic and ischaemic coronary nodes rather than a genuine repurposing signal, and it carries an active patient safety risk that warrants an immediate Hold.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for dipyridamole as a treatment for Prinzmetal angina.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3421166](https://pubmed.ncbi.nlm.nih.gov/3421166/) | 1988 | Clinical Study | Am J Cardiology | **Critical safety finding:** Dipyridamole stress testing provokes coronary vasospasm in variant angina patients; aminophylline required to reverse the episode |
| [3190956](https://pubmed.ncbi.nlm.nih.gov/3190956/) | 1988 | Clinical Study | British Heart Journal | Short-term reproducibility of exercise testing in patients with ST elevation and different dipyridamole echocardiography responses; diagnostic use only |
| [633593](https://pubmed.ncbi.nlm.nih.gov/633593/) | 1978 | Review | Japanese Circ Journal | Dipyridamole 50 mg administered to Prinzmetal patients did not suppress attacks; propranolol tended to aggravate rest angina |
| [8417062](https://pubmed.ncbi.nlm.nih.gov/8417062/) | 1993 | Clinical Study | JACC | Novel echocardiographic sign of ischaemia: myocardial echodensity changes during dipyridamole-induced ischaemic episodes; mechanistic/diagnostic context |
| [2022043](https://pubmed.ncbi.nlm.nih.gov/2022043/) | 1991 | Review | Circulation | Pathophysiological basis for non-invasive evaluation of coronary stenosis using dipyridamole and other pharmacological stressors |
| [6779029](https://pubmed.ncbi.nlm.nih.gov/6779029/) | 1981 | Diagnostic Study | Japanese Circ Journal | Dipyridamole-loading myocardial imaging for CAD detection: diagnostic sensitivity 66%, improved to 87% combined with exercise |
| [8634169](https://pubmed.ncbi.nlm.nih.gov/8634169/) | 1996 | Clinical Study | Portuguese J Cardiology | Three-year prognosis in suspected CAD patients with normal dipyridamole-thallium scintigraphy; diagnostic prognostication |
| [7628141](https://pubmed.ncbi.nlm.nih.gov/7628141/) | 1995 | Case Report | Clinical Nuclear Medicine | Patient with migraine, asthma, and documented variant angina — dipyridamole used diagnostically with scintigraphic evidence of ischaemia |
| [16630456](https://pubmed.ncbi.nlm.nih.gov/16630456/) | 2006 | Clinical Study | Chinese Cardiovascular Journal | Comparison of clinical features in typical versus atypical coronary artery spasm patients |
| [2221701](https://pubmed.ncbi.nlm.nih.gov/2221701/) | 1990 | Review | Ann NY Acad Sciences | ECG diagnosis of transient myocardial ischaemia: sensitivity, specificity, and practical significance of different detection modalities |

---

## South Africa Market Information

Dipyridamole currently has **no SAHPRA registrations** and is not available on the South African market. No approved product information or SAHPRA-approved PI documents exist in country. Should this drug be considered for any diagnostic use (e.g., pharmacological stress imaging), the responsible prescriber would need to follow an unregistered medicine access pathway and obtain the reference country PI directly from the originator.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Specific safety note for this prediction:** Clinical literature consistently identifies dipyridamole as **contraindicated** in patients with Prinzmetal (variant) angina. The drug can provoke coronary vasospasm through adenosine-mediated mechanisms and must be avoided in this patient population. Whenever dipyridamole is used for pharmacological cardiac stress imaging in any setting, aminophylline must be immediately available as a reversal agent, and patients with known or suspected vasospastic angina must be identified and excluded prior to testing.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This TxGNN prediction represents a pharmacological reverse indication — dipyridamole triggers the pathophysiological mechanism underlying Prinzmetal angina rather than treating it, and no therapeutic evidence exists anywhere in the literature to support this use.

**To proceed, the following is needed:**

- **No further development** of dipyridamole for Prinzmetal angina should be pursued; this finding should be documented as a safety contraindication rather than a repurposing candidate
- If dipyridamole is being evaluated for cardiac stress imaging in South Africa, a formal contraindication screening protocol for vasospastic angina must be established before any unregistered medicine access application is submitted to SAHPRA
- A **separate repurposing evaluation report** should be initiated for the two high-evidence indications identified in this same evidence pack:
  - **Stroke disorder (Rank 2, L1):** 31 clinical trials including multiple completed Phase 3 RCTs; dipyridamole ER + aspirin combination (Aggrenox) has robust secondary prevention evidence
  - **Transient ischemic attack (Rank 5, L1):** 15 clinical trials + 20 publications including Tier-1 meta-analyses (PMID 15569877, 11786451, 34399713) and the ESPRIT Phase 4 trial (n=4,500) — the strongest legitimate repurposing signal in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

