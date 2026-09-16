string = "2 + 2 * 2"
res = string.replace(" ", "")

while any(op in res for op in ['+', '-', '*', '/']):
    memory = []
    inside_brackets = False
    
    if "(" in res:
        for char in res:
            if char == "(":
                inside_brackets = True
                continue
            elif char == ")":
                inside_brackets = False
                break  
                
            if inside_brackets == True:
                memory.append(char)
                
        to_replace = "(" + "".join(memory) + ")"
    else:
        memory = str(res)
        to_replace = res

 
    mem_str = "".join(memory) if isinstance(memory, list) else memory
    for op in ['+', '-', '*', '/']:
        if op in mem_str:
            value = [mem_str.split(op)[0], op, mem_str.split(op)[1]]
            break

    chislo1 = int(value[0])
    znak = value[1]
    chislo2 = int(value[2])

    match znak:
        case '+':
            res1 = chislo1 + chislo2
        case '-':
            res1 = chislo1 - chislo2
        case '*':
            res1 = chislo1 * chislo2
        case '/':
            if chislo2 != 0:
                res1 = int(chislo1 / chislo2)
            else:
                raise ValueError("Ділення на нуль!")
        case _:
            raise ValueError(f"Невідомий оператор: {znak}")


    res = res.replace(to_replace, str(res1), 1)

print(f"Результат обчислення виразу {string} = {res1}")