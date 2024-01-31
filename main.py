import logging
logging.basicConfig(level = logging.DEBUG)

while True:
    result = 0

    a = float(input("Podaj pierwszą liczbe: "))
    operation = input("Podaj operacje jaką chcesz wykonać: '+' - dodawanie, '-' - odejmowanie, '*' - mnozenie, '/' - dzielenie: ")
    b = float(input("Podaj drugą liczbe: "))


    if(operation == '+'):
        result = a + b
    elif(operation == '-'):
        result = a - b
    elif(operation == '*'):
        result = a * b
    elif(operation == '/'):
        if(a == 0 or b == 0):
            print("Nie dziel przez 0!!")
        else:
            result = a / b

    print(f"Wynik to: {result}")

    if operation == '+':
        logging.debug(f"Dodaję {a} i {b}")
    elif operation == '-':
        logging.debug(f"Odejmuje {a} i {b}")
    elif operation == '*':
        logging.debug(f"Mnoze {a} i {b}")
    elif operation == '/':
        logging.debug(f"Dziele {a} i {b}")

    answer = input("Czy chcesz wykonac wiecej obliczen? [T/N] ")
    if answer.lower() != 't':
        break
