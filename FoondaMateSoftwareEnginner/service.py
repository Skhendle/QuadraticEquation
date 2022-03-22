import sys, ast, datetime
import requests
import matplotlib.pyplot as plt
import matplotlib.dates

## Programs takes to arguments. -> Order Type, Graph Type

try:
  order_type = sys.argv[0]
  graph_type = sys.argv[1]
except:
  print("Input Error:Invalid Application Arguements")



# Getting Data and converting it to a map
request = requests.get("http://sam-user-activity.eu-west-1.elasticbeanstalk.com/")
data = ast.literal_eval(request.text)
#if order_type == "start":
sort_orders = sorted(data.items(), key=lambda x: x[1], reverse=False)
# else:
#   sort_orders = sorted(data.items(), key=lambda x: x[1], reverse=False)

# print(sort_orders)

xdata = [datetime.datetime.strptime(x[0], '%d-%m-%Y') for x in sort_orders]
ydata = [int(x[1]) for x in sort_orders]


# my_list = sorted(sorted_keys, reverse=False) 
# print(my_list)
# dates = matplotlib.dates.date2num(xdata)
# plt.plot(xdata, ydata)
plt.scatter(xdata, ydata, label = "label_name" )
plt.gcf().autofmt_xdate()
# plt.xlim(max(xdata), min(xdata))

plt.show()
