import random
import string
import uuid
from typing import List
from constants import CARS_TYPES
from constants import CARS_PRODUCER
from constants import TOWNS

"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.
Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.
    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.
    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID
Гараж має наступні характеристики:
    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.
    Повинен мати реалізованими наступні методи
    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі
Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.
    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.
    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""

class Car:

    def __init__(self, price: float, car_type: string, producer: string, mileage: float):
        self.price = round(price,2)
        self.car_type = car_type
        self.producer = producer
        self.mileage = round(mileage,2)
        self.number = uuid.uuid4()


    def __repr__(self):
        return f"\nCar produser: {self.producer}, type: {self.car_type}, " \
               f"number: {self.number}, price: {self.price}, spend mileage: {self.mileage}"


    def __le__(self, other):
        return self.price <= other.price


    def __lt__(self, other):
        return self.price < other.price


    def __eq__(self, other):
        return self.price == other.price


    def __ne__(self, other):
        return self.price != other.price


    def change_UUID(self):
        self.number = uuid.uuid4()
        return self.number

class Garage:

    def __init__(self, town: string, places: int, garage_cars: List[Car],  owner=None):
        self.town = town
        self.places = places
        self.cars = garage_cars if garage_cars is not None else []
        self.owner = owner
        self.current = 0


    def __repr__(self):
        return f"\nTown: {self.town}, Places: {self.places}, owner: {self.owner}, car: {self.cars}"


    def add(self, new_car: string):
        if len(self.cars) < self.places:
            self.cars.append(new_car)
            return self
        else:
            return f"Garage haven't got any free places"


    def remove(self, my_car: string):
        if my_car in self.cars:
            self.cars.remove(my_car)
            print('THE CAR WAS DELETED!')
        return self


    def hit_hat(self):
        return round(sum(car.price for car in self.cars),2)


class Cesar:

    def __init__(self, name: string, cesar_garages: List[Garage]):
        self.name = name
        self.cesar_garages = cesar_garages if cesar_garages is not None else []
        self.register_id = uuid.uuid4()


    def __repr__(self):
        return f"CESAR NAME: {self.name}, " \
               f"\nREGISTER_ID: {self.register_id}, " \
               f"\nCOUNT OF GARAGE: {self.garages_count()}, " \
               f"\nCOUNT CAR IN ALL GARAGES:  {self.сars_count()}, " \
               f"\nSUM PRICE ALL CAR:  {self.hit_hat()}" \
               f"\nGARAGE: {self.cesar_garages}, "


    def compare_cesar(cesar_list: list):
        return max((cesar for cesar in cesar_list), key=lambda x: x.hit_hat() )


    def hit_hat(self):
        return round(sum(item.hit_hat() for item in self.cesar_garages),2)


    def garages_count(self):
        return len(self.cesar_garages)


    def сars_count(self):
        return sum(len(garage.cars) for garage in self.cesar_garages)


    def add_car(self, car: string, garage = None):
        new_car_max_free_garage = 0
        if garage == None:
            return max(self.cesar_garages, key = lambda x:(x.places-len(x.cars))).add(car)
        else:
            return garage.add(car)



if __name__ == "__main__":

    cars = []
    for car_counter in range(random.randint(10, 100)):
        car = Car(price=random.uniform(100.5, 999.5),
                  car_type=random.choice(CARS_TYPES),
                  producer=random.choice(CARS_PRODUCER),
                  mileage=random.uniform(0, 1000000),
                  )
        cars.append(car)

    car1 = Car(price=random.uniform(100.5, 999.5),
               car_type=random.choice(CARS_TYPES),
               producer=random.choice(CARS_PRODUCER),
               mileage=random.uniform(0, 1000000),
               )
    car2 = Car(price=random.uniform(100.5, 999.5),
               car_type=random.choice(CARS_TYPES),
               producer=random.choice(CARS_PRODUCER),
               mileage=random.uniform(0, 1000000),
               )

    print ("CAR1: ", car1)
    print ("CAR2: ", car2)

    # CHECK UUID CHANGE
    print ("\n------CHECK UUID CHANGE--------")
    old_number = car1.number
    car1.number = car1.change_UUID()
    print("The number {} of car {} was changed on: {}".format(old_number, car1.producer, car1.number))

    # CHECK COMPARE
    print ("\n-----CHECK COMPARE-------")
    if car1.price <= car2.price:
        print(
            "price {} car {} biggest then price {} car {}".format(car2.price, car2.producer, car1.price, car1.producer))
    else:
        print(
            "price {} car {} biggest then price {} car {}".format(car1.price, car1.producer, car2.price, car2.producer))

    if car1.price < car2.price:
        print(
            "car {} price {} cheaper then car {} price {}".format(car1.producer, car1.price, car2.producer, car2.price))
    else:
        print("car {} cheaper then car {}".format(car2.producer, car1.producer))

    if car1.price == car2.price:
        print(
            "price {} car {} is equal to price {} car {}".format(car1.price, car1.producer, car2.price, car2.producer))

    if car1.price != car2.price:
        print("price car {} isn't equal to price car {}".format(car1.producer, car2.producer))


    print ("\n-----CHECK GARAGE------")
    CESAR_NAME = ["Oleg", "Vitaliya", "Marina", "Grisha", "Petr"]
    cesars = []
    for cesar_counter in range(random.randint(2, 3)):
        garages = []
        for garage_counter in range(random.randint(1, 3)):
            count_cars = random.randint(1, 4)
            random_place = random.randint(0, 10)

            get_car = []
            for i in random.sample(cars, count_cars):
                if i not in get_car:
                    cars.remove(i)
                    get_car.append(i)

                if count_cars > random_place:
                    raise ValueError("Count cars more then count place. RUN PGOGRAM AGAIN")
                else:
                    garage = Garage(town=random.choice(TOWNS),
                                    places=random_place,
                                    garage_cars=get_car)
            garages.append(garage)
            print (garage)
            #print("\nCOUNT CARS: ", len(get_car))
            #print("COUNT PLACE: ", random_place)
            #print("PRICE ALL CAR IN GARAGES: ", garage.hit_hat())



        cesar = Cesar(name=random.choice(CESAR_NAME), cesar_garages=garages)
        cesars.append(cesar)

    print ("\n-----CHECK CESAR------")
    for item in cesars:
        print(item, "\n")

    print ("THE RICHEST CESAR IS: ",(Cesar.compare_cesar(cesars)).name)

    print("\n----CHECK ADD CARS----------")
    print("BEFORE ADD NEW CAR: ", garages[0])
    print("PRICE ALL CARS IN GARAGE BEFORE ADD CAR: ", garages[0].hit_hat())

    print("\nAFTER ADD NEW CAR: ", garages[0].add(car1))
    print("PRICE ALL CARS IN GARAGE AFTER ADD CAR: ", garages[0].hit_hat())

    print("\nBEFORE REMOVE NEW CAR: ", garages[0])
    print("\nCAR FOR REMOVE: ", garages[0].cars[0])
    print("\nAFTER REMOVE NEW CAR: ", garages[0].remove(garages[0].cars[0]))

    print("\nADD CAR TO FREE GARAGE: ", cesars[0].add_car(car1))
    print("\nADD CAR TO SELECTED GARAGE: ", cesars[0].add_car(car2, garages[0]))


print ("-----------------------------------")