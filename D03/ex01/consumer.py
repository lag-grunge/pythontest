#! /bin/python3
import logging
import json
from producer import r
import time
import sys

stop = False

if __name__=="__main__":
    evil_list = []
    for i in sys.argv[2:]:
        for j in i.split(' '):
            for k in j.split(','):
                evil_list.append(k)
    logging.basicConfig(level=logging.INFO)
    def handler_a_oper(data):
        time.sleep(3)
        if data["data"].decode('utf-8') == "Bye":
            global stop
            stop = True
            return
        time.sleep(1)
        oper = json.loads(data["data"])
        meta = oper["metadata"]
        if (len(str(meta["to"])) != 10) or (len(str(meta["from"])) != 10):
            logging.error("wrong account meta['to'] or ['from']")
            return
        if str(meta["to"]) in evil_list:
            logging.info("meta['to'] in evil")
            if oper["amount"] >= 0:
                logging.info("amount more than zero, substitution")
                tmp = meta["from"]
                meta["from"] = meta["to"]
                meta["to"] = tmp
            else:
                logging.info("amount less than zero, substitution")
        logging.info(oper)
        return
    p = r.pubsub()
    p.subscribe('default')
    p.channels[b'default'] = handler_a_oper
    t = p.run_in_thread(sleep_time=0.01)
    logging.info("Thread runs")
    while True:
        time.sleep(1)
        logging.info("|")
        if stop:
            t.stop()
            logging.info("Thread stops")
            logging.info("All work done")
            quit(0)
