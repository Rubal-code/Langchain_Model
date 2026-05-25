from pydantic import BaseModel #pydantic is the library that allows us to create data models with type validation and parsing. It is commonly used in Python for data validation and settings management.

# basic example
class my_student(BaseModel):
    name: str
    age: int
    grade: str

new_student={'name': 'Alice', 'age': 20, 'grade': 'A'}
student1 = my_student(**new_student) # we use ** to unpack the dictionary and pass its contents as keyword arguments to the my_student model. This allows us to create an instance of my_student with the values from the new_student dictionary.

print(student1)

# default values
class my_teacher(BaseModel):
    name: str
    subject: str
    years_of_experience: int = 5 # we can set a default value for years_of_experience, so if it is not provided when creating an instance of my_teacher, it will default to 5.

teacher1={'name': 'Mr. Smith', 'subject': 'Math'}
teacher_instance = my_teacher(**teacher1)
print(teacher_instance.years_of_experience) # this will print 5, since we did not provide a value for years_of_experience when creating the teacher_instance.

# optional fields
from typing import Optional
class my_course(BaseModel):
    name: str
    description: Optional[str] = None # we can use Optional to indicate that the description field is optional. If it is not provided, it will default to None.
course1={'name': 'Introduction to Python'}
course_instance = my_course(**course1)
print(course_instance.description) # this will print None, since we did not provide a value for description when creating the course_instance.

# pydantic is coerce which means it will try to convert the input data to the specified types. For example, if we provide a string for the age field in my_student, pydantic will attempt to convert it to an integer.

# we can get into json or in dict format
print(student1.model_dump_json()) # this will print the student1 instance in JSON format.  