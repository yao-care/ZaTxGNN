---
layout: default
title: Privacy Policy
nav_order: 95
permalink: /privacy-policy/
description: "ZaTxGNN privacy policy: a static site with no accounts or forms; it uses Google Analytics 4 analytics cookies for usage statistics."
---

# Privacy Policy

<div class="key-takeaway">
This is a static site — no registration and no forms. It uses Google Analytics 4 analytics cookies to compile usage statistics.
</div>

---

## What we collect

<p class="key-answer" data-question="Does ZaTxGNN collect personal data?">
<strong>Only usage statistics, through Google Analytics 4.</strong> This site is hosted on GitHub Pages as a purely static site.
There is no account system and there are no forms, and we do not collect names, email addresses or medical
records. The site uses Google Analytics 4 analytics cookies to compile usage statistics (pages viewed, referrer,
scroll depth and time on page). The cookies are set when a page loads; search terms, form contents and URL
query strings are not sent.
</p>

---

## Third-party services

The site uses the following third-party resources, which may log access according to their own
policies:

| Service | Purpose | Privacy policy |
|---------|---------|----------------|
| GitHub Pages | Site hosting | [GitHub Privacy Statement](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement) |
| Google Analytics 4 (www.googletagmanager.com, google-analytics.com) | Visit statistics (pages viewed, referrer); uses analytics cookies. Search terms, form contents and URL query strings are not sent. | [Google Privacy Policy](https://policies.google.com/privacy) |
| cdn.jsdelivr.net | Script libraries: d3 charts on every page; Fuse.js name matching and the SMART on FHIR client on the SMART pages and in the home-page drug lookup | [jsDelivr Privacy Policy](https://www.jsdelivr.com/terms/privacy-policy-jsdelivr-net) |
| clinicaltrials.gov | Clinical-trial lookup on the SMART pages: only when you ask for trials, the drug and indication names are sent to the ClinicalTrials.gov API | [NLM Web Policies](https://www.nlm.nih.gov/web_policies.html) |
| rxnav.nlm.nih.gov | SMART app: the RxNorm codes of the medications read from your EHR are sent to the NLM RxNav API to look up ingredient names (no patient identifiers) | [NLM Web Policies](https://www.nlm.nih.gov/web_policies.html) |

When you actively launch the SMART on FHIR app, it requests medication data from your electronic
health record system. Patient identity and EHR data are <strong>not sent to this site's servers</strong> (this is a
static site with no backend) and are not stored by this site. To match drug names, the app sends the
medications' RxNorm codes to the US National Library of Medicine's RxNav service; these codes contain no
patient identifiers. When you ask for clinical trials, the drug and indication names are sent to ClinicalTrials.gov.

---

<!-- privacy-law:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改；法規與連結見 .claude/privacy_text_20261119.py）-->
## Applicable law

For visitors in South Africa the relevant law is the [Protection of Personal Information Act 4 of 2013 (POPIA)](https://www.gov.za/documents/protection-personal-information-act), supervised by the [Information Regulator](https://inforegulator.org.za/). The personal information involved is the usage data Google Analytics 4 collects through cookies; it is transferred to Google outside South Africa, which section 72 of POPIA regulates.

## Your rights and how to use them

- Ask whether personal information about you is held and request access to it (section 23).
- Ask for correction or deletion (section 24).
- Object to the processing (section 11(3)).
- Lodge a complaint with the Information Regulator (section 74).

Requests: service@yao.care (there are no accounts, so tell us the date and pages of your visit). Analytics cookies can be blocked or deleted in your browser.

## Copyright and data sources

Site texts are protected under the [Copyright Act 98 of 1978](https://www.gov.za/documents/copyright-act-16-apr-2015-0942). The site's code is published under the MIT License in the [GitHub repository](https://github.com/yao-care/ZaTxGNN); report texts are © 藥提醒科技有限公司 (yao.care).

Data sources used on this site and their terms:

- **TxGNN** data (Harvard Dataverse): CC0 1.0; cite Huang et al., *Nature Medicine* 2024.
- **ClinicalTrials.gov**, **PubMed**: [ClinicalTrials.gov terms](https://clinicaltrials.gov/about-site/terms-conditions), [NCBI policies](https://www.ncbi.nlm.nih.gov/home/about/policies/).
- **DrugBank**: [DrugBank](https://go.drugbank.com/) licence terms, non-commercial use.
- **Local dataset** – [Medicine Price Registry and SAHPRA medapps](https://medicineprices.org.za/), published by SAHPRA and the National Department of Health (Medicine Price Registry); reuse is governed by the publisher's terms, and this site does not grant any further rights.

<!-- privacy-law:end -->

---

## Changes to this policy

Any changes will be published directly on this page.

---

## About the Developer

This platform is developed and operated by **藥提醒科技有限公司** (yao.care). See the
<a href="{{ '/about/' | relative_url }}">About</a> page for the full company and methodology background.

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
This report is for academic research reference only and <strong>does not constitute medical advice</strong>. Always follow your physician's instructions; never adjust medication on your own. Any drug repurposing decision requires full clinical validation and regulatory review.
<br><br>
<small>Reviewed by: 藥提醒科技有限公司 (yao.care)</small>
</div>
