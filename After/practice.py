n = int(input())

people = {}

for _ in range(n):
    event = input().strip()
    name, action = event.split()

    if action == 'enter':  
        people[name] = True
    elif action == 'leave':
        del people[name]

for name in sorted(people.keys(), reverse=True):
    print(name)