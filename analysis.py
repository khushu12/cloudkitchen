from statistics import mean
import csv
import pandas as pd
import os

class Analysis():
    columns=['Order','Courier']
    def __init__(self):
        self.courier_wait_time_list=[]
        self.food_wait_time_list=[]

    def average_list(self,some_list):
        return mean(some_list)

    def show_food_stats(self,some_list):
        try:
            print("average_food_wait_time:",self.average_list(self.food_wait_time_list()))
        except Exception as e:
           raise

    def show_courier_stats(self,some_list):
        print("average_courier_wait_time:" , self.average_list(self.courier_wait_time_list()))

    def _write(self,filename, data):
        # print(data)
        d={'index':[data[0]],'order':[data[1]],'courier':[data[2]]}
        data_frame = pd.DataFrame(d)
        if not os.path.isfile(filename):
            data_frame.to_csv(filename,index=False)
        else:
            data_frame.to_csv(filename, mode='a', header=False, index=False)
