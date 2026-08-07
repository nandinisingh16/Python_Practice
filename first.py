#area of rectangle
n=int(input("enter length "))
m=int(input("enter breadth "))
area=n*m
print("area of rectangle is ",area)


#shopping cart program
item=input("enter item name ")
price=float(input("enter item price "))
quantity=int(input("enter item quantity "))
price=price*quantity
print("total price is ",price)


#Madlibs program
adj1=input("enter an adjective ")
noun1=input("enter a noun ")
verb1=input("enter a verb ending ing ")
adj2=input("enter another adjective ")
adj3=input("enter one more adjective ")
print(f"Today I went to a {adj1} zoo. I saw a(n) {noun1} {verb1} in a tree. It was very {adj2}. I also saw a(n) {adj3} elephant. It was a great day!")


#circumference and area of circle
import math
radius=float(input("enter radius of circle "))
p=math.pi
circum=2*p*radius
circum=round(circum,3)
area=p*pow(radius,2)
print("area of circle is ",area)
print("circumference of circle is ",circum)

#python calculator
n1=float(input("enter first number "))
n2=float(input("enter second number "))
choice=input("ENTER OPERATION +,-,*,/ ")
if(choice=="+"):
    print("sum is ",round(n1+n2,2))
elif(choice=="-"):
    print("difference is ",round(n1-n2,2))
elif(choice=="*"):
    print("product is ",round(n1*n2,2))
elif(choice=="/"):
    print("quotient is ",round(n1/n2,2))
else:
    print("invalid operation")

#validate user input
a=input("enter user input ")
if(len(a)>=12 and a.find(" ")==-1 and  a.isalpha()):
    print("valid input")
else:
    print("invalid input")

#compound interest calculator
principal=0
interest=0
time=0
while principal<=0:
    principal=float(input("enter principal amount "))
    if principal<=0:
        print("principal amount cannot be negative")
while interest<=0:
    interest=float(input("enter interest rate "))
    if interest<=0:
        print("interest rate cannot be negative")
while time<=0:
    time=float(input("enter time in years "))
    if time<=0:
        print("time cannot be negative")
final_amount=principal*(1+(interest/100))**time
final_amount=round(final_amount,2)
print(f"balance after {time} years is {final_amount}")

#format string
price=34.6789
print(f"price is {price: .2f}")
name = "Bob"
num=7
print(f"price is {num:04}")
print(f"|{price:10}|")

#countdown timer
import time

time_input=int(input("enter time in seconds "))
for x in range(time_input, 0, -1):
    sec=x%60
    min=int(x/60)%60
    hour=int(x/3600)
    print(f"{hour:02}:{min:02}:{sec:02}")
    time.sleep(1)
print("time is up")

for x in range(3):
    i=x
    for y in range(i,i+5):
        print(y, end=" ")
    print()