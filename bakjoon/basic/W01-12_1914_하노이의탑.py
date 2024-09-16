# n 개의 원판을 첫 번째 장대에서 세 번째 장대로 옮긴다 
# 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다 
# 위의 원판이 아래 원판보다 작아야 한다

def hanoi(n: int, fromP: int, toP: int, tempP: int) -> None:    
    # N 이 1 일 때는 바로 From -> To 로 옮기기 
    if n == 1:
        print(f"{fromP} {toP}")
        return

    # N-1 을 시작 기둥에서 임시 기둥으로 옮기기 
    hanoi(n-1, fromP, tempP, toP)

    # 가장 큰 원판 N 을 from -> To 옮기기 
    print(f"{fromP} {toP}")
    # result.append(f"{fromP} {toP}")

    # N-1 을 임시 기둥에서 목표 기둥으로 옮기기 
    hanoi(n-1, tempP, toP, fromP)

if __name__ == '__main__':
    # 기둥 개수 입력받기 
    n = int(input())

    print(2 ** n -1) # 이동 횟수 출력하기 
    
    # N 이 20 보다 큰 경우 과정 출력 안 해도 됨 
    if n <= 20: 
        # 1번에서 3번으로 이동, 2번은 임시 기둥 
        hanoi(n, 1, 3, 2)