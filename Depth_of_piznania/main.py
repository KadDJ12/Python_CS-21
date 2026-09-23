from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self,name: str, speed: int, distance: int, capacity: int):
        if not isinstance(name,str) or not type(speed) is int or not type(capacity) is int or not type(distance) is int:
            raise ValueError("Wrong data format")
        elif speed <= 0 or capacity <= 0 or distance <= 0:
            raise ValueError("Wrong data speed or capacity or dictanse can not be less than 0")
        self.name = name
        self.speed = speed
        self.capacity = capacity
        self.distance = distance


    @abstractmethod
    def move(self) -> float:
        return self.distance / self.speed

    @abstractmethod
    def fuel_consumption(self) -> float:
        pass

    def calculate_cost(self, price_per_unit: float) -> float:
        return float(self.fuel_consumption()) * price_per_unit
        

    @abstractmethod
    def info(self, time_to_destination) -> str:
        if time_to_destination < 0:
            raise ValueError("time cannot be less than 0")
        return (
            f"Транспортний засіб: {self.name}\n"
            f"Проїхав: {self.distance}\n"
            f"Було витрачено палива: {self.fuel_consumption():.1f}\n"
            f"Час у дорозі: {time_to_destination}\n"
            f"Вміщає в себе: {self.capacity} пасажирів"
        )


class Car(Transport):
    def move(self):
        return super().move()

    def fuel_consumption(self):
        print(f"Машина проїхала {self.distance} і витратила {self.distance * 0.07:.1f} літрів пального")
        return self.distance * 0.07

    def info(self, time_to_destination):
        return super().info(time_to_destination)


class Bus(Transport):
    def move(self):
        return super().move()

    def fuel_consumption(self):
       print(f"Автобус проїхав {self.distance} і витратив {self.distance * 0.15}")
       return self.distance * 0.15

    def pacangers_capacity(self, pacangers):
        if pacangers > self.capacity:
            return "Перевантажено!"
        return f"Кількість пасажирів у нормі: {pacangers} з {self.capacity}"

    def info(self, time_to_destination):
        return super().info(time_to_destination)


class Bicycle(Transport):
    def __init__(self, name: str, speed: int, distance: int, capacity: int):
        if speed > 20:
            raise ValueError(
                f"Максимально допустима швидкість для велосипеда становить 20 км/год, ви вказали: {speed}"
            )
        super().__init__(name, speed, distance, capacity)

    def move(self):
        return super().move()

    def fuel_consumption(self):
        return 0

    def info(self, time_to_destination):
        return super().info(time_to_destination)


class ElectricCar(Car):
    def battery_usage(self) -> float:
        return self.distance * 0.2

    def fuel_consumption(self):
        return 0

    def calculate_cost(self, price_per_unit):
        return "Не рахуй ті копійки..."

    def info(self, time_to_destination):
        return super().info(time_to_destination)


def print_ve(transport: Transport) -> None:
    print(transport.name, transport.speed, transport.capacity)










car = Car(name="Toyota Camry", speed=100, distance=350, capacity=5)
print("--- CAR ---")
# Передаємо час, який вираховується автоматично (відстань / швидкість = 350 / 100 = 3.5)
print(car.info(car.move()))
# Демонстрація відпрацювання блоку try-except у calculate_cost (через текстовий fuel_consumption)
print("Вартість:", car.calculate_cost(12))


# 2. Екземпляр Bus
bus = Bus(name="Богдан", speed=70, distance=210, capacity=40)
print("\n--- BUS ---")
print(bus.info(bus.move()))
# Перевірка логіки пасажирів
print(bus.pacangers_capacity(45)) # Має вивести: Перевантажено!
print(bus.pacangers_capacity(25)) # Має вивести: Кількість пасажирів у нормі...


# 3. Екземпляр Bicycle
# Швидкість вказана 18, щоб не спрацював ValueError (обмеження до 20 км/год)
bike = Bicycle(name="Kellys", speed=18, distance=36, capacity=1)
print("\n--- BICYCLE ---")
print(bike.info(bike.move()))


# 4. Екземпляр ElectricCar
tesla = ElectricCar(name="Tesla Model 3", speed=120, distance=480, capacity=5)
print("\n--- ELECTRIC CAR ---")
print(tesla.info(tesla.move()))
# Перевірка унікального методу батареї
print(f"Використання батареї: {tesla.battery_usage()} кВт")
# Перевірка перевизначеного методу вартості
print("Вартість:", tesla.calculate_cost(12))
