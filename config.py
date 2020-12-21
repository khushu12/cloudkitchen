# from app import log_dir
import os

working_dir=os.getcwd()
log_dir=working_dir+'/logs/'

class config():
    low_size=100
    high_size=200
    filename = "dispatch_orders.json"
    order_delivery_size=2
    # Assuming a gap of 1 second after every order taken by receptioon
    order_delivery_rate=1
    matched_analysis_file = log_dir+'analysis_matched.csv'
    fifo_analysis_file = log_dir+'analysis_fifo.csv'
    matched_analysis_log_file = log_dir + 'app_matched.log'
    fifo_analysis_log_file = log_dir + 'app_fifo.log'