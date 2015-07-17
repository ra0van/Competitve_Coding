#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
		int a,b;
		cin>>a>>b;
		long o=1;
		while(b>0){
			if(b%2){
				o*=a;
				b--;
			}
			b/=2;
			a*=a;
			//cout<<"a:"<<a<<" o: "<<o<<endl;
			a=a%10;
			o=o%10;
			//cout<<"MOD: a:"<<a<<" o: "<<o<<endl;
		}
		cout<<o<<endl;
	}
	return 0;
}