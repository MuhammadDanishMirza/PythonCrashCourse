from module_2 import ElectricCar
from module_1 import Car


instance1 = ElectricCar('tesla', 'model s', 2016)
instance1.battery.get_range()  
instance1.battery.upgrade_battery()
instance1.battery.get_range()



my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())