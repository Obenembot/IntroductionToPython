import requests
from bs4 import BeautifulSoup

url = "https://hpaisaglobal.nvizible.co.za/cms/login"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

jobs_data = []

print('soup', response.status_code)
print('soup',soup)


