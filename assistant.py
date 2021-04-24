import re
import requests
from bs4 import BeautifulSoup

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def print_news(index, title, link):
    print("{}. {}".format(index+1, title))
    print(" (Link : {})". format(link))

# def scrape_weather():
#     print("[Today's Weather]")
#     url = "https://weather.com/weather/tenday/l/Bedford+TX?canonicalCityId=87220e95df4e2392abb2a4653a37d5089e152446497b7ce6997caead596cfc2f"
#     soup = create_soup(url)
#     cast = soup.find("p data-testid" == "wxPhrase", attrs={"class":"DailyContent--narrative--3AcXd"}).get_text()    
#     curr_temp = soup.find("span data-testid" == "TemperatureValue", attrs={"class":"DailyContent--temp--_8DL5"}).get_text()
#     min_temp = soup.find("span data-testid" == "TemperatureValue", attrs={"class":"DetailsSummary--lowTempValue--1DlJK"}).get_text()
#     max_temp = soup.find("span data-testid" == "TemperatureValue", attrs={"class":"DetailsSummary--highTempValue--3x6cL"}).get_text()
#     rain_rate = soup.find("span data-testid" == "PercentageValue", attrs={"class":"DailyContent--value--3Xvjn"}).get_text()

#     print(cast)
#     print("Current {} (Min {} / Max {})".format(curr_temp, min_temp, max_temp))
#     print("Chace of Rain {}".format(rain_rate))
#     print()

def scrape_headline_news():
    print("[News Headlines]")
    url = "https://www.bbc.com/news"
    soup = create_soup(url)
    main_news = soup.find("div", attrs = {"class":"gel-layout gel-layout--no-flex nw-c-top-stories--standard nw-c-top-stories--international"}).get_text()
#    main1 = soup.find("h3", attrs={"class":"gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text"})
    for index, news in enumerate(main_news):
        title = news.find("h3", attrs={"class":"gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text"}).get_text()
        link = news.find("a"== "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor")["href"]
        print_news(index, title, link)
    # news_list = soup.find("h3", attrs={"class"=="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text"}).get_text()
    # print(news_list)
    # for index, news in enumerate(news_list):
    #     title = news.find("a class"== "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor").get_text()
    #     link = news.find("a class"== "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor")["href"]
    #     print_news(index, title, link)

#     print(cast)
#     print("Current {} (Min {} / Max {})".format(curr_temp, min_temp, max_temp))
#     print("Chace of Rain {}".format(rain_rate))
#     print()
    

if __name__ == "__main__":
    # scrape_weather()
    scrape_headline_news() 