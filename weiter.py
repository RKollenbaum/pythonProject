Buchstabe = str(input("Buchstabe bitte:"))
if Buchstabe == "A":
    print("Apple")
elif Buchstabe == "B":
    print("Banane")
elif Buchstabe == "C":
    print("Coconut")


Credits = int(input("How many Credits?: "))
if Credits > 90:
    print("Senior")
elif Credits > 60:
    print("Junior")
elif Credits > 30:
    print("Sophomore")
else:
    print("Freshman")


RSI = float(input("RSI: "))
Momentum = float(input("Momentum: "))
if RSI and Momentum > 70:
    print("buy the stock!")
elif RSI and Momentum < 30:
    print("sell")
else:
    print("You´re your position")


#L6 P4: Write a program that sums a series of (positive) integers entered by
#the user, excluding all numbers that are greater than 100.

num = int(input("Gib ne Zahl: "))
total = 0
while (num != -1):
    if (num >= 0) and (num <= 100):
        total = total + num
        print(total)
    num = int(input("noch eine: "))
print('sum = ', format(total,',.0f'))

#L6P5. Write a program, in which the user can enter any number of positive and negative integer values,
# that displays the number of positive values entered,
# #as well as the number of negative values.

entry = int(input('Enter first number (enter 0 to exit): '))
pos_count = 0
neg_count = 0
while entry != 0:
    if entry >= 0:
        pos_count = pos_count + 1
    else:
        neg_count = neg_count + 1
    entry = int(input('Enter next number (enter 0 to quit): '))
print('\nNumber of positive values entered: ', format(pos_count))
print('Number of negative values entered: ', format(neg_count))