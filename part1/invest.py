def invest(amount, rate, time):
    result = amount * ((1+rate)**time)
    return result

str1 = input("principal amount: $")
str2 = input("annual rate of return: ")
amnt = float(str1)
r = float(str2)

for i in range(1,9):
    tot = invest(amnt, r, i)
    print("year {}:".format(i), "${}".format(tot))

print("")

str3 = input("principal amount: $")
str4 = input("annual rate of return: ")
amnt2 = float(str3)
r2 = float(str4)

for j in range(1,6):
    tot2 = invest(amnt2, r2, j)
    print("year {}:".format(j), "${}".format(tot2))
