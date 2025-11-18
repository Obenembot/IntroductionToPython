import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"  # An example website for scraping
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

page_title = soup.title.string
print(f"Page Title: {page_title}\n")

book_titles = soup.find_all("h3")
print("Book Titles:")
for title_tag in book_titles:
    # The actual title text is usually within an <a> tag inside the <h3>
    link_tag = title_tag.find("a")
    if link_tag:
        print(f"- {link_tag.get('title')}")
prices = soup.find_all("p", class_="price_color")
print("\nProduct Prices:")
for price_tag in prices:
    print(f"- {price_tag.get_text().strip()}")

# Find the first link on the page
first_link = soup.find("a")
if first_link:
    print(f"\nFirst Link Href: {first_link.get('href')}")