import requests
from bs4 import BeautifulSoup 


url = "https://www.amazon.com/BENGOO-G9000-Controller-Cancelling-Headphones/dp/B01H6GUCCQ/ref=sr_1_3?keywords=gaming%2Bheadsets&pd_rd_r=f576e6eb-6cc9-4278-bc52-8513192288ed&pd_rd_w=vwjVA&pd_rd_wg=VIEzn&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=X9FR0ABG4C9TTE8T7J7J&qid=1683649819&sr=8-3&th=1"

headers = {
           "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
           "Accept-Language":"en-GB,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-US;q=0.6"
            }

response = requests.get(url, headers=headers)
content = response.content
# print(content)
with open("amazon.html", "w") as file:
    file.write(f"""
               {content}
               """)

soup = BeautifulSoup(content, 'html.parser')
whole_prices = soup.find_all("span", class_="a-price-whole")
product_price = whole_prices[0].get_text()
print(f"product_price = {product_price}")
