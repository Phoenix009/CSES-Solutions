#include<bits/stdc++.h>
using namespace std;

#define l long
#define ll long long
#define au auto
#define REP(i, a, n, inc) for(au i=a; i<n; i+=inc)

int main(){
    l n, cap;
    cin >> n >> cap;
    ll vals[n];
    REP(i, 0, n, 1) cin >> vals[i];
    
    ll dp[cap+1][n];
    REP(i, 0, n, 1) {
        dp[0][i] = 1;
        cout << dp[0][i];
    }
    cout << endl;

    REP(i, 0, n, 1){
        REP(j, 1, cap+1, 1){
            dp[i][j] = 0;
            if(i-1 > -1) dp[i][j] += dp[i-1][j];
            if(j-vals[i] > -1) dp[i][j] += dp[i][j-vals[i]];
            cout << dp[i][j] << " ";
        }
        cout << endl;
    }
    cout << dp[n-1][cap];
    return 0;
}


