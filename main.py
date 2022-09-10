#      BeautifulSoup webscraper modified from example provided on StackOverflow
#      https://stackoverflow.com/questions/26002076/python-nltk-clean-html-not-implemented
#      Original author - Michael
#      Modifying author - Caitlin Brown
#      Date modified: 13/07/2022


import mechanize
from bs4 import BeautifulSoup
from html2text import html2text
import re


def clean_html(html):
    # First we remove inline JavaScript/CSS:
    cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
    # Then we remove html comments. This has to be done before removing regular
    # tags since comments can contain '>' characters.
    cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
    # Next we can remove the remaining tags:
    cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
    # Finally, we deal with whitespace
    cleaned = re.sub(r"&nbsp;", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    return cleaned.strip()


url = 'https://www.ncl.ac.uk/singapore/about/staff/'
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]
html = br.open(url).read().decode('utf-8')
cleanhtml = clean_html(html)
text = html2text(cleanhtml)
soup = BeautifulSoup(html, 'lxml')
text2 = soup.get_text()
print(text2)

with open('url.txt', 'w', encoding='utf-8') as f:
    f.write(text2)
f.close()
