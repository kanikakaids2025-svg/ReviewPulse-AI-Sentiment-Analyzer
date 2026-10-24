# ReviewPulse AI – Sentiment Analyzer

A small Streamlit prototype that integrates the pretrained VADER sentiment analysis model to classify English product reviews as Positive, Negative, or Neutral.

## Features
- Accepts a product review as text input
- Uses VADER sentiment analysis
- Shows Positive / Neutral / Negative scores and a compound score
- Includes example reviews
- Does not require a secret API key

## Requirements
- Python 3.10 or newer
- pip

## Run locally

### Windows
```bash
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Example inputs and expected outputs
These are illustrative examples; exact scores depend on the VADER model:
- `This product is amazing. I love it!` → Positive
- `Terrible quality. It stopped working after one day.` → Negative
- `The package arrived today. The box is blue.` → Neutral

## Model integration
This prototype imports `SentimentIntensityAnalyzer` from the `vaderSentiment` library. VADER is a pretrained, lexicon/rule-based sentiment model designed for English text. The compound score is mapped to:
- `>= 0.05`: Positive
- `<= -0.05`: Negative
- otherwise: Neutral

## Limitations
This is a learning prototype, not a production-grade review moderation system. Sarcasm, slang, mixed opinions, and domain-specific wording can affect predictions. It analyzes English text and does not train on a custom dataset.

## Security
No secret API keys are used or stored in this repository.
