import requests
import datetime as dt
import json


class API():
    def __init__(self):
        self.data = []

    def getData(self, limit, symbol, interval, startTime):
        url = "https://api.binance.com/api/v3/klines"

        startTime = str(int(startTime.timestamp() * 1000))

        print("defstar2")
        req_params = {
            "symbol": symbol,
            "interval": interval,
            "startTime": startTime,
            "limit": int(limit)
        }

        response = requests.get(url, params=req_params).text

        response = json.loads(response)

        for item in response:
            date = dt.datetime.fromtimestamp(item[0] / 1000.00)
            date = f"{date.year}/{date.month}/{date.day} {date.hour}:{date.minute}"

            df = [date,item[4],item[5]]
            self.data.append(df)


        return self.data


#API().getData(1000,"BTCUSDT",interval="1m",startTime=dt.datetime(2022,4,4,00,00))