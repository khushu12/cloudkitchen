from statistics import mean


class Analysis():

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

