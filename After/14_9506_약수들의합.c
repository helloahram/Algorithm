// https://www.acmicpc.net/problem/9506
// 틀렸음 < 틀린 이유 perfect 인데 Perfect 로 써서ㅡ.ㅡ 

// n 이 자신을 제외한 모든 약수들의 합과 같으면 그 수를 완전수라고 한다
// n 이 완전수인지 아닌지 판단해주는 프로그램을 작성하라 
// 완전수라면 n 이 아닌 약수들의 합으로 나타내어 오름차순으로 출력한다 
// 완전수가 아니라면 n is NOT perfect 를 출력한다 

#include <stdio.h>

int main(){
    int n = 0;

    while(1){
        scanf("%d", &n);
        if (n == -1) break;
        
        int divisors[1000] = {0}; /* 약수를 저장할 배열 */
        int index = 0; 
        int sum = 0; /* 약수들의 합을 저장할 변수 */

        /* n 의 약수 구하기 (자신은 제외이므로 < n 까지만) */
        /* 약수인 경우 배열에 저장하고 sum 에 더하기 */
        for(int i = 1; i < n; i++){
            if(n % i == 0){ 
                divisors[index++] = i; 
                sum += i; 
            }
        }
        
        /* 완전수인지 검사하기 */
        if(n == sum){

            printf("%d = ", n);

            /* 약수 오름차순 정렬 */
            /* 이거 해도 맞았음 
            for(int i = 0; i < index - 1; i++){
                for(int j = i+1; j < index; j++){
                    if(divisors[i] > divisors[j]){
                        int temp = divisors[i];
                        divisors[i] = divisors[j];
                        divisors[j] = temp;
                    }
                }
            } */

            /* 약수 출력 */
            for(int i = 0; i < index; i++){
                printf("%d", divisors[i]);
                /* 마지막 숫자 전까지 + 표시해주기 */
                if(i < index-1) printf(" + ");
            }
            printf("\n");
        }
        else {
            printf("%d is NOT perfect.\n", n);
        }
    }
}