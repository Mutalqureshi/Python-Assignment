#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Question1:
Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city
in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information
stored in your dictionary. Add a new key value pair about qualification then update the qualification value to high academic
level then delete it.
'''

person_dictionary={"First_name":"John","Last_name":"Smith","Age":"21","City":"karachi"}
for key, value in person_dictionary.items():
    print(key+" : "+value)
    
print("\n Add Qualification \n")
person_dictionary["qualification"]="intermediate"
for key, value in person_dictionary.items():
    print(key+" : "+value)
    
print("\n Update Qualification \n")
person_dictionary["qualification"]="high academic"
for key, value in person_dictionary.items():
    print(key+" : "+value)


# In[4]:


'''Question2:
Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
Create a dictionary of information about each city and include the country that the city is in,
its approximate population, and one fact about that city. The keys for each city’s dictionary should
be something like country, population, and fact. Print the name of each city and all of the information
you have stored about it.
'''

cities={
    "Lahore":{
        "country":"pakistan",
        "population":12188000,
        "fact":"Lahore is the capital city of the Pakistani province of Punjab. It is the second largest and most populouscity in Pakistan"
    },
    "Karachi":{
        "country":"pakistan",
        "population":15741000,
        "fact":"Karachi is vital to Pakistan's economy, contributing 42 per cent of GDP , 70 per cent of income tax revenue and 62 per cent of sales tax revenue"
    },
    "Islamabad":{
        "country":"pakistan",
        "population":1095064,
        "fact":"Islamabad is the capital city of Pakistan, and is federally administered as part of the Islamabad Capital Territory. Built as a planned city in the 1960s"
    }
}
for citykey,cityinfo in cities.items():
    print("\n"+citykey+"\n")
    for city in cityinfo:
        print(city+" : "+str(cityinfo[city]))


# In[6]:


'''Question3:
A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3,
the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15.
Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
'''
flag='y'
while flag!='n':
    age=int(input("Enter age : "))
    if age>12:
        print("Ticket is 15$")
    elif age>=3:
        print("Ticket is 10$")
    else:
        print("Ticket is free")
    flag=input("Are you want to take ticket y/n: ")


# In[9]:


'''Question4:
Write a function called favorite_book() that accepts one parameter, title. The function should print a message, 
such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as
an argument in the function call.
'''

def favorite_book(title):
    print(title)
book_title="One of my favorite books is Alice in Wonderland."
if(len(book_title)!=0):
    favorite_book(book_title)
else:
    print("Please populate the book title")


# In[ ]:


'''Question5:
Guess the number game
Write a program which randomly generate a number between 1 to 30 and ask the user in input
field to guess the correct number. Give three chances to user guess the number and also give hint to 
user if hidden number is greater or smaller than the number he given to input field.
'''
import random
c=0
rNumber=0
while c<3:
    rNumber=int(random.randrange(1,30))
    userNumber=int(input("Enter number between 1 and 30: "))
    c=c+1
    if rNumber>userNumber:
        print("Hidden number is greater\n")
    elif rNumber<userNumber:
        print("Hidden number is Smaller\n")
    else:
        print("Hidden number is equal\n")


# In[ ]:





# In[ ]:





# In[ ]:




