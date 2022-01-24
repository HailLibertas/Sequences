# print("please input three integers separated by , ")
# a = input()
# b = input()
# c = input()
#
# result = a + b - c
# integer_values = []
# for value in result:
#     integer_values.append(int(value))
# print(integer_values)
# Take input from the user
# user_input = input("Please enter three numbers: ")
#
# # Split the given input string into 3 parts
# string_tokens = user_input.split(",")
#
# # Convert the tokens into integers
# int_tokens = []
# for st in string_tokens:
#     int_tokens.append(int(st))
#
# # Calculate the result: a + b - c
# a, b, c = int_tokens
# result = a + b - c
# # result = int_tokens[0] + int_tokens[1] - int_tokens[2]
#
# # Output the result
# print(result)


bilow = input("gali sadex number oo ay , u dhaxayso: ")

celcelis = bilow.split(",")
numbaro_kaliya = []
for kalmad in celcelis:
    numbaro_kaliya.append(int(kalmad))
a, b, c = numbaro_kaliya
jawaab = a + b - c
print(jawaab)