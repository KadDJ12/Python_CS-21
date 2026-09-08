class Calculator:
    def __init__(self, expression):
        # Видаляємо всі пробіли для зручності
        self.s = expression.replace(" ", "")
        self.pos = 0

    def current_char(self):
        """Повертає поточний символ або None, якщо рядок закінчився."""
        if self.pos < len(self.s):
            return self.s[self.pos]
        return None

    def next_char(self):
        """Пересуває вказівник на наступний символ."""
        self.pos += 1

    def parse_factor(self):
        """Обробляє числа, унарний мінус та дужки (Найвищий пріоритет)."""
        char = self.current_char()
        
        # Якщо це відкриваюча дужка
        if char == '(':
            self.next_char()
            result = self.parse_expression() # Рекурсивно обчислюємо вираз всередині
            self.next_char() # Пропускаємо закриваючу дужку ')'
            return result
            
        # Якщо це унарний мінус (наприклад, -5)
        elif char == '-':
            self.next_char()
            return -self.parse_factor()
            
        # Якщо це число
        elif char is not None and (char.isdigit() or char == '.'):
            start = self.pos
            # Збираємо всі цифри та крапку в одне число
            while self.current_char() is not None and (self.current_char().isdigit() or self.current_char() == '.'):
                self.next_char()
            return float(self.s[start:self.pos])
            
        raise ValueError(f"Неочікуваний символ: {char}")

    def parse_term(self):
        """Обробляє множення та ділення (Середній пріоритет)."""
        result = self.parse_factor()
        
        while self.current_char() in ('*', '/'):
            op = self.current_char()
            self.next_char()
            
            if op == '*':
                result *= self.parse_factor()
            elif op == '/':
                divisor = self.parse_factor()
                if divisor == 0:
                    raise ZeroDivisionError("Ділення на нуль!")
                result /= divisor
                
        return result

    def parse_expression(self):
        """Обробляє додавання та віднімання (Найнижчий пріоритет)."""
        result = self.parse_term()
        
        while self.current_char() in ('+', '-'):
            op = self.current_char()
            self.next_char()
            
            if op == '+':
                result += self.parse_term()
            elif op == '-':
                result -= self.parse_term()
                
        return result

    def evaluate(self):
        """Запускає обчислення всього виразу."""
        if not self.s:
            return 0
        return self.parse_expression()






# --- Приклад використання ---
if __name__ == "__main__":
    formulas = [
        "2 + 2 * 2",
        "(2 + 2) * 2",
        "10 / 2 - -3",
        "5 * (10 + (3 - 1) * 2) / 2"
    ]
    
    for formula in formulas:
        calc = Calculator(formula)
        result = calc.evaluate()
        print(f"{formula} = {result}")
