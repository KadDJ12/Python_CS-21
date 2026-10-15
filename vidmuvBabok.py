import random
from functools import wraps


def parse(line):
    try:
        name, num = line.split()
        return float(num)
    except (AttributeError, ValueError): 
        return None

def shema_coutner_aftet_limit(threshold):
    def decorator(random_values):
        @wraps(random_values)
        def wrapper(*args, **kwargs):
            counted = 0
            for line in random_values(*args, **kwargs):
                amount = parse(line)
                if amount is not None and abs(amount) >= threshold:
                    counted += amount
                    print(f"Попередження: підозрілих сум на {counted}")
                yield line
        return wrapper
    return decorator


def shadow(limit=200):
    def decorator(random_values):
        @wraps(random_values)
        def wrapper(*args, **kwargs):
            total = 0
            triggered = False
            for line in random_values(*args, **kwargs):
                print(line)
                amount = parse(line)
                if amount is None:
                    continue
                total += amount
                if total > limit and not triggered:
                    triggered = True
                    print("Тіньовий ліміт перевищено. Активую схему")
                yield line
            return total
        return wrapper
    return decorator



@shadow(limit=200)
@shema_coutner_aftet_limit(threshold=250)
def transactions():
    options = ["payment 120", "refund 50", "transfer 300", "oops", "payment abc"]
    for _ in range(8):
        yield random.choice(options)



gen = transactions()
try:
    while True:
        next(gen)
except StopIteration as stop:
    print("Фінальна сума:", stop.value)








