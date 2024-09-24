def knp (incput1, input2):
    if (user_input == "kamen" and user_input2 == "papir"):
        print("2 hrac vyhral ")
    elif user_input == "kamen" and user_input2 == "nuzky":
        print("1 hrac vyhral ")
    elif user_input == "kamen" and user_input2 == "kamen":
        print("remiza ")
    elif user_input == "nuzky" and user_input2 == "nuzky":
        print("remiza ")
    elif user_input == "kamen" and user_input2 == "kamen":
        print("remiza ")
    elif user_input == "nuzky" and user_input2 == "papir":
        print("1 hrac vyhral")
    elif user_input == "nuzky" and user_input2 == "kamen":
        print("2 hrac vyhral")
    elif user_input == "kamen" and user_input2 == "papir":
        print("2 hrac vyhral")

try_again = "y"
while try_again == "y" or try_again == "":
    user_input = input("1 hrac zadej kamen/nuzky/papir\n")
    user_input2 = input("2 hrac zadej kamen/nuzky/papir\n")
    knp(user_input, user_input2)
    try_again = input("Hrat znovu ? [Enter]")