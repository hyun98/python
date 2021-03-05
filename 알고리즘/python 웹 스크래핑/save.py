import csv

def save_to_file(jobs):
	FilePath = "C:/Users/CVRIE/OneDrive - pusan.ac.kr/알고리즘/python으로 웹 스크래퍼 만들기/"#"C:/Users/HYU NOO/OneDrive - pusan.ac.kr/알고리즘/python으로 웹 스크래퍼 만들기/"
	file = open(f"{FilePath}collected_jobs.csv", mode="w", encoding="utf-8") #한글, 영어 호환문제 엑셀에서 한글 나오게하려면 eurko
	writer = csv.writer(file)
	writer.writerow(["title", "company", "location", "link"])
	
	for job in jobs:
		writer.writerow(list(job.values()))	
