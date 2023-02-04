import requests
import json

def get_btc_pairs():
    # API endpoint to retrieve the latest price of all symbols
    url = "https://api.binance.com/api/v3/ticker/price"

    # Make a GET request to the API endpoint
    response = requests.get(url)
    
    # Parse the response JSON
    data = response.json()

    # Create a list to store the BTC pairs
    btc_pairs = []

    # Loop through each symbol in the response
    for pair in data:
        # Check if the symbol ends with "BTC"
        if pair["symbol"].endswith("BTC"):
            # If it does, add it to the list of BTC pairs
            btc_pairs.append(pair["symbol"])

    # Write the list of BTC pairs to a JSON file
    with open("btc_pairs.json", "w") as file:
        json.dump(btc_pairs, file)

    # Return the list of BTC pairs
    return btc_pairs

get_btc_pairs()
# Print a message indicating the operation was successful
print("BTC pairs retrieved and stored in btc_pairs.json")



def count_btc_pairs():
    # Open the btc_pairs.json file
    with open("btc_pairs.json", "r") as file:
        # Load the list of BTC pairs from the file
        btc_pairs = json.load(file)

    # Return the number of BTC pairs
    return len(btc_pairs)

# Call the function to count the number of BTC pairs
count = count_btc_pairs()

# Print the number of BTC pairs
print("Number of BTC pairs:", count)



def get_candlesticks(symbol):
    # Define the API endpoint for the candlestick data
    endpoint = "https://api.binance.com/api/v3/klines"

    # Define the interval (1 day) and the symbol
    params = {
        "interval": "1d",
        "symbol": symbol
    }

    # Make a request to the API endpoint
    response = requests.get(endpoint, params=params)

    # Check the status code of the response
    if response.status_code == 200:
        # Return the list of candlesticks
        return response.json()
    else:
        # Raise an error if the request was not successful
        raise Exception("Request failed with status code: " + str(response.status_code))

def store_candlesticks(candlesticks, symbol):
    # Write the list of candlesticks to a JSON file
    with open("candlesticks_" + symbol + ".json", "w") as file:
        json.dump(candlesticks, file)

# Load the list of BTC pairs from the btc_pairs.json file
with open("btc_pairs.json", "r") as file:
    btc_pairs = json.load(file)

# For each BTC pair
for symbol in btc_pairs:
    # Get the candlestick data
    candlesticks = get_candlesticks(symbol)

    # Store the candlestick data in a JSON file
    store_candlesticks(candlesticks, symbol)

# Print a message indicating the operation was successful
print("Candlestick data for all BTC pairs retrieved and stored in separate JSON files")
