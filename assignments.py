
#Assignments
# Write a Python program that assigns your name and age to two different variables. Then, reassign the age variable with a new value.

a="charan"
b=24
c=b
print(a)
print(c)


# In[100]:


# Assign the value of x = 10. Reassign it to x + 5 and print the result.


# In[101]:


x=10
x=x+5
print(x)


# In[102]:


# Take a number from the user as input. The input is a string by default. Convert it into an integer and print the result.


# In[121]:


a=input("enter the value: ")
print(a)
print(type(a))
b=int(a)
print(type(b))
print(b)


# In[122]:


# Assign a float value to a variable, then cast it to an integer. Print both the float and the integer values.


# In[3]:


a=20.5
print(type(a))
print(a)
b=int(a)
print(b)


# In[4]:


# Write a Python program that prompts the user to enter their age, and then cast the input to an integer.
#After that, assign their age in the next decade (age + 10) to a new variable and print it.


# In[6]:


a=int(input("enter your age: "))
b=type(a)
print(b)
c=a+10
print(c)


# In[7]:


# Problem: Write a Python program that asks the user for a number and checks whether it is odd or even.
#Print "Odd" or "Even" accordingly.


# In[5]:


a=int(input("enter a number: "))
if (a%2==0):
    print("a is even",a)
else:
    print("a is odd",a)


# In[6]:


# Write a Python program that takes a number as input and prints whether the number is positive, negative, or zero.


# In[9]:


a=int(input("enter a number: "))
if(a>0):
    print("it is a positive number")
elif(a<0):
    print("it is a negative number")
elif(a==0):
    print("the number is 0")
else:
    print("its not a number")


# In[ ]:


#Write a program that takes a student's marks as input and prints their grade based on the following scale:
# 90 and above: A
# 80 to 89: B
# 70 to 79: C
# 60 to 69: D
# Below 60: F


# In[2]:


sm=int(input("enter the marks: "))
if(sm>=90):
    print("A")
elif(sm>=80):
    print("B")
elif(sm>=70):
    print("C")
elif(sm>=60):
    print("D")
else:
    print("F")
    


# In[ ]:


# Write a Python program that takes three numbers as input and prints the largest of the three.


# In[7]:


a=int(input("enter the number: "))
b=int(input("enter the number: "))
c=int(input("enter the number: "))
if(a>b and a>c):
    print("a is greatest")
elif(b>c and b>a):
    print("b is greatest")
elif(c>a and c>b):
    print("c is greatest")
else:
    print("number is invalid!")


# In[8]:


# Write a Python program that takes a letter as input and checks whether it is a vowel or a consonant.


# In[16]:


vc=input("enter a letter: ")
cv=["a","e","i","o","u"]
if(vc in cv):
    print("The letter is a vowel")
else:
    print("The letter is a consonant")


# In[17]:


#  Write a Python program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input, 
#and then perform the appropriate operation.


# In[26]:


a=float(input("enter the 1st number: "))
b=float(input("enter the 2nd number: "))
c=input("enter an operation(+,-,*,/): ")
if(c=="+"):
    print(f"it is an addition {a+b}")
elif(c=="-"):
    print(f"it is an subtraction {a-b}")
elif(c=="*"):
    print(f"it is an muliplication {a*b}")
elif(c=="/"):
    if(b!=0):
        print(f"it is an division {a/b}")
    else:
        print("division is not possible")
else:
    print("number is invalid")


# In[27]:


#Write a Python program to find the sum of the first n natural numbers, where n is provided by the user.


# In[7]:


n=int(input("enter the number: "))
m=0
for i in range(1,n+1):
    m=m+i
print(m)


# In[8]:


#using formula


# In[7]:



n = int(input("Enter the number: "))
m = (n * (n + 1)) // 2
print(f"The sum of the first {n} natural numbers is: {m}")


# In[6]:


#Write a Python program to print the multiplication table of a number entered by the user, up to 10.


# In[6]:


n = int(input("Enter the number: "))
m=0
for i in range(1,11):
    m=n*i
    print(m)   
print(m)
    


# In[15]:


# Write a Python program that prints all even numbers between 1 and n, where n is provided by the user.


# In[17]:


n=int(input("enter the number: "))
for i in range(1,n+1):
    if(i%2==0):
        print(i)


# In[18]:


# Write a Python program to print numbers from n to 1, where n is provided by the user.


# In[3]:


n=int(input("enter the number: "))
for i in range(n,0,-1):
    print(i)


# In[4]:


n=int(input("enter the number: "))
for i in range(0,n+1,2):
    print(i)


# In[5]:


n = int(input("Enter the number: "))
i = 0
while i <= n:
    print(i)
    i += 2


# In[6]:


#Write a Python program that takes two numbers from the user and performs addition, subtraction,multiplication,and division.
#Display the results for each operation.


# In[7]:


