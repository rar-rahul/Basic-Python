
#### List ####
newList = list(('mango','banana','apple')) #list is contructor here
print(newList)

#####
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[3:])

thislist[3:5] = ["bor","nariyal"]



## Insert and append method

thislist.insert(3,"testInsert")
thislist.append("appendTest")
print(thislist)

## Extend method to add element fro another list to current list
listOne = ["test","one","two"]
listSecond = ["second","third"]
listOne.extend(listSecond)
print(listOne)

#############################
###### REMOVE ###############
listOne.remove("one")
listOne.pop() ## without any input specified it will remove the last index
del listOne[1]
print(listOne)


############# Loop ##################
i = 0 # initialize
while i < len(thislist):
    print(thislist[i])
    i = i + 1 # increment by 1


################### For #########\
listLoop = ["one","two","three"]
for c in listLoop:
    print(c)

[print(c) for c in listLoop] ## short hand syntax of for loop

########## copy method ####################
one = ["one","two","three"]
two = one.copy()

three = list(two) # using list method
four = two[:]

print(three)

############################# Tuple ##################

tuple = ("test","one","three")
t = ("forth",) # give comma at the end otherwise it will not identified as tuple
tuple += t
print(tuple)

##### change touple value while changing tuple into list
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
#x = tuple(y)



######### Set ##############

newSet = {"rar","lak","neh"}
updatedSet = {"sand","temp"}

#newSet.add(input())

set3 = newSet.union(updatedSet)
set4 = newSet | updatedSet
print(set4)

##calling set 
for c in newSet:
    print(c)


############## Dictionary ##################

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#print(thisdict["model"])

thisdict.update({"update":2024})
print(thisdict)
#print(thisdict.get("brand"))