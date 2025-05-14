# string formatting
letter = "my name is {} and i am from {}"
country="india"
name="anchal"
print(letter.format(name,country))
# or
letter = "my name is {1} and i am from {0}"
print(letter.format(country,name))
"""using fstring"""
print(f"my name is {name} and i am from {country}")

"""for decimal"""
txt="price{p:.2f}"
print(txt.format(p=49.89799))

"""for value to directly print"""
print(f"my name is {{name}} and i am from {{country}}")
