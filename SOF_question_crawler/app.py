from bs4 import BeautifulSoup
import requests
import random
import numpy as np
import pandas as pd
import os
from config import *


response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")
pages = np.arange(1, 500, 50)
questions = soup.select(".question-summary")

try:
    for page in pages:
        for question in questions:
            tags = []
            for tag in question.select('.tags'):
                tagstr = str(tag.getText()).split()
                for tag in tagstr:
                    tags.append(tag)
            qt = question.select_one(".question-hyperlink").getText()
            votes_count = question.select_one(".vote-count-post").getText()
            views_count = question.select_one(".views").getText()
            time_asked_z = str(
                question.find(class_='user-action-time').find('span').get("title"))
            time_asked_UTC = time_asked_z.replace('Z', " UTC")
            user_name = str(question.find(
                class_='user-details').find('a').get('href'))
            question_title.append(qt)
            votes.append(votes_count)
            views.append(views_count)
            time.append(time_asked_UTC)
            user.append(user_name)
            question_tags_list.append(tags)
        page = requests.get("https://stackoverflow.com/questions?tab=newest&page=" +
                            str(page) + "&ref_=adv_nxt")
        soup = BeautifulSoup(page.text, 'html.parser')
        questions = soup.select(".question-summary")
        question_div = soup.find_all(
            'div', class_='s-pagination--item js-pagination-item')
except AttributeError:
    pass

summary = pd.DataFrame({
    'question': question_title,
    'votes': votes,
    'views': views,
    'time_asked': time,
    'user_asked': user,
    'tags': question_tags_list
})

summary['question'] = summary['question'].astype(str)
summary['time_asked'] = summary['time_asked'].astype(str)
summary['user_asked'] = summary['user_asked'].astype(str)
summary['votes'] = summary['votes'].astype(str)
summary['views'] = summary['views'].astype(str)
summary['tags'] = summary['tags'].astype(str)

summary.to_csv('sto_questions.csv')
