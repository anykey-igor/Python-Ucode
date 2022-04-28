import requests
import json
import sys
import re
from bs4 import BeautifulSoup
url = sys.argv[1]

try:

    link = requests.get(url)
    beauti_soup = BeautifulSoup(link.content, 'html.parser')
    b_link = beauti_soup.findAll('a', class_="reference external")
    m_list = []
    for key in b_link:
        ltitle = requests.get(key.get('href'))
        lsoup = BeautifulSoup(ltitle.content, 'html.parser')
        title = beauti_soup.find('title')
        m_list.append({"link_text": key.contents[0], "url": key.get('href'), "title": title.string})
    jsonString = json.dumps(m_list)
    head = beauti_soup.find("h1").string
    print(head)

    with open(head, 'w') as f:
        json.dump(all_dicts, f, sort_keys=False, indent=1, ensure_ascii=False)

except Exception as exp:
    exp