#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Dictionaries
# OOP - classes
# Numpy, Pandas


# In[ ]:


'Name': Amit        # key:value
'City': Maynooth
'Nationality':
'Zipcode': 


# In[ ]:


[], list() # lists
{}, dict() # disctionaries


# In[1]:


info = {'Name': 'Amit', 'City': 'Maynooth', 'Nationality': 'India','Zipcode': 'hdhhv'}


# In[2]:


info['City']


# In[3]:


print(info)


# In[3]:


info_group_b = { '200' : {'Name': 'Carlos', 'City':'Dublin'},
                  '201' : {'Name': 'Camila', 'City':'Bray'},}


# In[4]:


print(info_group_b)


# In[5]:


info_group_b['201']


# In[19]:


info_group_b['201']['Name']


# In[21]:


info_group_b['201']['City']


# In[23]:


info_group_b['201']['City'] = 'Dublin'


# In[25]:


print(info_group_b)


# In[27]:


info.keys()


# In[29]:


info.values()


# In[6]:


for key in info.keys():
    info[key] = '0000'


# In[7]:


info


# In[35]:


for key in info:
    info[key] = '9999'


# In[37]:


info


# In[39]:


info['color'] = 'red'


# In[41]:


info


# In[43]:


info2 = dict(little=1, medium=2)


# In[45]:


info2


# In[47]:


info['Name']


# In[49]:


info.get('Name')


# In[51]:


info['birthday']


# In[13]:


info.get('birthday',-1)


# In[65]:


'birthday' in info.keys()


# In[67]:


'Name' in info


# In[15]:


# dir({})


# In[71]:


for k in info:
    print(k)


# In[16]:


info.items()


# In[20]:


for k,v in info.items():
    print(k,v)


# In[79]:


info.items()


# In[ ]:


[] # list
{} # dict
() # tuple


# In[21]:


info.keys()


# In[23]:


list(info.keys())[0]


# In[89]:


list(info.values())


# In[24]:


info['new_key'] = 'new_value'
info


# In[25]:


info.update({'new_key1': 'new_value1', 'new_key2': 'new_value2'})


# In[26]:


info


# In[5]:


students_data = {
    'id_0' : {
        'name' : {
            'first_name' : 'Camilla',
            'second_name' : 'Cabelo',
            'adress' : {'city' : 'Los Angeles'}
        }
    },
    'id_1' : 'unknown'
}


# In[6]:


students_data['id_0']['name']['adress']['city']


# In[7]:


students_data.get('id_2', 'NA')


# # Write a dictionary with numbers as key and its squares as value
# {
#     1:1,
#     2:4,
#     3:9
# }

# In[17]:


squareValues = {}
for i in range(1, 4):
    squareValues[i] = i * i
print(squareValues)


# # Question 2
# # https://www.py4e.com/html3/09-dictionaries

# In[33]:


file = open('mbox.txt', 'r')
days_week = {}
for f in file:
    if f.startswith('From '):
        key = f.split()[2]
        if key in days_week.keys():
            days_week[key] = days_week[key]+1
        else:
            days_week[key] = 1
file.close()


# In[34]:


days_week


# In[112]:


file = open('mbox.txt', 'r')
days_week = {}
for f in file:
    if f.startswith('From '):
        key = f.split()[2]
        if key in days_week.keys():
            days_week[key] = days_week[key]+1
        else:
            days_week[key] = 1    # creates new entry or key:value pair in the dictionary
file.close()


# In[114]:


days_week


# In[120]:


file = open('mbox.txt', 'r')
email_dict = {}
for f in file:
    if f.startswith('From '):
        key = f.split()[1]
        if key in email_dict:
            email_dict[key] += 1
        else:
            email_dict[key] = 1
file.close()


# In[122]:


email_dict


# In[41]:


file = open('mbox.txt', 'r')
domain_dict = {}
for f in file:
    if f.startswith('From:'):
        index = f.find('@')
        domain_name = f[index+1:].replace('\n','')
        if domain_name in domain_dict.keys():
            domain_dict[domain_name] = domain_dict[domain_name]+1
        else:
            domain_dict[domain_name] = 1
file.close()


# In[47]:


file = open('mbox.txt', 'r')
domain_dict = {}
for f in file:
    if f.startswith('From:'):
        domain_name = f.split('@')[1].replace('\n','')
        if domain_name in domain_dict.keys():
            domain_dict[domain_name] = domain_dict[domain_name]+1
        else:
            domain_dict[domain_name] = 1
file.close()


# In[48]:


domain_dict


# # OOP

# In[1]:


# procedural programming
# data analtics - data understanding/business understanding
                 # data preparation & transformations
                 # exploratory data analysis, visualisations
                 # machine learning/AI 
                 # predictive analytics


# In[2]:


class Car():
    def __init__(self):
        self.__color = '' # private variable
        self.make = 'toyota' # public variable 
        self.__model = 'yaris'
        self.__mileage = 0


# In[3]:


myCar1 = Car() #  car object created


# In[4]:


myCar2 = Car()


# In[5]:


myCar1.__color


# In[ ]:


myCar1.make


# In[6]:


myCar1._Car__model


# In[7]:


myCar2.make = 'ferrari'


# In[8]:


myCar2.make


# In[9]:


myCar1.__model


# In[30]:


import random
class Car():
    def __init__(self, color = 'red'):  # initialization constructor
        self.__color = color # private variable
        self.make = 'toyota' # public variable 
        self.__model = 'yaris'
        self.__mileage = 0
    def setColor(self, value):
        colors = ['red', 'green', 'yellow']
        index = random.randint(0,2)
        self.__color = colors[index]
    def getColor(self):
        return self.__color


# In[31]:


from car import Car


# In[17]:


myCar3 = Car()


# In[18]:


myCar3.getColor()


# In[13]:


myCar3.setColor(value = 'yellow')
print(myCar3.getColor())


# In[13]:


class Shapes():          # Base class
    def __init__(self):
        self.length = 1
    def area(self):
        pass
    def perimeter(self):
        pass             # Return NotImplementedError


# In[14]:


class Circle(Shapes):    # inheritance
    def area(self):
        return 3.14*self.length*self.length
    def perimeter(self):
        return 2*3.14*self.length


# In[15]:


circle1 = Circle()


# In[16]:


circle1.length = 10


# In[17]:


circle1.area()


# In[18]:


circle1.perimeter()


# In[19]:


circle2 = Circle()
circle2.length = 25
circle2.area()


# In[20]:


class Rectangle(Shapes):
    def __init__(self):
        self.length2 = 1
    def area(self):
        return self.length*self.length2
    def perimeter(self):
        return 2*(self.length+self.length2)


# In[21]:


rectangle1 = Rectangle()


# In[22]:


rectangle1.length = 25
rectangle1.length2 = 10
rectangle1.area()


# In[23]:


rectangle1.perimeter()


# In[24]:


from Shapes import Shapes
Shapes1 = Shapes()


# In[60]:


Shapes1.length


# In[ ]:


# create a class for H.Dip group A students.
# properties: name, location, grades in subject math, python.
# method: whether the student has passed or not.
# create two objects 

