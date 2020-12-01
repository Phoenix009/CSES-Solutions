#include<bits/stdc++.h>
using namespace std;

#define l long
#define ll long long
#define au auto

int main(){
    string s1, s2;
    cin >> s1 >> s2;
    l dp[s2.length() + 1][s1.length() + 1];
    l n = s1.length(), m= s2.length();

    for (au i = 0; i < n; i++) dp[i][0] = i;
    for (au j = 0; j < m; j++) dp[0][j] = j;

    for (au i=1; i<n+1; i++){
        for (au j=1; j<m+1; j++){
            if (s1[i-1] == s2[j-1]) dp[i][j] = dp[i-1][j-1];
            else dp[i][j] = min({dp[i-1][j], dp[i-1][j-1], dp[i][j-1]}) + 1;
        }
    }
    cout << dp[n][m];

    return 0;
}

