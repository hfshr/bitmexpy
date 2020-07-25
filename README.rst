bitmexpy
========

bitmexpy is a small project to learn how to create python packages. Heavily based on my bitmexr R package for accessing BitMEX's API for cryptocurrency data.

Useage
------

Currently bucketed trade data can be obtained using `bucket_trades()`. 

For data spanning more one API call (there is a 1000 row limit per API call) `map_bucket_trades()` can be used. This function creates a range of start dates and loops over the `bucket_trades()` function to capture all the required data. See examples below!

Examples
--------

Below are some simple examples of current functionality::

        # Request: Last 100 days of data for symbol XBTUSD:

        xbt = bucket_trades(symbol = "XBTUSD", 
                            reverse = "true",
                            count = "100)


        # Request: Hourly data since 2019-01-01

        eth = map_bucket_trades(symbol = "ETHUSD",
                                start_date = "2019-01-01",
                                binSize = "1h)