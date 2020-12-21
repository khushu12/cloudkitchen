#!/usr/bin/python
import logging
import time
from reception import Reception
from cook import Cook as cook
from courier import Courier as courier
from config import config
from statistics import mean
from mt_list import MTList
from analysis import Analysis
import sys

def main(matched_flag):
   dispatch = MTList()
   cooking  = MTList()
   matched_id = MTList()
   average_order_time=[]
   average_courier_time=[]
   _id = None
   global _index
   _index=0
   analysis_filename = config.fifo_analysis_file
   log_file = config.fifo_analysis_log_file

   if matched_flag :
      analysis_filename = config.matched_analysis_file
      log_file = config.matched_analysis_log_file

   logging.basicConfig(filename=log_file, filemode='w', format='%(levelname)s - %(message)s' , level=logging.INFO)

   try:
      reception_thread = Reception(cooking,matched_id)
      cooking = reception_thread.get_cooking_queue()
      if matched_flag:
         matched_id = reception_thread.get_matched_id_queue()
      time.sleep(1)

      cooking_thread_1 = cook(dispatch , cooking)
      # cooking_thread_2 = cook(dispatch , cooking)

      #Start Accepting orders
      reception_thread.start()
      time.sleep(1)

      # Start Cooking orders ( 2 cooking threads mean 2 cooks in 1 resto)
      cooking_thread_1.start()
      # cooking_thread_2.start()
      time.sleep(1)
      list_of_threads=[]
      dispatch = cooking_thread_1.get_delivery_queue()
      csv_writer = Analysis()

      def main_app(order):
         global _index
         if order!=None:
            logging.info("order is {}".format(order))

            #start dispatching courier for every new order
            logging.info("courier order {}".format(order))
            courier_thread = courier(order)
            courier_thread.start()
            list_of_threads.append(courier_thread)
            order_wait_time, courier_wait_time = courier_thread.get_order_details(order)

            #for 0 courier wait time we might  return float(below to check)
            if not isinstance(courier_wait_time,float):
               courier_wait_time=float(courier_wait_time.total_seconds()*1000)
            average_courier_time.append(courier_wait_time)
            mean_courier=mean(average_courier_time )
            logging.info("current_courier_wait_time: {}ms \t average_courier_wait_time {}ms"
                         .format(courier_wait_time, mean_courier))

            # for 0 order wait time we might  return float(below to check)
            if not isinstance(order_wait_time,float):
               order_wait_time=float(order_wait_time.total_seconds()*1000)
            average_order_time.append(order_wait_time)
            mean_order=mean(average_order_time)
            logging.info("current_order_wait_time: {}ms \t average_order_wait_time {}ms"
                         .format(order_wait_time ,mean_order))
            logging.info("*"*100)

            #Below to wriite to a csv file(later used for plotting)
            csv_writer._write(analysis_filename,[_index,mean_order,mean_courier])
            _index += 1

      while 1:
         # add id as optional arg for below dispatch ( Matched ) else FIFO
         if matched_id!=[]:
            _id = matched_id.get()
         if _id:
            order = dispatch.get(_id)
         else:
            order = dispatch.get()
         main_app(order)


      reception_thread.join()
      cooking_thread_1.join()
      # cooking_thread_2.join()
      for thread in list_of_threads:
         thread.join()

   except Exception as e:
      logging.exception(str(e))


if __name__ == '__main__':
   if (sys.argv[1])=="Matched":
      matched_flag=True
      main(matched_flag)
   elif (sys.argv[1]) == "FIFO" :
      matched_flag = False
      main(matched_flag)
   else:
      print("Incorrect arg, use Matched/FIFO ")
