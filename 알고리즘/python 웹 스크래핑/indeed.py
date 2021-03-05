import requests
from bs4 import BeautifulSoup
limit = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={limit}&radius=25"

def extract_last_page():

    html = requests.get(URL)
    soup = BeautifulSoup(html.text, 'html.parser')
    
    pagination = soup.find("div", {"class": "pagination"})
    pages = pagination.find_all("a")

    spans = []
    for p in pages[:-1]:
        spans.append(int(p.find("span").string))
    last_page = spans[-1]

    return last_page

def extract_job(jobcard):
    title = jobcard.find("h2", {"class": "title"})
    title = title.find("a")["title"]

    com = jobcard.find("span", {"class":"company"})
    if com.find("a"):
        comp = str(com.find("a").string)
        company = comp.strip("\n")
    else:   
        company = str(com.string).strip("\n")
        
    sjcl = jobcard.find("div", {"class":"sjcl"})
    if sjcl.find("div", {"class":"location"}):
        location = sjcl.find("div", {"class":"location"}).string
    else:
        location = sjcl.find("span", {"class":"location"}).string

    job_id = jobcard["data-jk"]

    return {"title":title , "company":company, "location":location,\
         "link":f"https://kr.indeed.com/%EC%B1%84%EC%9A%A9%EB%B3%B4%EA%B8%B0?jk={job_id}"}


def extract_jobcard(last_page):
    jobs = []
    for p in range(last_page):
        result = requests.get(f"{URL}&start={limit*p}")
        soup = BeautifulSoup(result.text, 'html.parser')
        job_card = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for select in job_card:
            jobs.append(extract_job(select))
        print(f"Scrapped Indeed p.{p+1}")
            
    return jobs

def get_jobs():
    last_page = extract_last_page()
    jobs = extract_jobcard(2)
    return jobs
