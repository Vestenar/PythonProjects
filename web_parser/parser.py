# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from authorization import headers
import json

minimal_lenghth = 100


def parse(index):
    url_parse = 'http://teamfinding.com/ru/project/show/' + str(index)
    resp = requests.get(url_parse, headers=headers)
    resp.encoding = 'utf-8'

    if resp.status_code != 200:
        print(f'Page {index=} not found')
        return False

    soup = BeautifulSoup(resp.content, 'lxml')

    try:
        print(f"PROJECT PAGE {index=}")
        project_title = soup.title.text[:-13].strip()
        soup_text = soup.find('div', {'class': 'public-project-describe'})
        raw_text = soup_text.text.strip().replace('\r\n', '').replace('\n\r', '').replace('\t', '')
        if len(raw_text) < minimal_lenghth:
            return False

        project_text = json.dumps([{'data': {'text': raw_text}, 'type': 'paragraph'}], ensure_ascii=False)
        raw_tags = soup.find('div', {'class': 'public-project-specialization'})
        if raw_tags:
            tags = [raw_tags.contents[i].text.strip() for i in range(1, len(raw_tags.contents), 4)]
        else: tags = []
        # Author
        span3 = soup.find('div', {'class': 'span3 well'})
        author = {"name": span3.contents[5].contents[1], "link": span3.contents[5].attrs['href'].split('/')[-1]}

        data_to_fill_db = [(project_title, project_text, tags), author]
        return data_to_fill_db

    except AttributeError:
        return False
