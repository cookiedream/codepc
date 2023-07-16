#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;

int m;                  // 限制的步驟數
vector<int> A, B, C;    // 三個柱子的狀態

void print_hanoi(){
    printf( "A=>" );    // 印出柱子 A 的標記
    if( A.size() ){     // 如果柱子 A 不是空的
        printf( " " );
        for( int i = 0 ; i < A.size() ; i++ )
            printf( " %d", A[i] );  // 印出柱子 A 中的數字
    }
    printf( "\n" );
    printf( "B=>" );    // 印出柱子 B 的標記
    if( B.size() ){     // 如果柱子 B 不是空的
        printf( " " );
        for( int i = 0 ; i < B.size() ; i++ )
            printf( " %d", B[i] );  // 印出柱子 B 中的數字
    }
    printf( "\n" );
    printf( "C=>" );    // 印出柱子 C 的標記
    if( C.size() ){     // 如果柱子 C 不是空的
        printf( " " );
        for( int i = 0 ; i < C.size() ; i++ )
            printf( " %d", C[i] );  // 印出柱子 C 中的數字
    }
    printf( "\n" );
    printf( "\n" );
}

void hanoi( int n, vector<int> &start, vector<int> &temp, vector<int> &finish ){
    if( m <= 0 ) return;    // 如果步驟數已達到限制，則結束函式執行
    if( n == 1 ){
        finish.push_back( start.back() );  // 將最上方的一個數字移動到目標柱子上
        start.pop_back();                  // 從原柱子上刪除該數字
        print_hanoi();                      // 印出目前柱子狀態
        m--;                               // 步驟數減一
        return;
    }
    hanoi( n-1, start, finish, temp );    // 將 n-1 個數字從原柱子移動到暫存柱子上
    if( m <= 0 ) return;
    finish.push_back(start.back());    // 將最上方的一個數字移動到目標柱子上
    start.pop_back();                    // 從原柱子上刪除該數字
    print_hanoi();                        // 印出目前柱子狀態
    m--;                                 // 步驟數減一
    if( m <= 0 ) return;
    hanoi( n-1, temp, start, finish );    // 將暫存柱子上的 n-1 個數字移動到目標柱子上
}

int main(){
    int n;               // 柱子上的數字總數
    int problem = 1;     // 問題編號

    while( scanf( "%d%d", &n, &m ) != EOF && !(n == 0 && m == 0) ){
        printf( "Problem #%d\n\n", problem++ );    // 印出問題編號
        A.clear();                                 // 清空柱子 A
        B.clear();                                 // 清空柱子 B
        C.clear();                                 // 清空柱子 C

        for( int i = n ; i >= 1 ; i-- )
            A.push_back(i);                        // 將數字由大到小放入柱子 A
        print_hanoi();                              // 印出初始柱子狀態
        hanoi( n, A, B, C );                         // 執行河內塔演算法
    }
    return 0;
}
