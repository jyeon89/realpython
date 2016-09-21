a = input("Enger a positive interger: ")
num = int(a)

for i in range(1,num+1):
    if num%i == 0:
        print(i,"is a divisor of ", a)
        
