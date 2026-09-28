## Exercise 1: Frequency Counter

### Frequency Counter
from collections import Counter

technologies = [
    "api",
    "python",
    "api",
    "git",
    "python",
    "api",
]


# 1. Using dictionary.get()
frequency_with_get = {}

for tech in technologies:
    frequency_with_get[tech] = frequency_with_get.get(tech, 0) + 1

print("1. Using get():", frequency_with_get)


# 2. Using if/else
frequency_with_if = {}

for tech in technologies:
    if tech in frequency_with_if:
        frequency_with_if[tech] += 1
    else:
        frequency_with_if[tech] = 1

print("2. Using if/else:", frequency_with_if)


# 3. Using Counter
frequency_with_counter = Counter(technologies)

print("3. Counter object:", frequency_with_counter)
print("   As dictionary:", dict(frequency_with_counter))


# 4. Using dictionary comprehension and count()
frequency_with_comprehension = {
    tech: technologies.count(tech)
    for tech in dict.fromkeys(technologies)
}

print("4. Using comprehension:", frequency_with_comprehension)


### Employee Filtering
employees = [
    {"name": "A", "experience": 2},
    {"name": "B", "experience": 5},
    {"name": "C", "experience": 4},
]

# 1. Normal loop
experienced_employees_loop = []

for employee in employees:
    if employee["experience"] >= 4:
        experienced_employees_loop.append(employee)

print("Normal loop:", experienced_employees_loop)


# 2. List comprehension
experienced_employees_comprehension = [
    employee
    for employee in employees
    if employee["experience"] >= 4
]

print("List comprehension:", experienced_employees_comprehension)


### Course Class Exercise
class Course:
    def __init__(self, name, duration_weeks):
        if duration_weeks <= 0:
            raise ValueError("Duration must be greater than zero")

        self.name = name
        self.duration_weeks = duration_weeks

    def describe(self):
        return f"{self.name} - {self.duration_weeks} weeks"


course = Course("FDE", 16)

print(course.describe())

class Course:
    def __init__(self, name, duration_weeks):
        if duration_weeks <= 0:
            raise ValueError("Duration must be greater than zero")

        self.name = name
        self.duration_weeks = duration_weeks

    def describe(self):
        return f"{self.name} - {self.duration_weeks} weeks"

### Inheritance Exercise
class OnlineCourse(Course):
    def __init__(self, name, duration_weeks, platform):
        super().__init__(name, duration_weeks)
        self.platform = platform

    def describe_platform(self):
        return f"{self.name} is available on {self.platform}"


course = OnlineCourse(
    "FDE",
    16,
    "Krish Naik Academy",
)

print(course.describe())
print(course.describe_platform())

#### Example Problems
# Example 1: Unique Values and Occurrences
values = [1, 2, 2, 3, 3, 3]
# Possible questions:
# - return unique values#
# - count occurrences

def unique_count(values):
    return {value: values.count(value) for value in set(values)}
def count_occurrences(values):
    return {value: values.count(value) for value in set(values)}

unique_values = set(values)
occurrences = count_occurrences(values)

print("Unique values:", unique_values)
print("Occurrences:", occurrences)

# Example 2 - 
employees = {
    "A": 2,
    "B": 5,
    "C": 4
}
#  Return employees with:
#  experience >= 4

def filter_experienced_employees(employees, min_experience):
    return {name: exp for name, exp in employees.items() if exp >= min_experience}

print("Employees with experience >= 4:", filter_experienced_employees(employees, 4))


# Example 3 — Fix the class
# Given:
class User:
    def __init__(name, age):
        name = name
        age = age
# Correct concept:
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Example 4 — Exception
# Complete:
try:
    value = int("abc")

except ValueError:
    print("Invalid")
#Expected:
#ValueError
