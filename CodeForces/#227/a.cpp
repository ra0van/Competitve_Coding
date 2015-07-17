#include <iostream>
using namespace std;

int main(){
	string s,t;
	getline(cin,s);
	getline(cin,t);
	int s1=0,s2=0,t1=0,t2=0;
	cout<<s<<" "<<t<<endl;
	//s1 
	int i=0;
	do{
		int tmp=(int)s[i]-48;
		cout<<tmp<<endl;
		s1*=10;
		s1+=tmp;
		i++;
	}while(s[i]==':');
	i++;
	do{
		int tmp=(int)s[i]-48;
		s2*=10;
		s2+=tmp;
		i++;
		cout<<tmp<<endl;
	}while(s[i]);

	i=0;
	do{
		int tmp=(int)t[i]-48;
		t1*=10;
		t1+=tmp;
		i++;
		cout<<tmp<<endl;
	}while(t[i]==':');
	i++;
	do{
		int tmp=(int)t[i]-48;
		t2*=10;
		t2+=tmp;
		i++;
		cout<<tmp<<endl;
	}while(t[i]);
	cout<<s1-s2<<":"<<t1-t2<<endl;

}