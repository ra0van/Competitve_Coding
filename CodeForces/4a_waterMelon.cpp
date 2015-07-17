#include <iostream>
using namespace std;

bool div(int w){
	if(w%2==1) return false;
	else{
		int p=w/2;
		if(p%2==0) return true;
		if(p-1==0) return false;
		else return true;
	}
}


int main(){
    int w;
    cin>>w;
    if(div(w)) cout<<"YES";
    else cout<<"NO";
}