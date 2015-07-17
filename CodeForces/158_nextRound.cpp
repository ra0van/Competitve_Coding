#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	int n,k;
	cin>>n>>k;
	vector<int> a;
	for(int i=0;i<n;i++){
		int tmp;
		cin>>tmp;
		a.push_back(tmp);
	}
	int pos=a[k-1];
	sort(a.begin(),a.end());
	int count=0;
	for(int i=0;i<n;i++){
		if(a[i]>0 && pos<=a[i])count++;
	}
	cout<<count;
}