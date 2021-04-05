cars = {
    "honda": 3000,
    "hyundai": 3000,
    "bmw": 4000,
    "audi": 4500,
    "bentley": 100000,
}

for num, (name, price) in enumerate(cars.items(), 1):
    print(f'{num}) {name}: {price}$')


def key_check(dict):
    cname = input("Enter car name: ")
    if cname in dict:
        x = dict[cname]
        print(f"{x}")
        return x
    else:
        True

def check_answer():
    answer = input("Do you want to pay? [Yes/No]")

    if answer.lower() == "yes":
        print("thanks")
    elif answer.lower() == "no":
        print("OK, stop")
    else:
        input("Enter car name: ")


def menu_printer(dict):
    while True:
        pric = key_check(dict)
        quantity = input("Quantity: ")
        full_price = float(pric) * float(quantity)
        print(f"{full_price} $")
        check_answer()
        return print("goodbye")


menu_printer(cars)
