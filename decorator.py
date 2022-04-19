"""decorator allow you to wrap your function
 around another function"""
import time
def cal_square(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number ** 2)
    end = time.time()
    print(f"cal_square took {str((end-start) * 1000)}  mil sec")
    return result

def cal_cube(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number ** 3)
    end = time.time()
    print(f"cal_square took {str((end-start) * 1000)}  mil sec")
    return result

array = range(1,1000)

squared_number = cal_square(array)
cube_number = cal_cube(array)
#print(cube_number)
#performance of a function: is how long it take to run

#using time module to calculate the run time of function

#print(f"cal_square took {str((end-start) * 1000)}  mil sec")

