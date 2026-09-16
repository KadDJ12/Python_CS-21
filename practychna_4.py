deals = [ 
    ["Олексій", 500, "clean"],
    ["Марія", "сто", "suspicious"],
    ["Іван", 50, "clean"],
    ["Олена", 1500, "fraud"],
    ["Дмитро", 200, "pending"],
]

result = []

for name, amount, status in deals:
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        category = "Фальшиві дані"
    elif amount < 100:
        category = "Дрібнота"
    elif amount < 1000:
        category = "Середнячок"
    else:
        category = "Великий клієнт"

    match status:
        case "clean":
            decision = "Працювати без питань"
        case "suspicious":
            decision = "Перевірити документи"
        case "fraud":
            decision = "У чорний список"
        case _:
            decision = "Невідомий статус"

    result.append([name, category, decision])

print(result)