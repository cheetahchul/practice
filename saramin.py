import requests
from bs4 import BeautifulSoup

start = 1
URL = f"https://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=auto&searchword=PYTHON&recruitPage={start}&recruitSort=relation&recruitPageCount=100"


def get_last_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all("a")
    pages = []
    for link in links[0:-1]:
        pages.append(int(link.string))

    last_page = pages[-1]
    return last_page


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapper page {page}")
        result = requests.get(f"{URL}{page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "area_job"})
        for result in results:
            title = result.find("h2", {"class": "job_tit"})
            anchor = title.find("a")["title"]
            return anchor


def extract_company(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}{page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        companys = soup.find_all("div", {"class": "area_corp"})
        for company in companys:
            company_name = company.find(
                "strong", {"class": "corp_name"}).find("a")["title"]
            print(company_name)
