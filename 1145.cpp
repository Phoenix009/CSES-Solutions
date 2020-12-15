#include<bits/stdc++.h>
using namespace std;

#define l long
#define ll long long
#define au auto
#define REP(i, a, n, inc) for(au i=a; i<n; i+=inc)

int main(){
    l n;
    cin >> n;
    l nums[n];
    REP(i, 0, n, 1) cin >> nums[i];

    ll dp[n];
    dp[0] = 1;
    REP(i, 1, n, 1){
        dp[i] = 1;
        REP(j, 0, i, 1){
            if (nums[i] > nums[j] && dp[j]+1 > dp[i]) dp[i] = dp[j]+1;
        }
    }
    cout << dp[n-1];

    return 0;

}


