import urllib3
import Adafruit_DHT as dht
import time as t
import sys

while True:
    umid, temp = dht.read_retry(dht.DHT11, 4)
    t.sleep(10)
    chave = '067R1XZ158FU3L0C'
    url = 'https://api.thingspeak.com/update?api_key={}&field1={}&field2={}'
    if temp < 31.0 or umid < 70.0:
        print('Temp: {0:0.1f}   Umid: {1:0.1f}'.format(temp, umid))
        print('Termômetro finalizado.')
        sys.exit()
    urllib3.PoolManager().request('GET', url.format(chave, temp, umid))
    print('Temp: {0:0.1f}   Umid: {1:0.1f}'.format(temp, umid))





