import requests
from bs4 import BeautifulSoup

# Function to fetch HTML content from a URL
def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve HTML. Status code: {response.status_code}")
        return None

# Function to extract data using BeautifulSoup
def extract_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Your scraping logic goes here
    # Use soup.find(), soup.find_all(), etc., to locate and extract the desired data

    # Example: Extracting all the links on the page
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))

# Main function to run the scraper
def main():
    # URL of the website you want to scrape
    url = 'https://example.com'

    # Get HTML content
    html_content = get_html(url)

    if html_content:
        # Extract data
        extract_data(html_content)

if __name__ == "__main__":
    main()
