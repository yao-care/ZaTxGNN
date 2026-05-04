---
layout: default
title: Cefixime
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 10
---

# Cefixime
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

# Cefixime: From Bacterial Infections to Gonococcal Urethritis

## One-Sentence Summary

Cefixime is a third-generation oral cephalosporin antibiotic with established activity against susceptible Gram-negative organisms, including *Neisseria gonorrhoeae*. The TxGNN model assigns its highest score to **Ureaplasma urethritis** (Rank 1) and **Gonococcal Urethritis** (Rank 2), both at 98.98%; however, the Ureaplasma prediction is mechanistically invalid (Ureaplasma lacks a cell wall and is inherently resistant to all β-lactams) and has been assessed as **Hold** — this report therefore prioritises the Rank 2 prediction for Gonococcal Urethritis, which is supported by **2 registered clinical trials** and **20 publications** and carries a **Proceed with Guardrails** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum bacterial infections (no SAHPRA registration data available; cefixime is not currently marketed in South Africa) |
| Predicted New Indication | Gonococcal Urethritis |
| TxGNN Prediction Score | 98.98% |
| Evidence Level | L2 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cefixime is a third-generation cephalosporin that inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins (PBP1, PBP2, and PBP3), disrupting peptidoglycan cross-linking and causing bacterial lysis. Detailed mechanism of action data were not included in this Evidence Pack (Data Gap DG002); however, the above description reflects well-established pharmacological knowledge for this drug class.

*Neisseria gonorrhoeae*, the causative organism of gonococcal urethritis, possesses the peptidoglycan cell wall that β-lactams directly target. Historically, cefixime 400 mg as a single oral dose was a WHO and CDC first-line recommendation for uncomplicated gonorrhoea, supported by multiple randomised controlled trials demonstrating bacteriological eradication rates exceeding 95–97%. This is therefore not a novel repurposing in the traditional sense — it represents a well-established but increasingly restricted clinical application driven by resistance trends.

The central clinical concern for South Africa is antimicrobial resistance (AMR). South Africa has already documented the **first two cases of extended-spectrum cephalosporin-resistant *N. gonorrhoeae*** with verified cefixime treatment failure (PMID 23416957). Current international guidelines (WHO, CDC, ECDC) and the South African NICD/NDoH STI Management Guidelines have de-prioritised oral cefixime in favour of injectable ceftriaxone as first-line therapy. Any proposed use of cefixime for gonorrhoea in South Africa must be preceded by a review of current local susceptibility data from NICD/NHLS surveillance.

