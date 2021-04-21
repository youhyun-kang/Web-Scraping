import re
import requests
from bs4 import BeautifulSoup

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    print("[Today's Weather]")
    url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()    
    curr_temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨", "")
    min_temp = soup.find("span", attrs={"class":"min"}).get_text()
    max_temp = soup.find("span", attrs={"class":"max"}).get_text()
    morning_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().replace("강수확률", "").strip() 
    afternoon_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().replace("강수확률", "").strip() 

    print(cast)
    print("Current {} (Min {} / Max {})".format(curr_temp, min_temp, max_temp))
    print("Chace of Rain (AM {} / PM {})".format(morning_rain_rate, afternoon_rain_rate))
    print()

if __name__ == "__main__":
    scrape_weather()