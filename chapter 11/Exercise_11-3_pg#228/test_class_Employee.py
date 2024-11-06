from stored_class import Employee
import unittest
class Test_Employee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Hasan","Raza",1000)
        
    def test_give_default_raise(self):
        self.assertEqual(self.employee.give_raise(),6000)
    
    def test_give_custom_raise(self):
        self.assertEqual(self.employee.give_raise(10000),11000)
    
unittest.main()