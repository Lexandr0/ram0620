while True:

    user_input = input("Sisesta number 1-1000:")

    try:
        number = int(user_input)
    except:
        print("Vale sümbol, sisesta number 1-1000")
        continue

    if number < 1 or number > 1000:
        print("Vale sümbol, sisesta number 1-1000")
        continue

    result = ""

    # tuhaded
    if number >= 1000:
        result = result + "M"
        number = number - 1000

    # sajad
    if number >= 900:
        result = result + "CM"
        number = number - 900

    elif number >= 500:
        result = result + "D"
        number = number - 500

    elif number >= 400:
        result = result + "CD"
        number = number - 400

    while number >= 100:
        result = result + "C"
        number = number - 100

    # kümned
    if number >= 90:
        result = result + "XC"
        number = number - 90

    elif number >= 50:
        result = result + "L"
        number = number - 50

    elif number >= 40:
        result = result + "XL"
        number = number - 40

    while number >= 10:
        result = result + "X"
        number = number - 10

    # ühed
    if number == 9:
        result = result + "IX"
        number = 0

    elif number >= 5:
        result = result + "V"
        number = number - 5

    elif number == 4:
        result = result + "IV"
        number = 0

    while number >= 1:
        result = result + "I"
        number = number - 1

    print("Rooma number:", result)
    break