a=float(input("enter the 1st number: "))
b=float(input("enter the 2nd number: "))
c=input("enter an operation(+,-,*,/): ")
if(c=="+"):
    print(f"it is an addition {a+b}")
elif(c=="-"):
    print(f"it is an subtraction {a-b}")
elif(c=="*"):
    print(f"it is an muliplication {a*b}")
elif(c=="/"):
    if(b!=0):
        print(f"it is an division {a/b}")
    else:
        print("division is not possible")
else:
    print("number is invalid")


# In[8]:


#  Write a Python program to calculate the remainder and the quotient of two numbers. Quotient Should be an Integer


# In[11]:


r=float(input("enter the number: "))
q=int(input("enter the number: "))

a=r//q
b=r%q
print("quotient: ",a)
print("remainder: ",b)


# In[12]:


#Given a number, write a program that calculates its square and cube.


# In[22]:


n=float(input("enter the number: "))

a=n**2
b=n**3
print(a)
print(b)


# In[23]:


# Start with a variable x = 10. Use assignment operators to increment x by 5, multiply it by 3, and subtract 4.
#Print the final value of x.


# In[25]:


x=10
print(x)
x=x+5
print(x)
x=x*3
print(x)
x=x-4
print(x)


# In[26]:


# Write a Python program that takes a number from the user and doubles it using the assignment operator.


# In[27]:


n=int(input("enter the number: "))
n*=2
print("double value: ",n)


# In[28]:


# Write a Python program to find the bitwise AND, OR, and XOR of two numbers.


# In[4]:


m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))

a = m & n
b = m | n
c = m ^ n

print(f"Bitwise AND of {m} and {n}: {a}")
print(f"Bitwise OR of {m} and {n}: {b}")
print(f"Bitwise XOR of {m} and {n}: {c}")


# In[5]:


# Write a Python program that takes a number, adds 7, multiplies it by 3, divides by 2, and prints the result.


# In[7]:


n=int(input("Enter the number: "))
print(n)
n=n+7
print(n)
n=n*3
print(n)
n=n/2
print(n)


# In[ ]:


# Sum of Two Numbers
# Write a function add(a, b) that takes two numbers as input and returns their sum.
# Example: add(3, 5) should return 8


# In[20]:


def fun1(a,b):
    print(f"The sum of {a} and {b} : {a+b} ")

fun1(3,5)


# In[21]:


# Odd or Even Checker
# Write a function is_even(n) that checks if a given number n is even. If it’s even, return True; otherwise, return False.
# Example: is_even(4) should return True, and is_even(7) should return False.


# In[2]:


def fun2(n):
    if(n%2==0):
        print(n," Is even and true")
    else:
        print(n," Is odd and false")
        
fun2(89)


# In[5]:


# String Length
# Write a function string_length(s) that returns the length of a given string s.
# Example: string_length("hello") should return 5.


# In[17]:


def string_length(s):
    s=len(s)
    print(s)

string_length("hello")


# In[16]:


s="hello"
m=len(s)
print(m)


# In[7]:


# Character Counter
# Write a function count_character(s, char) that counts the occurrences of a character char in a string s.
# Example: count_character("banana", "a") should return 3.


# In[19]:


def count_character(s):
    m=s.count("a")
    print(m)
count_character("banana")


# In[14]:


s="banana"
m=s.count("a")
print(m)


# In[20]:


# Write a function add(a, b, /) that only allows positional arguments. The function should return the sum of a and b.


# In[29]:


def add(a,b,/):
    print(f"The sum of {a} and {b} : {a+b} ")

add(3,5)


# In[30]:


# Write a function greet(*, name) that only accepts name as a keyword argument and returns a greeting message.


# In[33]:


def greet(*,name):
    print(f"HAPPY DIWALI {name}")

greet(name="CHARAN")


# In[34]:


# Write a function describe_person(age, /, *, name) that requires age as a positional-only argument and name 
# as a keyword-only argument.The function should return a description


# In[35]:


def person(age,/,*,name):
    print(f"My name is {name} and age is {age}")

person(24,name="Charan")


# In[36]:


# Write a function that accepts any number of positional arguments and returns their product.


# In[49]:


def function(*pro):
    num=1
    for i in pro:
        num*=i
    print(f"The product is: {num}")
function(1,8,6,5,4,9)


# In[50]:


# Write a function that accepts any number of keyword arguments and iterate the List of Numbers By using While Loops.


# In[64]:


def fun12(**pro):
    m=list(pro.values())
    i=0
    
    while(i<len(m)):
        print(m[i])
        i+=1
fun12(a=1,b=2,c=3,d=4,e=5,f=6)


# In[25]:


def fun(**pro):
    values=list(pro.values())
    for j in values[1:]:
        print(j)
fun(a=1,b=2,c=3)
        
        


# In[ ]:





# In[ ]:




