#include<bits/stdc++.h>
using namespace std;

#define l long
#define ll long long
#define au auto
#define REP(i, a, n, inc) for(au i=a; i<n; i+=inc)

int main(){
    l n;
    cin >> n;
    l coins[n], cap = 0;
    
    REP(i, 0, n, 1){
        cin >> coins[i];
        cap += coins[i];
    }
    
    l dp[n+1][cap+1] = {};
    REP(i, 0, n+1, 1) dp[i][0] = 1;

    REP(i, 1, n+1, 1){
        REP(j, 1, cap+1, 1){
            dp[i][j] = dp[i-1][j];
            if (j-coins[i-1] > -1) dp[i][j] |= dp[i-1][j-coins[i-1]];
        }
    }
    
    l ct = 0;
    REP(i, 1, cap+1, 1){
        if (dp[n][i]) ct += 1;
    }
    
    cout << ct << endl;
    REP(i, 1, cap+1, 1){
        if (dp[n][i]) cout << i << " ";
    }

    return 0;
}

