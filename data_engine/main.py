import os
import pandas as pd
from api import fetch_trading_pairs, fetch_klines
from utils import write_data_to_csv
from config import DATA_FOLDER


def main():
    trading_pairs = fetch_trading_pairs()

    for pair in trading_pairs:
        print(f"Processing trading pair {pair}...")

        for interval in ['1d', '1w']:
            filename = f"{DATA_FOLDER}/{pair}/{pair}_{interval}.csv"

            if os.path.exists(filename):
                df = pd.read_csv(filename)
                last_date = pd.to_datetime(int(df["Close time"].iloc[-1]), unit="ms")
                new_klines = fetch_klines(pair, interval, start_str=int(last_date.timestamp() * 1000))
                new_df = pd.DataFrame(new_klines)
                df = pd.concat([df, new_df], ignore_index=True)
            else:
                klines = fetch_klines(pair, interval)
                df = pd.DataFrame(klines)

            write_data_to_csv(filename, df, append=True)


if __name__ == "__main__":
    main()
