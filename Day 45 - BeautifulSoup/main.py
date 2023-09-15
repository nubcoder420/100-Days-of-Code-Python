from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

# article_tag = soup.find(class_="titleline")
# print(article_tag.get_text("a"))
#
# article_text = article_tag.get_text()
# print(article_text)
#
# article_link = article_tag.find("a")["href"]
# print(article_link)
#
# article_score = soup.find(id="score_37519066").get_text()
# print(article_score)

#--------- get the article titles ------------#
article_tags = soup.select(".titleline")
articles = [article_tag.getText() for article_tag in article_tags]
print(articles)

#--------- get the article links ------------#
article_links = [link.get("href") for link in soup.select(".titleline a") if link.get("href").startswith("http")]
print(article_links)

#--------- get the article upvotes ------------#
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(class_="score")]
print(article_upvotes)

#--------- get the article and link with most upvotes ------------#
max_upvotes_index = article_upvotes.index(max(article_upvotes))
max_upvote_article = articles[max_upvotes_index]
max_upvote_link = article_links[max_upvotes_index]
print(max_upvote_article)
print(max_upvote_link)
