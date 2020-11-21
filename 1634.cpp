#include<bits/stdc++.h>
using namespace std;

#define l long
#define ll long long
#define au auto
#define REP(i, a, n, inc) for(au i=a; i<n; i+=inc)
#define MAX 1e9


int main(){
    l n, cap, temp;
    cin >> n >> cap;
    l weights[n];
    REP(i, 0, n, 1) cin >> weights[i];
    
    ll dp[cap+1];
    dp[0] = 0;
    REP(i, 1, cap+1, 1){
        dp[i] = -1;
        temp = MAX;
        REP(j, 0, n, 1){
            temp = (dp[i-weights[j]]+1) < temp? dp[i-weights[j]]+1:temp;
        }
        if(temp != MAX) dp[i] = temp;
    }
    cout << dp[cap] << endl;

    return 0;
}


