# Message = "Hello World!"
# print(Message)
#
# name = input("Enter Your Name: ")
#
# print (f"This is the name: {name}", end="")



# while True:
#     try:
#         num = int(input("Enter a number: "))
#         break   # exit loop if success
#     except ValueError:
#         print("Please enter a valid number!")
#
# print("Double:", num * 2)


try:
    age = int(input("Enter Your Age: "))
    print(f"This is your {age}")
except ValueError:
    print("Bye world!")
