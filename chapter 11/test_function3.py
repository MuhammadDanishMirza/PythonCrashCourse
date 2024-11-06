from function3 import get_formatted_name
import unittest

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        
    def test_first_middle_last_name(self):
        """Do names like 'Muhammad Danish Mirza' work?"""
        formatted_name = get_formatted_name('muhammad','mirza','danish')
        self.assertEqual(formatted_name, 'Muhammad Danish Mirza')
        


unittest.main()