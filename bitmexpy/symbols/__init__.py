import pandas as pd
import requests

def available_symbols():

    df = requests.get("https://www.bitmex.com/api/bitcoincharts")
    result = pd.read_json(df.content, orient="index").iloc[0]
    result = result.tolist()
    return result

AS = available_symbols()