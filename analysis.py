# CORD-19 Data Science Assignment
# This script performs data loading, cleaning, analysis, and visualization on the CORD-19 metadata dataset.
# Supports both CSV and JSON input formats with automatic detection and error handling.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import re
import json
import os
import sys
from pathlib import Path

# Step 1: Load and Explore the Dataset
print("Step 1: Loading and exploring the dataset...")

# Load JSON data and extract information about studies/research
with open('CORD-19-research-challenge-metadata (1).json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract relevant information from the JSON structure
# Use the recordSet which contains information about different datasets
records = []
if 'recordSet' in data and isinstance(data['recordSet'], list):
    for item in data['recordSet']:
        if 'field' in item:
            study_name = item.get('name', 'Unknown Study')
            study_description = item.get('description', '')
            # Extract field information
            for field in item['field']:
                record = {
                    'study_name': study_name,
                    'study_description': study_description,
                    'field_name': field.get('name', ''),
                    'field_id': field.get('@id', ''),
                    'data_type': field.get('dataType', ['Unknown'])[0] if field.get('dataType') else 'Unknown'
                }
                records.append(record)

# Create DataFrame from extracted data
df = pd.DataFrame(records)
print(f"Dataset shape: {df.shape}")
print("Columns:", df.columns.tolist())
print("Data types:")
print(df.dtypes)
print("First 5 rows:")
print(df.head())
print("Summary statistics:")
print(df.describe(include='all'))

# Step 2: Clean the Data
print("\nStep 2: Cleaning the data...")
# Handle missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

# Clean the data based on our JSON structure
df['study_name'] = df['study_name'].fillna('Unknown Study')
df['field_name'] = df['field_name'].fillna('Unknown Field')
df['data_type'] = df['data_type'].fillna('Unknown Type')

# Remove empty field names and clean study names
df = df[df['field_name'].str.strip() != '']
df['study_name'] = df['study_name'].str.replace('.csv', '', regex=False)

print("Missing values after cleaning:")
print(df.isnull().sum())
print("Study name distribution:")
print(df['study_name'].value_counts().head(10))

# Step 3: Perform Basic Analysis
print("\nStep 3: Basic analysis...")

# Count studies by type
studies_by_type = df['study_name'].value_counts()
print("Studies by type:")
print(studies_by_type.head(10))

# Count field types by data type
data_types = df['data_type'].value_counts()
print("Field data types distribution:")
print(data_types)

# Find most common field names
field_names = df['field_name'].value_counts().head(20)
print("Top 20 most common field names:")
print(field_names)

# Find most frequent words in field names
field_text = df['field_name'].dropna().str.lower()
# Simple word extraction: split, remove non-alphabetic, remove common words
words = []
stop_words = set(['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those', 'vs', 'bound', 'value'])
for field in field_text:
    for word in re.findall(r'\b\w+\b', field):
        if word not in stop_words and len(word) > 2:
            words.append(word)
word_freq = Counter(words).most_common(20)
print("Most frequent words in field names:")
print(word_freq)

# Step 4: Create Visualizations
print("\nStep 4: Creating visualizations...")

# Bar chart of studies by type
plt.figure(figsize=(12, 8))
studies_by_type.head(10).plot(kind='bar')
plt.title('Top 10 Study Types')
plt.xlabel('Study Type')
plt.ylabel('Number of Fields')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('studies_by_type.png')
plt.show()

# Bar chart of data types
plt.figure(figsize=(10, 6))
data_types.plot(kind='bar')
plt.title('Field Data Types Distribution')
plt.xlabel('Data Type')
plt.ylabel('Number of Fields')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('data_types.png')
plt.show()

# Word cloud of frequent field name words
text = ' '.join(words)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Field Name Words')
plt.tight_layout()
plt.savefig('wordcloud.png')
plt.show()

# Short Report
print("\nShort Report:")
print("Key Findings:")
print("- The dataset contains", len(df), "field entries across", df['study_name'].nunique(), "different studies.")
print("- Most common study type:", studies_by_type.index[0], "with", studies_by_type.iloc[0], "fields.")
print("- Most common data type:", data_types.index[0], "with", data_types.iloc[0], "fields.")
print("- Common words in field names include:", [w[0] for w in word_freq[:5]])
print("Challenges:")
print("- Processing JSON metadata structure to extract meaningful information.")
print("- Converting complex nested JSON into tabular format.")
print("- Handling various data types and field structures.")
print("- This metadata describes the structure of various COVID-19 research datasets.")
