# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification
import numpy as np

def sumvalues(values):
    """Your documentation goes here:
    We set a variable to 0.0, assume no data is smaller than 0
    Then we iterate through each value in the list, and update _sum_ , each time a value larger than _sum_ is presented""" 
    _sum_=0.0  
    for i in values:
        try:
            np.float(i)
        except ValueError:
            raise TypeError("The data type is not integer or float")

        _sum_ = _sum_ + i
    return _sum_

def maxvalue(values):
    """Your documentation goes here"""    
    ## Your code goes here
    _max_ = 0
    for i in values:
        try:
            np.float(i)
            
        except ValueError:
            raise TypeError("The data type is not integer or float")
        if i > _max_:
            _max_= i
    return _max_

def minvalue(values):
    """Your documentation goes here"""    
    ## Your code goes here
    _min_ = values[0]
    for i in values:
        try:
            np.float(i)
        except ValueError:
            raise TypeError("The data type is not integer or float")
        if i < _min_:
            _min_= i
    return _min_

def meanvalue(values):
    """Your documentation goes here"""    
    ## Your code goes here
    for i in values:
        try:
            np.float(i)
        except ValueError:
            raise TypeError("The data type is not integer or float")
    mean = sumvalues(values)/len(values)
    return mean

def countvalue(values,xw):
    """Your documentation goes here"""    
    ## Your code goes here
    for i in values:
        try:
            np.float(i)
        except ValueError:
            raise TypeError("The data type is not integer or float")
    count = 0
    for i in values:
        if xw == i:
            count= count + 1
    return count

# arr1 = np.array()
# print(meannvalue(arr1))