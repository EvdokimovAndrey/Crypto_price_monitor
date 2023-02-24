import websockets
import asyncio
import json
import time
from Predictor import Prediction


history_of_price = []


async def main():

    url_btc = 'wss://stream.binance.com:9443/stream?streams=btcusdt@miniTicker'
    url_eth = 'wss://stream.binance.com:9443/stream?streams=ethusdt@miniTicker'

    async with websockets.connect(url_btc) as client_btc:
        async with websockets.connect(url_eth) as client_eth:
            while True:
                data_btc = json.loads(await client_btc.recv())['data']
                data_eth = json.loads(await client_eth.recv())['data']

                predict_eth = float(Prediction.get_predict_eth(float(data_btc['c'])))

                event_time = time.localtime(data_eth['E'] // 1000)
                event_time = f'{event_time.tm_hour}:{event_time.tm_min}:{event_time.tm_sec}'

                dif = abs(predict_eth-float(data_eth['c']))
                print(event_time, '->', dif)

                history_of_price.append(float(data_eth['c']))
                first_value = history_of_price[0]
                if float(data_eth['c']) > first_value*1.01:
                    print('Price increase on 1%')
                    first_value = data_eth['c']


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())