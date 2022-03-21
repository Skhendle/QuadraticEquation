import sys, ast, datetime
import requests

for args in sys.argv:
  print(args)


# Dictionary with two keys

request = requests.get("http://sam-user-activity.eu-west-1.elasticbeanstalk.com/")
data = ast.literal_eval(request.text)
print("Keys before Dictionary Updation:")
keys = list(data)
for key in keys:
    print(key)
    print( datetime.datetime.strptime(key, '%d-%m-%Y').date())