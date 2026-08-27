---
layout: default
title: Morphine
parent: 僅模型預測 (L5)
nav_order: 324
evidence_level: L5
indication_count: 10
---

# Morphine
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

# Morphine: From Moderate-to-Severe Pain to Myofascial Pain Syndrome

## One-Sentence Summary

Morphine is a mu-opioid receptor full agonist classically used for moderate-to-severe pain (analgesia). The TxGNN model predicts it may be effective for **Myofascial Pain Syndrome**, with **33 clinical trials** and **17 publications** identified in the surrounding evidence base — but none of them directly test morphine as a treatment for myofascial pain syndrome itself, so this signal should be read as a mechanistic hypothesis rather than clinical proof.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate-to-severe pain (opioid analgesia) — general pharmacological knowledge; not captured in this Evidence Pack's regulatory data |
| Predicted New Indication | Myofascial Pain Syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this Evidence Pack. Based on general pharmacological knowledge, morphine is a full agonist at the mu-opioid receptor and its efficacy in relieving moderate-to-severe nociceptive pain is well established; mechanistically, broad-spectrum opioid analgesia could plausibly extend to pain arising from myofascial trigger points, since both involve central and peripheral nociceptive signalling.

However, myofascial pain syndrome (MFPS) is a distinct clinical entity driven by localized muscle/fascial trigger points, muscle hyperirritability, and referred pain patterns — a pathophysiology that current first-line treatments (dry needling, trigger point injection, manual therapy, exercise) target directly, rather than through systemic opioid receptor blockade.

