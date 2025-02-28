import pandas as pd


df = pd.read_csv("brightermonday_jobs.csv")


search_query = input("Enter a job title (e.g., Data Scientist): ").lower()


filtered_jobs = df[df["Title"].str.lower().str.contains(search_query, na=False)]


if not filtered_jobs.empty:
    print("\n🔍 Matching Jobs:\n")
    print(filtered_jobs.to_string(index=False))
else:
    print("\n❌ No matching jobs found.")
