---
layout: default
title: Iron
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 6
---

# Iron
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Iron: From Iron Deficiency Anaemia to Plummer-Vinson Syndrome

## One-Sentence Summary

Iron is an essential micronutrient supplement universally administered to correct iron deficiency anaemia. The TxGNN model's most clinically actionable prediction — **Plummer-Vinson Syndrome (PVS)** — identifies iron supplementation as a causal intervention for this rare condition characterised by the triad of dysphagia, iron deficiency anaemia, and esophageal webs, with **no registered clinical trials** but **19 publications** consistently supporting iron repletion as the standard treatment.

> **Analyst note:** The highest-ranked TxGNN prediction (Rank 1: vitamin B12- and folate-independent constitutional megaloblastic anaemia, score 99.89%) is assessed as a likely knowledge-graph artefact arising from broad "anaemia" node proximity, with no mechanistic basis and zero supporting evidence (Evidence Level: L5, Recommendation: Hold). This report therefore focuses on **Rank 2: Plummer-Vinson Syndrome**, which carries a direct causal mechanistic link, a strong literature base, and a "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Iron deficiency anaemia (no SAHPRA-registered indication on record for this entry) |
| Predicted New Indication | Plummer-Vinson Syndrome |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Iron deficiency is not merely a risk factor for Plummer-Vinson syndrome — it is its primary aetiological driver. Chronic iron deficiency impairs the activity of iron-dependent enzymes, notably cytochrome oxidase and myeloperoxidase, within the mucosal lining of the upper gastrointestinal tract. This enzymatic dysfunction causes progressive atrophy of the post-cricoid esophageal epithelium and the formation of thin, eccentric mucosal webs that partially occlude the esophageal lumen, producing the painless, progressive dysphagia that defines the syndrome.

Iron supplementation directly reverses this pathophysiological cascade. Published case series and clinical reviews consistently demonstrate that adequate iron repletion corrects the underlying anaemia and, in the majority of patients, results in spontaneous regression of esophageal webs — often resolving dysphagia without requiring endoscopic dilatation or surgical intervention. This is therefore a **causal, aetiological treatment** rather than a conventional drug repurposing scenario. Mechanistic data for the specific DrugBank entry (DB01592) are not available in this evidence pack, but the biological rationale is well established in the broader haematological and gastroenterological literature.

The TxGNN model's high prediction score (99.89%) accurately captures the strong biological connection between iron metabolism and PVS within the knowledge graph. The evidence level (L3) reflects the nature of the available literature — predominantly case reports, case series, and expert reviews — which is entirely consistent with the rare-disease epidemiology of PVS, for which prospective randomised trials are neither ethically feasible nor practically viable given that iron therapy is already the accepted standard of care.

---

## Clinical Trial Evidence

No registered clinical trials specifically investigating iron supplementation for Plummer-Vinson syndrome were identified in ClinicalTrials.gov or the WHO ICTRP registry.

> Currently no related clinical trials registered for this indication.

