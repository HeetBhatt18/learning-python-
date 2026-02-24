# student = {'name':'john', 'age': 25, 'courses': ['math', 'compsci']}

# print (student['name'])

# print (student['courses'])

# print (student['age'])  to print all the values seperately 





# student = {'name':'john', 'age': 25, 'courses': ['math', 'compsci']}

# print(student['phone'])   this shows the error if key does not exsist in the list 

# print(student.get('phone', 'not found')) # this will not show error if key does not exsist in the list




# student = {'name':'john', 'age': 25, 'courses': ['math', 'compsci']}

# student ['name'] = 'jane'

# print(student)  # this will update the value of the key name from john to jane



# student = {'name':'john', 'age': 25, 'courses': ['math', 'compsci']}

# student ['phone'] = '555-55555555' # this will add new key and value to the dictionary

# print(student)




# student = {'name':'john', 'age': 25, 'courses': ['math', 'compsci'], 'phone': '555-55555555'}

# student.update({'name': 'jane' , 'age': 27 , 'phone': '5-5' , 'courses': ['Art'] })

# print(student)  # this will update multiple key values at once and if key does not exsist it will add new key and value to the dictionary




student = {'name':'john', 'age': 25, 'courses': ['math', 'compsci']}

# del student['age']

# print(student)  # this will delete the key age and its value from the dictionary

# print(len(student)) # this will print the length of the dictionary which is 3 in this case 

# print(student.keys()) # this will print all the keys in the dictionary

# print(student.values()) # this will print all the values in the dictionary

# print(student.items())

# for key in student:
#     print(key) # this will print all the keys in the dictionary one by one

for key , value in student.items():
    print(key , value)  # this will print all the keys and values in the dictionary one by one