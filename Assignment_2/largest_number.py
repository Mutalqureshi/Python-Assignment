#!/usr/bin/env python
# coding: utf-8

# In[2]:


def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([4, 6, -8, 0]))


# In[ ]:




