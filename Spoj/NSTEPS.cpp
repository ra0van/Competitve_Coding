#include <iostream>
using namespace std;

const string wrongOp = "No Number";
int main(){
	int t;
	cin>>t;
	while(t--){
		int a,b;
		cin>>a>>b;
		int c=a-b;
		bool cflag = (c==2 || c==0)?true:false;
		int ap = a%2;
		int bp = b%2;
		bool pflag = (ap==bp ? true:false);
		if(cflag && pflag){
			if(ap==1){
				cout<<a+b-1<<endl;
			}
			else{
				cout<<a+b<<endl;
			}
		}
		else
			cout<<wrongOp<<endl;
	}
}