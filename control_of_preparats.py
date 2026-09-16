medications = [
    ["Амоксицилін", 100, "antibiotic", 15.5],      # Усе ок, температура в нормі
    ["Пфайзер", 50, "vaccine", 2.0],               # Надто холодно
    ["Вітамін С", 200, "vitamin", 28.5],           # Надто жарко
    ["Аспірин", "сто", "vitamin", 20.0],           # Помилка даних (кількість не int)
    ["Парацетамол", 500, "antibiotic", "20.0"],    # Помилка даних (температура не float)
    ["Ібупрофен", 300, "painkiller", 18.0],        # Невідома категорія
    ["Вакцина А", 10, "vaccine", 5.0],             # Межове значення (5.0 - має бути Норма)
    ["Вакцина Б", 20, "vaccine", 25.0],            # Межове значення (25.0 - має бути Норма)
    ["Плацебо", True, "vitamin", 10.0]             # Помилка даних (bool замість int)
]

for name , amount , category, teperature in medications:
    if type(amount)is not int or type(teperature) is not float:   # спочатку написав через isinstance але згадав що bool - це нащадок int і воно вертає true
        print(f"{name} - не правильний тип полів")
    else:
        match teperature:
            case t if t < 5.0:
                print(f"{name} - Надто холодно")
            case t if t > 25.0:
                print(f"{name} - Надто жарко")
            case _:
                print(f"{name} - Норма") 
            

        match category:
            case "antibiotic":
                print(f"{name} - Рецептуарний припарат")
            case "vitamin":
                print(f"{name} - Вільний продаж")
            case "vaccine":
                print(f"{name} - Потребує спецзберігання")
            case _:
                print(f"{name} - Невідома категорія")

        print("\n")






    
    


        