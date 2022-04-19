#This is the use of for loop
number = [1,2,3,4,5,6,7,8,9,10]
even=[]
for num in number:
    #even = []
    if num % 2 == 0:
        even.append(num)
print(f"This is the output of the for loop: {even} ")

# the use of list comprehension

even2 = [num for num in number if num % 2 == 0]
print(f"This is the output of the list comprehension: {even2} ")

state = ["Abia","Adamawa","Bauchi","Ogun","Oyo","Lagos","Kwara","Ekiti","Ondo"]

capital = ["Umahia","Yola","Bauchi","Abeokuta","Ikeja","Ilorin","Ado","Akure"]

state_capital = {state:capital for state,capital in zip(state,capital)}

print(state_capital)