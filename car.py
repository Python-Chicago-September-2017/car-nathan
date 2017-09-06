class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def display_all(self):
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed)
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage)
        print "Tax: " + str(self.tax)

car_1 = Car(20000,"20mph","Full",5000)
car_2 = Car(2500,"30mph","Almost full",10000)
car_3 = Car(10000,"10mph","Empty",0)
car_4 = Car(10001,"10mph","Empty",0)
car_5 = Car(999999,"250mph","Overflowing",18293729)
car_6 = Car(1,"2mph","Two Drops",25)

print "1#"
car_1.display_all()
print "2#"
car_2.display_all()
print "3#"
car_3.display_all()
print "4#"
car_4.display_all()
print "5#"
car_5.display_all()
print "6#"
car_6.display_all()