import pandas as pd
import requests


def trades(
    symbol = "XBTUSD",
    count="1000",
    reverse="true",
    start_date="2020-01-01",
    end_date=""
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
        + start_date
    )

    df = requests.get(url)

    result = pd.read_json(df.content, orient="records")

    return result

