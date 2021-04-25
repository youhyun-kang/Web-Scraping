import re
import requests
from bs4 import BeautifulSoup

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    print()
    print("[Today's Weather]")
    url = "https://weather.com/weather/tenday/l/Bedford+TX?canonicalCityId=87220e95df4e2392abb2a4653a37d5089e152446497b7ce6997caead596cfc2f"
    soup = create_soup(url)
    cast = soup.find("p data-testid" == "wxPhrase", attrs={"class":"DailyContent--narrative--3AcXd"}).get_text()    
    curr_temp = soup.find("span data-testid" == "TemperatureValue", attrs={"class":"DailyContent--temp--_8DL5"}).get_text()
    min_temp = soup.find("span data-testid" == "TemperatureValue", attrs={"class":"DetailsSummary--lowTempValue--1DlJK"}).get_text()
    max_temp = soup.find("span data-testid" == "TemperatureValue", attrs={"class":"DetailsSummary--highTempValue--3x6cL"}).get_text()
    rain_rate = soup.find("span data-testid" == "PercentageValue", attrs={"class":"DailyContent--value--3Xvjn"}).get_text()

    print(cast)
    print("Current {} (Min {} / Max {})".format(curr_temp, min_temp, max_temp))
    print("Chace of Rain {}".format(rain_rate))
    print()

def scrape_headline_news():
    print("[News Headlines]")
    url = "https://www.bbc.com/news"
    soup = create_soup(url)
    main_news = soup.find("div", attrs = {"class":"gel-layout gel-layout--no-flex nw-c-top-stories--standard nw-c-top-stories--international"}).find_all("div class" == "gs-c-promo-body gs-u-display-none gs-u-display-inline-block@m gs-u-mt@xs gs-u-mt0@m gel-1/3@m", limit = 1)
    sub_news = soup.find("div", attrs = {"class":"gel-layout__item nw-c-top-stories__secondary-item gel-1/1 gel-1/3@m gel-1/4@l nw-o-keyline nw-o-no-keyline@m gs-u-float-left nw-c-top-stories__secondary-item--2 gel-1/5@xxl"}).find_all("div class"=="gs-c-promo-body gel-1/2@xs gel-1/1@m gs-u-mt@m", limit = 1)
    sub_news2 = soup.find("div", attrs = {"class":"gel-layout__item nw-c-top-stories__secondary-item gel-1/1 gel-1/3@m gel-1/4@l nw-o-keyline nw-o-no-keyline@m gs-u-float-left nw-c-top-stories__secondary-item--1 gel-3/16@xxl gs-u-float-none@xxl gs-u-mt gs-u-mt0@xs"}).find_all("div class" == "gs-c-promo nw-c-promo gs-u-pb gs-u-pb+@m gs-u-mh0 gs-c-promo--flex", limit = 1)

    for index, news in enumerate(main_news):
        title = news.find("h3").get_text()
        link = url.strip("/news") + news.find("a")["href"]
        print("{}. {}".format(index+1, title))
        print(" (Link : {})". format(link))

    for index, news in enumerate(sub_news):
        title = news.find("h3").get_text()
        link = url.strip("/news") + news.find("a")["href"]
        print("{}. {}".format(index+2, title))
        print(" (Link : {})". format(link))
    
    for index, news in enumerate(sub_news2):
        title = news.find("h3").get_text()
        link = url.strip("/news") + news.find("a")["href"]
        print("{}. {}".format(index+3, title))
        print(" (Link : {})". format(link))
    print()

def scrape_idiom():
    print("[Idiom of the Day]")
    url = "https://www.englishclub.com/ref/idiom-of-the-day.php"
    soup = create_soup(url)
    sentences = soup.find("h2", attrs = {"class":"clr-green"}).get_text()
    search = soup.find_all("p")
    meaning = search[1].get_text()

    print("\"{}\"".format(sentences))
    print("Meaning: {}".format(meaning))
    print()

   
if __name__ == "__main__":
    scrape_weather()
    scrape_headline_news() 
    scrape_idiom()
