print("******************************************")
print("All copyrights belong to @ts._.taha in IG")
print("******************************************")
print()
print("Hello There!")
first_name = input("What's your first name? ")
print("Welcome to the handypack1.0 " + first_name.capitalize() + " !")
app_choice = input("(C)alculator or (W)eightCalculator or (L)engthCalculator? ")
if app_choice.upper() == "C":
    operation = input("Choose your operation? (M)ultiply , (A)ddition , (S)ubstraction , (D)ivide ")
    if operation.upper() == "M":
        first_number = input("FirstNumber: ")
        second_number = input("SecondNumber: ")
        print("Your Result:")
        print(float(first_number) * float(second_number))
    elif operation.upper() == "A":
        first_number = input("FirstNumber: ")
        second_number = input("SecondNumber: ")
        print("Your Result:")
        print(float(first_number) + float(second_number))
    elif operation.upper() == "S":
        first_number = input("FirstNumber: ")
        second_number = input("SecondNumber: ")
        print("Your Result:")
        print(float(first_number) - float(second_number))
    elif operation.upper() == "D":
        first_number = input("FirstNumber: ")
        second_number = input("SecondNumber: ")
        print("Your Result:")
        print(float(first_number) / float(second_number))
if app_choice.upper() == "W":
    operation_choice = input("Kindly choose the unit you wish to calculate into (L)bs , (K)g ")
    if operation_choice.upper() == "L":
        weight = input("Weight in Kg: ")
        print("Your weight in Lbs is:")
        current_weight = float(weight) * 2.205
        print(str(current_weight) + " Lbs")
    if operation_choice.upper() == "K":
        weight = input("Weight in Lbs: ")
        print("Your weight in Kg is:")
        current_weight = float(weight) / 2.205
        print(str(current_weight) + " Kg")
if app_choice.upper() == "L":
    operation_choice = input("Kindly choose the unit you wish to calculate into (C)m , (I)nch ")
    if operation_choice.upper() == "C":
        length = input("Length in Inch: ")
        print("Your length in Cm is:")
        current_length = float(length) * 2.54
        print(str(current_length) + " Cm")
    if operation_choice.upper() == "I":
        length = input("Length in Cm: ")
        print("Your length in Inch is:")
        current_length = float(length) / 2.54
        print(str(current_length) + " Inch")

print()
print("******************************************")
print("All copyrights belong to @ts._.taha in IG")
print("******************************************")
