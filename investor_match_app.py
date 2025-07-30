
import streamlit as st
import pandas as pd

# Load investor data (replace with real or mock CSV)
def load_data():
    return pd.read_csv("investor_data.csv")

# Score matching based on filters
def score_investors(df, stage, therapeutic, location):
    df["Score"] = 0
    if stage:
        df["Score"] += df["Stage"].str.contains(stage, case=False, na=False).astype(int)
    if therapeutic:
        df["Score"] += df["Therapeutic Focus"].str.contains(therapeutic, case=False, na=False).astype(int)
    if location:
        df["Score"] += df["Location"].str.contains(location, case=False, na=False).astype(int)
    return df.sort_values(by="Score", ascending=False)

# UI
st.title("Biotech Investor Finder")
st.write("Match your startup profile with biotech investors.")

# Sidebar filters
stage = st.sidebar.selectbox("Funding Stage", ["", "Seed", "Series A", "Series B"])
therapeutic = st.sidebar.text_input("Therapeutic Area (e.g. Oncology)")
location = st.sidebar.text_input("Location (e.g. USA, Global)")

# Load and filter data
try:
    df = load_data()
    filtered_df = score_investors(df, stage, therapeutic, location)
    st.write("### Top Matching Investors")
    st.dataframe(filtered_df[["Investor", "Stage", "Therapeutic Focus", "Location", "Score"]].head(20))
except FileNotFoundError:
    st.error("Investor data file not found. Please upload 'investor_data.csv' in your app directory.")

