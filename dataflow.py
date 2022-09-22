#nested loops
"""
num = 200
if num > 100:
    print(f"{num} is greater than 50")
num = 20
if num > 100:
    print(f"{num} is greater than 50")
num = 10
if num > 5:
    print(f"{num} is greater than 5")
else:
    print(f"{num} is less than 5")
name = "Pesu"
if name == "Pesu":
    print(f"Here at {name} you will get knowledge of IT skills")
    print(f"{name} situated at Electronic city")
    print(f"{name} is in Bengaluru south")
else:
    print("You are in another IT institute")
    print("You are not in Bengaluru south")
    print("Thank you for your information")
brand = input("Enter your favourite Brand: ")
if brand == "XY" :
    print("It is children's brand")
elif brand == "AB":
    print("This is women's brand")
elif brand == "PQ":
    print("This is a men's brand")
else:
    print("Other brands are not available")
s = "hbs"
for x in s:
    print(x)
s = input("Enter some String: ")
i=0
for x in s:
    print("The character present at ",i,"index is :",x)
    i = i+1
i = 1
while i <= 10:
    print(i)
    i+=1
i = 0
while True:
    i = i+1
    print("Hello",i)
for i in range(4):
    for j in range(4):
        print("1=",i,"j=",j)
#Transfer staetments
for i in range(10):
    if i == 7:
        print("processing is enough..plz break")
        break
    print(i)
print("We are done with loop execution") 
for i in range(10):
    if i%2 ==0:
        continue
    print(i)
cart = [10,20,600,40,50]
for item in cart:
    if item >= 500:
        print("We cannot process this order")
        break
    print(item)
else:
    print("Congrats ... all items processed successfully")
cart = [10,20,30,40,50]
for item in cart:
    if item >= 500:
        print("We cannot process this order")
        break
    print(item)
else:
    print("Congrats ... all items processed successfully")
    if True:
        pass
def m1(): pass
num =int(input("Enter a num"))
for var in range(5):
    print(var)#object is not iterable range(start(0),end,step(1)),non premitive data
    
n = 100
i =1
while True:
    print(n)
    i = i+1
    if i == 10:
        break
for i in range(4):
    for j in range(4):
        for k in range(4):
            print("i=",i,"j=",j,"k=",k)
            
#break:break loop execution based on some condition
for i in range(10):
    if i==7:
        print("processing is enough..plz break")
        break
    print(i)
print("We are done with loop execution")

#continue:To skip current iteration and continue next iteration
for i in range(10):
    if i%2==0:
        continue
    print(i)
    
cart = [10, 20, 30, 40, 50]
for item in cart:
    if item>=500:
        print("We cannot process this order")
        break
    print(item)
else:print("Congrats ... all items processed successfully")


cart = [10, 20, 600, 40, 50]
for item in cart:
    if item>=500:
        print("We cannot process this order")
        break
    print(item)
else:print("Congrats ... all items processed successfully")
"""
#pass statement:In our programming syntactically if block is 
#required which won't do anything then we can define that empty block with pass keyword.
#if True:expected an indented block after "if" statement on line 1
if True:
    pass
#Sometimes in the parent class we have to declare a function with empty 
#body and child class responsible to provide proper implementation
def m1():pass

#assert statement:The assert keyword is used when debugging code.
#city = "Yadgir"
#assert city == "Wadgera","city should be 'Wadgera'"
#AssertionError:city should be 'Wadgera'

greet = "Hello"
#if the condition returns True, then nothing happens:
assert greet == "Hello"


