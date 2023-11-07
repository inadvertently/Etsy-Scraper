from store_response import StoreResponseError, get_store_response
from scraper import scrape_store

def main():
    store_url = input("Please enter the URL of the store or page you'd like to analyze then press enter: ")
    try:
        store_response = get_store_response(store_url)
        if store_response:
            scrape_store(store_response, store_url)
    except StoreResponseError as e:
        print(e)

if __name__ == "__main__":
    main()
