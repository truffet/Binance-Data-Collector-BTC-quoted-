# Binance BTC Trading Pairs Historical Data Fetcher

This collection of Python scripts fetches historical candlestick data for all spot BTC trading pairs (plus the BTCUSDT pair) on Binance and stores the data into separate files in different folders for each pair.

## Files
- `config.py`: This file contains the configuration constants.
- `api.py`: This file contains the functions for interacting with the Binance API.
- `utils.py`: This file contains utility functions like writing data to a CSV file.
- `main.py`: This file contains the main logic of the script.

## Usage
1. Make sure you have Python 3 installed.
2. Install the necessary Python libraries by running `pip install pandas requests`.
3. Run the `main.py` script with `python main.py`.

This script will create a `data` directory and inside it, folders for each trading pair. Inside these folders, it will create and update CSV files for daily and weekly candlestick data.
