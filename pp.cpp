//一个Pigeonhole Principle的简单应用：
//给定含m个整数的序列，找出所有连续子序列使得它们的和能被m整除
#include <iostream>
using namespace std;

int main(){
    int m;
    cout << "Give the length of the sequence:";
    cin >> m;
    int n[100] = {0};
    int sum[100] = {0};

    //input
    cout << "Input the sequence:";
    for (int i = 0; i < m; ++i)
        cin >> n[i];

    //compute sum
    for (int i = 0; i < m; ++i){
        if (i == 0)
            sum[i] = n[i];
        else{
            sum[i] = sum[i-1] + n[i];
            sum[i] = sum[i]%m;
        }
    }

    //search
    for (int i = 0; i < m; ++i){
        for (int j = i+1; j < m; ++j){
            if (sum[i] == sum[j]){
                int s = 0, k;
                for (k = i+1; k < j; ++k){
                    cout << n[k] << "+";
                    s += n[k];
                }
                s += n[j];
                cout << n[j] << " = " << (s/m) << "*" << m << endl;
            }
        }
    }

    return 0;
}
