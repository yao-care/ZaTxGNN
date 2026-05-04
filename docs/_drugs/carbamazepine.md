---
layout: default
title: Carbamazepine
parent: 僅模型預測 (L5)
nav_order: 97
evidence_level: L5
indication_count: 10
---

# Carbamazepine
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

# Carbamazepine: From Epilepsy & Trigeminal Neuralgia to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Carbamazepine (CBZ) is a well-established sodium channel-blocking drug internationally recognised for epilepsy, trigeminal neuralgia, and bipolar disorder — although no current SAHPRA registration data was retrieved in this Evidence Pack.
The TxGNN model predicts it may be effective for **Trigeminal Nerve Neoplasm** (specifically, management of neoplasm-induced trigeminal pain),
with **1 clinical trial** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No SAHPRA registration data on record; internationally approved for epilepsy and trigeminal neuralgia |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L3 |
| South Africa Market Status | Not marketed (no SAHPRA registration retrieved) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this Evidence Pack. Based on established pharmacological knowledge, carbamazepine blocks voltage-gated sodium channels (Nav1.2/Nav1.6), stabilising the inactivated state of neuronal sodium channels and suppressing high-frequency repetitive neuronal firing. This is precisely the mechanism underlying its internationally recognised first-line role in trigeminal neuralgia — the paroxysmal, electric shock-like facial pain arising from the trigeminal nerve distribution.

The predicted new indication — **trigeminal nerve neoplasm** — encompasses a range of tumours (schwannomas, primary lymphomas, meningiomas, sarcoid granulomas, lipomas, dermoid cysts, and rare malignancies such as melanoma) that compress or infiltrate the trigeminal nerve, frequently causing secondary trigeminal neuralgia as the presenting symptom. The biological rationale is mechanistically coherent: neoplastic compression or nerve infiltration generates ectopic neuronal discharges along the trigeminal nerve trunk, and CBZ's sodium channel blockade can suppress these aberrant high-frequency discharges to provide meaningful pain relief — particularly when the underlying tumour is not immediately amenable to surgery, or when bridging symptom control is required pre-operatively.

