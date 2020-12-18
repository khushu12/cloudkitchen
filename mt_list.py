import threading
import logging
logger = logging.getLogger(__name__)
# Custom list with locking mechanism.


class MTList(object):
    #Just Like regular list it takes value to append or remove but with locking the list

    def __init__(self):
        self.lock = threading.Lock()
        self.value = []

    def put(self, val):
        self.lock.acquire()
        try:
            self.value.append(val)
        finally:
            self.lock.release()

    def get(self, val=None):
        if len(self.value)>0:
            self.lock.acquire()
            try:
                if val == None:
                    return (self.value.pop())
                else:
                    for i, order in enumerate(self.value):
                        if val==order.kid:
                            return (self.value.pop(i))
            except Exception:
                logger.exception("Popping out of empty list")
            finally:
                self.lock.release()

