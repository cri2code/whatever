import requests
from bs4 import BeautifulSoup
from datetime import datetime

def check_price():
    url = "https://www.emag.ro/tableta-samsung-galaxy-tab-s10-lite-10-9-8gb-ram-256gb-5g-gray-sm-x406bzapeue/pd/DM78TS3BM/?ref=fam"
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find price - adjust selector if needed
        price_elem = soup.find('p', class_='product-new-price')
        if price_elem:
            price = price_elem.text.strip()
        else:
            price = "Price element not found"
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{timestamp}] Current price: {price}")
        
        # Save to file
        with open('price_history.txt', 'a') as f:
            f.write(f"[{timestamp}] {price}\n")
        
        return price
        
    except Exception as e:
        print(f"Error checking price: {e}")
        return None

if __name__ == "__main__":
    check_price()
