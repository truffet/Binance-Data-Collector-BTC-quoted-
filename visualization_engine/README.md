# Binance BTC Trading Pairs Data Visualizer

This Python script reads the historical candlestick data for a specified trading pair and displays the daily and weekly candlestick graphs with volume.

## Requirements

You will need the following:

- Python 3
- pandas
- matplotlib
- mplfinance

## Installation

First, ensure that you have Python 3 installed on your system.

Next, install the necessary Python libraries using pip. You can do this by running the following command in your terminal:

\`\`\`sh
pip install pandas matplotlib mplfinance
\`\`\`

## Usage

To use this script, follow these steps:

1. Run the script by typing `python visualizer.py` into your terminal.

2. When prompted, enter the trading pair you want to visualize (e.g., "BTCUSDT").

3. The script will display the weekly and daily candlestick graphs with volume for the specified trading pair.

## Notes

- This script assumes that you have already fetched the historical data using the Binance BTC Trading Pairs Historical Data Fetcher scripts and stored the data in a folder named `data` one level up in the directory structure.
- The trading pair name should be entered in all uppercase letters (e.g., "BTCUSDT").
