number_of_hours = 24
units = "hours"


def hour_clock(days):
    return f"There are {days * number_of_hours} {units} in {days} days"


def validate_execute():
    try:
        user_input = int(list_elements)
        # Making conversion for only positive numbers
        if user_input > 0:
            result = hour_clock(user_input)
            print(result)
        elif user_input == 0:
            print("you have entered 0 which will mean 0 hours, please enter a positive number")
        else:
            print("You have entered a negative value. Enter a positive value")
    except ValueError:
        print("Your input is invalid, enter a number")


user_in = " "
while user_in != "exit":
    user_in = input(f"Welcome, Enter your input in comma separated form:\n")
    print(type(user_in.split(", ")))
    list_of_days = user_in.split(", ")
    print(type(set(list_of_days)))
    print(f"You have entered these {user_in.split()} values")
    for list_elements in set(list_of_days):
        validate_execute()
print(" Good Bye")
