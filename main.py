import requests
from bs4 import BeautifulSoup
from AmazonProduct import AmazonProduct
from email.message import EmailMessage
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()
email = os.getenv("MY_EMAIL")
passWord = os.getenv("EMAIL_PASSWORD")
email_to = "kirolosyassa2017@gmail.com"

url = "https://www.amazon.com/SanDisk-MicroSDXC-Memory-Nintendo-Switch/dp/B07QD6R5L7/ref=pd_rhf_d_dp_s_pd_crcbs_sccl_2_3/143-7024595-4034758?pd_rd_w=A3Jga&content-id=amzn1.sym.31346ea4-6dbc-4ac4-b4f3-cbf5f8cab4b9&pf_rd_p=31346ea4-6dbc-4ac4-b4f3-cbf5f8cab4b9&pf_rd_r=1EKPE8J3AFSHGWCMWTYT&pd_rd_wg=4A8Kn&pd_rd_r=8b468908-a908-4a6d-bf56-558177ed296a&pd_rd_i=B07QD6R5L7&psc=1"
# url = input("Enter your required product on Amazon: ")
max_product_price = 27

product = AmazonProduct(url=url)
product_price = product.get_product_price()
print(f"product_price = {product_price}")
print(f"product_price <= max_product_price ~~~~> {product_price <= max_product_price}")

if product_price <= max_product_price:
    with open("Email Content.txt", "r") as file:
        message = file.read()

    message = message.replace("[PRICE]", str(max_product_price))
    message = message.replace("[WEBSITE]", url)

    msg = EmailMessage()
    msg["Subject"] = f"Amazon Product Price Alert"
    msg["From"] = "Amazon Alert"
    msg["To"] = email_to
    msg.set_content(message, subtype="html")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=passWord)
        connection.send_message(msg)
