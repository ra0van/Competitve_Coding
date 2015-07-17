#include <iostream>
using namespace std;

int main(){
	int n,c;
	cin>>n>>c;

	int a[n];
	for(int i=0;i<n;i++)cin>>a[i];

	int profit=0;
	for(int i=0;i<n-1;i++){
		int tod=a[i];
		int tom=a[i+1];
		int profit_tmp=0;
		if(tod>tom){
			profit_tmp=tod-tom-c;
			if(profit_tmp>profit)profit=profit_tmp;
		}
	}
	cout<<profit;
}