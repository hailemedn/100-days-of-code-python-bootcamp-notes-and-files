from bs4 import BeautifulSoup
import lxml

# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
# all_anchor_tags = soup.findAll(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# # works similar to css selectors
# # company_url = soup.select_one(selector="#name")
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# soup.select(selector=".heading")

# grab live website
import requests
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# link_tag = soup.select_one(selector="span.titleline a")
# article_text = link_tag.getText()
# article_link = link_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").getText()
# print(article_text)
# print(article_link)
# print(article_upvote)

article_spans = soup.findAll(name="span", class_="titleline")
article_texts = [span.a.getText() for span in article_spans]
article_links = [span.a.get("href") for span in article_spans]


soup.findAll(name="span", class_="score")


article_upvote = [int(score.getText().split()[0]) for score in soup.findAll(name="span", class_="score")]


print(article_texts)
print(article_links)
print(article_upvote)

largest_upvote = max(article_upvote)
largest_index = article_upvote.index(largest_upvote)

print(article_texts[largest_index])
print(article_links[largest_index])

# web scraping Law
# public data, not copyrighted is a fair game
# You can't scrape Data behind Authentication.

# web scraping Ethics
# public API First
# Respect the web owner
# news/ycombinator.com/robots.txt - let's you know what you can't scrape


