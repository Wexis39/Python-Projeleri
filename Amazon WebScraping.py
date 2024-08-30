import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com.tr/gp/bestsellers/computers"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

html = requests.get(url,headers=headers).content

soup = BeautifulSoup(html,'html.parser')

general_div = soup.find("div",{"class":"p13n-gridRow _cDEzb_grid-row_3Cywl"})

for item in general_div:
    try:
        name =  item.find("div",{"class":"_cDEzb_p13n-sc-css-line-clamp-3_g3dy1"}).text
        price = item.find("span",{"class":"_cDEzb_p13n-sc-price_3mJ9Z"}).text
        with open('Laptos.txt','a',encoding='utf-8') as f:
            f.write(f'{name}\n{price}\n')
    except:
        continue