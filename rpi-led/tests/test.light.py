import unittest
import requests
import sys
import time

RPI_PORT = "5000"
RPI_IP = "127.0.0.1"


class TestParser(unittest.TestCase):
    def test_cycle(self):
        endpoint = 'lights/1'
        url = 'http://{}:{}/{}'.format(RPI_IP, RPI_PORT, endpoint)
        body = {'on': False}
        requests.patch(url, json=body)
        time.sleep(1)
        body = {'on': True}
        requests.patch(url, json=body)
        time.sleep(1)
        body = {'on': False}
        requests.patch(url, json=body)


def main(argv):
    unittest.main()


if __name__ == "__main__":
    main(sys.argv)
