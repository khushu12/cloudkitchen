from datetime import datetime, timedelta
import time
import threading
import logging
logger = logging.getLogger(__name__)

#Cook accepts delivery queue and cooking queue as args, reads cooking queue and preps the order and throw
#in delivery queue


class Cook(threading.Thread):

    def __init__(self,delivery_queue, cooking_queue):
        threading.Thread.__init__(self)
        self.delivery_queue = delivery_queue
        self.cooking_queue = cooking_queue

    def cook_order(self):
        try:
            while self.cooking_queue.value:
                order = self.get_order()
                logger.info("cooking order:{}".format(order))
                order.order_cook_time = order.prepTime
                time.sleep(order.prepTime)
                order.order_in_delivery_queue_time = datetime.now()
                self.complete_order(order)
        except Exception:
            raise

    def complete_order(self,order):
        self.delivery_queue.put(order)

    def get_order(self):
        try:
            return self.cooking_queue.get()
        except:
            logger.warning("No order to cook")

    def get_cooking_queue(self):
        return self.cooking_queue

    def get_delivery_queue(self):
        return self.delivery_queue

    def run(self):
        self.cook_order()
