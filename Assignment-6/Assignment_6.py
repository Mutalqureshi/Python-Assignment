#!/usr/bin/env python
# coding: utf-8

# In[3]:


class car:

    def __init__(self, model, color, number_plate, name, engine):
        self.model = model
        self.color = color
        self.number_plate = number_plate
        self.name = name
        self.engine = engine

car = car(
    "July 1972",
    "White",
    "PGR378",
    "CIVIC",
    "610HFF"
)

print(car.model)
print(car.color)
print(car.number_plate)
print(car.name)
print(car.engine)


# In[ ]:




