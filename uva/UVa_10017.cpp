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
//定義了一個名為 hanoi 的函式，它接受四個參數：一個整數 n 和三個 vector<int> 型別的參考參數 start、temp 和 finish。
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

    //成功讀取到 n 和 m 的值，並且沒有遇到檔案結尾時，非同時等於零時條件成立。
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


// 這段程式碼是用來解決河內塔問題的，讓我們一步一步詳細解釋其原理和邏輯：

// 1.首先，程式碼使用vector<int>來表示三個柱子A、B和C的狀態，並且定義了一個全域變數m來表示限制的步驟數。
// 2.print_hanoi()函式用於打印出目前柱子的狀態。它使用printf來印出每個柱子的標記，然後遍歷柱子的內容並印出數字。
// 3.hanoi()函式是用遞迴的方式實現河內塔算法。它接受四個參數：n表示要移動的數字總數，start、temp和finish分別表示起始柱子、暫存柱子和目標柱子。
// 4.在hanoi()函式中，首先檢查步驟數是否已達到限制，如果是則直接返回。
// 5.再來，如果n等於1，表示只有一個數字需要移動。在這種情況下，將起始柱子start的最上方的一個數字移動到目標柱子finish上，並從起始柱子中刪除該數字。然後打印出目前柱子的狀態，並將步驟數減一。
// 6.如果n大於1，則遞迴調用hanoi()函式兩次。首先，將前n-1個數字從起始柱子start移動到暫存柱子temp上，遞迴調用：hanoi(n-1, start, finish, temp);。然後，將起始柱子start上剩下的最後一個數字直接移動到目標柱子finish上，執行操作：將最上方的一個數字移動到目標柱子上，從原柱子上刪除該數字，打印出目前柱子狀態，並將步驟數減一。最後，遞迴調用hanoi()函式，將之前暫存的n-1個數字從暫存柱子temp移動到目標柱子finish上。
// 7.main()函式是程式的入口。在主函式中，首先讀取問題的數字總數n和限制的步驟數m，並進行判斷。然後，使用一個while循環處理多個問題。在每個問題中，清空三個柱子的狀態，然後將數字由大到小放入起始柱子A中。接著打印出初始柱子的狀態，並執行河內塔演算法。
// 8.整個程式在執行過程中，會根據河內塔演算法的邏輯逐步移動數字，並在每次移動後打印出目前柱子的狀態，直到達到步驟數限制或完成所有問題的處理。

// 總結來說，這段程式碼使用遞迴的方式實現了河內塔問題的解決。它遵循河內塔算法的邏輯，根據數字的數量和移動規則進行遞迴操作，並在每次移動後打印出柱子的狀態，直到達到步驟數限制或完成所有問題的處理。