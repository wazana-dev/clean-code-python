from multiplier import multiplier
from kmh_to_mih import convert_speed
from person import Person

# Create the person
person = Person("Arthur", "Viana", 27)
person.info()
person.info(" Full Stack Developer")
print(person.name)

# Multiply number and print the result
prod = multiplier(5, 352)
print(prod)

# Convert and print the speed
convert_speed(100.5)

# Construct and print object
obj = {
    "person": {
        "name": person.name,
        "surname": person.surname,
        "age": person.age,
        "fullName": f"{person.name} {person.surname}",
    },
    "number": prod,
}
print(obj)