It is important to note that CBZ is proposed here for **symptomatic pain management** in trigeminal nerve neoplasms, not as an oncological treatment of the tumour itself. Multiple case reports in the retrieved literature document CBZ being initiated as first-line symptomatic therapy in patients subsequently confirmed to have trigeminal nerve tumours. A critical clinical implication runs in both directions: failure of CBZ to control presumed trigeminal neuralgia should prompt urgent neuroimaging to exclude an underlying neoplasm; conversely, once a neoplasm is confirmed, CBZ may serve a legitimate palliative analgesic role alongside definitive tumour management.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT06853119](https://clinicaltrials.gov/study/NCT06853119) | N/A | Not Yet Recruiting | 120 | MRI-based observational study examining brain network dynamics, microstructural changes, and blood-brain barrier integrity in trigeminal neuralgia patients. Not a CBZ intervention trial. Provides background on neural plasticity in trigeminal nerve conditions that may apply to neoplasm-related neuralgia. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36824641](https://pubmed.ncbi.nlm.nih.gov/36824641/) | 2022 | Review | Acta Clinica Croatica | Comprehensive review of trigeminal neuralgia treatment options; explicitly notes that TN can be caused by vascular compression **or a tumour process**; CBZ discussed as the primary medical treatment across both aetiologies |
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Review of Neurotherapeutics | Detailed review of the TN treatment landscape; discusses focal demyelination and aberrant neural discharge as the shared mechanism in vascular- and mass-related TN; positions CBZ as central to medical management |
| [11286444](https://pubmed.ncbi.nlm.nih.gov/11286444/) | 2001 | Clinical Survey | British Journal of Oral & Maxillofacial Surgery | Survey of 254 oral and maxillofacial surgeons on TN management; specifically addresses the need to screen for **secondary trigeminal neuralgia** (tumour-related) and CBZ therapeutic drug monitoring in practice |
| [30741017](https://pubmed.ncbi.nlm.nih.gov/30741017/) | 2023 | Case Report | British Journal of Neurosurgery | Primary malignant lymphoma of the trigeminal nerve presenting as unilateral facial pain; CBZ was prescribed initially but did not improve symptoms; subsequent MRI revealed nerve swelling and a Meckel's cave mass — illustrates that CBZ failure should trigger urgent imaging to exclude neoplasm |
| [9109911](https://pubmed.ncbi.nlm.nih.gov/9109911/) | 1997 | Case Report | Neurology | Post-irradiation neuromyotonia in bilateral facial and trigeminal nerve distribution — a radiation-induced nerve injury model; patient responded to CBZ therapy; demonstrates CBZ efficacy in structurally damaged trigeminal nerve conditions |
| [22647513](https://pubmed.ncbi.nlm.nih.gov/22647513/) | 2012 | Case Report | No Shinkei Geka (Neurological Surgery) | Combined glossopharyngeal and trigeminal neuralgia caused by vascular compression; CBZ described as standard first-line medical treatment for cranial neuralgias, with microvascular decompression reserved for CBZ failure |
| [3181365](https://pubmed.ncbi.nlm.nih.gov/3181365/) | 1988 | Experimental | Experimental Neurology | IV carbamazepine produced immediate, dose-dependent inhibition of spontaneous ectopic discharges from experimental neuromas in rats — provides direct mechanistic evidence that CBZ suppresses peripheral nerve injury-related aberrant firing, analogous to neoplasm-induced nerve compression |
| [25433061](https://pubmed.ncbi.nlm.nih.gov/25433061/) | 2014 | Case Report | No Shinkei Geka (Neurological Surgery) | Trigeminal neuralgia caused by cerebellopontine angle lipoma; CBZ initiated but pain control was inadequate due to side effects; surgical resection ultimately required — illustrates CBZ as symptomatic bridge therapy pending definitive tumour treatment |
| [25968963](https://pubmed.ncbi.nlm.nih.gov/25968963/) | 2015 | Case Report + Review | World Neurosurgery | Trigeminal neuralgia secondary to venous angioma; reviews ectopic neural conduction pathophysiology applicable to any mass lesion compressing the trigeminal root; CBZ incorporated in management plan |
| [15235745](https://pubmed.ncbi.nlm.nih.gov/15235745/) | 2004 | Case Report | Arquivos de Neuro-psiquiatria | Primary melanoma of Meckel's cave with initial normal MRI; CBZ and microvascular decompression surgery both failed to relieve pain; repeat MRI revealed expansive lesion — underscores the clinical imperative that unresponsive trigeminal pain must prompt re-imaging to detect malignant neoplasm |

---

## South Africa Market Information

Carbamazepine has **no SAHPRA product registrations on record** in this Evidence Pack. However, carbamazepine is included on the **South African Essential Medicines List (EML)** for both primary healthcare and hospital level, and is widely used within the public health sector. The absence of retrieved registration records likely reflects a data gap in the evidence collection process rather than actual unavailability. Healthcare professionals should verify the current registration status and approved indications directly with SAHPRA before prescribing in a new indication context.

---

## Safety Considerations

No SAHPRA-specific safety data was available in this Evidence Pack. Key safety information well-established from international prescribing information includes:

- **Serious dermatological reactions**: Stevens-Johnson Syndrome (SJS) and Toxic Epidermal Necrolysis (TEN) are rare but life-threatening; strongly associated with the **HLA-B\*15:02 allele**, which has higher prevalence in certain Asian and some African population groups — pharmacogenomic screening is recommended before initiating CBZ in at-risk populations
- **Enzyme induction**: CBZ is a potent inducer of CYP3A4 and other cytochrome P450 enzymes, leading to numerous clinically significant drug-drug interactions; careful medication reconciliation is essential
- **Haematological effects**: Aplastic anaemia and agranulocytosis have been reported (rare); routine full blood count monitoring is advised
- **Hyponatraemia**: Syndrome of inappropriate antidiuretic hormone secretion (SIADH) can occur, particularly in elderly patients

Please refer to the internationally recognised prescribing information (e.g., manufacturer's Professional Information) for the full safety profile. Report any adverse drug reactions to **SAHPRA** using the MedSafety reporting system.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between CBZ's sodium channel blockade and the suppression of ectopic trigeminal nerve discharges caused by neoplastic compression or infiltration is pharmacologically sound, and is corroborated by multiple case reports, clinical surveys, and treatment reviews (L3 evidence). CBZ is already internationally established for trigeminal neuralgia of all aetiologies, including tumour-related secondary neuralgia. The clinical application in trigeminal nerve neoplasm is for **symptomatic pain management**, not oncological tumour treatment — this distinction must be clearly communicated to patients and documented in the clinical record.

**To proceed, the following is needed:**

- **Confirm SAHPRA registration status**: Verify current registration details with SAHPRA directly, given the discrepancy between EML inclusion and absence of registration records in this data pack
- **Clarify indication scope**: Ensure all prescribing documentation specifies that CBZ is being used for *symptomatic management of trigeminal neuralgia secondary to trigeminal nerve neoplasm*, not as antineoplastic therapy
- **Mandatory pre-treatment neuroimaging**: MRI with gadolinium enhancement of the posterior fossa and Meckel's cave must be performed prior to CBZ initiation for any new presentation of trigeminal pain, to identify or exclude an underlying neoplasm requiring definitive management
- **Pharmacogenomic screening**: Consider HLA-B*15:02 screening in eligible patient populations prior to initiating CBZ to mitigate risk of severe cutaneous adverse reactions
- **Mechanism of action data**: Obtain formal DrugBank MOA data (Data Gap DG002) to strengthen the mechanistic rationale documentation
- **Prospective outcomes tracking**: Establish a clinical registry or structured case series documenting CBZ response rates, time to pain control, and safety events in patients with confirmed trigeminal nerve neoplasms in the South African clinical context
- **Multidisciplinary review**: Management decisions should involve neurosurgery, neurology, and oncology given the dual nature of the condition (neoplasm + neuropathic pain)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

