# CORD-19 Data Science Assignment

## Overview
This project analyzes the metadata from the CORD-19 Research Challenge dataset. It supports both CSV and JSON formats with automatic file detection, includes data cleaning, exploratory analysis, and generates visualizations.

## Features
- ✅ **Flexible Data Loading**: Automatically detects and loads CSV or JSON files
- ✅ **Error Handling**: Robust error handling for missing files and dependencies  
- ✅ **Data Analysis**: Comprehensive analysis of study types, field distributions, and word frequencies
- ✅ **Visualizations**: Generates charts and word clouds automatically
- ✅ **Virtual Environment**: Uses isolated Python environment for dependencies

## Dataset
The dataset used is from the CORD-19 Research Challenge on Kaggle: [https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)

**Supported file formats:**
- `metadata.csv` (original CSV format)
- `CORD-19-research-challenge-metadata.json` (JSON metadata format)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Omurwa01/Analysis2-.git
cd Analysis2-
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
```

### 3. Activate Virtual Environment
**Windows:**
```bash
.venv\Scripts\activate
```
**Mac/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Requirements
- Python 3.x
- pandas
- matplotlib
- seaborn
- wordcloud
- streamlit
- re (built-in)
- collections (built-in)

Install dependencies:
```
pip install pandas matplotlib seaborn wordcloud streamlit
```

## Files
- `analysis.py`: Python script for data loading, cleaning, analysis, and visualizations.
- `app.py`: Streamlit app for interactive exploration.
- `metadata.csv`: Dataset file (download separately).
- `README.md`: This file.

## Usage
1. Run the analysis script:
   ```
   python analysis.py
   ```
   This will generate plots and print results.

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
   Open the provided URL in a browser to interact with the app.

## Key Findings
- [Summarize main insights from the analysis, e.g., publication trends, top journals, common title words.]

## Challenges
- [Mention any difficulties, e.g., handling large dataset, missing data, date conversions.]

## License
[Specify license if applicable, e.g., MIT]
