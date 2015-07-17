#include <iostream>
using namespace std;

long long cal(int n){
	long long sum =0;
	sum = n*(n+1)*((2*n)+1);
	sum /=6;
	return sum;
}

int main() {
	int n=0;
	while(1){
		cin>>n;
		if(n==0)
		 break;
		cout<<cal(n)<<endl;
	}

	return 0;
}