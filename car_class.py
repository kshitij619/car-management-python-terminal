import car_type as ct
import datetime as dt

class Car:
    parkingFeesPaid = False

    def __init__(self, carBrand, numberPlate, carType: ct.CarType):
        self.carBrand = carBrand
        self.numberPlate = numberPlate.upper()
        self.carType = carType
        self.entryTime = dt.datetime.now()
    
    def amountToBePaid (self):
        time = dt.datetime.now() - self.entryTime
        if self.carType == ct.CarType.Suv:
            return int(time.total_seconds()) * 2
        elif self.carType == ct.CarType.Hatchback:
            return int(time.total_seconds()) * 1
        else:
            return 5
            
    def describeCar(self):
        return f'{self.carBrand} number: {self.numberPlate}\nTime spent(in hours): {self.entryTime}\nAmount to be Paid: {self.amountToBePaid()}\nType: {self.carType.name}'