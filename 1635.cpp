#include<bits/stdc++.h>
using namespace std;

#define l long
#define ll long long
#define au auto
#define REP(i, a, n, inc) for(au i=a; i<n; i+=inc)
#define MOD 1000000007

int main(){
    l n, x;
    cin >> n >> x;
    l coins[n];
    REP(i, 0, n, 1) cin >> coins[i];

    l dp[x+1];
    dp[0] = 1;
    REP(i, 1, x+1, 1){
        dp[i] = 0;
        REP(j, 0, n, 1){
            if(i-coins[j] > -1) dp[i] += dp[i-coins[j]];
            dp[i] %= MOD;
        }
    }
    cout << dp[x];
    return 0;
}


