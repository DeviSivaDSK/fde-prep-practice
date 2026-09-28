languages = ["python", "java", "typescript", "python"]

print(languages[0])

languages.append("go")

print(languages)


coordinates = (10, 20)

print(coordinates[0])

languages = ["python", "java", "python", "typescript"]

unique_languages = set(languages)

print(unique_languages)

employee = {
    "name": "Siva",
    "role": "QA Automation Engineer",
    "experience": 4
}

print(employee["name"])
print(employee["role"])


numbers = [1, 2, 3, 4, 5, 6]

squares = []

for number in numbers:
    squares.append(number * number)

print(squares)

squares = [number * number for number in numbers]

print(squares)

even_squares = [
    number * number
    for number in numbers
    if number % 2 == 0
]

print(even_squares)

def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(100, 3)

print(total)

def calculate_discount(price, discount_percent=10):
    discount = price * discount_percent / 100
    return price - discount


print(calculate_discount(1000))
# 900

print(calculate_discount(1000, 20))
# 800


#sample-exercise
def find_even_numbers(numbers):
    print([number for number in numbers if number % 2 == 0])

find_even_numbers([1, 2, 3, 4, 5, 6])


### OOPS
class Employee:

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def describe(self):
        return f"{self.name} works as {self.role}"

employee = Employee(
    "Siva",
    "QA Automation Engineer"
)

print(employee.describe())




class AIEngineer(Employee):

    def __init__(self, name, role, specialization):
        super().__init__(name, role)
        self.specialization = specialization

    def describe_specialization(self):
        return (
            f"{self.name} specializes in "
            f"{self.specialization}"
        )


engineer = AIEngineer(
    "Siva",
    "AI Engineer",
    "Natural Language Processing"
)
print(engineer.describe())
print(engineer.describe_specialization())


### Exception Handling
# try:
#     number = int(input("Enter number: "))

#     result = 100 / number

#     print(result)

# except ValueError:
#     print("Please enter a valid integer.")

# except ZeroDivisionError:
#     print("Number cannot be zero.")

def validate_experience(years):

    if years < 0:
        raise ValueError(
            "Experience cannot be negative"
        )

    return years

validate_experience(5)
validate_experience(-3)  # This will raise ValueError