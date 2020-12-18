from orders import Order
import random
from datetime import datetime, timedelta
import threading
import logging
from config import config

logger = logging.getLogger(__name__)


class Courier(threading.Thread):

    def __init__(self,order, _id = None):
        threading.Thread.__init__(self)
        self.order = order
        self._id = _id
        self.courier_wait_time = 0.0
        self.courier_arrival_time = self.arrival_time()

    def arrival_time(self):
        return self.order.order_order_time + timedelta(seconds=
                                                       int(random.uniform(config.low_size ,config.high_size)))

    def get_order(self):
        try:
            self.is_order_ready(self.order)
        except Exception as e:
            logger.exception(e)

    def is_order_ready(self, order):
        if self.courier_arrival_time < order.order_in_delivery_queue_time:
            self.courier_wait_time = order.order_in_delivery_queue_time - self.courier_arrival_time
            order.order_pick_time = order.order_in_delivery_queue_time
        else:
            order.order_wait_time=self.courier_arrival_time - order.order_in_delivery_queue_time

    def get_order_details(self,order):
        return order.order_wait_time, self.courier_wait_time

    def run(self):
        self.get_order()


