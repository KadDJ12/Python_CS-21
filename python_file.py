string = "(21 + 234) * 4"
res = string.replace(" ", "")

# Головний цикл: працює, поки у рядку є хоча б один оператор (+, -, *, /)
while any(op in res for op in ['+', '-', '*', '/']):
    memory = []
    inside_brackets = False
    
    # 1. Витягуємо вираз: з дужок або, якщо їх немає, беремо весь
    if "(" in res:
        for char in res:
            if char == "(":
                inside_brackets = True
                continue
            elif char == ")":
                inside_brackets = False
                break  # Зупиняємось після першої закриваючої дужки
                
            if inside_brackets:
                memory.append(char)
                
        # Зберігаємо точний текст з дужками, щоб потім замінити його на результат
        to_replace = "(" + "".join(memory) + ")"
    else:
        # Якщо дужок немає, відправляємо в memory весь рядок, що залишився
        memory = list(res)
        to_replace = res

    # 2. Ваш код розподілу на chislo1, action, chislo2
    chislo1 = []
    action = []
    chislo2 = []
    switsh_to_chislo2 = False
    
    for char in memory:
        if char.isdigit():
            if switsh_to_chislo2:
                chislo2.append(char)
            else:
                chislo1.append(char)
        else:
            action.append(char)
            switsh_to_chislo2 = True

    # Перетворюємо на числа
    num1 = int("".join(chislo1))
    num2 = int("".join(chislo2))
    operator = "".join(action)

    # 3. Виконуємо дію
    match operator:
        case '+':
            res1 = num1 + num2
        case '-':
            res1 = num1 - num2
        case '*':
            res1 = num1 * num2
        case '/':
            if num2 != 0:
                # Використовуємо int(), щоб не з'явилась крапка (float),
                # бо isdigit() не вміє читати дробові числа.
                res1 = int(num1 / num2) 
            else:
                raise ValueError("Ділення на нуль!")
        case _:
            raise ValueError(f"Невідомий оператор: {operator}")

    # 4. ЗАМІНА: Вставляємо порахований res1 назад у рядок
    # Функція replace замінить "(21+234)" на "255", або потім "255*2" на "510"
    res = res.replace(to_replace, str(res1), 1)

# Коли всі дії виконані, цикл завершиться, і в res залишиться тільки фінальна цифра
print(f"Результат обчислення виразу {string} = {res}")