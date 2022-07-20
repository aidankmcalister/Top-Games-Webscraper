from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = 'https://newzoo.com/insights/rankings/top-20-pc-games'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("table", {"class": "rankingtable"})

for container in containers:

    rows = container.findAll("tr", {"class":"ranking-row"})
    for row in rows:
        rank_numberUnstripped = row.find("div", {"class":"rank-number"})
        game_titleUnstripped = row.find("a")
        column = row.find("td")
        publisherUnstripped = column.find_next_sibling("td").find_next_sibling("td")
        gameTitle = game_titleUnstripped.text.strip()
        publisher = publisherUnstripped.text.strip()
        rankNumber = rank_numberUnstripped.text.strip()

        content = (rankNumber + "  " + gameTitle + "  |  " + publisher)
        print(content)



