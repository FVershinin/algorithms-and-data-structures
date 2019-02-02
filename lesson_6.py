from memory_profiler import profile
from pympler import asizeof as size

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

class PersonWithSlots:
    __slots__ = ['firstname', 'lastname']
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

person = Person('firstname', 'lastname')
person_with_slots = PersonWithSlots('firstname', 'lastname')

print('person:')
print(size.asizeof(person))
print('person with slots:')
print(size.asizeof(person_with_slots))

# Profile не работает с генератором "yeld"

@profile
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b


fib(1000)


# Line #    Mem usage    Increment   Line Contents
# ================================================
#      6     13.3 MiB     13.3 MiB   @profile
#      7                             def fib(n):
#      8     13.3 MiB      0.0 MiB       a, b = 0, 1
#      9     13.3 MiB      0.0 MiB       while a < n:
#     10     13.3 MiB      0.0 MiB           print(a)
#     11     13.3 MiB      0.0 MiB           a, b = b, a + b