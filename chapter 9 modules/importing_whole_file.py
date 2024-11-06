import stored_classes

instance1 = stored_classes.ElectricCar('tesla', 'model s', 2016)
instance1.battery.get_range()  
instance1.battery.upgrade_battery()
instance1.battery.get_range()