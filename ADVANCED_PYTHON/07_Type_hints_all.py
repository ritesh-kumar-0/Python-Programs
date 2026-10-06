#Type hint 

#Type hint for variables 
age: int = 20
name: str = "Ritesh"
height: float = 5.7
is_student: bool = True

print(age , name , height , is_student ) # Output: 20 Ritesh 5.7 True

#Type Hints in Function Parameters
#You can specify the expected type of function arguments.
def add(a: int, b: int): # a and b  should be an integer
    return a + b

print(add(10, 20))  # Output: 30

#Return Type Hint
def add(a: int, b: int) -> int:  # -> int ,  This function is expected to return an integer.
    return a + b

# Type Hint with str
def greet(name: str) -> str:
    return "Hello " + name

print(greet("Ritesh")) # Output: Hello Ritesh

#Type Hint with float
# Here both the parameter and return value are expected to be float.
def calculate_price(price: float) -> float:
    return price * 1.18

print(calculate_price(100.0)) # Output: 118.0

#Type Hint with bool
def is_adult(age: int) -> bool:
    return age >= 18

print(is_adult(20))   # Output: true

#Type Hint with List
def total(numbers: list[int]) -> int:  #A list containing integers.
    return sum(numbers)

print(total([10, 20, 30]))  # Output: 60

#Type Hint with Dictionary
student: dict[str, int] = {
    "Math": 90,
    "Python": 95
}
print(student)   # output: {'Math': 90, 'Python': 95}

#Type hint with tuple 
student: tuple[str, int] = ("Ritesh", 20) # firt value be str and second be int 
print(student)
