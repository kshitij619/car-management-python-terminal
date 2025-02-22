from typing import List
import car_class 
import car_type as ct


class ParkingArea:
    __suvCount = 0
    __hatchbackCount = 0

    __suvCarList: List[car_class.Car] = []
    __hatchbackCarList: List[car_class.Car] = []

    def addCarToParking(self, carName, carNumber, carType: ct.CarType):
        if carType == ct.CarType.Suv and self.__suvCount < self.totalSuv:
            self.__suvCarList.append(car_class.Car(carName, carNumber, carType))
            self.__suvCount += 1
            print('Added SUV Car in SUV section')
        elif carType == ct.CarType.Hatchback:
            if self.__hatchbackCount < self.totalHatchback:
                self.__hatchbackCarList.append(car_class.Car(carName, carNumber, carType))
                self.__hatchbackCount += 1
                print('Added hatchback Car in hatchback section')
            elif self.__suvCount < self.totalSuv:
                self.__suvCarList.append(car_class.Car(carName, carNumber, carType))
                self.__suvCount += 1
                print('Added hatchback Car in SUV section')
        else:
            print('SORRY, NO PARKING!!')


    def getSuvList(self):
        if self.__suvCarList:
            for suv in self.__suvCarList:
                print(suv.describeCar())

    def getHatchbackList(self):
        if self.__hatchbackCarList:
            for hatchback in self.__hatchbackCarList:
                print(hatchback.describeCar())

    def getAllCarList(self):
        if self.__suvCarList:
            print('SUV Cars:')
            self.getSuvList()
            print()
            for i in range(10):
                print('-',end='')
        print()

        if self.__hatchbackCarList:
            print('Hatchback Cars:')
            self.getHatchbackList()
            for i in range(10):
                print('-',end='')
        print()

    def getCount(self):
        print(f'SUV: {self.__suvCount}\nHatchback: {self.__hatchbackCount}')
    
    def __removeCar(self, car):
        if car.carType == ct.CarType.Suv:
            self.__suvCarList.remove(car)
            print('Removed suv')
        if car.carType == ct.CarType.Hatchback:
            self.__hatchbackCarList.remove(car)
            print('Removed hatchback')
        
    def findCar(self, carNumber):
        for car in self.__suvCarList:
            if carNumber == car.numberPlate:
                return car
        for car in self.__hatchbackCarList:
            if carNumber == car.numberPlate:
                return car

    def parkCar(self):
        carName = input('Enter car name: ')
        carNumber = input('Enter car number: ')
        carTypeString = input('Enter car type:')
        if carTypeString.upper() == 'S':
            carTypeEnum = ct.CarType.Suv
        elif carTypeString.upper() == 'H':
            carTypeEnum = ct.CarType.Hatchback
        self.addCarToParking(carName, carNumber, carTypeEnum)
        
    def exitParking(self):
        carNumber = input('Enter number of car you want to exit: ')
        car = self.findCar(carNumber)
        finalRate = car.amountToBePaid()
        print(f'Amount to be paid: ₹{finalRate}')
        while True:
            payment = int(input('Enter payment amount: '))
            if payment >= finalRate:
                print('Thank you for using our parking services!!!')
                break
            else:
                print('Please enter correct amount!!!')
        self.__removeCar(car)
        
    def startService(self):
        self.totalSuv = int(input('Enter parking space for SUV cars: '))
        self.totalHatchback = int(input('Enter parking space for Hatchback cars: '))
        while True:
            print()
            print('Park your car admin:')
            print('1. Get count of cars')
            print('2. View all cars')
            print('3. Park a car')
            print('4. Exit a car from parking')
            print('5. Stop Service')
            choice = int(input('Enter your choice: '))
            
            if choice == 1:
                self.getCount()
            elif choice == 2:
                self.getAllCarList()
            elif choice == 3:
                self.parkCar()
            elif choice == 4:
                self.exitParking()
            elif choice == 5:
                break
            else:
                print('Enter correct option!!!\nTry again...')

             