The absence of formal trial registration is expected and does not diminish clinical confidence: PVS is sufficiently rare, and iron supplementation is sufficiently well-established, that a placebo-controlled trial would be ethically unjustifiable.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [29089792](https://pubmed.ncbi.nlm.nih.gov/29089792/) | 2017 | Narrative Review | Journal of Blood Medicine | Comprehensive review of PVS; iron deficiency anaemia is the central mechanism; iron supplementation resolves anaemia and often promotes esophageal web regression, relieving dysphagia |
| [16978405](https://pubmed.ncbi.nlm.nih.gov/16978405/) | 2006 | Review | Orphanet Journal of Rare Diseases | Detailed disease overview confirming iron deficiency as primary aetiology; iron therapy described as first-line treatment; prevalence declining globally due to improved nutrition |
| [38871147](https://pubmed.ncbi.nlm.nih.gov/38871147/) | 2024 | Review/Case Series | Clinical Gastroenterology and Hepatology | Reaffirms the classic diagnostic triad; iron repletion is the cornerstone of management alongside endoscopic dilatation when dysphagia persists |
| [31417270](https://pubmed.ncbi.nlm.nih.gov/31417270/) | 2019 | Review | Journal of Multidisciplinary Healthcare | Advocates multidisciplinary management; iron supplementation central to treatment; highlights risk of postcricoid carcinoma requiring long-term endoscopic surveillance |
| [12823219](https://pubmed.ncbi.nlm.nih.gov/12823219/) | 2003 | Case Report | Diseases of the Esophagus | Two middle-aged women with confirmed PVS (dysphagia, sideropenia, esophageal webs); iron supplementation alone eliminated symptoms in both cases |
| [7575056](https://pubmed.ncbi.nlm.nih.gov/7575056/) | 1995 | Case Report & Review | Archives of Internal Medicine | PVS case with supporting literature review; iron repletion frequently improves or resolves dysphagia; surveillance endoscopy recommended due to postcricoid carcinoma association |
| [34651287](https://pubmed.ncbi.nlm.nih.gov/34651287/) | 2022 | Case-based Review | Immunologic Research | PVS complicating Sjögren syndrome; systematic review of the rare association; iron deficiency confirmed as the shared pathological mechanism; iron therapy as therapeutic cornerstone |
| [38034443](https://pubmed.ncbi.nlm.nih.gov/38034443/) | 2023 | Case Report | JPGN Reports | PVS diagnosed in a 4-year-old child; treated with iron supplementation combined with endoscopic balloon dilatation with successful resolution of dysphagia |
| [41756818](https://pubmed.ncbi.nlm.nih.gov/41756818/) | 2026 | Case Report | Case Reports in Hematology | 26-year-old Ghanaian woman with 5-year progressive dysphagia and chronic iron deficiency; PVS confirmed; managed with iron supplementation — notable case from the African continent |
| [7865729](https://pubmed.ncbi.nlm.nih.gov/7865729/) | 1994 | Historical Review | Journal of Gastroenterology and Hepatology | Reviews the global decline in PVS incidence, attributed to improved nutritional status and dietary iron intake; supports the causal role of iron deficiency in disease development |

---

## South Africa Market Information

Iron (DrugBank ID: DB01592) has **no SAHPRA-registered products** recorded under this entry.

> **Important note for practitioners:** This evidence pack entry does not capture the full landscape of iron products available in South Africa. Numerous iron formulations — including ferrous sulphate, ferric carboxymaltose (Ferinject®), iron polymaltose (Ferremed®), and iron isomaltoside — are registered with SAHPRA under their specific compound names. Oral iron preparations (e.g., ferrous sulphate 200 mg) appear on the **Essential Medicines List (EML)** for primary-level healthcare facilities for treatment of iron deficiency anaemia. Clinicians should consult the SAHPRA online product database to identify the specific registered formulation most appropriate for route, dose, and clinical setting.

---

## Safety Considerations

Formal product-level safety data for this DrugBank entry are not available in this evidence pack.

> Please refer to the SAHPRA-approved Professional Information (PI) for the specific iron formulation being prescribed. Report suspected adverse drug reactions to SAHPRA's pharmacovigilance programme (ADR reporting portal).

**Known clinical safety considerations for iron supplementation:**

- **Gastrointestinal effects:** Nausea, epigastric discomfort, constipation, and dark stools are common with oral preparations; taking iron with food or switching formulation may improve tolerability
- **Intravenous iron:** Risk of hypersensitivity and anaphylaxis (particularly with older preparations); administer in a setting equipped for resuscitation and observe for at least 30 minutes after infusion
- **Iron overload:** Avoid in haemochromatosis, haemosiderosis, or haemolytic anaemia not associated with iron deficiency; monitor serum ferritin to guide duration of therapy
- **Interactions:** Tetracyclines, fluoroquinolones, levothyroxine, and calcium-containing preparations reduce iron absorption; separate administration by at least 2 hours

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Iron supplementation for Plummer-Vinson syndrome is mechanistically unambiguous and supported by a consistent body of published clinical evidence demonstrating resolution of both anaemia and esophageal web formation following adequate iron repletion. Although no randomised controlled trials exist — a reflection of the syndrome's rarity and the ethical impracticability of withholding treatment — the causal link is clinically and biologically established across multiple independent publications spanning three decades.

**To proceed, the following is needed:**

- Confirm the diagnosis of Plummer-Vinson syndrome with barium swallow or upper endoscopy before attributing dysphagia to iron deficiency; exclude other structural and motility causes
- Identify and prescribe a SAHPRA-registered iron formulation appropriate to the route, severity of deficiency, and patient tolerability (oral vs. intravenous)
- Investigate and address the underlying aetiology of iron deficiency (dietary insufficiency, menorrhagia, malabsorption, chronic gastrointestinal blood loss) — iron therapy will fail to produce durable benefit without treating the root cause
- Establish a structured monitoring plan: full blood count (FBC), serum ferritin, and transferrin saturation at baseline, 3 months, and 6 months post-initiation
- Endoscopic reassessment at 3–6 months to evaluate esophageal web regression; if dysphagia persists despite normalisation of iron stores, proceed to endoscopic balloon dilatation or bougie dilatation
- Implement long-term endoscopic surveillance given the well-documented association of PVS with postcricoid (hypopharyngeal) carcinoma; current literature recommends ongoing follow-up even after clinical resolution

---

*This report is generated for research reference purposes only. Drug repurposing candidates require clinical validation before therapeutic application. All prescribing decisions should be guided by registered product information and current South African clinical practice guidelines.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

