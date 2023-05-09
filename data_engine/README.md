# Binance Data Collector

This project fetches and updates the daily and weekly candlestick data for all spot BTC trading pairs (and the BTCUSDT pair) on Binance and stores this data into CSV files, which are organized in separate folders for each pair. The data is collected via the Binance API.

## File Structure

- `api.py`: Contains functions that interact with the Binance API.
- `config.py`: Stores global configurations for the project.
- `utils.py`: Contains utility functions used across the project.
- `main.py`: Main script that uses functions from `api.py` and `utils.py` to fetch and update the data.

## How to Run

1. Make sure you have Python 3 installed on your machine.

2. Install the necessary Python packages:

    ```
    pip install pandas requests
    ```

3. Run the main script:

    ```
    python main.py
    ```

## Output

The script will create a data directory, within which there will be separate folders for each trading pair. Inside each of these folders, there will be two CSV files for each pair: one for daily data and one for weekly data. These CSV files will be updated if they already exist.

The CSV files have the following columns: 'Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', and 'Ignore'.
