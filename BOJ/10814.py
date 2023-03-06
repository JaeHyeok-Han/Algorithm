import sys

people_count = int(sys.stdin.readline())
list_of_people = []

for i in range(people_count):
    input_str = sys.stdin.readline().strip().split(' ')
    age = int(input_str[0])
    name = input_str[1]
    list_of_people.append((age, name, i))
list_of_people.sort(key=lambda x: (x[0], x[2]))

for people in list_of_people:
    print(f'{people[0]} {people[1]}')
