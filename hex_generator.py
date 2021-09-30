#! python3
import math

print("Decimal (base-10) to hexadecimal (base-16) converter.")
user_num = int(input("Enter your number: "))

d = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
}

hexadecimal = ''
while user_num > 0:
    remainder = user_num % 16
    hexadecimal = d[remainder] + hexadecimal
    user_num = user_num // 16

# Does not work with extremely large numbers e.g. 9999999999999999
# hex_list = []
# while math.floor(user_num) > 0:
#     user_num = user_num / 16
#     fraction = user_num % 1

#     whole = fraction * 16
#     hex_list.append(whole)


# hex_list.reverse()
# hex_str = ''
# for item in hex_list:
#     hex_str += d[int(item)]

print(f'Hexadecimal representation: {hexadecimal}')
