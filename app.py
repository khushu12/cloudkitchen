#!/usr/bin/python
import logging
import time
from reception import Reception
from cook import Cook as cook
from courier import Courier as courier
import queue

from statistics import mean
from mt_list import MTList
logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(message)s', level=logging.INFO)



# dispatch = queue.Queue()
# cooking  = queue.Queue()

dispatch = MTList()
cooking  = MTList()
average_order_time=[]
average_courier_time=[]
# Create two threads as follows

# logging.info('Admin logged in')

try:
   reception_thread = Reception(cooking)
   cooking = reception_thread.get_cooking_queue()
   time.sleep(1)
   cooking_thread = cook(dispatch , cooking)

   #Start Accepting orders
   reception_thread.start()
   time.sleep(1)

   #Start Cooking orders
   cooking_thread.start()
   time.sleep(1)
   list_of_threads=[]
   dispatch = cooking_thread.get_delivery_queue()

   while 1:
      # add id as optional arg for below dispatch ( Matched ) else FIFO
      order = dispatch.get()

      if order:
         #start dispatching courier for every new order
         logging.info("courier order {}".format(order))
         courier_thread = courier(order)
         courier_thread.start()

         list_of_threads.append(courier_thread)
         order_wait_time, courier_wait_time = courier_thread.get_order_details(order)

         if not isinstance(courier_wait_time,float):
            courier_wait_time=float(courier_wait_time.total_seconds()*1000)
         average_courier_time.append(courier_wait_time)

         logging.info("current_courier_wait_time: {}ms \t average_courier_wait_time {}ms"
                      .format(courier_wait_time, mean(average_courier_time )))

         if not isinstance(order_wait_time,float):
            order_wait_time=float(order_wait_time.total_seconds()*1000)
         average_order_time.append(order_wait_time)

         logging.info("current_order_wait_time: {}ms \t average_order_wait_time {}ms"
                      .format(order_wait_time , mean(average_order_time)))
         logging.info("*"*100)

   reception_thread.join()
   cooking_thread.join()
   for thread in list_of_threads:
      thread.join()

except Exception as e:
   logging.exception(str(e))


