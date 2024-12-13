n, m = map(int, input().split())

no_seen = {input().strip() for _ in range(n)} # 듣도 못한 사람 set 생성 
# intersection() 으로 교집합을 바로 계산하여 불필요한 반복문과 리스트 조작 줄이기 
no_heard_seen = sorted(no_seen.intersection(input().strip() for _ in range(m)))

print(len(no_heard_seen))
print("\n".join(no_heard_seen))