import requests
from bs4 import BeautifulSoup
import pandas as pd


URL = "https://www.brightermonday.co.ke/jobs"


headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


jobs = []
job_cards = soup.find_all("div", class_="job-list-card")  # Find all job cards

for job in job_cards:
    title = job.find("h3").text.strip() if job.find("h3") else "N/A"
    company = job.find("h4").text.strip() if job.find("h4") else "N/A"
    location = job.find("span", class_="location").text.strip() if job.find("span", class_="location") else "N/A"
    job_type = job.find("span", class_="job-type").text.strip() if job.find("span", class_="job-type") else "N/A"
    link = job.find("a")["href"] if job.find("a") else "N/A"

    jobs.append({"Title": title, "Company": company, "Location": location, "Type": job_type, "Link": link})


df = pd.DataFrame(jobs)
df.to_csv("brightermonday_jobs.csv", index=False)

print("✅ Jobs scraped and saved to brightermonday_jobs.csv!")
