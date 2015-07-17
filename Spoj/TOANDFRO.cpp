#include <iostream>
#include <string>
using namespace std;

string reverseString(string s){
	string tmp;
	for(int i=s.length()-1;i>=0;i--){
		tmp+=s[i];
	}
	return tmp;
}

int main(){
	while(1){
		int n;
		cin>>n;
		if(n==0)
			break;

		string s;
		cin>>s;

		int m=s.length()/n;
		string a[m];
		bool isEven=false;
		int k=0;
		for(int i=0;i<s.length();i=i+n){
			string tmp=s.substr(i,n);
			if(isEven){
				tmp = reverseString(tmp);
			}
			a[k++]=tmp;
			isEven = !isEven;
		}

		// for(int i=0;i<m;i++){
		// 	int t=i%2 ? 1 : 0;
		// 	cout<<a[i]<<" : "<<a[i][t]<<endl;
		// }
		
		for(int j=0;j<n;j++){
			for(int i=0;i<m;i++){
				//int t=i%2 ? j+1 : j;
				cout<<a[i][j];
			}
		}
		
		cout<<endl;
	}

}