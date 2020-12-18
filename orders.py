
from datetime import datetime, timedelta


class Order():

    def __init__(self,dictionary):
        for k , v in dictionary.items():
            setattr(self , k , v)
        self.order_cook_time=None
        self.order_pick_time=None
        self.order_in_delivery_queue_time=None
        self.order_wait_time=0.0
        self.order_order_time=datetime.now()

    def __str__(self):
        return ("id:{} name:{} prepttime:{}".format(self.id,self.name,self.prepTime))

    def get_order_wait_time(self):
        return self.order_wait_time

