from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")
titles_boxes = soup.find_all(name="div", class_="article-title-description__text")
titles = [title.find(name="h3", class_="title").getText() for title in titles_boxes]
titles_reverted = [titles[(len(titles)-x)] for x in range(1, len(titles)+1)]    #or titles[::-1]

with open("movies.txt", "w", encoding="utf8") as my_file:
    for _ in range(0, len(titles)):
        my_file.write(titles_reverted[_] + '\n')
