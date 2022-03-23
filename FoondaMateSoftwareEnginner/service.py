import sys, ast, datetime, requests
import matplotlib.pyplot as plt
import matplotlib.dates


def plot_graphs(start_date: str, end_date:str):

  try:
    start_date = datetime.datetime.strptime(start_date, '%d-%m-%Y')
    end_date = datetime.datetime.strptime(end_date, '%d-%m-%Y')
  except Exception as e:
    raise Exception("Invalid start and end date formating(d-m-yr e.g 16-2-)")

  if start_date.date() >= end_date.date():
    raise Exception("Invalid start and end date interval")
    
  # Making API call to get data and converting it into a MAP
  request = requests.get("http://sam-user-activity.eu-west-1.elasticbeanstalk.com/")
  data = ast.literal_eval(request.text)

  # Sorting Data, and casting values to datetime(date) and int(number of users)
  sort_orders = sorted(data.items(), key=lambda x: x[1], reverse=False)
  xdata = []
  ydata = []
  for item in sort_orders:
    if datetime.datetime.strptime(item[0], '%d-%m-%Y') >= start_date and  datetime.datetime.strptime(item[0], '%d-%m-%Y') <= end_date:
      xdata.append(datetime.datetime.strptime(item[0], '%d-%m-%Y') )
      ydata.append(int(item[1]))


  plt.plot(xdata, ydata, label = "Userbase Growth")
  plt.scatter(xdata, ydata, label = "Userbase Growth" )
  
  # plt.xlim(max(xdata), min(xdata))

  plt.show()

  