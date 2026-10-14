from abc import ABC, abstractmethod


class JunkItem:
  def __init__(self, name: str, quantity: int, value: float):
    if isinstance(name, str) and type(quantity) is int and isinstance(value, (float, int)):
      self.name = name
      self.quantity = quantity
      self.value = float(value)
    else:
      raise ValueError(f"Неправильний тип даних при створенні JunkItem: {name}, {quantity}, {value}")


  def formating_data(self):
    replaced_value = str(self.value).replace(".", ",")
    return f"{self.name} | {self.quantity} | {replaced_value}\n"


  def __repr__(self):
    return f"JunkItem(name='{self.name}', quantity={self.quantity}, value={self.value})"



class StorageBackend(ABC):  # інтерфейс для сховищ
  @abstractmethod
  def save(self, items: list) -> None:
    pass


  @abstractmethod
  def load(self) -> list[JunkItem]:
    pass




class JunkStorage(StorageBackend):
  def __init__(self, filename: str):
    self.filename = filename


  def serialize(self, items: list[JunkItem], filename: str):
    if isinstance(items, list):
      with open(filename, "w", encoding="utf-8") as f:
        for item in items:
          if isinstance(item, JunkItem):
            f.write(item.formating_data())
          else:
            print(f"Пропущено некоректний об'єкт: {item}")
    else:
      print("Неправильний тип об'єкта передано в serializer")


  def parse(self, filename: str) -> list[JunkItem]:
    items_list = []
    try:
      with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
          line = line.strip()
          if not line:
            continue

          line_to_parth = line.split("|")
          if len(line_to_parth) != 3:
            print(f"Попередження: немає трьох полів -> {line}")
            continue

          try:
            name = line_to_parth[0].strip()
            quantity = int(line_to_parth[1].strip())
            value = float(line_to_parth[2].replace(",", ".").strip())
            items_list.append(JunkItem(name, quantity, value))
          except ValueError:
            print(f"Попередження: помилка типів (кількість не int / ціна не float) -> {line}")
            continue
    except FileNotFoundError:
      return []
    return items_list


  def save(self, items: list) -> None:
    self.serialize(items, self.filename)


  def load(self) -> list[JunkItem]:
    return self.parse(self.filename)




class Warehouse:
  def __init__(self, storage: StorageBackend):
    self.storage = storage
    self.items: list[JunkItem] = self.storage.load()


  def add_item(self, item: JunkItem):
    if isinstance(item, JunkItem):
      self.items.append(item)


  def get(self, name: str):
    item = self.find(name)
    if item:
      self.items.remove(item)
      return item
    return None


  def find(self, name: str):
    for i in self.items:
      if i.name.lower() == name.lower():
        return i
    return None


  def sync(self):
    self.storage.save(self.items)





file_path = "example.txt"

# 1. Створення предметів з умови
item1 = JunkItem("Бляшанка", 5, 2.5)
item2 = JunkItem("Стара плата", 3, 7.8)
item3 = JunkItem("Купа дротів", 10, 1.2)

# 2. Збереження у файл через JunkStorage
storage = JunkStorage(file_path)
storage.save([item1, item2, item3])

# 3. Робота через Warehouse
warehouse = Warehouse(storage)
print("\nЗавантажені об'єкти на складі:")
for item in warehouse.items:
  print(f"{item} (тип value: {type(item.value)})")

# Перевірка пошуку
found = warehouse.find("Купа дротів")
print(f"\nРезультат пошуку: {found}")