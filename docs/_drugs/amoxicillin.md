---
layout: default
title: Amoxicillin
parent: 僅模型預測 (L5)
nav_order: 35
evidence_level: L5
indication_count: 10
---

# Amoxicillin
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

# Amoxicillin: From Bacterial Infections to Epiglottitis — 10-Indication Repurposing Screen

## One-Sentence Summary

Amoxicillin is a broad-spectrum beta-lactam antibiotic that inhibits bacterial cell wall synthesis, widely used as first-line therapy for susceptible gram-positive and gram-negative bacterial infections.
The TxGNN model generated **10 predicted new indications**; the strongest evidence supports **epiglottitis** (Evidence Level L3, 15 publications including three clinical practice guidelines and a prospective paediatric study), while **immunoproliferative small intestinal disease (IPSID)** — a distinct subtype of monoclonal gammopathy — presents a biologically plausible antibiotic-responsive mechanistic pathway supported by case-level literature.
The remaining 8 predicted indications are unsupported by clinical or mechanistic evidence and are all classified as **Hold**; one (congenital haematological disorder) carries an active **safety counter-signal**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum bacterial infections (beta-lactam antibiotic class) |
| Lead Predicted Indication | Epiglottitis |
| TxGNN Prediction Score (Epiglottitis) | 98.70% |
| Evidence Level | L3 — Clinical practice guidelines and observational studies |
| South Africa Market Status | Not retrieved — likely data gap (see note below) |
| Number of SAHPRA Registrations | 0 retrieved — probable data retrieval failure |
| Recommended Decision | **Proceed with Guardrails** (epiglottitis) · **Research Question** (IPSID/monoclonal gammopathy) · **Hold** (remaining 8) |

> **⚠ Data Note — SAHPRA Registration**: This analysis returned zero SAHPRA records for amoxicillin, which is almost certainly a data retrieval failure. Amoxicillin is a WHO Essential Medicine (EML Section 6.2.1), appears on South Africa's National Essential Medicines List in multiple formulations, and is one of the most widely prescribed antibiotics in South African primary healthcare. Clinicians should verify current registration status directly via the [SAHPRA website](https://www.sahpra.org.za/).

---

## All 10 Predicted Indications — Evaluation Summary

| Rank | Indication | TxGNN Score | Evidence Level | Decision | Key Rationale |
|------|-----------|------------|---------------|---------|--------------|
| 1 | Polyclonal hyperviscosity syndrome | 99.63% | L5 | **Hold** | No mechanistic link; elevated IgM is caused by autoimmune/infectious triggers, not treatable with antibiotics; likely KG model noise |
| 2 | Hyperamylasemia | 99.63% | L5 | **Hold** | Amoxicillin can *induce* drug-related pancreatitis → amylase elevation; reverse causality risk |
| 3 | Congenital analbuminemia | 99.59% | L5 | **Hold** | Autosomal recessive *ALB* gene mutation; antibiotics cannot restore albumin synthesis |
| 4 | Blood group incompatibility | 99.40% | L5 | **Hold** | Antibody-mediated haemolysis; one retrieved publication describes incidental infection management, not treatment of incompatibility |
| 5 | Premalignant haematological disease | 99.29% | L5 | **Hold** | No evidence; clonal haematopoietic mutations are not bacterially driven |
| 6 | Monoclonal gammopathy | 99.22% | L4 | **Research Question** | IPSID subtype (Mediterranean lymphoma) has established antibiotic-response mechanism via *C. jejuni* / *H. pylori* eradication |
| 7 | Haematological disease + peripheral neuropathy | 99.14% | L5 | **Hold** | Paraprotein-mediated nerve damage (POEMS, AL amyloid); no antibiotic mechanism applicable |
| 8 | Septicemic plague | 99.13% | L4 | **Hold** | *Y. pestis* has intrinsic chromosomal beta-lactamase; amoxicillin not recommended in any plague guideline; treatment failure = high mortality |
| 9 | Congenital haematological disorder | 98.70% | L4 | **Hold** | **Safety counter-signal**: amoxicillin induced haemolytic anaemia in a child with G6PI deficiency (PMID 20516363) |
| **10** | **Epiglottitis** | **98.70%** | **L3** | **Proceed with Guardrails** | Multiple ENT clinical guidelines support amoxicillin-clavulanate; prospective paediatric study in 24 epiglottitis cases confirms efficacy |

