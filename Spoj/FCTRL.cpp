#include <iostream>
#include <cmath>
using namespace std;

int z(int n){
	int count=0;
	double val = 5;
	while(val<=double(n)){
		count+=n/(int)val;
		val*=5;
	}
	return count;
}

int main(){
	int t;
	cin>>t;
	while(t--){
		long n;
		cin>>n;
		cout<<z(n)<<endl;
	}
}
