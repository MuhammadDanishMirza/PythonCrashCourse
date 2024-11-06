import unittest
from city_functions import place

class PlaceTestCase(unittest.TestCase):
    def  test_city_country(self):
        self.assertEqual(place('karachi','pakistan'),'Karachi, Pakistan')
        
unittest.main()