#Day 17 of the 90 days python challenge 



from urllib.request import urlopen

def fetch_url(url):
    try:
        with urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(f"Status Code: {response.status}")
            print("Headers:")
            for header, value in response.getheaders():
                print(f"  {header}: {value}")
            print("\nContent:")
            print(content[:1000])  # Print first 1000 chars to avoid flooding console
    except Exception as e:
        print(f"Error fetching URL: {e}")

if __name__ == "__main__":
    url = input("Enter URL to fetch (include http:// or https://): ")
    fetch_url(url)
