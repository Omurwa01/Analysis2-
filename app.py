import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re
from collections import Counter
import json

# Load and clean data from JSON
@st.cache_data
def load_data():
    with open('CORD-19-research-challenge-metadata (1).json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    records = []
    if 'recordSet' in data and isinstance(data['recordSet'], list):
        for item in data['recordSet']:
            if 'field' in item:
                study_name = item.get('name', 'Unknown Study')
                study_description = item.get('description', '')
                for field in item['field']:
                    record = {
                        'study_name': study_name,
                        'study_description': study_description,
                        'field_name': field.get('name', ''),
                        'field_id': field.get('@id', ''),
                        'data_type': field.get('dataType', ['Unknown'])[0] if field.get('dataType') else 'Unknown'
                    }
                    records.append(record)

    df = pd.DataFrame(records)
    df['study_name'] = df['study_name'].fillna('Unknown Study')
    df['field_name'] = df['field_name'].fillna('Unknown Field')
    df['data_type'] = df['data_type'].fillna('Unknown Type')
    df = df[df['field_name'].str.strip() != '']
    df['study_name'] = df['study_name'].str.replace('.csv', '', regex=False)
    return df

df = load_data()

# Title and description
st.title("CORD-19 Research Challenge Metadata Analysis")
st.write("""
This app analyzes the CORD-19 metadata structure from the Croissant JSON file.
It provides visualizations of studies, field types, and word clouds from field names.
Use the filters to explore the data.
""")

# Filter by study
studies = df['study_name'].unique()
selected_studies = st.multiselect("Select studies", studies, default=studies[:5])

# Filter data
filtered_df = df[df['study_name'].isin(selected_studies)]

# Studies by type
st.subheader("Studies by Type")
studies_by_type = filtered_df['study_name'].value_counts().head(10)
fig, ax = plt.subplots()
studies_by_type.plot(kind='bar', ax=ax)
ax.set_title('Top Studies by Number of Fields')
ax.set_xlabel('Study')
ax.set_ylabel('Number of Fields')
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

# Data types distribution
st.subheader("Field Data Types Distribution")
data_types = filtered_df['data_type'].value_counts()
fig2, ax2 = plt.subplots()
data_types.plot(kind='bar', ax=ax2)
ax2.set_title('Field Data Types Distribution')
ax2.set_xlabel('Data Type')
ax2.set_ylabel('Number of Fields')
plt.xticks(rotation=45)
st.pyplot(fig2)

# Word cloud of field names
st.subheader("Word Cloud of Field Name Words")
field_text = filtered_df['field_name'].dropna().str.lower()
words = []
stop_words = set(['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those', 'vs', 'bound', 'value'])
for field in field_text:
    for word in re.findall(r'\b\w+\b', field):
        if word not in stop_words and len(word) > 2:
            words.append(word)
text = ' '.join(words)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
fig3, ax3 = plt.subplots()
ax3.imshow(wordcloud, interpolation='bilinear')
ax3.axis('off')
st.pyplot(fig3)

# Sample of the dataset
st.subheader("Sample of Filtered Dataset")
st.dataframe(filtered_df.head(10))
