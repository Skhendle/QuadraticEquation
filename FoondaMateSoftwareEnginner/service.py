import sys, ast, datetime
import requests
import matplotlib.pyplot as plt
import matplotlib.dates

GRAPH_TYPE = ["line", "scatter"]
GRAPH_ORDER = ["start", "end"]

def plot_graphs(graph_order:str, graph_type:str):
  # Making API call to get data and converting it into a MAP
  request = requests.get("http://sam-user-activity.eu-west-1.elasticbeanstalk.com/")
  data = ast.literal_eval(request.text)

  # Sorting Data, and casting values to datetime(date) and int(number of users)
  sort_orders = sorted(data.items(), key=lambda x: x[1], reverse=False)
  xdata = [datetime.datetime.strptime(x[0], '%d-%m-%Y') for x in sort_orders]
  ydata = [int(x[1]) for x in sort_orders]

  if graph_type == "line":
    plt.plot(xdata, ydata)
  else:
    plt.scatter(xdata, ydata, label = "label_name" )
  
  if graph_order == "end":
    plt.xlim(max(xdata), min(xdata))

  plt.show()


if __name__ == "__main__":
  try:
    graph_order = sys.argv[1]
    graph_type = sys.argv[2]

    if graph_order in GRAPH_ORDER and graph_type in GRAPH_TYPE:
      plot_graphs(graph_type=graph_type, graph_order=graph_order)
    else:
      raise Exception("Invalid Application Arguements")
  except Exception as e:
    print(e)
  