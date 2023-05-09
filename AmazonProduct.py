import requests
from bs4 import BeautifulSoup


class AmazonProduct:
    def __init__(self, url="https://www.amazon.com/"):
        self.url = url

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
            "Accept-Language": "en-GB,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-US;q=0.6",
        }

        response = requests.get(url, headers=self.headers)
        content = response.content
        # print(content)
        with open("amazon.html", "w") as file:
            file.write(
                f"""
                    {content}
                    """
            )

        self.soup = BeautifulSoup(content, "html.parser")

    def get_product_price(self):
        prices_whole = self.soup.find_all("span", class_="a-price-whole")
        prices_fraction = self.soup.find_all("span", class_="a-price-fraction")

        product_price = prices_whole[0].text + prices_fraction[0].text
        product_price = float(product_price)
        return product_price
