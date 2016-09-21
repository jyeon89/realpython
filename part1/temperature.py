def CtoF(cel):
    fah = cel*9/5 + 32
    return fah

def FtoC(fah):
    cel = (fah-32)*5/9
    return cel

Str1 = input("Celcius: ")
Str2 = input("Fahrenheit: ")

celc = float(Str1)
fahr = float(Str2)

print("Celcius to Fahrenheit: ", CtoF(celc), "F")
print("Fahrenheit to Celcius: ", FtoC(fahr), "C")