The evidence pack itself flags this limitation directly: the TxGNN score most likely reflects morphine's general association with "pain" concepts in the knowledge graph rather than a disease-specific mechanistic link to MFPS. No identified clinical trial or publication tests morphine specifically as an MFPS therapy; the closest direct evidence is a single 2026 RCT using morphine as part of a peri-operative myofascial infiltration mixture, which is a narrow surgical-anaesthesia context rather than support for treating MFPS as a standalone condition.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06955923](https://clinicaltrials.gov/study/NCT06955923) | Phase 2 | Completed | 11 | Trigger point injections after total knee arthroplasty reduced pain scores/opioid use vs. sham; supports the MFPS-opioid interplay but did not test morphine directly. |
| [NCT07413770](https://clinicaltrials.gov/study/NCT07413770) | NA | Recruiting | 60 | Classical massage (alone or with physiotherapy) evaluated for pain, muscle sensitivity, and quality of life in MFPS patients; non-pharmacological. |
| [NCT05478928](https://clinicaltrials.gov/study/NCT05478928) | NA | Unknown | 60 | Compares invasive techniques (percutaneous microelectrolysis, dry needling) for myofascial trigger points using algometry; no opioid arm. |
| [NCT04640896](https://clinicaltrials.gov/study/NCT04640896) | Phase 4 | Recruiting | 60 | Trigger point injections vs. traditional therapy for post-surgical cervical myofascial pain after anterior cervical surgery; non-opioid comparator. |
| [NCT04684784](https://clinicaltrials.gov/study/NCT04684784) | NA | Completed | 46 | Dry needling effect on EMG activity at latent myofascial trigger points; no drug arm. |
| [NCT03813485](https://clinicaltrials.gov/study/NCT03813485) | NA | Unknown | 24 | EMG comparison of dry needling at latent trigger points in tonic vs. phasic trapezius fibers; no drug arm. |
| [NCT00580294](https://clinicaltrials.gov/study/NCT00580294) | NA | Completed | 12 | Pilot study of rapid rotation from morphine/oxycodone to oxymorphone; not MFPS-specific. |
| [NCT01878019](https://clinicaltrials.gov/study/NCT01878019) | N/A | Completed | 92 | Naloxone (a morphine antagonist) used to probe brain pain responses in chronic pain patients; mechanistic tool study, not MFPS-specific. |
| [NCT05069363](https://clinicaltrials.gov/study/NCT05069363) | NA | Recruiting | 20 | Feasibility trial of whole-body photobiomodulation for chronic pain; references morphine among current standard treatments but does not test it. |
| [NCT06179199](https://clinicaltrials.gov/study/NCT06179199) | NA | Not yet recruiting | 40 | Evaluates tDCS analgesia in sedated ICU patients, citing side effects of excessive morphine use as rationale; not an MFPS trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41664327](https://pubmed.ncbi.nlm.nih.gov/41664327/) | 2026 | RCT | Asian Spine Journal | Double-blind RCT comparing dexmedetomidine + morphine vs. plain ropivacaine for myofascial infiltration in thoracolumbar spinal fusion — the most direct morphine + myofascial evidence found, but limited to peri-operative infiltration. |
| [35066974](https://pubmed.ncbi.nlm.nih.gov/35066974/) | 2022 | Cohort | Pain Practice | Retrospective cohort: a structured stretching program resolved myofascial pain and reduced opioid usage in "legacy pain" patients — an opioid-*reduction* outcome, not opioid efficacy evidence. |
| [22648287](https://pubmed.ncbi.nlm.nih.gov/22648287/) | 2012 | Cohort | Journal of Anesthesia | Cervical facet joint injections added to a multimodal program improved long-standing cervical MFPS; opioids were not the primary intervention studied. |
| [21419546](https://pubmed.ncbi.nlm.nih.gov/21419546/) | 2011 | Review | J Oral Maxillofac Surg | Reviews long-term opioid use in chronic temporomandibular joint dysfunction; evidence "neither supports nor refutes" opioid use in this myofascial-adjacent condition. |
| [39793344](https://pubmed.ncbi.nlm.nih.gov/39793344/) | 2025 | Case series | Eur J Obstet Gynecol Reprod Biol | Pudendal nerve block after botulinum toxin injection for myofascial pelvic pain; no morphine arm. |
| [20390305](https://pubmed.ncbi.nlm.nih.gov/20390305/) | 2010 | Observational | Schmerz | Altered pain thresholds during and after opioid withdrawal in chronic low back pain patients on long-term opioid therapy. |
| [16713811](https://pubmed.ncbi.nlm.nih.gov/16713811/) | 2006 | Case series | J Oral Maxillofac Surg | TMJ arthrocentesis followed by intra-articular morphine infusion for refractory TMJ pain — direct morphine use, but in a TMJ/intra-articular context rather than systemic MFPS. |
| [17870625](https://pubmed.ncbi.nlm.nih.gov/17870625/) | 2008 | RCT | European Journal of Pain | Compares epidural analgesia vs. intercostal cryoanalgesia for post-thoracotomy pain; morphine used as part of the epidural comparator regimen. |
| [21691691](https://pubmed.ncbi.nlm.nih.gov/21691691/) | 2011 | Descriptive | Rev Assoc Med Bras | Descriptive study of therapeutic approaches in 56 patients with failed back surgery pain syndrome. |
| [9214190](https://pubmed.ncbi.nlm.nih.gov/9214190/) | 1997 | Clinical study | Zh Nevrol Psikhiatr | Combined analgesic (caffetin) evaluated for acute cervicalgia/lumbar sciatica; not morphine-specific. |

---

## South Africa Market Information

No SAHPRA registrations for Morphine are recorded in this Evidence Pack (market status: **Not marketed**, 0 licenses on file). This does not necessarily reflect real-world availability of morphine formulations in South Africa — it reflects a data gap in the source dataset used to build this pack (see Conclusion below).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No clinical trial or publication in this pack directly tests morphine as a treatment for myofascial pain syndrome; the strongest available evidence (a 2026 RCT) only covers morphine as part of a peri-operative infiltration mixture, not systemic MFPS management. Evidence level is L4 (mechanism/rationale only), and the underlying mechanistic link is judged weak — likely a broad "pain" association in the knowledge graph rather than an MFPS-specific effect.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings, contraindications) — currently a **blocking** data gap that prevents any safety (S1) evaluation
- Confirmed mechanism-of-action data from DrugBank or equivalent source
- A dedicated study of morphine (or an opioid class effect) specifically in an MFPS population, ideally against first-line non-opioid comparators (dry needling, trigger point injection, physiotherapy)
- Given morphine's status as a controlled substance, a formal opioid risk-benefit assessment before considering use in a non-cancer, non-life-threatening chronic pain condition such as MFPS
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

