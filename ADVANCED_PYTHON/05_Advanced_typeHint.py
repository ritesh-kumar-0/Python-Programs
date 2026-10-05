'''Python hints atre added using the colon (:) Syntax for variables and the -> syntax for 
function return types.
Python typing module provides more advanced type hints, such as List, Tuple, Dict, and Union.

You can import List , Tuple and Dict types From the typing modules like this 
from typing import list, Tuple , Dict, Union'''

from typing import List, Tuple, Dict, Union

#List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

#Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

#Dictionary with string keys and integer values 
score: Dict[str, int] = {"Alice": 90, "Bob": 85}

#union type for    variables that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier = 12345  #Also valid 

print(numbers)
print(person)
print(score)
print(identifier)