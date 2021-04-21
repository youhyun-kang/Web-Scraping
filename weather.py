import requests
from bs4 import BeautifulSoup

def scrape_weather():
    print("[Today's Weather]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%AF%B8%EA%B5%AD%20%EB%8C%88%EB%9F%AC%EC%8A%A4%20%EB%82%A0%EC%94%A8"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    cast = soup.find("p", attrs = {"class":"cast_txt"}).get_text()
    curr_temp = soup.find("p", attrs = {"class":"info_temperature"}).get_text()
    min_temp = soup.find("span", attrs = {"class":"min"}).get_text()
    max_temp = soup.find("span", attrs = {"class":"max"}).get_text()
    morning_rain_rate = soup.find("span", attrs = {"class":"point_time_morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span", attrs = {"class":"point_time_afternoon"}).get_text().strip()

    print(cast)
    print("Current {} (Min {} / Max {})".format(curr_temp, min_temp, max_temp))
    print("Chance of Rain (Morning {} / Afternoon {})".format(morning_rain_rate, afternoon_rain_rate))

if __name__ == "__main__":
    scrape_weather() 