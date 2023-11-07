import httpx, re
from bs4 import BeautifulSoup
from pdf_creator import make_pdf

def scrape_store(store_response, store_url):
    store_soup = BeautifulSoup(store_response.text, 'html.parser')
    listings = store_soup.find_all('a', {'class': 'listing-link'})
    pagination_element = store_soup.find_all('p', {'class': 'wt-action-group__item'})
    if pagination_element:
        pagination_text_list = [elem.get_text() for elem in pagination_element]
        pattern = re.compile(r'^Page \d+ of \d+$')
        page_of_y_text = [text for text in pagination_text_list if pattern.match(text)]
        if page_of_y_text:
            total_pages_text = page_of_y_text[0]
            total_pages = int(re.search(r'\d+', total_pages_text[::-1]).group()[::-1])
            print(total_pages)
        else:
            print("No pagination detected via this shop's URL")

    for page in range(1, total_pages + 1):
        page_url = f"{store_url}?page={page}#items"
        print(page)
        print(page_url)
        page_response = httpx.get(page_url)
        page_soup = BeautifulSoup(page_response.text, 'html.parser')
        listings = page_soup.find_all('a', {'class': 'listing-link'})

        for listing in listings:
            listing_url = listing['href']
            listing_response = httpx.get(listing_url)
            listing_soup = BeautifulSoup(listing_response.text, 'html.parser')
            description_element = listing_soup.find('p', {'class': 'wt-text-body-01 wt-break-word'})

            if description_element is not None:
                description_text = description_element.get_text()
                description_text = description_text[:4990] + (description_text[4990:] and '..')
                print(description_text)

            # Translate the description to Spanish

            listing_name_element = listing_soup.find('h1', {'class': 'wt-text-body-01 wt-line-height-tight wt-break-word wt-mt-xs-1'})
            if listing_name_element:
                listing_name = listing_name_element.get_text().strip()
                listing_name = listing_name.replace(" ", "-")  #
                listing_name = listing_name.replace("/", "-")
                listing_name = listing_name.replace(".", "")
                listing_name = listing_name.replace('"', "")
                listing_name = listing_name.replace('%', "")
            else:
                listing_name = "Untitled Listing"

            make_pdf(listing_name, description_text)

            # Export translated description to PDF