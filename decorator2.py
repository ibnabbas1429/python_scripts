'''function is a  first class object in python what it menas 
is that it can be treated just like any variable and you can pass them as 
argument to another function or even return them as a return value'''

import time

def time_it(func):
    def wrapper(*args, **Kwargs):
        start = time.time()
        result = func(*args, **Kwargs)
        end = time.time()
        print(func.__name__+ "took" + str((end-start)*1000) + "mil sec")
        return result
    return wrapper

@time_it
def cal_square(numbers):
    
    result = []
    for number in numbers:
        result.append(number ** 2)
    
    return result

@time_it
def cal_cube(numbers):
    
    result = []
    for number in numbers:
        result.append(number ** 3)
    
    return result

array = range(1,1000)

squared_number = cal_square(array)
cube_number = cal_cube(array)