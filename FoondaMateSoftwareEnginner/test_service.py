import unittest, requests
from service import plot_graphs


class MyTestCase(unittest.TestCase):

    def test_invalid_date_format(self):
       with self.assertRaises(Exception):
           plot_graphs(start_date="pie", end_date="start")

    def test_invalid_date_interval(self):
       with self.assertRaises(Exception):
           plot_graphs(start_date="01-01-2022", end_date="01-01-2021")

    def test_data_url(self):
        request = requests.get("http://sam-user-activity.eu-west-1.elasticbeanstalk.com/")
        self.assertEquals(first=request.status_code,second=200)


if __name__ == "__main__":
    unittest.main()