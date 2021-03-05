import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python"

def extract_last_page():
	html = requests.get(URL)
	soup = BeautifulSoup(html.text, "html.parser")
	page = soup.find("div", {"class":"s-pagination"}).find_all("a")
	last_page = page[-2].get_text().strip()
	
	return int(last_page)

def extract_job(html):
	title = html.find("h2", {"class":"mb4"}).find("a")["title"]

	comp_lo = html.find("h3", {"class":"fc-black-700"})\
		.find_all("span", recursive=False)
	company, location = map(lambda x:str(x.string).strip(), comp_lo)
	# company = html.find("h3", {"class":"fc-black-700"}).find("span").string
	# company = str(company).strip()
	
	# location = html.find("h3", {"class":"fc-black-700"})\
	# 	.find("span", {"class":"fc-black-500"}).string
	# location = str(location).strip()

	link = int(html["data-jobid"])
	
	return {"title":title, "company":company, "location":location, \
		"link":f"https://stackoverflow.com/jobs?id={link}&q=python"} 


def extract_jobcard(lastpage):
	jobs = []
	for p in range(1, lastpage+1):
		result = requests.get(f"{URL}&pg={p}")
		soup = BeautifulSoup(result.text, "html.parser")
		jobid = soup.find_all("div", {"class":"-job"})
		for j in jobid:
			jobs.append(extract_job(j))
		print(f"Scrapped SO p.{p}")

	return jobs

def get_jobs():
	lp = extract_last_page()
	jobs = extract_jobcard(2)
	return jobs

if __name__ == "__main__":
	get_jobs()