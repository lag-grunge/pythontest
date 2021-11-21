#! /bin/python3
from redis import Redis
import time
import json

r = Redis()

if __name__=="__main__":
    data = []
    data.append({"metadata": {"from": 1111111111, "to": 2222222222}, "amount": 10000})
    data.append({"metadata": {"from": 3333333333, "to": 4444444444}, "amount": -3000})
    data.append({"metadata": {"from": 3333333333, "to": 4444444444}, "amount": -3000})
    data.append({"metadata": {"from": 3333333333, "to": 5555555555}, "amount": -3000})
    data.append({"metadata": {"from": 2222222222, "to": 5555555555}, "amount": 5000})
    while data:
        time.sleep(10)
        jstr= json.dumps(data.pop(0))
        a = r.publish('default', jstr)
    r.publish('default', "Bye")
