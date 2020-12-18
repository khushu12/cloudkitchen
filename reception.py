import json
import time
from orders import Order
import threading
from config import config


class Reception(threading.Thread):

    data=None

    def __init__(self, cooking_queue):
        threading.Thread.__init__(self)
        self.cooking_queue = cooking_queue

    def read_orders(self,filename):
        with open(filename) as f :
            Reception.data = json.load(f)
        return Reception.data

    def process_orders(self):
        self.read_orders(config.filename)

        #Make Json data lenghth even
        remainder=len(Reception.data) % config.order_delivery_size
        if remainder!=0:
            while remainder <0:
                self.cooking_queue.put(Order(Reception.data.pop()))
                remainder-=1
        while Reception.data:
            order_count=0
            while order_count <config.order_delivery_size:
                self.cooking_queue.put(Order(Reception.data.pop()))
                order_count+=1
            time.sleep(config.order_delivery_rate)


    def get_cooking_queue(self):
        return self.cooking_queue

    def get_delivery_queue(self):
        return self.delivery_queue

    def run(self):
        self.process_orders()
