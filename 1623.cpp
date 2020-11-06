#include<bits/stdc++.h>
using namespace std;
 
#define l long
#define ll long long
#define au auto
#define REP(i, a, n, s) for(au i=a; i<n; i+=s)
#define PB push_back
#define MP make_pair
#define umap unordered_map
 
ll pow(l n, l p){
	ll ans = 0, temp = n;
	while(p){
		if(p&1) ans*=temp;
		temp *= n;
		p >>= 1;
	}
	return ans;
 
}
 
int main(){
	l n, temp, j;
	cin >> n;
	l arr[n];
	REP(i, 0, n, 1) cin >> arr[i];
 
	l grp1, grp2, ans = 1e9;
	REP(i, 0, pow(2, n), 1){
		grp1 = 0; grp2 = 0;
		temp = i;
		REP(j, 0, n, 1){
			if(temp&1<<j) grp1 += arr[j];
			else grp2 += arr[j];
		}
		ans = min(ans, abs(grp1 - grp2));
	}
	cout << ans;
 
}
