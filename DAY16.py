Day 16 of the 90 days python challenge  



import requests
from bs4 import BeautifulSoup

def scrape_news_headlines():
    url = "https://www.bbc.com/news"
    
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        
        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all headline elements
        # Note: Website structures change often - may need to update selectors
        headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')
        
        print("Latest BBC News Headlines:")
        print("-" * 50)
        
        # Display headlines with numbering
        for i, headline in enumerate(headlines[:10], 1):  # Show top 10 headlines
            headline_text = headline.get_text().strip()
            print(f"{i}. {headline_text}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    scrape_news_headlines()