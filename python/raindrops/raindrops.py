def convert(number):
    return "".join(drop for divisor, drop in {3: "Pling", 5: "Plang", 7: "Plong"}.items()
                    if number % divisor == 0) or str(number)
