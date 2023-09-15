
from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
page = r.text

soup = BeautifulSoup(page, "html.parser")

movie_titles_numbered = [title.getText() for title in soup.find_all(class_="listicleItem_listicle-item__title__hW_Kn")]
movie_titles = [title.split(") ")[1] for title in movie_titles_numbered]
movie_titles.reverse()
# print(movie_titles)

with open("movie_to_watch.txt", "w") as file:
    for title in movie_titles:
        file.write(title + "\n")
