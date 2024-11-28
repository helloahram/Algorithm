// https://www.acmicpc.net/problem/5086

/* 두 수가 주어졌을 때 다음 중 어떤 관계인지 구하는 프로그램 
 1. 첫번째 숫자가 두번째 숫자의 약수 factor
 2. 첫번째 숫자가 두번째 숫자의 배수 mulitple
 3. 약수와 배수 둘 다 아니다 neither
 */

/* a % b == 0 이면 factor, b % a == 0 이면 multiple,
 둘 다 != 0 이면 neither 출력 */

#include <stdio.h>

int main(){
    int a, b;

    while(1){
        scanf("%d %d", &a, &b);
        /* a b 둘 다 0 이면 종료 */
        if(a == 0 && b == 0)
            break;

        /* 두 수의 관계 계산 */
        if(b % a == 0){ 
            printf("factor\n");
        } else if (a % b == 0){
            printf("multiple\n");
        } else {
            printf("neither\n");
        }
    }
    
    return 0;
}