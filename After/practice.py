n, m = map(int, input().split())

pokemon_list = {}
reversed_list = {}
result = []

for i in range(n):
    monster = input().strip()
    pokemon_list[i+1] = monster
    reversed_list[monster] = i+1

for _ in range(m):
    question = input().strip()

    if question.isdigit():
        result.append(pokemon_list[int(question)])
    else:
        result.append(str(reversed_list[question]))

print('\n'.join(result))