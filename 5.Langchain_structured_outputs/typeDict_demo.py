from typing import TypedDict
class User(TypedDict):
    name: str
    age: int

new_person: User = {'name': 'Alice', 'age': 30}
print(new_person)