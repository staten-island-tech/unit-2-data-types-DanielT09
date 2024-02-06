import random

def tip_calculator(tip_percentage):
    sub_total = float(input("Enter subtotal: "))
    tip = sub_total * tip_percentage/100
    total = tip + sub_total
    print(f"Your tip is {tip} and your total is {total}")

def word_count():
    sentence = str.split(input("Enter a sentence: "))
    words = 0 
    for word in sentence:
        words += 1
    print(words)
    


def odd_or_even():
    number = int(input("Give me a number: "))
    if number%2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


def tip_based_on_percentage():
    bill = int(input("Enter a bill: "))
    service = input("How good was the service(bad, okay, good, great): ")
    if service == "bad":
        print("Don't pay a tip lol")
    elif service == "okay":
        print(f"Your tip is ${bill * 0.15}.")
    elif service == "good":
        print(f"Your tip is ${bill * 0.2}.")
    elif service == "great":
        print(f"Your tip is ${bill * 0.25}.")
    else:
        print("You didn't enter an option.")


def factor():
    number = int(input("Enter a number: "))
    x = 1
    factor = []
    while x <= number:
        if number%x == 0:
            factor.append(x)
            x += 1
        else:
            x += 1
    print(factor)



def greatestcf(number):
    x = 1
    factor = []
    while x <= number:
        if number%x == 0:
            factor.append(x)
            x += 1
        else:
            x += 1
    return factor

def gcf(x, y):
    a = 1
    x_factor = []
    while a <= x:
        if x%a == 0:
            x_factor.append(a)
            a += 1
        else:
            a += 1
    b = 1
    y_factor = []
    while b <= x:
        if y%b == 0:
            y_factor.append(b)
            b += 1
        else:
            b += 1
    gcf=0
    for factor in x_factor:
        if factor in y_factor:
            gcf = factor
    print(gcf)

def number_guess(x,y):
    history = []
    the_number = random.randint(x,y)
    global_guess = 0
    while global_guess == 0:
        guess = int(input(f"Guess a number from {x} to {y}: "))
        if guess == the_number:
            print(f"{guess} is correct!")
            print("Your guesses were: ")
            for i in history:
                print(i)
            global_guess = guess
        elif guess > the_number:
            print(f"{guess} is larger than the number, guess again.")
            history.append(guess)
        elif guess < the_number:
            print(f"{guess} is smaller than the number, try again.")
            history.append(guess)

number_guess(1,10)


