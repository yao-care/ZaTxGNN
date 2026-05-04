---
layout: default
title: Abacavir
parent: 僅模型預測 (L5)
nav_order: 11
evidence_level: L5
indication_count: 3
---

# Abacavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Here is the complete pharmacist report in Markdown format:

---

# ZaTxGNN Pharmacist Report: ABACAVIR (DB01048)

**Report ID**: ZA-DB01048-multi | **Version**: v4 | **Generated**: 2026-04-03 | **Data Cutoff**: 2026-04-03

---

## 1. Executive Summary

Abacavir (ABC) is a well-established nucleoside reverse transcriptase inhibitor (NRTI) widely used in South Africa as a cornerstone of antiretroviral therapy (ART) for HIV-1 infection. It is listed on the South African Essential Medicines List (EML) and is a critical component of first-line ART regimens in the national HIV programme.

The TxGNN knowledge graph model generated three predicted novel indications for abacavir:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|----------------|----------------|
| 1 | Simian immunodeficiency virus (SIV) infection | 99.79% | L4 | **Hold** |
| 2 | Feline acquired immunodeficiency syndrome (FAIDS) | 99.79% | L4 | **Hold** |
| 3 | Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.78% | L5 | **Hold** |

**Overall Assessment**: All three predictions are assigned a **Hold** recommendation at decision stage S0 (pre-screening). The first two predictions (SIV and FAIDS) relate to animal lentivirus infections with no human clinical applicability, reflecting the model's detection of legitimate phylogenetic and mechanistic relationships between retroviral species but without translational relevance to human medicine. The third prediction (a rare neurodevelopmental disorder) is highly speculative with no supporting evidence. **None of these predictions warrant further drug repurposing investigation for human therapeutic use.**

**SAHPRA Registration Status**: Abacavir is registered with SAHPRA and is available in South Africa in both single-agent and fixed-dose combination formulations.

---

## 2. Drug Information

### 2.1 Identification

| Item | Detail |
|------|--------|
| International Nonproprietary Name (INN) | Abacavir |
| DrugBank ID | DB01048 |
| ATC Code | J05AF06 |
| Chemical Class | Nucleoside reverse transcriptase inhibitor (NRTI) |
| Pharmacological Class | Antiretroviral agent |

### 2.2 South African Brand Names and Formulations

Abacavir is available in South Africa through multiple SAHPRA-registered products:

- **Ziagen** (originator, ViiV Healthcare / GlaxoSmithKline) — 300 mg tablets, 20 mg/mL oral solution
- **Fixed-dose combinations**:
  - **Triumeq** (abacavir 600 mg / dolutegravir 50 mg / lamivudine 300 mg)
  - **Kivexa / Epzicom** (abacavir 600 mg / lamivudine 300 mg)
- **Generic formulations**: Multiple generics are available in the South African public and private sectors

### 2.3 Current SAHPRA-Registered Indications

- Treatment of HIV-1 infection in adults and children, in combination with other antiretroviral agents

### 2.4 Schedule Classification

- **Schedule 4 (S4)** — Prescription-only medicine

### 2.5 Essential Medicines List (EML) Status

- **Listed on the South African EML** for the treatment of HIV infection
- Abacavir-containing regimens feature prominently in the National Department of Health Standard Treatment Guidelines (STGs) for HIV
- Currently included in preferred first-line ART regimens, particularly in paediatric populations and in adults with renal impairment where tenofovir-based regimens may be contraindicated
- The fixed-dose combination of abacavir/lamivudine/dolutegravir (TLD-ABC) is part of the state-sector formulary

### 2.6 Mechanism of Action

Abacavir is a carbocyclic synthetic nucleoside analogue. Following intracellular phosphorylation to its active metabolite carbovir triphosphate (CBV-TP), it competes with the natural substrate deoxyguanosine-5'-triphosphate (dGTP) for incorporation into viral DNA by HIV-1 reverse transcriptase (RT). Once incorporated, CBV-TP acts as a chain terminator, preventing further elongation of the viral DNA strand, thereby inhibiting HIV-1 replication.

> **Note**: The evidence pack flagged mechanism of action data as a Data Gap (DG002). The above information is provided from established pharmacological knowledge of abacavir.

---

## 3. Predicted New Indications

### 3.1 Prediction 1: Simian Immunodeficiency Virus (SIV) Infection

