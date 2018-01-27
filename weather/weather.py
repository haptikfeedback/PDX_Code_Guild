import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    response = requests.get('https://katu.com/weather')
    response.raise_for_status()

    html = BeautifulSoup(response.text, 'html.parser')
    rows = html.find_all('td')

    forecast = [row for row in rows if 'daily-forecast' in row.get('class', '')]

    print(len(forecast))