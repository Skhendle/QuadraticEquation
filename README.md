# FoondaMate Software Engineer Coding Challenge-001

## Background

1. Assume a fast growing company would like to visualise the growth of their userbase using a CLI application
2. They want to do this by running a terminal command that draws a graphs in the terminal
3. Their brilliant backend engineers have hacked together an API endpoint for them here. That outputs
-Dates (as keys) and
-the number of active users on those dates (as values)
4. They would like to be able to filter the data by:
- Start date
- And end date

(by passing these as flags when running the CLI command) and have the graph visualise data for the range they’ve selected.


They would also like to restrict the filtering of the data to the dates they have available:
Note, they don’t always know what dates they have data for, and are at the mercy of the API endpoint.


## TASK


1. Use any programming language to create a CLI tool per the specifications under background above.
2. Write tests for your business logic, bonus points for testing other layers such as the networking layer.
3. Write a Readme.md in your repo on how your app works and how one can go about setting it up locally.
4. Push your code to a public repo on GitHub and send the link via email to work@foondamate.com

# Solution
Please note this solution was built and tested on 0.04.4 LTS with Python 3.9

## To Run The Application
```console
# "Activating virtual environment and installing requirements"
user@device:~/QuadraticEquation$ python3.9 -m venv env
user@device:~/QuadraticEquation$ source ./env/bin/activate
user@device:~/QuadraticEquation$ pip3 install requirements.txt

# "Start and End date should be formatted d-m-yr e.g 16-02-2022"
# "To run the application"
# "python FoondaMateSoftwareEnginner/main.py start_date end_date"
user@device:~/QuadraticEquation$ python FoondaMateSoftwareEnginner/main.py 01-01-2022 02-02-2022

# "To run tests"
user@device:~/QuadraticEquation$ python FoondaMateSoftwareEnginner/test_service.py
```

