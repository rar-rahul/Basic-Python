print("Hellow world")
print(5)
print("Hellow Rahul please change the line \n from there ok \n ok i am changing the line")


#variable
a = 5
b = "5" 

#to check type of str and number
print(type(a))
print(type("5"))

#print(type(a))  #type

x = "Global varible"

#function decleration
def myFunc():
    x = "testing local varible"
    print(x)

myFunc()

#String Methods
#String are immutable
a = "rahul raut I am !!!!!!!! RAR !!!!!!!!" 
b = "I am Rahul raut"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
#split into list like array
print(b.split(" "))
print(a.count("rahul"))

c = "Here is te swap method"

print(c.swapcase())

# in loop method 
text = "Here is the string need to check"

print("Here" in text)

for c in "Rahul":
    print(c)
if "Here" in text:
    print("yesy here is present")

###############################

name = input("Please enter your name")

print("My name is" +name)


