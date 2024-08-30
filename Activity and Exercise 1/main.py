"""
money = int(input("How much money do you have? "))
nintendoWiis = 400
canAfford = int(money/nintendoWiis)
print("Based on your money, you can afford", canAfford)
left = int(money%nintendoWiis)
add = int(nintendoWiis - canAfford)
print("In order for you to buy another one, the additional is ",add)


"""

"""
number = input("Enter a number: ")
factorial = 0

for i in range(1, number + 1):
    factorial = factorial * i
print("The factorial of ", number, "is", factorial)

"""


""
number = int(input("Enter a number: "))
x = 1
while x <= number:
    if number % x == 0:
        print(x)
        x = x + 1
    else:
        x = x * 1

