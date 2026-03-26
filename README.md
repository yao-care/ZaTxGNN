# ZaTxGNN - South Africa Drug Repurposing Predictions

Drug repurposing predictions for South Africa using the TxGNN knowledge graph.

## Data Source

- **SAHPRA** (South African Health Products Regulatory Authority)
- **Medicine Price Registry** (MPR) via medicineprices.org.za API

## Features

- Knowledge graph-based drug repurposing predictions
- FHIR R4 compliant resources
- Evidence collection from ClinicalTrials.gov and PubMed
- South African health news monitoring

## Quick Start

```bash
# Install dependencies
uv sync

# Download drug data
python scripts/download_mpr_data.py

# Prepare external data
uv run python scripts/prepare_external_data.py

# Run KG prediction
uv run python scripts/run_kg_prediction.py
```

## Disclaimer

This project is for research purposes only and does not constitute medical advice.
Drug repurposing predictions require clinical validation before therapeutic application.

## License

MIT
