# CORD-19 Data Science Assignment

## Overview
This project analyzes the metadata from the CORD-19 Research Challenge dataset. It includes data cleaning, exploratory analysis, visualizations, and an interactive Streamlit app for filtering and viewing results.

## Dataset
The dataset used is `metadata.csv` from the CORD-19 Research Challenge on Kaggle: [https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)

Download the file and place it in the project directory.

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
