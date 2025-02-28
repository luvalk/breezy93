import streamlit as st
import pandas as pd


df = pd.read_csv("brightermonday_jobs.csv")


st.title("🌟 AI Job Finder - BrighterMonday")

search_query = st.text_input("Enter a job title (e.g., Data Scientist):")

if search_query:
    filtered_jobs = df[df["Title"].str.lower().str.contains(search_query.lower(), na=False)]
    
    if not filtered_jobs.empty:
        st.write(f"🔍 Found {len(filtered_jobs)} job(s):")
        st.dataframe(filtered_jobs)
    else:
        st.warning("❌ No matching jobs found.")

st.write("🔄 **Run the scraper again** to update job listings.")
