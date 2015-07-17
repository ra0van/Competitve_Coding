#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(long n){
  if (n < 2) return false;
  for(long i=2; i<= sqrt(n); i++) {
    if ((n%i) == 0) return false;
  }
  return true;
}

int main(){
	long n,m;
	cin>>n;
	long a[n];
	for(long i=0;i<n;i++)cin>>a[i];

	cin>>m;
	long l,r;
	while(m--){
		cin>>l>>r;
		long count=0;
		if(l==2){
			for(long j=0;j<n;j++){
				if(a[j]%2==0)count++;
			}
		}
		l++;
		if(l%2==0 && l!=2){
			for(long i=l+1;i<=r;i+2){
				if(isPrime(i)){
					for(long j=0;j<n;j++){
						if(a[j]%i==0)count++;
					}
				}
			}
		}
		else if(l%2==1){
			for(long i=l;i<=r;i+2){
				if(isPrime(i)){
					for(long j=0;j<n;j++){
						if(a[j]%i==0)count++;
					}
				}
			}
		}
		cout<<count<<endl;
	}
}