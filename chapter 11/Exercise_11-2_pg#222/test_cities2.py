import unittest
from city_functions2 import place

class PlaceTestCase(unittest.TestCase):
    def  test_city_country(self):
        self.assertEqual(place('karachi','pakistan'),'Karachi, Pakistan')
        
    def  test_city_country_population(self):
        self.assertEqual(place('karachi','pakistan',22000000),'Karachi, Pakistan - Population 22000000')
        
unittest.main()