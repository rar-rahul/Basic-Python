a = 10
b = 5

##function declearation
def addnumber(a,b):
    print(a + b)
    
addnumber(a,b)

def checkLarge():
    a = 50
    b = 60
    if(a > b):
        return "true"
    else:
       return "false"

res = checkLarge()


def getValue(*arg):

    print("this the first arg"+arg[0])

getValue("test")

################## Lamda ##############

abc = lambda a,b : a * b # one expression can take multiple argurment
cde = lambda a,b,c : a+b+c
print(cde(5,50,10))

input = int(input("Please Enter The Number Here:"))

if(input > 10):
    print("Yes it is greater")
elif(input == 10):
    print("It is same value")
else:
    print("not matching")


