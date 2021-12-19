from enum import  Enum

class Cat(Enum):
    good_cat = 1
    bad_cat = 2
    sweet_cat = 3


enbi = Cat.good_cat
roy = Cat.bad_cat
jake = Cat.good_cat


print(enbi)
print(enbi.name)
print(type(enbi.name))
print(enbi.value)
print(type(enbi.value))

