// https://www.acmicpc.net/problem/2501

// n 의 약수들 중에 k 번째로 작은 수를 출력하는 프로그램 

#include <stdio.h>

int main(){
    int n, k; 
    scanf("%d %d", &n, &k);

    int devisor[n]; /* 약수를 저장할 배열 */
    int index = 0; /* 약수 개수를 저장할 변수 */

    /* i 1부터 n 까지 */
    for(int i = 1; i <= n; i++){
        /* 나머지가 0 이면 n 의 약수 */
        if(n % i == 0){
            devisor[index++] = i;
        }
    }
    
    if(k<=index) /* k번째 약수가 존재하는지 확인 */
        printf("%d\n", devisor[k-1]);
    else /* k번째 약수가 없다면 0 출력 */
        printf("0\n");
    
    return 0;
}