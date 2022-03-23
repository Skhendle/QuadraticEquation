import sys
from service import plot_graphs

if __name__ == "__main__":
    start_date = sys.argv[1]
    end_date = sys.argv[2]
     
    plot_graphs(start_date=start_date, end_date=end_date)
