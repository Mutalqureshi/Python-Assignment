#!/usr/bin/env python
# coding: utf-8

# In[1]:


""" 
Answer # 1
    Write a Python function to calculate the factorial of a number (a non-negative
integer). The function accepts the number as an argument.
"""

def factorial(n):
    num = 1
    while n > 0:
        num *= n
        n -= 1
    return num

print(factorial(1))


# In[2]:


"""
Answer # 2
    Write a Python function that accepts a string and calculate the number of upper
case letters and lower case letters.
"""

def caseCLC(string):
    uppers = 0
    lowers = 0
    for char in string:
        if char.islower():
            lowers += 1
        elif char.isupper():
            uppers += 1
    return uppers, lowers

print(caseCLC("Hello Ali Asghar! are you ready to be called as Microsoft Certified Python Developer after 14 December?"))


# In[3]:


"""
Answer # 3
    Write a Python function to print the even numbers from a given list.
"""


def evenIndex(nums):
    li = []
    for num in range(0,len(nums)):
        if nums[num] % 2 == 0:
            li.append(nums[num])
    return li
    
print(evenIndex([114,26,33,5,63,7,445,6,74,64,45.5,102.2,44]))


# In[ ]:


"""
Answer # 4
Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same
backward as forward, e.g., madam
"""

def palindromeTEST(word):
    reverse = ''.join(reversed(word))
    if word == reverse and word != "":
        return "You entered a palindrome."
    else:
        return "It is'nt palindrome."

check_palindrome = input("Enter any word to test if it is pelindrome: ")
print(palindromeTEST(check_palindrome))


# In[ ]:


"""
Answer # 5
Write a Python function that takes a number as a parameter and check the
number is prime or not.
"""

def isprime():
    nums = int(input("Enter any number to check if it is prime or not: "))
    return prime(nums)

def prime(nums):
    if nums > 1:
        for num in range(2,nums):
            if (nums % num) == 0:
                print("It is not a prime number.")
                print(num,"times",nums//num, "is", nums)
                break
        else:
            print("It is a prime number.")

isprime()


# In[ ]:


"""
Answer # 6
Suppose a customer is shopping in a market and you need to print all the items
which user bought from market.
Write a function which accepts the multiple arguments of user shopping list and
print all the items which user bought from market.
(Hint: Arbitrary Argument concept can make this task ease)
"""



def boughtITEM():
    cart = []
    while True:                                  
        carts = input("\nEnter an item to add it in your cart: \nor Press [ENTER] to finish: \n")
        if carts == "":
            break
        cart.append(carts)
    item_list = ""
    for item in range(0,len(cart)):
        item_list = item_list + cart[item].title() + "\n"
    print("\nItems you have bought is:\n"+item_list)

boughtITEM()


# In[ ]:




