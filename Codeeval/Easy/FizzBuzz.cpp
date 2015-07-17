#include <iostream>
#include <string>
using namespace std;

int main(){
	int a,b,c;
	cin>>a>>b>>c;
	for(int i=1;i<=c;i++){
	string s;
		if(i%a==0){
			s+="F";
		}
		if(i%b==0){
			s+="B";
		}
		if(s.length()>0){
			cout<<s<<" ";
		}
		else{
			cout<<i<<" ";
		}
	}
}