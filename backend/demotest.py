# lista = [1,2,3]
# listb = [2,3,4]
# a= sum(lista)
# b=sum(listb)
# print(a+b)



number1 = "64957"
number2 = "48"

num1=int(number1)
num2=int(number2)

def generateList(num):
    lista = [num]
    return lista

def addTwoLists(num1,num2):
    listc = num1+num2
    print(sum(listc))


List1 = generateList(num1)
print(List1)
List2 = generateList(num2)
print(List2)
List = addTwoLists(List1, List2)

