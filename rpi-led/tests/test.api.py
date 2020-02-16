import unittest
import requests
import sys


RPI_IP = "127.0.0.1"
RPI_PORT = "5000"


class TestParser(unittest.TestCase):
    def test_turn_on(self):
        endpoint = 'lights/1'
        url = 'http://{}:{}/{}'.format(RPI_IP, RPI_PORT, endpoint)
        body = {'on': True}
        response = requests.patch(url, json=body)
        data = response.json()
        self.assertEqual(data['status'], 'success')
        self.assertTrue(data['on'])

    def test_turn_off(self):
        endpoint = 'lights/1'
        url = 'http://{}:{}/{}'.format(RPI_IP, RPI_PORT, endpoint)
        body = {'on': False}
        response = requests.patch(url, json=body)
        data = response.json()
        self.assertEqual(data['status'], 'success')
        self.assertTrue(not data['on'])

    def test_cycle_several_states(self):
        endpoint = 'lights/1'
        url = 'http://{}:{}/{}'.format(RPI_IP, RPI_PORT, endpoint)
        off = {'on': False}
        on = {'on': True}

        # Turn off
        response = requests.patch(url, json=off)
        data = response.json()
        self.assertEqual(data['status'], 'success')
        self.assertTrue(not data['on'])

        # Turn on
        response = requests.patch(url, json=on)
        data = response.json()
        self.assertEqual(data['status'], 'success')
        self.assertTrue(data['on'])

        # Turn off
        response = requests.patch(url, json=off)
        data = response.json()
        self.assertEqual(data['status'], 'success')
        self.assertTrue(not data['on'])

        # Turn off
        response = requests.patch(url, json=off)
        data = response.json()
        self.assertEqual(data['status'], 'success')
        self.assertTrue(not data['on'])

        # Turn on
        response = requests.patch(url, json=on)
        data = response.json()
        self.assertEqual(data['status'], 'success')
        self.assertTrue(data['on'])


def main(argv):
    unittest.main()


if __name__ == "__main__":
    main(sys.argv)
