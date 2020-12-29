import requests
import re
from bs4 import BeautifulSoup

from authorization import prostev

url = 'https://schools.school.mosreg.ru/marks.aspx?school=14874&index=5&tab=period&homebasededucation=False'
url_login = 'https://login.school.mosreg.ru/'

session = requests.Session()
authorization = session.post(url_login, data=prostev)


request = requests.get(url)
client = requests.session()


with open('marks.html', 'w') as output_file:
    output_file.write(request.text)