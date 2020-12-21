import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys
plt.style.use('fivethirtyeight')
from config import config

x_values = []
y_values = []
z_values = []


def main(matched_flag):
    def animate(i, matched_flag):
        # print(matched_flag)
        if matched_flag:
            data = pd.read_csv(config.matched_analysis_file)
            title='Matched'
        else:
            title = 'FIFO'
            data = pd.read_csv(config.fifo_analysis_file)
        x_values = data['index']
        y_values = data['order']
        z_values = data['courier']
        plt.cla()
        x=[y_values,z_values]
        legs={0:["-b","mean order wait time"],1:["-r","mean courier wait time"]}
        for i,vals in enumerate(x):
            plt.plot(x_values,vals,legs[i][0], label=legs[i][1])
        plt.legend(loc="upper left")
        plt.xlabel('Index')
        plt.ylabel('Time(ms)')
        plt.title(title)
        plt.gcf().autofmt_xdate()
        plt.tight_layout()
    ani_1 = FuncAnimation(plt.gcf(), animate,interval=1,fargs=(matched_flag,))
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':

   if (sys.argv[1])=="Matched":
      matched_flag=True
      main(matched_flag)
   elif (sys.argv[1]) == "FIFO" :
      matched_flag = False
      main(matched_flag)
   else:
      print("Incorrect arg, use Matched/FIFO ")