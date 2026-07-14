# if-else condition

num = 77
num = int(input("enter any number : "))
res = "even" if num%2==0 else "odd"
print(res)

num = int(input("enter any number : "))
if num > 0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")        

num = int(input("enter first number : "))
num2 = int(input("enter second number : "))
res = "first is largest " if num>num2 else "second is largest"
print(res)

num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))
num3 = int(input("enter third number : "))
if num1>num2 and num1>num3:
    print("first number is largest")
elif num2>num3:
    print("second is largest")
else:
    print("third is largest")        


year = int(input("enter the year : "))
res = "leap year " if year%4==0 else "normal year"
print(res)

letter = input("enter any letter : ")
res = "vowel" if letter in "aeiou" else "consonent"
print(res)

num = int(input("enter number : "))
if num>=0 and num<=100:
    print("number is in range from 0 to 100")
else:
    print("not in range")    

user = input("enter the username : ")
passw = input("enter the password : ")
if user=="admin" and passw=="password123":
    print("login successfull")
else:
    print("invalid username or password")    

passwd = input("enter your password : ")
if len(passwd)>=8:
    print("strong password")
else:
    print("weak password")    










