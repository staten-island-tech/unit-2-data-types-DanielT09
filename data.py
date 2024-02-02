def tip_calculator(tip_percentage):
    sub_total = float(input("Enter subtotal: "))
    tip = sub_total * tip_percentage/100
    total = tip + sub_total
    print(f"Your tip is {tip} and your total is {total}")

tip_calculator(15)