> **On the Rank 1 prediction (Ureaplasma urethritis):** Although TxGNN assigned the same score (98.98%) to Ureaplasma urethritis, this prediction is mechanistically invalid. *Ureaplasma urealyticum/parvum* are wall-less organisms and are inherently resistant to all β-lactam antibiotics. Treatment requires macrolides (azithromycin) or tetracyclines (doxycycline). The high score likely reflects false-positive graph topology — the "non-gonococcal urethritis" and "gonococcal urethritis" nodes share close proximity in the knowledge graph. **Recommendation: Hold.**

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03840811](https://clinicaltrials.gov/study/NCT03840811) | Phase 1 | Completed | 27 | Experimental human infection model using isogenic *N. gonorrhoeae* mutants to investigate virulence determinants in the male urethra; provides mechanistic insight into gonococcal pathogenesis but does not directly evaluate cefixime therapy |
| [NCT05294588](https://clinicaltrials.gov/study/NCT05294588) | Phase 2 | Completed | 65 | Double-blind RCT evaluating whether the 4C-MenB (Bexsero) meningococcal vaccine provides cross-protective immunity against *N. gonorrhoeae* urethral infection using a controlled human infection model; a preventive vaccine study, not a cefixime treatment trial |

> **Note:** No registered clinical trials directly evaluating cefixime for gonococcal urethritis were identified in ClinicalTrials.gov. Key efficacy evidence derives from pre-registration-era RCTs documented in the peer-reviewed literature below. No SANCTR (South African National Clinical Trials Register) or PACTR (Pan African Clinical Trials Registry) trials were identified.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [2183719](https://pubmed.ncbi.nlm.nih.gov/2183719/) | 1990 | RCT | *Antimicrob Agents Chemother* | Single 800 mg oral cefixime cured 96/97 (99%) men with uncomplicated gonococcal urethritis vs amoxicillin + probenecid; neither regimen covered co-existing *Chlamydia* or *Ureaplasma* |
| [1534422](https://pubmed.ncbi.nlm.nih.gov/1534422/) | 1992 | RCT | *Sex Transm Dis* | Cefixime 400 mg or 800 mg single oral dose vs ceftriaxone 250 mg IM: 97% bacteriological eradication in gonococcal urethritis/cervicitis (N=155 evaluable patients) |
| [12673405](https://pubmed.ncbi.nlm.nih.gov/12673405/) | 2003 | Clinical Trial | *J Infect Chemother* | Double-dosing 200 mg cefixime at a 6-hour interval maintains drug concentration above 4×MIC₉₀ for ≥10 h, achieving ≥95% eradication; supports an alternative dosing strategy for uncomplicated gonococcal urethritis |
| [23299608](https://pubmed.ncbi.nlm.nih.gov/23299608/) | 2013 | Treatment Failure Study | *JAMA* | Documented cefixime treatment failure in Toronto; cefixime is the only oral option but rising MICs worldwide; endorses ceftriaxone IM as primary first-line therapy |
| [23416957](https://pubmed.ncbi.nlm.nih.gov/23416957/) | 2013 | Case Study | *J Antimicrob Chemother* | **South Africa-specific:** First two ESC-resistant *N. gonorrhoeae* cases in South Africa, one with phenotypically and genetically verified cefixime treatment failure — critical local AMR alert directly relevant to clinical practice in South Africa |
| [34475363](https://pubmed.ncbi.nlm.nih.gov/34475363/) | 2021 | Surveillance Study | *Sex Transm Dis* | US GISP/SURRG data showing anatomic site differences in gonococcal AMR among men who have sex with men; highlights need for site-specific susceptibility monitoring |
| [33082237](https://pubmed.ncbi.nlm.nih.gov/33082237/) | 2021 | Surveillance Study | *Sex Transm Infect* | First WHO-protocol standardised gonococcal AMR surveillance programme in Kampala, Uganda; establishes sub-Saharan Africa AMR baseline directly relevant to the South African context |
| [20643433](https://pubmed.ncbi.nlm.nih.gov/20643433/) | 2010 | Review | *J Urol* | Comprehensive review of emerging drug resistance in *N. gonorrhoeae* with focus on fluoroquinolone, cefixime, and azithromycin resistance mechanisms and clinical implications |
| [40922809](https://pubmed.ncbi.nlm.nih.gov/40922809/) | 2025 | Surveillance Study | *Lancet Reg Health West Pac* | WHO EGASP 2023 AMR data from 9 sentinel countries confirms ongoing global spread of cefixime resistance, underlining the need for continued national surveillance before empiric use |
| [20353145](https://pubmed.ncbi.nlm.nih.gov/20353145/) | 2010 | Review | *Am Fam Physician* | Clinical overview of male urethritis diagnosis and treatment; identifies gonococcal and non-gonococcal causes and places cefixime within syndromic management protocols |

---

## South Africa Market Information

Cefixime is currently **not registered with SAHPRA** and is **not marketed in South Africa**. There are no product licences to list.

> Clinicians considering use of cefixime in South Africa must apply for a **Section 21 (unregistered medicine) authorisation** from SAHPRA prior to clinical use. The **National Institute for Communicable Diseases (NICD)** and **NDoH STI Management Guidelines** should be consulted for the current recommended treatment regimen for gonorrhoea. Cefixime is included in the WHO Essential Medicines List (EML) as an option for uncomplicated gonorrhoea, which may support a motivation for Section 21 approval.

---

## Safety Considerations

No SAHPRA-approved Professional Information (PI) is available, as cefixime is currently unregistered in South Africa. For a complete safety profile, refer to an established international prescribing reference (FDA prescribing information, BNF, or WHO EML formulary).

The following clinically significant safety signals are identified from evidence within this report:

- **Antimicrobial resistance risk:** Extended-spectrum cephalosporin resistance in *N. gonorrhoeae* has been documented in South Africa (PMID 23416957). Use without current local MIC susceptibility data risks treatment failure and selection pressure for further resistance.
- **Serious hypersensitivity reactions:** A case of Stevens-Johnson Syndrome (SJS) associated with cefixime has been reported (PMID 35860067). As with all cephalosporins, anaphylaxis and severe cutaneous reactions are possible; cross-reactivity with penicillins should be assessed before use in patients with a penicillin allergy history.
- **Co-infection gap:** Cefixime has no activity against *Chlamydia trachomatis* or *Ureaplasma* spp., which frequently co-infect patients with gonococcal urethritis. Current STI guidelines recommend co-administration of azithromycin or doxycycline to provide coverage against these organisms.

Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cefixime has robust historical RCT evidence supporting direct bactericidal activity against *N. gonorrhoeae*, and was formerly a globally recommended first-line oral treatment for uncomplicated gonorrhoea. However, the well-documented emergence of cefixime resistance — including verified treatment failure cases in South Africa — means empiric use is no longer appropriate without current local AMR confirmation, and the drug's absence from the South African market creates an additional regulatory barrier.

**To proceed, the following is needed:**
- **Local AMR data:** Review current NICD/NHLS surveillance data on *N. gonorrhoeae* MIC distribution for cefixime in South Africa to confirm whether susceptibility levels support clinical use
- **SAHPRA authorisation:** Apply for Section 21 authorisation or initiate a SAHPRA registration dossier before any clinical use in South Africa
- **Full safety documentation:** Retrieve and review the complete PI from an international regulatory authority to address Data Gap DG001 (SAHPRA PI warnings and contraindications)
- **MOA documentation:** Confirm mechanism of action detail via DrugBank API query to address Data Gap DG002 and strengthen the mechanistic justification
- **Combination therapy protocol:** Determine whether cefixime should be co-administered with azithromycin or doxycycline to cover *Chlamydia trachomatis* and *Ureaplasma* co-infection, in line with NDoH/NICD STI guidelines
- **Guideline alignment check:** Formally compare this recommendation against the current NDoH/NICD STI Management Guidelines to confirm the proposed clinical pathway does not conflict with national policy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

