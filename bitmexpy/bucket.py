import requests
import pandas as pd
from datetime import datetime
from time import sleep
from bitmexpy import symbols


def bucket_trades(
    symbol="XBTUSD", count="1000", binSize="1d", reverse="true", startTime="2020-01-01"
):
    """
    bucket_trades() retrieves open high low close (OHLC) data for the specified symbol/time frame.
    The API will only return 1000 rows per call. If the desired time frame requires more than one API call,
    consider using map_bucket_trades().

    Args:
        symbol (str, optional): Instrument ticker. Defaults to "XBTUSD".
        count (str, optional): Number of rows to return. Defaults to "1000".
        binSize (str, optional): The time interval to bucket by, must be one of: 
        "1m", "5m", "1h" or "1d". Defaults to "1d".
        reverse (str, optional): If "true", result will be ordered with starting with the newest. Defaults to "true".
        startTime (str, optional): Start date of data. Defaults to "2020-01-01".

    Returns:
        pandas df: dataframe containing bucketed trade data
    """

    if symbol not in symbols.AS:
        print("Symbol must be one of:")
        print(*symbols.AS, sep="\n")
        return

    url = (
        "https://www.bitmex.com/api/v1/trade/bucketed?partial=false&"
        + "reverse="
        + reverse
        + "&binSize="
        + binSize
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


def map_bucket_trades(
    symbol="XBTUSD",
    count="1000",
    binSize="1d",
    reverse="true",
    startTime="2015-09-25 13:00:00",
    endTime=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
):
    """Bucket trade data over an extended period

    Args:
        symbol (str, optional): Instrument ticker. Defaults to "XBTUSD".
        count (str, optional): Number of rows to return. Defaults to "1000".
        binSize (str, optional): The time interval to bucket by, must be one of: 
        "1m", "5m", "1h" or "1d". Defaults to "1d".
        reverse (str, optional): If "true", result will be ordered with starting with the newest. Defaults to "true".
        startTime (str, optional): Start date of data. Defaults to "2015-09-25 13:00:00".
        endTime ([type], optional): End date of data. Defaults to datetime.now().strftime("%Y-%m-%d %H:%M:%S").

    Returns:
        pandas df: dataframe containing bucketed trade data
    """

    if symbol not in symbols.AS:
        print("Symbol must be one of:")
        print(*symbols.AS, sep="\n")
        return

    time_dict = {"1d": "1000 D", "1h": "1000 H", "5m": "5000 T", "1m": "1000 T"}

    dates = pd.date_range(start=startTime, end=endTime, freq=time_dict[binSize])

    data = []

    for date in dates:
        date = date.strftime("%Y/%m/%d %H:%M:%S")
        xbt = bucket_trades(
            binSize=binSize,
            reverse=reverse,
            symbol=symbol,
            count=count,
            startTime=date,
        )
        data.append(xbt)
        sleep(1)

    appended_data = pd.concat(data)

    return appended_data

