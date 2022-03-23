import sys
from service import plot_graphs

if __name__ == "__main__":
    graph_order = sys.argv[1]
    graph_type = sys.argv[2]
     
    plot_graphs(graph_type=graph_type, graph_order=graph_order)
