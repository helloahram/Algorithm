// https://www.acmicpc.net/problem/2869

// 달팽이는 높이 V미터인 막대를 올라간다 
// 낮에는 A미터 올라갈 수 있고 밤에는 B미터 미끄러진다 
// 달팽이가 나무 막대를 모두 올라가려면 며칠이 걸리는지 구하는 프로그램

// 도착 0 에서 올라가고 +a 내려가서 -b 정상까지 구하기 

#include <stdio.h>
int main(){
    int a, b, v; /* 올라가는 거리 a, 미끄러진 거리 b, 나무 높이 v */
    scanf("%d %d %d", &a, &b, &v);

    if(v>1000000000){ /* 입력 유효성 검사 */
        printf("Invalid Input\n");
        return 1;
    }

    /* v - b - 마지막 날 밤에 미끄러지지 않기 때문에 b 를 빼준다 */
    /* -1 은 정수 나눗셈의 올림 효과를 위해서 ex. (a+b-1)/b 공식 */
    /* a - b - 하루에 실제로 올라가는 순 높이, +1 은 마지막 날 포함 */
    int days = (v - b - 1)/ (a - b) + 1;
    printf("%d\n", days);

    return 0;
}

/* 원래 아래처럼 코드를 작성했는데, 시간 복잡도가 O(N) 이라고 안 좋은 함수라고 함 */
// #include <stdio.h>

// /* 달팽이가 나무를 올라가는 일자를 구하는 함수 */
// int going_snail(int a, int b, int v){
//     int height = 0; /* 누적 높이 */
//     int days = 0; /* 누적 일자 */
    
//     /* height 이 v 가 될 때까지 while */
//     while(height < v){
//         days++; /* 아침이니 누적 일자 +1 */
//         height += a;

//         /* a 만큼 올라가서 정상에 도달했다면 나오기 */
//         if(height >= v)
//             break;
//         height -= b;
//     }
//     /* 누적 일자 반환 */
//     return days;
// }

// int main(){
//     int a, b, v; /* 올라가는 거리 a, 미끄러진 거리 b, 나무 높이 v */
//     scanf("%d %d %d", &a, &b, &v);

//     printf("%d\n", going_snail(a, b, v));

//     return 0;
// }
