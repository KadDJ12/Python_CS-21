print('welcome to the calculator program!')
chiclo1 = input('Please enter chiclo: ')
chiclo2 = input('Please enter chiclo: ')
action = str(input("+, -, *, /,: "))

match action:
    case '+':
        print(int(chiclo1) + int(chiclo2))
    case '-':
        print(int(chiclo1) - int(chiclo2))
    case '*':
        print(int(chiclo1) * int(chiclo2))
    case '/':
        print(int(chiclo1) / int(chiclo2))




