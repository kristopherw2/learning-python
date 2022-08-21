name = 'Kris'

age = 38

def name_generator(input_name, input_age):
    return "Name: " + input_name + " " + "Age: " + str(input_age)

def one_string(name, age):
    return name + str(age)

def decade_handler(age):
    return str( age // 10) + " decades"


print(name_generator(name, age))
print(one_string(name, age))
print(decade_handler(age))