---

## Why is This Prediction Reasonable?

### Epiglottitis (Lead Indication — L3)

Amoxicillin's mechanism of action is directly relevant to epiglottitis. As a beta-lactam, amoxicillin binds irreversibly to penicillin-binding proteins (PBP 1A and PBP 2X), inhibiting transpeptidation of bacterial peptidoglycan and triggering osmotic lysis. This bactericidal mechanism is precisely matched to the principal pathogens driving acute epiglottitis: *Haemophilus influenzae* type b (Hib) in children, and *Streptococcus pneumoniae* and Group A Streptococcus in adults — all gram-positive or gram-negative organisms within amoxicillin's coverage spectrum.

The relationship between amoxicillin's established use in upper respiratory bacterial infections and epiglottitis is straightforward: epiglottitis is itself a severe bacterial upper airway infection, representing an extension of the drug's core therapeutic territory rather than a mechanistic leap. This explains the biological plausibility of the TxGNN prediction. The addition of clavulanate (forming co-amoxiclav / amoxicillin-clavulanate) extends coverage to beta-lactamase-producing strains of *H. influenzae*, which is particularly important following the shift in adult epiglottitis pathogen distribution after widespread Hib vaccination.

Three key clinical limitations must be observed: (1) in severe epiglottitis with airway compromise, parenteral antibiotics and emergency airway management take precedence over oral amoxicillin; (2) since Hib vaccination has altered the adult pathogen profile, local antibiogram data should guide empiric therapy; and (3) in clinically suspected beta-lactamase-producing infections, co-amoxiclav rather than amoxicillin alone is appropriate.

### Monoclonal Gammopathy / IPSID (Research Question — L4)

There is a specific and clinically meaningful mechanistic pathway for **Immunoproliferative Small Intestinal Disease (IPSID)** — also known as Mediterranean lymphoma or alpha heavy chain disease — a rare extranodal marginal zone B-cell lymphoma closely associated with chronic intestinal infection by *Campylobacter jejuni* and, in some reports, *Helicobacter pylori*. The mechanism mirrors the now-established model of gastric MALT lymphoma responding to H. pylori eradication: chronic antigenic stimulation by the bacterium drives polyclonal and then monoclonal B-cell expansion; removing the antigen source by antibiotic eradication allows immune regression of the early-stage lymphoproliferative lesion.

Early-stage IPSID (Stage A) has been documented in case series and published case reports to achieve durable remission with broad-spectrum antibiotics including ampicillin/amoxicillin and tetracyclines (PMID 9030995; PMID 20300878; PMID 8988128). This represents an underrecognised but real biological rationale. **Critical caveat**: this mechanism applies exclusively to IPSID, a rare and geographically clustered condition (historically prevalent in Middle East, Mediterranean, and parts of Africa). It does not apply to MGUS, Waldenström's macroglobulinaemia, or multiple myeloma — other entities classified under "monoclonal gammopathy" in the knowledge graph.

> **MOA data status**: Detailed mechanism of action data was not retrieved from DrugBank for this candidate. The above mechanistic description is based on established pharmacological knowledge of the beta-lactam class and information present in the Evidence Pack's repurposing rationale fields.

---

## Clinical Trial Evidence

### Epiglottitis
No clinical trials specifically investigating amoxicillin or co-amoxiclav for epiglottitis were identified in ClinicalTrials.gov or ICTRP at the time of data collection.

