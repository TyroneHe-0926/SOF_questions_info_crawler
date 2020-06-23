from bs4 import BeautifulSoup
import requests
import random
import numpy as np
import pandas as pd
import os


response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")
questions = soup.select(".question-summary")

for question in questions:
    qt = question.select_one(".question-hyperlink").getText()
    print(qt)
    
        # print("Question Title:", qt)
        # print("Tags:", tags)
        # print("User asked:", user_name)
        # print("Date asked:", time_asked_UTC)
        # print("Votes: ", votes_count)
        # print("Views: ", views_count)