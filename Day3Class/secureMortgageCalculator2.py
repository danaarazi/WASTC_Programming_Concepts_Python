def pswd(x,wrong):
    if x!= "dana":
        print("that was attempt # ", wrong)
        if wrong < 3:
            print("that was the wrong password please enter the correct password: ", end="")
            return 0
        else:
            print("too many tries")
            quit()
    else:
        print("you are in")
        return 1
y = 0
wrong = 0
while y != 1:
    wrong += 1
    print("Please enter a password: ", end="")
    x = input()
    y = pswd(x,wrong)


print("Enter borrowed amount:", end='')
p = int(input())
print("entered annual APR rate%:", end='')
i = float(input())


r = i / 12 / 100
n = 30 * 12

x = (1 + r)**n
mp = (p * x * r) / (x-1)
mpFormatted = "%.2f" % mp
totalPayments = mp * n
totalPaymentsFormatted = "%.2f" % totalPayments
print("Your Monthly payment is: ", mpFormatted)
print("Your total payment is: ", totalPaymentsFormatted)