### Monoclonal Gammopathy (Low Relevance)

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|----------|-------------|
| [NCT00062231](https://clinicaltrials.gov/study/NCT00062231) | NA | Terminated | 351 | Compared moxifloxacin monotherapy vs. ciprofloxacin + amoxicillin-clavulanate for fever in low-risk neutropenic cancer patients. Population included various haematological malignancies; however, the study objective was empirical infection management — **not** treatment of monoclonal gammopathy itself. Trial was terminated before completing its enrolment target. Relevance to repurposing: very low. |

---

## Literature Evidence

### Epiglottitis

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [37730165](https://pubmed.ncbi.nlm.nih.gov/37730165/) | 2023 | Clinical Practice Guideline | *Infectious Diseases Now* | French ENT antimicrobial treatment guidelines; specifies antibiotic selection for bacterial upper respiratory infections including epiglottitis, supporting amoxicillin-based regimens where appropriate |
| [29290238](https://pubmed.ncbi.nlm.nih.gov/29290238/) | 2017 | Clinical Practice Guideline | *Archives de Pédiatrie* | French paediatric ENT infection guidelines; outlines antibiotic decision pathways for epiglottitis and other upper respiratory infections in children |
| [26332822](https://pubmed.ncbi.nlm.nih.gov/26332822/) | 2015 | Clinical Practice Guideline | *Nederlands Tijdschrift voor Geneeskunde* | Dutch GP guideline revision for acute sore throat; contextualises epiglottitis in differential diagnosis and treatment strategy |
| [3571053](https://pubmed.ncbi.nlm.nih.gov/3571053/) | 1987 | Prospective Clinical Study | *J Antimicrobial Chemotherapy* | Sequential IV-oral amoxicillin-clavulanate in 71 hospitalised children; **24 patients had acute epiglottitis** — efficacy and safety directly demonstrated; moderate-to-severe disease included |
| [10893774](https://pubmed.ncbi.nlm.nih.gov/10893774/) | 2000 | Review | *Anales de Medicina Interna* | Comprehensive review of *H. influenzae* infections including epiglottitis; antibiotic susceptibility data relevant to amoxicillin coverage |
| [17334726](https://pubmed.ncbi.nlm.nih.gov/17334726/) | 2007 | Retrospective Cohort | *J Infection and Chemotherapy* | 52 children with invasive *H. influenzae* in Japan; epiglottitis in 4 cases (7.7%); antibiotic susceptibility and MIC data |
| [15960127](https://pubmed.ncbi.nlm.nih.gov/15960127/) | 2005 | Case Report | *Acta Otorrinolaringológica Española* | Base-of-tongue actinomycosis with epiglottis involvement; complete disease resolution with surgical drainage followed by oral amoxicillin therapy |
| [8322095](https://pubmed.ncbi.nlm.nih.gov/8322095/) | 1993 | Case Report | *Southern Medical Journal* | Acute epiglottitis in pregnancy caused by *Staphylococcus aureus*; reviews antibiotic management principles for this life-threatening condition |

### Monoclonal Gammopathy — IPSID Subtype

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [9030995](https://pubmed.ncbi.nlm.nih.gov/9030995/) | 1996 | Case Series | *Internal Medicine (Tokyo)* | Mediterranean lymphoma (IPSID/alpha heavy chain disease) treated with antibiotics; duodenal IPSID with elevated IgA achieved clinical remission — supports antibiotic-driven regression model |
| [20300878](https://pubmed.ncbi.nlm.nih.gov/20300878/) | 2010 | Case Report | *J Gastrointestinal Cancer* | 20-year-old male with extensive proximal small-bowel IPSID; achieved regression following *H. pylori* eradication therapy; confirms infection-driven pathogenesis |
| [8988128](https://pubmed.ncbi.nlm.nih.gov/8988128/) | 1997 | Case Report | *Lancet* | Published in *Lancet*: early report of IPSID regression after *H. pylori* eradication; landmark case supporting antibiotic-responsive monoclonal lymphoproliferation |
| [16253033](https://pubmed.ncbi.nlm.nih.gov/16253033/) | 2005 | Case Report | *Archives of Pathology & Laboratory Medicine* | Nonsecretory IPSID variant in a 19-year-old woman; pathological and immunophenotypic characterisation; describes features relevant to identifying antibiotic-eligible patients |

---

## South Africa Market Information

SAHPRA registration data was **not retrieved** for Amoxicillin in this data pull (0 records returned). Based on publicly available information, amoxicillin is expected to have multiple SAHPRA registrations across oral and parenteral formulations and **appears on the South African National Essential Medicines List (NEML)**. This data gap should be resolved before any procurement or formulary decisions are made.

| Action Required | Detail |
|----------------|--------|
| Verify SAHPRA registration | Search registered medicines at [www.sahpra.org.za](https://www.sahpra.org.za/) |
| Confirm EML listing | Check the current National EML — amoxicillin (oral) is expected to be listed |
| Obtain current PI | Download SAHPRA-approved Professional Information for local dosing, safety, and contraindication guidance |

---

## Safety Considerations

Detailed SAHPRA-specific safety data was not retrieved for this candidate. Please refer to the **SAHPRA-approved Professional Information (PI)** for complete warnings, contraindications, and drug interaction data. Report all adverse drug reactions to SAHPRA.

Based on information present in the Evidence Pack:

- **Safety counter-signal — enzyme-deficient red cell disorders**: PMID 20516363 documents amoxicillin-induced non-immune haemolytic anaemia in a child with **glucose-6-phosphate isomerase (GPI) deficiency**. This is directly relevant to the Rank 9 prediction (congenital haematological disorder) and represents a contraindication signal in patients with red blood cell enzyme deficiencies.

- **Drug-induced pancreatitis / hyperamylasemia**: Published case reports associate amoxicillin with drug-induced pancreatitis. This creates a reverse causality problem with the Rank 2 prediction (hyperamylasemia) — amoxicillin may *cause* the condition, not treat it.

- **Plague treatment risk**: In septicemic plague (Rank 8), *Y. pestis* carries intrinsic chromosomal beta-lactamases (BlaA/BlaB). Using amoxicillin instead of guideline-recommended streptomycin, gentamicin, doxycycline, or ciprofloxacin could result in treatment failure and death.

---

## Conclusion and Next Steps

### Epiglottitis — **Decision: Proceed with Guardrails**

**Rationale:**
Multiple clinical practice guidelines from France and the Netherlands, supported by a 1987 prospective paediatric study that directly treated 24 epiglottitis cases with amoxicillin-clavulanate, provide Level 3 evidence for this use. The mechanism of action maps directly to the causative bacterial pathogens.

**To proceed, the following is needed:**
- Confirm SAHPRA registration status for both amoxicillin and co-amoxiclav (amoxicillin-clavulanate) formulations
- Obtain local ENT antibiogram data to confirm regional pathogen susceptibility to amoxicillin in South Africa
- Align with South African standard treatment guidelines (STGs) and NEML — check whether amoxicillin-clavulanate is already listed for ENT infections
- Establish clear clinical criteria for oral vs. parenteral therapy: **intravenous co-amoxiclav or cefuroxime is standard of care for severe epiglottitis with airway compromise**; oral amoxicillin applies only to confirmed mild presentations or step-down therapy
- Develop a monitoring protocol for treatment response and airway status

---

### Monoclonal Gammopathy (IPSID) — **Decision: Research Question**

**Rationale:**
A plausible and historically documented mechanistic pathway exists specifically for IPSID (Stage A), supported by case-level evidence in *Lancet* and other peer-reviewed journals. The evidence base is insufficient for routine clinical application but sufficient to warrant further investigation.

**To proceed, the following is needed:**
- Estimate prevalence of IPSID among South African patients presenting with monoclonal gammopathy (particularly in communities with historically elevated *Campylobacter* exposure)
- Conduct systematic review of antibiotic regimens used in IPSID — including whether amoxicillin/ampicillin or tetracyclines are preferred in Southern African epidemiological context
- Establish diagnostic criteria to clearly separate IPSID from MGUS and multiple myeloma, as antibiotic therapy is not appropriate for those entities
- Consider prospective case registry before any clinical trial is designed

---

### Remaining 8 Indications (Ranks 1–5, 7–9) — **Decision: Hold**

No further research investment is recommended at this stage. Ranks 1–5 and 7 lack both mechanistic plausibility and clinical evidence — TxGNN scores reflect knowledge graph proximity through shared comorbidity nodes rather than true therapeutic signal. **Rank 9 (congenital haematological disorder) should be flagged as a contraindication context** given the documented safety counter-signal (amoxicillin-induced haemolysis in G6PI deficiency). **Rank 8 (septicemic plague) carries a patient safety risk** if amoxicillin were selected over guideline-recommended agents.

---

> **Disclaimer**: This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require rigorous clinical validation before application in patient care. All adverse drug reactions should be reported to SAHPRA.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