**TxGNN Score**: 0.9979 (Rank #1496) | **Evidence Level**: L4 | **Stage**: S0 | **Recommendation**: Hold

#### Disease Description
Simian immunodeficiency virus (SIV) is a retrovirus of the genus *Lentivirus* that infects non-human primates (NHPs), including African green monkeys, sooty mangabeys, and macaques. SIV is the phylogenetic precursor to HIV-1 and HIV-2, sharing significant genomic and structural homology, including a dependence on reverse transcriptase (RT) for viral replication.

#### Biological Rationale
The TxGNN knowledge graph correctly identifies the close evolutionary relationship between SIV and HIV-1. Both viruses belong to the *Lentivirus* genus and share an RT-dependent replication mechanism, making NRTIs such as abacavir mechanistically relevant. SIV infection in macaques is, in fact, a well-established preclinical model for HIV research.

**However**, SIV is an animal pathogen and does not infect humans. This prediction reflects a legitimate biological signal within the knowledge graph (shared molecular targets between related viruses) but has **no translational applicability to human drug repurposing**. In the veterinary and biomedical research context, NRTIs including abacavir are routinely used in NHP models of SIV/SHIV infection for preclinical studies, but this does not constitute a novel repurposing opportunity.

#### Mechanism of Action Relevance
**High mechanistic plausibility** — Abacavir's active metabolite (CBV-TP) inhibits RT, a mechanism directly applicable to SIV replication. However, differences in RT sequences between SIV strains and HIV-1 may affect drug susceptibility.

### 3.2 Prediction 2: Feline Acquired Immunodeficiency Syndrome (FAIDS)

**TxGNN Score**: 0.9979 (Rank #1497) | **Evidence Level**: L4 | **Stage**: S0 | **Recommendation**: Hold

#### Disease Description
Feline acquired immunodeficiency syndrome (FAIDS) is caused by feline immunodeficiency virus (FIV), a lentivirus that infects domestic cats. FIV causes progressive immune dysfunction analogous to HIV/AIDS in humans, and the FIV-infected cat model has been studied as a comparative model for HIV pathogenesis.

#### Biological Rationale
FIV, like HIV and SIV, is a lentivirus with RT-dependent replication. The TxGNN model detects this phylogenetic and mechanistic relationship. Published in vitro data (Bisset et al., 2002) demonstrates that the combination of zidovudine, lamivudine, and abacavir has activity against FIV replication, albeit with lower efficiency than against HIV-1, consistent with RT sequence divergence between the two virus families.

**However**, FAIDS is an exclusively veterinary condition. This prediction has **no applicability to human drug repurposing**. The finding is of potential interest only in veterinary medicine or as validation of the TxGNN model's ability to detect cross-species lentivirus relationships.

#### Mechanism of Action Relevance
**Moderate mechanistic plausibility** — NRTI activity against FIV RT has been demonstrated in vitro, but FIV RT has significant sequence differences from HIV-1 RT, resulting in reduced drug potency.

### 3.3 Prediction 3: Neurodevelopmental Disorder with Ataxic Gait, Absent Speech, and Decreased Cortical White Matter

**TxGNN Score**: 0.9978 (Rank #1554) | **Evidence Level**: L5 | **Stage**: S0 | **Recommendation**: Hold

#### Disease Description
This is a rare monogenic neurodevelopmental disorder characterised by severe intellectual disability, absent or severely limited speech, cerebellar ataxia, and reduced cortical white matter volume on MRI. The condition is typically caused by biallelic mutations in specific genes involved in neurodevelopmental pathways.

#### Biological Rationale
There is **no established mechanistic link** between abacavir (an NRTI) and this neurodevelopmental condition. The only theoretical (and highly speculative) connection involves the hypothesis that NRTIs may suppress endogenous retrotransposon (LINE-1) activity, which has been proposed to play a role in certain neurodegenerative and neuroinflammatory processes. However:

- This hypothesis remains unvalidated in clinical settings
- No published evidence connects LINE-1 activity to this specific neurodevelopmental disorder
- The blood-brain barrier penetration of abacavir, while adequate for HIV CNS reservoirs, has not been studied in this context
- The risk-benefit profile of chronic NRTI use in a non-HIV-infected paediatric population would be highly unfavourable

#### Mechanism of Action Relevance
**Weak mechanistic plausibility** — No direct or well-supported indirect mechanism. Purely computational prediction with no biological validation.

---

## 4. Evidence Summary

### 4.1 Clinical Trial Evidence

#### ClinicalTrials.gov
No clinical trials were identified directly investigating abacavir for any of the three predicted indications.

Four clinical trials were returned in the query for FAIDS, but all are HIV-1 trials where abacavir serves as background NRTI backbone therapy (not as the investigational agent) and have no relevance to FIV/FAIDS:

| NCT ID | Title | Phase | Relevance |
|--------|-------|-------|-----------|
| NCT01227824 | SPRING-2: DTG vs RAL + dual NRTI (n=828) | Phase 3 | **Grade C** — HIV-1 trial; ABC as background NRTI only |
| NCT00951015 | SPRING-1: DTG dose-finding + ABC/3TC or TDF/FTC (n=208) | Phase 2 | **Grade C** — HIV-1 trial; ABC as background NRTI only |
| NCT01499199 | DTG CNS PK study + ABC/3TC (n=13) | Phase 3b | **Grade C** — HIV-1 PK study; no FAIDS relevance |
| NCT01263015 | SINGLE: DTG+ABC/3TC vs Atripla (n=844) | Phase 3 | **Grade C** — HIV-1 trial; ABC in combination arm only |

#### South African Clinical Trial Register (SANCTR) & Pan African Clinical Trials Registry (PACTR)
Not queried in this evidence pack. No known South African or Pan African trials investigating abacavir for any of the predicted indications.

#### ICTRP (WHO International Clinical Trials Registry Platform)
No relevant trials identified across all three indications.

### 4.2 Published Literature (PubMed)

| PMID | Year | Title | Study Type | Relevance |
|------|------|-------|------------|-----------|
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | Susceptibility of HIV-2, SIV and SHIV to various anti-HIV-1 compounds: implications for treatment and postexposure prophylaxis | In vitro susceptibility study (Tier 3) | Demonstrates NRTI activity against SIV strains in vitro. Relevant to SIV prediction only. |
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Combined effect of ZDV, 3TC, and ABC antiretroviral therapy in suppressing in vitro FIV replication | Animal model intervention study (Tier 3) | Demonstrates in vitro activity of ABC-containing regimen against FIV. Relevant to FAIDS prediction only. |

### 4.3 South African Studies
No South African-specific studies were identified for any of the predicted indications. This is expected given the veterinary/non-human nature of two predictions and the rarity of the third.

### 4.4 African Context Considerations
- **HIV programme relevance**: Abacavir is a critical drug in South Africa's national ART programme, the largest in the world. Any repurposing consideration must be weighed against the importance of maintaining abacavir supply for HIV treatment.
- **Veterinary context**: SIV is endemic in African NHP populations; however, NHP infections are managed by research institutions, not through human pharmaceutical channels.
- **Rare disease burden**: The neurodevelopmental disorder in Prediction 3 is extremely rare globally. Prevalence data for sub-Saharan Africa are unavailable, and genetic testing infrastructure for such conditions remains limited in many African settings.

---

## 5. Safety Considerations

> **Data Gap Notice**: The evidence pack flagged SAHPRA package insert warnings and contraindications as a Blocking Data Gap (DG001). The following safety information is provided from established pharmacological knowledge and international labelling.

### 5.1 Key Adverse Effects

| Category | Adverse Effects |
|----------|----------------|
| **Black Box Warning** | **Hypersensitivity reaction (HSR)** — Potentially fatal; strongly associated with HLA-B\*5701 allele. HLA-B\*5701 screening is **mandatory** before initiating abacavir in South Africa per STGs. |
| **Serious** | Lactic acidosis, severe hepatomegaly with steatosis (class effect of NRTIs) |
| **Cardiovascular** | Some observational data suggest possible increased risk of myocardial infarction (controversial; data are inconsistent) |
| **Common** | Nausea, headache, fatigue, malaise, diarrhoea, fever |
| **Metabolic** | Lipodystrophy, hyperlipidaemia (class effect) |

### 5.2 Contraindications
- Known hypersensitivity to abacavir or any formulation component
- Patients positive for HLA-B\*5701 allele
- Moderate to severe hepatic impairment (for combination products)

### 5.3 Drug Interactions Relevant to South African Prescribing

| Interacting Drug/Class | Effect | SA Relevance |
|------------------------|--------|--------------|
| Alcohol (ethanol) | Increased abacavir AUC (~41%) via competition for alcohol dehydrogenase | Common co-morbidity in SA ART population |
| Methadone | Increased methadone clearance; may require dose adjustment | Relevant in substance use disorder programmes |
| Ribavirin | Potential antagonism (both guanosine analogues) | HBV/HCV co-infection management |
| Tipranavir/ritonavir | Decreased abacavir levels | ART regimen switching scenarios |

> **Note**: Drug-drug interaction data from the evidence pack returned no results (query status: not_found). The above interactions are from established pharmacological references.

### 5.4 Adverse Drug Reaction Reporting
Any suspected adverse drug reactions should be reported to SAHPRA via the national ADR reporting system:
- **SAHPRA Adverse Drug Reaction Reporting Form**: Available at [https://www.sahpra.org.za](https://www.sahpra.org.za)
- **National Adverse Drug Event Monitoring Centre (NADEMC)**, University of Cape Town

---

## 6. Recommendations

### 6.1 Evidence Strength Assessment

| Prediction | Evidence Level | Strength | Assessment |
|------------|---------------|----------|------------|
| SIV infection | L4 (in vitro data) | Very Weak | Mechanistically sound but clinically irrelevant — SIV is a non-human pathogen |
| FAIDS | L4 (in vitro data) | Very Weak | Mechanistically plausible but veterinary-only disease |
| Neurodevelopmental disorder | L5 (computational only) | None | No supporting evidence of any kind |

**Overall Evidence Grade**: **Insufficient for repurposing action**

### 6.2 Suggested Next Steps

- **No further investigation recommended** for any of the three predictions in a human drug repurposing context
- The SIV and FAIDS predictions may serve as **model validation signals**, confirming that TxGNN correctly identifies cross-species lentivirus relationships via shared RT dependence
- For the neurodevelopmental disorder prediction, the evidence gap is too large and the mechanistic rationale too speculative to justify any research investment

### 6.3 Model Improvement Considerations
These predictions highlight a potential refinement opportunity for ZaTxGNN:
- **Species filtering**: Implementing a post-prediction filter to exclude purely veterinary/animal-model diseases from human repurposing candidate lists would improve clinical relevance of outputs
- **Minimum evidence threshold**: Predictions at L5 (no evidence) with weak mechanistic rationale could be automatically deprioritised

### 6.4 Relevant South African Research Institutions
While these specific predictions do not warrant investigation, South African institutions with relevant expertise include:
- **Desmond Tutu HIV Centre**, University of Cape Town — HIV/ART research
- **Centre for the AIDS Programme of Research in South Africa (CAPRISA)** — Antiretroviral research
- **Africa Health Research Institute (AHRI)** — HIV therapeutics
- **National Institute for Communicable Diseases (NICD)** — Infectious disease surveillance
- **South African Medical Research Council (SAMRC)** — Drug development and repurposing research

### 6.5 Public Health Implications
- **No public health action required** based on these predictions
- Abacavir remains a vital component of South Africa's ART programme; its supply chain and regulatory status should not be affected by computational predictions for non-human indications
- The national HLA-B\*5701 screening programme should continue to be reinforced regardless of any future repurposing considerations

---

## Data Gaps Identified

| ID | Category | Item | Severity | Impact | Remediation |
|----|----------|------|----------|--------|-------------|
| DG001 | Drug Level | SAHPRA package insert warnings/contraindications | **Blocking** | Cannot complete formal S1 safety assessment | Download and parse SAHPRA-approved PI from SAHPRA database |
| DG002 | Drug Level | Mechanism of Action (MOA) | High | Affects mechanistic association analysis | Query DrugBank API for complete MOA data |

---

## Data Collection Log

| # | Source | Query Date | Query Parameters | Status | Count |
|---|--------|-----------|-----------------|--------|-------|
| 1 | DrugBank | 2026-03-26 | drug=ABACAVIR | Success | 1 |
| 2 | ClinicalTrials.gov | 2026-03-26 | drug=ABACAVIR, disease=SIV infection | Success | 0 |
| 3 | ICTRP | 2026-03-26 | drug=ABACAVIR, disease=SIV infection | Success | 0 |
| 4 | PubMed | 2026-03-26 | drug=ABACAVIR, disease=SIV infection | Success | 1 |
| 5 | ClinicalTrials.gov | 2026-03-26 | drug=ABACAVIR, disease=FAIDS | Success | 4 |
| 6 | ICTRP | 2026-03-26 | drug=ABACAVIR, disease=FAIDS | Success | 0 |
| 7 | PubMed | 2026-03-26 | drug=ABACAVIR, disease=FAIDS | Success | 1 |
| 8 | ClinicalTrials.gov | 2026-03-26 | drug=ABACAVIR, disease=Neurodevelopmental disorder | Success | 0 |
| 9 | ICTRP | 2026-03-26 | drug=ABACAVIR, disease=Neurodevelopmental disorder | Success | 0 |
| 10 | PubMed | 2026-03-26 | drug=ABACAVIR, disease=Neurodevelopmental disorder | Success | 0 |

---

> **Research Use Only**: This report is generated for research purposes only and does not constitute medical advice. Drug repurposing predictions require clinical validation before therapeutic application. This is not a SAHPRA-approved assessment. Always refer to current Standard Treatment Guidelines and the Essential Medicines List.

---

*Generated by ZaTxGNN — South Africa Drug Repurposing Predictions*
*Report version: v4 | Candidate ID: ZA-DB01048-multi*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

