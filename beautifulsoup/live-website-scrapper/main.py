import requests
from bs4 import BeautifulSoup
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
# print(articles)
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)


upvote = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_="score")]

largest_number = max(upvote)
largest_index = upvote.index(largest_number)
print(article_texts)
print(article_links)
print(upvote)

print(largest_index)
print(largest_number)

