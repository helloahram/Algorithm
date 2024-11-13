// https://www.acmicpc.net/problem/11279
// 24.10.28 MON

/*
* 최대 힙
1. 배열에 자연수 x 를 넣는다
2. 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거한다
프로그램은 처음에 비어 있는 배열에서 시작하게 된다
*/

// 연산의 개수 N 연산의 정보를 나타내는 x
// x 가 자연수라면 배열에 넣기 + 배열에 추가하고, 정렬하기
// x 가 0 이라면 배열에서 가장 큰 값 출력하고 배열에서 제거

#include <stdio.h>

int heap_size = 0;
int heap[100001];

// 힙에 값을 추가하는 함수
void insert(int x)
{
    int i = ++heap_size; // 1. 힙 크기 증가 후, 마지막 인덱스 i 설정
    // ++heap_size 해주는 이유는 index 1 부터 시작하게 만들기
    while ((i != 1) && (x > heap[i / 2])) // 2. 부모와 비교
    {
        heap[i] = heap[i / 2]; // 3. 부모 노드의 값을 아래로 내리기
        i /= 2;                // 4. 부모의 인덱스로 이동
    }
    heap[i] = x; // 5. 최종 위치에 새로운 값을 넣음
}

// 힙에서 최대값을 추출하는 함수
int delete_max()
{
    if (heap_size == 0)
        return 0;

    int max = heap[1];            // 1. 루트에 있는 최대값 저장
    int temp = heap[heap_size--]; // 2. 힙의 마지막 값을 가져오고, 힙 크기 줄이기
    int parent = 1;               // 3. 부모 인덱스 초기화 (루트부터 시작)
    int child = 2;                // 4. 자식 인덱스 초기화 (왼쪽 자식부터 시작)

    while (child <= heap_size)
    { // 자식이 힙의 범위 내에 있는 동안 선택
        if (child < heap_size && heap[child] < heap[child + 1])
            child++; // 오른쪽 자식이 더 크면 child 를 오른쪽 자식으로 변경

        if (temp >= heap[child]) // temp가 자식보다 크면 자리를 찾음, 반복 종료
            break;

        // 자식을 부모로 올려서 자리 채움
        heap[parent] = heap[child];
        parent = child; // 부모를 자식으로 업데이트
        child *= 2;     // 왼쪽 자식으로 이동
    }
    heap[parent] = temp; // 최종 위치에 temp 배치
    return max;          // 최대값 반환
}

int main()
{
    int n, x;
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &x);

        if (x != 0)
            insert(x);

        else
            printf("%d\n", delete_max());
    }
}