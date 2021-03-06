#include<bits/stdc++.h>
using namespace std;

#define l long
#define ll long long
#define au auto
#define REP(i, a, n, inc) for(au i=a; i<n; i+=inc)
#define MAX 1e9

int main(){
    l n, x;
    cin >> n >> x;
    l coins[n];
    REP(i, 0, n, 1) cin >> coins[i];

    l dp[x+1];
    dp[0] = 0;

    REP(i, 1, x+1, 1){
        dp[i] = -1;
        REP(j, 0, n, 1){
            if (i-coins[j] > -1 && dp[i-coins[j]] != -1){
                if (dp[i] == -1) dp[i] = dp[i-coins[j]] + 1;
                else dp[i] = min(dp[i], dp[i-coins[j]] + 1);
            }
        }
    }
    cout << dp[x];
    return 0;
}


