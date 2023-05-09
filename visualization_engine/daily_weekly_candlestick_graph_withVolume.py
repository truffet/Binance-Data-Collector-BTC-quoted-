import pandas as pd
import mplfinance as mpf

def visualize_candlestick(pair):
    daily_filename = f'../data/{pair}/{pair}_1d.csv'
    weekly_filename = f'../data/{pair}/{pair}_1w.csv'

    daily_df = pd.read_csv(daily_filename, header=None, names=['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close_time', 'Quote_asset_volume', 'Number_of_trades', 'Taker_buy_base_asset_volume', 'Taker_buy_quote_asset_volume', 'Ignore'])
    weekly_df = pd.read_csv(weekly_filename, header=None, names=['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close_time', 'Quote_asset_volume', 'Number_of_trades', 'Taker_buy_base_asset_volume', 'Taker_buy_quote_asset_volume', 'Ignore'])

    daily_df['Date'] = pd.to_datetime(daily_df['Date'], unit='ms')
    weekly_df['Date'] = pd.to_datetime(weekly_df['Date'], unit='ms')

    daily_df.set_index('Date', inplace=True)
    weekly_df.set_index('Date', inplace=True)

    mpf.plot(daily_df, type='candle', style='charles', title=f'{pair} Daily chart', volume=True, ylabel='Price', datetime_format='%Y-%m-%d %H:%M:%S')
    mpf.plot(weekly_df, type='candle', style='charles', title=f'{pair} Weekly chart', volume=True, ylabel='Price', datetime_format='%Y-%m-%d %H:%M:%S')

def main():
    pair = input("Enter the trading pair: ")
    visualize_candlestick(pair)

if __name__ == "__main__":
    main()
