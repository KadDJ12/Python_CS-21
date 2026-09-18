from abc import ABC, abstractmethod

class Medicine(ABC):
    def __init__(self, name: str, quantity: int, price: float):
        if (
            type(name) is not str
            or type(quantity) is not int
            or type(price) not in (int, float)
        ):
            raise TypeError("Type error")

        if price < 0 or quantity < 0:
            raise ValueError('value can not be less than 0')
        self.name = name
        self.quantity = quantity
        self.price = price

    @abstractmethod
    def requires_prescription(self): 
        pass

    @abstractmethod
    def storage_requirements(self): 
        pass

    def info(self):
        return (
            f"Продукт: {self.name}\n"
            f"Ціна за одиницю: {self.price}$\n"
            f"Є на складі: {self.quantity}\n"
            f"Загальна вартість партії: {self.total_price():.1f}$\n"
            f"Потрібна наявність рецепту: {self.requires_prescription()}\n"
            f"Вимоги до зберігання: {self.storage_requirements()}\n"
        )
    def total_price(self):
        return self.quantity * self.price
        

        



class Antibiotic(Medicine):
    def requires_prescription(self) -> bool:
        return True 
    
    def storage_requirements(self) -> str:
         return "8 - 15 градусів, темне холодне місце"


    

class Vitamin(Medicine):
    def requires_prescription(self) -> bool:
        return False 

    def storage_requirements(self) -> str:
        return "15 - 25 градусів, сухе місце"

                   
class Vaccine(Medicine):
    def requires_prescription(self) -> bool:
        return True 

    def storage_requirements(self) -> str:
        return "2 - 8 градусів, холодильник"

    def total_price(self) -> float:
        return super().total_price() * 1.1
                






