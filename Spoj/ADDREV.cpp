#include <iostream>
#include <string>
using namespace std;

string setEqual(string s,int len){
	while(len--){
		s=s+'0';
	}
	return s;
}

long revAdd(string a,string b){
	int lengthOfa,lengthOfb;
	lengthOfa=a.length();
	lengthOfb=b.length();

	if(lengthOfa>lengthOfb){
		b=setEqual(b,(lengthOfa-lengthOfb));
		lengthOfb=b.length();
	}
	else if(lengthOfb>lengthOfa){
		a=setEqual(a,(lengthOfb-lengthOfa));
		lengthOfa=a.length();
	}
	//cout<<a<<" "<<b<<endl;
	long tmp=0,sum=0,carry=0;
	for(int i=0;i<lengthOfa;i++){
		tmp=0;	
		tmp+=(int)a[i]-'0';
		// cout<<"tmp: "<<tmp;
		tmp+=(int)b[i]-'0';
		// cout<<"tmp: "<<tmp;
		tmp+=carry;
		// cout<<"tmp: "<<tmp;
		sum*=10;
		sum+=tmp%10;
		// cout<<" sum:"<<sum;
		carry=tmp/10;
		// cout<<" carry:"<<carry<<endl;
	}
	if(carry!=0){
		sum*=10;
		sum+=carry;
	}
	return sum;
}

int main(){
	int t;
	cin>>t;
	while(t--){
		string a,b;
		cin>>a>>b;
		cout<<revAdd(a,b)<<endl;
	}
	return 0;
}
