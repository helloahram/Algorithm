# https://www.acmicpc.net/problem/1620

# N개의 포켓몬 이름이 주어졌을 때 M개의 문제를 맞추는 문제
# 문제가 숫자이면 해당하는 번호의 포켓몬 이름을, 
# 문제가 이름이면 해당하는 번호의 숫자를 출력 

# 질문이 숫자인지 글자인지 어떻게 알지?_? 

n, m = map(int, input().split())
# 포켓몬을 저장할 딕셔너리 
pokemon = {} # 번호 -> 이름 매핑 
reverse_pokemon = {} # 이름 -> 번호 매핑 

result = [] # 결과를 저장할 리스트 

for i in range(n):
    poke = input().strip()
    pokemon[i+1] = poke
    reverse_pokemon[poke] = i+1

for _ in range(m):
    question = input().strip()

    if question.isdigit(): # 숫자인 경우 
        result.append(pokemon[int(question)])
    else:
        result.append(str(reverse_pokemon[question]))

# 줄바꿈으로 출력 
print('\n'.join(result))
