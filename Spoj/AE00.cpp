#include <iostream>

using namespace std;

int main(){
	int n;
	
	cin>>n;
	int a[n][n] = {-1};

	int l=1,b=1;
	int count=0;
	while(b*b <= n){
		for(int i=1;i*b<=n;i++){
			if((i*b <= n) && a[i-1][b-1]!=1  &&  a[b-1][i-1]!=1){
				a[i-1][b-1]=1;
				a[b-1][i-1]=1;
				count++;
			}
		}
		b++;
		l=1;
	}
	cout<<count<<endl;
}