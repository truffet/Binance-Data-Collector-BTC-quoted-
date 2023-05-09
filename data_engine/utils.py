import os
import pandas as pd


def write_data_to_csv(filename, data, append=False):
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    
    mode = 'a' if append else 'w'
    with open(filename, mode) as f:
        data.to_csv(f, header=not append, index=False)
