#include <bits/stdc++.h> 
#define ll long long int
using namespace std; 
void count(string str, ll &c1, ll &c0,ll n) {
	for (ll i=0;i<n;i++) {
		str[i]=='0'?c0++:c1++;
	}
}

int main() 
{ 

	ll T;
	cin>>T;
	while(T--) {
		ll n,x;
		cin>>n>>x;
		char str[100001];
		cin>>str;
		ll c1=0, c0=0;
		count(str,c1,c0,n);
		ll diff = c0 - c1;
		 
		if (diff == x ) {
			cout<<-1<<endl;
			continue;
		}
		else if (x<n && x!=0) {
			ll ans=0,c0sp=0,c1sp=0;
			for (ll i=0;i<n;i++) {
				str[i]=='0'?c0sp++:c1sp++;
				if (c0sp - c1sp == x) {
					ans++;
					//cout<<"positoive";
				}
			
			}
		cout<<ans<<endl;
			continue;
		}
		else {
			ll mul1=0;
			if (diff == 0)
				mul1 = 1;
			else
				mul1 = abs(x)/abs(diff);
			ll count1 =0,c0sp=0,c1sp=0;
			if (mul1*diff == x) {
				count1++;
			}
				//count1++;
			ll c0up = c0*mul1;
			ll c1up = c1*mul1;
			ll c1dw = c1*mul1;
			ll c0dw = c0*mul1;
			ll count1up=0,count1dw=0;
			for (ll i=0;i<n;i++) {
				str[i]=='0'?c0up++:c1up++;
				if (c0up - c1up == x) {
					count1up++;
					//cout<<"positoive";
				}
				str[n-1-i]=='0'?c0dw--:c1dw--;
				if (c0dw - c1dw == x){
					count1dw++;
					//cout<<"NEGA";
				}
				
			}
			if (diff == 0 && count1+count1up+count1dw != 0) {
				cout<<-1<<endl;
			}
			else
			cout<<count1+count1up+count1dw<<endl;
		}

		

	}
	return 0; 
} 


