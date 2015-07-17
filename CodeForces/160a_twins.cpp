#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	int n;
	cin>>n;
	vector<int> a;
	int sum=0;
	for(int i=0;i<n;i++){
		int tmp;
		cin>>tmp;
		a.push_back(tmp);
		sum+=tmp;
	}
	sort(a.begin(),a.end());
	int diff=0;
	int count=0,ptr=n-1;
	do{
		sum-=a[ptr];
		diff+=a[ptr];
		ptr--;
		count++;
	}while(diff<=sum && ptr>=0);
	cout<<count<<endl;
}