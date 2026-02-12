registartion = 21

data = []
n = int(input("enter number of element in the list: "))

for i in range(n):
    value = input("enter the list data it can string and number: ")
    if value.isdigit():
        data.append(int(value))
    else:
        if value != "":
            data.append(value)

number = []
numericaldata = 0
stringdata = 0
stringlist = []

for i in data:
    if type(i) == int:
        number.append(i)
        numericaldata = numericaldata + 1
    else:
        stringlist.append(i)
        stringdata = stringdata + 1

if registartion % 2 == 0:
    print(number[::-1])
else:
    print(stringlist[::-1])

print("The numerical data is:", numericaldata)
print("the string data is :", stringdata)
