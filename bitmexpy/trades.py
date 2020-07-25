from bitmexpy.utils import available_symbols
import pandas as pd
import requests


def trades(
    symbol = "XBTUSD",
    count="1000",
    reverse="true",
    startTime="2020-01-01"
):

    url = (
        "https://www.bitmex.com/api/v1/trade?partial=false&"
        + "reverse="
        + reverse
        + "&symbol="
        + symbol
        + "&count="
        + count
        + "&startTime="
        + startTime
    )

    df = requests.get(url)

    result = pd.read_json(df.content, orient="records")

    return result

