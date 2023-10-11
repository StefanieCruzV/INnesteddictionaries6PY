# #Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# #1
x[1][0] = 15
print(x)
# #2
students[0]['last_name'] = "Bryant"
print(students)
# #3
sports_directory["soccer"][0] = "Andres"
print(sports_directory)
# #4
z[0]['y'] = 30
print(z)
print("---------------------------------------")
# #Iterate Through a List of Dictionaries

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(students):
    for i in range(len(students)):
        print("\n")
        for key, val in students[i].items():
            print(key, "-", val,)


iterateDictionary(students)
print("--------------------------------------00-")
# Get Values From a List of Dictionaries


def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        # print(i)
        if key_name in (some_list[i]):
            print(some_list[i][key_name])


iterateDictionary2('first_name', students)
# print(iterateDictionary2('first_name', students))

print("---------------------------------------")
# GIterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# def printInfo(some_dict):
#     for key,var in some_dict.items():
#         print(f"{key} {len(var)}\n{var}\n")
# printInfo(dojo)


def printInfo(some_dict):
    for key, a in some_dict.items():
        print(f"\n{len(a)} {key.upper()}\n")
        for var in some_dict[key]:
            print(f"{var} ")


printInfo(dojo)
