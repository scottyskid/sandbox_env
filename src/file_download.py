from datetime import datetime, timedelta
import requests


if __name__ == '__main__':
    for hour in range(24):
        dt = datetime.now() + timedelta(hours=hour)
        url = f"http://trading.bretherton.id.au/period/5a920718e7e29dda8536f777?collate=hourly&format=tsv&start time={dt}&depth=60"
        print(url)
        # r = requests.get(url)
        # with open('tmp2.tsv', 'wb') as f:
        #     f.write(r.content)