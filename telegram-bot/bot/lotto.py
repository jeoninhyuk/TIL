import  random

lotteryNumbers = []


for i in range (0,6):
    number = random.randint(1,46)

    while number in lotteryNumbers:

        number = random.randint(1,50)

    lotteryNumbers.append(number)

lotteryNumbers.sort()

userNumbers = []
for i in range(0,6):
    number = int(input("please enter a number between 1 and 46"))
    wile number<1 or number>46:
        number = int(input("Please try again: enter a number between 1 and 46."))

    userNumbers.append(number)

userNumbers.sort()

print(">>>Today's lottery numbers are:")
print(lotteryNumbers)

print(">>> Your selection:")
print(uerNumbers)

counter = 0
for number in userNumbers:
    if number in lotteryNumbers:
        counter += 1
print("You have guessed " + str(counter) + "number(s) correctly.")