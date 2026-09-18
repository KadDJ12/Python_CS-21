from medicine import Antibiotic, Vitamin, Vaccine, Medicine

lidokain = Antibiotic("lidokain", 13, 15.0)
print(lidokain.info())

vitamin_B1 = Vitamin("vitamin_B1", 87, 3.0)
print(vitamin_B1.info())

vacina_vid_ckazy = Vaccine("vacina_vid_ckazy", 4, 100.0)
print(vacina_vid_ckazy.info())


def print_all(items: list[Medicine]) -> None:
    for item in items:
        print(item.info())


