import json
import time
from orders import Order
import threading
from config import config

#Reception class takes in cooking queue and optional matched_queue(for matched courier case)
#As soon as started it reads json file and parses the orders creeated the order object and delivers to cooking queue


class Reception(threading.Thread):

    data=None

    def __init__(self, cooking_queue,matched_queue = None):
        threading.Thread.__init__(self)
        self.cooking_queue = cooking_queue
        self.matched_queue = matched_queue

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
                self.put_order_to_queue(Reception.data.pop())
                remainder-=1
        while Reception.data:
            order_count=0
            while order_count <config.order_delivery_size:
                self.put_order_to_queue(Reception.data.pop())
                order_count+=1
            time.sleep(config.order_delivery_rate)

    def put_order_to_queue(self,order):
        self.cooking_queue.put(Order(order))
        if self.matched_queue!=None:
            self.matched_queue.put(order["id"])

    def get_cooking_queue(self):
        return self.cooking_queue

    def get_matched_id_queue(self):
        return self.matched_queue

    def run(self):
        self.process_orders()
