#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main(){
	string s;
	getline(cin,s);
	// s="bearb";
	int length=s.length();
	vector<int> pos;
	for(int i=0;i<=length-4;i++){
		// cout<<i<<endl;
		if(s[i]=='b' && s[i+1]=='e' && s[i+2]=='a'&& s[i+3]=='r')pos.push_back(i);
	}
	vector<int>::iterator it;
	int count=0;
	for(it=pos.begin();it!=pos.end();it++){
		int tmp=*it;tmp++;
		int x=tmp-1,y=tmp+3;
		y=length-y;
		if(x==0 || y==0)count+=x+y;
		else count+=((x*y)+x+y);
	}
	cout<<count;
}