from stored_classes import ElectricCar

instance1 = ElectricCar('tesla', 'model s', 2016)
instance1.battery.get_range()  
instance1.battery.upgrade_battery()
instance1.battery.get_range() 