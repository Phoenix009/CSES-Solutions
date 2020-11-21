#include<bits/stdc++.h>
using namespace std;

#define l long
#define ll long long
#define au auto
#define REP(i, a, n, inc) for(au i=a; i<n; i+=inc)

int main(){
    l n, cap;
    cin >> n >> cap;
    l weights[n], values[n];
    REP(i, 0, n, 1) cin >> weights[i];
    REP(i, 0, n, 1) cin >> values[i];

    ll dp[cap+1][n+1];
    REP(i, 0, n+1, 1) dp[i][0] = 0;
    REP(j, 0, cap+1, 1) dp[0][j] = 0;

    REP(i, 1, n+1, 1){
        REP(j, 1, cap+1, 1){
            dp[i][j] = dp[i-1][j];
            if(j-weights[i-1] > -1 && dp[i-1][j-weights[i-1]]+values[i-1] > dp[i][j]){
                dp[i][j] = dp[i-1][j-weights[i-1]]+values[i-1];
            }
        }
    }
    cout << dp[n][cap];

    return 0;
}


