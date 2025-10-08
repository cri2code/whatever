import requests
from bs4 import BeautifulSoup
from datetime import datetime

def check_price(product_url):
    try:
        response = requests.get(product_url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Adjust selector for your website
        price = soup.find('span', class_='price').text
        
        # Log to file
        with open('price_log.txt', 'a') as f:
            f.write(f"[{datetime.now()}] Price: {price}\n")
        
        print(f"Price checked: {price}")
        return price
    except Exception as e:
        print(f"Error: {e}")

# Run once when script executes
check_price("https://www.emag.ro/tableta-samsung-galaxy-tab-s10-lite-10-9-8gb-ram-256gb-5g-gray-sm-x406bzapeue/pd/DM78TS3BM/?ref=fam#Gri")
