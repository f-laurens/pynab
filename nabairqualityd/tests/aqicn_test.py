import unittest

from nabairqualityd import aqicn


class TestAQICN(unittest.TestCase):
    def do_test_index(self, index):
        latitude = "48.8331"
        longitude = "2.3264"
        client = aqicn.aqicnClient(index, latitude, longitude)
        client.update()
        airquality = client.get_data()
        self.assertTrue(isinstance(airquality, int))
        self.assertTrue(airquality >= 0)
        self.assertTrue(airquality <= 2)
        city = client.get_city()
        self.assertTrue(isinstance(city, str))

    def test_indexes(self):
        for index in range(0, 2):
            self.do_test_index(index)
