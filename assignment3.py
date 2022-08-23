# 1. Create a list of 'person' dictionaries with name, age, and list of
#       hobbies for each person. Fill in any data you want
from unicodedata import name


persons = [
            {
                'name': 'Kris', 
                'age': '38', 
                'hobbies': ['weightlifting', 'gaming']
            }, 
            {
                'name': 'Zoe', 
                'age': '21',
                'hobbies': ['music', 'gaming']
            }, 
            {
                'name': 'Evan',
                'age': '21',
                'hobbies': ['being emo', 'gaming'] 
            }
        ]

# 2. Use a list comprehension to convert this list of persons into a list of names (of the persons!)
name_list = [person['name'] for person in persons]
print(name_list)

# 3. Use a list comprehension to check whether all persons are older than 20.
older_than_twenty = all([int(person['age']) > 20 for person in persons])
print(older_than_twenty)

# 4. Copy the person list such that you can safely edit the name of the first person (without changing the original list).
copied_persons = [person.copy() for person in persons]
copied_persons[0]['name'] = 'Dan'
print(copied_persons, persons)

# 5 Unpack the persons of the original list into different variables and output these variables
person_1, person_2, person_3 = persons
print(person_1)
print(person_2)
print(person_3)