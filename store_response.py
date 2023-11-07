import requests

class StoreResponseError(Exception):
    pass

def get_store_response(url):
    store_response = requests.get(url)
    print("Status code:", store_response.status_code)
    
    if store_response.status_code != 200:
        print("Response content:", store_response.content)  # Print the response content
        raise StoreResponseError(f"Failed to fetch the store response. Status code: {store_response.status_code}")
    
    return store_response
