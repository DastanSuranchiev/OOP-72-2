from faker import Faker
# faker это генератор вымышленных данных
# name() это метод библиотки faker котрый генерирует полное имя
# email() генерирует почту
# age генерирует возраст
rus = Faker("ru_RU")
eng = Faker("en_US")
for i in range(10):
    print(rus.name())
print()
for i in range(10):
    print(eng.name())
print()
f = Faker("en_US")
name = f.first_name()
email = f.email()
age = f.random_int(min=18, max=65)
print(name)
print(email)
print(age)


print()
print()
print()


from tabulate import tabulate
# tabulate помещает или превравает списки в таблицу
tasks = [
    ["Наумова", "Марфа", "Яковлевна"],
    ["Фадеева", "Оксана", "Вячеславовна"],
    ["Радислав", "Захарьевич", "Корнилов"],
]

print(tabulate(tasks, headers=["Фамилия", "Имя", "Отчество"], tablefmt="grid"))
print(tabulate(tasks, headers=["Фамилия", "Имя", "Отчество"], tablefmt="simple_grid"))
print(tabulate(tasks, headers=["Фамилия", "Имя", "Отчество"], tablefmt="double_grid"))
print(tabulate(tasks, headers=["Фамилия", "Имя", "Отчество"], tablefmt="fancy_grid"))

persons = []
for i in range(20):
    name = f.first_name()
    email = f.email()
    age = f.random_int(min=18, max=65)
    persons.append([name,email,age])
print(tabulate(persons, headers=["Имя", "Email", "Возраст"], tablefmt="simple_grid"))