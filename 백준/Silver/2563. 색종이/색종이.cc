// https://www.acmicpc.net/problem/2563
// 24.10.31 THU

// 가로, 세로 크기의 각각 10인 정사각형 모양의 검은색 종이를 붙이고
// 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램

// 색종이가 겹치는 영역을 어떻게 처리할까?
// -> 전체 배열을 만들고 색종이가 붙은 부분을 1 로 표시하면 된다

#include <stdio.h>

int main()
{
    int n; // 색종이의 수 n
    scanf("%d", &n);

    int paper[100][100] = {0}; // 도화지 배열 초기화
    int x, y;                  // 입력 받을 좌표 x, y
    int sum = 0;               // 색종이가 붙은 부분

    for (int i = 0; i < n; i++)
    {
        scanf("%d %d", &x, &y); // 좌표 입력 받기

        // 색종이 영역을 도화지에 표시
        // x, y 부터 x+10, y+10 까지 넓이
        for (int row = x; row < x + 10; row++)
        {
            for (int col = y; col < y + 10; col++)
            {
                paper[row][col] = 1;
            }
        }
    }

    for (int i = 0; i < 100; i++)
    {
        for (int j = 0; j < 100; j++)
        {
            if (paper[i][j] == 1)
                sum++;
        }
    }
    printf("%d\n", sum);
}
