import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

def check_price():
    url = "https://www.emag.ro/tableta-samsung-galaxy-tab-s10-lite-10-9-8gb-ram-256gb-5g-gray-sm-x406bzapeue/pd/DM78TS3BM/?ref=fam"
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'ro-RO,ro;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0',
        }
        
        session = requests.Session()
        response = session.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Try multiple selectors
        price = None
        selectors = [
            ('p', 'product-new-price'),
            ('span', 'product-new-price'),
            ('p', {'class': 'product-new-price'}),
        ]
        
        for tag, class_name in selectors:
            price_elem = soup.find(tag, class_=class_name)
            if price_elem:
                price = price_elem.text.strip()
                break
        
        if not price:
            price = "Price not found - check selectors"
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{timestamp}] Current price: {price}")
        
        # Save to file
        with open('price_history.txt', 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {price}\n")
        
        return price
        
    except requests.exceptions.HTTPError as e:
        error_msg = f"HTTP Error {e.response.status_code}: {e}"
        print(error_msg)
        with open('price_history.txt', 'a', encoding='utf-8') as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {error_msg}\n")
        return None
    except Exception as e:
        error_msg = f"Error: {e}"
        print(error_msg)
        with open('price_history.txt', 'a', encoding='utf-8') as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {error_msg}\n")
        return None

if __name__ == "__main__":
    check_price()
